"""Complete pool of primes p (any size) with e_p = |<2,3> mod p| = lcm(ord_p 2, ord_p 3) <= E.

Every such p divides G(e) = gcd(2^e - 1, 3^e - 1).  We strip primes already found at proper
divisors of e; what remains is the product of primes with e_p = e exactly (all == 1 mod e).
Output (JSON lines): p, e, o2, o3, alpha, beta  with  psi_p(k,l) = alpha*k + beta*l  (mod e),
psi_p(k,l) = log_h(2^k 3^l) for a fixed generator h of H_p.
"""
import sys, json, math, gmpy2
from sympy import factorint, divisors, primitive_root, isprime
from sympy.ntheory import n_order, discrete_log

E = int(sys.argv[1]); out = sys.argv[2]
found = {}                      # p -> e_p
unfactored = []
for e in range(1, E + 1):
    g = gmpy2.gcd(gmpy2.mpz(2) ** e - 1, gmpy2.mpz(3) ** e - 1)
    for d in divisors(e)[:-1]:
        for p, ep in found.items():
            if ep == d:
                while g % p == 0: g //= p
    if g == 1: continue
    # primes with e_p = e satisfy p == 1 mod e; trial divide, then ECM/pollard on the rest
    f = factorint(int(g), limit=10**7) if g.bit_length() > 60 else factorint(int(g))
    for p in f:
        if not isprime(p):
            f2 = factorint(p)          # full factorisation (may be slow)
            for q in f2: found[q] = math.lcm(n_order(2, q), n_order(3, q))
        else:
            found[p] = math.lcm(n_order(2, p), n_order(3, p))
    if e % 500 == 0: print(e, len(found), file=sys.stderr, flush=True)

with open(out, 'w') as fh:
    for p in sorted(found):
        e = found[p]; assert (p - 1) % e == 0 and e <= E
        g = primitive_root(p); h = pow(g, (p - 1) // e, p)
        a = discrete_log(p, 2, h) % e; b = discrete_log(p, 3, h) % e
        assert pow(h, a, p) == 2 % p and pow(h, b, p) == 3 % p
        fh.write(json.dumps(dict(p=int(p), e=int(e), o2=int(n_order(2, p)), o3=int(n_order(3, p)), alpha=int(a), beta=int(b))) + '\n')
print('primes', len(found), 'sum 1/e', sum(1 / e for e in found.values()))
