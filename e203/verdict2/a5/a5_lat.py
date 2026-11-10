# a5_lat.py (agent 5, run5): exact lattice utilities for Lambda_d = {(i,j): 2^i 3^j = 1 mod d}, written independently of D_*.py.
# A lattice is given by constraints <v,(a,b)> = 0 mod m. Index computed by successive kernels (no enumeration of H_W).
from math import gcd
from fractions import Fraction
import itertools

def inv(b, m):
    return pow(b, -1, m) if m > 1 else 0

def intersect(basis, a, b, m):
    """basis: ((x1,y1),(x2,y2)) of a lattice L; return basis of L cap {v : a*v0 + b*v1 = 0 mod m}."""
    (u, v) = basis
    x1 = (a*u[0] + b*u[1]) % m
    x2 = (a*v[0] + b*v[1]) % m
    d = gcd(gcd(x1, x2), m)
    mp = m // d; x1 //= d; x2 //= d
    if mp == 1:
        return basis
    g1 = gcd(x2, mp); mq = mp // g1
    j0 = (-x1 * inv((x2 // g1) % mq, mq)) % mq if mq > 1 else 0
    # kernel in coefficient space: (g1, j0) and (0, mq)
    w1 = (g1*u[0] + j0*v[0], g1*u[1] + j0*v[1])
    w2 = (mq*v[0], mq*v[1])
    assert ((a*w1[0] + b*w1[1]) % m == 0) and ((a*w2[0] + b*w2[1]) % m == 0)
    return (w1, w2)

def index(basis):
    (u, v) = basis
    return abs(u[0]*v[1] - u[1]*v[0])

def lattice(cons):
    L = ((1, 0), (0, 1))
    for (a, b, m) in cons:
        L = intersect(L, a, b, m)
    return L

def gfrac(ps):
    r = Fraction(1)
    for p in ps:
        r *= Fraction(1, p - 2)
    return r
