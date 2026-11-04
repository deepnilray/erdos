# Corrected test: RHS_d computed over ALL multiples (closed-form geometric sums), LHS from Poisson draws truncated at X (undercounts LHS => conservative).
import numpy as np, math, sys
from sympy import divisors, factorint
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
def f(q,a): return 1.0 if a==0 else (g(q) if q>=5 else 1.0)/(q**(a-1)*(q-1))
def tailsum(q,a0): # sum_{a>=a0} f(q,a)
    if a0==0: return 1.0+ (g(q) if q>=5 else 1.0)/(q-1)*(1/(1-1/q))
    return (g(q) if q>=5 else 1.0)/(q**(a0-1)*(q-1))*(1/(1-1/q))
def phi(e):
    r=e
    for q in factorint(e): r=r//q*(q-1)
    return r
def Gof(e,pr): return math.prod(g(q) for q in pr if q>=5 and e%q==0)
rng=np.random.default_rng(2); T=int(sys.argv[2]) if len(sys.argv)>2 else 300
for ell in [int(x) for x in sys.argv[1].split(',')]:
    pr=[p for p in (2,3,5,7,11,13,17,19) if p<=ell]
    es=[e for e in smooth(pr,X) if e>E0 and e%ell==0]
    nh=np.array([tau*e/phi(e) for e in es]); w=np.array([Gof(e,pr)/e for e in es])
    divs=[divisors(e) for e in es]
    cache={}
    def RHS(d):
        if d in cache: return cache[d]
        v={q:0 for q in pr}
        for q,a in factorint(d).items(): v[q]=a
        tot=tau
        for q in pr:
            a0=max(v[q],1 if q==ell else 0)
            tot*=tailsum(q,a0)
        # remove e<=E0 multiples of d with P+(e)=ell
        for e in smooth(pr,E0):
            if e%d==0 and e%ell==0: tot-=tau*Gof(e,pr)/phi(e)
        cache[d]=tot; return tot
    th=lambda d: math.prod((q-1)/(q+1) for q in factorint(d)) if d>1 else 1.0
    Qm=sum(th(d)*RHS(d)**2 for d in smooth(pr,X) if d>=1)
    Qs=[]
    viol={1.0:0,1.5:0,2.0:0}; worst=0
    for t in range(T):
        n=rng.poisson(nh); L={}
        for i in np.nonzero(n)[0]:
            for d in divs[i]: L[d]=L.get(d,0)+n[i]*w[i]
        Qs.append(sum(th(d)*L[d]**2 for d in L)/Qm)
        mx=max((L[d]/RHS(d) for d in L),default=0); worst=max(worst,mx)
        for k in viol:
            if mx>k: viol[k]+=1
    print("ell=%d P(H_dens(kappa) violated for some d) over %d trials: %s ; worst L/RHS %.2f"%(ell,T,{k:v/T for k,v in viol.items()},worst),flush=True)
    print('   aggregate Q=sum theta(d) L_d^2 / model-Q: mean %.2f median %.2f 90%% %.2f max %.2f'%(np.mean(Qs),np.median(Qs),np.quantile(Qs,.9),max(Qs)),flush=True)
