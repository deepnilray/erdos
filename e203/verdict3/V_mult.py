import json, math
from collections import Counter, defaultdict
pool=[json.loads(l) for l in open('/home/claude/e203wt/e203/poolE800000.jsonl')]
def lat(al,be,e):
    g1=math.gcd(al,e); a=e//g1
    c=g1//math.gcd(g1,be)
    # need b with al*b + be*c = 0 mod e
    rhs=(-be*c)%e
    assert rhs%g1==0
    m=a
    if m==1: b=0
    else: b=(rhs//g1)*pow((al//g1)%m,-1,m)%m
    assert a*c==e and (al*b+be*c)%e==0 and (al*a)%e==0 and (be*c*0)%e==0
    return (a,b,c)
ne=Counter(); nl=Counter()
for p in pool:
    ne[p['e']]+=1; nl[(p['e'],)+lat(p['alpha'],p['beta'],p['e'])]+=1
print("max n(e)",max(ne.values()),"hist",sorted(Counter(ne.values()).items()))
big=[ (e,n) for e,n in ne.items() if n>=5]; print("e with n>=5:",sorted(big)[:20], "count",len(big))
print("max primes sharing one lattice",max(nl.values()),"hist",sorted(Counter(nl.values()).items()))
for E in (1e4,1e5,4e5,8e5):
    print(E, "max n(e) for e<=E", max(n for e,n in ne.items() if e<=E))
