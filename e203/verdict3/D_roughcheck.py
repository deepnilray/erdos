# D_roughcheck.py: control for the rough-number second moment.  R_z(m)=#{(k,l) in [1,N]^2 : 2^k 3^l m+1 has no prime factor p, 5<=p<z}.
# For fixed z this is a periodic function of m, so E[R_z^2]/E[R_z]^2 is predicted EXACTLY (sampling error aside) by
#   1/E + (sum_{u!=u'} W(u,u'))/(sum_u W_u)^2 ,  W(u,u')=prod_{5<=p<z}(1-nu_p/p), W_u=prod(1-1/p)   (nu_p=1 if p | A_u'-A_u else 2).
import numpy as np, random, sys
from sympy import primerange
N=int(sys.argv[1]); z=int(sys.argv[2]); M=int(sys.argv[3]); random.seed(7)
P=list(primerange(5,z))
T2={};T3={}
for p in P:
    a=np.empty(N,dtype=np.int64);b=np.empty(N,dtype=np.int64);x=1;y=1
    for i in range(N): x=x*2%p;y=y*3%p;a[i]=x;b[i]=y
    T2[p]=a;T3[p]=b
Rs=[]
for _ in range(M):
    while True:
        m=random.randrange(10**9,10**13)
        if m%2 and m%3: break
    alive=np.ones((N,N),dtype=bool)
    for p in P:
        if m%p==0: continue
        alive&=~((np.outer(T2[p],T3[p])%p)==(-pow(m,-1,p))%p)
    Rs.append(alive.sum())
Rs=np.array(Rs,float); E=Rs.mean(); V=Rs.var()
# prediction
Dn=2*N-1; I=np.arange(-(N-1),N)
logW=np.zeros((Dn,Dn)); logW1=0.0
for p in P:
    t=lambda g:(lambda gi:(np.array([pow(g,k,p) if k>=0 else pow(gi,-k,p) for k in map(int,I)])))(pow(g,-1,p))
    Mx=(np.outer(t(2),t(3))%p)==1
    logW+=np.where(Mx,np.log(1-1/p),np.log(1-2/p)); logW1+=np.log(1-1/p)
w=np.outer(N-np.abs(I),N-np.abs(I)).astype(float); w[N-1,N-1]=0
pairs=(w*np.exp(logW)).sum(); first=N*N*np.exp(logW1)
EP=first*1.0  # expected R (per m coprime to 6)
pred_E2=EP + pairs
print("N",N,"z",z,"M",M,"mean R",E,"pred",EP," E[R^2] obs",(Rs**2).mean(),"pred",pred_E2," Var/E^2 obs",V/E**2,"pred",pred_E2/EP**2-1)
