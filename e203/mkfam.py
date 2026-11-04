"""Emit a C header describing family S on G_S = Z^2/cap L_p (HNF [[A,0],[C,D]])."""
import sys, lattice
pool = {r['p']: r for r in lattice.load(sys.argv[1])}
S = [pool[int(x)] for x in sys.argv[2].split(',')]
H = [[1, 0], [0, 1]]
for p in S: H = lattice.intersect(p, H)
(a, _), (c, d) = H
with open(sys.argv[3], 'w') as f:
    f.write(f"#define NP {len(S)}\n#define A {a}\n#define C {c}\n#define D {d}\n")
    f.write("static const long P[NP]={%s};\n" % ','.join(str(p['p']) for p in S))
    for k, key in (('E', 'e'), ('AL', 'alpha'), ('BE', 'beta')):
        f.write("static const long %s[NP]={%s};\n" % (k, ','.join(str(p[key]) for p in S)))
print('cells', a * d, 'sum1/e', sum(1 / p['e'] for p in S))
