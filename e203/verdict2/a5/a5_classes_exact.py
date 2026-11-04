# a5_classes_exact.py (agent 5, run5): D_classes.py's FFT method for the class distribution of nu_r (w=31), but with EXACT
# integer weights: weight of a class pattern S is num_S/(prod p * size_S), num_S = prod_{p in S} e_p prod_{p not in S} (p - e_p).
# Output per bin of width BW counts (nu in [b*BW, (b+1)*BW)/|H|): exact integer weight numerators over the common denominator.
# Controls: (1) total weight = 1 exactly; (2) E[nu] = prod(1-1/p) exactly; (3) E[nu^2] equals the independent lattice formula
# from a5_consts.py exactly; (4) FFT values within 1e-3 of integers (as D).
import numpy as np, math, sys, itertools, pickle, os
from math import gcd
from fractions import Fraction
w = 31; BW = int(sys.argv[1]) if len(sys.argv) > 1 else 64
DD = '/home/user/erdos/e203/verdict3/D_data/'
dt = np.dtype([('q','<u4'),('e','<u4'),('o2','<u4'),('o3','<u4'),('G','<u2'),('a','<u2'),('b','<u2')])
D = np.fromfile(DD+'ep_1e6.bin', dtype=dt); small = D[D['q'] < w]
P = [int(x) for x in small['q']]; ee = {int(r['q']): int(r['e']) for r in small}
al = {int(r['q']): int(r['a']) for r in small}; be = {int(r['q']): int(r['b']) for r in small}
h = 1
for o in small['o3']: h = h*int(o)//gcd(h, int(o))
def inLam(i, j): return all((i*al[p]+j*be[p]) % ee[p] == 0 for p in P)
for c in range(1, 10**6):
    js = [j for j in range(h) if inLam(c, j)]
    if js: break
Hs = c*h
I = np.repeat(np.arange(c, dtype=np.int64), h); J = np.tile(np.arange(h, dtype=np.int64), c)
L = {p: (I*al[p]+J*be[p]) % ee[p] for p in P}
key = np.zeros(Hs, dtype=np.int64)
for p in P: key = key*ee[p]+L[p]
assert len(np.unique(key)) == Hs
nb = Hs//BW + 1
binw = [0]*nb                       # numerators over DEN = prod p * LCM
Pp = math.prod(P)
recs = []                           # (num_S, size_S, bincounts(object), sum f, sum f^2)
for k in range(0, len(P)+1):
    for S in itertools.combinations(P, k):
        num = math.prod(ee[p] if p in S else (p-ee[p]) for p in P)
        if k == 0:
            cnt = {Hs: 1}; size = 1
            recs.append((num, size, {Hs//BW: 1}, Hs, Hs*Hs)); continue
        p0 = S[-1]; Sp = S[:-1]; mask = L[p0] != 0
        if not Sp:
            f0 = int(mask.sum()); recs.append((num, 1, {f0//BW: 1}, f0, f0*f0)); continue
        shape = tuple(ee[p] for p in Sp)
        idx = np.ravel_multi_index(tuple(L[p][mask] for p in Sp), shape)
        hist = np.bincount(idx, minlength=int(np.prod(shape))).reshape(shape).astype(float)
        Dm = np.ones(shape)
        for ax, p in enumerate(Sp):
            sl = [slice(None)]*len(Sp); sl[ax] = 0; Dm[tuple(sl)] = 0
        f = np.fft.irfftn(np.fft.rfftn(hist)*np.fft.rfftn(Dm), s=shape, axes=list(range(len(shape))))
        fi = np.rint(f).astype(np.int64).ravel()
        assert np.abs(f.ravel()-fi).max() < 1e-3
        if os.environ.get('A5_PLANT') and len(S) == 5 and S[0] == 5: fi[0] -= 1   # planted: one wrong count
        bc = np.bincount(fi//BW, minlength=nb); nz = np.nonzero(bc)[0]
        recs.append((num, fi.size, {int(b): int(bc[b]) for b in nz}, int(fi.sum()), int((fi*fi).sum())))
LCM = 1
for r in recs: LCM = LCM*r[1]//gcd(LCM, r[1])
DEN = Pp*LCM
tot = 0; m1 = 0; m2 = 0
for (num, size, bcs, s1, s2) in recs:
    fac = num*(LCM//size)
    for b, cc in bcs.items(): binw[b] += fac*cc
    tot += fac*size; m1 += fac*s1; m2 += fac*s2
Enu = Fraction(m1, DEN*Hs); Enu2 = Fraction(m2, DEN*Hs*Hs)
print("total weight == 1:", Fraction(tot, DEN) == 1)
print("E[nu] =", float(Enu), " exact prod(1-1/p) match:", Enu == math.prod(Fraction(p-1, p) for p in P))
ref = pickle.load(open(DD+'a5_consts.pkl', 'rb')) if len(sys.argv) < 3 else None
if ref is not None:
    print("E[nu^2] =", float(Enu2), " independent lattice formula:", float(ref['Enu2']), " exact match:", Enu2 == ref['Enu2'])
nzb = [b for b in range(nb) if binw[b]]
print("bins with mass:", len(nzb), " lowest nonempty bin nu in [", nzb[0]*BW/Hs, ",", (nzb[0]+1)*BW/Hs, ")")
if not os.environ.get('A5_PLANT'): pickle.dump(dict(BW=BW, Hs=Hs, DEN=DEN, binw=binw), open(DD+f'a5_nubins_BW{BW}.pkl', 'wb'))
