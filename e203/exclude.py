"""Rigorous upper bound on the coverage achievable by ANY choice of cosets from a prime pool.

Lemma (independence).  Z^2 -> prod_{p in T} Z/e_p is onto iff for each prime ell, at most two
p in T have ell | e_p, and when two do, (alpha_p, beta_p) mod ell are linearly independent.
If {i} u J is jointly independent then |A_i \\ U_{j in J} A_j| = w_i prod_{j in J} (1 - w_j)
for every choice of cosets (w = 1/e).  Hence, for any ordering and any admissible J_i among
earlier primes:   |U A_i|  <=  sum_i  w_i prod_{j in J_i} (1 - w_j).
If the bound is < 1, no covering exists using only pool primes.
"""
import sys, json, math
from sympy import primefactors

def dirn(r, l):
    a, b = r['alpha'] % l, r['beta'] % l
    return (1, b * pow(a, -1, l) % l) if a else (0, 1)

def compatible(T, r):
    """can r join the jointly-independent set T?"""
    for l in primefactors(r['e']):
        others = [s for s in T if s['e'] % l == 0]
        if len(others) >= 2: return False
        if others and dirn(others[0], l) == dirn(r, l): return False
    return True

def bound(pool, beam=64):
    pool = sorted(pool, key=lambda r: r['e'])
    total, detail = 0.0, []
    for i, r in enumerate(pool):
        # best admissible J among earlier primes: greedy from heaviest, restarted from each seed
        best_f, best_J = 1.0, []
        earlier = pool[:i][:beam]
        for seed in range(len(earlier) + 1):
            T, f = [r], 1.0
            order = earlier[seed:seed+1] + earlier
            for s in order:
                if s in T: continue
                if compatible(T, s): T.append(s); f *= 1 - 1 / s['e']
            if f < best_f: best_f, best_J = f, [s['p'] for s in T[1:]]
        total += best_f / r['e']; detail.append((r['p'], r['e'], best_f, best_J))
    return total, detail

if __name__ == '__main__':
    for path in sys.argv[1:]:
        pool = [json.loads(l) for l in open(path)]
        U, det = bound(pool)
        print(f"{path}: primes={len(pool)} sum1/e={sum(1/r['e'] for r in pool):.4f}  "
              f"coverage <= {U:.4f}  -> {'NO COVERING POSSIBLE' if U < 1 else 'inconclusive'}")
