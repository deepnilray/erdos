"""Link between rare representations and the least quadratic non-residue prime l(p).
Prop C => for p=1 mod 8 every hit has an odd prime q | a' with (q/p) = -1, so a' >= l(p), a >= 4 l(p).
Prints R(p) (exhaustive count) vs l(p) for hard primes in a range, and correlation of R with l(p).
usage: python3 es_lnr.py LO HI"""
import sys
from sympy import primerange, isprime, legendre_symbol
LO, HI = int(sys.argv[1]), int(sys.argv[2]); H = {1, 121, 169, 289, 361, 529}
def R(p):
    r = 0
    for m in range(3, (p + 1) // 2 + 2, 4):
        M = p + m; t = 3
        while m * t - 1 <= M:
            if M % (m * t - 1) == 0: r += 1
            t += 4
    return r
def lnr(p):
    for q in primerange(2, 10**4):
        if legendre_symbol(q, p) == -1: return q
rows = [(R(p), lnr(p), p) for p in primerange(LO, HI) if p % 840 in H]
rows.sort()
print("n =", len(rows)); print("lowest R:", rows[:8]); 
import statistics as S
by = {}
for r, l, p in rows: by.setdefault(l, []).append(r)
for l in sorted(by): print("l(p)=%2d  n=%4d  mean R=%.1f  min R=%d" % (l, len(by[l]), S.mean(by[l]), min(by[l])))
