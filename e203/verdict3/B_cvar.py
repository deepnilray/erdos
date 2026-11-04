# Second-moment barrier: how large can a Cauchy-Schwarz bound over m be, even with perfect pair-correlation asymptotics?
# C_ind(m) = 3 prod_{5<=p<=Z} (1-delta_p/e_p)/(1-1/p), delta_p = [(-m)^{e_p}==1 mod p]  (independence Euler product, h_model.py convention)
import random, math
from sympy import primerange, n_order
random.seed(20261023)
Z=3000
P=[p for p in primerange(5,Z)]
E=[]
for p in P:
    o2=n_order(2,p); o3=n_order(3,p); E.append(o2*o3//math.gcd(o2,o3))
base=sum(math.log(1/(1-1/p)) for p in P)
def C(m):
    s=math.log(3)+base
    for p,e in zip(P,E):
        if m%p and pow((-m)%p,e,p)==1: s+=math.log1p(-1/e)
    return math.exp(s)
Cs=[]
while len(Cs)<20000:
    m=random.randrange(10**9,10**10)
    if m%2 and m%3: Cs.append(C(m))
mean=sum(Cs)/len(Cs); m2=sum(c*c for c in Cs)/len(Cs)
Cs.sort()
print("n",len(Cs),"mean C",round(mean,4),"E[C^2]/E[C]^2",round(m2/mean**2,4),"=> ideal CS ratio E[C]^2/E[C^2]",round(mean**2/m2,4),"min",round(Cs[0],3),"max",round(Cs[-1],3))
