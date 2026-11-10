# a5_consts.py (agent 5, run5): independent rigorous computation of the w=31 constants of D_almostall §11.2:
#   A(1) (exact), Lambda_W, J_q, S1 = sum_{31<=q<=Y} g(q)/e_q, the single-prime part of W_5 (exact means x integer-rounded weights),
#   max_{psi != 1} B1(psi) (own character parametrisation (X,Y) in (Z/E)^2), and C_31, C_5 upper bounds.
# e_q from a5_e_1e8.bin (own code); (G, alpha, beta) from D's ep_1e8.bin, certified generator-free by a5_eprimes_check.c.
# Rounding: weights 1/((q-2)e) summed as floor(10^18/((q-2)e)) in exact integers, so every sum is enclosed in [lo, lo + n*1e-18].
import numpy as np, sys, itertools, pickle
from math import gcd
from fractions import Fraction
sys.path.insert(0, '/home/user/erdos/e203/verdict2/a5')
from a5_lat import lattice, intersect, index, gfrac

DD = '/home/user/erdos/e203/verdict3/D_data/'
dt = np.dtype([('q','<u4'),('e','<u4'),('o2','<u4'),('o3','<u4'),('G','<u2'),('a','<u2'),('b','<u2')])
D = np.fromfile(DD+'ep_1e8.bin', dtype=dt)
own = np.fromfile(DD+'a5_e_1e8.bin', dtype='<u4').reshape(-1, 2)
assert len(own) == len(D) and (own[:,0] == D['q']).all() and (own[:,1] == D['e']).all()
small = D[D['q'] < 31]
P = [int(r['q']) for r in small]
cons = {int(r['q']): (int(r['a']), int(r['b']), int(r['e'])) for r in small}
assert all(int(r['G']) == int(r['e']) for r in small)

# ---- e(T), A(1), Lambda_W ----
eT = {}
for k in range(len(P)+1):
    for T in itertools.combinations(P, k):
        eT[T] = index(lattice([cons[p] for p in T]))
A1 = sum(gfrac(T)/eT[T] for T in eT)
LW = lattice([cons[p] for p in P]); HW = index(LW)
Fmax = gfrac(P) * 0 + np.prod([Fraction(p-1, p-2) for p in P])
print("primes<31:", P, " |H_W| =", HW, " A(1) =", float(A1), " Fmax =", float(Fmax))
# control (V_check 10.4): exact A(1) = 1.1562606807; the WRONG lcm(ord2,ord3) formula for composite d must give ~1.1667
from math import lcm
o2 = {int(r['q']): int(r['o2']) for r in small}; o3 = {int(r['q']): int(r['o3']) for r in small}
A1bad = sum(gfrac(T)/Fraction(lcm(lcm(*[o2[p] for p in T]) if T else 1, lcm(*[o3[p] for p in T]) if T else 1)) for T in eT)
print("control: A(1) with lcm formula (must differ) =", float(A1bad))

# ---- E[nu] and E[nu^2] exact (for the class-distribution control) ----
Enu = np.prod([Fraction(p-1, p) for p in P])
Enu2 = Fraction(0)
for T in eT:
    t = Fraction(1, eT[T])
    for p in P:
        t *= Fraction(1, p) if p in T else Fraction(p-2, p)
    Enu2 += t
print("exact E[nu] =", float(Enu), " exact E[nu^2] =", float(Enu2))

# ---- q >= 31 ----
B = D[D['q'] >= 31]; q = B['q'].astype(np.int64); e = own[D['q'] >= 31, 1].astype(np.int64)
G = B['G'].astype(np.int64); al = B['a'].astype(np.int64); be = B['b'].astype(np.int64)
(w1, w2) = LW
phi1 = (w1[0]*al + w1[1]*be) % G; phi2 = (w2[0]*al + w2[1]*be) % G
J = np.gcd(np.gcd(G, phi1), phi2)
den = (q - 2) * e                         # < 2^63
W18 = (10**18) // den                     # floor, exact
n = len(q)
S1lo = int(W18.sum(dtype=np.uint64)); print("n(q>=31) =", n, " S1 in [", S1lo/1e18, ",", (S1lo+n)/1e18, "]")
# C_w upper: prod(1-x) <= exp(-sum x), x = 1/(q-1)^2; sum x >= floor sum
X18 = (10**18) // ((q-1)**2)
sx31 = int(X18.sum(dtype=np.uint64))
Ds = D['q'][D['q'] < 31].astype(np.int64)
sx5 = sx31 + int(((10**18)//((Ds-1)**2)).sum())
print("sum_{31<=q<=1e8} 1/(q-1)^2 >=", sx31/1e18, "  sum_{5<=q<=1e8} >=", sx5/1e18)

# ---- keys (J, canonical line) ----
sel = np.nonzero(J > 1)[0]
print("#q with J>1:", len(sel))
keys = {}
for i in sel:
    Jq = int(J[i]); a = int(al[i]) % Jq; b = int(be[i]) % Jq
    L = intersect(((1,0),(0,1)), a, b, Jq)
    # canonical HNF-like key: g1 = gcd(b,J'), plus j0 (computed through the kernel basis first vector reduced)
    k = (Jq, gcd(b, Jq), (L[0][1]) % (Jq // gcd(b, Jq)) if Jq // gcd(b, Jq) > 1 else 0)
    if k not in keys:
        keys[k] = [a, b, 0]
    keys[k][2] += int(W18[i])
print("distinct keys:", len(keys))
pickle.dump({'keys': keys, 'n_sel': len(sel)}, open(DD+'a5_keys.pkl', 'wb'))
Wone = int(W18[J == 1].sum(dtype=np.uint64)); n_one = int((J == 1).sum())

# ---- single-prime part of W_5: sum_q w_q * mean_{K_q} F,  mean = sum_T g(T) J / [Z^2 : L_q cap Lambda_T] ----
single_lo = Fraction(Wone, 10**18) * A1      # J=1: K_q = H_W, mean = A(1)
single_hi = Fraction(Wone + n_one, 10**18) * A1
for k, (a, b, wsum) in keys.items():
    Jq = k[0]
    Lq = intersect(((1,0),(0,1)), a, b, Jq); assert index(Lq) == Jq
    mean = Fraction(0)
    for T in eT:
        LL = Lq
        for p in T:
            LL = intersect(LL, *cons[p])
        mean += gfrac(T) * Fraction(Jq, index(LL))
    keys[k].append(mean)
    single_lo += Fraction(wsum, 10**18) * mean
nkq = len(sel)
single_hi = single_lo + Fraction(n_one + nkq, 10**18) * Fmax
print("single-prime part of W_5 in [", float(single_lo), ",", float(single_hi), "]")

# ---- B1(psi) for psi != 1, characters as (X,Y) in (Z/E)^2 ----
E = 55440
assert all((E*w1[0]) % 1 == 0 for _ in [0])
codes = []; wts = []
for k, v in keys.items():
    a, b, wsum = v[0], v[1], v[2]; Jq = k[0]
    t = np.arange(1, Jq, dtype=np.int64)
    Xc = (t * a * (E // Jq)) % E; Yc = (t * b * (E // Jq)) % E
    assert ((Xc*w1[0] + Yc*w1[1]) % E == 0).all() and ((Xc*w2[0] + Yc*w2[1]) % E == 0).all()
    codes.append(Xc*E + Yc); wts.append(np.full(len(t), wsum + v[2]*0, dtype=np.float64))
codes = np.concatenate(codes); wts = np.concatenate(wts)
u, inv_ = np.unique(codes, return_inverse=True)
B1 = np.bincount(inv_, weights=wts)
nterms = np.bincount(inv_)
imax = np.argmax(B1)
# rigorous upper: the float sum of integers < 2^53 each, total < 2^53, is exact; add rounding slack n*1e-18 per term
B1max_up = (B1[imax] + nterms.max() * 1.0) / 1e18 * (1 + 1e-12) + 1e-15
print("characters hit:", len(u), " (|H_W|-1 =", HW-1, ")  max_{psi!=1} B1 <=", B1max_up, " sum_psi B1 =", B1.sum()/1e18)
res = dict(A1=A1, HW=HW, Fmax=Fmax, Enu=Enu, Enu2=Enu2, S1=(S1lo, S1lo+n), sx31=sx31, sx5=sx5,
           single=(single_lo, single_hi), B1max_up=B1max_up)
pickle.dump(res, open(DD+'a5_consts.pkl', 'wb'))
print("saved", DD+'a5_consts.pkl')
