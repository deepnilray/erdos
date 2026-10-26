"""C_testQ.py -- out-of-sample test of the AGGREGATE hypothesis H_Q (replaces the withdrawn pointwise H_dens).
Per stage l=P+(e): Y_d = sum_{e in window, P+(e)=l, d|e} n(e) Lam(e)/e,  Q_l = sum_d theta(d) Y_d^2 (theta(d)=prod_{q|d}(q-1)/(q+1), d over divisors of e/l^v).
Model: n_hat(e) = C0 (e/phi e)/ln e, C0 calibrated on (E1/2,E1] only; window (E1, 8e5].  Reported: Q_real/Q_model per stage (l<=30) and per bucket
(sum over stages in bucket, weighted by Q_model), plus controls (data inflated x1.5 must give ~2.25; model without e/phi)."""
import json, math, numpy as np
from collections import defaultdict
z = np.load('verdict3/stages_E800000.npz'); ells = [int(x) for x in z['ells']]; dv = np.minimum(z['dv'], 0.28); idx = {l: i for i, l in enumerate(ells)}
def g(q): return 1.0 if q in (2,3) or q not in idx else 1/(1-dv[idx[q]])
n = defaultdict(int)
for l in open('poolE800000.jsonl'): n[json.loads(l)['e']] += 1
E = 800000; spf = np.zeros(E+1, dtype=np.int64)
for i in range(2, E+1):
    if spf[i] == 0: spf[i::i][spf[i::i] == 0] = i
def fac(m):
    f = {}
    while m > 1: p = int(spf[m]); f[p] = f.get(p, 0)+1; m //= p
    return f
info = {}
for e in range(2, E+1):
    f = fac(e); ph = 1; lam = 1.0
    for q, a in f.items(): ph *= q**(a-1)*(q-1)
    l = max(f)
    for q in f:
        if q != l and q >= 5: lam *= g(q)
    info[e] = (l, f, lam, e/ph)
def divs(f, l):
    ds = [(1, 1.0)]
    for q, a in f.items():
        if q == l: continue
        ds = [(d*q**c, t*(1 if c == 0 else (q-1)/(q+1))) for d, t in ds for c in range(a+1)]
    return ds
def Q(weights):   # weights: dict e -> mass n*Lam/e ; returns dict l -> Q_l
    Y = defaultdict(lambda: defaultdict(float)); th = {}
    for e, w in weights.items():
        l, f, lam, _ = info[e]
        for d, t in divs(f, l): Y[l][d] += w; th[(l, d)] = t
    return {l: sum(th[(l, d)]*v*v for d, v in Yl.items()) for l, Yl in Y.items()}
def bucket(l): return 5 if l<7 else 7 if l<12 else 12 if l<30 else 30 if l<100 else 100 if l<1000 else 1000
for E1 in (100000, 200000, 400000):
    print('calibrate (%d,%d], window (%d,800000]' % (E1//2, E1, E1))
    for name, shape in (('H', lambda e, ep: ep/math.log(e)), ('no e/phi (control)', lambda e, ep: 1/math.log(e))):
        C0 = sum(n.get(e,0) for e in range(E1//2+1, E1+1)) / sum(shape(e, info[e][3]) for e in range(E1//2+1, E1+1))
        win = range(E1+1, E+1)
        real = Q({e: n[e]*info[e][2]/e for e in win if n.get(e)}); mod = Q({e: C0*shape(e, info[e][3])*info[e][2]/e for e in win})
        infl = Q({e: 1.5*n[e]*info[e][2]/e for e in win if n.get(e)})
        B = defaultdict(lambda: [0., 0., 0.])
        for l in mod:
            b = bucket(l); B[b][0] += real.get(l, 0.); B[b][1] += mod[l]; B[b][2] += infl.get(l, 0.)
        print('  %-20s C0=%.3f  bucket Q_real/Q_model: %s   total %.3f%s' % (name, C0, ' '.join('%d:%.2f' % (b, B[b][0]/B[b][1]) for b in sorted(B)), sum(v[0] for v in B.values())/sum(v[1] for v in B.values()),
              ('   [data x1.5 control: total %.3f]' % (sum(v[2] for v in B.values())/sum(v[1] for v in B.values())) if name == 'H' else '')))
        if name == 'H': print('   per stage l<=29:', ' '.join('%d:%.2f' % (l, real.get(l,0)/mod[l]) for l in sorted(mod) if l < 30))
