import json, sys, random, numpy as np
from math import gcd
D=int(sys.argv[1]); N=(1<<D)-1; passes=int(sys.argv[2])
P=json.load(open('ffpool15.json'))
def mul(a,b,pi,d):
    r=0
    while b:
        if b&1: r^=a
        b>>=1; a<<=1
        if a>>d&1: a^=pi
    return r
forms=[]
for pi,d,e in P:
    if N%e: continue
    o=(1<<d)-1
    # find primitive element by trial, build log table
    for g in range(2,1<<d):
        x=1; seen=0; log={}
        for i in range(o):
            log[x]=i; x=mul(x,g,pi,d)
            if x==1 and i<o-1: break
        else:
            if len(log)==o: break
    a=log[2]; b=log[3]; g0=gcd(gcd(a,b),o)
    assert o//g0==e,(o,g0,e)
    forms.append((a//g0 % e, b//g0 % e, e))
print("primes used",len(forms),"budget",sum(1/e for *_,e in forms),flush=True)
K=np.arange(N,dtype=np.int64)
kk=K[:,None]; ll=K[None,:]
cover=np.zeros((N,N),dtype=np.int16)
off=[0]*len(forms)
def f(a,b,e): return ((a*kk+b*ll)%e).astype(np.int32)
order=sorted(range(len(forms)),key=lambda i:forms[i][2])
for i in order:   # greedy init
    a,b,e=forms[i]; F=f(a,b,e); U=cover==0
    cnt=np.bincount(F[U],minlength=e); c=int(cnt.argmax()); off[i]=c
    cover+=(F==c)
print("greedy uncovered fraction",(cover==0).mean(),flush=True)
best=(cover==0).mean()
for ps in range(passes):
    idx=list(range(len(forms))); random.shuffle(idx)
    for i in idx:
        a,b,e=forms[i]; F=f(a,b,e)
        cover-=(F==off[i]); U=cover==0
        cnt=np.bincount(F[U],minlength=e); c=int(cnt.argmax()); off[i]=c
        cover+=(F==c)
    u=(cover==0).mean(); print("pass",ps,"uncovered",u,flush=True)
    if u==0: print("FULL COVER of Z_%d^2"%N); break
json.dump({"forms":forms,"off":off,"uncovered":float(u)},open(f'ffcover_{D}.json','w'))
