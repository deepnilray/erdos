"""Compare family reps (m,t,u) [p=mut-m-u, mt=1 mod 4] with Chamberland reps (q,r,s1,s2)
[p=qr-4 s1 s2, q=3 mod 4, s1,s2 | (q+1)/4, r>=1] -- Chamberland formulation AS GIVEN IN THE TASK STATEMENT,
not checked against the paper. Chamberland q is searched up to QCAP*p (cap noted in output).
usage: python3 es_compare.py PMAX [bogus]   ('bogus' plants a wrong rule: drop the s|(q+1)/4 requirement)"""
import sys
PMAX = int(sys.argv[1]); bogus = len(sys.argv) > 2; QCAP = 4
def isprime(n):
    if n < 2: return False
    i = 2
    while i * i <= n:
        if n % i == 0: return False
        i += 1
    return True
def fam(p):
    out = set()
    for m in range(3, p + 4, 4):
        for a in range(4, p + m + 1, 4):
            if (p + m) % a == 0 and (a + 1) % m == 0:
                out.add((m, (a + 1) // m, (p + m) // a))
    return out
def divs(n): return [d for d in range(1, n + 1) if n % d == 0]
def cham(p):
    out = set()
    for q in range(3, QCAP * p + 2, 4):
        D = divs((q + 1) // 4)
        for s1 in (range(1, q + 1) if bogus else D):
            for s2 in (range(s1, q + 1) if bogus else [d for d in D if d >= s1]):
                v = p + 4 * s1 * s2
                if v % q == 0 and v // q >= 1: out.add((q, v // q, s1, s2))
    return out
rows = []
for p in range(5, PMAX + 1, 4):
    if not isprime(p): continue
    F, C = fam(p), cham(p)
    Fm = {x[0] for x in F}; Ft = {x[1] for x in F}; Cq = {x[0] for x in C}
    rows.append((p, bool(F), bool(C), Fm <= Cq, Ft <= Cq, Cq <= Fm, Cq <= Ft, Fm == Cq, Ft == Cq))
n = len(rows)
print("mode", "BOGUS" if bogus else "MAIN", "primes p=1 mod 4 in [5,%d]:" % PMAX, n)
print("family has rep:", sum(r[1] for r in rows), " chamberland has rep:", sum(r[2] for r in rows))
for i, name in enumerate(["F.m subset C.q", "F.t subset C.q", "C.q subset F.m", "C.q subset F.t", "F.m == C.q", "F.t == C.q"], 3):
    print(f"{name:16s} holds for {sum(r[i] for r in rows)}/{n}")
print("p with a rep in one but not the other:", [(r[0], r[1], r[2]) for r in rows if r[1] != r[2]][:10])
