# Independent brute-force check of C's Lemma A: intersection of kernels contains a primitive vector <=> g_pq | D_pq for all pairs.
import random, math, itertools
random.seed(11)
mods=[2,3,4,5,6,8,9,10,12,15,16,18,20,24,30,36]
agree=0; dis=0; weak_dis=0; yes=0
def prim(a,b,n): return math.gcd(math.gcd(a,b),n)==1
for t in range(6000):
    k=random.choice([2,2,3,3,4])
    F=[]
    for _ in range(k):
        e=random.choice(mods)
        while True:
            a,b=random.randrange(e),random.randrange(e)
            if prim(a,b,e): break
        F.append((a,b,e))
    L=1
    for f in F: L=math.lcm(L,f[2])
    if L>240: continue
    # brute force: primitive residue vector in all kernels
    direct=any(math.gcd(math.gcd(x,y),L)==1 and all((a*x+b*y)%e==0 for a,b,e in F)
               for x in range(L) for y in range(L))
    crit=all(((a*d-b*c)%math.gcd(e,f))==0 for (a,b,e),(c,d,f) in itertools.combinations(F,2))
    yes+=direct
    if direct==crit: agree+=1
    else: dis+=1; print("DISAGREE",F,direct,crit)
    # control: weak criterion "kernel lines coincide mod each prime ell" (C says it disagrees)
print("families",agree+dis,"agree",agree,"disagree",dis,"(with primitive vector:",yes,")")
# planted failure: use criterion with gcd replaced by min(e) -> must disagree sometimes
bad=0;n=0
random.seed(5)
for t in range(3000):
    F=[]
    for _ in range(2):
        e=random.choice(mods)
        while True:
            a,b=random.randrange(e),random.randrange(e)
            if prim(a,b,e): break
        F.append((a,b,e))
    L=math.lcm(F[0][2],F[1][2])
    if L>240: continue
    direct=any(math.gcd(math.gcd(x,y),L)==1 and all((a*x+b*y)%e==0 for a,b,e in F) for x in range(L) for y in range(L))
    (a,b,e),(c,d,f)=F
    wrong=((a*d-b*c)%min(e,f)==0)
    n+=1; bad+=(wrong!=direct)
print("planted wrong criterion disagrees",bad,"of",n)
