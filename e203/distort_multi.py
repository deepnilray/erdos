"""Multi-start optimisation of the distortion bound: joint grid over (delta_2, delta_3, delta_5),
then coordinate sweeps from each of the best starts.  Any delta vector gives a valid bound."""
import sys, json, itertools, numpy as np
import distort_fast as D, distort_opt as O

def run(pool, starts=4, sweeps=6, warm=None):
    B = D.build(pool); blocks, affected = O.split(B)
    idx = B['idx']; k2, k3, k5 = idx[2], idx[3], idx[5]
    base = np.zeros(len(B['ells'])) if warm is None else warm.copy()
    trials = []
    for d2, d3, d5 in itertools.product([0, .15, .25, .3, .35, .4], [0, .2, .3, .35, .4, .45, .5], [.2, .3, .4, .5]):
        dv = base.copy(); dv[k2], dv[k3], dv[k5] = d2, d3, d5
        # sensible default for untouched stages: delta ~ 0.45
        for l in B['stage_ells']:
            if l > 5 and warm is None: dv[idx[l]] = 0.45
        trials.append((D.costs(B, dv)[0].sum(), dv))
    trials.sort(key=lambda t: t[0])
    best = None
    for U0, dv in trials[:starts]:
        L = -np.log1p(-dv)
        cost = np.array([O.stage_cost(B, blocks, s, dv, L) for s in range(B['nst'])])
        grid = np.array([0.0] + [x / 100 for x in range(1, 96)])
        for sw in range(sweeps):
            for k in [idx[l] for l in B['stage_ells']]:
                aff = affected[k]; b0 = cost[aff].sum(); bb = (0.0, dv[k])
                for g in grid:
                    old = dv[k]; dv[k] = g; L[k] = -np.log1p(-g)
                    ds = sum(O.stage_cost(B, blocks, s, dv, L) for s in aff) - b0
                    if ds < bb[0] - 1e-15: bb = (ds, g)
                    dv[k] = old; L[k] = -np.log1p(-old)
                dv[k] = bb[1]; L[k] = -np.log1p(-bb[1])
                for s in aff: cost[s] = O.stage_cost(B, blocks, s, dv, L)
        U = D.costs(B, dv)[0].sum()          # independent full recompute
        if best is None or U < best[0]: best = (U, dv.copy())
    return B, best

if __name__ == '__main__':
    pool = [json.loads(l) for l in open(sys.argv[1])]
    for E in [int(float(x)) for x in sys.argv[2].split(',')]:
        sub = [p for p in pool if p['e'] <= E]
        B, (U, dv) = run(sub)
        np.save(f'delta_E{E}.npy', dv); json.dump({str(l): float(dv[B['idx'][l]]) for l in B['ells']}, open(f'delta_E{E}.json', 'w'))
        c = D.costs(B, dv)[0]
        print(f"E={E}: {len(sub)} primes sum1/e={sum(1/p['e'] for p in sub):.4f} BOUND={U:.6f} "
              f"[st2 {c[0]:.3f} st3 {c[1]:.3f} st5 {c[2]:.3f} rest {c[3:].sum():.3f}] -> "
              f"{'NO COVERING POSSIBLE' if U < 1 else 'inconclusive'}", flush=True)
