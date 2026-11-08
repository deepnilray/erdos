"""(1) Is the family a TYPE I family (exactly one denominator divisible by p)?  (2) Chamberland reciprocity law:
for p = q r - 4 s1 s2 (q=3 mod 4, s_i | (q+1)/4):  Jacobi (p/q) = -(2/q)^(v2(s1)+v2(s2)).  Control: wrong sign must fail.
usage: python3 es_types.py"""
import collections
from fractions import Fraction as F
from sympy import jacobi_symbol as J, primerange
def v2(n):
    c = 0
    while n % 2 == 0: n //= 2; c += 1
    return c
# (1) family -> Type I
n1 = bad1 = 0; types = collections.Counter()
for line in open('reps_hard_1e6.txt'):
    p, m, t, u = map(int, line.split()); w = (m * t - 1) // 4; X = u * t - 1
    d = [u * w, p * w * X, u * w * X]
    assert F(1, d[0]) + F(1, d[1]) + F(1, d[2]) == F(4, p)
    types[sum(x % p == 0 for x in d)] += 1
print("family reps by number of denominators divisible by p:", dict(types))
# (2) Chamberland law, all reps with q <= 4p+1, primes p = 1 mod 4 up to PMAX
PMAX = 400; tot = viol = ctrl = 0
for p in primerange(5, PMAX):
    if p % 4 != 1: continue
    for q in range(3, 4 * p + 2, 4):
        D = [d for d in range(1, (q + 1) // 4 + 1) if ((q + 1) // 4) % d == 0]
        for s1 in D:
            for s2 in D:
                if (p + 4 * s1 * s2) % q == 0:
                    tot += 1
                    pred = -((J(2, q) ** (v2(s1) + v2(s2))))
                    if J(p, q) != pred: viol += 1
                    if J(p, q) != -pred: ctrl += 1       # planted wrong sign: should fail often
print("Chamberland reps tested:", tot, " violations of law:", viol, " | wrong-sign control fails:", ctrl, "of", tot)
