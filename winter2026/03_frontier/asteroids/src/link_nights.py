"""Optional step 2b: link tracklets across consecutive nights (simple, calibrated).

Each tracklet's linear fit (position and rate at its mid-time, tangent plane) is
extrapolated to the mid-time of every tracklet on the next night. The prediction
error and rate change of TRUE pairs is calibrated on known objects that have a
matched tracklet on both nights; the acceptance window is set from that
distribution, and blind linking is scored on the known pairs (completeness and
purity) before being applied to the unmatched tracklets.
usage: python link_nights.py REGION
"""
import os, sys
import numpy as np, pandas as pd
from link import gnomonic, fit
from regions import REGIONS

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, '..', 'data')


def states(tr, dd, ra0, dec0):
    rows = []
    for t, d in dd.groupby('tracklet'):
        x, y = gnomonic(d.ra.values, d.dec.values, ra0, dec0)
        tt = d.tmid.values * 24
        tm, cx, cy, _ = fit(tt, x, y, False)
        rows.append(dict(tracklet=t, tm=tm, x=cx[0], y=cy[0], vx=cx[1], vy=cy[1],
                         night=int(d.night.iloc[0]), mag=d.mag_auto.median()))
    s = pd.DataFrame(rows).merge(tr[['tracklet', 'known', 'n']], on='tracklet')
    return s


def candidates(A, B):
    """All A->B pairings with prediction error and rate change."""
    out = []
    for a in A.itertuples():
        dt = B.tm.values - a.tm
        px, py = a.x + a.vx * dt, a.y + a.vy * dt
        err = np.hypot(B.x.values - px, B.y.values - py)
        dv = np.hypot(B.vx.values - a.vx, B.vy.values - a.vy)
        for j in np.nonzero(err < 3600)[0]:
            out.append((a.tracklet, B.tracklet.values[j], err[j], dv[j],
                        abs(B.mag.values[j] - a.mag), dt[j], a.known, B.known.values[j]))
    return pd.DataFrame(out, columns=['ta', 'tb', 'err', 'dv', 'dmag', 'dt_h', 'ka', 'kb'])


def main(reg):
    R = REGIONS[reg]
    ra0 = (R['box'][0] + R['box'][1]) / 2
    dec0 = (R['box'][2] + R['box'][3]) / 2
    tr = pd.read_csv(os.path.join(DATA, f'{reg}_tracklets_classified.csv'))
    dd = pd.read_csv(os.path.join(DATA, f'{reg}_dets_classified.csv'))
    tr = tr[tr.n >= 5]
    dd = dd[dd.tracklet.isin(tr.tracklet)]
    s = states(tr, dd, ra0, dec0)
    nights = sorted(s.night.unique())
    allp = []
    for n1, n2 in zip(nights[:-1], nights[1:]):
        if n2 - n1 > 2:
            continue
        B = s[s.night == n2].copy()
        if NULL_SHIFT:
            B['x'] = B.x + NULL_SHIFT  # null test: displace night-2 tracklets
            B['known'] = None
        c = candidates(s[s.night == n1], B)
        c['n1'], c['n2'] = n1, n2
        allp.append(c)
    if not allp:
        print('no consecutive nights')
        return
    c = pd.concat(allp, ignore_index=True)
    if NULL_SHIFT:
        print(f'NULL test (night-2 shifted by {NULL_SHIFT}"):', end=' ')
        ok = c[(c.err < E_TOL) & (c.dv < V_TOL) & (c.dmag < 1.0)].copy()
        ok['score'] = ok.err / E_TOL + ok.dv / V_TOL
        b = ok.sort_values('score').drop_duplicates('ta').sort_values('score').drop_duplicates('tb')
        print('links', len(b), ' of which unknown(night1)-any', b.ka.isna().sum())
        return
    true = c[c.ka.notna() & (c.ka == c.kb)]
    print('known objects with tracklets on both nights:', true.ka.nunique())
    print('true-pair prediction error (arcsec) percentiles 50/90/99:',
          np.percentile(true.err, [50, 90, 99]).round(1),
          ' rate change ("/h):', np.percentile(true.dv, [50, 90, 99]).round(2))
    e_tol = 3 * np.percentile(true.err, 90)
    v_tol = 3 * np.percentile(true.dv, 90)
    ok = c[(c.err < e_tol) & (c.dv < v_tol) & (c.dmag < 1.0)].copy()
    # mutual best match by prediction error
    ok['score'] = ok.err / e_tol + ok.dv / v_tol
    best_a = ok.sort_values('score').drop_duplicates('ta')
    best = best_a.sort_values('score').drop_duplicates('tb')
    kk = best[best.ka.notna() & best.kb.notna()]
    print(f'windows: err < {e_tol:.1f}", dv < {v_tol:.2f}"/h; '
          f'blind links among known-known: {len(kk)}, correct {(kk.ka == kk.kb).sum()} '
          f'(completeness {(kk.ka == kk.kb).sum() / max(true.ka.nunique(), 1):.3f})')
    uu = best[best.ka.isna() & best.kb.isna()]
    mixed = best[best.ka.isna() ^ best.kb.isna()]
    print('unknown-unknown links:', len(uu), ' known-unknown links (fragments / ephemeris '
          'misses):', len(mixed))
    best.to_csv(os.path.join(DATA, f'{reg}_night_links.csv'), index=False)
    true.to_csv(os.path.join(DATA, f'{reg}_night_links_truepairs.csv'), index=False)


NULL_SHIFT = 0
E_TOL, V_TOL = None, None
if __name__ == '__main__':
    main(sys.argv[1])
    t = pd.read_csv(os.path.join(DATA, f'{sys.argv[1]}_night_links_truepairs.csv'))
    E_TOL, V_TOL = 3 * np.percentile(t.err, 90), 3 * np.percentile(t.dv, 90)
    for sh in (600, -600, 1200, -1200):
        NULL_SHIFT = sh
        main(sys.argv[1])
