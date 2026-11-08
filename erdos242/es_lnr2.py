"""Round 4: for each hard prime p (<1e6) and each rep, which primes q | a=mt-1 (and | b=ut-1) have (q/p) = -1?
Test: does some rep have l(p) | a (least non-residue prime divides a)?  Control: replace l(p) by a random QR prime."""
import collections, random
from sympy import factorint, primerange, legendre_symbol
reps = collections.defaultdict(list)
for line in open('reps_hard_1e6.txt'):
    p, m, t, u = map(int, line.split()); reps[p].append((m, t, u))
P = list(primerange(3, 3000)); random.seed(7)
def lnr(p):
    for q in P:
        if legendre_symbol(q, p) == -1: return q
def stats(ctrl):
    c_a = c_ab = c_any = 0
    for p, rs in reps.items():
        q = lnr(p)
        if ctrl:   # planted failure: a random prime that IS a residue mod p
            q = random.choice([r for r in P if legendre_symbol(r, p) == 1])
        in_a = any((m*t-1) % q == 0 for m, t, u in rs)
        in_ab = any((m*t-1) % q == 0 or (u*t-1) % q == 0 for m, t, u in rs)
        in_N = any((p*t+1) % q == 0 for m, t, u in rs)
        c_a += in_a; c_ab += in_ab; c_any += in_N
    n = len(reps); return n, c_a, c_ab, c_any
for ctrl in (False, True):
    n, a, ab, N = stats(ctrl)
    print("CONTROL(QR prime)" if ctrl else "MAIN (least non-residue l(p))", "primes", n, "| some rep with q|a:", a, "| q|a or q|b:", ab, "| q | pt+1:", N)
