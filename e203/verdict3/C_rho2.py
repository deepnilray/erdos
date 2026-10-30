"""C_rho2.py -- sharpened per-prime cost for Theorem Z (C_allE.md sec 3d).
A new prime p (e_p = e > E0) has a single coset of Lambda_p; Z^2/Lambda_p is cyclic of order e, so the image of Lambda_p in (Z/144)^2
has CYCLIC quotient of order gcd(e,144).  Its coupled price is therefore at most
   r(e) := max{ R(type) : type in coupled_full_E200000.txt, gcd(a,c,d)=1 (cyclic quotient), a*d = gcd(e,144) }   (r=1 if gcd(e,6)=1),
instead of RMAX = 2.6145 (attained only by NON-cyclic types).  rho(e) = r(e) prod_{q|e,q>=5} g_q / e.  Same DFS/large-prime bound as C_size.py.
usage: python3 verdict3/C_rho2.py DELTA_JSON B'   (DELTA_JSON: {ell: delta}, e.g. verdict3/V_delta_cap028.json)"""
import sys, json, math, sympy
from math import gcd
E0 = 800000; LIM = 64 * E0; OPT = 0.578318; LAM0 = 0.04850936
RT = {1: 1.0}
for l in open('coupled_full_E200000.txt'):
    k, R = l.split()[:2]; a, c, d = map(int, k.split(','))
    if gcd(gcd(a, c), d) == 1: RT[a * d] = max(RT.get(a * d, 0.0), float(R))
assert len(RT) == 15 and all(144 % n == 0 for n in RT)
CORR = 1.0000251                                  # table prices use lambda = 0.0485; light mass at 8e5 is 0.04850936 (V_check.md)
RT = {k: (v * CORR if k > 1 else v) for k, v in RT.items()}
RMX = max(RT.values()); print('cyclic-type price table r(gcd(e,144)):', {k: round(v, 4) for k, v in sorted(RT.items())}, ' max %.6f' % RMX)
dl = {int(k): float(v) for k, v in json.load(open(sys.argv[1])).items()}; B1 = float(sys.argv[2])
def g(q): return 1.0 if q in (2, 3) or q not in dl else 1.0 / (1.0 - dl[q])
def r_of(e): return RT[gcd(e, 144)]
qs = list(sympy.primerange(5, 401)); allp = [2, 3] + qs
gmax_big = max([g(q) for q in dl if q > 400] + [1.0])
best = [0.0, None]
def dfs(i, m, prod):
    if m > E0:
        v = r_of(m) * prod / m
        if v > best[0]: best[0] = v; best[1] = m
        return
    for j in range(i, len(allp)):
        q = allp[j]; mm = m; first = True; pp = prod
        while True:
            mm *= q
            if mm > LIM: break
            if first and q >= 5: pp *= g(q)
            first = False
            dfs(j + 1, mm, pp)
            if mm > E0: break
dfs(0, 1, 1.0)
best2 = [0.0]
def dfs2(i, m, prod):
    for w in (1, 2, 3, 4): best2[0] = max(best2[0], r_of(m) * prod * gmax_big ** w / max(m * 401 ** w, E0 + 1))
    for j in range(i, len(allp)):
        mm = m * allp[j]
        if mm <= E0: dfs2(j + 1, mm, prod * (g(allp[j]) if allp[j] >= 5 else 1.0))
dfs2(0, 1, 1.0)
c = max(best[0], best2[0], RMX * (gmax_big / 401) ** 5, RMX * 16 / LIM)
print('smooth max rho %.4e at e=%d (gcd(e,144)=%d) ; large-prime bound %.4e ; c = %.4e' % (best[0], best[1], gcd(best[1], 144), best2[0], c))
ok = lambda N: (1 - OPT - LAM0) / (1 - OPT - LAM0 - N / E0) * B1 + N * c >= 1
lo = 0
while not ok(lo + 1): lo += 1
print("B'=%.6f -> coverings need |P_>| >= %d primes with e_p > %d" % (B1, lo + 1, E0))
