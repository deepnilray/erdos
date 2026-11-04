# a5_delta.py (agent 5, run5): rigorous upper bounds for the exceptional density of Theorem A''' (5_noside_analytic.md §3),
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
BW = int(sys.argv[1]) if len(sys.argv) > 1 else 64
NB = pickle.load(open(DD+f'a5_nubins_BW{BW}.pkl', 'rb'))
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
# E's from a5_fh_all.log (printed upper ends, inflated by 1e-5 relative to cover printing)
rows = []
for line in open(A5+'a5_fh_all.log'):
    m = re.match(r'\s*(\d+)\s+([\d.]+)\s+([\d.e+-]+)\s+[\d.]+\s+([\d.e+-]+)', line)
    if m: rows.append((int(m.group(1)), float(m.group(2)), float(m.group(3))*(1+1e-5), float(m.group(4))*(1+1e-5)))
rows.append((10**9, float('inf'), 0.0, 0.0))
Hs = NB['Hs']; DEN = NB['DEN']
bins = [(b, w) for b, w in enumerate(NB['binw']) if w]
assert sum(w for b, w in bins) == DEN
def phi(nu_lo, E1, E2):
    if nu_lo <= 0: return iv.mpf(1)
    ratio = C31*(W31 + M31*(1/nu_lo - 1))
    v = 1 - (1-E1)**2/(iv.exp(E2)*ratio)
    return min(1.0, max(0.0, float(v.b)))      # upper end, clipped
out = []
print(" r0     s       E1 <=        eta2=e^E2-1 <=   delta_unstrat <=   delta_strat(w=31) <=")
for (r0, s, E1, E2) in rows:
    E1i = iv.mpf(E1); E2i = iv.mpf(E2)
    du = float((1 - (1-E1i)**2/(iv.exp(E2i)*rho_up)).b)
    tot = iv.mpf(0)
    for b, wnum in bins:
        nu_lo = Fraction(b*BW, Hs)
        tot += iv.mpf(phi(fr(nu_lo) if b > 0 else 0, E1i, E2i))*wnum
    ds = float((tot/DEN).b)
    out.append((r0, s, E1, math.expm1(E2), du, ds))
    print(f"{r0 if r0 < 10**9 else 'inf':>4} {s:8.4f}  {E1:.3e}    {math.expm1(E2):.3e}        {du:.6f}          {ds:.6f}", flush=True)
pickle.dump(out, open(A5+f'a5_delta_BW{BW}.pkl', 'wb'))
