"""Same computation as distort23r.py __main__ (copied logic), plus per-stage dumps. Run from scratch dir."""
import sys, json, time
import numpy as np
sys.path.insert(0, '/home/user/erdos/e203')
import distort23 as D23, distort23r as DR, distort_opt as O, distort_fast as D
from sympy import factorint
pool = [json.loads(l) for l in open(sys.argv[1])]
heavy = [5, 7, 13, 17, 19, 37, 73, 97, 577]; opt_heavy = float(sys.argv[3]); tag = sys.argv[4]
sweeps = int(sys.argv[5]) if len(sys.argv) > 5 else 6
for E in [int(float(x)) for x in sys.argv[2].split(',')]:
    t0 = time.time()
    sub = [p for p in pool if p['e'] <= E]
    light = sum(1 / p['e'] for p in sub if max(factorint(p['e'])) <= 3 and p['p'] not in heavy)
    astar = opt_heavy + light
    rfun, stats = DR.make_r(tag, astar, lam_E=light)
    B = D23.build(sub, heavy, astar, r_override=rfun)
    t1 = time.time()
    dv, cost = O.optimise(B, sweeps=sweeps)
    c, m1, m2 = D.costs(B, dv)
    U = c.sum()
    d = np.array([dv[B['idx'][l]] for l in B['stage_ells']])
    # uninflated m1 (delta = 0) for reference
    c0, m10, m20 = D.costs(B, np.zeros_like(dv))
    np.savez(f'stages_E{E}.npz', ells=np.array(B['stage_ells']), cost=c, m1=m1, m2=m2, delta=d, Acap=B['Acap'],
             m1_raw=m10, m2_raw=m20, dvec=dv, all_ells=np.array(B['ells']))
    print(f"E={E}: light={light:.7f} astar={astar:.6f} BOUND={U:.6f} (incremental {cost.sum():.6f}) "
          f"{'NO COVERING POSSIBLE' if U < 1 else 'inconclusive'} r-src {stats} build {t1-t0:.0f}s opt {time.time()-t1:.0f}s", flush=True)
