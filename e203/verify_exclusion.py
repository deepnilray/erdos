"""Independent verifier for:  THEOREM(N).  No finite set of primes P with lcm_{p in P} e_p | N
yields a covering, i.e. for every integer m there are k,l >= 0 with p not dividing 2^k 3^l m + 1
for all p in P.   (e_p = |<2,3> mod p|.)

Shares no code with the search.  Steps:
 1. G = gcd(2^N-1, 3^N-1); every prime with e_p | N divides G.  Candidate primes (d+1 prime,
    d | N, and 1+t*e for e | N, t <= T) are divided out; the pool is complete iff cofactor == 1.
 2. For each pool prime and each ell | e_p, the kernel line of psi_p mod ell is found WITHOUT
    discrete logs:  (x,y) in F_ell^2 lies on it iff (2^x 3^y)^(e_p/ell) == 1 (mod p).
 3. Bound (exact rationals):  core C = {5,7,11,13,17,19} contributes OPT_C = 4915/8640
    (exhaustive enumeration, brute_core.c); 23 (e=11, the only core-adjacent prime with 11 | e)
    is folded exactly: OPT <- OPT + (1-OPT)/11.  Every other prime i (in increasing e) adds
    w_i prod_{j in J_i}(1-w_j) with J_i earlier and {i} u J_i jointly independent:
    for every ell, at most two members with ell | e, and then with distinct kernel lines.
"""
import sys, math, gmpy2
from fractions import Fraction
from sympy import divisors, isprime
from sympy.ntheory import n_order

def pool(N, T=2000):
    M = (gmpy2.mpz(1) << N) - 1
    R = gmpy2.gcd(M, gmpy2.powmod(3, N, M) - 1); del M
    P = set()
    def strip(p):
        nonlocal R
        if R % p == 0:
            P.add(p)
            while R % p == 0: R //= p
    ds = divisors(N)
    for d in ds:
        if d + 1 > 3 and isprime(d + 1): strip(d + 1)
    for e in ds:
        if R == 1: break
        for t in range(1, T + 1):
            if R % (1 + t * e) == 0 and isprime(1 + t * e): strip(1 + t * e)
    assert R == 1, 'pool not certified complete'
    return sorted(P)

def kernel_line(p, e, l):
    """canonical generator of {(x,y) mod l : (2^x 3^y)^(e/l) == 1 mod p} (a line through 0)."""
    f = e // l
    pts = [(x, y) for x in range(l) for y in range(l) if (x, y) != (0, 0)
           and pow(pow(2, x, p) * pow(3, y, p) % p, f, p) == 1]
    assert len(pts) == l - 1, (p, e, l, len(pts))     # exactly a line
    x, y = min(pts)
    inv = pow(x, -1, l) if x else pow(y, -1, l)
    return (x * inv % l, y * inv % l)

def main(N):
    ps = pool(N)
    info = {}
    for p in ps:
        e = math.lcm(int(n_order(2, p)), int(n_order(3, p))); assert N % e == 0
        lines = {l: kernel_line(p, e, l) for l in sorted(set(int(q) for q in __import__('sympy').primefactors(e)))}
        info[p] = (e, lines)
    def indep(T):
        for l in set(l for q in T for l in info[q][1]):
            mem = [q for q in T if l in info[q][1]]
            if len(mem) > 2 or (len(mem) == 2 and info[mem[0]][1][l] == info[mem[1]][1][l]): return False
        return True
    core, free = [5, 7, 11, 13, 17, 19], [23]
    assert all(q in info for q in core + free)
    assert indep([23, 11]) and all(11 not in info[q][1] for q in core)   # 23 independent of core
    U = Fraction(4915, 8640)
    U += (1 - U) / info[23][0]
    order = core + free + sorted((q for q in ps if q not in core + free), key=lambda q: (info[q][0], q))
    for i in range(len(core) + 1, len(order)):
        q = order[i]; earlier = sorted(order[:i], key=lambda s: (info[s][0], s))[:64]
        best = Fraction(1)
        for seed in range(len(earlier) + 1):
            T, f = [q], Fraction(1)
            for s in earlier[seed:seed+1] + earlier:
                if s not in T and indep(T + [s]): T.append(s); f *= 1 - Fraction(1, info[s][0])
            best = min(best, f)
        U += best / info[q][0]
    S = sum(Fraction(1, info[q][0]) for q in ps)
    print(f"N={N}: pool certified complete, {len(ps)} primes, sum 1/e = {float(S):.4f}; "
          f"coverage <= {float(U):.6f} (exact rational) -> {'THEOREM HOLDS' if U < 1 else 'NOT PROVED'}", flush=True)
    return U < 1

if __name__ == '__main__':
    for N in sys.argv[1:]: main(int(N))
