"""Round 8: combined-type coverage.  For n = 1 mod 4, 5<=n<=N:
 FAM(n): Type I family rep (m,t,u): n = m u t - m - u, m=t=3 mod 4.
 CHAM(n): Chamberland/Type II rep n = q r - 4 s1 s2, q=3 mod 4, s_i | (q+1)/4, r>=1, q <= QCAP.
Controls: (a) Elsholtz-Tao: odd squares have NO Type II solution -> CHAM must fail on odd squares (independent theory check of this code);
          (b) planted failure: drop the s_i | (q+1)/4 rule ('bogus') -> squares must acquire reps.
usage: python3 es_combined.py N [bogus]"""
import sys, math
N = int(sys.argv[1]); bogus = len(sys.argv) > 2; QCAP = 4 * N + 1
fam = bytearray(N + 1)
for m in range(3, N, 4):
    for t in range(3, (N + m + 1) // m + 2, 4):
        a = m * t - 1
        # n = u*a - m for u>=1
        for n in range(a - m, N + 1, a):
            if n >= 5 and n % 4 == 1: fam[n] = 1
cham = bytearray(N + 1)
for q in range(3, QCAP + 1, 4):
    h = (q + 1) // 4
    D = [d for d in range(1, h + 1) if h % d == 0] if not bogus else list(range(1, min(h, 60) + 1))
    res = {(4 * s1 * s2) % q for s1 in D for s2 in D}
    for rho in res:
        n0 = (-rho) % q
        if n0 < 5: n0 += q
        for n in range(n0, N + 1, q):
            if n % 4 == 1 and n >= 5: cham[n] = 1
odd = [n for n in range(5, N + 1, 4)]
isq = lambda n: math.isqrt(n) ** 2 == n
sq = [n for n in odd if isq(n)]
A = [n for n in odd if not fam[n]]; B = [n for n in odd if not cham[n]]
print("MODE", "BOGUS" if bogus else "MAIN", "N =", N, " q <=", QCAP)
print("odd squares: %d | with Type II rep (should be 0): %d | with family rep (should be 0): %d" % (len(sq), sum(cham[n] for n in sq), sum(fam[n] for n in sq)))
print("no family rep:", len(A), " no Chamberland rep:", len(B), " both missing:", len(set(A) & set(B)))
print("family-missing non-squares:", [n for n in A if not isq(n)][:40])
print("Chamberland-missing non-squares:", [n for n in B if not isq(n)][:40])
print("family-missing non-squares that HAVE a Chamberland rep:", [n for n in A if not isq(n) and cham[n]][:40])
print("Chamberland-missing non-squares that HAVE a family rep:", [n for n in B if not isq(n) and fam[n]][:40])
primes = [n for n in odd if n > 1 and all(n % d for d in range(2, int(n ** .5) + 1))]
print("primes: no family rep:", [n for n in primes if not fam[n]], " no Chamberland rep:", [n for n in primes if not cham[n]])
