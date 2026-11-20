"""Build the exclusion list for the clutter-preserving false-tracklet test.

Removes (a) detections in real tracklets with n >= 5 and (b) any detection within
5" of a SkyBoT-predicted known object in the same exposure. What remains is static
clutter, noise and faint unlinked movers; the time-scrambled run on it then
measures false tracklets while keeping the spatial structure of the clutter.
usage: python make_exclude.py REGION
"""
import os, sys
import numpy as np, pandas as pd
from scipy.spatial import cKDTree

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, '..', 'data')

reg = sys.argv[1]
tr = pd.read_csv(os.path.join(DATA, f'{reg}_tracklets.csv'))
dd = pd.read_csv(os.path.join(DATA, f'{reg}_tracklet_dets.csv'))
ex = set(dd[dd.tracklet.isin(tr.tracklet[tr.n >= 5])].measid)
m = pd.read_parquet(os.path.join(DATA, f'{reg}_meas.parquet'))
from topo import correct_df
sb = correct_df(pd.read_parquet(os.path.join(DATA, f'{reg}_skybot.parquet')))
sbg = {k: v for k, v in sb.groupby('exposure')}
for e, d in m.groupby('exposure'):
    if e not in sbg:
        continue
    s = sbg[e]
    c = np.cos(np.radians(d.dec.mean()))
    t = cKDTree(np.c_[s.ra * c, s.dec])
    dist, _ = t.query(np.c_[d.ra * c, d.dec], distance_upper_bound=5 / 3600)
    ex |= set(d.measid[np.isfinite(dist)])
pd.DataFrame({'measid': sorted(ex)}).to_csv(os.path.join(DATA, f'{reg}_exclude.csv'), index=False)
print(reg, 'excluded', len(ex))
