"""Smallest modulus m for the family criterion, and exact-identity verification.
Criterion (research log): p in family iff exists m=3 (mod 4) and divisor a | p+m with 4|a, a = -1 (mod m).
Then t=(a+1)/m, u=(p+m)/a, p = m*u*t - m - u, and 4/p = 1/(u w)+1/(p w X)+1/(u w X), w=a/4, X=u t-1.
usage: python3 es_minm.py N [control]"""
import sys, numpy as np
from fractions import Fraction as F
N = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else ""
control = mode == "control"; tamper = mode == "tamper"
LIM = N + 5000
spf = np.zeros(LIM + 1, dtype=np.int32)
for i in range(2, int(LIM ** .5) + 1):
    if spf[i] == 0:
        idx = np.arange(i * i, LIM + 1, i); sel = idx[spf[idx] == 0]; spf[sel] = i
def factor(n):
    f = {}
    while n > 1:
        q = int(spf[n]) or n
        while n % q == 0: f[q] = f.get(q, 0) + 1; n //= q
    return f
def divisors(f):
    ds = [1]
    for q, e in f.items(): ds = [d * q ** k for d in ds for k in range(e + 1)]
    return ds
def primes_upto(n):
    s = np.ones(n + 1, bool); s[:2] = False
    for i in range(2, int(n ** .5) + 1):
        if s[i]: s[i * i::i] = False
    return np.nonzero(s)[0]
HARD = {1, 121, 169, 289, 361, 529}
def check(p, m, a):
    t = (a + 1) // m; u = (p + m) // a; w = a // 4; X = u * t - 1
    assert p == m * u * t - m - u and (m * t) % 4 == 1
    rhs = F(1, u * w) + F(1, p * w * X) + F(1, u * w * X)
    if tamper: rhs += F(1, p * p * 7)           # planted failure: corrupted identity must be caught
    return rhs == F(4, p)
best = {}; hist = {}; bad = 0; nchk = 0; nohit = []
test = [int(p) for p in primes_upto(N) if (p % 840 in HARD)] if not control else \
       [int(p) for p in primes_upto(N) if p % 4 == 3 and p > 3]  # control: p=3 mod 4 must give NO hit
for p in test:
    found = None
    for m in range(3, 4000, 4):
        Nn = p + m
        if control and Nn % 4: continue
        if Nn % 4: break   # p=1 mod 4 -> Nn=0 mod 4 always; p=3 mod 4 -> never
        for d in sorted(divisors(factor(Nn))):
            if d % 4 == 0 and (d + 1) % m == 0:
                found = (m, d); break
        if found: break
    if not found: nohit.append(p); continue
    nchk += 1
    if not check(p, *found): bad += 1
    hist[found[0]] = hist.get(found[0], 0) + 1
    best[p] = found[0]
mx = sorted(best.items(), key=lambda kv: -kv[1])[:12]
print(f"{mode.upper() or 'MAIN'} tested={len(test)} hits={nchk} nohit={len(nohit)} identity_failures={bad}")
if not control:
    print("min-m histogram:", dict(sorted(hist.items())))
    print("12 worst (p, min m):", mx)
    rec = []; cur = 0
    for p in sorted(best):
        if best[p] > cur: cur = best[p]; rec.append((p, cur))
    print("records of min m:", rec)
else: print("nohit sample", nohit[:5])
