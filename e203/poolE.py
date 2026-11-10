"""Certified pool of ALL primes p (not 2,3) with e_p <= E.  For each e, G(e) = gcd(2^e-1, 3^e-1)
with primes of proper-divisor levels removed is exactly the product of primes with e_p = e.
Composite cofactors are fully factored (sympy); nothing is dropped.  Writes JSON lines."""
import sys, json, math, gmpy2
from collections import defaultdict
from sympy import factorint, divisors, primitive_root, isprime
from sympy.ntheory import n_order, discrete_log
E = int(sys.argv[1]); out = sys.argv[2]
by_e = defaultdict(list)
pow2 = gmpy2.mpz(1); pow3 = gmpy2.mpz(1)
for e in range(1, E + 1):
    pow2 <<= 1; pow3 *= 3
    g = gmpy2.gcd(pow2 - 1, pow3 - 1)
    if g == 1: continue
    for d in divisors(e)[:-1]:
        for p in by_e.get(d, ()):
            while g % p == 0: g //= p
    if g == 1: continue
    for q in factorint(int(g)):
        assert isprime(q)
        eq = math.lcm(int(n_order(2, q)), int(n_order(3, q))); assert eq == e, (q, e, eq)
        by_e[e].append(q)
    if e % 10000 == 0: print(e, sum(map(len, by_e.values())), file=sys.stderr, flush=True)
with open(out, 'w') as fh:
    for e in sorted(by_e):
        for p in sorted(by_e[e]):
            g = primitive_root(p); h = pow(g, (p - 1) // e, p)
            a = int(discrete_log(p, 2, h)) % e; b = int(discrete_log(p, 3, h)) % e
            assert pow(h, a, p) == 2 % p and pow(h, b, p) == 3 % p
            fh.write(json.dumps(dict(p=int(p), e=e, alpha=a, beta=b)) + '\n')
print('E', E, 'primes', sum(map(len, by_e.values())), 'sum1/e', sum(len(v) / e for e, v in by_e.items()))
