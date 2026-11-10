# Independent spot-check of a coverage table: random points in covered cells must admit a certificate.
import random, sys
import numpy as np
R=float(sys.argv[2]); t=0.5; W=30
rows=[l.split()[1] for l in open(sys.argv[1])]; N=len(rows)
cells=[(i,j) for i in range(N) for j in range(N) if i+j<N-1 and rows[i][j]=='1']
random.seed(7); bad=0; tested=0
ws=np.arange(1,W+1)
def cert(l,v):
    best=t
    for i in range(3):
        L=ws*l[i]; V=ws*v[i]
        hux=np.maximum(2*L-2*V, t+np.minimum(L-2*V,4*L-6*V))
        gm=np.maximum.reduce([2*L-2*V,3.6*L-4*V,t+2.4*L-4*V])
        best=min(best,hux.min(),gm.min())
    r=[sum(l[i]-v[i] for i in range(3))]
    for X in range(3):
        o=[i for i in range(3) if i!=X]
        r.append(min(sum(2*l[i]-2*v[i] for i in o),0.5+R+sum(l[i]-2*v[i] for i in o)))
    return best <= max(r)
for (i,j) in random.sample(cells, min(3000,len(cells))):
    for _ in range(40):
        a=(i+random.random())/N; c=(j+random.random())/N; b=1-a-c
        if b<=0: continue
        l=(a,b,c); v=[random.uniform(-1,0.8*x) for x in l]
        tested+=1
        if not cert(l,v): bad+=1; print("FAIL",l,v); break
print(sys.argv[1],"covered cells",len(cells),"points tested",tested,"failures",bad)
# planted control: known-uncovered point must fail
print("control balanced point certifies?", cert((1/3,1/3,1/3),(0.21,0.21,0.21)))
