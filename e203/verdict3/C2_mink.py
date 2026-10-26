# C2_mink.py: Minkowski short vectors of Lambda_p for every pool prime, with controls.
# Checks (all for e_p<=8e5 pool): (1) shortest vector v of Lambda_p has |v|_inf<=sqrt(e) (Minkowski),
# (2) p | 2^a 3^b - 1 for that v (direct modular check), (3) log p <= sqrt(e) log 6,
# (4) distribution of L^2/e compared with random primitive forms mod same e (control),
# (5) control that can fail: perturbed form beta+1 should NOT annihilate v.
import json, math, random, sys
from math import gcd
random.seed(1)
def basis(al,be,e):
    g=gcd(al,e); ap=al//g; ep=e//g
    k0=(-be*pow(ap,-1,ep))%ep if ep>1 else 0
    return (e//g,0),(k0,g)
def reduce2(u,v):
    n=lambda w:w[0]*w[0]+w[1]*w[1]
    while True:
        if n(u)<n(v): u,v=v,u
        m=round((u[0]*v[0]+u[1]*v[1])/n(v))
        if m==0: return v,u
        u=(u[0]-m*v[0],u[1]-m*v[1])
def short(al,be,e):
    u,v=reduce2(*basis(al,be,e))
    best=None
    for a in range(-2,3):
        for b in range(-2,3):
            w=(a*u[0]+b*v[0],a*u[1]+b*v[1])
            if w!=(0,0):
                key=(max(abs(w[0]),abs(w[1])),w)
                if best is None or key<best: best=key
    return best[1],u,v
def ok(p,w):
    return (pow(2,w[0],p)*pow(3,w[1],p))%p==1
rows=[json.loads(l) for l in open('poolE800000.jsonl')]
bad=0;viol=0;sizeviol=0;ctrl_fail=0;ctrl_n=0;r_pool=[];r_rand=[]; hv=0
for r in rows:
    p,e,al,be=r['p'],r['e'],r['alpha'],r['beta']
    if e<3: continue
    w,u,v=short(al,be,e)
    if (al*w[0]+be*w[1])%e: bad+=1
    if not ok(p,w): viol+=1
    if max(abs(w[0]),abs(w[1]))>math.isqrt(e)+0: sizeviol+=1
    if u[0]**2+u[1]**2>2/math.sqrt(3)*e+1e-9: hv+=1
    if math.log(p)>math.sqrt(e)*math.log(6)+1e-9: sizeviol+=1000000
    r_pool.append((u[0]**2+u[1]**2)/e)
    # control: perturbed beta must break the vector (unless w[1]=0)
    if w[1]%e!=0:
        ctrl_n+=1
        if not ok(p,w) or (al*w[0]+(be+1)*w[1])%e: pass
        if (al*w[0]+(be+1)*w[1])%e==0: ctrl_fail+=1   # control "fails" if still annihilated
    # random primitive form control, same e
    while True:
        a2=random.randrange(e); b2=random.randrange(e)
        if gcd(gcd(a2,b2),e)==1 and gcd(a2,e)>=1: break
    w2,_u,_v=short(a2,b2,e); r_rand.append((_u[0]**2+_u[1]**2)/e)
print('pool primes',len(rows))
print('form-annihilation failures (algebra)',bad,'| modular failures p|2^a3^b-1',viol,'| size/Minkowski/log p violations',sizeviol,'| Hermite 2/sqrt3 violations',hv)
print('control (beta+1 still annihilates v, should be rare):',ctrl_fail,'of',ctrl_n)
import statistics as st
for name,x in (('pool',r_pool),('random',r_rand)):
    x=sorted(x); n=len(x)
    print(name,'L^2/e mean %.4f median %.4f q10 %.4f q01 %.4f max %.4f'%(st.mean(x),x[n//2],x[n//10],x[n//100],x[-1]))
print('min over pool of e/(log p/log 6)^2:',min(r['e']/(math.log(r['p'])/math.log(6))**2 for r in rows if r['e']>2))
