"""Resumable chunked version of poolE_par.py: primes with E1 < e_p <= E2 (E2 <= 2*E1), one output file per chunk
(verdict2/pool1600k/chunk_<lo>_<hi>.jsonl, written atomically when the chunk finishes), so a restart loses at most
the chunks in flight.  Same mathematics as poolE_par.py: G(e) = gcd(2^e-1, 3^e-1) with primes of proper divisors
removed is exactly the product of primes with e_p = e; every factor is checked prime with lcm(ord 2, ord 3) = e.
  python3 verdict2/pool_chunked.py base.jsonl E1 E2 outdir workers [step]"""
import sys, os, json, math, gmpy2
from collections import defaultdict
from multiprocessing import Pool
from sympy import factorint, divisors, primitive_root, isprime
from sympy.ntheory import n_order, discrete_log
base, E1, E2, outdir, W = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4], int(sys.argv[5])
step = int(sys.argv[6]) if len(sys.argv) > 6 else 2000
assert E2 <= 2 * E1
by_e = defaultdict(list)
for l in open(base):
    p = json.loads(l)
    if p['e'] <= E1: by_e[p['e']].append(p['p'])

def chunk(r):
    lo, hi = r; fn = os.path.join(outdir, f'chunk_{lo}_{hi}.jsonl')
    if os.path.exists(fn): return fn
    new = []
    p2 = gmpy2.mpz(2) ** (lo - 1); p3 = gmpy2.mpz(3) ** (lo - 1)
    for e in range(lo, hi):
        p2 <<= 1; p3 *= 3
        g = gmpy2.gcd(p2 - 1, p3 - 1)
        if g == 1: continue
        for d in divisors(e)[:-1]:
            for q in by_e.get(d, ()):
                while g % q == 0: g //= q
        if g == 1: continue
        for q in factorint(int(g)):
            assert isprime(q)
            assert math.lcm(int(n_order(2, q)), int(n_order(3, q))) == e
            gg = primitive_root(q); h = pow(gg, (q - 1) // e, q)
            a = int(discrete_log(q, 2, h)) % e; b = int(discrete_log(q, 3, h)) % e
            assert pow(h, a, q) == 2 % q and pow(h, b, q) == 3 % q
            new.append(dict(p=int(q), e=e, alpha=a, beta=b))
    tmp = fn + '.tmp'
    with open(tmp, 'w') as fh:
        for d in new: fh.write(json.dumps(d) + '\n')
    os.replace(tmp, fn)
    print('chunk', lo, hi, len(new), flush=True)
    return fn

if __name__ == '__main__':
    os.makedirs(outdir, exist_ok=True)
    rs = [(lo, min(lo + step, E2 + 1)) for lo in range(E1 + 1, E2 + 1, step)]
    todo = [r for r in rs if not os.path.exists(os.path.join(outdir, f'chunk_{r[0]}_{r[1]}.jsonl'))]
    print('chunks total', len(rs), 'todo', len(todo), flush=True)
    with Pool(W) as P: list(P.imap_unordered(chunk, todo, chunksize=1))
    print('ALL CHUNKS DONE', flush=True)
