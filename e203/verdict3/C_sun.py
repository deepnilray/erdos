"""C_sun.py -- S_K = { e : f(e) <= K-1 },  f(n)=sum_{q^a || n} a(q-1)  (Sun, Acta Arith. 2008, Thm 1.3; Mycielski function).
A minimal covering certificate with K primes has f(e_p) <= K-1 for every p (and e_p <= 2^(K-1)).
Counts the e in S_K above a given pool limit, and lists them.  usage: python3 C_sun.py 8e5 40"""
import sys
LIM = int(float(sys.argv[1])); KMAX = int(sys.argv[2])
primes = [q for q in range(2, KMAX + 2) if all(q % r for r in range(2, int(q ** .5) + 1))]
def gen(bound):                  # all e with f(e) <= bound  (e>=1)
    out = []
    def rec(i, budget, e):
        if i == len(primes): out.append(e); return
        q = primes[i]; a = 0; x = e
        while True:
            if a * (q - 1) > budget: break
            rec(i + 1, budget - a * (q - 1), x)
            a += 1; x *= q
    rec(0, bound, 1)
    return sorted(out)
def f(n):
    s = 0; q = 2
    while n > 1:
        while n % q == 0: s += q - 1; n //= q
        q += 1
    return s
for K in range(18, KMAX + 1):
    S = gen(K - 1)
    assert all(f(e) <= K - 1 for e in S[:200]) and max(S) <= 2 ** (K - 1)
    ext = [e for e in S if e > LIM]
    sm = [e for e in ext if all(e % 5 and e % 7 for _ in [0]) ]
    print('K=%2d  |S_K|=%7d  e<=2^(K-1)=%.3g   above %d: %5d values, largest %d, 3-smooth among them %d'
          % (K, len(S), 2 ** (K - 1), LIM, len(ext), max(S), sum(1 for e in ext if all(e % r for r in primes[2:]))))
