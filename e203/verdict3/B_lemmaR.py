# Numerical sanity check of Lemma R / pair-correlation lemma (B_noside.md, section 3).
# F(i,j) = prod_{p>=5, p | (2^i 3^j - 1) (numerator)} (1+1/(p-2)), truncated at p<=Z (tail from p>Z is <1e-3, see text).
# Reports (1/N^2) * sum_{|i|,|j|<=N, (i,j)!=0} F(i,j) for several N. Lemma R predicts boundedness in N.
import numpy as np, sys
from sympy import primerange
Z=int(sys.argv[1]) if len(sys.argv)>1 else 100000
Ns=[10,20,40,80]
Nmax=max(Ns)
I=np.arange(-Nmax,Nmax+1)
logF=np.zeros((2*Nmax+1,2*Nmax+1))
hits_total=np.zeros_like(logF)
S1=0.0
for p in primerange(5,Z):
    # 2^i mod p and 3^j mod p for i in [-Nmax,Nmax]
    inv2=pow(2,-1,p); inv3=pow(3,-1,p)
    def tab(g,gi):
        t=np.empty(2*Nmax+1,dtype=np.int64)
        t[Nmax]=1
        x=1
        for k in range(1,Nmax+1):
            x=x*g%p; t[Nmax+k]=x
        x=1
        for k in range(1,Nmax+1):
            x=x*gi%p; t[Nmax-k]=x
        return t
    t2=tab(2,inv2); t3=tab(3,inv3)
    M=(np.outer(t2,t3)%p)==1
    logF+=M*np.log1p(1.0/(p-2))
F=np.exp(logF)
for N in Ns:
    sub=F[Nmax-N:Nmax+N+1,Nmax-N:Nmax+N+1].copy()
    sub[N,N]=0.0
    print(f"N={N:3d}  cells={(2*N+1)**2-1:6d}  mean F={sub.sum()/((2*N+1)**2-1):.5f}  max F={sub.max():.3f}")
