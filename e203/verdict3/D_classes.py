# D_classes.py w : exact distribution of nu_r = (#cells of H_W surviving all primes 5<=p<w for class r)/|H|, r uniform over m coprime to 6.
# Method: S = set of primes p<w with (-1/m mod p) in H_p ("killing primes"); given S, kill targets c_p uniform on H_p.
# Fix c_{p0}=1 for p0=max S (each coset of im(H) meets this slice equally), FFT-convolve the histogram of H (h_{p0}!=1) with the
# "all coordinates differ" indicator on G'=prod_{p in S\p0} Z/e_p.  Output: D_data/nu_w{w}.npz (counts f=nu*|H| and weights).
import numpy as np, math, sys, itertools
from math import gcd
w=int(sys.argv[1])
dt=np.dtype([('q','<u4'),('e','<u4'),('o2','<u4'),('o3','<u4'),('G','<u2'),('a','<u2'),('b','<u2')])
D=np.fromfile('D_data/ep_1e6.bin',dtype=dt); small=D[D['q']<w]
P=[int(x) for x in small['q']]; ee={int(r['q']):int(r['e']) for r in small}
al={int(r['q']):int(r['a']) for r in small}; be={int(r['q']):int(r['b']) for r in small}
assert all(int(r['G'])==int(r['e']) for r in small)
h=1
for o in small['o3']: h=h*int(o)//gcd(h,int(o))
def inLam(i,j): return all((i*al[p]+j*be[p])%ee[p]==0 for p in P)
for c in range(1,10**6):
    js=[j for j in range(h) if inLam(c,j)]
    if js: jc=js[0]; break
Hs=c*h
I=np.repeat(np.arange(c,dtype=np.int64),h); J=np.tile(np.arange(h,dtype=np.int64),c)
L={p:(I*al[p]+J*be[p])%ee[p] for p in P}
# sanity: reps distinct
key=np.zeros(Hs,dtype=np.int64)
for p in P: key=key*ee[p]+L[p]
assert len(np.unique(key))==Hs, "reps not distinct"
acc=np.zeros(Hs+1)
for k in range(0,len(P)+1):
    for S in itertools.combinations(P,k):
        PS=1.0
        for p in P: PS*= (ee[p]/p) if p in S else (1-ee[p]/p)
        if k==0: acc[Hs]+=PS; continue
        p0=S[-1]; Sp=S[:-1]
        mask=L[p0]!=0
        if not Sp:
            acc[int(mask.sum())]+=PS; continue
        shape=tuple(ee[p] for p in Sp)
        idx=np.ravel_multi_index(tuple(L[p][mask] for p in Sp),shape)
        hist=np.bincount(idx,minlength=int(np.prod(shape))).reshape(shape).astype(float)
        Dm=np.ones(shape)
        for ax,p in enumerate(Sp):
            sl=[slice(None)]*len(Sp); sl[ax]=0; Dm[tuple(sl)]=0
        f=np.fft.irfftn(np.fft.rfftn(hist)*np.fft.rfftn(Dm),s=shape,axes=list(range(len(shape))))
        fi=np.rint(f).astype(np.int64).ravel()
        assert np.abs(f.ravel()-fi).max()<1e-3
        acc+=np.bincount(fi,minlength=Hs+1)*(PS/fi.size)
nu=np.arange(Hs+1)/Hs
mean=(acc*nu).sum(); pred=np.prod([1-1/p for p in P])
print(f"w={w} |H|={Hs} total weight {acc.sum():.12f} E[nu]={mean:.10f} pred prod(1-1/p)={pred:.10f}")
print(f"  P(nu=0) (covering classes, primes<w) = {acc[0]:.6e};  P(nu<0.05)={acc[nu<0.05].sum():.4e} P(nu<0.1)={acc[nu<0.1].sum():.4e}  min positive nu={nu[(acc>0)&(nu>0)].min():.5f}")
np.savez(f'D_data/nu_w{w}.npz',nu=nu,mu=acc,H=Hs)
