"""Sierpinski-type (1D) coverings: all sets A_p must be unions of lines parallel to a primitive v,
i.e. psi_p(v)=0 (p | 2^a 3^b - 1 or |2^a - 3^b|).  Necessary: S1(v) = sum_{psi_p(v)=0} 1/e_p >= 1."""
import json, math, numpy as np
pool = [json.loads(l) for l in open('pool800k.jsonl')]
A = 160
a, b = np.meshgrid(np.arange(0, A + 1), np.arange(-A, A + 1), indexing='ij'); a = a.ravel(); b = b.ravel()
g = np.gcd(a, b); keep = (g == 1) & ~((a == 0) & (b < 0)); a = a[keep]; b = b[keep]
S = np.zeros(len(a)); Ssmall = np.zeros(len(a))
for p in pool:
    if p['e'] > 20000: continue
    hit = ((p['alpha'] * a + p['beta'] * b) % p['e'] == 0)
    S += hit / p['e']
    if p['e'] <= 200: Ssmall += hit / p['e']
o = np.argsort(-S)
print("vectors:", len(a), " mean S1 =", S.mean(), " (expected sum 1/e^2 =", sum(1 / p['e'] ** 2 for p in pool if p['e'] <= 20000), ")")
for k in o[:15]:
    M = (2 ** int(a[k]) * 3 ** int(b[k]) - 1) if b[k] >= 0 else (2 ** int(a[k]) - 3 ** int(-b[k]))
    print(f"  v=({a[k]},{b[k]})  S1(e_p<=2e4)={S[k]:.4f}  (e_p<=200: {Ssmall[k]:.4f})   M has {len(str(abs(M)))} digits")
# exact maximum over the heavy torus (Z/144)^2 for {2,3}-smooth primes with e | 144
sm = [p for p in pool if 144 % p['e'] == 0]
best = 0; bv = None
for x in range(144):
    for y in range(144):
        if math.gcd(math.gcd(x, y), 6) != 1: continue  # v must be nonzero mod 2 and mod 3 (primitive lift)
        s = sum(1 / p['e'] for p in sm if (p['alpha'] * x + p['beta'] * y) % p['e'] == 0)
        if s > best: best, bv = s, (x, y)
print(f"primes with e_p | 144: {[(p['p'], p['e']) for p in sm]}  sum 1/e={sum(1/p['e'] for p in sm):.4f}")
print(f"  exact max over primitive v mod 144 of aligned mass: {best:.4f} at v={bv}")
