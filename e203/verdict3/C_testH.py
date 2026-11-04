"""C_testH.py -- out-of-sample test of the density hypothesis H_n:  n(e) = #{p: e_p = e}  vs  n_hat(e) = C0 * (e/phi(e)) / ln(e).
C0 is calibrated ONLY on e in (E1/2, E1]; the statistic is then evaluated on (E1, 8e5] in buckets of P+(e), with the stage weights
G(e) = prod_{q|e, q>=5} g_q (g_q = 1/(1-delta_q), delta of the 8e5 run capped at 0.5):    sum n(e) G(e)/e   vs   sum n_hat(e) G(e)/e.
Controls that must fail: model without the e/phi(e) factor; model with 1/ln(e) replaced by 1/ln(e)^2 (both recalibrated the same way).
"""
import json, math, numpy as np
from collections import defaultdict
from sympy import factorint
z = np.load('verdict3/stages_E800000.npz'); ells = [int(x) for x in z['ells']]; dv = np.minimum(z['dv'], 0.5); idx = {l: i for i, l in enumerate(ells)}
def g(q): return 1.0 if q in (2, 3) or q not in idx else 1 / (1 - dv[idx[q]])
n = defaultdict(int)
for l in open('poolE800000.jsonl'): n[json.loads(l)['e']] += 1
E = 800000
info = {}
for e in range(2, E + 1):
    f = factorint(e); G = 1.0; ph = 1
    for q, a in f.items():
        ph *= q ** (a - 1) * (q - 1)
        if q >= 5: G *= g(q)
    info[e] = (max(f), G, e / ph)
def bucket(l): return 5 if l < 7 else 7 if l < 30 else 30 if l < 100 else 100 if l < 1000 else 1000
models = {'e/phi / ln e (H)': lambda e, ep: ep / math.log(e), 'no e/phi (control)': lambda e, ep: 1 / math.log(e), '(e/phi)/ln^2 e (control)': lambda e, ep: ep / math.log(e) ** 2}
for E1 in (100000, 200000, 400000):
    print('calibrate on (%d,%d], test on (%d,800000]' % (E1 // 2, E1, E1))
    for name, shape in models.items():
        num = sum(n.get(e, 0) for e in range(E1 // 2 + 1, E1 + 1)); den = sum(shape(e, info[e][2]) for e in range(E1 // 2 + 1, E1 + 1))
        C0 = num / den
        B = defaultdict(lambda: [0.0, 0.0])
        for e in range(E1 + 1, E + 1):
            l, G, ep = info[e]; b = bucket(l)
            B[b][0] += n.get(e, 0) * G / e; B[b][1] += C0 * shape(e, ep) * G / e
        tot = [sum(v[0] for v in B.values()), sum(v[1] for v in B.values())]
        print('   %-26s C0=%.3f  ratios by P+ bucket: %s   total %.3f (data %.4f)' % (name, C0, ' '.join('%d:%.2f' % (b, B[b][0] / B[b][1]) for b in sorted(B)), tot[0] / tot[1], tot[0]))
