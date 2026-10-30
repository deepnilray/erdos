# Omega(kappa) constant with w2 allowed just above a prime (sup over real w1<w2), primes >= P0
import math, sys
from sympy import primerange
for P0 in (5,31):
  for kap in (1,2):
    ps=list(primerange(P0,200000)); best=(0,None)
    for i in range(len(ps)):
        prod=1.0
        for j in range(i,min(len(ps),i+3000)):
            prod*= 1/(1-kap/ps[j])
            r=prod/(math.log(ps[j])/math.log(ps[i]))**kap   # w1=p_i, w2 -> p_j^+
            if r>best[0]: best=(r,(ps[i],ps[j]))
    print("primes>=%d kappa=%d: K=%.5f at [%d, %d] (w2 just above), K^10=%.3f"%(P0,kap,best[0],*best[1],best[0]**10))
