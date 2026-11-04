# a5_fh.py (agent 5, run5): limit errors E^inf of the Brun-Hooley sieve (Ford notes Thm 2.3 upper, Thm 3.2 lower) for the
# limit configuration of 5_noside_analytic.md §2: t_j = K^{1-j}, even k_j chosen greedily for j <= J0, k_j = 2j for j > J0.
#   upper (kappa=2):  cost = sum_j k_j t_j            must be < s
#   lower (kappa=1):  cost = 1 + sum_j k_j t_j        must be < s   (Ford (3.3): d <= z_1^{k_1+1} z_2^{k_2} ...)
#   E^inf = sum_j e^{lam 1[k_j>0]} lam^{k_j+1}/(k_j+1)!, lam = kappa log K.
# The greedy is in floats (any choice is a valid sieve); the reported E and cost are enclosed with mpmath.iv, tails included.
import math, sys
from mpmath import iv, mpf
iv.dps = 40

def greedy(s, kappa, K, lower, J0=200):
    lam = kappa*math.log(K); t = [K**(-j) for j in range(J0)]
    term = lambda k: math.exp((lam if k > 0 else 0.0) + (k+1)*math.log(lam) - math.lgamma(k+2))
    k = [0]*J0; used = (1.0 if lower else 0.0) + 1e-7        # 1e-7: room for the tail cost and the slack sigma
    while True:
        best = None
        for j in range(J0):
            gain = term(k[j]) - term(k[j]+2); cost = 2*t[j]
            if used + cost <= s and gain > 0 and (best is None or gain/cost > best[0]):
                best = (gain/cost, j)
        if best is None: break
        j = best[1]; k[j] += 2; used += 2*t[j]
    return k

def enclose(s, kappa, K, k, lower):
    """rigorous E^inf and cost for configuration k (len J0) + tail k_j = 2j (j > J0, 1-based j = index+1)."""
    J0 = len(k); Ki = iv.mpf(K) if not isinstance(K, str) else iv.mpf(K)
    lam = kappa*iv.log(Ki)
    E = iv.mpf(0); cost = iv.mpf(1 if lower else 0)
    for j in range(J0):                       # block j+1, t = K^{-j}
        kk = k[j]
        E += (iv.exp(lam) if kk > 0 else 1) * lam**(kk+1) / iv.factorial(kk+1)
        cost += kk * Ki**(-j)
    # tail blocks j = J0+1, ...: k = 2j, t = K^{1-j}.  error <= e^lam sum_{n >= 2J0+3} lam^n/n! <= e^lam lam^n0/n0! / (1 - lam/(n0+1))
    n0 = 2*J0 + 3
    Etail = iv.exp(lam) * lam**n0 / iv.factorial(n0) / (1 - lam/(n0+1))
    # cost: sum_{j>J0} 2j K^{1-j} = 2K sum_{j>J0} j r^j, r = 1/K;  sum_{j>m} j r^j = r^{m+1}((m+1) - m r)/(1-r)^2
    r = 1/Ki; m = J0
    ctail = 2*Ki * r**(m+1) * ((m+1) - m*r) / (1-r)**2
    return E + Etail, cost + ctail

def best(s, kappa, lower, Ks=(1.3,1.4,1.5,1.6,1.75,2,2.25,2.5,3,3.5,4,5,6)):
    out = None
    for K in Ks:
        k = greedy(s, kappa, K, lower)
        E, c = enclose(s, kappa, K, k, lower)
        if not (c.b < s):
            continue                       # cost must be strictly below s (slack sigma = s - cost > 0)
        if out is None or E.b < out[0].b:
            out = (E, c, K, k)
    return out

if __name__ == '__main__':
    c = eps = 0.001
    print("r0  s        E1(kappa=1,lower) upper      cost1     E2(kappa=2,upper) upper     cost2   K1  K2")
    for r0 in list(range(10, 31)):
        s = (r0+1)*(1-eps)/(1+c) - 1e-6
        b1 = best(s, 1, True); b2 = best(s, 2, False)
        print(f"{r0:3d} {s:8.4f}  {float(b1[0].b):.6e}  {float(b1[1].b):.6f}   {float(b2[0].b):.6e}  {float(b2[1].b):.6f}  {b1[2]} {b2[2]}", flush=True)
