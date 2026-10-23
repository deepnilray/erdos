"""Run the float pipeline (distort23r logic) at one E and keep everything needed afterwards:
   delta23r_E{E}.npy / .json, stage data npz, pickled build B (for re-evaluating other delta vectors).
   usage (from e203/):  python3 verdict3/run_bound.py POOL.jsonl E OPT_HEAVY TAG"""
import sys, json, time, pickle
sys.path.insert(0, '.')
import numpy as np
import distort23 as D23, distort23r as DR, distort_opt as O, distort_fast as D
from sympy import factorint
pool = [json.loads(l) for l in open(sys.argv[1])]
E = int(float(sys.argv[2])); opt_heavy = float(sys.argv[3]); tag = sys.argv[4]
heavy = [5, 7, 13, 17, 19, 37, 73, 97, 577]
t0 = time.time()
sub = [p for p in pool if p['e'] <= E]
light = sum(1 / p['e'] for p in sub if max(factorint(p['e'])) <= 3 and p['p'] not in heavy)
astar = opt_heavy + light
rfun, stats = DR.make_r(tag, astar, lam_E=light)
import os
PK=f'verdict3/B_E{E}.pkl'
B = pickle.load(open(PK,'rb')) if os.path.exists(PK) else D23.build(sub, heavy, astar, r_override=rfun)
t1 = time.time()
print(f'E={E}: {len(sub)} primes, light={light:.8f}, astar={astar:.6f}, build {t1-t0:.0f}s, r-source {stats}', flush=True)
if not os.path.exists(PK): pickle.dump(B, open(PK, 'wb'), protocol=4)
dv, cost = O.optimise(B, sweeps=6)
c, m1, m2 = D.costs(B, dv); U = c.sum()
np.save(f'delta23r_E{E}.npy', dv)
json.dump({str(l): float(dv[i]) for i, l in enumerate(B['ells'])}, open(f'delta23r_E{E}.json', 'w'))
np.savez(f'verdict3/stages_E{E}.npz', ells=np.array(B['ells']), dv=dv, stage_ells=np.array(B['stage_ells']), cost=c, m1=m1, m2=m2, Acap=B['Acap'])
print(f"E={E}: BOUND={U:.6f} -> {'NO COVERING POSSIBLE' if U < 1 else 'inconclusive'}  opt {time.time()-t1:.0f}s total {time.time()-t0:.0f}s", flush=True)
