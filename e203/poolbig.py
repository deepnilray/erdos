"""Certified-complete pool of primes p with e_p | N, via ONE gcd:
   G(N) = gcd(2^N - 1, 3^N - 1) is divisible by exactly the primes with e_p | N.
Strip Fermat primes (p-1 | N), then primes 1 + t*e for divisors e of N (t <= T); the pool is
CERTIFIED COMPLETE iff the remaining cofactor is 1 (else the cofactor is factored or reported)."""
import sys, json, math, time, gmpy2
from sympy import divisors, isprime, factorint, primitive_root
from sympy.ntheory import n_order, discrete_log
N = int(sys.argv[1]); T = int(sys.argv[2]) if len(sys.argv) > 2 else 2000
t0 = time.time()
M = (gmpy2.mpz(1) << N) - 1
G = gmpy2.gcd(M, gmpy2.powmod(3, N, M) - 1); del M
print(f'N={N}: gcd computed ({time.time()-t0:.0f}s), {G.bit_length()} bits', flush=True)
found = set(); R = G
def strip(p):
    global R
    if R % p == 0:
        found.add(p)
        while R % p == 0: R //= p
divs = divisors(N)
for d in divs:
    if d + 1 > 3 and isprime(d + 1): strip(d + 1)
for e in divs:
    if R == 1: break
    for t in range(1, T + 1):
        p = 1 + t * e
        if p > 3 and R % p == 0 and isprime(p): strip(p)
cof = int(R)
if cof != 1:
    print('cofactor digits', len(str(cof)), flush=True)
    for q in factorint(cof): found.add(q) if isprime(q) else print('UNFACTORED', q)
rows = []
for p in sorted(found):
    e = math.lcm(int(n_order(2, p)), int(n_order(3, p))); assert N % e == 0
    g = primitive_root(p); h = pow(g, (p - 1) // e, p)
    a = int(discrete_log(p, 2, h)) % e; b = int(discrete_log(p, 3, h)) % e
    assert pow(h, a, p) == 2 % p and pow(h, b, p) == 3 % p
    rows.append(dict(p=int(p), e=e, o2=int(n_order(2, p)), o3=int(n_order(3, p)), alpha=a, beta=b))
# certificate: product of p^(v_p(G)) over found primes == G
chk = gmpy2.mpz(G)
for r in rows:
    while chk % r['p'] == 0: chk //= r['p']
with open(f'poolN_{N}.jsonl', 'w') as fh:
    for r in rows: fh.write(json.dumps(r) + '\n')
print(f"N={N} primes={len(rows)} sum1/e={sum(1/r['e'] for r in rows):.4f} COMPLETE={chk == 1} ({time.time()-t0:.0f}s)", flush=True)
