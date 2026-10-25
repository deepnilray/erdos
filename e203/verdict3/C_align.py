"""C_align.py -- structural lemmas of C_allE.md section 1 (alignment criterion, 1D reduction, common discrete log).
usage: python3 verdict3/C_align.py   (run from e203/)
Tests (each has a control that can fail):
 T1  Alignment criterion:  cap_p Lambda_p contains a primitive vector  <=>  gcd(e_p,e_q) | D_pq for all pairs
     (D_pq = alpha_p beta_q - beta_p alpha_q).  Compared with the direct lattice computation (lattice.py).
     Control: the WEAKER criterion 'lines coincide mod every prime l | gcd' is shown to disagree with the direct computation.
 T2  1D reduction: for aligned families and random offsets, the covered fraction of the torus (Z/L)^2
     equals the covered fraction of Z/L by the classes  c'_p mod e_p  (with the map pi_v).  Control: wrong map.
"""
import sys, json, math, random, itertools
sys.path.insert(0, '.')
import lattice as LT
pool = LT.load('poolE800000.jsonl')
byp = {q['p']: q for q in pool}

def content(B): return math.gcd(math.gcd(abs(B[0][0]), abs(B[0][1])), math.gcd(abs(B[1][0]), abs(B[1][1])))
def meet(fam):
    B = [[1, 0], [0, 1]]
    for q in fam: B = LT.intersect(q, B)
    return B
def D(a, b): return a['alpha'] * b['beta'] - a['beta'] * b['alpha']
def pair_ok(a, b): return D(a, b) % math.gcd(a['e'], b['e']) == 0
def aligned_pairwise(fam): return all(pair_ok(a, b) for a, b in itertools.combinations(fam, 2))
def aligned_direct(fam): return content(meet(fam)) == 1
def weak_prime_lines(fam):          # control: coincidence only modulo each prime l | gcd (not l^min)
    from sympy import primefactors
    for a, b in itertools.combinations(fam, 2):
        g = math.gcd(a['e'], b['e'])
        for l in primefactors(g):
            if D(a, b) % l: return False
    return True

random.seed(1)
small = [q for q in pool if q['e'] <= 3000]
print('pool small', len(small))
# T1 : random families biased towards positives: sample 2-4 primes among those sharing factors
n = agree = pos = weakdis = 0
for _ in range(20000):
    k = random.choice([2, 3, 4])
    fam = random.sample(small, k)
    if random.random() < 0.7:           # make positives likely: seed with a common short vector
        a, b = random.randint(-30, 30), random.randint(-30, 30)
        if math.gcd(a, b) != 1: continue
        cand = [q for q in small if (q['alpha'] * a + q['beta'] * b) % q['e'] == 0]
        if len(cand) < 2: continue
        fam = random.sample(cand, min(k, len(cand)))
    d = aligned_direct(fam); pw = aligned_pairwise(fam); wk = weak_prime_lines(fam)
    n += 1; agree += (d == pw); pos += d; weakdis += (wk != d)
print('T1: %d families, %d aligned; pairwise criterion agrees with direct lattice test on %d; weak (mod-prime) criterion disagrees on %d  (control fires: %s)'
      % (n, pos, agree, weakdis, weakdis > 0))
assert agree == n
# T2 : 1D reduction
def covered_2d(fam, offs, L):
    cov = bytearray(L * L)
    for q, c in zip(fam, offs):
        for k in range(L):
            base = (q['alpha'] * k - c) % q['e']
            # l with beta l == c - alpha k mod e
            for l in range(L):
                if (base + q['beta'] * l) % q['e'] == 0: cov[k * L + l] = 1
    return sum(cov) / (L * L)
def covered_1d(fam, offs, L, v):
    a, b = v; cov = bytearray(L)
    # pi_v(k,l) = b k - a l ; psi_p(k,l)=c  <=> ... class of pi_v: use psi_p(x0 + t*w)=? derive by brute force map class->t
    # we realise the reduction concretely: find w with pi_v(w)=1, then x = t*w + s*v ; psi_p(x)= t*psi_p(w) since psi_p(v)=0
    w = None
    for k in range(-50, 51):
        for l in range(-50, 51):
            if b * k - a * l == 1: w = (k, l); break
        if w: break
    for q, c in zip(fam, offs):
        for t in range(L):
            if (t * (q['alpha'] * w[0] + q['beta'] * w[1]) - c) % q['e'] == 0: cov[t] = 1
    return sum(cov) / L
tests = fails = 0
tiny = [q for q in small if q['e'] <= 60]
tries = 0
while tests < 60 and tries < 20000:
    tries += 1
    fam = random.sample(tiny, random.choice([2, 3, 4]))
    L = 1
    for q in fam: L = L * q['e'] // math.gcd(L, q['e'])
    if L > 400 or not aligned_pairwise(fam): continue
    B = meet(fam)
    # a primitive vector of M: search the box
    v = None
    for r in range(1, 400):
        for a in range(-r, r + 1):
            for b in (-r, r) if abs(a) < r else range(-r, r + 1):
                if math.gcd(a, b) == 1 and all((q['alpha'] * a + q['beta'] * b) % q['e'] == 0 for q in fam): v = (a, b); break
            if v: break
        if v: break
    assert v is not None
    offs = [random.randrange(q['e']) for q in fam]
    f2 = covered_2d(fam, offs, L); f1 = covered_1d(fam, offs, L, v)
    tests += 1; fails += abs(f1 - f2) > 1e-12
print('T2: %d (aligned family, offsets) tests of the 1D reduction, mismatches %d' % (tests, fails))
assert tests >= 60 and fails == 0
# control for T2: a NON-aligned family pushed through the 1D formula must disagree with the torus count in some cases
bad = tot = 0
tries = 0
while tot < 60 and tries < 20000:
    tries += 1
    fam = random.sample(tiny, 3)
    L = 1
    for q in fam: L = L * q['e'] // math.gcd(L, q['e'])
    if L > 400 or aligned_pairwise(fam): continue
    v = (1, 1)
    offs = [random.randrange(q['e']) for q in fam]
    tot += 1; bad += abs(covered_2d(fam, offs, L) - covered_1d(fam, offs, L, v)) > 1e-12
print('T2 control: %d non-aligned families, 1D formula disagrees with the torus count on %d (must be > 0)' % (tot, bad))
assert bad > 0
