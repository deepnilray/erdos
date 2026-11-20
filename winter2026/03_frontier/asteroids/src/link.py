"""Step 2: single-night tracklet finder for NSC DR2 measurements.

Algorithm (per night):
 1. Gnomonic projection about the field centre (arcsec).
 2. Drop 'stationary' detections: a detection with >=2 other-exposure detections
    within 1.0" that are >30 min away in time is a fixed source (variable star,
    galaxy fragment, artefact), not a mover at >=0.05 deg/day (7.5"/h).
 3. Seed pairs: detections in different exposures, dt in [dt_min, dt_max],
    implied rate in [rate_min, rate_max] deg/day, |dmag| < dmag_pair.
 4. Each seed pair predicts positions in every exposure within +-ext_window of
    the pair; a 3D KD-tree on (x, y, t*TSCALE) returns the nearest detection
    in that exposure within tol. Pairs are ordered by number of hits.
 5. Greedy growth: take the best unclaimed seed, iteratively add the nearest
    detection in each exposure of the night to the current fit (linear, or
    quadratic in time when span > 1.5 h, to absorb topocentric parallax
    curvature), sigma-clip, refit, until stable. Claim members.
 6. Accept a tracklet if >= min_det distinct exposures, rate in range,
    rms residual <= max(rms_floor, rms_fac * median astrometric error),
    magnitudes consistent.
Outputs data/<tag>_tracklets.csv (one row per tracklet) and
data/<tag>_tracklet_dets.csv (one row per detection).
"""
import os, sys, argparse
import numpy as np, pandas as pd
from scipy.spatial import cKDTree

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, '..', 'data')
TSCALE = 20.0  # arcsec per minute in the time axis of the KD-tree


def gnomonic(ra, dec, ra0, dec0):
    ra, dec, ra0, dec0 = map(np.radians, (ra, dec, ra0, dec0))
    cosc = np.sin(dec0) * np.sin(dec) + np.cos(dec0) * np.cos(dec) * np.cos(ra - ra0)
    x = np.cos(dec) * np.sin(ra - ra0) / cosc
    y = (np.cos(dec0) * np.sin(dec) - np.sin(dec0) * np.cos(dec) * np.cos(ra - ra0)) / cosc
    return np.degrees(x) * 3600, np.degrees(y) * 3600


def inv_gnomonic(x, y, ra0, dec0):
    x, y = np.radians(np.asarray(x) / 3600), np.radians(np.asarray(y) / 3600)
    ra0, dec0 = np.radians(ra0), np.radians(dec0)
    rho = np.hypot(x, y)
    c = np.arctan(rho)
    with np.errstate(invalid='ignore', divide='ignore'):
        dec = np.arcsin(np.cos(c) * np.sin(dec0) + np.where(rho > 0, y * np.sin(c) * np.cos(dec0) / rho, 0))
        ra = ra0 + np.arctan2(x * np.sin(c), rho * np.cos(dec0) * np.cos(c) - y * np.sin(dec0) * np.sin(c))
    return np.degrees(ra) % 360, np.degrees(dec)


def fit(t, x, y, quad):
    """Least-squares x(t), y(t); t in hours relative to mean. Returns coefs, resid."""
    tm = t.mean()
    tt = t - tm
    A = np.vstack([np.ones_like(tt), tt] + ([tt ** 2] if quad else [])).T
    cx, *_ = np.linalg.lstsq(A, x, rcond=None)
    cy, *_ = np.linalg.lstsq(A, y, rcond=None)
    r = np.hypot(x - A @ cx, y - A @ cy)
    return tm, cx, cy, r


def predict(tm, cx, cy, t):
    tt = t - tm
    px = cx[0] + cx[1] * tt + (cx[2] * tt ** 2 if len(cx) > 2 else 0)
    py = cy[0] + cy[1] * tt + (cy[2] * tt ** 2 if len(cy) > 2 else 0)
    return px, py


class Night:
    def __init__(self, d, P):
        self.d = d.reset_index(drop=True)
        self.P = P
        self.x = self.d.x.values
        self.y = self.d.y.values
        self.tmin = self.d.tmin.values
        self.mag = self.d.mag_auto.values
        self.filt = self.d['filter'].values
        self.err = np.hypot(self.d.raerr.values, self.d.decerr.values)
        self.eid = self.d.eid.values
        self.tree3 = cKDTree(np.c_[self.x, self.y, self.tmin * TSCALE])
        ue = np.unique(self.eid)
        self.exp_t = np.array([self.tmin[self.eid == e][0] for e in ue])
        self.exp_ids = ue

    def query(self, px, py, pt, tol):
        dist, idx = self.tree3.query(np.c_[px, py, pt * TSCALE], k=1,
                                     distance_upper_bound=tol)
        ok = np.isfinite(dist)
        return ok, np.where(ok, idx, -1), dist

    def seeds(self):
        P = self.P
        n = len(self.x)
        tree2 = cKDTree(np.c_[self.x, self.y])
        rmax = P.rate_max * 3600 / 24 / 60 * P.dt_max  # arcsec
        I, J = [], []
        # pair search in chunks by query_ball_point on 2D tree
        pairs = tree2.query_pairs(rmax, output_type='ndarray')
        i, j = pairs[:, 0], pairs[:, 1]
        swap = self.tmin[i] > self.tmin[j]
        i, j = np.where(swap, j, i), np.where(swap, i, j)
        dt = self.tmin[j] - self.tmin[i]
        sep = np.hypot(self.x[j] - self.x[i], self.y[j] - self.y[i])
        rate = sep / np.maximum(dt, 1e-6) * 60 * 24 / 3600  # deg/day
        ok = ((dt >= P.dt_min) & (dt <= P.dt_max) & (rate >= P.rate_min) &
              (rate <= P.rate_max) & (np.abs(self.mag[i] - self.mag[j]) < P.dmag_pair) &
              (self.filt[i] == self.filt[j]))
        return i[ok], j[ok]

    def score_seeds(self, i, j):
        """Count hits of each seed pair in exposures within ext_window."""
        P = self.P
        hits = np.zeros(len(i), int)
        vx = (self.x[j] - self.x[i]) / (self.tmin[j] - self.tmin[i])
        vy = (self.y[j] - self.y[i]) / (self.tmin[j] - self.tmin[i])
        for k, te in enumerate(self.exp_t):
            sel = ((te > self.tmin[i] - P.ext_window) & (te < self.tmin[j] + P.ext_window) &
                   (np.abs(te - self.tmin[i]) > 0.5) & (np.abs(te - self.tmin[j]) > 0.5))
            if not sel.any():
                continue
            s = np.nonzero(sel)[0]
            dtt = te - self.tmin[i[s]]
            px = self.x[i[s]] + vx[s] * dtt
            py = self.y[i[s]] + vy[s] * dtt
            # tolerance grows with extrapolation distance
            base = self.tmin[j[s]] - self.tmin[i[s]]
            lever = np.maximum(np.abs(te - self.tmin[i[s]]), np.abs(te - self.tmin[j[s]])) / base
            tol = np.minimum(P.tol0 + P.tol_lever * lever, P.tol_max)
            ok, idx, dist = self.query(px, py, np.full(len(s), te), P.tol_max)
            good = ok & (dist <= tol)
            good[good] &= np.abs(self.mag[idx[good]] - self.mag[i[s[good]]]) < P.dmag_pair
            hits[s[good]] += 1
        return hits

    def grow(self, members, claimed):
        P = self.P
        mem = np.array(sorted(set(members)))
        for it in range(12):
            t = self.tmin[mem] / 60.0
            span = t.max() - t.min()
            quad = span > 1.5 and len(mem) >= 6
            tm, cx, cy, r = fit(t, self.x[mem], self.y[mem], quad)
            rms = np.sqrt(np.mean(r ** 2)) if len(mem) > 2 else 0.0
            tol = min(max(P.tol0, 4 * rms + 0.3), P.tol_max)
            # predict in exposures within ext_window of current span (whole night ok)
            te = self.exp_t
            sel = (te / 60 > t.min() - P.ext_window / 60) & (te / 60 < t.max() + P.ext_window / 60)
            te = te[sel]
            px, py = predict(tm, cx, cy, te / 60.0)
            # growing extrapolation tolerance outside current span
            outside = np.maximum(0, np.maximum(t.min() - te / 60, te / 60 - t.max()))
            tl = np.minimum(tol + P.tol_lever * outside / max(span, 0.1), P.tol_max)
            ok, idx, dist = self.query(px, py, te, P.tol_max)
            ok &= dist <= tl
            new = idx[ok]
            new = new[~claimed[new]]
            medmag = np.median(self.mag[mem])
            new = new[np.abs(self.mag[new] - medmag) < P.dmag_track]
            cand = np.array(sorted(set(mem) | set(new)))
            # one detection per exposure: keep closest to fit
            t2 = self.tmin[cand] / 60.0
            px2, py2 = predict(tm, cx, cy, t2)
            res = np.hypot(self.x[cand] - px2, self.y[cand] - py2)
            df = pd.DataFrame(dict(c=cand, e=self.eid[cand], r=res)).sort_values('r')
            df = df.drop_duplicates('e')
            cand = np.sort(df.c.values)
            # sigma clip
            if len(cand) >= 4:
                t2 = self.tmin[cand] / 60.0
                q2 = (t2.max() - t2.min()) > 1.5 and len(cand) >= 6
                tm2, cx2, cy2, r2 = fit(t2, self.x[cand], self.y[cand], q2)
                rr = np.sqrt(np.mean(r2 ** 2))
                keep = r2 < max(3 * rr, P.clip_floor)
                cand = cand[keep]
            if set(cand) == set(mem):
                break
            mem = cand
            if len(mem) < 3:
                return None
        return mem

    def run(self):
        P = self.P
        i, j = self.seeds()
        print(f'  seed pairs {len(i)}', flush=True)
        hits = self.score_seeds(i, j)
        keep = hits >= 1
        i, j, hits = i[keep], j[keep], hits[keep]
        print(f'  seeds with >=1 hit {len(i)}', flush=True)
        order = np.argsort(-hits, kind='stable')
        claimed = np.zeros(len(self.x), bool)
        out = []
        import time
        t0 = time.time()
        for nk, k in enumerate(order):
            if nk % 20000 == 0:
                print(f'    seed {nk}/{len(order)} tracklets {len(out)} {time.time()-t0:.0f}s', flush=True)
            if hits[k] < P.min_hits:
                break
            a, b = i[k], j[k]
            if claimed[a] or claimed[b]:
                continue
            mem = self.grow([a, b], claimed)
            if mem is None or len(mem) < P.min_det:
                continue
            res = self.evaluate(mem)
            if res is None:
                continue
            claimed[mem] = True
            out.append((mem, res))
        return out

    def evaluate(self, mem):
        P = self.P
        if len(np.unique(self.eid[mem])) < P.min_det:
            return None
        t = self.tmin[mem] / 60.0
        span = t.max() - t.min()
        quad = span > 1.5 and len(mem) >= 6
        tm, cx, cy, r = fit(t, self.x[mem], self.y[mem], quad)
        rms = np.sqrt(np.mean(r ** 2))
        mederr = np.median(self.err[mem])
        if rms > max(P.rms_floor, P.rms_fac * mederr):
            return None
        rate = np.hypot(cx[1], cy[1]) / 3600 * 24  # deg/day ("/h -> deg/day)
        if not (P.rate_min <= rate <= P.rate_max):
            return None
        # magnitude consistency within the main filter
        f = self.d['filter'].values[mem]
        mags = self.mag[mem]
        main = pd.Series(f).value_counts().index[0]
        mm = mags[f == main]
        magrms = np.std(mm) if len(mm) > 1 else 0.0
        if magrms > P.magrms_max:
            return None
        pa = np.degrees(np.arctan2(cx[1], cy[1])) % 360  # east of north
        return dict(n=len(mem), nexp=len(np.unique(self.eid[mem])), span_h=span,
                    rate=rate, pa=pa, rms=rms, mederr=mederr, quad=quad,
                    mag=np.median(mm), magrms=magrms, filt=main,
                    vx=cx[1], vy=cy[1])


class Params:
    def __init__(self, **kw):
        self.dt_min = 6.0       # min
        self.dt_max = 30.0      # min
        self.rate_min = 0.05    # deg/day
        self.rate_max = 2.0
        self.dmag_pair = 1.0
        self.dmag_track = 1.2
        self.ext_window = 40.0  # min
        self.tol0 = 1.0         # arcsec
        self.tol_lever = 0.6    # arcsec per unit lever arm
        self.tol_max = 4.0
        self.clip_floor = 0.6
        self.min_det = 3
        self.rms_floor = 0.35   # arcsec
        self.rms_fac = 3.0
        self.magrms_max = 0.5
        self.min_hits = 1
        self.__dict__.update(kw)


def prepare(meas, exps, ra0, dec0):
    m = meas.merge(exps[['exposure', 'exptime', 'fwhm']].rename(columns={'fwhm': 'exp_fwhm'}),
                   on='exposure', how='left')
    m['exptime'] = m.exptime.fillna(90)
    # detection quality: drop SExtractor-deblended fragments (flag bit 2), saturated /
    # truncated (bits 4+), and sources much broader or sharper than the exposure PSF.
    # Without this, deblended fragments around bright stars and galaxies form
    # spatially clustered false 3-point tracklets (found in T3).
    ef = m.exp_fwhm.fillna(m.exp_fwhm.median())
    m = m[((m['flags'] & ~1) == 0) & (m.fwhm < 2.0 * ef) & (m.fwhm > 0.5 * ef)].copy()
    m['tmid'] = m.mjd + m.exptime / 2 / 86400.0
    m['night'] = np.floor(m.mjd - 0.6).astype(int)
    m['x'], m['y'] = gnomonic(m.ra.values, m.dec.values, ra0, dec0)
    m = m[(m['flags'] < 4) & (m.mag_auto < 30) & (m.mag_auto > 10)].copy()
    m['eid'] = pd.factorize(m.exposure)[0]
    return m


def drop_stationary(n):
    """Flag detections with repeated detections at the same place far apart in time."""
    tree = cKDTree(np.c_[n.x.values, n.y.values])
    pairs = tree.query_pairs(1.0, output_type='ndarray')
    t = n.tmid.values * 1440
    far = np.abs(t[pairs[:, 0]] - t[pairs[:, 1]]) > 30
    cnt = np.zeros(len(n), int)
    np.add.at(cnt, pairs[far, 0], 1)
    np.add.at(cnt, pairs[far, 1], 1)
    return cnt >= 2


def run_region(tag, meas, exps, ra0, dec0, P, scramble=None, seed=0, exclude=None):
    m = prepare(meas, exps, ra0, dec0)
    if exclude is not None:
        m = m[~m.measid.isin(exclude)].copy()
    rows, dets = [], []
    tid = 0
    rng = np.random.default_rng(seed)
    for night, n in m.groupby('night'):
        n = n.copy()
        if scramble == 'times':
            # permute exposure mid-times among exposures of the night
            ue = n.exposure.unique()
            tt = n.groupby('exposure').tmid.first().loc[ue].values
            mp = dict(zip(ue, rng.permutation(tt)))
            n['tmid'] = n.exposure.map(mp)
        st = drop_stationary(n)
        n = n[~st].copy()
        if scramble == 'rotate':
            # rotate each exposure's detections by a random angle about the field
            # centre: keeps density and per-exposure structure, destroys motion.
            for e, idx in n.groupby('exposure').groups.items():
                th = rng.uniform(0, 2 * np.pi)
                x, y = n.loc[idx, 'x'].values, n.loc[idx, 'y'].values
                n.loc[idx, 'x'] = x * np.cos(th) - y * np.sin(th)
                n.loc[idx, 'y'] = x * np.sin(th) + y * np.cos(th)
        t0 = np.floor(n.tmid.min() * 1440) / 1440
        n['tmin'] = (n.tmid - t0) * 1440.0
        print(f'night {night}: {len(n)} detections after removing {st.sum()} stationary, '
              f'{n.exposure.nunique()} exposures', flush=True)
        if len(n) < 10:
            continue
        N = Night(n, P)
        for mem, res in N.run():
            d = N.d.iloc[mem].copy()
            d['tracklet'] = f'{tag}_{night}_{tid:05d}'
            res.update(tracklet=f'{tag}_{night}_{tid:05d}', night=night,
                       ra=np.median(d.ra), dec=np.median(d.dec),
                       t_first=d.tmid.min(), t_last=d.tmid.max())
            rows.append(res)
            dets.append(d)
            tid += 1
        print(f'  tracklets so far {tid}', flush=True)
    tr = pd.DataFrame(rows)
    dd = pd.concat(dets, ignore_index=True) if dets else pd.DataFrame()
    return tr, dd


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('region')
    ap.add_argument('--scramble', default=None)
    ap.add_argument('--seed', type=int, default=0)
    ap.add_argument('--tag', default=None)
    ap.add_argument('--exclude', default=None, help='CSV with a measid column to remove')
    a = ap.parse_args()
    meas = pd.read_parquet(os.path.join(DATA, f'{a.region}_meas.parquet'))
    exps = pd.read_csv(os.path.join(DATA, f'{a.region}_exposures.csv'))
    from regions import REGIONS
    R = REGIONS[a.region]
    ra0 = (R['box'][0] + R['box'][1]) / 2
    dec0 = (R['box'][2] + R['box'][3]) / 2
    tag = a.tag or (a.region + ('' if not a.scramble else f'_{a.scramble}{a.seed}'))
    P = Params(**R.get('params', {}))
    exc = set(pd.read_csv(a.exclude).measid) if a.exclude else None
    tr, dd = run_region(tag, meas, exps, ra0, dec0, P, a.scramble, a.seed, exc)
    tr.to_csv(os.path.join(DATA, f'{tag}_tracklets.csv'), index=False)
    dd.to_csv(os.path.join(DATA, f'{tag}_tracklet_dets.csv'), index=False)
    print('DONE', len(tr), 'tracklets')
