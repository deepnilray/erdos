"""Distortion bound with EXACT first stage (ell = 2).

Stage 2: B_2 = U_{e_p = 2^k} A_p depends only on the 2-coordinate, so alpha_2 is a constant
<= alpha2max.  Taking delta_2 > alpha2max removes B_2 completely at zero cost:
    P_2(x) = u(x) 1[x not in B_2] / (1 - alpha_2).
Refined inflation (proof in DISTORTION.md):  for any A,
    P_{j-1}(A) <= prod_{i in supp A, i >= 3} (1-delta_i)^-1 * P_2(A),
    P_2(A) = u(A \\ B_2)/(1-alpha_2) <= u(A) (1 - LB(A)) / (1 - alpha2max),
    LB(A) = sum_{i forced} 1/e_i - sum_{i<j forced} 1/|(psi_i,psi_j)(L_A)|,
where i ranges over stage-2 primes and 'forced' means psi_i(L_A) = Z/e_i (then u(A cap A_i) = u(A)/e_i
exactly, whatever the offsets).  L_A = lattice of the coset A (A_p^< or A_p^< cap A_q^<).
For A not depending on coordinate 2, P_2(A) = u(A)."""
import json, math, sys, itertools
import numpy as np, scipy.sparse as sp
from sympy import factorint
import lattice as LT

def earlier_lattice(p, ell):
    """lattice of psi_p mod e'_p (e'_p = e_p without its ell-part)."""
    e = p['e']
    while e % ell == 0: e //= ell
    if e == 1: return [[1, 0], [0, 1]], e
    return LT.hnf(LT.kernel_basis(p['alpha'] % e, p['beta'] % e, e)), e

def img(p, H):          # |psi_p(L)| for lattice basis H
    return LT.image_size(p, H)

def joint_img(p, q, H):  # |(psi_p, psi_q)(L)|
    return img(p, H) * img(q, LT.intersect(p, H))

def alpha2max(st2):
    """exact max over offsets of u(U A_i) for the stage-2 primes (brute force on (Z/2^a)^2)."""
    a = max(p['e'] for p in st2); M = a
    k, l = np.meshgrid(np.arange(M), np.arange(M), indexing='ij')
    vals = [(p['alpha'] * k + p['beta'] * l) % p['e'] for p in st2]
    best = 0.0
    # translation symmetry: first prime's offset 0
    for offs in itertools.product(*[range(p['e']) for p in st2[1:]]):
        cov = vals[0] == 0
        for v, c in zip(vals[1:], offs): cov = cov | (v == c)
        best = max(best, cov.mean())
    return best

def _check_primitive(pool):
    import math
    for p in pool:  # NONPRIMITIVE forms make the bound unsound (e.g. {2x=0 mod 4} u {2x=2 mod 4} covers)
        assert math.gcd(math.gcd(p['alpha'], p['beta']), p['e']) == 1, ('non-primitive form', p)

def build(pool):
    _check_primitive(pool)
    by = {}
    for p in pool:
        f = factorint(p['e']); by.setdefault(max(f), []).append((p, f))
    st2 = [p for p, f in by.get(2, [])]
    a2 = alpha2max(st2) if st2 else 0.0
    if a2 >= 1 - 1e-12: return None          # stage 2 alone covers: no bound possible
    ells = sorted({q for p in pool for q in factorint(p['e'])} - {2})
    idx = {l: i for i, l in enumerate(ells)}
    stage_ells = [l for l in sorted(by) if l != 2]; sidx = {l: i for i, l in enumerate(stage_ells)}
    def r(H, uses2):
        if not uses2 or not st2: return 1.0
        forced = [p for p in st2 if img(p, H) == p['e']]
        LB = sum(1 / p['e'] for p in forced)
        for p, q in itertools.combinations(forced, 2): LB -= 1 / joint_img(p, q, H)
        return max(0.0, 1 - LB) / (1 - a2)
    T1, T2 = [], []; Acap = np.zeros(len(stage_ells)); nforced = [0, 0]
    for l in stage_ells:
        s = sidx[l]; lst = by[l]
        info = []
        for p, f in lst:
            H, ep = earlier_lattice(p, l)
            sup = [idx[q] for q in f if q not in (l, 2)]
            rr = r(H, 2 in f and l != 2)
            if 2 in f: nforced[1] += 1; nforced[0] += rr < 1 / (1 - a2) - 1e-12
            info.append((H, ep, sup, 2 in f))
            T1.append((s, rr / p['e'], sup)); T2.append((s, rr * l ** -f[l] / p['e'], sup))
            Acap[s] += l ** -f[l]
        for i in range(len(lst)):
            a, fa = lst[i]; Ha, ea, supa, u2a = info[i]
            for j in range(i + 1, len(lst)):
                b, fb = lst[j]; Hb, eb, supb, u2b = info[j]
                c = math.gcd(a['alpha'] * b['beta'] - a['beta'] * b['alpha'], math.gcd(a['e'], b['e']))
                while c % l == 0: c //= l
                if u2a or u2b:
                    # lattice of A_a^< cap A_b^<: intersect the two earlier lattices
                    H = Ha
                    bb = dict(b); bb['e'] = eb; bb['alpha'] %= eb; bb['beta'] %= eb
                    if eb > 1: H = LT.intersect(bb, H)
                    rr = r(H, True)
                else: rr = 1.0
                T2.append((s, 2 * rr * c / (a['e'] * b['e']), sorted(set(supa) | set(supb))))
    def mat(T):
        rows = [k for k, t in enumerate(T) for _ in t[2]]; cols = [q for t in T for q in t[2]]
        S = sp.csr_matrix((np.ones(len(rows)), (rows, cols)), shape=(len(T), len(ells)))
        return S, np.array([t[0] for t in T]), np.array([t[1] for t in T])
    B = dict(ells=ells, idx=idx, stage_ells=stage_ells, T1=mat(T1), T2=mat(T2),
             Acap=np.minimum(1.0, Acap), nst=len(stage_ells), alpha2max=a2, nforced=nforced)
    return B

if __name__ == '__main__':
    import distort_opt as O, distort_fast as D
    pool = [json.loads(l) for l in open(sys.argv[1])]
    for E in [int(float(x)) for x in sys.argv[2].split(',')]:
        sub = [p for p in pool if p['e'] <= E]
        B = build(sub)
        dv, cost = O.optimise(B, sweeps=6)
        U = D.costs(B, dv)[0].sum()
        np.save(f'delta2_E{E}.npy', dv)
        print(f"E={E}: {len(sub)} primes sum1/e={sum(1/p['e'] for p in sub):.4f}  alpha2max={B['alpha2max']:.6f} "
              f"(stage-2 cost 0)  primes with forced overlap {B['nforced'][0]}/{B['nforced'][1]}  "
              f"BOUND={U:.6f} -> {'NO COVERING POSSIBLE' if U < 1 else 'inconclusive'}", flush=True)
