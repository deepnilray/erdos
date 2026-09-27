# Exact min mean cycle via Howard-like approach: value iteration then follow greedy policy to find cycle.
import sys, math
from math import gcd
y=int(sys.argv[1]); Emax=int(sys.argv[2]); T=int(sys.argv[3])
P=1
for p in [2,3,5,7,11,13]:
    if p<=y: P*=p
unit=[gcd(i,P)==1 for i in range(P)]
H=P//2
INF=float('inf')
import array
f=[0.0 if unit[s] else INF for s in range(P) for h in range(H)]
def nxt(s,h):
    d=2*h
    out=[]
    for e in range(0,Emax+1,2):
        if e==0 and d==0: continue
        d2=(d+e)%P; s2=(s+d2)%P
        if unit[s2]: out.append((e,s2*H+d2//2))
    return out
adj=[nxt(i//H,i%H) if unit[i//H] else [] for i in range(P*H)]
for t in range(T):
    g=[min((e+f[j] for e,j in adj[i]),default=INF) for i in range(P*H)]
    m=min(g); f=[x-m for x in g]
# greedy policy
pol=[min(adj[i],key=lambda ej: ej[0]+f[ej[1]]) if adj[i] else None for i in range(P*H)]
# find cycle from argmin state
i=min(range(P*H),key=lambda k:f[k])
seen={}
path=[]
while i not in seen:
    seen[i]=len(path); path.append(i); i=pol[i][1]
cyc=path[seen[i]:]
es=[pol[k][0] for k in cyc]
print("cycle length",len(cyc),"total e",sum(es),"mean",sum(es)/len(cyc))
print("e seq:",es[:200])
print("d seq:",[2*(k%H) for k in cyc][:200])
