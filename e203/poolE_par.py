"""Parallel form of poolE_range.py: certified primes with E1 < e_p <= E2 (E2 <= 2*E1), e split over workers.
For e in (E1, E2], G(e) = gcd(2^e-1, 3^e-1) with the primes of proper divisors removed (all proper divisors
are <= e/2 <= E1, covered by the base pool) is exactly the product of primes with e_p = e.  Nothing is dropped;
composite cofactors are factored and every factor is checked to be prime with lcm(ord 2, ord 3) = e.
  python3 poolE_par.py base.jsonl E1 E2 out.jsonl [workers]"""
import sys, json, math, gmpy2
from collections import defaultdict
from multiprocessing import Pool
from sympy import factorint, divisors, primitive_root, isprime
from sympy.ntheory import n_order, discrete_log
base, E1, E2, out = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
W = int(sys.argv[5]) if len(sys.argv) > 5 else 4
assert E2 <= 2 * E1
by_e = defaultdict(list)
for l in open(base):
    p = json.loads(l)
    if p['e'] <= E1: by_e[p['e']].append(p['p'])

def chunk(r):
    lo, hi = r; new = []
    p2 = gmpy2.mpz(2) ** (lo - 1); p3 = gmpy2.mpz(3) ** (lo - 1)
    for e in range(lo, hi):
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
            gg = primitive_root(q); h = pow(gg, (q - 1) // e, q)
            a = int(discrete_log(q, 2, h)) % e; b = int(discrete_log(q, 3, h)) % e
            assert pow(h, a, q) == 2 % q and pow(h, b, q) == 3 % q
            new.append(dict(p=int(q), e=e, alpha=a, beta=b))
    print('chunk', lo, hi, len(new), flush=True)
    return new

if __name__ == '__main__':
    step = 5000
    rs = [(lo, min(lo + step, E2 + 1)) for lo in range(E1 + 1, E2 + 1, step)]
    rs.sort(key=lambda r: -r[0])          # big e first: better load balance
    with Pool(W) as P: res = P.map(chunk, rs, chunksize=1)
    allp = sorted((p for r in res for p in r), key=lambda d: (d['e'], d['p']))
    with open(out, 'w') as fh:
        for d in allp: fh.write(json.dumps(d) + '\n')
    print('E range', E1, E2, 'new primes', len(allp))
