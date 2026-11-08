from fractions import Fraction as F
import sys
N=int(sys.argv[1])
def fac(m):
    f={};p=2
    while p*p<=m:
        while m%p==0:f[p]=f.get(p,0)+1;m//=p
        p+=1
    if m>1:f[m]=f.get(m,0)+1
    return f
sv=bytearray([1])*(N+1);sv[0]=sv[1]=0
for i in range(2,int(N**.5)+1):
    if sv[i]:sv[i*i::i]=bytearray(len(sv[i*i::i]))
bad=mx=0
for n in (i for i in range(2,N+1) if sv[i]):
    ok=0
    for x in range(n//4+1,3*n//4+2):
        a=4*x-n;b=n*x
        ds=[1]
        for p,e in fac(b).items():ds=[d*p**k for d in ds for k in range(2*e+1)]
        for d in ds:
            if d<=b and (b+d)%a==0:
                y=(b+d)//a;z=(b+b*b//d)//a
                assert F(1,x)+F(1,y)+F(1,z)==F(4,n);ok=1;mx=max(mx,x-n//4-1);break
        if ok:break
    if not ok:bad+=1;print("fail",n)
print("exact-verified primes<=",N,"fails",bad,"max offset",mx)
