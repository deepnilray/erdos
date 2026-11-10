"""Lower bound for S(N) = sum_{p: e_p | N} 1/e_p using only primes with (p-1) | N (Fermat)."""
import math, sys
from sympy import divisors, isprime, factorint
from sympy.ntheory import n_order
def S_fermat(N):
    s = 0.0; cnt = 0
    for d in divisors(N):
        p = d + 1
        if p > 3 and isprime(p):
            e = math.lcm(int(n_order(2, p)), int(n_order(3, p))); s += 1 / e; cnt += 1
    return cnt, s
for N in [720, 5040, 55440, 720720, 1441440, 4324320, 21621600, 367567200, 6983776800,
          2**6*3**3*5**2*7*11*13*17*19*23]:
    c, s = S_fermat(N)
    print(f"N={N:>14} ({dict(factorint(N))}) primes(p-1|N)={c:5d}  sum 1/e_p >= {s:.4f}", flush=True)
