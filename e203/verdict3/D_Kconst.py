# D_Kconst.py: K_kappa(w) = sup_{w<=w1<w2} prod_{w1<=p<w2}(1-kappa/p)^{-1} (log w1/log w2)^kappa  (Omega(kappa) constant, primes >= w)
# sup over w1,w2 among primes up to Y (w2 = next prime after last included). Large-scale tail: Mertens -> ratio -> const, checked by monotone trend.
import numpy as np, sys
from sympy import primerange
Y=int(sys.argv[1])
P=np.array(list(primerange(5,Y)),dtype=float)
for kappa in (1,2):
  for w in (5,13,17,19,23,29,31,37,41,53):
    Q=P[P>=w]
    L=np.cumsum(-np.log1p(-kappa/Q))            # L[i] = sum_{j<=i}
    # w1=Q[a], w2 = Q[b+1] (product over a..b): val = L[b]-L[a-1] - kappa*(log log Q[b+1] - log log Q[a])
    ll=np.log(np.log(Q))
    # for fixed b, maximize over a<=b: -(L[a-1] ) + kappa*ll[a]  -> prefix max
    Lm1=np.concatenate([[0.0],L[:-1]])
    g=kappa*ll-Lm1
    pm=np.maximum.accumulate(g)
    val=L[:-1]-kappa*ll[1:]+pm[:-1]
    print("kappa",kappa,"w",w,"K",np.exp(val.max()),"at w2 index",val.argmax(),"Q",Q[val.argmax()+1])
