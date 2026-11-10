# Data version of the pointwise H_dens test on the pool itself: window e in (E1, 8e5], P+(e)=ell, d | e, d chosen = a realised e.
import json, math, numpy as np
from collections import Counter
from sympy import factorint, divisors
E0=800000; E1=int(1e5); tau=0.813/math.log(E0)
z=np.load('stages_E800000.npz'); dv=dict(zip(map(int,z['ells']),np.minimum(z['dv'],0.5)))
g=lambda q: 1.0/(1.0-dv[q]) if (q in dv and q>=5) else 1.0
n=Counter(json.loads(l)['e'] for l in open('../poolE800000.jsonl'))
def info(e):
    f=factorint(e); ph=1; G=1.0
    for q,a in f.items(): ph*=q**(a-1)*(q-1); G*=g(q)
    return max(f),G,ph
cache={}
def I(e):
    if e not in cache: cache[e]=info(e)
    return cache[e]
for ell in (5,7,11,13):
    es=[e for e in range(E1+1,E0+1) if e%ell==0 and I(e)[0]==ell]
    worst=(0,None); 
    LHS={};RHS={}
    for e in es:
        _,G,ph=I(e)
        for d in divisors(e):
            LHS[d]=LHS.get(d,0)+n.get(e,0)*G/e
            RHS[d]=RHS.get(d,0)+tau*G/ph
    ratios=[(LHS[d]/RHS[d],d) for d in LHS if LHS[d]>0]
    r=max(ratios); 
    print("ell=%d window (%d,%d]: #e=%d, worst LHS_d/RHS_d = %.2f at d=%d; share of d with ratio>1.5: %.3f"%(ell,E1,E0,len(es),r[0],r[1],sum(1 for x,_ in ratios if x>1.5)/len(ratios)))
