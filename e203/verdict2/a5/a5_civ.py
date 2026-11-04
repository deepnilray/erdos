# a5_civ.py: interval enclosures of the w=31 and w=5 constants (shared by a5_delta.py and a5_delta_moments.py).
#   unstratified: delta_5 = 1 - (1-E1)^2 / (e^{E2} rho),          rho <= C_5 W_5
#   stratified w=31: delta_31 = sum_bins weight_b * phi(nu_b^lo), phi(nu) = min(1, max(0, 1 - (1-E1)^2/(e^{E2} C (W + M(1/nu - 1)))))
# phi is decreasing in nu, so evaluating at the lower bin edge is an upper bound. All arithmetic in mpmath.iv; bin weights exact.
import pickle, re, sys, math
from fractions import Fraction
from mpmath import iv
iv.dps = 30
DD = '/home/user/erdos/e203/verdict3/D_data/'
A5 = '/home/user/erdos/e203/verdict2/a5/'
K = pickle.load(open(DD+'a5_consts.pkl', 'rb'))
T = pickle.load(open(DD+'a5_tau_iv_w31.pkl', 'rb'))
def fr(x): return iv.mpf(x.numerator)/x.denominator
tau = iv.mpf(T['tau'])
S1hi = iv.mpf(K['S1'][1])/10**18
import numpy as np
qs = np.fromfile(DD+'a5_e_1e8.bin', dtype='<u4').reshape(-1, 2)[:, 0].astype(np.int64)
qb = qs[qs >= 1000]; nb_ = len(qb)
sxb = int(((10**18)//((qb-1)**2)).sum(dtype=np.uint64))      # floor sums: sum_{1000<=q<=1e8} x in [sxb, sxb+nb_]*1e-18
def Cbounds(w):
    ps = [int(p) for p in qs if w <= p < 1000]
    exact = Fraction(1)
    for p in ps: exact *= 1 - Fraction(1, (p-1)**2)
    up = fr(exact)*iv.exp(-iv.mpf(sxb)/10**18)                     # prod(1-x) <= exp(-sum x)
    # log(1-x) >= -x-x^2 (x<=1/2); sum_{q>=1000} x^2 < 1e-9; tail q>1e8: prod >= 1 - 1.01e-8
    lo = fr(exact)*iv.exp(-iv.mpf(sxb+nb_)/10**18 - iv.mpf('1e-9'))*(1 - iv.mpf('1.01e-8'))
    return up, lo
C31, C31lo = Cbounds(31)
C5, C5lo = Cbounds(5)
W31 = 1 + S1hi + tau
M31 = iv.mpf(K['B1max_up']) + tau
W5 = fr(K['A1']) + fr(K['single'][1]) + tau*fr(K['Fmax'])
W5lo = fr(K['A1']) + fr(K['single'][0])
rho_up = C5*W5; rho_lo = C5lo*W5lo
print("W_31 <=", float(W31.b), " M_31 <=", float(M31.b), " C_31 <=", float(C31.b), " tau_31 <=", float(tau.b))
print("W_5 in [", float(W5lo.a), ",", float(W5.b), "];  rho in [", float(rho_lo.a), ",", float(rho_up.b), "]")
