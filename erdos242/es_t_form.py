"""Lemma B check: p=1 mod 4 prime is in the (m,u,t) family iff some t=3 mod 4 and divisor a of p*t+1
with 4|a, a=-1 (mod t), a<p*t+1 ... then m=(a+1)/t, u=(b+1)/t, b=(p*t+1)/a.  Independent search over t."""
import sys
from sympy import primerange, divisors
from fractions import Fraction
HARD={1,121,169,289,361,529}
def t_search(p,Tmax):
    for t in range(3,Tmax+1,4):
        N=p*t+1
        for a in divisors(N):
            if a%4==0 and (a+1)%t==0:
                b=N//a
                if (b+1)%t==0:
                    m=(a+1)//t; u=(b+1)//t
                    if m>=1 and u>=1:
                        assert m*u*t-m-u==p and (m*t)%4==1
                        w=a//4; X=u*t-1
                        assert Fraction(1,u*w)+Fraction(1,p*w*X)+Fraction(1,u*w*X)==Fraction(4,p)
                        return t,m,u
    return None
N=int(sys.argv[1]);T=int(sys.argv[2])
miss=[];mx=(0,0);n=0
for p in primerange(11,N):
    if p%840 in HARD:
        r=t_search(p,T);n+=1
        if r is None: miss.append(p)
        elif r[0]>mx[0]: mx=(r[0],p,r)
print("primes",n,"no hit with t<=%d:"%T,len(miss),miss[:10],"max min-t",mx)
# control: p=2 mod 3 style prime not 1 mod 4 must fail the 4|a requirement
print("control p=7 (3 mod 4):",t_search(7,200))
