# Is C's H_dens(kappa) ("for every prime l>=5 and every d: sum_{e>E0,P+(e)=l,d|e} n(e)G(e)/e <= kappa * model") violated by its OWN Poisson model?
import numpy as np, math, random, itertools, sys
from sympy import divisors
E0=800000; X=10**10; tau=0.813/math.log(E0)
z=np.load('stages_E800000.npz'); dv=dict(zip(map(int,z['ells']),np.minimum(z['dv'],0.5)))
def g(q): return 1.0/(1.0-dv[q]) if q in dv else 1.0
def smooth(primes,X):
    out=[1]
    for p in primes:
        new=[]
        for m in out:
            x=m
            while x<=X: new.append(x); x*=p
        out=new
    return out
def phi(e):
    r=e; 
    for q in (2,3,5,7,11,13,17,19,23,29,31):
        if e%q==0: r=r//q*(q-1)
    return r
rng=np.random.default_rng(1)
for ell in (5,7,11,13):
    pr=[p for p in (2,3,5,7,11,13) if p<=ell]
    es=[e for e in smooth(pr,X) if e>E0 and e%ell==0]
    nh=np.array([tau*e/phi(e) for e in es]); G=np.array([math.prod(g(q) for q in pr if q>=5 and e%q==0) for e,_ in zip(es,range(len(es)))])
    w=G/np.array(es,float)
    divs=[divisors(e) for e in es]
    # RHS_d
    RHS={}
    for e,d_list,a in zip(es,divs,nh*w):
        for d in d_list: RHS[d]=RHS.get(d,0)+a
    viol={1.0:0,1.5:0,2.0:0}; T=2000
    for t in range(T):
        n=rng.poisson(nh)
        L={}
        for i in np.nonzero(n)[0]:
            for d in divs[i]: L[d]=L.get(d,0)+n[i]*w[i]
        for k in viol:
            if any(L[d]>k*RHS[d] for d in L): viol[k]+=1
    print("ell=%d  #e=%d  total model mass %.3e  P(H_dens(kappa) violated for some d): %s"%(ell,len(es),sum(nh*w),{k:v/T for k,v in viol.items()}),flush=True)
