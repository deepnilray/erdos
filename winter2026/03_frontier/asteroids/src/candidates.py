"""Step 4: build the ranked candidate list (unidentified moving-object tracklets).

Tiers (VERIFIED false-rate numbers are in README):
  A  : unmatched on two consecutive nights, linked (both tracklets n >= 5)
  B  : unmatched single-night tracklet with n >= 5
  C  : unmatched single-night tracklet with n == 4
Tracklets with n == 3 are NOT candidates (scrambled-data runs produce as many).
A tracklet flagged 'poor_orbit_known' (a catalogued object with a large ephemeris
uncertainty nearby with the same rate) is listed but marked.
usage: python candidates.py REGION
"""
import os, sys
import numpy as np, pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, '..', 'data')


def main(reg):
    tr = pd.read_csv(os.path.join(DATA, f'{reg}_tracklets_classified.csv'))
    dd = pd.read_csv(os.path.join(DATA, f'{reg}_dets_classified.csv'))
    lk_fn = os.path.join(DATA, f'{reg}_night_links.csv')
    links = pd.read_csv(lk_fn) if os.path.exists(lk_fn) else pd.DataFrame(columns=['ta', 'tb', 'ka', 'kb', 'err', 'dv'])
    u = tr[tr.known.isna() & (tr.n >= 4)].copy()
    uu = links[links.ka.isna() & links.kb.isna()]
    partner = dict(zip(uu.ta, uu.tb)) | dict(zip(uu.tb, uu.ta))
    lerr = dict(zip(uu.ta, uu.err)) | dict(zip(uu.tb, uu.err))
    u['linked_to'] = u.tracklet.map(partner)
    u['link_pred_err_arcsec'] = u.tracklet.map(lerr)
    u['tier'] = np.where(u.linked_to.notna(), 'A', np.where(u.n >= 5, 'B', 'C'))
    u['rms_over_err'] = u.rms / u.mederr
    # candidate id: one per object (A pairs share an id)
    ids = {}
    k = 0
    for r in u.sort_values(['tier', 'n'], ascending=[True, False]).itertuples():
        if r.tracklet in ids:
            continue
        ids[r.tracklet] = f'{reg}-C{k:04d}'
        if isinstance(r.linked_to, str):
            ids[r.linked_to] = ids[r.tracklet]
        k += 1
    u['cand_id'] = u.tracklet.map(ids)
    tot = u.groupby('cand_id').n.sum()
    u['n_total'] = u.cand_id.map(tot)
    u['score'] = u.n_total - 5 * u.rms_over_err - 10 * u.poor_orbit_known.notna()
    u = u.sort_values(['tier', 'score'], ascending=[True, False])
    cols = ['cand_id', 'tier', 'tracklet', 'night', 'n', 'n_total', 'linked_to',
            'link_pred_err_arcsec', 'ra', 'dec', 't_first', 't_last', 'span_h', 'rate', 'pa',
            'vx', 'vy', 'mag', 'filt', 'magrms', 'rms', 'mederr', 'rms_over_err',
            'poor_orbit_known', 'kcand', 'ksep', 'kerr', 'score']
    u[cols].to_csv(os.path.join(DATA, f'{reg}_candidates.csv'), index=False)
    det = dd[dd.tracklet.isin(u.tracklet)].merge(u[['tracklet', 'cand_id', 'tier']], on='tracklet')
    det = det[['cand_id', 'tier', 'tracklet', 'measid', 'exposure', 'ccdnum', 'filter', 'mjd',
               'tmid', 'ra', 'dec', 'raerr', 'decerr', 'mag_auto', 'magerr_auto', 'fwhm',
               'class_star', 'flags']]
    det.to_csv(os.path.join(DATA, f'{reg}_candidate_detections.csv'), index=False)
    print(reg, 'tracklets: A', (u.tier == 'A').sum(), 'B', (u.tier == 'B').sum(), 'C',
          (u.tier == 'C').sum(), '| objects:', u.cand_id.nunique(),
          '| A objects', u[u.tier == 'A'].cand_id.nunique(),
          '| poor-orbit flagged', u.poor_orbit_known.notna().sum())


if __name__ == '__main__':
    main(sys.argv[1])
