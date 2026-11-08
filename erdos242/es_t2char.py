"""Test agent claim: n (=1 mod 4) has a Chamberland rep  <=>  exist A,g,d,r>=1: n + r = 4*A*g*d and r | g + d.
Reference = direct Chamberland enumeration (q<=4N+1, s_i | (q+1)/4).  Control: replace 'r | g+d' by 'r | g+d+1'.  usage: python3 es_t2char.py N"""
import sys
N = int(sys.argv[1])
ref = bytearray(N + 1)
for q in range(3, 4 * N + 2, 4):
    h = (q + 1) // 4; D = [d for d in range(1, h + 1) if h % d == 0]
    for s1 in D:
        for s2 in D:
            rho = (4 * s1 * s2) % q; n0 = (-rho) % q
            if n0 < 5: n0 += q
            for n in range(n0, N + 1, q):
                if n % 4 == 1: ref[n] = 1
def build(shift):
    got = bytearray(N + 1)
    for A in range(1, N // 4 + 2):
        for g in range(1, N // (4 * A) + 2):
            for d in range(1, N // (4 * A * g) + 2):
                M = 4 * A * g * d; s = g + d + shift
                if s <= 0: continue
                for r in range(1, M):          # n = M - r >= 5
                    if s % r == 0:
                        n = M - r
                        if 5 <= n <= N and n % 4 == 1: got[n] = 1
    return got
for shift, name in ((0, "MAIN"), (1, "CONTROL (r | g+d+1)")):
    got = build(shift)
    diff = [n for n in range(5, N + 1, 4) if got[n] != ref[n]]
    print(name, "N =", N, "mismatches with Chamberland enumeration:", len(diff), diff[:10])
