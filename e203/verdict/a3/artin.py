import json, math, numpy as np
from sympy import factorint
n = np.load('n_e.npy')
def c_k(m):
    a = (m % 8 == 0); b = (m % 12 == 0)
    return 4 if (a and b) else (2 if (a or b) else 1)
IMAX = 600
FI = {i: set(factorint(i)) if i > 1 else set() for i in range(1, IMAX + 1)}
def pred_n(E0, kummer=True):
    qs = list(factorint(E0)); divs = [(1, 1)]
    for q in qs: divs = divs + [(d * q, -mu) for d, mu in divs]
    tot = 0.0
    for i in range(1, IMAX + 1):
        M = i * E0
        if M % 2: continue
        corr = 1.0
        for q in set(qs) | FI[i]: corr *= q / (q - 1)
        fprob = sum(mu * (c_k(i * d) if kummer else 1) / (i * d) ** 2 for d, mu in divs)
        tot += corr / math.log(M + 1) * fprob
    return tot
rng = np.random.default_rng(7)
for lo, hi in [(10000, 50000), (100000, 200000), (400000, 800000)]:
    s = rng.integers(lo + 1, hi + 1, size=2500)
    pr = np.array([pred_n(int(x)) for x in s]); pr0 = np.array([pred_n(int(x), False) for x in s[:500]])
    ac = n[s]; ev = s % 2 == 0; m4 = s % 4 == 0
    print(f"({lo},{hi}] N=2500: actual {ac.mean():.4f}+-{ac.std()/50:.4f}  Kummer-pred {pr.mean():.4f} ratio {ac.mean()/pr.mean():.3f} | no-Kummer pred (500) {pr0.mean():.4f} vs actual {ac[:500].mean():.4f}")
    for name, msk in [('odd', ~ev), ('2||e', ev & ~m4), ('4|e', m4)]:
        print(f"    {name}: actual {ac[msk].mean():.4f} pred {pr[msk].mean():.4f} ratio {ac[msk].mean()/pr[msk].mean():.3f} (n={msk.sum()})")
    # predicted kappa
    print(f"    implied kappa_pred = {(pr).mean() / np.mean([x/float(__import__('sympy').totient(int(x)))/math.log(x) for x in s[:500]]) :.3f}")
