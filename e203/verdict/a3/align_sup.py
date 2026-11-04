"""sup over primitive directions v of S1(v) = sum_{p: psi_p(v)=0} 1/e_p  (necessary >=1 for a 1D Sierpinski covering
along v).  Lower bound: explicit local choices (CRT => a primitive v exists).  Upper bound: stagewise max ignoring
compatibility below.  Pool e_p <= 8e5 (complete-by-construction)."""
import json, math, numpy as np
from sympy import factorint
from collections import defaultdict
pool = [json.loads(l) for l in open('pool800k.jsonl')]
for p in pool: p['f'] = factorint(p['e']); p['L'] = max(p['f'])
heavyset = {5, 7, 13, 17, 19, 37, 73, 97, 577}
K = defaultdict(int)
for p in pool:
    for q, k in p['f'].items(): K[q] = max(K[q], k)
def ok(p, q, d):   # aligned at q
    m = q ** p['f'][q]; return (p['alpha'] * d[0] + p['beta'] * d[1]) % m == 0
stages = defaultdict(list)
for p in pool: stages[p['L']].append(p)
sm = stages[2] + stages[3]
# ---------- upper bound ----------
sm144 = [p for p in sm if 144 % p['e'] == 0]
best144 = []
for x in range(144):
    for y in range(144):
        if math.gcd(math.gcd(x, y), 6) != 1: continue
        s = sum(1 / p['e'] for p in sm144 if (p['alpha'] * x + p['beta'] * y) % p['e'] == 0)
        best144.append((s, x, y))
best144.sort(reverse=True)
light23 = sum(1 / p['e'] for p in sm if 144 % p['e'] != 0)
UB = best144[0][0] + light23
UBst = {}
for l, lst in stages.items():
    if l <= 3: continue
    cnt = defaultdict(float)
    for p in lst:
        k = p['f'][l]; m = l ** k; d = (p['beta'] % m, (-p['alpha']) % m)
        # normalise projective point mod l^k
        if d[0] % l: inv = pow(d[0], -1, m); key = (k, 1, d[1] * inv % m)
        else: inv = pow(d[1], -1, m); key = (k, d[0] * inv % m, 1)
        cnt[key] += 1 / p['e']
    # a direction mod l^K contains points at each level; crude upper bound: sum over levels of max at that level
    lev = defaultdict(float)
    for (k, a, b), v in cnt.items(): lev[k] = max(lev[k], v)
    UBst[l] = sum(lev.values())
UB += sum(UBst.values())
print(f"UPPER bound sup_v S1 (e_p<=8e5): heavy-144 exact {best144[0][0]:.4f} + light23 {light23:.4f} + stages>=5 {sum(UBst.values()):.4f} = {UB:.4f}")
for lo, hi in [(5, 100), (100, 1000), (1000, 10000), (10000, 100000), (100000, 800000)]:
    print(f"   UB part l in [{lo},{hi}): {sum(v for l, v in UBst.items() if lo <= l < hi):.4f}")
# ---------- lower bound: greedy local choices ----------
def lower(x, y):
    d = {2: (x % 16, y % 16), 3: (x % 9, y % 9)}
    tot = 0.0
    # deepen 2-adic and 3-adic directions greedily using {2,3}-smooth primes
    for q in (2, 3):
        while True:
            cur = [p for p in sm if all(ok(p, r, d[r]) if r in d else True for r in p['f'])]
            # candidate deeper directions from smooth primes aligned at other prime and consistent at q mod current depth
            cands = set()
            for p in sm:
                if q not in p['f']: continue
                m = q ** p['f'][q]; dd = (p['beta'] % m, (-p['alpha']) % m)
                cands.add((p['f'][q], dd))
            base = sum(1 / p['e'] for p in cur); bestc = None
            for k, dd in cands:
                # dd must agree with d[q] projectively at the current depth: test via the primes already aligned
                trial = dict(d); trial[q] = dd
                s = sum(1 / p['e'] for p in sm if all(ok(p, r, trial[r]) for r in p['f']))
                if s > base + 1e-15: base, bestc = s, dd
            if bestc is None: break
            d[q] = bestc
    tot = sum(1 / p['e'] for p in sm if all(ok(p, r, d[r]) for r in p['f']))
    part = {}
    for l in sorted(stages):
        if l <= 3: continue
        comp = [p for p in stages[l] if all(ok(p, r, d[r]) for r in p['f'] if r != l)]
        best, bd = 0.0, None
        for p0 in comp:
            m = l ** K[l]; m0 = l ** p0['f'][l]
            dd = (p0['beta'] % m0, (-p0['alpha']) % m0)
            s = sum(1 / p['e'] for p in comp if ok(p, l, dd))
            if s > best: best, bd = s, dd
        if bd is not None: d[l] = bd
        else: d[l] = (1, 0) if all(not ok(p, l, (1, 0)) for p in stages[l] if l in p['f']) else (1, 1)
        part[l] = best; tot += best
    return tot, part, d
res = []
for s, x, y in best144[:6]:
    t, part, d = lower(x, y); res.append(t)
    print(f"LOWER: start v mod 144=({x},{y}) heavy {s:.4f} -> greedy total {t:.4f}; by l-range: " +
          ", ".join(f"[{lo},{hi}):{sum(v for l, v in part.items() if lo <= l < hi):.4f}" for lo, hi in [(5, 100), (100, 1000), (1000, 10000), (10000, 100000), (100000, 800000)]))
print("best lower bound on sup_v S1:", max(res))
