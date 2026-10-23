"""Prove that each pool form (alpha,beta,e) defines the right lattice: ker(k,l -> alpha k + beta l mod e) = {(k,l): 2^k 3^l = 1 mod p}.
Argument: gcd(alpha,beta,e)=1 makes psi onto Z/e, so ker psi has index e; it has the explicit basis
v1=(e/g,0), v2=(c,g) with g=gcd(alpha,e), c = -beta*(alpha/g)^-1 mod e/g.  We check 2^k 3^l = 1 (mod p) on v1,v2 and that
|<2,3> mod p| = e (= lcm of the two orders), so ker psi <= ker phi with equal index, hence equal.  Planted control: perturb alpha."""
import sys, json, math
from sympy.ntheory import n_order
def ok(p, e, a, b, check_order=True):
    if math.gcd(math.gcd(a, b), e) != 1: return False
    g = math.gcd(a, e); ep = e // g; ap = a // g
    c = (-b * pow(ap, -1, ep)) % ep if ep > 1 else 0
    assert (a * c + b * g) % e == 0 and (a * (e // g)) % e == 0
    if pow(2, e // g, p) != 1: return False
    if (pow(2, c, p) * pow(3, g, p)) % p != 1: return False
    if check_order and math.lcm(int(n_order(2, p)), int(n_order(3, p))) != e: return False
    return True
bad = 0; n = 0
for f in sys.argv[1:]:
    for l in open(f):
        r = json.loads(l); n += 1
        if not ok(r['p'], r['e'], r['alpha'], r['beta']): bad += 1; print('BAD', r)
        if n % 20000 == 0: print(n, flush=True)
print('forms audited', n, 'bad', bad)
# control: perturbing alpha by 1 (or beta) must be detected on a sample
import random; rnd = random.Random(7); fired = tot = 0
rows = [json.loads(l) for l in open(sys.argv[-1])]
for r in rnd.sample(rows, 400):
    tot += 1
    if not ok(r['p'], r['e'], (r['alpha'] + 1) % r['e'], r['beta'], False): fired += 1
print(f'control: perturbed forms rejected {fired}/{tot}')
