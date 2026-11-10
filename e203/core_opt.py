import sys, json, lattice, exact
pool = {r['p']: r for r in lattice.load(sys.argv[1])}
S = [pool[int(x)] for x in sys.argv[2].split(',')]
H = [[1, 0], [0, 1]]
for p in S: H = lattice.intersect(p, H)
r = exact.solve(S, H, tlimit=float(sys.argv[3]), workers=4)
print(json.dumps(dict(core=[p['p'] for p in S], cells=r['n'], status=r['status'], best=r['best'], bound=r['bound'],
                      best_frac=r['best']/r['n'], bound_frac=r['bound']/r['n'], time=round(r['time']))), flush=True)
