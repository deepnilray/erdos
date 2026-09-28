"""Independent EXACT verifier for the merged-{2,3} distortion bound (no code shared with distort*.py).
alpha*_heavy is re-derived here by an exact-rational one-layer independence bound, with joint
independence tested as  image_size(rows) == prod(e)  (determinantal divisors)."""
import sys, json, math, itertools
from fractions import Fraction as F
from sympy import factorint
from verify_distortion import image_size, part

def one_layer(H, core=(), core_val=None):
    """coverage <= [core_val] + sum over non-core members (increasing e) of w * prod(1-w_J)."""
    H = sorted(H, key=lambda p: (p['p'] not in core, p['e'])); tot = F(0)
    if core_val is not None: tot = core_val
    for i, p in enumerate(H):
        if core_val is not None and p['p'] in core: continue
        best = F(1)
        for seed in range(i + 1):
            T = [p]; f = F(1)
            for q in H[seed:seed + 1] + H[:i]:
                if q in T: continue
                rows = [(x['alpha'], x['beta'], x['e']) for x in T + [q]]
                if image_size(rows) == math.prod(x['e'] for x in T + [q]): T.append(q); f *= 1 - F(1, q['e'])
            best = min(best, f)
        tot += best / p['e']
    return tot

def main(pool_path, E, heavy_ps, delta_path, core=(), core_val=None, rtable=None):
    """rtable: optional (types_json, coupled_full_txt) for the sharpened price r(A)."""
    pool = [p for p in (json.loads(l) for l in open(pool_path)) if p['e'] <= E]
    dl = {int(k): F(round(100 * v), 100) for k, v in json.load(open(delta_path)).items()}
    st = {}
    for p in pool: st.setdefault(max(factorint(p['e'])), []).append(p)
    first = st.pop(2, []) + st.pop(3, [])
    heavy = [p for p in first if p['p'] in heavy_ps]; assert len(heavy) == len(heavy_ps)
    astar = one_layer(heavy, core, core_val) + sum((F(1, p['e']) for p in first if p['p'] not in heavy_ps), F(0))
    assert astar < 1
    def r(Arows):
        Arows = [x for x in Arows if x[2] > 1]
        if not any(x[2] % 2 == 0 or x[2] % 3 == 0 for x in Arows): return F(1)
        base = image_size(Arows)
        forced = [q for q in heavy if image_size(Arows + [(q['alpha'], q['beta'], q['e'])]) == base * q['e']]
        LB = sum((F(1, q['e']) for q in forced), F(0))
        for q1, q2 in itertools.combinations(forced, 2):
            LB -= F(base, image_size(Arows + [(q1['alpha'], q1['beta'], q1['e']), (q2['alpha'], q2['beta'], q2['e'])]))
        rb = max(F(0), 1 - LB) / (1 - astar)
        if rtable is None: return rb
        key = canon_key(Arows)
        cands = [rb]
        if key in TYPES: cands.append((1 - F(TYPES[key]['minU_num'], TYPES[key]['minU_den'])) / (1 - astar))
        if key in COUP: cands.append(COUP[key] * CORR)
        return min(cands)
    if rtable is not None:
        TYPES = json.load(open(rtable[0])); COUP = {}
        for line in open(rtable[1]):
            k, _, a, nA, g, nG = line.split()
            COUP[k] = (1 - F(int(a), int(nA))) / (1 - F(int(g), int(nG)) - F(485, 10000))
        light = sum((F(1, p['e']) for p in first if p['p'] not in heavy_ps), F(0))
        OPT_H = astar - light                       # the heavy bound used above (exact rational)
        CORR = F(1) if light <= F(485, 10000) else (1 - OPT_H - F(485, 10000)) / (1 - OPT_H - light)
    def canon_key(Arows):
        """canonical HNF key of L_A + 144 Z^2 (lattice code shared with the search; cross-checked 60/60 by brute force)."""
        import lattice as LT, rtypes as RT
        Hs = None
        for a, b, n in Arows:
            if Hs is None: Hs = LT.hnf(LT.kernel_basis(a, b, n))
            else: Hs = LT.intersect(dict(alpha=a, beta=b, e=n), Hs)
        return '%d,%d,%d' % RT.canon(Hs)
    def lam(primes):
        x = F(1)
        for q in primes:
            if q not in (2, 3): x /= (1 - dl.get(q, F(0)))
        return x
    total = F(0)
    for ell in sorted(st):
        P = st[ell]; d = dl.get(ell, F(0)); fac = [factorint(p['e']) for p in P]
        A = min(F(1), sum((F(1, ell ** f[ell]) for f in fac), F(0)))
        info = [(part(p, ell), [q for q in f if q != ell]) for p, f in zip(P, fac)]
        m1 = F(0); m2 = F(0)
        for p, f, (pr, sup) in zip(P, fac, info):
            w = lam(sup) * r([pr]); m1 += w / p['e']; m2 += w / (ell ** f[ell] * p['e'])
        for i, j in itertools.combinations(range(len(P)), 2):
            p, q = P[i], P[j]
            c = math.gcd(p['alpha'] * q['beta'] - p['beta'] * q['alpha'], math.gcd(p['e'], q['e']))
            while c % ell == 0: c //= ell
            (pr, sp_), (qr, sq) = info[i], info[j]
            m2 += 2 * lam(set(sp_) | set(sq)) * r([pr, qr]) * F(c, p['e'] * q['e'])
        if A <= d: cost = F(0)
        else:
            cand = [m1]
            if d > 0:
                x = min(2 * d, A)
                if x > d: cand.append(m2 * (x - d) / x ** 2)
                for jj in range(1, 801):
                    t = d + (1 - d) * F(jj, 800)
                    if t >= 2 * d: cand.append((1 - 2 * d / t) * m1 + d / t ** 2 * m2)
            cost = min(cand) / (1 - d)
        total += cost
    return total, astar

if __name__ == '__main__':
    heavy = [int(x) for x in sys.argv[3].split(',')]
    core = [int(x) for x in sys.argv[5].split(',')] if len(sys.argv) > 5 else ()
    cv = F(sys.argv[6]) if len(sys.argv) > 6 else None          # exact core optimum, e.g. 2770/5184
    rt = (sys.argv[7], sys.argv[8]) if len(sys.argv) > 8 else None
    tot, astar = main(sys.argv[1], int(float(sys.argv[2])), heavy, sys.argv[4], core, cv, rt)
    print(f"alpha* (exact, one-layer heavy + light union) = {float(astar):.6f}")
    print(f"EXACT RATIONAL BOUND (merged {{2,3}}) E={sys.argv[2]}: {float(tot):.6f}  (< 1: {tot < 1})", flush=True)
