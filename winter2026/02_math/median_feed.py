#!/usr/bin/env python3
"""Test: if f is the feed (last) vertex of some median order of an oriented graph D and f is adjacent to every
other vertex, is f a Seymour vertex?  Median orders are computed exactly by subset DP (n <= 11).
Control: the same test without the completeness condition (feed vertices with missing edges) is reported too;
a failure there shows the checker can fire.
Usage: median_feed.py n trials missing_prob seed   (missing_prob < 0: delete a random number 0..n of edges from a random tournament)"""
import sys, random
n, trials, pm, seed = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]), int(sys.argv[4])
random.seed(seed)
fails_complete = fails_any = tested_complete = tested_any = 0
example = None
for t in range(trials):
    out = [0] * n
    pairs = [(u, v) for u in range(n) for v in range(u + 1, n)]
    miss = set(random.sample(pairs, random.randint(0, n))) if pm < 0 else set()
    for u in range(n):
        for v in range(u + 1, n):
            if (pm >= 0 and random.random() < pm) or (u, v) in miss:
                continue
            if random.random() < 0.5:
                out[u] |= 1 << v
            else:
                out[v] |= 1 << u
    inn = [sum(1 << u for u in range(n) if out[u] >> v & 1) for v in range(n)]
    full = (1 << n) - 1
    best = [0] * (1 << n)  # best[S] = max forward arcs of an order of S
    for S in range(1, 1 << n):
        b = -1
        m = S
        while m:
            f = (m & -m).bit_length() - 1; m &= m - 1
            val = best[S & ~(1 << f)] + bin(inn[f] & S).count('1')
            if val > b: b = val
        best[S] = b
    OPT = best[full]
    for f in range(n):
        if best[full & ~(1 << f)] + bin(inn[f]).count('1') != OPT:
            continue
        N1 = out[f]; N2 = 0
        for u in range(n):
            if N1 >> u & 1: N2 |= out[u]
        N2 &= ~N1 & ~(1 << f)
        sey = bin(N2).count('1') >= bin(N1).count('1')
        complete = (out[f] | inn[f]) == full & ~(1 << f)
        tested_any += 1; fails_any += not sey
        if complete:
            tested_complete += 1; fails_complete += not sey
            if not sey and example is None: example = [bin(o) for o in out]
print('n', n, 'trials', trials, 'pmiss', pm, '| feed vertices tested', tested_any, 'non-Seymour', fails_any,
      '| complete feed vertices tested', tested_complete, 'non-Seymour', fails_complete)
if example: print('EXAMPLE', example)
