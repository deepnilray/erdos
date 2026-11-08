"""Erdos-Straus: the (m,u,t) family  p + m + u = m*u*t  with m = t = 3 (mod 4).

Claim (proved in es_research_log.md, section 'Theorem A'): for a prime p = 1 (mod 4), if positive
integers m,u,t exist with p + m + u = m*u*t and m = t = 3 (mod 4), then with x = (p+m)/4 the equation
4/p = 1/x + 1/y + 1/z has a solution.  This script (i) searches the family, (ii) feeds x = (p+m)/4 to the
independent divisor-criterion solver of es_experiment.py and verifies the resulting triple in exact
arithmetic, (iii) runs a planted-failure control (wrong m) that must fail often.
"""
import sys
from fractions import Fraction
from math import gcd
from sympy import primerange
from es_experiment import decompose, verify

HARD = {1, 121, 169, 289, 361, 529}

def build_spf(n):
    spf = list(range(n + 1))
    i = 2
    while i * i <= n:
        if spf[i] == i:
            for j in range(i * i, n + 1, i):
                if spf[j] == j:
                    spf[j] = i
        i += 1
    return spf

def divisors(n, spf):
    divs = [1]
    while n > 1:
        q = spf[n]
        e = 0
        while n % q == 0:
            n //= q
            e += 1
        divs = [d * q ** k for d in divs for k in range(e + 1)]
    return divs

def family_search(p, Umax, spf):
    from sympy import divisors as sdivisors
    for u in range(1, Umax + 1):
        P = p + u
        for m in (divisors(P, spf) if spf is not None else sdivisors(P)):
            if m % 4 != 3 or m >= p:
                continue
            c = P // m                      # c = u*t - 1
            if (c + 1) % u:
                continue
            t = (c + 1) // u
            if t % 4 == 3:
                assert p + m + u == m * u * t
                return u, m, t
    return None

if __name__ == "__main__":
    N = int(sys.argv[1]); Umax = int(sys.argv[2])
    spf = build_spf(N + Umax + 5) if N <= 3000000 else None
    minu = {}
    worst = (0, None)
    nofind = []
    checked = 0
    ctrl_fail = 0
    ctrl_total = 0
    for p in primerange(11, N):
        if p % 840 not in HARD:
            continue
        r = family_search(p, Umax, spf)
        if r is None:
            nofind.append(p)
            continue
        u, m, t = r
        minu[u] = minu.get(u, 0) + 1
        if u > worst[0]:
            worst = (u, p, m, t)
        sol = decompose(p, (p + m) // 4)
        assert sol is not None and verify(p, sol), ("THEORY FAILS", p, u, m, t)
        checked += 1
        # planted-failure control: shift m by 4 (keeps p+m divisible by 4, breaks the family)
        for shift in (4, 8):
            sol2 = decompose(p, (p + m + shift) // 4)
            ctrl_total += 1
            if sol2 is None:
                ctrl_fail += 1
    print("hard primes with family hit:", checked, " without hit (u<=%d):" % Umax, len(nofind))
    print("no-hit primes:", nofind[:50])
    print("worst min-u:", worst)
    print("histogram of minimal u:", dict(sorted(minu.items())))
    print("control: wrong-m runs that FAILED to decompose:", ctrl_fail, "of", ctrl_total)
