"""a4/gcd_data.py -- 4_tail.md section 2.3.
For n <= NMAX: g_n = gcd(2^n-1, 3^n-1). Reports max log g_n /(n log 2) (the trivial effective bound is 1) and the n attaining it.
Cross-check: log g_n == sum over pool primes p (e_p | n) of v_p(g_n) log p, i.e. g_n is fully explained by poolE800000.jsonl.
Planted control: delete one pool prime with e_p <= NMAX and confirm the cross-check fails for exactly the n divisible by its e_p.
Also: the elementary bound c(e) < e log2 / (2 log e - 2 loglog e - 1) checked on the pool (all e <= 8e5).
usage: python3 verdict2/a4/gcd_data.py [NMAX]"""
import sys, json, math
import gmpy2
NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
pool = [json.loads(l) for l in open('poolE800000.jsonl')]
small = [(r['p'], r['e']) for r in pool if r['e'] <= NMAX]
def check(primes):
    bad = []; best = (0, 0)
    for n in range(1, NMAX + 1):
        g = gmpy2.gcd(gmpy2.mpz(2) ** n - 1, gmpy2.mpz(3) ** n - 1)
        rem = g
        for p, e in primes:
            if n % e == 0:
                while rem % p == 0: rem //= p
        if rem != 1: bad.append(n)
        r = float(gmpy2.log(g)) / (n * math.log(2)) if g > 1 else 0.0
        if r > best[0]: best = (r, n)
    return bad, best
bad, best = check(small)
print(f"n <= {NMAX}: pool explains g_n for all n: {not bad} (unexplained n: {bad[:10]}); max log g_n/(n log 2) = {best[0]:.4f} at n = {best[1]}")
# windowed maxima
for lo in (100, 1000):
    if lo < NMAX:
        m = 0; arg = 0
        for n in range(lo, NMAX + 1):
            g = gmpy2.gcd(gmpy2.mpz(2) ** n - 1, gmpy2.mpz(3) ** n - 1)
            r = float(gmpy2.log(g)) / (n * math.log(2)) if g > 1 else 0.0
            if r > m: m, arg = r, n
        print(f"  max over {lo} <= n <= {NMAX}: {m:.4f} at n = {arg}")
# planted control
victim = max(small, key=lambda t: t[0] if t[1] > 50 else 0)
bad2, _ = check([t for t in small if t != victim])
expect = [n for n in range(1, NMAX + 1) if n % victim[1] == 0]
print(f"control: deleted p={victim[0]} (e={victim[1]}): unexplained n = {bad2[:6]}... count {len(bad2)}, expected {len(expect)} -> fires: {bad2 == expect}")
# elementary pointwise bound
from collections import Counter
c = Counter(r['e'] for r in pool)
viol = [(e, k) for e, k in c.items() if e >= 20 and k >= e * math.log(2) / (2 * math.log(e) - 2 * math.log(math.log(e)) - 1)]
print(f"c(e) bound on pool (e in [20, 8e5]): violations {viol[:5]} ; max c(e) = {max(c.values())}")
