# D_comp.py w E0 : sharper bound for the composite part  sum_{d: omega(d)>=2, p|d => p>=w} g(d)/e(d)  (g(p)=1/(p-2)).
# Assign d to its two largest keys p1>p2 (key=(e_p,p)); e(d) >= lcm(e_{p1},e_{p2}); remaining part bounded by Pi_key(p2).
#   part A: p1 known (<=Y), e1<=E0, p2 known: exact double sum with lcm.
#   part B: p1 known, e1<=E0, p2 unknown (>Y, e2<=e1): g1/e1 * (exp(U(e1))-1) * Pi_key(p1)
#   part C: p1 known, e1>E0: crude g1/e1*(Pi_key(p1)-1).    (p1 unknown: inside T1 of D_W.py)
import numpy as np, math, sys
from math import gcd
w=int(sys.argv[1]); E0=int(sys.argv[2]); Y=10**8
exec(open('D_W.py').read().split("# ---- max-key composite bound ----")[0].split("small=D[D['q']<w]")[0].replace("w=int(sys.argv[1]); Y=int(float(sys.argv[2])); fn=sys.argv[3] if len(sys.argv)>3 else 'D_data/ep_1e8.bin'","fn='D_data/ep_1e8.bin'"))
big=D[D['q']>=w]
q=big['q'].astype(np.int64); e=big['e'].astype(np.int64)
lnY=math.log(Y)
src=open('D_W.py').read(); exec(src[src.index("def U(y):"):src.index("# ---- max-key composite bound ----")])
order=np.lexsort((q,e)); qs=q[order]; es_=e[order]; gs=1.0/(qs-2)
lg=np.log1p(gs); cum=np.concatenate([[0.0],np.cumsum(lg)[:-1]])
Ue=np.array([U(int(x)) for x in es_]) if len(es_)<10 else None
ue=np.unique(es_); Uv=np.array([U(int(x)) for x in ue]); Ue=Uv[np.searchsorted(ue,es_)]
Pikey=np.exp(cum+Ue)            # prod over keys < p (known) times unknown-with-e<=e_p
small_idx=np.nonzero(es_<=E0)[0]; n=len(small_idx)
print(f"w={w} E0={E0}: known primes with e<=E0: {n}",flush=True)
A=0.0
e1=es_[small_idx]; g1=gs[small_idx]; PK=Pikey[small_idx]
for t in range(1,n):
    # p1 = small_idx[t]; p2 = earlier keys among small (all have e<=e1)
    l=np.lcm(e1[:t],e1[t])
    A+=g1[t]*np.sum(g1[:t]*PK[:t]/l)
B=np.sum(g1/e1*(np.exp(Uv[np.searchsorted(ue,e1)])-1)*PK)
big_idx=np.nonzero(es_>E0)[0]
Cc=np.sum(gs[big_idx]/es_[big_idx]*(Pikey[big_idx]-1))
print(f"  A(exact pairs)={A:.4e}  B(unknown second)={B:.4e}  C(crude, e1>E0)={Cc:.4e}  composite <= {A+B+Cc:.4e}")
