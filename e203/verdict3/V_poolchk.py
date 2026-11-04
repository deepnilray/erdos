# Independent sampled completeness audit of poolE800000.jsonl (own code: no import from repo).
import json, random, gmpy2, sys
from sympy import factorint, divisors
pool=[json.loads(l) for l in open('/home/claude/e203wt/e203/poolE800000.jsonl')]
print("pool size",len(pool), "distinct", len({p['p'] for p in pool}))
# (1) each pool entry: p prime, p>3, e_p exact = smallest e with 2^e=3^e=1 mod p (via factor of candidate e)
for p in pool:
    q=p['p']; e=p['e']
    assert q>3 and gmpy2.is_prime(q,30)
    assert pow(2,e,q)==1 and pow(3,e,q)==1
    for r in factorint(e):
        assert not (pow(2,e//r,q)==1 and pow(3,e//r,q)==1),(q,e,r)
    # lattice form: alpha,beta with h^alpha=2,h^beta=3 for a common h of order e
    # check via invariance: the map (k,l)->(alpha k+beta l) mod e has kernel = {2^k3^l=1}
    a,b=p['alpha'],p['beta']
    # pick h = any element of order e in H: find by search among powers of 2 and 3 products
    # equivalent check: 2^k 3^l == 1 mod q  <=> a*k+b*l = 0 mod e, tested on random (k,l)
    for _ in range(30):
        k,l=random.randrange(3*e),random.randrange(3*e)
        assert (pow(2,k,q)*pow(3,l,q)%q==1)==((a*k+b*l)%e==0),(q,e,a,b,k,l)
print("entries validated")
from collections import defaultdict
by=defaultdict(list)
for p in pool: by[p['e']].append(p['p'])
random.seed(int(sys.argv[1]) if len(sys.argv)>1 else 1)
levels=random.sample(range(2,800001),int(sys.argv[2]) if len(sys.argv)>2 else 600)
levels+= [e for e in (720720,5040,55440,100000,798336,720000,604800,665280,360360,479001) if e<=800000]
bad=0
for e in levels:
    g=gmpy2.gcd(gmpy2.mpz(2)**e-1,gmpy2.mpz(3)**e-1)
    for d in divisors(e):
        for q in by.get(d,()):
            while g%q==0: g//=q
    if g!=1: bad+=1; print("INCOMPLETE",e)
print("levels",len(levels),"bad",bad)
# planted failure: delete one prime at a nontrivial level, must be detected
fired=0;tr=0
for p in random.sample(pool,60):
    e=p['e']; g=gmpy2.gcd(gmpy2.mpz(2)**e-1,gmpy2.mpz(3)**e-1)
    for d in divisors(e):
        for q in by.get(d,()):
            if q==p['p']: continue
            while g%q==0: g//=q
    tr+=1; fired+= (g!=1)
print("planted deletions detected",fired,"/",tr)
