"""a4/pencil_ffkpy.py -- checks for 4_tail.md sections 1.2, 1.3.
(1) Pencil: the l+1 lines through 0 in F_l^2 are pairwise independent cosets (Lambda_i + Lambda_j = Z^2) that cover F_l^2,
    so FFKPY Lemma 2.1 with beta over ALIGNED pairs only (delta >= alpha - beta_al) fails; with beta over gcd(e_i,e_j)>1 it holds.
    Control: dropping one line leaves points uncovered.
(2) Random cyclic-quotient coset systems on Z^2: exact uncovered density delta vs alpha - beta_gcd (must always hold, PROVED)
    and vs alpha - beta_aligned (should fail sometimes: control that the aligned version is really false, not just in the pencil).
(3) Pencil(F_2^2) x 1-D exact covering with odd moduli -> covering of Z^2 by cyclic-quotient cosets, non-aligned.
usage: python3 verdict2/a4/pencil_ffkpy.py [trials]"""
import sys, random, itertools
from math import gcd
from fractions import Fraction

def lcm(a, b): return a * b // gcd(a, b)

def snf_d1(vecs_mod):
    pass

# a coset system element: (e, a, b, c): set {(k,l) : a k + b l = c mod e}, with gcd(a,b,e)=1 (cyclic quotient Z/e)
def covered_density(sys_, N):
    """exact density of the union on the torus (Z/N)^2, N a multiple of every e."""
    cov = 0
    for k in range(N):
        for l in range(N):
            for (e, a, b, c) in sys_:
                if (a * k + b * l - c) % e == 0:
                    cov += 1; break
    return Fraction(cov, N * N)

def sum_index(p, q):
    """[Z^2 : Lambda_p + Lambda_q] computed directly on the torus: size of the common quotient = #image of Z^2 in Z/e1 x Z/e2 divided..."""
    (e1, a1, b1, _), (e2, a2, b2, _) = p, q
    # Lambda_p cap Lambda_q has index |image of (k,l) -> (a1k+b1l mod e1, a2k+b2l mod e2)|; [Z^2:L1+L2] = e1 e2 / index(L1 cap L2)
    N = lcm(e1, e2)
    img = {((a1 * k + b1 * l) % e1, (a2 * k + b2 * l) % e2) for k in range(N) for l in range(N)}
    return e1 * e2 // len(img)

def alpha_beta(sys_):
    al = Fraction(1)
    for s in sys_: al *= 1 - Fraction(1, s[0])
    bg = Fraction(0); ba = Fraction(0)
    for i in range(len(sys_)):
        for j in range(i + 1, len(sys_)):
            w = Fraction(1, sys_[i][0] * sys_[j][0])
            if gcd(sys_[i][0], sys_[j][0]) > 1: bg += w
            if sum_index(sys_[i], sys_[j]) > 1: ba += w
    return al, bg, ba

def pencil(l):
    dirs = [(1, 0)] + [(t, 1) for t in range(l)]   # forms a k + b l, kernels = the l+1 lines through 0
    return [(l, a, b, 0) for (a, b) in dirs]

ok = True
print("(1) pencil")
for l in (2, 3, 5, 7):
    P = pencil(l)
    d = 1 - covered_density(P, l)
    al, bg, ba = alpha_beta(P)
    dc = 1 - covered_density(P[:-1], l)
    print(f"  l={l}: delta={d}  alpha={al}  beta_gcd={bg}  beta_aligned={ba}  aligned-version holds? {d >= al - ba}  gcd-version holds? {d >= al - bg}  control (drop a line): delta={dc}")
    ok &= (d == 0 and ba == 0 and d < al - ba and d >= al - bg and dc > 0)

trials = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
random.seed(20261104)
viol_g = viol_a = 0; nonempty = 0
for t in range(trials):
    n = random.randint(2, 5)
    S = []
    for _ in range(n):
        e = random.choice([2, 3, 4, 5, 6])
        while True:
            a, b = random.randrange(e), random.randrange(e)
            if gcd(gcd(a, b), e) == 1: break
        S.append((e, a, b, random.randrange(e)))
    N = 1
    for s in S: N = lcm(N, s[0])
    d = 1 - covered_density(S, N)
    al, bg, ba = alpha_beta(S)
    nonempty += 1
    if d < al - bg: viol_g += 1
    if d < al - ba: viol_a += 1
print(f"(2) random systems: {nonempty} tested; violations of gcd-version {viol_g} (must be 0); of aligned-version {viol_a} (control: >0 expected)")
ok &= (viol_g == 0 and viol_a > 0)

print("(3) pencil(F_2^2) x exact 1-D cover {0,1 mod 3; 2,5,8 mod 9}")
cov1 = [(3, 0), (3, 1), (9, 2), (9, 5), (9, 8)]
# lattice for (line d in F_2^2, class r mod n): {(k,l): phi_d(k,l) = 0 mod 2, k = r mod n}; as a single form mod 2n via CRT:
# psi(k,l) = n*phi_d(k,l) + 2*u*k  mod 2n with u = inverse of 2 mod n ... realised directly as a set test below
sys3 = [((a, b), n, r) for (a, b) in [(1, 0), (0, 1), (1, 1)] for (n, r) in cov1]
N = 18
miss = sum(1 for k in range(N) for l in range(N) if not any(((a * k + b * l) % 2 == 0 and (k - r) % n == 0) for (a, b), n, r in sys3))
miss_ctrl = sum(1 for k in range(N) for l in range(N) if not any(((a * k + b * l) % 2 == 0 and (k - r) % n == 0) for (a, b), n, r in sys3[:-1]))
# cyclic quotient: image of Z^2 under (phi_d mod 2, k mod n) is Z/2 x Z/n with n odd, cyclic; check the image size = 2n and phi_d primitive
cyc = all(len({((a * k + b * l) % 2, k % n) for k in range(2 * n) for l in range(2)}) == 2 * n and n % 2 == 1 for (a, b), n, r in sys3)
# alignment: is there a primitive v=(x,y) lying in every lattice (a x + b y = 0 mod 2 and x = 0 mod n)? x = 0 mod 9 and all three
# lines mod 2 contain (x,y) mod 2 only if (x,y) = (0,0) mod 2, i.e. v not primitive.
aligned = any(gcd(x, y) == 1 and all((a * x + b * y) % 2 == 0 and x % n == 0 for (a, b), n, r in sys3)
              for x in range(-36, 37) for y in range(-36, 37))
print(f"  uncovered cells on (Z/18)^2: {miss} (0 = covering); control (drop one coset): {miss_ctrl}; all quotients cyclic: {cyc}; common primitive vector in box |v|<=36: {aligned}")
ok &= (miss == 0 and miss_ctrl > 0 and cyc and not aligned)
print("ALL CHECKS PASS" if ok else "SOME CHECK FAILED")
