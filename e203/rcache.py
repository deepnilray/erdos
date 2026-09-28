"""Build the type table for the merged {2,3} stage over a pool: every single term (A = A_p^<) and pair term
(A = A_p^< cap A_q^<) that reads coordinate 2 or 3 is keyed by the canonical HNF of L_A + 144 Z^2.
Writes types_E{E}.json: key -> {weight, minU}.  minU is exact (minunion.c)."""
import sys, json, math, subprocess
from collections import defaultdict
from sympy import factorint
import lattice as LT, rtypes as R
from distort2 import earlier_lattice
pool = [p for p in (json.loads(l) for l in open(sys.argv[1])) if p['e'] <= int(float(sys.argv[2]))]
byp = {p['p']: p for p in pool}
H = [byp[p] for p in [5, 7, 13, 17, 19, 37, 73, 97, 577]]; R.set_heavy(H)
by = defaultdict(list)
for p in pool:
    f = factorint(p['e']); l = max(f)
    if l > 3: by[l].append((p, f))
W = defaultdict(float)
for l, lst in by.items():
    info = []
    for p, f in lst:
        Hl, ep = earlier_lattice(p, l); uses = (2 in f) or (3 in f)
        info.append((Hl, ep, uses))
        if uses: W[R.canon(Hl)] += 1 / p['e']
    for i in range(len(lst)):
        Ha, ea, ua = info[i]; a = lst[i][0]
        for j in range(i + 1, len(lst)):
            Hb, eb, ub = info[j]; b = lst[j][0]
            if not (ua or ub): continue
            Hx = Ha
            if eb > 1:
                bb = dict(b); bb['e'] = eb; bb['alpha'] %= eb; bb['beta'] %= eb; Hx = LT.intersect(bb, Ha)
            c = math.gcd(a['alpha'] * b['beta'] - a['beta'] * b['alpha'], math.gcd(a['e'], b['e']))
            while c % l == 0: c //= l
            W[R.canon(Hx)] += 2 * c / (a['e'] * b['e'])
print('types:', len(W), flush=True)
out = {}
for k, w in sorted(W.items(), key=lambda t: -t[1]):
    g1, g2 = R.gens_from_canon(k)
    out['%d,%d,%d' % k] = dict(weight=w, minU=R.minU_img(g1, g2))
json.dump(out, open(f'types_E{int(float(sys.argv[2]))}.json', 'w'))
print('wrote', len(out), 'types; top weights', [round(v['weight'], 4) for v in list(out.values())[:8]])
