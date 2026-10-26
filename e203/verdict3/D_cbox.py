# D_cbox.py: exact box version of the second-moment loss. For random m coprime to 6, c(m)=mean over cells (k,l) in [1,N]^2
# of [cell survives all 5<=p<=Z] * prod (1-1/p)^{-1} (killed cell = weight 0).  Reports E[c^2]/E[c]^2 (the HL ideal Cauchy-Schwarz loss, no independence assumption across p).
import numpy as np, random, sys
from sympy import primerange
N=int(sys.argv[1]); Z=int(sys.argv[2]); M=int(sys.argv[3]); seed=int(sys.argv[4]) if len(sys.argv)>4 else 1
random.seed(seed)
P=list(primerange(5,Z))
T2={};T3={}
for p in P:
    a=np.empty(N,dtype=np.int64);b=np.empty(N,dtype=np.int64);x=1;y=1
    for i in range(N):
        x=x*2%p;y=y*3%p;a[i]=x;b[i]=y
    T2[p]=a;T3[p]=b
base=sum(np.log(1/(1-1/p)) for p in P)
cs=[]
while len(cs)<M:
    m=random.randrange(10**9,10**12)
    if m%2==0 or m%3==0: continue
    alive=np.ones((N,N),dtype=bool)
    for p in P:
        if m%p==0: continue
        tgt=(-pow(m,-1,p))%p
        killed=(np.outer(T2[p],T3[p])%p)==tgt
        alive&=~killed
    c=np.exp(base)*alive.mean()
    cs.append(c)
cs=np.array(cs)
print("N",N,"Z",Z,"M",M,"mean c",cs.mean(),"E[c^2]/E[c]^2",(cs**2).mean()/cs.mean()**2,"min",cs.min(),"max",cs.max())
