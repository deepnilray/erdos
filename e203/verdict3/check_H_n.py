"""Data check of H_n: for e in (LO, 8e5] compare sum_{p} Lam_p/e_p with sum_e C0 (e/phi e)/ln(E0) * Lam(e)/e, bucketed by P+(e).
Ratio <= kappa is what H_n(kappa) asserts for e > E0; here it is tested on the top half of the data range."""
import json, math, numpy as np
from collections import defaultdict
from sympy import factorint
z = np.load('verdict3/stages_E800000.npz'); ells = [int(x) for x in z['ells']]; dv = z['dv']; idx = {l: i for i, l in enumerate(ells)}
def g(q): return 1.0 if q in (2, 3) else 1 / (1 - (0.5 if q >= 1000 else dv[idx[q]]))
E0 = 800000; C0 = 0.813
n = defaultdict(int)
for l in open('poolE800000.jsonl'): n[json.loads(l)['e']] += 1
for LO in (400000, 200000):
    B = defaultdict(lambda: [0.0, 0.0])
    for e in range(LO + 1, E0 + 1):
        f = factorint(e); l = max(f); lam = 1.0
        for q in f:
            if q != l and q >= 5: lam *= g(q)
        ph = 1
        for q, a in f.items(): ph *= q ** (a - 1) * (q - 1)
        key = 5 if l < 7 else 7 if l < 30 else 30 if l < 100 else 100 if l < 1000 else 1000 if l < 10000 else 10000
        B[key][0] += n.get(e, 0) * lam / e; B[key][1] += C0 / math.log(E0) * (e / ph) * lam / e
    print('range', LO, '-', E0)
    for k in sorted(B): print('  P+ >=', k, ' data %.5f  model(1/lnE0) %.5f  ratio %.3f' % (B[k][0], B[k][1], B[k][0] / B[k][1] if B[k][1] else 0))
    tot = [sum(v[0] for v in B.values()), sum(v[1] for v in B.values())]; print('  total ratio %.3f' % (tot[0] / tot[1]))
