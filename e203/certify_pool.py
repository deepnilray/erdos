"""Certify that a pool contains EVERY prime p (not 2,3) with e_p <= E:
for each e <= E, dividing G(e) = gcd(2^e-1, 3^e-1) by all pool primes with e_p | e must leave 1.
Also re-derives e_p = lcm(ord_p 2, ord_p 3) for every pool prime."""
import sys, json, math, gmpy2
from collections import defaultdict
from sympy import divisors
from sympy.ntheory import n_order
pool = [json.loads(l) for l in open(sys.argv[1])]; E = int(sys.argv[2])
by_e = defaultdict(list)
for p in pool:
    assert math.lcm(int(n_order(2, p['p'])), int(n_order(3, p['p']))) == p['e']
    by_e[p['e']].append(p['p'])
bad = 0; p2 = gmpy2.mpz(1); p3 = gmpy2.mpz(1)
for e in range(1, E + 1):
    p2 <<= 1; p3 *= 3
    g = gmpy2.gcd(p2 - 1, p3 - 1)
    if g == 1: continue
    for d in divisors(e):
        for q in by_e.get(d, ()):
            while g % q == 0: g //= q
    if g != 1: bad += 1; print('INCOMPLETE at e =', e, flush=True)
print(f'{sys.argv[1]}: {len(pool)} primes; certified complete for e <= {E}:', bad == 0, flush=True)
