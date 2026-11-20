"""Why are known objects missed? For each missed (night, object) in the control,
take up to 3 on-chip exposures and look for ANY NSC DR2 measurement within 3"
of the topocentric SkyBoT position (full meas table, no pre-selection).
Reasons: no_nsc_detection | excluded_by_object_cut (ndet>20 or deltamjd>=0.6) |
dropped_by_quality_cut | present_but_not_linked (incl. rate < 0.05 deg/day)."""
import os, sys
import numpy as np, pandas as pd
from tap import tap

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, '..', 'data')
reg = sys.argv[1]
g = pd.read_csv(os.path.join(DATA, f'{reg}_control.csv'))
on = pd.read_parquet(os.path.join(DATA, f'{reg}_control_onchip.parquet'))
mine = set(pd.read_parquet(os.path.join(DATA, f'{reg}_meas.parquet'), columns=['measid']).measid)
maxmag = float(sys.argv[2]) if len(sys.argv) > 2 else 99
miss = g[~g.recovered & (g.mv < maxmag)]
out = []
for r in miss.itertuples():
    s = on[(on.name == r.name) & (on.night == r.night)]
    s = s.iloc[np.linspace(0, len(s) - 1, min(3, len(s))).astype(int)]
    found = []
    for k in s.itertuples():
        q = f"""SELECT m.measid,m.mag_auto,m.flags,m.fwhm,o.ndet,o.deltamjd,m.ra,m.dec FROM nsc_dr2.meas m
          JOIN nsc_dr2.object o ON m.objectid=o.id WHERE m.exposure='{k.exposure}'
          AND m.ra BETWEEN {k.ra - 0.001} AND {k.ra + 0.001} AND m.dec BETWEEN {k.dec - 0.001} AND {k.dec + 0.001}"""
        try:
            d = tap(q)
        except Exception as e:
            continue
        if len(d):
            d['sep'] = np.hypot((d.ra - k.ra) * np.cos(np.radians(k.dec)), d.dec - k.dec) * 3600
            d = d[d.sep < 3]
        found.append(d.sort_values('sep').head(1) if len(d) else None)
    hits = [f for f in found if f is not None and len(f)]
    if not hits:
        why = 'no_nsc_detection'
    else:
        h = pd.concat(hits)
        if ((h.ndet > 20) | (h.deltamjd >= 0.6)).all():
            why = 'excluded_by_object_cut'
        elif not h.measid.isin(mine).any():
            why = 'excluded_by_object_cut'
        elif r.rate < 0.05:
            why = 'present_but_rate_below_0.05'
        else:
            why = 'present_but_not_linked'
    out.append(dict(night=r.night, name=r.name, mv=r.mv, rate=r.rate, nexp_on=r.nexp_on,
                    poserr=r.poserr, reason=why, n_hits=len(hits)))
    print(out[-1], flush=True)
pd.DataFrame(out).to_csv(os.path.join(DATA, f'{reg}_missed_diagnosis.csv'), index=False)
print(pd.DataFrame(out).reason.value_counts())
