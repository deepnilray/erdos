import numpy as np, math
z = np.load('pool_meta.npz'); e, L = z['e'], z['L']
h = 1e-3; u = np.arange(0, 15, h); r = np.ones_like(u)
for i in range(len(u)):
    if u[i] > 1: r[i] = r[i-1] - h * r[int(round((u[i]-1)/h))] / u[i]
cumI = np.concatenate([[0], np.cumsum(r[:-1] / (1 + u[:-1]) * h)]); Itot = cumI[-1]
def I(u0): return Itot - np.interp(u0, u, cumI)   # int_{u0}^inf rho/(1+u)
np.save('dickman_I.npy', np.vstack([u, Itot - cumI]))
# per-stage lambda at E
for E in [200000, 400000, 800000]:
    m = (e <= E) & (L > 3)
    lam = np.bincount(L[m], weights=L[m] / e[m])
    ls = np.nonzero(lam)[0]
    out = []
    for lo, hi in [(5, 30), (30, 100), (100, 1000), (1000, 10000), (10000, 100000)]:
        k = ls[(ls >= lo) & (ls < hi)]
        pred = np.array([1 - I(math.log(E / l) / math.log(l)) for l in k])
        out.append(f"[{lo},{hi}) lam={lam[k].mean():.3f} (1-I(u0)) mean={pred.mean():.3f} implied lam_inf={lam[k].sum()/pred.sum():.3f}")
    print(f"E={E}: " + "\n     ".join(out))
