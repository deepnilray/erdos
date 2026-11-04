# a5_tau_control.py: control for the two-largest-keys composite bound (part A of a5_tau.py) on a finite prime set where the
# exact value is computable: Q = primes 31 <= p <= 1e8 with e_p <= EMAX. Exact: sum over all T subset Q, |T| >= 2, g(T)/e(T)
# with e(T) the exact lattice index (a5_lat). Bound: sum_{p1>p2 keys} g1 g2 Pi(<p2)/lcm(e1,e2) restricted to Q.
# (only primes with e_p | 55440, so that D's (alpha,beta) are full logs.) PASS iff bound >= exact. Planted failure: drop the Pi(<p2) factor (ignores d with >= 3 primes) -> must fall below exact.
import numpy as np, itertools, sys
from fractions import Fraction
from math import lcm
sys.path.insert(0,'.')
from a5_lat import lattice, index
EMAX=int(sys.argv[1]) if len(sys.argv)>1 else 24
dt=np.dtype([('q','<u4'),('e','<u4'),('o2','<u4'),('o3','<u4'),('G','<u2'),('a','<u2'),('b','<u2')])
D=np.fromfile('/home/user/erdos/e203/verdict3/D_data/ep_1e8.bin',dtype=dt)
S=D[(D['q']>=31)&(D['e']<=EMAX)&(D['G']==D['e'])]
Q=[(int(r['e']),int(r['q']),int(r['a']),int(r['b']),int(r['G'])) for r in S]; Q.sort()
assert all(G==e for (e,q,a,b,G) in Q)   # e <= EMAX small: G = e, so (a,b) are full logs mod e
print("primes in Q:",len(Q),[x[1] for x in Q])
exact=Fraction(0)
for k in range(2,len(Q)+1):
    for T in itertools.combinations(Q,k):
        gT=Fraction(1)
        for t in T: gT/=t[1]-2
        exact+=gT/index(lattice([(t[2],t[3],t[0]) for t in T]))
bound=Fraction(0); planted=Fraction(0)
Pi=[Fraction(1)]
for t in Q: Pi.append(Pi[-1]*(1+Fraction(1,t[1]-2)))
for i in range(len(Q)):
    for j in range(i):
        term=Fraction(1,(Q[i][1]-2)*(Q[j][1]-2))/lcm(Q[i][0],Q[j][0])
        bound+=term*Pi[j]; planted+=term
print("exact %.6e  bound %.6e  PASS=%s   planted(no Pi) %.6e  fires=%s"%(float(exact),float(bound),bound>=exact,float(planted),planted<exact))
