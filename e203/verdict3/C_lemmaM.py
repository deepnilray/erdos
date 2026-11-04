"""C_lemmaM.py -- Monte Carlo check of Lemma M:  for independent uniform primitive forms (a,b) mod e1 and (a',b') mod e2,
E[ gcd(a b' - b a', e1, e2) ] = prod_{r^k || g} (1 + k (r-1)/(r+1)),  g = gcd(e1,e2).  Control: the formula with rho_r replaced by 1 (c=tau(g)) must fail."""
import random, math
from sympy import factorint
def prim(e, rnd):
    while True:
        a, b = rnd.randrange(e), rnd.randrange(e)
        if math.gcd(math.gcd(a, b), e) == 1: return a, b
rnd = random.Random(7); worst = 0; worst_c = 0
for e1, e2 in [(12, 18), (30, 45), (60, 36), (100, 75), (210, 330), (64, 96), (360, 504), (49, 343), (1155, 105)]:
    g = math.gcd(e1, e2); N = 200000; s = 0
    for _ in range(N):
        a, b = prim(e1, rnd); c, d = prim(e2, rnd)
        s += math.gcd(a * d - b * c, g)
    pred = 1.0; ctrl = 1.0
    for r, k in factorint(g).items(): pred *= 1 + k * (r - 1) / (r + 1); ctrl *= 1 + k
    se = 0.0
    print('e=(%d,%d) g=%d  MC %.4f  model %.4f  control(tau) %.4f' % (e1, e2, g, s / N, pred, ctrl))
    worst = max(worst, abs(s / N - pred) / pred); worst_c = max(worst_c, abs(s / N - ctrl) / ctrl)
print('max rel. deviation from model %.4f ; from control %.4f' % (worst, worst_c)); assert worst < 0.02 < worst_c
