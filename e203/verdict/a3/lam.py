import json, numpy as np, math
from sympy import factorint
from collections import defaultdict
pool = [json.loads(l) for l in open('pool800k.jsonl')]
rows = []
for p in pool:
    f = factorint(p['e']); l = max(f); rows.append((p['e'], l, f[l]))
e = np.array([r[0] for r in rows]); L = np.array([r[1] for r in rows]); v = np.array([r[2] for r in rows])
np.savez('pool_meta.npz', e=e, L=L, v=v)
print("lambda_l(E) = l*sum_{stage l, e<=E} l^{-v}... use m1*l = sum l^(1-v)/e' with e'=e/l^v;  mean over l in bucket")
print("also n_l (primes per stage) and fraction of stages with >=2 primes")
for E in [20000, 200000, 400000, 800000]:
    m = e <= E
    lam = defaultdict(float); cnt = defaultdict(int)
    for ee, l, vv in zip(e[m], L[m], v[m]):
        if l <= 3: continue
        lam[l] += l / ee; cnt[l] += 1   # l * (1/e)
    out = []
    for lo, hi in [(5, 30), (30, 100), (100, 1000), (1000, 10000), (10000, 100000), (100000, 800000)]:
        ls = [l for l in lam if lo <= l < hi]
        if not ls: continue
        nprimes = sum(1 for q in range(lo, min(hi, E)) if factorint(q) == {q: 1}) if hi <= 10000 else None
        out.append(f"[{lo},{hi}): mean lam {np.mean([lam[l] for l in ls]):.3f} mean n {np.mean([cnt[l] for l in ls]):.1f} frac n>=2 {np.mean([cnt[l]>=2 for l in ls]):.2f} m1sum {sum(lam[l]/l for l in ls):.4f}")
    print(f"E={E}:"); print("   " + "\n   ".join(out))
# new mass in (E/2,E] by P+(e) bucket
print("new mass sum 1/e_p with e in (E/2,E] by l=P+(e) bucket")
for E in [40000, 200000, 400000, 800000]:
    m = (e > E // 2) & (e <= E)
    tot = (1 / e[m]).sum()
    s = []
    for lo, hi in [(2, 4), (5, 100), (100, 1000), (1000, 10000), (10000, 1e6)]:
        mm = m & (L >= lo) & (L < hi); s.append(f"[{lo},{hi}):{(1/e[mm]).sum()/tot:.3f}")
    print(f"  ({E//2},{E}] total {tot:.4f}: " + " ".join(s))
