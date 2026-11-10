import numpy as np, math, json
z = np.load('pool_meta.npz'); e, L = z['e'], z['L']
uI = np.load('dickman_I.npy'); 
def I(u0): return np.interp(u0, uI[0], uI[1])
LAMINF = 1.43
res = {}
for E in [20000, 50000, 100000, 200000, 400000, 800000]:
    m = (e <= E) & (L > 3)
    lam = np.bincount(L[m], weights=L[m] / e[m], minlength=10**6)
    out = {}
    for Lmax in [30, 100, 1000, 10**4]:
        ls = np.nonzero(lam[:Lmax])[0]
        miss = sum(lam[l] / l * I(math.log(E / l) / math.log(l)) / (1 - I(math.log(E / l) / math.log(l))) for l in ls)
        out[Lmax] = miss
    # model missing mass for ALL l (including l > E not yet present): sum over primes l of LAMINF/l * I(u0), u0 = max(0, log(E/l)/log l)
    from sympy import primerange
    tot = 0.0
    for l in primerange(5, 10**7):
        u0 = max(0.0, math.log(E / l) / math.log(l)); tot += LAMINF / l * I(u0)
    out['all_model(l<1e7)'] = tot
    res[E] = out
    print(E, {k: round(v, 4) for k, v in out.items()})
json.dump({str(k): {str(a): b for a, b in v.items()} for k, v in res.items()}, open('missing.json', 'w'))
