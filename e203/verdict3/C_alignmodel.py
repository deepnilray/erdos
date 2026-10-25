"""C_alignmodel.py -- test of the 'random primitive form' alignment model on the 8e5 pool.
For p != q in the same stage l (P+(e)=l) let c_pq = l-free part of gcd(alpha_p beta_q - beta_p alpha_q, e_p, e_q)   (as in distort_fast.py).
Model: for independent uniformly random primitive forms mod e_p, e_q,  E[c_pq] = prod_{r | g} (1 + a_r*rho_r),
   g = l-free part of gcd(e_p,e_q), a_r = v_r(g), rho_r = (r-1)/(r+1)      [DERIVED in C_allE.md, Lemma M]
Statistic per stage-bucket:  Ratio = sum_{p<q} w_p w_q c_pq / sum_{p<q} w_p w_q E[c_pq],  w_p = 1/e_p.
Control: ratio of the same statistic against the NAIVE model c=1 (mean-field), and against the worst case c=g (shows the three models differ).
"""
import json, math, sys, random
from collections import defaultdict
from sympy import factorint
pool = [json.loads(l) for l in open('poolE800000.jsonl')]
maxE = int(float(sys.argv[1])) if len(sys.argv) > 1 else 800000
st = defaultdict(list)
for p in pool:
    if p['e'] > maxE: continue
    f = factorint(p['e']); l = max(f)
    if l < 5: continue
    st[l].append((p['alpha'], p['beta'], p['e'], f))
def rho(r): return (r - 1) / (r + 1)
buckets = [(5, 6), (7, 12), (12, 30), (30, 100), (100, 300), (300, 1000), (1000, 10 ** 7)]
acc = {b: [0.0, 0.0, 0.0, 0.0, 0] for b in buckets}   # actual, model, naive, worst, npairs
for l, P in st.items():
    b = next(b for b in buckets if b[0] <= l < b[1])
    n = len(P)
    if n < 2: continue
    if n > 1500: P = random.Random(l).sample(P, 1500); n = 1500; scale = (len(st[l]) / 1500) ** 2
    else: scale = 1.0
    for i in range(n):
        ai, bi, ei, fi = P[i]
        for j in range(i + 1, n):
            aj, bj, ej, fj = P[j]
            g = math.gcd(ei, ej)
            while g % l == 0: g //= l
            c = math.gcd(ai * bj - bi * aj, g)
            m = 1.0
            for r, a in factorint(g).items(): m *= 1 + a * rho(r)
            w = scale / (ei * ej)
            acc[b][0] += w * c; acc[b][1] += w * m; acc[b][2] += w; acc[b][3] += w * g; acc[b][4] += 1
print('E<=%d   bucket of l      #pairs      actual/model(theta)   actual/naive(c=1)   worst(c=g)/actual' % maxE)
tot = [0, 0, 0, 0]
for b in buckets:
    a, m, nv, w, k = acc[b]
    if k == 0: continue
    print('  l in [%5d,%8d)  %9d      %.3f              %.3f              %.2f' % (b[0], b[1], k, a / m, a / nv, w / a))
