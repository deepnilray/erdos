# a5_fh_control.py: controls for a5_fh.py.
# (1) L3's fh_table.py constraint ((k1+1)+sum_{j>=2} k_j t_j <= s for BOTH kappas, J=150, no tail) at s=19.96, kappa=2, K=2:
#     my greedy with lower=True must give E within the same order (L3 reported eta2=5.2e-4 at r0=19 over its K grid).
# (2) independent re-evaluation of E for a fixed configuration with mpmath mpf at 50 digits (no iv), must lie inside the iv enclosure.
# (3) planted: a configuration whose cost exceeds s must be rejected by best()'s cost test (c.b < s).
import math, sys
sys.path.insert(0,'.')
from a5_fh import greedy, enclose, best
from mpmath import mp, mpf, exp, log, factorial
mp.dps=50
s=19.960039
k=greedy(s,2,2.0,True,J0=150); E,c=enclose(s,2,2.0,k,True)
print("(1) kappa=2, K=2, L3-style constraint: E in [%.4e, %.4e], e^E-1 ~ %.3e, cost %.6f <= s=%.6f"%(float(E.a),float(E.b),math.expm1(float(E.b)),float(c.b),s))
lam=2*log(2); Em=sum((exp(lam) if kk>0 else 1)*lam**(kk+1)/factorial(kk+1) for kk in k)
print("(2) mpf re-evaluation (no tail) %.12e inside iv [%.12e, %.12e]: %s"%(float(Em),float(E.a),float(E.b), E.a<=Em<=E.b))
kbad=list(k); kbad[0]+=20
E2,c2=enclose(s,2,2.0,kbad,True)
print("(3) planted over-budget config: cost %.4f, accepted=%s (must be False)"%(float(c2.a), bool(c2.b<s)))
