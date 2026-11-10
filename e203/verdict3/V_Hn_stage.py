# Stage-level pointwise form of A's (H_n): sum_{p in stage l, e_p in window} Lam/e <= kappa * model, checked on the pool window (4e5,8e5].
import json, math, numpy as np
from collections import Counter, defaultdict
from sympy import factorint
E0=800000; LO=400000; tau=0.813/math.log(E0)
z=np.load('stages_E800000.npz'); dv=dict(zip(map(int,z['ells']),np.minimum(z['dv'],0.5)))
g=lambda q: 1.0/(1.0-dv[q]) if (q in dv and q>=5) else 1.0
n=Counter(json.loads(l)['e'] for l in open('../poolE800000.jsonl'))
R=defaultdict(float); M=defaultdict(float)
for e in range(LO+1,E0+1):
    f=factorint(e); l=max(f); ph=1; G=1.0
    for q,a in f.items(): ph*=q**(a-1)*(q-1); G*=g(q)
    if l<5: continue
    R[l]+=n.get(e,0)*G/e; M[l]+=tau*G/ph
for lo,hi in [(5,30),(30,100),(100,1000),(1000,10000),(10000,100000),(100000,800001)]:
    ls=[l for l in M if lo<=l<hi]
    tot_r=sum(R[l] for l in ls); tot_m=sum(M[l] for l in ls)
    over=[l for l in ls if R[l]>1.5*M[l]]; 
    print("l in [%d,%d): stages %d, aggregate ratio %.2f, stages with realised > 1.5*model: %d (%.1f%%), max stage ratio %.1f"%(lo,hi,len(ls),tot_r/tot_m,len(over),100*len(over)/len(ls),max(R[l]/M[l] for l in ls)))
print("sum of squares (what the quadratic stage cost sees), realised / model:")
for lo,hi in [(30,100),(100,1000),(1000,10000),(10000,100000),(100000,800001)]:
    ls=[l for l in M if lo<=l<hi]
    print("  l in [%d,%d): sum R^2 = %.3e   sum M^2 = %.3e   ratio %.2f"%(lo,hi,sum(R[l]**2 for l in ls),sum(M[l]**2 for l in ls),sum(R[l]**2 for l in ls)/sum(M[l]**2 for l in ls)))
