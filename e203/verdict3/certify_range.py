"""Second-route completeness certificate (certify_pool.py logic) for the e-range (LO, HI].
Claim certified: every prime p (not 2,3) with e_p = lcm(ord_p 2, ord_p 3) in (LO, HI] is in the pool.
Method: for each e in (LO,HI], G(e)=gcd(2^e-1,3^e-1) divided (with multiplicity) by every pool prime whose e_p | e
must leave exactly 1.  (p | G(e)  <=>  e_p | e, p odd, p != 3.)  Levels e <= LO are NOT re-derived here.
Pool primes are re-validated: prime, p not in {2,3}, unique, e_p = lcm(n_order(2),n_order(3)) recomputed.
Usage: certify_range.py LO HI pool1.jsonl [pool2.jsonl ...]  [--control N]  [--skipcheck]
"""
import sys, json, math, time, random, gmpy2
from collections import defaultdict
from sympy import divisors
from sympy.ntheory import n_order
args = [a for a in sys.argv[1:] if not a.startswith('--')]
LO, HI = int(args[0]), int(args[1]); files = args[2:]
ctrl = int(sys.argv[sys.argv.index('--control') + 1]) if '--control' in sys.argv else 0
if ctrl: args = [a for a in args if a != str(ctrl)]; files = [f for f in files if f != str(ctrl)]
pool = []
for f in files: pool += [json.loads(l) for l in open(f)]
pool = [p for p in pool if p['e'] <= HI]
ps = [p['p'] for p in pool]
assert len(set(ps)) == len(ps), 'duplicate primes in pool'
by_e = defaultdict(list); t0 = time.time()
for p in pool:
    q = p['p']; assert q > 3 and gmpy2.is_prime(q, 40) and p['e'] > 0
    if '--skipcheck' not in sys.argv:
        assert math.lcm(int(n_order(2, q)), int(n_order(3, q))) == p['e'], ('bad e', q)
    by_e[p['e']].append(q)
print(f'pool {len(pool)} primes validated in {time.time()-t0:.0f}s; levels in range:',
      sum(len(v) for e, v in by_e.items() if LO < e <= HI), flush=True)

def leftover(e, drop=None):
    g = gmpy2.gcd(gmpy2.mpz(2) ** e - 1, gmpy2.mpz(3) ** e - 1)
    for d in divisors(e):
        for q in by_e.get(d, ()):
            if q == drop: continue
            while g % q == 0: g //= q
    return g

if ctrl:   # planted control: delete one pool prime at a random level, certificate MUST report INCOMPLETE at that level
    rnd = random.Random(12345); cand = [p for p in pool if LO < p['e'] <= HI]
    fired = 0
    for p in rnd.sample(cand, ctrl):
        g = leftover(p['e'], drop=p['p'])
        assert g % p['p'] == 0 and g != 1, ('CONTROL FAILED to fire', p)
        fired += 1
    # and the unplanted check passes at the same levels
    for p in rnd.sample(cand, 5): assert leftover(p['e']) == 1
    print(f'CONTROL: {fired}/{ctrl} planted deletions detected; 5 unplanted levels clean', flush=True); sys.exit(0)

bad = 0; p2 = gmpy2.mpz(2) ** LO; p3 = gmpy2.mpz(3) ** LO; t0 = time.time(); nontriv = 0
for e in range(LO + 1, HI + 1):
    p2 <<= 1; p3 *= 3
    g = gmpy2.gcd(p2 - 1, p3 - 1)
    if g != 1:
        nontriv += 1
        for d in divisors(e):
            for q in by_e.get(d, ()):
                while g % q == 0: g //= q
    if g != 1: bad += 1; print('INCOMPLETE at e =', e, 'leftover bits', g.bit_length(), flush=True)
    if e % 2000 == 0: print(f'progress e={e} bad={bad} nontrivial={nontriv} t={time.time()-t0:.0f}s', flush=True)
print(f'RESULT range ({LO},{HI}] pools {files}: {len(pool)} primes; certified complete: {bad == 0}; nontrivial G levels {nontriv}', flush=True)
