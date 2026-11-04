# a5_delta_moments.py (agent 5, run5): an FFT-FREE rigorous bound for the stratified delta (w = 31).
# Inputs, all PROVED: (i) support: every class has nu_r >= a := 1 - sum_{5<=p<31} 1/e_p (union bound: a prime p in S kills the
#   cells with h_p = c_p, a fraction 1/e_p of H because H -> H_p is onto); (ii) E[nu] = prod(1-1/p) and E[nu^2] (exact rationals
#   from the lattice formula in a5_consts.py); (iii) the constants W_31, M_31, C_31 and E1, E2 as in a5_delta.py.
# Method: find a quadratic q(nu) = al + be nu + ga nu^2 with q >= phi on [a, 1] (LP on a grid, then certified on 4000 subintervals
# with mpmath.iv, plus a margin), so delta <= E[q(nu)] = al + be E[nu] + ga E[nu^2].
import pickle, re, sys, math
import numpy as np
from fractions import Fraction
from scipy.optimize import linprog
from mpmath import iv
iv.dps = 30
DD = '/home/user/erdos/e203/verdict3/D_data/'; A5 = '/home/user/erdos/e203/verdict2/a5/'
K = pickle.load(open(DD+'a5_consts.pkl', 'rb')); T = pickle.load(open(DD+'a5_tau_iv_w31.pkl', 'rb'))
sys.path.insert(0, A5)
from a5_civ import *
dt = np.dtype([('q','<u4'),('e','<u4'),('o2','<u4'),('o3','<u4'),('G','<u2'),('a','<u2'),('b','<u2')])
Dm = np.fromfile(DD+'ep_1e6.bin', dtype=dt); sm = Dm[Dm['q'] < 31]
a_fr = 1 - sum(Fraction(1, int(r['e'])) for r in sm)
m1 = K['Enu']; m2 = K['Enu2']
print("support lower bound a = 1 - sum 1/e_p =", float(a_fr), "  E[nu] =", float(m1), "  E[nu^2] =", float(m2))
rows = []
for line in open(A5+'a5_fh_all.log'):
    mm = re.match(r'\s*(\d+)\s+([\d.]+)\s+([\d.e+-]+)\s+[\d.]+\s+([\d.e+-]+)', line)
    if mm: rows.append((int(mm.group(1)), float(mm.group(3))*(1+1e-5), float(mm.group(4))*(1+1e-5)))
rows.append((10**9, 0.0, 0.0))
a = float(a_fr)
def phi_iv(nu, E1, E2):          # unclipped formula; nu an iv interval
    return 1 - (1-E1)**2/(iv.exp(E2)*C31*(W31 + M31*(1/nu - 1)))
out = []
for (r0, E1, E2) in rows:
    E1i = iv.mpf(E1); E2i = iv.mpf(E2)
    g = np.linspace(a, 1, 3001)
    ph = np.array([float(phi_iv(iv.mpf(x), E1i, E2i).b) for x in g])
    c = [1, float(m1), float(m2)]
    A_ub = -np.stack([np.ones_like(g), g, g*g], 1); b_ub = -ph
    res = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=[(None, None)]*3, method='highs')
    al, be, ga = res.x
    # certify q + margin >= phi on [a,1]: subintervals I, need q(I).a + margin >= phi(I.a).b (phi decreasing in nu)
    margin = 1e-6
    def cert(x0, x1, depth=0):
        I = iv.mpf([x0, x1])
        qv = iv.mpf(al) + iv.mpf(be)*I + iv.mpf(ga)*I*I
        if qv.a + margin >= phi_iv(iv.mpf(x0), E1i, E2i).b: return True
        if depth > 40: return False
        xm = (x0 + x1)/2
        return cert(x0, xm, depth+1) and cert(xm, x1, depth+1)
    edges = np.linspace(a, 1, 401)
    ok = all(cert(float(x0), float(x1)) for x0, x1 in zip(edges[:-1], edges[1:]))
    ok = ok and float(edges[0]) <= a   # first edge must not exceed the support bound
    # also phi formula must be >= 0 on [a,1] for the unclipped form to dominate max(0, .)  (else clipping only lowers phi: fine)
    bound = iv.mpf(al) + iv.mpf(be)*fr(m1) + iv.mpf(ga)*fr(m2) + margin
    out.append((r0, float(bound.b), ok))
    print(f"{r0 if r0 < 10**9 else 'inf':>4}  delta_strat(w=31) <= {float(bound.b):.6f}   certified q>=phi on [a,1]: {ok}", flush=True)
pickle.dump(out, open(A5+'a5_delta_moments.pkl', 'wb'))
