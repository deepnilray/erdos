# Independent sieve: e_p for every prime 5<=p<LIM from scratch (spf table, exact orders), compare with pool entries below LIM.
import numpy as np, json, math, sys
LIM=int(float(sys.argv[1]))
spf=np.zeros(LIM,dtype=np.int32)
for i in range(2,int(LIM**.5)+1):
    if spf[i]==0: 
        s=spf[i*i::i]; s[s==0]=i
isp=[p for p in range(5,LIM) if spf[p]==0]
def fac(n):
    f={}
    while n>1:
        q=int(spf[n]) or n
        f[q]=f.get(q,0)+1; n//=q
    return f
def order(a,p,f):
    o=p-1
    for q in f:
        while o%q==0 and pow(a,o//q,p)==1: o//=q
    return o
found={}
for p in isp:
    f=fac(p-1); e=math.lcm(order(2,p,f),order(3,p,f))
    if e<=800000: found[p]=e
pool={}
for l in open('../poolE800000.jsonl'):
    q=json.loads(l)
    if q['p']<LIM: pool[q['p']]=q['e']
print("primes scanned",len(isp),"with e<=8e5:",len(found),"pool entries below LIM:",len(pool),"equal:",found==pool)
# planted: remove one pool prime
k=next(iter(pool)); del pool[k]; print("planted deletion detected:",found!=pool)
