"""Erdos-Straus structural experiment.
For each prime p in the six Mordell classes mod 840, find the smallest offset t>=0
such that x = (p+3)/4 + t yields a decomposition 4/p = 1/x + 1/y + 1/z, using the
exact criterion: m/n = 1/y + 1/z (gcd(m,n)=1) iff exists d | n^2 with d = -n (mod m).
All results are verified by exact Fraction arithmetic.
"""
import sys
from fractions import Fraction
from sympy import factorint, primerange
from math import gcd

HARD = {1, 121, 169, 289, 361, 529}

def divisors_of_square(fx, p):
    # divisors of p^2 * x^2 given factorization fx of x
    divs = [1]
    for q, e in list(fx.items()) + [(p, 1)]:
        new = []
        pw = 1
        for _ in range(2 * e + 1):
            for d in divs:
                new.append(d * pw)
            pw *= q
        divs = new
    return divs

def decompose(p, x):
    m = 4 * x - p
    n = p * x
    if m <= 0:
        return None
    assert gcd(m, n) == 1
    fx = factorint(x)
    for d in divisors_of_square(fx, p):
        if (d + n) % m == 0:
            y = (n + d) // m
            z = (n + n * n // d) // m
            if (y > 0 and z > 0 and (n * n // d + n) % m == 0):
                return (x, y, z)
    return None

def verify(p, sol):
    x, y, z = sol
    return Fraction(1, x) + Fraction(1, y) + Fraction(1, z) == Fraction(4, p)

def min_offset(p):
    x0 = (p + 3) // 4
    t = 0
    while True:
        sol = decompose(p, x0 + t)
        if sol:
            assert verify(p, sol)
            return t, sol
        t += 1
        if t > 100000:
            return None, None

if __name__ == "__main__":
    N = int(sys.argv[1])
    worst = (-1, None)
    hist = {}
    count = 0
    for p in primerange(11, N):
        if p % 840 in HARD:
            t, sol = min_offset(p)
            count += 1
            hist[t] = hist.get(t, 0) + 1
            if t > worst[0]:
                worst = (t, p)
                print("new worst", p, p % 840, "t =", t, sol, flush=True)
    print("hard primes checked:", count)
    print("worst offset:", worst)
    print("histogram of minimal offsets (t:count):", dict(sorted(hist.items())))
