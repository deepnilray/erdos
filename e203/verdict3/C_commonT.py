"""C_commonT.py -- common discrete-log family (C_allE.md section 1.2).
For p with 3 in <2> (gcd(alpha,e)=1) let t_p = beta/alpha mod e_p (3 = 2^t mod p), o_p = e_p.
 * checks 2^t = 3 mod p directly
 * quadratic-character split  (3/p) = (2/p)^T
 * exact maximum of sum 1/e_p over pairwise-compatible families (T exists with T = t_p mod e_p for all p), branch and bound
usage: python3 verdict3/C_commonT.py E1,E2,...
"""
import sys, json, math, time
sys.path.insert(0, '.')
import lattice as LT
pool = LT.load('poolE800000.jsonl')
fam = []
for q in pool:
    a, b, e = q['alpha'], q['beta'], q['e']
    if math.gcd(a, e) == 1:
        t = b * pow(a, -1, e) % e if e > 1 else 0
        fam.append((e, t, q['p']))
        assert pow(2, t, q['p']) == 3 % q['p'], q
fam.sort()
print('pool %d primes; 3 in <2> for %d of them' % (len(pool), len(fam)))
def leg(a, p): return 1 if pow(a, (p - 1) // 2, p) == 1 else -1
for E in [2000, 20000, 200000, 800000]:
    sub = [f for f in fam if f[0] <= E]
    S = sum(1 / f[0] for f in sub); allS = sum(1 / q['e'] for q in pool if q['e'] <= E)
    ev = sum(1 / e for e, t, p in sub if leg(3, p) == 1)                      # allowed when T even
    od = sum(1 / e for e, t, p in sub if leg(3, p) == leg(2, p))              # allowed when T odd
    # sanity: the t_p parity forced by the character matches (control)
    for e, t, p in sub[:2000]:
        if e % 2 == 0:
            assert leg(3, p) == leg(2, p) ** t, (e, t, p)
    print('E=%7d  sum1/e (pool) %.4f   (3 in <2>) %.4f   T even-compatible %.4f   T odd-compatible %.4f' % (E, allS, S, ev, od))
# B&B
def maxfam(sub, tlimit=600):
    sub = sorted(sub, key=lambda f: f[0])           # heavy first
    n = len(sub); w = [1.0 / f[0] for f in sub]
    best = [0.0, []]; t0 = time.time(); nodes = [0]
    def rec(cands, cur, curw, T0, M0, chosen):
        nodes[0] += 1
        if curw > best[0]: best[0] = curw; best[1] = list(chosen)
        if time.time() - t0 > tlimit: return
        rest = sum(w[i] for i in cands)
        if curw + rest <= best[0] + 1e-15: return
        for pos, i in enumerate(cands):
            if curw + sum(w[j] for j in cands[pos:]) <= best[0] + 1e-15: return
            e, t, p = sub[i]
            g = math.gcd(M0, e)
            # new state
            if M0 == 1: T1, M1 = t % e, e
            else:
                # solve T = T0 mod M0, T = t mod e
                m1, m2 = M0 // g, e // g
                k = ((t - T0) // g * pow(m1, -1, m2)) % m2 if m2 > 1 else 0
                T1 = T0 + M0 * k; M1 = M0 * m2
            newc = []
            for j in cands[pos + 1:]:
                ej, tj, pj = sub[j]
                gj = math.gcd(M1, ej)
                if (T1 - tj) % gj == 0: newc.append(j)
            chosen.append(sub[i][2]); rec(newc, cur + 1, curw + w[i], T1, M1, chosen); chosen.pop()
    rec(list(range(n)), 0, 0.0, 0, 1, [])
    return best[0], best[1], nodes[0], time.time() - t0
for E in [int(x) for x in (sys.argv[1] if len(sys.argv) > 1 else '500,2000,5000').split(',')]:
    sub = [f for f in fam if f[0] <= E]
    b, ch, nn, dt = maxfam(sub)
    print('E=%d: max compatible mass %.5f using %d primes (nodes %d, %.1fs)  primes %s' % (E, b, len(ch), nn, dt, ch[:12]))
