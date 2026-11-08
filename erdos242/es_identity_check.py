"""Check Theorem A's explicit identity, independently of the divisor-criterion solver:
   p = m*u*t - m - u, w = (m*t - 1)/4, X = u*t - 1  =>
   4/p = 1/(u*w) + 1/(p*w*X) + 1/(u*w*X).
"""
import sys
from fractions import Fraction
from sympy import primerange
from es_family import family_search, build_spf, HARD

def triple(p, m, u, t):
    assert (m * t - 1) % 4 == 0
    w = (m * t - 1) // 4
    X = u * t - 1
    return (u * w, p * w * X, u * w * X)

if __name__ == "__main__":
    N = int(sys.argv[1]); Umax = int(sys.argv[2])
    spf = build_spf(N + Umax + 5) if N <= 3000000 else None
    ok = bad_ctrl = total_ctrl = n = 0
    for p in primerange(11, N):
        if p % 840 not in HARD:
            continue
        r = family_search(p, Umax, spf)
        u, m, t = r
        x, y, z = triple(p, m, u, t)
        assert Fraction(1, x) + Fraction(1, y) + Fraction(1, z) == Fraction(4, p), p
        n += 1
        # planted failure: perturb w by one in the first denominator
        total_ctrl += 1
        if Fraction(1, x + 1) + Fraction(1, y) + Fraction(1, z) != Fraction(4, p):
            bad_ctrl += 1
    print("explicit identity verified for", n, "hard primes below", N)
    print("control (x -> x+1) detected as wrong:", bad_ctrl, "of", total_ctrl)
