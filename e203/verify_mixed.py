"""Independent check of the mixed-construction terms (Theorem E): no alpha/beta, no Theorem C.
R3 = max over g with 3|g, over the cells killed by each 6-core prime for SOME M (or nothing), of
     u(3Z^2 \\ B_core) / (1 - u(B_core) - lam'),  lam' = light {2,3} mass + 1/36 + 1/48 + 1/144,
computed on (Z/144)^2 by enumerating M mod p and marking 2^k 3^l M^g == -1 (mod p) directly.
S  = sum_{5 <= q <= 4e5} q^-2/(1-delta_q) + tail sum_{q > 4e5} q^-2  (< 1/(4e5 - 1))."""
import json, itertools, numpy as np
from fractions import Fraction as F
from sympy import primerange, factorint
M = 144; CORE = [5, 7, 13, 17, 19, 37]
k, l = np.meshgrid(np.arange(M), np.arange(M), indexing='ij')
T3 = ((k % 3 == 0) & (l % 3 == 0)).ravel()
def killed_sets(p, g):
    pw = (pow(2, k, p) * pow(3, l, p)) % p if False else None
    v = np.array([[pow(2, int(a), p) * pow(3, int(b), p) % p for b in range(M)] for a in range(M)]).ravel()
    sets = {}
    for Mv in range(1, p):
        t = (-pow(pow(Mv, g, p), -1, p)) % p
        mask = (v == t)
        sets[mask.tobytes()] = mask
    nonempty = [s for s in sets.values() if s.any()]   # WLOG every usable prime is used (CRT on M)
    return nonempty if nonempty else [np.zeros(M * M, bool)]
    return list(sets.values())
pool = [json.loads(x) for x in open('poolE400000.jsonl')]
heavy = [5, 7, 13, 17, 19, 37, 73, 97, 577]
light = sum((F(1, p['e']) for p in pool if max(factorint(p['e'])) <= 3 and p['p'] not in heavy), F(0))
lam = light + F(1, 36) + F(1, 48) + F(1, 144)
best = (F(0), None)
for gp in [d for d in range(1, 145) if 144 % d == 0 and d % 3 == 0]:
    S = [killed_sets(p, gp) for p in CORE]
    for combo in itertools.product(*S):
        cov = np.zeros(M * M, bool)
        for c in combo: cov |= c
        num = int((T3 & ~cov).sum()); cg = int(cov.sum())
        r = F(num, M * M) / (1 - F(cg, M * M) - lam)
        if r > best[0]: best = (r, gp)
print(f"light {{2,3}} mass = {float(light):.8f};  lam' = {float(lam):.8f}")
print(f"R3 (all g with 3|g, all M) = {best[0]} = {float(best[0]):.6f}  attained at g' = {best[1]}")
d = json.load(open('delta23r_E400000.json'))
S = sum((F(1, q * q) / (1 - F(round(100 * d.get(str(q), 0.0)), 100)) for q in primerange(5, 400001)), F(0))
tail = F(1, 400000 - 1)
print(f"S = {float(S):.6f} (+ tail <= {float(tail):.2e})")
B = F(730585, 1000000)
print(f"Theorem E totals: 3 not| g: {float(B + S + tail):.6f}   3 | g: {float(B + S + tail + best[0]):.6f}")
