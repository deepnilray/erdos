# Independent check of C's "max compatible mass" for common-discrete-log families. Own pool via sympy n_order, own B&B (different branching: by T-class).
import math, sys, time
from sympy import primerange, n_order
def fam(E):
    out=[]
    for p in primerange(5,10**7):
        pass
    return out
# primes p with 3 in <2> and ord_p(2)=o<=E: p | 2^o-1; enumerate by factoring 2^o-1 for o<=E
from sympy import factorint, divisors
E=int(sys.argv[1]); 
seen={}
for o in range(2,E+1):
    for p in factorint(2**o-1):
        if p>3 and p not in seen:
            if n_order(2,p)==o:
                # is 3 in <2>? discrete log by brute force over powers of 2
                x=1; t=None
                for j in range(o):
                    if x==3%p: t=j;break
                    x=x*2%p
                if t is not None: seen[p]=(o,t)
F=sorted((o,t,p) for p,(o,t) in seen.items())
print("primes with 3 in <2>, ord2<=%d: %d, sum 1/o = %.4f"%(E,len(F),sum(1/o for o,t,p in F)))
# B&B over families: pick prime, intersect congruence; bound = current + sum of remaining weights of compatible
best=[0,None]; w=[1/o for o,t,p in F]
def compat(T,M,o,t):
    g=math.gcd(M,o); return (T-t)%g==0
def merge(T,M,o,t):
    g=math.gcd(M,o); m1=M//g; m2=o//g
    k=((t-T)//g*pow(m1,-1,m2))%m2 if m2>1 else 0
    return (T+M*k)%(M*m2), M*m2
def rec(idx,cands,T,M,cur,chosen):
    if cur>best[0]: best[0]=cur;best[1]=list(chosen)
    rest=sum(w[i] for i in cands)
    for pos,i in enumerate(cands):
        if cur+sum(w[j] for j in cands[pos:])<=best[0]+1e-12: return
        o,t,p=F[i]; T1,M1=merge(T,M,o,t)
        nc=[j for j in cands[pos+1:] if compat(T1,M1,F[j][0],F[j][1])]
        chosen.append(p); rec(i,nc,T1,M1,cur+w[i],chosen); chosen.pop()
t0=time.time(); rec(0,list(range(len(F))),0,1,0.0,[])
print("E=%d max compatible mass %.5f (%d primes) %.1fs"%(E,best[0],len(best[1]),time.time()-t0), best[1][:15])
# control: brute-force over T mod lcm for tiny E
if len(sys.argv)>2:
    L=1
    for o,t,p in F: L=math.lcm(L,o)
    print("lcm",L)
    if L<=3*10**6:
        bm=0
        for T in range(L):
            s=sum(1/o for o,t,p in F if (T-t)%o==0)
            bm=max(bm,s)
        print("direct max over T mod lcm:",bm)
