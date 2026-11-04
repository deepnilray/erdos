"""Beam search: families S maximising sum 1/e_p subject to |G_S| = |Z^2 / cap L_p| <= Bmax.
Adding p to a family with lattice L multiplies |G_S| by |psi_p(L)|.  Every pool prime q with
L_S subset L_q costs nothing and is absorbed automatically (closure)."""
import sys, math
from collections import defaultdict
from lattice import *
pool = load(sys.argv[1]); Bmax = int(float(sys.argv[2])); width = int(sys.argv[3]) if len(sys.argv) > 3 else 60
by_e = defaultdict(list)
for i, p in enumerate(pool): by_e[p['e']].append(i)
def exponent(H):
    (a, _), (c, d) = H; return a * d // math.gcd(math.gcd(a, c), d)
def close(S, H):
    ex = exponent(H); S = set(S)
    for e in by_e:
        if ex % e == 0:
            for i in by_e[e]:
                if i not in S and image_size(pool[i], H) == 1: S.add(i)
    return frozenset(S)
def dens(S): return sum(1 / pool[j]['e'] for j in S)
I = [[1, 0], [0, 1]]
beam = [(frozenset(), I)]; best = (0, frozenset(), I); seen = set()
while beam:
    cand = []
    for S, H in beam:
        idx = abs(det(H))
        for i, p in enumerate(pool):
            if i in S: continue
            c = image_size(p, H)
            if c == 1 or idx * c > Bmax: continue
            H2 = intersect(p, H); S2 = close(S | {i}, H2)
            if S2 in seen: continue
            seen.add(S2); d2 = dens(S2)
            cand.append((d2 / math.log(abs(det(H2)) + 2), d2, S2, H2))
    if not cand: break
    a = sorted(cand, key=lambda t: -t[0])[:width // 2]; b = sorted(cand, key=lambda t: -t[1])[:width // 2]
    beam = [(S, H) for _, _, S, H in {id(x): x for x in a + b}.values()]
    top = max(cand, key=lambda t: t[1])
    if top[1] > best[0]: best = (top[1], top[2], top[3])
print(f"Bmax={Bmax:.0e}  best sum1/e={best[0]:.4f}  |G_S|={abs(det(best[2]))}  |S|={len(best[1])}", flush=True)
print('  primes:', ','.join(str(pool[j]['p']) for j in sorted(best[1], key=lambda j: pool[j]['e'])), flush=True)
print('  HNF:', best[2])
