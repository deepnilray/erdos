import math, numpy as np
from sympy import factorint
n = np.load('n_e.npy')
IMAX = 600
FI = {i: set(factorint(i)) if i > 1 else set() for i in range(1, IMAX + 1)}
def qr(a, p24):  # Legendre (a/p) for a in {2,3} from p mod 24
    if a == 2: return p24 % 8 in (1, 7)
    return p24 % 12 in (1, 11)
def Pm(m, p24):
    a = 0
    while m % 2 == 0: m //= 2; a += 1
    if a == 0: return 1 / m ** 2
    return (1.0 if (qr(2, p24) and qr(3, p24)) else 0.0) / m ** 2 / 4 ** (a - 1)
def pred_n(E0):
    qs = list(factorint(E0)); divs = [(1, 1)]
    for q in qs: divs = divs + [(d * q, -mu) for d, mu in divs]
    tot = 0.0
    for i in range(1, IMAX + 1):
        M = i * E0
        if M % 2: continue
        p24 = (M + 1) % 24
        if p24 % 3 == 0: continue   # p = 3 only
        corr = 1.0
        for q in set(qs) | FI[i]: corr *= q / (q - 1)
        tot += corr / math.log(M + 1) * sum(mu * Pm(i * d, p24) for d, mu in divs)
    return tot
rng = np.random.default_rng(7)
for lo, hi in [(10000, 50000), (100000, 200000), (400000, 800000)]:
    s = rng.integers(lo + 1, hi + 1, size=2500)
    pr = np.array([pred_n(int(x)) for x in s]); ac = n[s]
    print(f"({lo},{hi}]: actual {ac.mean():.4f}+-{ac.std()/50:.4f}  pred(QR-entangled) {pr.mean():.4f}  ratio {ac.mean()/pr.mean():.3f}")
    for name, msk in [('odd', s % 2 == 1), ('2||e', s % 4 == 2), ('4|e', s % 4 == 0)]:
        print(f"    {name}: actual {ac[msk].mean():.4f} pred {pr[msk].mean():.4f} ratio {ac[msk].mean()/pr[msk].mean():.3f}")
# full-range comparison of sum 1/e_p over (4e5,8e5] with every e (pred for all e is expensive) -> sample-based estimate
s = rng.integers(400001, 800001, size=6000); pr = np.array([pred_n(int(x)) for x in s])
print("pred sum_{4e5<e<=8e5} n(e)/e ~", (pr / s).mean() * 400000, " actual", (n[400001:800001] / np.arange(400001, 800001)).sum())
