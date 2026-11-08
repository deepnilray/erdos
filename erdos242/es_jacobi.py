"""Check Prop C: for every family hit (m,a) of n (n=1 mod 4, m=3 mod 4, a | n+m, 4|a, a=-1 mod m),
with a = 2^e a', a' odd:  Jacobi (a'/n) = -(2/m)^e,  (2/m)=-1 iff m=3 mod 8.  Control: pairs (m,a) with a | n+m, 4|a but a != -1 mod m
must violate it roughly half the time (so the test has power).  usage: python3 es_jacobi.py N"""
import sys
from sympy import jacobi_symbol as J
N = int(sys.argv[1]); hits = viol = ctrl = ctrlviol = 0
def divisors(M):
    ds = []; d = 1
    while d * d <= M:
        if M % d == 0: ds += [d, M // d] if d * d != M else [d]
        d += 1
    return ds
for n in range(5, N + 1, 4):
    if int(n ** .5) ** 2 == n and False: pass
    for m in range(3, 200, 4):
        for a in divisors(n + m):
            if a % 4: continue
            ap = a; e = 0
            while ap % 2 == 0: ap //= 2; e += 1
            pred = -((-1 if m % 8 == 3 else 1) ** e)
            if (a + 1) % m == 0:
                hits += 1
                if J(ap, n) != pred: viol += 1
            elif J(ap, n) != 0:
                ctrl += 1
                if J(ap, n) != pred: ctrlviol += 1
print(f"n=1 mod 4 up to {N}: hits={hits} violations of (a'/n)=-(2/m)^e: {viol};  control pairs={ctrl}, violating={ctrlviol} ({ctrlviol/max(ctrl,1):.2f})")
