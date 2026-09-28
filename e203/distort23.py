"""Distortion bound with an EXACT merged first stage {2,3}.

B_23 = U_{P+(e_p) <= 3} A_p depends only on (x_2, x_3); its density is a constant alpha_23 <= astar,
where astar = OPT(heavy {2,3}-smooth primes) + sum_{light} 1/e_p  (OPT exact, CP-SAT certified).
With delta > astar the first stage removes B_23 completely at zero cost:
   P_23(x) = u(x) 1[x not in B_23] / (1 - alpha_23),
and for later sets A (see DISTORTION.md, L4'):
   P_{<ell}(A) <= prod_{i in supp A, i >= 5} (1-delta_i)^-1 * u(A) (1 - LB(A)) / (1 - astar),
   LB(A) = sum_{i forced} 1/e_i - sum_{i<j forced} 1/|(psi_i,psi_j)(L_A)|   over HEAVY first-stage primes i.
Sets A not reading coordinates 2 or 3 have P_23(A) = u(A)."""
import json, math, sys, itertools
import numpy as np, scipy.sparse as sp
from sympy import factorint
import lattice as LT
from distort2 import earlier_lattice, img, joint_img

def build(pool, heavy_ps, astar):
    by = {}
    for p in pool:
        f = factorint(p['e']); by.setdefault(max(f), []).append((p, f))
    first = [p for l in (2, 3) for p, f in by.get(l, [])]
    heavy = [p for p in first if p['p'] in heavy_ps]
    assert len(heavy) == len(heavy_ps) and astar < 1
    ells = sorted({q for p in pool for q in factorint(p['e'])} - {2, 3})
    idx = {l: i for i, l in enumerate(ells)}
    stage_ells = [l for l in sorted(by) if l > 3]; sidx = {l: i for i, l in enumerate(stage_ells)}
    def r(H, uses):
        if not uses: return 1.0
        forced = [p for p in heavy if img(p, H) == p['e']]
        LB = sum(1 / p['e'] for p in forced)
        for p, q in itertools.combinations(forced, 2): LB -= 1 / joint_img(p, q, H)
        return max(0.0, 1 - LB) / (1 - astar)
    T1, T2 = [], []; diag_rows = []; Acap = np.zeros(len(stage_ells))
    for l in stage_ells:
        s = sidx[l]; lst = by[l]; info = []
        for p, f in lst:
            H, ep = earlier_lattice(p, l)
            sup = [idx[q] for q in f if q not in (l, 2, 3)]
            uses = (2 in f) or (3 in f)
            rr = r(H, uses); info.append((H, ep, sup, uses))
            T1.append((s, rr / p['e'], sup)); diag_rows.append(len(T2)); T2.append((s, rr * l ** -f[l] / p['e'], sup))
            Acap[s] += l ** -f[l]
        for i in range(len(lst)):
            a, fa = lst[i]; Ha, ea, supa, ua = info[i]
            for j in range(i + 1, len(lst)):
                b, fb = lst[j]; Hb, eb, supb, ub = info[j]
                c = math.gcd(a['alpha'] * b['beta'] - a['beta'] * b['alpha'], math.gcd(a['e'], b['e']))
                while c % l == 0: c //= l
                if ua or ub:
                    H = Ha
                    if eb > 1:
                        bb = dict(b); bb['e'] = eb; bb['alpha'] %= eb; bb['beta'] %= eb
                        H = LT.intersect(bb, H)
                    rr = r(H, True)
                else: rr = 1.0
                T2.append((s, 2 * rr * c / (a['e'] * b['e']), sorted(set(supa) | set(supb))))
    def mat(T):
        rows = [k for k, t in enumerate(T) for _ in t[2]]; cols = [q for t in T for q in t[2]]
        S = sp.csr_matrix((np.ones(len(rows)), (rows, cols)), shape=(len(T), len(ells)))
        return S, np.array([t[0] for t in T]), np.array([t[1] for t in T])
    return dict(ells=ells, idx=idx, stage_ells=stage_ells, T1=mat(T1), T2=mat(T2),
                Acap=np.minimum(1.0, Acap), nst=len(stage_ells), astar=astar, diag_rows=np.array(diag_rows))

if __name__ == '__main__':
    import distort_opt as O, distort_fast as D
    pool = [json.loads(l) for l in open(sys.argv[1])]
    heavy = [int(x) for x in sys.argv[3].split(',')]; opt_heavy = float(sys.argv[4])
    for E in [int(float(x)) for x in sys.argv[2].split(',')]:
        sub = [p for p in pool if p['e'] <= E]
        light = sum(1 / p['e'] for p in sub if max(factorint(p['e'])) <= 3 and p['p'] not in heavy)
        astar = opt_heavy + light
        B = build(sub, heavy, astar)
        dv, cost = O.optimise(B, sweeps=6)
        U = D.costs(B, dv)[0].sum()
        np.save(f'delta23_E{E}_a{opt_heavy:.4f}.npy', dv); np.save(f'delta23_E{E}.npy', dv)
        print(f"E={E}: {len(sub)} primes; alpha* = {opt_heavy:.6f} + light {light:.6f} = {astar:.6f}; "
              f"BOUND={U:.6f} -> {'NO COVERING POSSIBLE' if U < 1 else 'inconclusive'}", flush=True)
