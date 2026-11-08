import random, sys, time
from sympy import nextprime, factorint, divisors
from fractions import Fraction
HARD={1,121,169,289,361,529}
def fam_u(p,Umax):
    for u in range(1,Umax+1):
        P=p+u
        f=factorint(P)
        ds=[1]
        for q,e in f.items(): ds=[d*q**k for d in ds for k in range(e+1)]
        for m in ds:
            if m%4!=3 or m>=p: continue
            c=P//m
            if (c+1)%u==0:
                t=(c+1)//u
                if t%4==3: return u,m,t
    return None
random.seed(20261108)
for digits in (12,15,18):
    lo=10**(digits-1); n=0; worst=0; miss=0; t0=time.time()
    while n<40 and time.time()-t0<150:
        x=random.randrange(lo,10*lo)
        p=nextprime(x)
        if p%840 not in HARD: continue
        r=fam_u(p,3000); n+=1
        if r is None: miss+=1; print("MISS",p); continue
        u,m,t=r; w=(m*t-1)//4; X=u*t-1
        assert m*u*t-m-u==p
        assert Fraction(1,u*w)+Fraction(1,p*w*X)+Fraction(1,u*w*X)==Fraction(4,p)
        worst=max(worst,u)
    print(digits,"digits: hard primes tested",n,"misses",miss,"worst min-u",worst,flush=True)
# control: composite-ish planted failure, p=7 mod 4 class must not be reported
print("control p=1000003 (3 mod 4):",fam_u(1000003,200))
