# Independent recomputation of D's rho = lim E[pair term]/E[first]^2 for the rough-number second moment.
import numpy as np, sys
from sympy import primerange
N=int(sys.argv[1]); PM=int(sys.argv[2])
I=np.arange(-(N-1),N)
logF=np.zeros((2*N-1,2*N-1)); prodlead=1.0
for p in primerange(5,PM):
    prodlead*=1-1/(p-1)**2
    # table 2^i mod p for i in [-(N-1),N-1]
    i2=pow(2,-1,p); i3=pow(3,-1,p)
    def tab(b,ib):
        t=np.empty(2*N-1,dtype=np.int64); x=1
        for k in range(N): t[N-1+k]=x; x=x*b%p
        x=1
        for k in range(N): t[N-1-k]=x; x=x*ib%p
        return t
    t2=tab(2,i2); t3=tab(3,i3)
    hit=((t2[:,None]*t3[None,:])%p==1)
    logF+=hit*np.log1p(1/(p-2))
F=np.exp(logF)
w=np.add.outer(np.zeros(2*N-1),np.zeros(2*N-1))
wi=(N-np.abs(I)).astype(float)
W=wi[:,None]*wi[None,:]; W[N-1,N-1]=0   # u != u'
meanF=(W*F).sum()/W.sum()
print("N=%d p<%d: prod_{p>=5}(1-1/(p-1)^2)=%.5f  meanF=%.5f  rho=%.5f"%(N,PM,prodlead,meanF,prodlead*meanF))
# planted control: drop the lattice (pretend F=1): rho must equal prod only
print("control (independent cells, F=1): rho=%.5f"%prodlead)
