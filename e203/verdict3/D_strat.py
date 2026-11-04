# D_strat.py: does stratifying m by residue mod W=prod_{5<=p<w}p remove the 0.027 variance?  Same R_z as D_roughcheck.
import numpy as np, random, sys
from sympy import primerange
N=int(sys.argv[1]); w=int(sys.argv[2]); z=int(sys.argv[3]); M=int(sys.argv[4]); NR=int(sys.argv[5]); random.seed(11)
P=list(primerange(5,z)); small=[p for p in P if p<w]
W=1
for p in small: W*=p
T2={};T3={}
for p in P:
    a=np.empty(N,dtype=np.int64);b=np.empty(N,dtype=np.int64);x=1;y=1
    for i in range(N): x=x*2%p;y=y*3%p;a[i]=x;b[i]=y
    T2[p]=a;T3[p]=b
def R(m):
    alive=np.ones((N,N),dtype=bool)
    for p in P:
        if m%p==0: continue
        alive&=~((np.outer(T2[p],T3[p])%p)==(-pow(m,-1,p))%p)
    return alive.sum()
tot=[]
for _ in range(NR):
    r=random.randrange(W)
    Rs=[]
    while len(Rs)<M:
        m=r+W*random.randrange(10**4,10**9)
        if m%2==0 or m%3==0: continue
        Rs.append(R(m))
    Rs=np.array(Rs,float); print("class",r,"mean",Rs.mean(),"Var/E^2",Rs.var()/Rs.mean()**2,flush=True)
