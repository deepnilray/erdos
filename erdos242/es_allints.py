"""Does the family criterion (m=3 mod 4, a | n+m, 4|a, a=-1 mod m) cover ALL n=1 mod 4, or only primes?
usage: python3 es_allints.py N   -- lists n=1 mod 4 (5<=n<=N) with NO hit using m<MMAX"""
import sys
N = int(sys.argv[1]); MMAX = 3000
def hit(n):
    for m in range(3, MMAX, 4):
        M = n + m
        # divisors a of M with 4|a, a = -1 mod m
        d = 1
        while d * d <= M:
            if M % d == 0:
                for a in (d, M // d):
                    if a % 4 == 0 and (a + 1) % m == 0: return m
            d += 1
    return None
bad = [n for n in range(5, N + 1, 4) if hit(n) is None]
isp = lambda n: n > 1 and all(n % i for i in range(2, int(n ** .5) + 1))
print("n=1 mod 4 in [5,%d]: %d, no-hit: %d" % (N, (N - 5) // 4 + 1, len(bad)))
print("no-hit list:", bad[:40]); print("no-hit that are prime:", [n for n in bad if isp(n)])
