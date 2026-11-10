"""Independent EXACT verifier of the 2D distortion bound (shares no code with distort*.py).

Image sizes of maps Z^2 -> prod Z/n_j (rows (a_j, b_j)) are computed as prod n_j / d_k, where d_k is
the gcd of the k x k minors of the k x (k+2) matrix [rows | diag(n)] (order of the cokernel).
All arithmetic is in Fractions; delta_ell = k/100 exactly.  Majorants: (a,b) = (1,0), the pure
quadratic through (min(2d,A), .), and tangent parabolas b = d/t^2, a = 1-2d/t, t = d + j (1-d)/800,
t >= 2d -- each verified to dominate (x-d)_+ on [0,A] (tangent ones on [0,inf))."""
import sys, json, math, itertools
from fractions import Fraction as F
from sympy import factorint

def det(M):
    n = len(M)
    if n == 1: return M[0][0]
    if n == 2: return M[0][0] * M[1][1] - M[0][1] * M[1][0]
    return sum((-1) ** c * M[0][c] * det([r[:c] + r[c+1:] for r in M[1:]]) for c in range(n))

def image_size(rows):
    """rows: list of (a, b, n).  |image of Z^2 in prod Z/n|."""
    k = len(rows)
    M = [[a, b] + [n if i == j else 0 for j in range(k)] for i, (a, b, n) in enumerate(rows)]
    g = 0
    for cols in itertools.combinations(range(k + 2), k):
        g = math.gcd(g, det([[M[i][c] for c in cols] for i in range(k)]))
        if g == 1: break
    return math.prod(n for _, _, n in rows) // g

def part(p, drop):
    e = p['e']
    while e % drop == 0: e //= drop
    return (p['alpha'] % e, p['beta'] % e, e)

def main(pool_path, E, delta_path):
    pool = [json.loads(l) for l in open(pool_path) if json.loads(l)['e'] <= E]
    dl = {int(k): F(round(100 * v), 100) for k, v in json.load(open(delta_path)).items()}
    st = {}
    for p in pool: st.setdefault(max(factorint(p['e'])), []).append(p)
    s2 = sorted(st.pop(2, []), key=lambda p: p['e']); M = max([p['e'] for p in s2] + [1])
    best = 0
    cells = [(k, l) for k in range(M) for l in range(M)]
    vals = [[(p['alpha'] * k + p['beta'] * l) % p['e'] for k, l in cells] for p in s2]
    for offs in itertools.product([0], *[range(p['e']) for p in s2[1:]]):
        best = max(best, sum(1 for x in range(len(cells)) if any(v[x] == o for v, o in zip(vals, offs))))
    a2 = F(best, len(cells)); assert a2 < 1
    def r(Arows):
        Arows = [x for x in Arows if x[2] > 1]
        if not any(x[2] % 2 == 0 for x in Arows): return F(1)
        base = image_size(Arows) if Arows else 1
        forced = [q for q in s2 if image_size(Arows + [(q['alpha'], q['beta'], q['e'])]) == base * q['e']]
        LB = sum((F(1, q['e']) for q in forced), F(0))
        for q1, q2 in itertools.combinations(forced, 2):
            LB -= F(base, image_size(Arows + [(q1['alpha'], q1['beta'], q1['e']), (q2['alpha'], q2['beta'], q2['e'])]))
        return max(F(0), 1 - LB) / (1 - a2)
    def lam(primes):
        x = F(1)
        for q in primes:
            if q != 2: x /= (1 - dl.get(q, F(0)))
        return x
    total = F(0); rows_out = []
    for ell in sorted(st):
        P = st[ell]; d = dl.get(ell, F(0))
        fac = [factorint(p['e']) for p in P]
        m1 = F(0); m2 = F(0); A = min(F(1), sum((F(1, ell ** f[ell]) for f in fac), F(0)))
        info = [(part(p, ell), [q for q in f if q != ell]) for p, f in zip(P, fac)]
        for p, f, (pr, sup) in zip(P, fac, info):
            w = lam(sup) * r([pr])
            m1 += w / p['e']; m2 += w / (ell ** f[ell] * p['e'])
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
        total += cost; rows_out.append((ell, len(P), float(d), float(m1), float(m2), float(cost)))
    return total, a2, rows_out

if __name__ == '__main__':
    tot, a2, rows = main(sys.argv[1], int(float(sys.argv[2])), sys.argv[3])
    print(f"alpha2max = {a2} = {float(a2):.6f}")
    for r_ in rows[:6]: print('  stage %d: n=%d delta=%.2f m1=%.4f m2=%.4f cost=%.4f' % r_)
    print(f"EXACT RATIONAL BOUND = {float(tot):.6f}  (< 1: {tot < 1})")
