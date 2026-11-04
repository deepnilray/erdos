"""2D distortion bound (after Balister-Bollobas-Morris-Sahasrabudhe-Tiba), for coverings of Z^2 by
A_p = {psi_p = c_p},  psi_p : Z^2 -> Z/e_p onto,  G = prod_ell G_ell,  G_ell = (Z/ell^a)^2.

Stage ell (increasing) holds the primes p with P^+(e_p) = ell;  v_p = v_ell(e_p), e'_p = e_p / ell^v_p.
Measures P_0 = uniform, P_ell tilts coordinate ell away from B_ell = U_{stage ell} A_p with parameter
delta_ell.  If the A_p cover, then 1 = P_final(U B_ell) <= sum_ell cost_ell, where

  cost_ell = E_{P_<}[(alpha-delta)_+]/(1-delta),   alpha(x_<) = fibre density of B_ell over x_<.

Rigorous ingredients (see DISTORTION.md):
  (L1) P_<(A) <= u(A) prod_{ell' in supp A} 1/(1-delta_ell')        (only the coordinates A uses)
  (L2) alpha <= sum_{p active} ell^-v_p, capped at 1
  (L3) E[alpha]   <= m1 = sum_p Lam_p / e_p
       E[alpha^2] <= m2 = sum_p Lam_p ell^-v_p / e_p + sum_{p != q} Lam_pq c<_pq / (e_p e_q)
       c<_pq = ell-free part of gcd(alpha_p beta_q - beta_p alpha_q, e_p, e_q)
  (L4) (x-delta)_+ <= a x + b x^2 on [0, A]  =>  cost <= (a m1 + b m2)/(1-delta)
"""
import json, math, sys
from collections import defaultdict
from sympy import factorint

def load(path): return [json.loads(l) for l in open(path)]

class Stage:
    def __init__(self, ell, prs):
        self.ell = ell; self.prs = prs
        self.fac = [factorint(p['e']) for p in prs]
        self.v = [f[ell] for f in self.fac]
        self.earlier = [tuple(sorted(q for q in f if q != ell)) for f in self.fac]
        n = len(prs); self.pairs = []            # (i, j, c<_ij, primes of lcm(e'_i, e'_j))
        for i in range(n):
            for j in range(i + 1, n):
                a, b = prs[i], prs[j]
                c = math.gcd(a['alpha'] * b['beta'] - a['beta'] * b['alpha'], math.gcd(a['e'], b['e']))
                while c % ell == 0: c //= ell
                sup = tuple(sorted(set(self.earlier[i]) | set(self.earlier[j])))
                self.pairs.append((i, j, c, sup))
        self.Acap = min(1.0, sum(ell ** -v for v in self.v))

def stages_of(pool):
    by = defaultdict(list)
    for p in pool:
        f = factorint(p['e']); by[max(f)].append(p)
    return [Stage(l, by[l]) for l in sorted(by)]

def lam(sup, delta):
    x = 1.0
    for q in sup: x /= (1 - delta.get(q, 0.0))
    return x

def moments(st, delta):
    m1 = sum(lam(st.earlier[i], delta) / p['e'] for i, p in enumerate(st.prs))
    m2 = sum(lam(st.earlier[i], delta) * st.ell ** -st.v[i] / p['e'] for i, p in enumerate(st.prs))
    for i, j, c, sup in st.pairs:
        m2 += 2 * lam(sup, delta) * c / (st.prs[i]['e'] * st.prs[j]['e'])
    return m1, m2

def majorant_cost(m1, m2, d, A):
    """min over (a,b)>=0 with a x + b x^2 >= (x-d)_+ on [0,A] of a m1 + b m2  (then / (1-d)).
    Candidates: (1,0) [x >= (x-d)_+]; pure quadratic b x^2 tangent/through; and the family of
    majorants a x + b x^2 touching (x-d) at x=t and passing... solved by 1-D scan over t."""
    if d <= 0: return m1
    best = m1
    # pure quadratic: b >= max_{x in [d,A]} (x-d)/x^2  (max at x=2d if 2d<=A else at A)
    x = min(2 * d, A); best = min(best, m2 * (x - d) / x ** 2) if x > d else 0.0
    if A <= d: return 0.0
    # mixed: a x + b x^2 >= x - d for x in [d, A] and >= 0 on [0, d] (automatic for a,b>=0)
    for k in range(1, 400):
        t = d + (A - d) * k / 400          # tangent point of the parabola to the line x - d
        # a + 2 b t = 1 and a t + b t^2 = t - d  =>  b t^2 = d  =>  b = d/t^2, a = 1 - 2d/t
        b = d / t ** 2; a = 1 - 2 * d / t
        if a < 0: continue
        best = min(best, a * m1 + b * m2)
    return best

def total(stages, delta, detail=False):
    tot = 0.0; rows = []
    for st in stages:
        d = delta.get(st.ell, 0.0)
        m1, m2 = moments(st, delta)
        c = majorant_cost(m1, m2, d, st.Acap) / (1 - d)
        tot += c; rows.append((st.ell, len(st.prs), d, m1, m2, c))
    return (tot, rows) if detail else tot

def optimise(stages, iters=6):
    ells = [st.ell for st in stages]
    delta = {l: 0.0 for l in ells}
    grid = [0.0] + [x / 100 for x in range(1, 96)]
    cur = total(stages, delta)
    for it in range(iters):
        for l in ells:
            best = (cur, delta[l])
            for g in grid:
                delta[l] = g; t = total(stages, delta)
                if t < best[0]: best = (t, g)
            delta[l] = best[1]; cur = best[0]
        print(f'  sweep {it}: bound {cur:.5f}', file=sys.stderr, flush=True)
    return delta, cur

if __name__ == '__main__':
    pool = load(sys.argv[1]); Emax = int(float(sys.argv[2])) if len(sys.argv) > 2 else 10 ** 18
    pool = [p for p in pool if p['e'] <= Emax]
    stages = stages_of(pool)
    print(f'pool {sys.argv[1]} e<= {Emax}: {len(pool)} primes, sum 1/e = {sum(1/p["e"] for p in pool):.4f}, '
          f'stages {len(stages)}, pairs {sum(len(s.pairs) for s in stages)}', flush=True)
    print('undistorted (delta=0) bound = sum 1/e_p :', round(total(stages, {}), 4))
    delta, U = optimise(stages)
    tot, rows = total(stages, delta, detail=True)
    for r in rows[:12]: print('  ell=%d n=%d delta=%.2f m1=%.4f m2=%.4f cost=%.4f' % r)
    print(f'DISTORTION BOUND = {tot:.5f} -> {"NO COVERING POSSIBLE" if tot < 1 else "inconclusive"}')
    json.dump({str(k): v for k, v in delta.items()}, open('delta_best.json', 'w'))
