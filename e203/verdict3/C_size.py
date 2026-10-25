"""C_size.py -- unconditional lower bound on the NUMBER of primes in any covering certificate.
Method (C_allE.md sec 3): P covering, P_> = {p in P: e_p > E0}.  With the delta-vector of the E0-run (capped at CAP) and the pool bound B' for the
whole pool {e_p<=E0}:   1 <= s*B' + sum_{p in P_>} r_p prod_{q|e_p,q>=5} g_q / e_p ,   g_q = 1/(1-delta_q),  delta_q=0 for q not in the run,
s = (1-OPT-lam0)/(1-OPT-lam0-|P_>|/E0)  (light-mass correction for 3-smooth tail primes).
usage: python3 C_size.py CAP
"""
import sys, pickle, math, numpy as np
sys.path.insert(0, '.')
import distort_fast as D
CAP = float(sys.argv[1]) if len(sys.argv) > 1 else 0.5
E0 = 800000; OPT = 0.578318; LAM0 = 0.04850936; RMAX = 2.614450284594
z = np.load('verdict3/stages_E800000.npz'); ells = [int(x) for x in z['ells']]; dv0 = z['dv'].copy()
Bp = pickle.load(open('verdict3/B_E800000.pkl', 'rb'))
assert [int(x) for x in Bp['ells']] == ells
chk = D.costs(Bp, dv0)[0].sum(); print('uncapped reproduces B(8e5) = %.6f' % chk)
dv = np.minimum(dv0, CAP)
B1 = D.costs(Bp, dv)[0].sum(); print('CAP=%.2f  B\' = %.6f' % (CAP, B1))
idx = {l: i for i, l in enumerate(ells)}
def g(q): return 1.0 if q in (2, 3) or q not in idx else 1.0 / (1.0 - dv[idx[q]])
qs = [q for q in ells if q <= 400 and q >= 5]
gmax_big = max([g(q) for q in ells if q > 400] + [1.0])
print('max g(q) over q>400: %.3f ; g(5..) = %s' % (gmax_big, [round(g(q), 2) for q in qs[:8]]))
# exact max over e in (E0, 64*E0] of  rho(e) = r(e) * prod g_q / e  : DFS over 400-smooth e, plus e = m*Q with Q > 400 prime
LIM = 64 * E0
best = [0.0, None]
def r_of(e): return RMAX if (e % 2 == 0 or e % 3 == 0) else 1.0
allp = [2, 3] + qs
def dfs(i, m, prod):
    # m = current product, prod = prod of g over primes >= 5 used
    if m > E0:
        val = r_of(m) * prod / m
        if val > best[0]: best[0] = val; best[1] = m
    if m > E0:       # multiplying further only lowers the ratio (h(q^a) < 1)
        return
    for j in range(i, len(allp)):
        q = allp[j]; mm = m; pp = prod; first = True
        while True:
            mm *= q
            if mm > LIM: break
            if first and q >= 5: pp *= g(q)
            first = False
            dfs(j + 1, mm, pp)
            if mm > E0: break
dfs(0, 1, 1.0)
print('smooth part: max rho = %.4e at e = %d' % (best[0], best[1]))
# e = m * Q, Q prime > 400, m smooth with m <= E0 (m*Q > E0): rho <= r * prod(m) * gmax_big / e, and e > E0
best2 = 0.0
def dfs2(i, m, prod):
    global best2
    # smallest admissible e = m * Q with Q > max(400, E0/m); bound: e >= max(401*m, E0)
    e_lb = max(401 * m, E0 + 1)
    val = RMAX * prod * gmax_big / e_lb
    best2 = max(best2, val)
    for j in range(i, len(allp)):
        q = allp[j]; mm = m * q
        if mm > E0: continue
        dfs2(j + 1, mm, prod * (g(q) if q >= 5 else 1.0))
dfs2(0, 1, 1.0)
c = max(best[0], best2, RMAX * 2.0 ** 4 / LIM)   # last: e>64E0 (rigorous, see C_allE.md)
print('large-prime part bound: %.4e ;  c = %.4e' % (best2, c))
# solve for the smallest N=|P_>| allowed:  1 <= s(N) B' + N c
def ok(N):
    s = (1 - OPT - LAM0) / (1 - OPT - LAM0 - N / E0)
    return s * B1 + N * c >= 1.0
lo = 0
while not ok(lo + 1) and lo < 10 ** 7: lo += 1 if lo < 10 ** 5 else 1000
print('coverings need |P_>| >= %d primes with e_p > %d (hence |P| >= that)' % (lo + 1, E0))
