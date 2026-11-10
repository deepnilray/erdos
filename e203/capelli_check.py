"""Control for the classification: c*z^d + 1 reducible over Q  <=>  c in Z^q (odd prime q | d) or (4|d and c in 4*Z^4).
Checked by sympy factorisation for c = 2^a 3^b M^j (M in {1,5,7,25,35}), d <= 12."""
from sympy import symbols, factor_list, integer_nthroot, primefactors
z = symbols('z')
def is_power(c, q):
    r, ok = integer_nthroot(c, q); return ok
def predicted(c, d):
    for q in primefactors(d):
        if q % 2 == 1 and is_power(c, q): return True
    if d % 4 == 0 and c % 4 == 0 and is_power(c // 4, 4): return True
    return False
bad = 0; n = 0; nred = 0
for M in [1, 5, 7, 25, 35, 11]:
  for j in [1, 2, 3, 4, 6, 12]:
    for a in range(0, 9):
      for b in range(0, 7):
        c = 2**a * 3**b * M**j
        if c == 1: continue
        for d in range(1, 13):
            fl = factor_list(c * z**d + 1)[1]
            red = len(fl) > 1 or fl[0][1] > 1
            n += 1; nred += red
            if red != predicted(c, d): bad += 1; print('MISMATCH', c, d, fl)
print('cases', n, 'reducible', nred, 'mismatches', bad)
# planted failure: drop the 4*Z^4 clause -> must produce mismatches
def predicted_broken(c, d):
    return any(q % 2 == 1 and is_power(c, q) for q in primefactors(d))
mm = sum(1 for d in [4, 8, 12] for c in [4, 4*5**4, 4*7**4*3**4] if predicted_broken(c, d) != (len(factor_list(c*z**d+1)[1]) > 1))
print('planted control mismatches (must be > 0):', mm)
