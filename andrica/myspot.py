#!/usr/bin/env python3
# Independent pointwise spot-check of certified cells. Own derivation of the inequality lists.
# Usage: python3 myspot.py SEED NCELLS NPOINTS   (paper, Controls (2): python3 myspot.py 1 100000 1500)
# Checks T400_0575M.txt (main grid) and Z400_0575.txt (zeta grid) at r = 0.0575.
import sys, itertools, numpy as np
S=''  # run from the bundle directory
r=0.0575; t=0.5; DEL=1e-6; W=np.arange(1,31)[:,None]
rng=np.random.default_rng(int(sys.argv[1]) if len(sys.argv)>1 else 1)
NC=int(sys.argv[2]) if len(sys.argv)>2 else 300; NP=int(sys.argv[3]) if len(sys.argv)>3 else 4000
def load(f): return {int(a):b for a,b in (l.split() for l in open(S+f))}
def lv(l,v):  # best of Huxley/GM over powers w<=30, and trivial
    L=W*l; V=W*v
    h=np.maximum(2*L-2*V, t+np.minimum(L-2*V,4*L-6*V))
    g=np.maximum(np.maximum(2*L-2*V,3.6*L-4*V), t+2.4*L-4*V)
    return np.minimum(np.minimum(h.min(0),g.min(0)), t)
def pts(i,j,N,zeta):
    a=(i+rng.random(NP))/N; c=(j+rng.random(NP))/N
    a[:4]=[i/N,i/N,(i+1)/N,(i+1)/N]; c[:4]=[j/N,(j+1)/N,j/N,(j+1)/N]
    b=1-a-c; k=b>=0; a,b,c=a[k],b[k],c[k]; L=[a,b,c]; V=[]
    for n,l in enumerate(L):
        hi=0.8*l
        if zeta and n==0: hi=np.minimum(hi,l/2+1/12)
        u=rng.random(l.size); u=np.where(rng.random(l.size)<0.7, 1-0.15*u, u)  # bias to top
        u=np.where(rng.random(l.size)<0.1, 1.0, u)
        V.append(-1+(hi+1)*u)
    return L,V
def T_ok(L,V,K=3):
    bd=np.minimum.reduce([lv(l,v) for l,v in zip(L,V)])
    vF=sum(V); best=sum(l-v for l,v in zip(L,V))
    for X in range(3):
        o=[k for k in range(3) if k!=X]
        best=np.maximum(best,np.minimum(sum(2*L[k]-2*V[k] for k in o), .5+r+sum(L[k]-2*V[k] for k in o)))
    for ks in itertools.product(range(K+1),repeat=3):
        q=sum(k*l for k,l in zip(ks,L)); vQ=sum(k*v for k,v in zip(ks,V))
        best=np.maximum(best,np.minimum(2-2*q-2*vF+2*vQ, 1.5+r-q-2*vF+2*vQ))
    return bd<=best-DEL
def Z_ok(L,V):
    z,b,c=L; vZ=V[0]
    bd=np.minimum.reduce([lv(l,v) for l,v in zip(L,V)]+[.5+2*z-4*vZ, 1+6*z-12*vZ])
    J={2:.5+z,4:.5+2*z,12:1+6*z}; J[6]=.75*J[4]+.25*J[12]; J[8]=.5*J[4]+.5*J[12]
    ok=np.zeros(z.size,bool)
    for Mm in (0,1,2):
      for X in range(8):
        if (Mm==0 and X) or X==7: continue
        x=sum(L[i] for i in range(3) if X>>i&1)+0*z
        if Mm==0: wt0,Lm=0.0,r+0*z
        elif Mm==1: wt0,Lm=.5,np.maximum(2*x+2*r,x+r+.5)/2
        else: wt0,Lm=.25,(2*r+np.maximum(4*x+2*r,2*x+r+.5))/4
        zo=[(0,0*z)] if X&1 else [(0,vZ)]+[(1/p,J[p]/p) for p in (2,4,6,8,12)]
        yo=lambda i: [(0,0*z)] if X>>i&1 else [(0,V[i])]+[(1/(2*k),(np.maximum(.5,k*L[i])+k*L[i])/(2*k)) for k in (1,2,3)]
        for (wz,cz),(wb,cb),(wc,cc) in itertools.product(zo,yo(1),yo(2)):
            wt=wt0+wz+wb+wc
            if wt>1+1e-12: continue
            tot=Lm+cz+cb+cc; a=1-wt
            ok|= (a*bd+tot<=1+r-DEL) if a>1e-12 else (tot<=1+r-DEL)
    return ok
def run(f,zeta,N):
    rows=load(f); cells=[(i,j) for i,s in rows.items() for j,ch in enumerate(s) if ch=='1' and i+j<N-1]
    if zeta: cells=[(i,j) for i,j in cells if i>=N//4 and i+1<=N//2]
    pick=[cells[k] for k in rng.choice(len(cells),min(NC,len(cells)),replace=False)]
    bad=0;n=0
    for i,j in pick:
        L,V=pts(i,j,N,zeta); ok=(Z_ok if zeta else T_ok)(L,V); n+=ok.size
        if not ok.all():
            bad+=1; k=np.argmin(ok); print('FAIL',f,i,j,[float(x[k]) for x in L+V])
    print(f,'cells',len(cells),'sampled',len(pick),'points',n,'failing cells',bad)
run('T400_0575M.txt',False,400)
run('Z400_0575.txt',True,400)
# controls: known-bad points must fail
print('ctrl T', T_ok([np.array([1/3])]*3,[np.array([.26])]*3), 'ctrl Z', Z_ok([np.array([.26]),np.array([.37]),np.array([.37])],[np.array([.21]),np.array([.29]),np.array([.29])]))
# negative controls: '0' cells should mostly show failing points
for f,zeta in (('T400_0575M.txt',False),('Z400_0575.txt',True)):
    rows=load(f); z=[(i,j) for i,s in rows.items() for j,ch in enumerate(s) if ch=='0' and i+j<399]
    pick=[z[k] for k in rng.choice(len(z),100,replace=False)]; nf=0
    for i,j in pick:
        L,V=pts(i,j,400,zeta); nf+= not (Z_ok if zeta else T_ok)(L,V).all()
    print('neg control',f,'0-cells with a failing point:',nf,'/100')
