#!/usr/bin/env python3
"""Independent checker: reads an 'arcs: [...]' line, prints for each vertex (d+, |N2|), Seymour status,
min outdegree, whether vertex 0 is complete, and the sets A = N+(0), B = N2(0), C = rest."""
import sys, ast
line = [l for l in open(sys.argv[1]) if l.startswith('arcs:')][0]
arcs = ast.literal_eval(line[5:].strip())
n = 1 + max(max(a) for a in arcs)
out = {v: set() for v in range(n)}
for u, v in arcs:
    assert v not in out[u] and u not in out[v], 'not oriented'
    out[u].add(v)
for v in range(n):
    N2 = set().union(*[out[u] for u in out[v]]) - out[v] - {v}
    print(v, 'd+', len(out[v]), '|N2|', len(N2), 'Seymour' if len(N2) >= len(out[v]) else '-')
print('n', n, 'min outdegree', min(len(out[v]) for v in range(n)))
print('0 complete:', all(v in out[0] or 0 in out[v] for v in range(1, n)))
A = out[0]; B = set().union(*[out[a] for a in A]) - A - {0}; C = set(range(n)) - A - B - {0}
print('A', sorted(A), 'B', sorted(B), 'C', sorted(C))
