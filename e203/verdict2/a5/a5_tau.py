# a5_tau.py (agent 5, run5): independent rigorous bound for
#   tau_w = sum over squarefree d (all primes >= w) that are NOT 1 and NOT a single known prime (q <= Y = 1e8) of g(d)/e(d),
# g(d) = prod 1/(p-2), e(d) = [Z^2 : Lambda_d] >= lcm_{p|d} e_p.   (Used: W_w <= 1 + S1 + tau, M_w <= max B1 + tau, W_5 tail.)
# Decomposition by the two largest keys (key = (e_p, p)), as D, but own code and own UNKNOWN-PRIME bound U(y):
#   U(y) >= sum_{q > Y prime, e_q <= y} 1/(q-2), from (i) count: such primes divide prod_{t<=y}(2^t-1) < 2^{y(y+1)/2}, so there are
#   n(y) <= y(y+1)log2/(2 log Y) of them, each 1/(q-2) <= 1/(Y-1);  (ii) wheel: n distinct primes > Y are among the integers > Y prime
#   to 30030, whose i-th is >= Y+1+30030*floor((i-1)/5760); so sum <= 5760/(Y-1) + (5760/30030) log(1 + ceil(n/5760)*30030/(Y-1)).
#   No Rosser-Schoenfeld input (D used RS; I could not open RS 1962: Project Euclid blocked the download).
# Parts:  A: p1, p2 known, e1 <= E0: g1 g2 Pi(<p2) / lcm(e1,e2)            (exact pair sum, float with inflation)
#         B: p1 known, e1 <= E0, rest contains an unknown prime: g1/e1 * Pi_known(<p1) * (exp(U(e1)) - 1)
#         C: p1 known, e1 > E0: g1/e1 * (Pi_known(<p1) exp(U(e1)) - 1)
#         D: p1 unknown: sum_{q unknown} g(q)/e_q Pi_known(e <= e_q) exp(U(e_q)), Abel summation on a grid + analytic tail.
# Floating point: all terms are nonnegative; Pi_known is a cumulative product of (q-1)/(q-2) (one division, exact operands);
# with n <= 6e6 operations per chain the relative error is <= (1+2^-53)^(2n) - 1 < 2e-9; every float result is inflated by 1e-7.
import numpy as np, math, sys, pickle
from mpmath import iv
iv.dps = 30
w = int(sys.argv[1]) if len(sys.argv) > 1 else 31
E0 = int(sys.argv[2]) if len(sys.argv) > 2 else 3000
Y = 10**8; INFL = 1 + 1e-7
DD = '/home/user/erdos/e203/verdict3/D_data/'
own = np.fromfile(DD+'a5_e_1e8.bin', dtype='<u4').reshape(-1, 2)
own = own[own[:, 0] >= w]
q = own[:, 0].astype(np.int64); e = own[:, 1].astype(np.int64)
order = np.lexsort((q, e)); q = q[order]; e = e[order]
g = 1.0/(q-2)
fac = (q-1).astype(np.float64)/(q-2)
Pi_incl = np.cumprod(fac)                       # prod over keys <= this key
Pi_before = np.concatenate([[1.0], Pi_incl[:-1]])  # keys < this key
Pi_all = float(Pi_incl[-1])*INFL

LOGY = iv.log(iv.mpf(Y)); LN2 = iv.log(2)
PH, PR = 5760, 30030
def U_iv(y):
    y = iv.mpf(y)
    nmax = y*(y+1)*LN2/(2*LOGY)                       # real upper bound for the count
    b1 = nmax/(Y-1)
    nb = nmax/PH + 1                                   # >= ceil(n/5760)
    b2 = iv.mpf(PH)/(Y-1) + iv.mpf(PH)/PR*iv.log(1 + nb*PR/(Y-1))
    v1 = float(b1.b) if b1.b < 1e300 else math.inf
    return min(v1, float(b2.b))
# U on a grid (U nondecreasing in y; use U(next grid point) for any y in between)
grid = np.unique(np.concatenate([np.arange(1, 3001), np.geomspace(3000, 1e15, 6000)]).astype(np.int64)).astype(float)
grid = np.concatenate([grid, np.geomspace(1e15, 1e300, 400)[1:]])
Ug = np.array([U_iv(y) for y in grid])
assert (np.diff(Ug) >= 0).all()
def U_at(y):  # y array -> U(next grid point >= y)
    k = np.searchsorted(grid, y, side='left'); return Ug[np.minimum(k, len(grid)-1)]
Ue = U_at(e.astype(float))
# ---- A, B, C ----
smallm = e <= E0; ns = int(smallm.sum())
es = e[smallm]; gs = g[smallm]; Pb = Pi_before[smallm]*np.exp(U_at(es.astype(float)))   # Pi(<p2) incl. unknown with e<=e2
A = 0.0
for t in range(1, ns):
    l = np.lcm(es[:t], es[t])
    A += gs[t]*np.sum(gs[:t]*Pb[:t]/l)
A *= INFL
Bp = float(np.sum(gs/es*Pi_before[smallm]*np.expm1(Ue[smallm])))*INFL
big = ~smallm
Cp = float(np.sum(g[big]/e[big]*(Pi_before[big]*np.exp(Ue[big]) - 1)))*INFL
print(f"w={w} E0={E0}: known q>={w}: {len(q)}, with e<=E0: {ns}")
print(f"  A (exact pairs) = {A:.6e}  B (unknown 2nd) = {Bp:.6e}  C (crude, e1>E0) = {Cp:.6e}")
# ---- D: unknown largest key.  f(y) = Pi_known(e<=y) exp(U(y)) / y on [grid_i, grid_{i+1}) <= Pi_known(<=grid_{i+1}) e^{U(grid_{i+1})}/grid_i
k = np.searchsorted(e, grid, side='right')        # number of known keys with e <= grid
Pk = np.where(k > 0, Pi_incl[np.maximum(k-1, 0)], 1.0)*INFL
Fi = Pk[1:]*np.exp(Ug[1:])/grid[:-1]               # bound on f over [grid_i, grid_{i+1})
Ft = np.maximum.accumulate(Fi[::-1])[::-1]         # decreasing envelope
# Abel: sum_{i=0}^{n-1} Ft_i (mu_{i+1}-mu_i) <= sum_{i=1}^{n-1} U(grid_i)(Ft_{i-1}-Ft_i) + Ft_{n-1} U(grid_n)
n = len(Ft)
Dp = float(np.sum(Ug[1:n]*(Ft[:n-1]-Ft[1:n])) + Ft[n-1]*Ug[n])*INFL
# analytic tail e_q >= y_top = grid[-1]: dyadic blocks (2^k y_top, 2^{k+1} y_top]:
#   <= sum_k U(2^{k+1} y_top) Pi_all e^{U(2^{k+1}y_top)} / (2^k y_top).  For y >= 1e300: U(y) <= 1e-4 + 0.192*log(1 + y^2) <= a + b log y
yt = iv.mpf(grid[-1]); a_ = iv.mpf('0.0002'); b_ = iv.mpf(2*PH)/PR + iv.mpf('1e-6')
# check the linear-log envelope at y_top (and it is preserved for larger y since U grows like (PH/PR) log(y^2))
assert U_iv(1e300) <= float((a_ + b_*iv.log(yt)).a)
r = iv.mpf(2)**(b_-1)                                  # ratio of y^{b-1} between consecutive dyadic blocks
Tsum = iv.mpf(0)
for kk in range(4000):
    yk = yt*iv.mpf(2)**(kk+1)
    Tsum += (a_ + b_*iv.log(yk))*Pi_all*iv.exp(a_)*yk**b_/(yt*iv.mpf(2)**kk)
Ttail = float(Tsum.b)*1.001 + 1e-300   # terms beyond kk=4000 are < 1e-700 relative (geometric with ratio < 0.66)
print(f"  D (largest key unknown, incl. singles q>Y) = {Dp:.6e}   analytic tail beyond 1e300: {Ttail:.3e}")
tau = A + Bp + Cp + Dp + Ttail
print(f"  tau_{w} <= {tau:.6e}    Pi_known(all) = {Pi_all:.6f}")
pickle.dump(dict(w=w, E0=E0, A=A, B=Bp, C=Cp, D=Dp, tail=Ttail, tau=tau), open(DD+f'a5_tau_w{w}.pkl', 'wb'))
