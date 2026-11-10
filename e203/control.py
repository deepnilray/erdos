"""Controls for exclude.py.
(1) Soundness: on families where CP-SAT found the EXACT optimum, the bound must be >= optimum.
(2) Planted failure: a deliberately wrong independence test (allowing 3 primes per ell) must be
    caught -- it has to produce a 'bound' BELOW the exact optimum on some family."""
import json, exclude, lattice, exact
pool = {r['p']: r for r in lattice.load('pool20000.jsonl')}
fams = [[5, 7, 11, 13], [5, 7, 11, 13, 17, 19], [5, 7, 13, 17, 41], [5, 11, 13, 23, 37, 61]]
good = exclude.compatible
def bad(T, r):   # WRONG: ignores the "at most two per ell" rule and the direction rule
    return True
for F in fams:
    S = [pool[p] for p in F]
    H = [[1, 0], [0, 1]]
    for p in S: H = lattice.intersect(p, H)
    opt = exact.solve(S, H, tlimit=120)
    exclude.compatible = good; U, _ = exclude.bound(S)
    exclude.compatible = bad;  W, _ = exclude.bound(S)
    exclude.compatible = good
    o = opt['best'] / opt['n']
    print(f"{F}: |G|={opt['n']} exact={o:.4f} ({opt['status']})  bound={U:.4f} {'OK' if U >= o - 1e-12 else 'VIOLATED'}"
          f"   planted-wrong-bound={W:.4f} {'FIRES (below exact)' if W < o - 1e-9 else 'silent'}")
