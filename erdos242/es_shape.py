"""Round 5: which 'shapes' of a = mt-1 suffice?  For each hard prime p<1e6 test if SOME rep has
 (A) a = 4*q, q prime; (B) a = 2^e*q (odd part prime); (C) a' = q*r (two primes); (D) a' has a non-residue prime factor of size <= 50.
Control: same tests on reps of the prime p+4 shifted? -> use 'wrong' prime: reps of p replaced by reps of another hard prime (planted mismatch)."""
import collections
from sympy import factorint, isprime
reps = collections.defaultdict(list)
for line in open('reps_hard_1e6.txt'):
    p, m, t, u = map(int, line.split()); reps[p].append((m, t, u))
def shape(a):
    e = 0
    while a % 2 == 0: a //= 2; e += 1
    f = factorint(a); return e, a, f
def test(rs):
    A = B = C = False
    for m, t, u in rs:
        e, ap, f = shape(m*t-1)
        if e == 2 and isprime(ap): A = True
        if isprime(ap): B = True
        if sum(f.values()) == 2: C = True
    return A, B, C
ps = sorted(reps); cnt = [0, 0, 0]; cntb = [0, 0, 0]
for i, p in enumerate(ps):
    r = test(reps[p]); 
    for j in range(3): cnt[j] += r[j]
print("hard primes:", len(ps))
print("(A) a=4q, q prime :", cnt[0]); print("(B) odd part of a prime:", cnt[1]); print("(C) odd part has exactly 2 prime factors:", cnt[2])
# which primes fail (A)?
failA = [p for p in ps if not test(reps[p])[0]]
print("first primes failing (A):", failA[:12])
