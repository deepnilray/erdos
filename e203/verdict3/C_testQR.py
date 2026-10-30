"""C_testQR.py -- out-of-sample test of the RANGE hypotheses H_L^R, H_Q^R of C_tailR.py with its weights w_l, v_l.
Window (E1, 8e5], C0 calibrated on (E1/2, E1]; prices Lambda with the same delta as C_tail.py (run delta, delta=1/2 for l>=1000).
Controls: data x1.5 (must give ~1.5 / ~2.25); model without e/phi (must fail at small l)."""
import json, math, numpy as np
from collections import defaultdict
z = np.load('verdict3/stages_E800000.npz'); ells = [int(x) for x in z['ells']]; dv = z['dv'].copy(); idx = {l: i for i, l in enumerate(ells)}
for l in ells:
    if l >= 1000: dv[idx[l]] = 0.5
def g(q): return 1.0 if q in (2, 3) else 1 / (1 - (dv[idx[q]] if q in idx else 0.5))
W = np.load('verdict3/C_tailR_weights.npz'); wl = dict(zip(W['L'].astype(int), W['w'])); vl = dict(zip(W['L'].astype(int), W['v']))
n = defaultdict(int)
for l in open('poolE800000.jsonl'): n[json.loads(l)['e']] += 1
E = 800000; spf = np.zeros(E + 1, dtype=np.int64)
for i in range(2, E + 1):
    if spf[i] == 0: spf[i::i][spf[i::i] == 0] = i
info = {}
for e in range(2, E + 1):
    m = e; f = {}
    while m > 1: p = int(spf[m]); f[p] = f.get(p, 0) + 1; m //= p
    ph = 1; lam = 1.0; l = max(f)
    for q, a in f.items(): ph *= q ** (a - 1) * (q - 1)
    for q in f:
        if q != l and q >= 5: lam *= g(q)
    info[e] = (l, f, lam, e / ph)
def stats(weights):
    Y = defaultdict(lambda: defaultdict(float)); th = {}
    for e, x in weights.items():
        l, f, lam, _ = info[e]
        if l < 5: continue
        ds = [(1, 1.0)]
        for q, a in f.items():
            if q != l: ds = [(dd * q ** c, t * (1 if c == 0 else (q - 1) / (q + 1))) for dd, t in ds for c in range(a + 1)]
        for dd, t in ds: Y[l][dd] += x; th[(l, dd)] = t
    return {l: (Yl[1], sum(th[(l, dd)] * y * y for dd, y in Yl.items())) for l, Yl in Y.items()}
RANGES = [(5, 7), (7, 12), (12, 30), (30, 100), (100, 1000), (1000, 10**4), (10**4, 10**5), (10**5, 10**9)]
for E1 in (100000, 200000, 400000):
    for name, shape in (('H', lambda e, ep: ep / math.log(e)), ('no e/phi (control)', lambda e, ep: 1 / math.log(e))):
        C0 = sum(n.get(e, 0) for e in range(E1 // 2 + 1, E1 + 1)) / sum(shape(e, info[e][3]) for e in range(E1 // 2 + 1, E1 + 1))
        win = range(E1 + 1, E + 1)
        real = stats({e: n[e] * info[e][2] / e for e in win if n.get(e)}); mod = stats({e: C0 * shape(e, info[e][3]) * info[e][2] / e for e in win})
        out = []
        for lo, hi in RANGES:
            ls = [l for l in mod if lo <= l < hi]
            a = [sum(wl.get(l, 0) * real.get(l, (0, 0))[k] for l in ls) if k == 0 else sum(vl.get(l, 0) * real.get(l, (0, 0))[1] for l in ls) for k in (0, 1)]
            b = [sum(wl.get(l, 0) * mod[l][0] for l in ls), sum(vl.get(l, 0) * mod[l][1] for l in ls)]
            out.append('[%g,%g) L %.2f Q %s' % (lo, hi, a[0] / b[0] if b[0] else float('nan'), ('%.2f' % (a[1] / b[1])) if b[1] else '-'))
        print('window (%d,8e5] %-18s C0=%.3f | %s' % (E1, name, C0, ' | '.join(out)), flush=True)
