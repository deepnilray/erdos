"""Vectorised 2D distortion bound (same mathematics as distort.py; see DISTORTION.md).
Every moment term t carries (stage, weight w_t, support set S_t); its inflation is
Lam_t = exp(sum_{ell' in S_t} -log(1 - delta_ell')).  m1, m2 per stage are bincounts."""
import json, math, sys
import numpy as np
import scipy.sparse as sp
from sympy import factorint

def build(pool):
    ells = sorted({max(factorint(p['e'])) for p in pool} | {q for p in pool for q in factorint(p['e'])})
    idx = {l: i for i, l in enumerate(ells)}
    by = {}
    for p in pool:
        f = factorint(p['e']); by.setdefault(max(f), []).append((p, f))
    stage_ells = sorted(by)
    sidx = {l: i for i, l in enumerate(stage_ells)}
    T1 = []; T2 = []       # (stage, weight, support-list)
    Acap = np.zeros(len(stage_ells))
    for l, lst in by.items():
        s = sidx[l]
        earl = [[idx[q] for q in f if q != l] for p, f in lst]
        for (p, f), E in zip(lst, earl):
            T1.append((s, 1 / p['e'], E))
            T2.append((s, l ** -f[l] / p['e'], E))
            Acap[s] += l ** -f[l]
        for i in range(len(lst)):
            a, fa = lst[i]
            for j in range(i + 1, len(lst)):
                b, fb = lst[j]
                c = math.gcd(a['alpha'] * b['beta'] - a['beta'] * b['alpha'], math.gcd(a['e'], b['e']))
                while c % l == 0: c //= l
                T2.append((s, 2 * c / (a['e'] * b['e']), sorted(set(earl[i]) | set(earl[j]))))
    def mat(T):
        rows = [k for k, t in enumerate(T) for _ in t[2]]; cols = [q for t in T for q in t[2]]
        S = sp.csr_matrix((np.ones(len(rows)), (rows, cols)), shape=(len(T), len(ells)))
        return S, np.array([t[0] for t in T]), np.array([t[1] for t in T])
    return dict(ells=ells, idx=idx, stage_ells=stage_ells, T1=mat(T1), T2=mat(T2),
                Acap=np.minimum(1.0, Acap), nst=len(stage_ells))

TS = np.linspace(0, 1, 801)[1:]

def costs(B, dvec):
    """dvec: delta per ell (indexed like B['ells']). Returns per-stage cost array."""
    L = -np.log1p(-dvec)
    S1, s1, w1 = B['T1']; S2, s2, w2 = B['T2']
    m1 = np.bincount(s1, w1 * np.exp(S1 @ L), minlength=B['nst'])
    m2 = np.bincount(s2, w2 * np.exp(S2 @ L), minlength=B['nst'])
    d = np.array([dvec[B['idx'][l]] for l in B['stage_ells']]); A = B['Acap']
    best = m1.copy()
    x = np.minimum(2 * d, A)
    with np.errstate(divide='ignore', invalid='ignore'):
        quad = np.where((d > 0) & (x > d), m2 * (x - d) / np.where(x > 0, x, 1.0) ** 2, np.inf)
    best = np.minimum(best, quad)
    # tangent-parabola family a x + b x^2 with b = d/t^2, a = 1 - 2d/t (t >= 2d): valid on [0, inf)
    t = TS[None, :]
    a = 1 - 2 * d[:, None] / t; b = d[:, None] / t ** 2
    val = np.where(a >= 0, a * m1[:, None] + b * m2[:, None], np.inf)
    best = np.minimum(best, val.min(axis=1))
    best = np.where(A <= d, 0.0, best)
    return best / (1 - d), m1, m2

def optimise(B, sweeps=4, grid=None, verbose=True):
    grid = np.array([0.0] + [x / 100 for x in range(1, 96)]) if grid is None else grid
    dvec = np.zeros(len(B['ells']))
    cur = costs(B, dvec)[0].sum()
    order = [B['idx'][l] for l in B['stage_ells']]
    for sw in range(sweeps):
        for k in order:
            vals = []
            for g in grid:
                dvec[k] = g; vals.append(costs(B, dvec)[0].sum())
            j = int(np.argmin(vals)); dvec[k] = grid[j]; cur = vals[j]
        if verbose: print(f'  sweep {sw}: bound {cur:.5f}', file=sys.stderr, flush=True)
    return dvec, cur

if __name__ == '__main__':
    pool = [json.loads(l) for l in open(sys.argv[1])]
    if len(sys.argv) > 2: pool = [p for p in pool if p['e'] <= int(float(sys.argv[2]))]
    B = build(pool)
    print(f"{sys.argv[1]}: {len(pool)} primes, sum1/e={sum(1/p['e'] for p in pool):.4f}, stages {B['nst']}", flush=True)
    dvec, U = optimise(B, sweeps=int(sys.argv[3]) if len(sys.argv) > 3 else 3)
    c, m1, m2 = costs(B, dvec)
    for i in range(min(8, B['nst'])):
        l = B['stage_ells'][i]
        print(f"  ell={l} delta={dvec[B['idx'][l]]:.2f} m1={m1[i]:.4f} m2={m2[i]:.4f} cost={c[i]:.4f}")
    print(f"  tail stages (ell > {B['stage_ells'][min(8,B['nst'])-1]}): cost {c[8:].sum():.4f}")
    print(f"DISTORTION BOUND = {c.sum():.5f} -> {'NO COVERING POSSIBLE' if c.sum() < 1 else 'inconclusive'}", flush=True)
    np.save(sys.argv[1] + '.delta.npy', dvec)
