"""Alignment excess in the data: eps_l = sum_{p!=q in stage l} w_p w_q (c_pq - 1) / (sum_p w_p)^2,  w_p = Lam_p / e_p,
c_pq = l-free part of gcd(alpha_p beta_q - beta_p alpha_q, e_p, e_q)   (delta vector of the 8e5 run, delta=0.5 for l>=1000)."""
import json, math, numpy as np
from collections import defaultdict
from sympy import factorint
z = np.load('verdict3/stages_E800000.npz'); ells = [int(x) for x in z['ells']]; dv = z['dv']; idx = {l: i for i, l in enumerate(ells)}
def g(q): return 1.0 if q in (2, 3) else 1 / (1 - (0.5 if q >= 1000 else dv[idx[q]]))
pool = [json.loads(l) for l in open('poolE800000.jsonl')]
st = defaultdict(list)
for p in pool:
    f = factorint(p['e']); l = max(f)
    if l < 5: continue
    lam = 1.0
    for q in f:
        if q != l and q >= 5: lam *= g(q)
    st[l].append((p['alpha'], p['beta'], p['e'], lam / p['e'], l))
out = []
for l in sorted(st):
    P = st[l]
    if len(P) < 2: continue
    a = np.array([x[0] for x in P], dtype=object); b = np.array([x[1] for x in P], dtype=object); e = [x[2] for x in P]
    w = np.array([x[3] for x in P]); s = 0.0
    for i in range(len(P)):
        for j in range(i + 1, len(P)):
            c = math.gcd(math.gcd(P[i][0] * P[j][1] - P[i][1] * P[j][0], P[i][2]), P[j][2])
            while c % l == 0: c //= l
            if c > 1: s += 2 * w[i] * w[j] * (c - 1)
    out.append((l, len(P), s / (w.sum() ** 2 + w.sum() / l), w.sum()))
out.sort()
for l, n, eps, W in out[:20]: print(l, n, round(eps, 4), round(W, 4))
big = [(l, n, eps, W) for l, n, eps, W in out if W * l > 0.0]
print('max eps over stages with >=2 primes:', max(out, key=lambda x: x[2]))
for lo, hi in [(5, 30), (30, 100), (100, 1000), (1000, 10**7)]:
    sel = [x for x in out if lo <= x[0] < hi]
    if sel: print(lo, hi, 'stages', len(sel), 'max eps', round(max(x[2] for x in sel), 4), ' mass-weighted mean', round(sum(x[2] * x[3] ** 2 for x in sel) / sum(x[3] ** 2 for x in sel), 4))
