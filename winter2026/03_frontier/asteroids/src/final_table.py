"""Merge candidates with MPChecker results; write the ranked shortlist
(data/T1_shortlist.csv) and print a markdown table + MPChecker summary for README."""
import os, sys
import numpy as np, pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, '..', 'data')
reg = sys.argv[1] if len(sys.argv) > 1 else 'T1'
c = pd.read_csv(os.path.join(DATA, f'{reg}_candidates.csv'))
k = pd.read_csv(os.path.join(DATA, f'{reg}_candidate_checks.csv'))
obj = c.groupby('cand_id').agg(tier=('tier', 'first'), n_total=('n_total', 'first'),
                               nights=('night', 'nunique'), ra=('ra', 'first'), dec=('dec', 'first'),
                               t_first=('t_first', 'min'), t_last=('t_last', 'max'),
                               rate=('rate', 'mean'), pa=('pa', 'mean'), mag=('mag', 'mean'),
                               rms=('rms', 'max'), poor=('poor_orbit_known', 'first'),
                               score=('score', 'first')).reset_index()
obj = obj.merge(k[['cand_id', 'mpc_status', 'mpc_n', 'mpc_nearest', 'mpc_sep_arcsec',
                   'mpc_identified', 'mpc_possible']], on='cand_id', how='left')
obj['status'] = np.select(
    [obj.mpc_identified.notna(), obj.mpc_possible.notna() | obj.poor.notna(), obj.mpc_status.notna()],
    ['identified (MPChecker)', 'possible poor-orbit known object', 'no catalogued match'],
    'not checked with MPChecker')
obj = obj.sort_values(['tier', 'score'], ascending=[True, False])
obj.to_csv(os.path.join(DATA, f'{reg}_shortlist.csv'), index=False)
chk = obj[obj.mpc_status.notna()]
print(f'MPChecker was run on the top {len(chk)} tier-A objects: '
      f'{(chk.status == "identified (MPChecker)").sum()} identified with a catalogued object '
      f'(<= 30" and motion within 3"/h), '
      f'{(chk.status == "possible poor-orbit known object").sum()} possibly a poor-orbit catalogued object '
      f'(same motion within 2"/h inside 2\', or the SkyBoT poor-orbit flag), '
      f'{(chk.status == "no catalogued match").sum()} with no catalogued match.')
best = obj[obj.status == 'no catalogued match'].head(10)
print('\n| id | tier | nights | detections | RA, Dec (median of first-listed tracklet) | UT span | rate deg/day | PA deg | VR mag | fit rms " |')
print('|---|---|---|---|---|---|---|---|---|---|')
from astropy.time import Time
for r in best.itertuples():
    t0 = Time(r.t_first, format='mjd').iso[:16]
    t1 = Time(r.t_last, format='mjd').iso[:16]
    print(f'| {r.cand_id} | {r.tier} | {r.nights} | {r.n_total} | {r.ra:.4f}, {r.dec:+.4f} | '
          f'{t0} – {t1} | {r.rate:.3f} | {r.pa:.0f} | {r.mag:.2f} | {r.rms:.2f} |')
