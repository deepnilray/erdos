# D_W.py  w Y_used : rigorous-style bounds for the Romanoff-type constants used in §11.
#  H = <2,3> mod W, W=prod_{5<=p<w} p, reps (i,j), 0<=i<c, 0<=j<h, lattice basis (0,h),(c,jc).
#  For each prime q>=w (q<=Y): J_q = gcd(g, h*beta, c*alpha+jc*beta), g=gcd(e_q,E_w); K_q = {(i,j): i*alpha+j*beta = 0 mod J_q}.
#  Outputs: S1 = sum_{w<=q<=Y} g(q)/e_q ; tau = composite+tail bound (max-key method) ; Bmax = max_{psi!=1} B1(psi) ;
#           for w=31 also the W_5 decomposition  sum_q g(q)/e_q * mean_{K_q} F  (rho).
import numpy as np, math, sys
from math import gcd, log
w=int(sys.argv[1]); Y=int(float(sys.argv[2])); fn=sys.argv[3] if len(sys.argv)>3 else 'D_data/ep_1e8.bin'
dt=np.dtype([('q','<u4'),('e','<u4'),('o2','<u4'),('o3','<u4'),('G','<u2'),('a','<u2'),('b','<u2')])
D=np.fromfile(fn,dtype=dt); D=D[D['q']<=Y]
small=D[D['q']<w]; big=D[D['q']>=w]
P=[int(x) for x in small['q']]
E=1
for e in small['e']: E=E*int(e)//gcd(E,int(e))
# lattice of W
h=1
for o in small['o3']: h=h*int(o)//gcd(h,int(o))
al={int(r['q']):int(r['a']) for r in small}; be={int(r['q']):int(r['b']) for r in small}; ee={int(r['q']):int(r['e']) for r in small}
def inLam(i,j): return all((i*al[p]+j*be[p])%ee[p]==0 for p in P)
c=None
for cc in range(1,10**6):
    js=[j for j in range(h) if inLam(cc,j)]
    if js: c=cc; jc=js[0]; break
Hs=c*h
print(f"w={w} primes<w={P} E={E} |H|={Hs} c={c} h={h} jc={jc}",flush=True)
# F on H reps
I=np.repeat(np.arange(c),h); Jj=np.tile(np.arange(h),c)
logF=np.zeros(Hs)
for p in P:
    logF+=((I*al[p]+Jj*be[p])%ee[p]==0)*math.log1p(1/(p-2))
F=np.exp(logF); A1=F.mean(); Fmax=F.max()
# q data
q=big['q'].astype(np.int64); e=big['e'].astype(np.int64); G=big['G'].astype(np.int64)
g=np.gcd(e,E); a=big['a'].astype(np.int64)%g; b=big['b'].astype(np.int64)%g
Jq=np.gcd(np.gcd(g,(h*b)%g),(c*a+jc*b)%g)
Jq=np.where(Jq==0,g,Jq)  # gcd(g,0)=g handled
wq=1.0/((q-2)*e.astype(float))
S1=wq.sum()
print(f"S1=sum g/e over {w}<=q<={Y}: {S1:.8f};  #q with J>1: {(Jq>1).sum()}  sum_{{J>1}} g/e = {wq[Jq>1].sum():.8f}",flush=True)
# ---- U(y): bound for sum_{q>Y, e_q<=y} 1/(q-2) ----
lnY=log(Y)
def U(y):
    y=float(y)
    logM=math.log(y)+math.log(y+1)+math.log(math.log(2)/2)   # log of log prod_{t<=y}(2^t-1) bound M
    b1=math.exp(min(logM,700))/lnY/(Y-2)
    lnQ=float(np.logaddexp(logM,math.log(1.01624*Y)))
    for _ in range(60): lnQ=float(np.logaddexp(logM,math.log(1.01624*Y)))-math.log(1-1/lnQ)
    b2=(math.log(lnQ/lnY)+1/lnY**2+1/(2*lnQ**2))*(1+3/Y)
    return min(b1,b2)
# ---- max-key composite bound ----
order=np.lexsort((q,e))
lg=np.log1p(1.0/(q-2))
cum=np.concatenate([[0.0],np.cumsum(lg[order])[:-1]])
Uv=np.array([U(int(x)) for x in np.unique(e)]); ue=np.unique(e)
Ue=Uv[np.searchsorted(ue,e)]
Pikey=np.empty(len(q)); Pikey[order]=np.exp(cum)
Pikey*=np.exp(Ue)
comp=(wq*(Pikey-1)).sum()
# ---- tail p>Y: sum_y U(y)(F(y)-F(y+1)), F decreasing envelope of Pibar(y)/y, Pibar(y)=prod_{known e_q<=y}(1+g) * exp(U(y))
es=np.sort(e); lgs=np.cumsum(lg[np.argsort(e,kind='stable')])
def logPiknown(y):
    k=np.searchsorted(es,y,side='right'); return lgs[k-1] if k>0 else 0.0
grid=np.unique(np.concatenate([np.arange(1,2000),np.geomspace(2000,1e15,4000).astype(np.int64)]))
grid=np.append(grid.astype(float),[1e20,1e40,1e80,1e160,1e300])
Pib=np.array([math.exp(logPiknown(min(y,1e18))+U(y)) for y in grid])
fup=np.empty(len(grid)); fup[:-1]=Pib[1:]/grid[:-1]; fup[-1]=Pib[-1]/grid[-1]
Fenv=np.maximum.accumulate(fup[::-1])[::-1]
Ug=np.array([U(y) for y in grid])
T1=(Ug[1:]*(Fenv[:-1]-Fenv[1:])).sum()+Ug[-1]*Fenv[-1]+Ug[0]*0
# (sum over y<grid[0]=1 is empty; last term bounds the remainder y>=1e300 by U(1e300)F(1e300) plus growth, negligible)
tau=comp+T1
print(f"composite (max-key) bound = {comp:.3e}; tail q>Y bound T1 = {T1:.3e}; tau_w = {tau:.3e}",flush=True)
Wup=1+S1+tau
C=1.0
for x in big['q']: C*=1-1/(int(x)-1)**2
print(f"W_w <= {Wup:.7f}   C_w <= {C:.7f}   C_w*W_w <= {C*Wup:.7f}",flush=True)
# ---- B1(psi) on characters indexed (k mod c, t mod h) ----
B1=np.zeros(c*h)
sel=np.nonzero(Jq>1)[0]
for idx in sel:
    J=int(Jq[idx]); aa=int(a[idx]); bb=int(b[idx])
    m=np.arange(1,J,dtype=np.int64)
    num=m*bb*h                       # t = m*b*h/J mod h
    t=(num//J)%h
    n=(num//J - t)//h               # mb/J = t/h + n  -> floor parts
    k=((m*(c*aa+jc*bb))//J - jc*n)%c
    np.add.at(B1,k*h+t,wq[idx])
Bmax=B1.max()
print(f"max_psi!=1 B1 = {Bmax:.6e} ; M <= {Bmax+tau:.6e} ; sum_psi B1 = {B1.sum():.4e} (=sum (J-1)g/e)",flush=True)
np.save(f'D_data/B1_w{w}.npy',B1)
print(f"A(1)=mean F over H (exact sum_{{d|P(<w)}} g/e) = {A1:.9f}, max F = {Fmax:.6f}")
if w==31 or len(sys.argv)>4:
    # W_5 = A1 + sum_q g/e mean_{K_q}F + (composite/tail)*Fmax
    cache={}; tot=0.0
    for idx in range(len(q)):
        J=int(Jq[idx])
        if J==1: tot+=wq[idx]*A1; continue
        key=(J,int(a[idx])%J,int(b[idx])%J)
        if key not in cache: cache[key]=F[((I*key[1]+Jj*key[2])%J)==0].mean()
        tot+=wq[idx]*cache[key]
    W5=A1+tot+tau*Fmax
    C5=1.0
    for x in D['q']: C5*=1-1/(int(x)-1)**2
    print(f"W_5 <= {W5:.7f} (A1 {A1:.7f} + single {tot:.7f} + tau*Fmax {tau*Fmax:.3e});  rho <= C_5*W_5 <= {C5*W5:.7f}   (C_5 trunc at Y: {C5:.7f})")
