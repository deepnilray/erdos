"""Steps 3-4: merge tracklet fragments, match to SkyBoT known objects, run the
recovery control, write unknown candidates.

usage: python classify.py REGION [--tag TAG]
"""
import os, sys, argparse, json
import numpy as np, pandas as pd
from matplotlib.path import Path
from scipy.spatial import cKDTree
from link import gnomonic, fit, predict, Params
from regions import REGIONS

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, '..', 'data')


def summarize(d, P):
    t = d.tmid.values * 24.0
    x, y = d.x.values, d.y.values
    span = t.max() - t.min()
    quad = span > 1.5 and len(d) >= 6
    tm, cx, cy, r = fit(t, x, y, quad)
    rms = np.sqrt(np.mean(r ** 2))
    f = d['filter'].values
    main = pd.Series(f).value_counts().index[0]
    mm = d.mag_auto.values[f == main]
    return dict(n=len(d), nexp=d.exposure.nunique(), span_h=span,
                rate=np.hypot(cx[1], cy[1]) / 3600 * 24,
                pa=np.degrees(np.arctan2(cx[1], cy[1])) % 360, rms=rms,
                mederr=np.median(np.hypot(d.raerr, d.decerr)), quad=quad,
                mag=np.median(mm), magrms=np.std(mm) if len(mm) > 1 else 0, filt=main,
                vx=cx[1], vy=cy[1], ra=np.median(d.ra), dec=np.median(d.dec),
                t_first=d.tmid.min(), t_last=d.tmid.max())


def merge_fragments(tr, dd, P, ra0, dec0):
    """Union tracklets in the same night that are one object (consistent motion)."""
    dd = dd.copy()
    dd['x'], dd['y'] = gnomonic(dd.ra.values, dd.dec.values, ra0, dec0)
    parent = {t: t for t in tr.tracklet}

    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a
    g = {k: v for k, v in dd.groupby('tracklet')}
    nmerge = 0
    for night, tn in tr.groupby('night'):
        tn = tn.reset_index(drop=True)
        # position of each tracklet extrapolated to a common time (night mid)
        tref = tn.t_first.min() * 24 + 3
        P0 = []
        for r in tn.itertuples():
            d = g[r.tracklet]
            tm, cx, cy, _ = fit(d.tmid.values * 24, d.x.values, d.y.values, False)
            px, py = predict(tm, cx, cy, np.array([tref]))
            P0.append((px[0], py[0], cx[1], cy[1]))
        P0 = np.array(P0)
        # neighbours in (x0, y0) within 60" and similar velocity
        tree = cKDTree(P0[:, :2])
        for a, b in tree.query_pairs(120.0):
            va, vb = P0[a, 2:], P0[b, 2:]
            if np.hypot(*(va - vb)) > 0.15 * np.hypot(*va) + 2.0:
                continue
            A, B = tn.tracklet[a], tn.tracklet[b]
            if find(A) == find(B):
                continue
            da, db = g[A], g[B]
            if len(set(da.exposure) & set(db.exposure)) > 0:
                continue
            d = pd.concat([da, db])
            t = d.tmid.values * 24
            q = (t.max() - t.min()) > 1.5 and len(d) >= 6
            _, _, _, r = fit(t, d.x.values, d.y.values, q)
            rms = np.sqrt(np.mean(r ** 2))
            if rms <= max(P.rms_floor, P.rms_fac * np.median(np.hypot(d.raerr, d.decerr))) \
                    and r.max() < 1.5:
                parent[find(A)] = find(B)
                nmerge += 1
    dd['tracklet'] = dd.tracklet.map(lambda t: find(t))
    rows = []
    for t, d in dd.groupby('tracklet'):
        s = summarize(d, P)
        s.update(tracklet=t, night=int(d.night.iloc[0]))
        rows.append(s)
    print('fragment merges:', nmerge)
    return pd.DataFrame(rows), dd


def match_known(dd, sb, tr):
    """For each detection, nearest SkyBoT object in the same exposure."""
    out = []
    sbg = {k: v for k, v in sb.groupby('exposure')}
    for e, d in dd.groupby('exposure'):
        if e not in sbg:
            continue
        s = sbg[e]
        cosd = np.cos(np.radians(d.dec.values.mean()))
        tree = cKDTree(np.c_[s.ra.values * cosd, s.dec.values])
        dist, idx = tree.query(np.c_[d.ra.values * cosd, d.dec.values], k=1,
                               distance_upper_bound=60 / 3600)
        ok = np.isfinite(dist)
        for i in np.nonzero(ok)[0]:
            k = s.iloc[idx[i]]
            out.append(dict(measid=d.measid.iloc[i], sep=dist[i] * 3600,
                            kname=k['name'], knum=k['num'], kmv=k.mv, kerr=k.poserr,
                            kcls=k.cls, kdra=k.dra, kddec=k.ddec))
    mk = pd.DataFrame(out)
    m = dd.merge(mk, on='measid', how='left')
    # tracklet -> known object: >=50% of dets within tolerance of the same object
    res = []
    for t, d in m.groupby('tracklet'):
        tol = np.minimum(np.maximum(3.0, 3 * d.kerr.fillna(0)), 60.0)
        good = d[d.sep <= tol]
        if len(good) == 0:
            res.append(dict(tracklet=t, known=None, kfrac=0, ksep=np.nan))
            continue
        vc = good.kname.value_counts()
        name = vc.index[0]
        frac = vc.iloc[0] / len(d)
        gg = good[good.kname == name]
        res.append(dict(tracklet=t, known=name if frac >= 0.5 else None, kfrac=frac,
                        ksep=gg.sep.median(), kmv=gg.kmv.iloc[0], kerr=gg.kerr.iloc[0],
                        kcls=gg.kcls.iloc[0], kdra=gg.kdra.iloc[0], kddec=gg.kddec.iloc[0],
                        kcand=name))
    tr = tr.merge(pd.DataFrame(res), on='tracklet', how='left')
    # Second chance for unmatched tracklets: a catalogued object whose ephemeris
    # uncertainty is large (> 30") may lie far from its prediction. Flag a tracklet
    # 'poor_orbit_known' if such an object is within min(2*err, 300") of the
    # tracklet's mid-position at a mid-tracklet exposure AND moves at the same rate
    # (vector difference < 5% + 1.5"/h).
    poor = sb[sb.poserr > 30]
    pg = {k: v for k, v in poor.groupby('exposure')}
    flag, fname = [], []
    for r in tr.itertuples():
        hit = None
        if pd.isna(r.known):
            d = m[m.tracklet == r.tracklet]
            e = d.exposure.iloc[len(d) // 2]
            if e in pg:
                s = pg[e]
                row = d.iloc[len(d) // 2]
                c = np.cos(np.radians(row.dec))
                sep = np.hypot((s.ra - row.ra) * c, s.dec - row.dec) * 3600
                dv = np.hypot(s.dra - r.vx, s.ddec - r.vy)
                ok = (sep < np.minimum(2 * s.poserr, 300)) & (dv < 0.05 * np.hypot(r.vx, r.vy) + 1.5)
                if ok.any():
                    hit = s.name.values[np.argmin(np.where(ok, sep, np.inf))]
        fname.append(hit)
    tr['poor_orbit_known'] = fname
    return tr, m


def edge_dist(p, pts):
    v = p.vertices
    dmin = np.full(len(pts), np.inf)
    for k in range(len(v)):
        a, b = v[k], v[(k + 1) % len(v)]
        ab = b - a
        t = np.clip(((pts - a) @ ab) / (ab @ ab), 0, 1)
        q = a + t[:, None] * ab
        dmin = np.minimum(dmin, np.hypot(*(pts - q).T))
    return dmin


def chip_paths(chips, ra0, dec0):
    paths = {}
    for e, c in chips.groupby('exposure'):
        L = []
        for r in c.itertuples():
            vr = [r.vertex_ra1, r.vertex_ra2, r.vertex_ra3, r.vertex_ra4]
            vd = [r.vertex_dec1, r.vertex_dec2, r.vertex_dec3, r.vertex_dec4]
            x, y = gnomonic(np.array(vr), np.array(vd), ra0, dec0)
            # order vertices around centroid
            ang = np.arctan2(y - y.mean(), x - x.mean())
            o = np.argsort(ang)
            L.append(Path(np.c_[x[o], y[o]]))
        paths[e] = L
    return paths


CONTROL_ONCHIP = []


def control(sb, chips, exps, tr, ra0, dec0, box, edge=20.0):
    """Expected known objects: on a chip (>= edge arcsec inside) in >=3 exposures of a
    night, inside the region box. Recovered: a tracklet that night matched to it."""
    paths = chip_paths(chips, ra0, dec0)
    sb = sb.copy()
    sb['x'], sb['y'] = gnomonic(sb.ra.values, sb.dec.values, ra0, dec0)
    inbox = (sb.ra >= box[0]) & (sb.ra < box[1]) & (sb.dec >= box[2]) & (sb.dec < box[3])
    sb = sb[inbox].copy()
    on = np.zeros(len(sb), bool)
    for e, s in sb.groupby('exposure'):
        if e not in paths:
            continue
        pts = np.c_[s.x.values, s.y.values]
        inside2 = np.zeros(len(s), bool)
        for p in paths[e]:
            inside2 |= p.contains_points(pts) & (edge_dist(p, pts) > edge)
        on[sb.index.get_indexer(s.index)] = inside2
    sb['on_chip'] = on
    e2 = exps.set_index('exposure')
    sb['night'] = np.floor(e2.loc[sb.exposure, 'mjd'].values - 0.6).astype(int)
    sb['depth'] = e2.loc[sb.exposure, 'depth95'].values
    CONTROL_ONCHIP.append(sb[sb.on_chip])
    g = sb[sb.on_chip].groupby(['night', 'name']).agg(
        nexp_on=('exposure', 'nunique'), mv=('mv', 'first'), cls=('cls', 'first'),
        poserr=('poserr', 'median'), dra=('dra', 'median'), ddec=('ddec', 'median'),
        depth=('depth', 'median')).reset_index()
    g = g[g.nexp_on >= 3]
    rec = tr.dropna(subset=['known']).groupby(['night', 'known']).agg(
        ndet_rec=('n', 'sum'), ntrk=('n', 'size')).reset_index()
    g = g.merge(rec, left_on=['night', 'name'], right_on=['night', 'known'], how='left')
    g['recovered'] = g.known.notna()
    g['rate'] = np.hypot(g.dra, g.ddec) / 3600 * 24
    return g


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('region')
    ap.add_argument('--tag', default=None)
    a = ap.parse_args()
    tag = a.tag or a.region
    R = REGIONS[a.region]
    ra0 = (R['box'][0] + R['box'][1]) / 2
    dec0 = (R['box'][2] + R['box'][3]) / 2
    P = Params(**R.get('params', {}))
    tr = pd.read_csv(os.path.join(DATA, f'{tag}_tracklets.csv'))
    dd = pd.read_csv(os.path.join(DATA, f'{tag}_tracklet_dets.csv'))
    print('raw tracklets', len(tr))
    tr, dd = merge_fragments(tr, dd, P, ra0, dec0)
    print('after merge', len(tr))
    from topo import correct_df
    sb = correct_df(pd.read_parquet(os.path.join(DATA, f'{a.region}_skybot.parquet')))
    tr, m = match_known(dd, sb, tr)
    tr.to_csv(os.path.join(DATA, f'{tag}_tracklets_classified.csv'), index=False)
    m.to_csv(os.path.join(DATA, f'{tag}_dets_classified.csv'), index=False)
    print('known-matched', tr.known.notna().sum(), 'unmatched', tr.known.isna().sum())
    if tag == a.region:
        chips = pd.read_csv(os.path.join(DATA, f'{a.region}_chips.csv'))
        exps = pd.read_csv(os.path.join(DATA, f'{a.region}_exposures.csv'))
        g = control(sb, chips, exps, tr, ra0, dec0, R['box'])
        g.to_csv(os.path.join(DATA, f'{a.region}_control.csv'), index=False)
        CONTROL_ONCHIP[0].to_parquet(os.path.join(DATA, f'{a.region}_control_onchip.parquet'))
        print('expected known (night,object):', len(g), 'recovered', g.recovered.sum(),
              f'{g.recovered.mean():.3f}')
        bins = [10, 19, 20, 21, 21.5, 22, 22.5, 23, 23.5, 24, 30]
        print(g.groupby(pd.cut(g.mv, bins)).recovered.agg(['size', 'sum', 'mean']))
