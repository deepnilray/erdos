"""Priority check: is the Type I family (m,t,u: n = mut-m-u, m=t=3 mod 4) the same SET of integers as
Elsholtz-Tao Prop 2.3 / Nakayama form  n = 4acd - f, f | 4a^2 d + 1  (a,c,d,f >= 1; E-T also require gcd(c,n)=1 -- tested with and without)?
Control: replace f | 4a^2d+1 by f | 4a^2d+2.   usage: python3 es_nakayama.py N"""
import sys, math
N = int(sys.argv[1])
fam = bytearray(N + 1)
for m in range(3, N + 4, 4):
    for t in range(3, (N + m) // m + 3, 4):
        a = m * t - 1
        for n in range(a - m, N + 1, a):
            if n >= 5 and n % 4 == 1: fam[n] = 1
def nak(shift, coprime):
    got = bytearray(N + 1)
    for a in range(1, N + 2):
        for d in range(1, (N + 4 * a * a) // (4 * a) + 2):
            M = 4 * a * a * d + 1 + shift
            if M <= 0: continue
            # f | M ; n = 4acd - f  =>  c = (n+f)/(4ad)
            divs = [f for f in range(1, int(M ** .5) + 1) if M % f == 0]
            for f0 in divs:
                for f in {f0, M // f0}:
                    c = 1
                    while True:
                        n = 4 * a * c * d - f
                        if n > N: break
                        if n >= 5 and n % 4 == 1 and (not coprime or math.gcd(c, n) == 1): got[n] = 1
                        c += 1
        if 4 * a > N + 4: break
    return got
for name, shift, cop in (("MAIN (with gcd(c,n)=1)", 0, True), ("MAIN (no gcd condition)", 0, False), ("CONTROL f | 4a^2d+2", 1, False)):
    g = nak(shift, cop)
    onlyF = [n for n in range(5, N + 1, 4) if fam[n] and not g[n]]
    onlyN = [n for n in range(5, N + 1, 4) if g[n] and not fam[n]]
    print(name, "| in family not Nakayama:", len(onlyF), onlyF[:8], "| in Nakayama not family:", len(onlyN), onlyN[:8])
