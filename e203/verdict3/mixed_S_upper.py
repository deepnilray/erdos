"""Upper bound for S = sum_{5<=q<=E} 1/(q^2 (1-delta_q)) + tail, in exact rationals without the huge common denominator:
each term is rounded UP to a multiple of 10^-40, and delta_q is rounded UP to the next 1/100 (conservative; verify_mixed.py
rounds to nearest).  Then prints Theorem E totals with B = exact fraction from verify23_800k.log and R3 from mixed_800k.log."""
import json, sys, math
from fractions import Fraction as F
from sympy import primerange
E = int(sys.argv[2]); d = json.load(open(sys.argv[1])); B = F(sys.argv[3]); R3 = F(sys.argv[4])
D = 10**40
S_num = 0
for q in primerange(5, E + 1):
    dq = math.ceil(100 * d.get(str(q), 0.0) - 1e-12) / 100          # rounded up
    t = F(1, q * q) / (1 - F(round(dq * 100), 100))
    S_num += -((-t.numerator * D) // t.denominator)                   # ceil(t * D)
S = F(S_num, D); tail = F(1, E - 1)
print(f"S <= {float(S):.6f} (+ tail <= {float(tail):.2e})")
print(f"Theorem E totals (upper bounds): 3 not| g: {float(B + S + tail):.6f}   3 | g: {float(B + S + tail + R3):.6f}")
print("both < 1:", B + S + tail < 1, B + S + tail + R3 < 1)
