"""Extend a certified pool from e <= E1 to e <= E2 (E2 <= 2*E1): for e in (E1, E2], G(e) = gcd(2^e-1, 3^e-1)
with primes of proper divisors removed (all proper divisors are <= e/2 <= E1, covered by the base pool)
is exactly the product of primes with e_p = e.  Nothing is dropped; composite cofactors are factored."""
import sys, json, math, gmpy2
from collections import defaultdict
from sympy import factorint, divisors, primitive_root, isprime
from sympy.ntheory import n_order, discrete_log
base, E1, E2, out = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
assert E2 <= 2 * E1
by_e = defaultdict(list)
for l in open(base):
    p = json.loads(l)
    if p['e'] <= E1: by_e[p['e']].append(p['p'])
new = []
p2 = gmpy2.mpz(2) ** E1; p3 = gmpy2.mpz(3) ** E1
for e in range(E1 + 1, E2 + 1):
    p2 <<= 1; p3 *= 3
    g = gmpy2.gcd(p2 - 1, p3 - 1)
    if g == 1: continue
    for d in divisors(e)[:-1]:
        for q in by_e.get(d, ()):
            while g % q == 0: g //= q
    if g == 1: continue
    for q in factorint(int(g)):
        assert isprime(q)
        assert math.lcm(int(n_order(2, q)), int(n_order(3, q))) == e
        new.append((e, q))
    if e % 20000 == 0: print(e, len(new), flush=True)
with open(out, 'w') as fh:
    for e, p in sorted(new):
        gg = primitive_root(p); h = pow(gg, (p - 1) // e, p)
        a = int(discrete_log(p, 2, h)) % e; b = int(discrete_log(p, 3, h)) % e
        assert pow(h, a, p) == 2 % p and pow(h, b, p) == 3 % p
        fh.write(json.dumps(dict(p=int(p), e=e, alpha=a, beta=b)) + '\n')
print('E range', E1, E2, 'new primes', len(new))
