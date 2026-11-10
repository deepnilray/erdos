# Independent recomputation of c = max_{e>E0} rho(e), rho(e)=r(e)*prod_{q|e,q>=5} g_q / e, CAP=0.5, by brute-force segmented sieve to 1e8
import numpy as np, sys
E0=800000; RMAX=2.614450284594; CAP=float(sys.argv[1]) if len(sys.argv)>1 else 0.5; TOP=int(float(sys.argv[2])) if len(sys.argv)>2 else 10**8
z=np.load('verdict3/stages_E800000.npz'); ells=[int(x) for x in z['ells']]; dv=np.minimum(z['dv'],CAP)
g={q:1.0/(1.0-d) for q,d in zip(ells,dv) if q>=5}
print("gmax",max(g.values()),"primes with g",len(g))
SEG=10**7; best=(0,0)
for lo in range(E0+1,TOP,SEG):
    hi=min(lo+SEG,TOP); n=hi-lo
    prod=np.ones(n)
    for q,gq in g.items():
        if q>=hi: continue
        s=(-lo)%q
        prod[s::q]*=gq
    e=np.arange(lo,hi,dtype=np.int64)
    r=np.where((e%2==0)|(e%3==0),RMAX,1.0)
    rho=r*prod/e
    i=int(rho.argmax()); 
    if rho[i]>best[0]: best=(float(rho[i]),int(e[i]))
print("max rho over e in (%d,%d): %.5e at e=%d"%(E0,TOP,*best))
# analytic tail e>=TOP: rho<=RMAX*gmax^w/e with w<=#distinct primes>=5 of e; first k primes>=5 product <= e
import math
gm=max(g.values()); P=1; k=0; bound=0
for q in [5,7,11,13,17,19,23,29,31,37,41,43,47,53]:
    P*=q; k+=1
    # for e in [P_k, P_{k+1}) w<=k ; worst e = max(P_k, TOP)
    bound=max(bound,RMAX*gm**k/max(P,TOP))
print("tail bound e>=TOP (w<=k, e>=max(P_k,TOP)): %.3e"%bound)
