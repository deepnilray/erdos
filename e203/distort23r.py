"""Merged-{2,3} distortion bound with the sharpened removal price r(A):
   r(A) = min( R_coupled(A)                       [exact coupled worst case, maxratio.c, if computed],
               (1 - minU(A)) / (1 - astar)         [exact decoupled min-coverage, minunion.c],
               (1 - LB_Bonferroni(A)) / (1 - astar) )
Each is a valid upper bound on P_23(A)/u(A) (DISTORTION.md, L4', L4''); types keyed by canonical HNF
of L_A + 144 Z^2.  R_coupled uses lambda = 0.0485 >= light-{2,3} union bound for every E <= 2e5."""
import sys, json, os
import numpy as np
import distort23 as D23, rtypes as R, distort2 as D2
LAM_MAX = 0.0485

def make_r(E_tag, astar):
    types = json.load(open(f'types_E{E_tag}.json'))
    coupled = {}
    if os.path.exists(f'coupled_full_E{E_tag}.txt'):       # key R bestA nA bestG nG  (exact certificates)
        for line in open(f'coupled_full_E{E_tag}.txt'):
            k, v = line.split()[:2]; coupled[k] = float(v)
    stats = dict(coupled=0, minU=0, bonf=0)
    def r(H, uses, bonf_value):
        if not uses: return 1.0
        k = '%d,%d,%d' % R.canon(H)
        cands = [bonf_value]
        if k in types: cands.append((1 - types[k]['minU']) / (1 - astar))
        if k in coupled: cands.append(coupled[k])
        v = min(cands); stats[['bonf', 'minU', 'coupled'][cands.index(v)] if len(cands) > 1 else 'bonf'] += 1
        return v
    return r, stats

if __name__ == '__main__':
    import distort_opt as O, distort_fast as D
    from sympy import factorint
    pool = [json.loads(l) for l in open(sys.argv[1])]
    heavy = [5, 7, 13, 17, 19, 37, 73, 97, 577]; opt_heavy = float(sys.argv[3]); tag = sys.argv[4]
    for E in [int(float(x)) for x in sys.argv[2].split(',')]:
        sub = [p for p in pool if p['e'] <= E]
        light = sum(1 / p['e'] for p in sub if max(factorint(p['e'])) <= 3 and p['p'] not in heavy)
        assert light <= LAM_MAX
        astar = opt_heavy + light
        rfun, stats = make_r(tag, astar)
        # patch distort23's r: wrap the Bonferroni computation
        orig_build = D23.build
        B = D23.build(sub, heavy, astar, r_override=rfun)
        dv, cost = O.optimise(B, sweeps=6)
        U = D.costs(B, dv)[0].sum()
        np.save(f'delta23r_E{E}.npy', dv)
        print(f"E={E}: BOUND={U:.6f} -> {'NO COVERING POSSIBLE' if U < 1 else 'inconclusive'}   r-source counts {stats}", flush=True)
