"""Round 1: do solution parameters relate to the two-squares decomposition p = x^2 + y^2?
For each hard prime, compare features of all reps (m,u,t, a=mt-1, b=ut-1) with linear forms e = alpha*x+beta*y.
Reports per-form: number of primes where e equals a feature (exact) / divides a or b (e>=30).  Control: random 'fake x,y'."""
import sys, math, random, collections
reps = collections.defaultdict(list)
for line in open('reps_hard_1e6.txt'):
    p, m, t, u = map(int, line.split()); reps[p].append((m, t, u))
def two_sq(p):
    for y in range(2, int(p ** .5) + 1, 2):
        x2 = p - y * y; x = math.isqrt(x2)
        if x * x == x2: return x, y     # x odd, y even
CONTROL = len(sys.argv) > 1
ps = sorted(reps); R = 8
eq = collections.Counter(); dv = collections.Counter(); n = 0
random.seed(1)
for p in ps:
    x, y = two_sq(p)
    if CONTROL: x, y = random.randint(1, 1000), random.randint(1, 1000)   # planted failure: meaningless x,y
    n += 1
    feats = set(); big = []
    for m, t, u in reps[p]:
        feats |= {m, u, t, m * t - 1, u * t - 1}; big += [m * t - 1, u * t - 1]
    seen_eq = set(); seen_dv = set()
    for al in range(-R, R + 1):
        for be in range(-R, R + 1):
            e = al * x + be * y
            if e < 30 or math.gcd(al, be) != 1: continue
            if e in feats: seen_eq.add((al, be))
            if any(g % e == 0 for g in big): seen_dv.add((al, be))
    eq.update(seen_eq); dv.update(seen_dv)
print("CONTROL" if CONTROL else "MAIN", "primes:", n)
print("top exact-equal forms (alpha,beta): count", eq.most_common(6))
print("top divisor forms     (alpha,beta): count", dv.most_common(6))
