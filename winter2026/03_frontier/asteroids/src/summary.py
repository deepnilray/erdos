"""Print every number quoted in README.md from the data files. usage: python summary.py"""
import os
import numpy as np, pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, '..', 'data')
P = lambda f: os.path.join(DATA, f)
nb = [3, 4, 5, 6, 8, 12, 20, 40, 400]

for reg in ['T1', 'T2', 'T3']:
    print(f'===== {reg}')
    e = pd.read_csv(P(f'{reg}_exposures.csv'))
    print('exposures in window:', len(e))
    raw = pd.read_csv(P(f'{reg}_tracklets.csv'))
    print('raw tracklets by n', dict(zip(['3', '4', '5', '6-7', '8-11', '12-19', '20-39', '40+'],
          pd.cut(raw.n, nb, right=False).value_counts().sort_index().values)))
    for kind in ['rotate', 'tclean']:
        rr = [P(f'{reg}_{kind}{s}_tracklets.csv') for s in (1, 2, 3)]
        rr = [pd.read_csv(f) for f in rr if os.path.exists(f)]
        if rr:
            print(f' {kind} false tracklets by n (per run):',
                  [list(pd.cut(r.n, nb, right=False).value_counts().sort_index().values) for r in rr])
    t = pd.read_csv(P(f'{reg}_tracklets_classified.csv'))
    print('merged tracklets', len(t), 'known-matched', t.known.notna().sum(),
          'unmatched', t.known.isna().sum())
    g = pd.read_csv(P(f'{reg}_control.csv'))
    for lab, s in [('all predicted on chips (>=3 exp)', g), ('sigma<10"', g[g.poserr < 10]),
                   ('sigma<10", rate>=0.05', g[(g.poserr < 10) & (g.rate >= 0.05)]),
                   ('sigma<10", rate>=0.05, V<22', g[(g.poserr < 10) & (g.rate >= 0.05) & (g.mv < 22)]),
                   ('sigma<10", rate>=0.05, V<23', g[(g.poserr < 10) & (g.rate >= 0.05) & (g.mv < 23)])]:
        print(f' control {lab}: {s.recovered.sum()}/{len(s)} = {s.recovered.mean():.3f}')
    if os.path.exists(P(f'{reg}_missed_diagnosis.csv')):
        m = pd.read_csv(P(f'{reg}_missed_diagnosis.csv'))
        m['sigma'] = np.where(m.poserr < 10, 'sigma<10"', 'sigma>=10"')
        print(' missed-object diagnosis:\n', pd.crosstab(m.reason, m.sigma))
    if os.path.exists(P(f'{reg}_candidates.csv')):
        c = pd.read_csv(P(f'{reg}_candidates.csv'))
        print(' candidate tracklets by tier', c.tier.value_counts().to_dict(),
              '| objects by tier', c.drop_duplicates('cand_id').tier.value_counts().to_dict(),
              '| poor-orbit-flagged objects',
              c[c.poor_orbit_known.notna()].cand_id.nunique())
    if os.path.exists(P(f'{reg}_candidate_checks.csv')):
        k = pd.read_csv(P(f'{reg}_candidate_checks.csv'))
        print(' MPChecker run on', len(k), 'objects; status', k.mpc_status.value_counts().to_dict(),
              '| identified', k.mpc_identified.notna().sum(),
              '| possible (motion match within 2\')', k.mpc_possible.notna().sum())
