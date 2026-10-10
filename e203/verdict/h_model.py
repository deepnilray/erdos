import numpy as np, math
T=np.load('/tmp/claude-0/-home-user-erdos/32befd5c-9d0c-507d-92ec-d6dd66bc97ea/scratchpad/agents5/ptab_1000000.npy')
P=T[:,0]; E=T[:,3]; O2=T[:,1]; O3=T[:,2]
LOG_EXTRA=math.log(2)+math.log(1.5)   # p=2 (k>=1) and p=3 (l>=1)
def delta(m,pmax):
    """delta_p=1 iff -m^{-1} in <2,3> mod p  <=> (-m)^{e_p}==1 mod p"""
    idx=np.searchsorted(P,pmax,side='right')
    d=np.fromiter(((pow(-m % int(p),int(e),int(p))==1) for p,e in zip(P[:idx],E[:idx])),dtype=bool,count=idx)
    return d,idx
def logC_ind(m,pmax=10**5,alg=True):
    d,idx=delta(m,pmax)
    p=P[:idx].astype(float); e=E[:idx].astype(float)
    s=LOG_EXTRA+np.sum(np.log1p(-d.astype(float)/e)-np.log1p(-1/p))
    if alg: s+=math.log(alg_factor(m))
    return s
def perfect_power_g(m):
    """largest g with m=M^g"""
    best=1
    for g in range(2,int(math.log2(max(m,2)))+2):
        r=round(m**(1/g))
        for c in (r-1,r,r+1):
            if c>1 and c**g==m: best=g
    return best
def alg_set_density(g):
    # density of Alg(m) = union_{odd primes q|g} qZ^2  U  [C4 if 4|g]  (MIXED.md sec 1)
    qs=[q for q in range(3,g+1,2) if g%q==0 and all(q%r for r in range(3,int(q**.5)+1,2))]
    # density of union of q Z^2 lattices: 1-prod(1-1/q^2) ; C4 = (2,0)+4Z^2 disjoint? C4 meets qZ^2 (q odd) with density 1/(16 q^2)
    dens_q=1-np.prod([1-1/q**2 for q in qs]) if qs else 0.0
    if g%4==0: dens=dens_q+(1/16)*(1-dens_q)
    else: dens=dens_q
    return dens
def alg_factor(m):
    return 1-alg_set_density(perfect_power_g(m))
