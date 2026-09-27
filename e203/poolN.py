"""Pool of all primes p with e_p | N (e_p = lcm(ord_p 2, ord_p 3)), any size of p.

For each divisor e of N (increasing), G(e) = gcd(2^e-1, 3^e-1) with primes of smaller e removed
consists exactly of primes with e_p = e.  Cofactors that resist factoring (ECM budget) are
reported and dropped (conservative: the pool can only be larger than reported).
"""
import sys, json, math, gmpy2, signal
from sympy import factorint, divisors, primitive_root, isprime
from sympy.ntheory import n_order, discrete_log

def build(N, budget_digits=60):
    found, dropped = {}, []
    for e in divisors(N):
        g = gmpy2.gcd(gmpy2.mpz(2) ** e - 1, gmpy2.mpz(3) ** e - 1)
        for p in found:
            if e % found[p] == 0:
                while g % p == 0: g //= p
        if g == 1: continue
        g = int(g)
        if isprime(g):
            fs = [g]
        else:
            fs = []
            f = factorint(g, limit=10**6)
            for q in f:
                if isprime(q): fs.append(q)
                elif len(str(q)) <= budget_digits:
                    fs += list(factorint(q))
                else:
                    dropped.append((e, q))
        for q in fs:
            found[q] = math.lcm(int(n_order(2, q)), int(n_order(3, q)))
            assert found[q] == e, (q, e, found[q])
    rows = []
    for p in sorted(found):
        e = found[p]; g = primitive_root(p); h = pow(g, (p - 1) // e, p)
        a = int(discrete_log(p, 2, h)) % e if e > 1 else 0
        b = int(discrete_log(p, 3, h)) % e if e > 1 else 0
        assert pow(h, a, p) == 2 % p and pow(h, b, p) == 3 % p
        rows.append(dict(p=int(p), e=int(e), o2=int(n_order(2, p)), o3=int(n_order(3, p)), alpha=a, beta=b))
    return rows, dropped

if __name__ == '__main__':
    N = int(sys.argv[1])
    rows, dropped = build(N)
    with open(f'poolN_{N}.jsonl', 'w') as fh:
        for r in rows: fh.write(json.dumps(r) + '\n')
    print(N, 'primes', len(rows), 'sum1/e %.4f' % sum(1 / r['e'] for r in rows),
          'dropped', [(e, len(str(q))) for e, q in dropped])
