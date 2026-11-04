# D_nucheck.py: control for D_classes.py at w=31: sample random m coprime to 6, compute nu(m) directly from residues
# (cell (i,j) in a full period of H killed by p iff 2^i 3^j m + 1 = 0 mod p, computed with pow, independent of the log tables).
import numpy as np, random, sys
from sympy import primerange, n_order
from math import gcd
w=int(sys.argv[2]) if len(sys.argv)>2 else 31; P=list(primerange(5,w)); random.seed(3)
z=np.load("D_data/nu_w%d.npz"%w); nu=z['nu']; mu=z['mu']; cdf=np.cumsum(mu)
W=1
for p in P: W*=p
# period lattice: i mod L2=lcm ord_p 2, j mod L3 = lcm ord_p 3 ; nu = fraction of surviving cells over the full torus Z/L2 x Z/L3
L2=1;L3=1
for p in P:
    a=n_order(2,p);b=n_order(3,p);L2=L2*a//gcd(L2,a);L3=L3*b//gcd(L3,b)
i=np.arange(L2); j=np.arange(L3)
pw2={p:np.array([pow(2,int(k),p) for k in i]) for p in P}; pw3={p:np.array([pow(3,int(k),p) for k in j]) for p in P}
vals=[]
for _ in range(int(sys.argv[1])):
    m=random.randrange(10**12,10**13)
    if m%2==0 or m%3==0: continue
    alive=np.ones((L2,L3),dtype=bool)
    for p in P:
        if m%p==0: continue
        t=(-pow(m,-1,p))%p
        # 2^i 3^j = t  <=> 3^j = t*2^{-i}
        need=(t*np.array([pow(int(x),-1,p) for x in pw2[p]]))%p
        alive&=~(need[:,None]==pw3[p][None,:])
    vals.append(alive.mean())
vals=np.array(vals)
print("L2,L3",L2,L3,"samples",len(vals),"mean",vals.mean(),"exact mean",(nu*mu).sum(),"min sample",vals.min(),"exact min",nu[mu>0].min())
for q in (0.01,0.1,0.5,0.9):
    print(" quantile",q,"sample",np.quantile(vals,q),"exact",nu[np.searchsorted(cdf,q)])
