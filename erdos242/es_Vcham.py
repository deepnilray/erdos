"""Do the large family-exceptions V (non-square, from U_12e6.txt) have a Chamberland (Type II) rep?  Search q ascending (q<=4n+1) until found.
Control: odd squares from the same file must NOT be found (Elsholtz-Tao), tested for the 6 smallest squares > 1e5 with q <= 4n+1 capped at 400000."""
import math
U = [int(x) for x in open('U_12e6.txt').read().split()]
V = [n for n in U if math.isqrt(n) ** 2 != n]
def find(n, qcap):
    for q in range(3, qcap + 1, 4):
        h = (q + 1) // 4
        D = [d for d in range(1, h + 1) if h % d == 0]
        res = {}
        for s1 in D:
            for s2 in D:
                if (n + 4 * s1 * s2) % q == 0: return (q, (n + 4 * s1 * s2) // q, s1, s2)
    return None
for n in V: print(n, find(n, 4 * n + 1))
sq = [n for n in U if math.isqrt(n) ** 2 == n and n > 100000][:3]
print("control squares (must be None):", [(n, find(n, 100000)) for n in sq])
