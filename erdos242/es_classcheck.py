"""Check each GOOD class of S_n points really yields a solution, n=1 mod 4 <= N.
 class (xz=1 or yz=1 mod 4): Theorem A (proved).  class (x=0 or y=0 mod 4): q=4sz-1,r=y,s1=s,s2=1 (algebra, proved) -> verified by exact fractions.
 class z=0 mod 4: no explicit identity yet -> test that n then has a Chamberland rep (independent enumeration).  Control: class z=2 must NOT imply a rep for all n.
usage: python3 es_classcheck.py N"""
import sys
from fractions import Fraction as F
N = int(sys.argv[1])
# independent Chamberland enumerator (q <= 4N+1)
ref = bytearray(N + 1)
for q in range(3, 4 * N + 2, 4):
    h = (q + 1) // 4; D = [d for d in range(1, h + 1) if h % d == 0]
    for s1 in D:
        for s2 in D:
            n0 = (-(4 * s1 * s2)) % q
            if n0 < 5: n0 += q
            for n in range(n0, N + 1, q):
                if n % 4 == 1: ref[n] = 1
def points(n):
    for x in range(1, n + 2):
        z = 1
        while True:
            a = x * z - 1
            if a <= 0: z += 1; continue
            if a > n + x: break
            if (n + x) % a == 0: yield x, (n + x) // a, z
            z += 1
bad_x0 = bad_z0 = ctrl_z2_fail = tot_x0 = tot_z0 = tot_z2 = 0
for n in range(5, N + 1, 4):
    for x, y, z in points(n):
        if x % 4 == 0:        # Chamberland construction, exact check of identity (4)
            tot_x0 += 1; s = x // 4; q = 4 * s * z - 1; r = y
            ok = (q * r - 4 * s * 1 == n) and q % 4 == 3 and ((q + 1) // 4) % s == 0
            if ok:
                A = r * (q + 1) // 4 - s * 1; B = (q + 1) // 4 * n; C = F(1, s) * F(q + 1, 4) * (F(r * (q + 1), 4 * 1) - s) * n
                ok = F(1, A) + F(1, B) + 1 / C == F(4, n)
            bad_x0 += (not ok)
        if z % 4 == 0:
            tot_z0 += 1; bad_z0 += (not ref[n])
        if z % 4 == 2:
            tot_z2 += 1; ctrl_z2_fail += (not ref[n])
print("N =", N)
print("points with 4|x : %d, failures of explicit Type II construction: %d" % (tot_x0, bad_x0))
print("points with 4|z : %d, n WITHOUT any Chamberland rep: %d" % (tot_z0, bad_z0))
print("CONTROL points with z=2 mod 4: %d, of which n has no Chamberland rep: %d  (nonzero expected: squares have z=2 points)" % (tot_z2, ctrl_z2_fail))
