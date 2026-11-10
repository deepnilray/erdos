# D_rho.py: rho = mean over ordered pairs u!=u' in box [1,N]^2 of G(u,u') = prod_{5<=p<Z} (1-nu_p/p)/(1-1/p)^2, nu_p=1 if p | A_u'-A_u else 2.
# This is the exact ideal (HL) value of E[R^2]/E[R]^2 (pairs part) in the Cauchy-Schwarz/Chebyshev argument; mean over m of local factor is 1 per cell.
import numpy as np, sys
from sympy import primerange
N=int(sys.argv[1]); Z=int(sys.argv[2])
I=np.arange(-(N-1),N)
logG=np.zeros((2*N-1,2*N-1))
for p in primerange(5,Z):
    def tab(g):
        t=np.empty(2*N-1,dtype=np.int64); gi=pow(g,-1,p); t[N-1]=1; x=1
        for k in range(1,N): x=x*g%p; t[N-1+k]=x
        x=1
        for k in range(1,N): x=x*gi%p; t[N-1-k]=x
        return t
    M=(np.outer(tab(2),tab(3))%p)==1
    a=np.log((1-1/p)/(1-1/p)**2); b=np.log((1-2/p)/(1-1/p)**2)
    logG+=np.where(M,a,b)
G=np.exp(logG)
w=np.outer(N-np.abs(I),N-np.abs(I)).astype(float); w[N-1,N-1]=0
print("N",N,"Z",Z,"rho",(w*G).sum()/w.sum())
