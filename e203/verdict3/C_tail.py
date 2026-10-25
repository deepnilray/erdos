"""[C_tail.py] copy of tail_bound.py (agent A) with the alignment model of C_allE.md Lemma M (theta-weights instead of phi / c=1).
Original docstring: Conditional all-E bound (Task 3).  See A_certify.md section 3 for the statement.
usage: tail_bound.py KAPPA [L1 override delta=0.5 from this stage on] [Q0 split]
Everything is an upper bound on sum_l cost_l for the pool of ALL primes (any E), assuming hypothesis H(kappa):
   n(e) <= data for e <= E0=8e5, and for e > E0 the stage functionals of n are <= kappa * (those of n_hat(e) = C0 (e/phi e)/ln E0).
"""
import sys, json, math, pickle, numpy as np
from collections import defaultdict
sys.path.insert(0, '.')
import distort_fast as D
KAPPA = float(sys.argv[1]); L1 = int(sys.argv[2]) if len(sys.argv) > 2 else 1000
E0 = 800000; C0 = 0.813; RSTAR = 1 / (1 - 0.626827)
z = np.load('verdict3/stages_E800000.npz'); ells = [int(x) for x in z['ells']]; dvec = z['dv'].copy()
idx = {l: i for i, l in enumerate(ells)}
for l in ells:
    if l >= L1: dvec[idx[l]] = 0.5
def delta(q): return dvec[idx[q]] if q in idx else 0.5       # q > E0: coordinate untouched by the pool, delta chosen 1/2
def g(q): return 1.0 if q in (2, 3) else 1.0 / (1 - delta(q))
# ---- sieve to E0
N = E0 + 1; spf = np.zeros(N, dtype=np.int64)
for i in range(2, N):
    if spf[i] == 0: spf[i::i][spf[i::i] == 0] = i
def fac(n):
    f = {}
    while n > 1: p = int(spf[n]); f[p] = f.get(p, 0) + 1; n //= p
    return f
pool = [json.loads(l) for l in open('poolE800000.jsonl')]
n_of = defaultdict(int)
for p in pool: n_of[p['e']] += 1
# per-e data for e<=E0
def Lam(f, l): 
    r = 1.0
    for q in f:
        if q != l and q >= 5: r *= g(q)
    return r
def phi_f(f):
    r = 1
    for q, a in f.items(): r *= q ** (a - 1) * (q - 1)
    return r
def Fclosed(f_d, l, d_fac_restrict=None):
    """F_d(l) = sum_{e in st(l), d | e} Lam(e)/phi(e) with d given by factorisation f_d (primes < l)."""
    v = l / (l - 1) ** 2
    return v * Fprod_cache(l, f_d)
primes = [int(q) for q in range(2, 20000000) if False]
import sympy
PR = list(sympy.primerange(2, 3000000))
# cumulative Euler product pieces over q < l, as logs
s_q = lambda q: 1 + g(q) * q / (q - 1) ** 2
u_q = lambda q: s_q(q) ** 2 + g(q) ** 2 * q ** 4 / ((q - 1) ** 4 * (q + 1) ** 2)   # theta-weighted Euler factor
logS = np.zeros(len(PR) + 1); logU = np.zeros(len(PR) + 1)
for i, q in enumerate(PR): logS[i + 1] = logS[i] + math.log(s_q(q)); logU[i + 1] = logU[i] + math.log(u_q(q))
pos = {q: i for i, q in enumerate(PR)}
def Fprod_cache(l, f_d):
    i = pos[l]; val = logS[i]
    tot = val
    for q, c in f_d.items():
        tot += -math.log(s_q(q)) + math.log(g(q) * q ** (2 - c) / (q - 1) ** 2)
    return math.exp(tot)
# data by stage
st_e = defaultdict(list)                      # e <= E0 with P+(e)=l : all e (for subtraction), and n_of for data
for e in range(2, E0 + 1):
    f = fac(e); st_e[max(f)].append((e, f))
ALIGN = True
EPS = float(sys.argv[4]) if len(sys.argv) > 4 else 0.0
TAU = KAPPA * C0 / math.log(E0)
TS = np.linspace(0, 1, 801)[1:]
def cost(m1, m2, d, A=1.0):
    best = m1; x = min(2 * d, A)
    if d > 0:
        if x > d: best = min(best, m2 * (x - d) / x ** 2)
        t = TS[TS >= 2 * d]
        if len(t): best = min(best, float(np.min((1 - 2 * d / t) * m1 + d / t ** 2 * m2)))
    return best / (1 - d)
res = {}
stage_list = sorted(set(l for l in PR if 5 <= l < 3000000))
fin = np.load('verdict3/stages_E800000.npz')
tot_lin = 0.0; tot_mom = 0.0; tot_best = 0.0; rows = []
# exact finite cost with the modified delta vector
Bp = pickle.load(open('verdict3/B_E800000.pkl', 'rb'))
_c, _m1, _m2 = D.costs(Bp, dvec); sl = Bp['stage_ells']; cfin = dict(zip(sl, _c)); M1F = dict(zip(sl, _m1)); M2F = dict(zip(sl, _m2)); del Bp
print('finite part with delta override (L1=%d): %.6f   (original %.6f)' % (L1, sum(cfin.values()), fin['cost'].sum()), flush=True)
for l in stage_list:
    d_l = delta(l)
    data = [(e, f) for e, f in st_e.get(l, ()) if n_of.get(e, 0)]
    allE = st_e.get(l, [])
    # F_d closed form for d | e<=E0 ; subtraction
    Fle = defaultdict(float)          # F^{<=}_d
    for e, f in allE:
        lam = Lam(f, l) / phi_f(f)
        f1 = {q: a for q, a in f.items() if q != l}
        ds = [(1, {})]
        for q, a in f1.items():
            ds = [(dd * q ** c, {**ff, **({q: c} if c else {})}) for dd, ff in ds for c in range(a + 1)]
        for dd, ff in ds: Fle[dd] += lam
    Ydata = defaultdict(float)
    for e, f in data:
        w = n_of[e] * Lam(f, l) / e
        f1 = {q: a for q, a in f.items() if q != l}
        ds = [1]
        for q, a in f1.items(): ds = [dd * q ** c for dd in ds for c in range(a + 1)]
        for dd in ds: Ydata[dd] += w
    # tail functionals
    F1 = l / (l - 1) ** 2 * math.exp(logS[pos[l]])
    F1gt = max(F1 - Fle.get(1, 0.0), 0.0)
    # sum_d phi(d) (F_d^>)^2 = Euler - 2 sum phi F F^<= + sum phi (F^<=)^2
    eul = (l / (l - 1) ** 2) ** 2 * math.exp(logU[pos[l]])   # sum_d theta(d) F_d^2 (closed form)
    def Fd(dd):
        fd = fac(dd) if dd < N else None
        return l / (l - 1) ** 2 * Fprod_cache(l, fd) / (l / (l - 1) ** 2) * (l / (l - 1) ** 2) if False else (l / (l - 1) ** 2) * Fprod_cache(l, fd)
    def phi_int(dd):
        r = 1.0
        for q in fac(dd): r *= (q - 1) / (q + 1)
        return r  # THETA(dd) = prod_{q|dd} (q-1)/(q+1)
    S2tail = eul; cross = 0.0
    for dd, v in Fle.items():
        ph = phi_int(dd); Fv = Fd(dd)
        S2tail += -2 * ph * Fv * v + ph * v * v
    S2tail = max(S2tail, 0.0)
    for dd, yv in Ydata.items():
        ph = phi_int(dd); Fgt = max(Fd(dd) - Fle.get(dd, 0.0), 0.0)
        cross += 2 * ph * TAU * yv * Fgt
    S2data = sum(phi_int(dd) * yv * yv for dd, yv in Ydata.items())
    Y1 = Ydata.get(1, 0.0) + TAU * F1gt
    Tt = RSTAR * TAU * F1gt
    m1 = M1F.get(l, 0.0) + Tt
    diag = sum(n_of[e] * Lam(f, l) * (l ** -f[l]) / e for e, f in data) + TAU * F1gt / l
    TH = 1.0 + EPS
    m2 = M2F.get(l, 0.0) + TH * RSTAR * (cross + TAU * TAU * S2tail) + RSTAR * TAU * F1gt / l     # cross already holds 2*theta*TAU*Y*F^>; pool diag is inside M2F
    c_mom = cost(m1, m2, d_l)
    # linear (Lipschitz) tail on top of finite cost
    c_lin = cfin.get(l, 0.0) + RSTAR * TAU * F1gt / (1 - d_l) if l in cfin else RSTAR * TAU * F1gt / (1 - d_l)
    rows.append((l, c_lin, c_mom, m1, m2))
    if l % 1000 == 7 and l < 100: pass
cl = np.array([r[1] for r in rows]); cm = np.array([r[2] for r in rows]); L = np.array([r[0] for r in rows])
best = np.minimum(cl, cm)
# beyond the largest stage computed (3e6): analytic decay; report partial sum and last-term scale
for Q0 in (11, 30, 50, 100, 200, 500, 1000):
    tot = cl[L < Q0].sum() + cm[L >= Q0].sum()
    print(f'KAPPA={KAPPA} L1={L1} split Q0={Q0}: sum(l<{Q0}) linear {cl[L<Q0].sum():.5f} + sum(l>={Q0}) moment {cm[L>=Q0].sum():.5f} = {tot:.5f}', flush=True)
print('min-per-stage total (up to l<3e6):', best.sum(), ' last cm terms:', cm[-3:], 'l:', L[-3:])
np.savez(f'verdict3/C_tailtheta_k{KAPPA}_L{L1}_e{EPS}.npz', L=L, cl=cl, cm=cm)
