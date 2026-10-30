# Independent rho_max with cyclic price r(gcd(e,144)); delta from V_delta_cap028.json (or argv[1]); segmented sieve (E0,TOP] + analytic tail.
import numpy as np, json, sys, math
E0=800000; TOP=int(float(sys.argv[2])) if len(sys.argv)>2 else 10**8
d=json.load(open(sys.argv[1] if len(sys.argv)>1 else 'verdict3/V_delta_cap028.json'))
g={int(q):1/(1-v) for q,v in d.items() if int(q)>=5}
rc={int(k):v for k,v in json.load(open('verdict3/V_rcyc.json')).items()}
CORR=1.0000250822246777; RC=max(rc.values())*CORR
best=(0,0); SEG=10**7
for lo in range(E0+1,TOP,SEG):
    hi=min(lo+SEG,TOP); prod=np.ones(hi-lo)
    for q,gq in g.items():
        if q<hi: prod[(-lo)%q::q]*=gq
    e=np.arange(lo,hi,dtype=np.int64); gc=np.gcd(e,144)
    r=np.zeros(hi-lo)
    for k,v in rc.items(): r[gc==k]=v*CORR
    rho=r*prod/e; i=int(rho.argmax())
    if rho[i]>best[0]: best=(float(rho[i]),int(e[i]))
gm=max(g.values()); P=1; tb=0
for q in [5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61]:
    P*=q; tb=max(tb,RC*gm**len(str(0))*0+RC*gm**([5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61].index(q)+1)/max(P,TOP))
print("max rho on (%d,%d]: %.5e at e=%d ; tail e>%d <= %.2e"%(E0,TOP,best[0],best[1],TOP,tb))
