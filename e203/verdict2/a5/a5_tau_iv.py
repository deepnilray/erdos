# a5_tau_iv.py (agent 5, run5): the bound of a5_tau.py redone with NO floating point in any bound:
# integers with directed rounding (ceil(10^18/x)) for all sums over the 5.76e6 known primes, and mpmath.iv for every transcendental.
#   log Pi_known(keys < p) <= sum_{keys<p} g(q)       (log(1+g) <= g), from exact integer cumulative sums of ceil(10^18/(q-2)).
#   A: p1,p2 known, e1 <= E0:   sum g1 g2 Pi(<p2) e^{U(e2)} / lcm(e1,e2)            (iv, 622^2/2 terms)
#   B: p1 known, e1 <= E0:      sum g1/e1 Pi(<p1) (e^{U(e1)} - 1)
#   C: p1 known, e1 > E0:       binned by e (geometric bins): (sum_{bin} g1/e1) * (Pi(< end of bin) e^{U(bin top)} - 1)
#   D: p1 unknown:              Abel summation on the grid as in a5_tau.py, Pi_known(e <= y) bounded via the integer sums.
import numpy as np, math, sys, pickle
from mpmath import iv
iv.dps = 30
sys.path.insert(0, '/home/user/erdos/e203/verdict2/a5')
w = 31; E0 = 3000; Y = 10**8; SC = 10**18
DD = '/home/user/erdos/e203/verdict3/D_data/'
own = np.fromfile(DD+'a5_e_1e8.bin', dtype='<u4').reshape(-1, 2); own = own[own[:, 0] >= w]
q = own[:, 0].astype(np.int64); e = own[:, 1].astype(np.int64)
o = np.lexsort((q, e)); q = q[o]; e = e[o]
gU = -((-SC) // (q-2))                                   # ceil(1e18/(q-2)) as int64 (exact)
cum = np.cumsum(gU.astype(np.uint64))                    # exact (total ~1.7e18 < 1.8e19)
assert int(cum[-1]) < 2**63
cum_before = np.concatenate([[0], cum[:-1]]).astype(np.uint64)
weU = -((-SC) // ((q-2)*e))                              # ceil(1e18/((q-2)e))
LOGY = iv.log(iv.mpf(Y)); LN2 = iv.log(2); PH, PR = 5760, 30030
def U(y):
    y = iv.mpf(y); nmax = y*(y+1)*LN2/(2*LOGY)
    b1 = nmax/(Y-1); nb = nmax/PH + 1
    b2 = iv.mpf(PH)/(Y-1) + iv.mpf(PH)/PR*iv.log(1 + nb*PR/(Y-1))
    return b1 if b1.b < b2.b else b2
def ivint(n): return iv.mpf(int(n))/SC
# ---- A, B ----
sm = np.nonzero(e <= E0)[0]; ns = len(sm)
es = [int(x) for x in e[sm]]; gs = [iv.mpf(1)/(int(x)-2) for x in q[sm]]
Pb = [iv.exp(ivint(cum_before[i])) for i in sm]
Ue = {x: U(x) for x in set(es)}
PbU = [Pb[k]*iv.exp(Ue[es[k]]) for k in range(ns)]
A = iv.mpf(0)
for t in range(1, ns):
    s_ = iv.mpf(0)
    for j in range(t):
        s_ += gs[j]*PbU[j]/math.lcm(es[j], es[t])
    A += gs[t]*s_
Bp = iv.mpf(0)
for k in range(ns):
    Bp += gs[k]/es[k]*Pb[k]*(iv.exp(Ue[es[k]]) - 1)
# ---- C: binned ----
bigi = np.nonzero(e > E0)[0]
edges = np.unique(np.concatenate([np.geomspace(E0+1, int(e.max())+2, 3000).astype(np.int64), [int(e.max())+1]]))
Cp = iv.mpf(0)
pos = np.searchsorted(e[bigi], edges, side='left')
for k in range(len(edges)-1):
    lo, hi = pos[k], pos[k+1]
    if hi <= lo: continue
    idx = bigi[lo:hi]
    swe = int(weU[idx].sum()) + 0                         # >= 1e18 * sum g/e over the bin
    Pi_end = iv.exp(ivint(cum_before[idx[-1]]))           # Pi(<p1) is increasing in key order: bounded at the bin's last key
    Cp += ivint(swe)*(Pi_end*iv.exp(U(int(edges[k+1]))) - 1)
# ---- D ----
grid = np.unique(np.concatenate([np.arange(1, 3001), np.geomspace(3000, 1e15, 6000)]).astype(np.int64)).astype(float)
grid = list(grid) + list(np.geomspace(1e15, 1e300, 400)[1:])
Ug = [U(y) for y in grid]
kk = np.searchsorted(e, np.array([min(y, 4e18) for y in grid]), side='right')
Pk = [iv.exp(ivint(cum[k-1])) if k > 0 else iv.mpf(1) for k in kk]
Fi = [Pk[i+1]*iv.exp(Ug[i+1])/iv.mpf(grid[i]) for i in range(len(grid)-1)]
Ft = [None]*len(Fi); m = iv.mpf(0)
for i in range(len(Fi)-1, -1, -1):
    m = iv.mpf(max(float(m.b), float(Fi[i].b))*(1+1e-14)); Ft[i] = m      # float upper ends nudged up: >= F_i, decreasing
n = len(Ft)
Dp = Ft[n-1]*Ug[n]
for i in range(1, n):
    Dp += Ug[i]*(Ft[i-1]-Ft[i])          # Ft decreasing: coefficients >= 0 (Ft stored as float upper ends, exact as iv points)
# analytic tail beyond 1e300 (as a5_tau.py)
yt = iv.mpf(grid[-1]); a_ = iv.mpf('0.0002'); b_ = iv.mpf(2*PH)/PR + iv.mpf('1e-6')
Pi_all = iv.exp(ivint(cum[-1]))
assert U(1e300).b <= (a_ + b_*iv.log(yt)).a
Tt = iv.mpf(0)
for j in range(4000):
    yk = yt*iv.mpf(2)**(j+1); Tt += (a_ + b_*iv.log(yk))*Pi_all*iv.exp(a_)*yk**b_/(yt*iv.mpf(2)**j)
tau = A + Bp + Cp + Dp + Tt*iv.mpf('1.001')
print(f"[iv] w=31 E0={E0}: A <= {float(A.b):.6e}  B <= {float(Bp.b):.6e}  C <= {float(Cp.b):.6e}  D <= {float(Dp.b):.6e}  tail <= {float(Tt.b):.2e}")
print(f"[iv] tau_31 <= {float(tau.b):.6e}   (Pi_known(all) <= {float(Pi_all.b):.6f})")
pickle.dump(dict(w=w, E0=E0, tau=float(tau.b)), open(DD+'a5_tau_iv_w31.pkl', 'wb'))
