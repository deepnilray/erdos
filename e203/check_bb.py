"""Independent check of minunion.c / maxratio.c (branch and bound + symmetry) against plain exhaustive
enumeration (numpy, no pruning, no symmetry) on a reduced heavy family where exhaustion is feasible."""
import json, itertools, subprocess, numpy as np, rtypes as R
pool = {json.loads(l)['p']: json.loads(l) for l in open('poolE200000.jsonl')}
Hs = [pool[p] for p in [5, 7, 13, 17, 19]]
types = json.load(open('types_E200000.json')); keys = list(types)[:3]
M = 144; k, l = np.meshgrid(np.arange(M), np.arange(M), indexing='ij')
vals = [((h['alpha'] * k + h['beta'] * l) % h['e']).ravel() for h in Hs]
lam = 0.0485
for key in keys:
    a, c, d = map(int, key.split(','))
    inA = np.zeros(M * M, bool)
    for x in range(M):
        for y in range(M): inA[((x * a) % M) * M + ((x * c + y * d) % M)] = True
    best_min, best_ratio = 2.0, 0.0
    for offs in itertools.product(*[range(h['e']) for h in Hs]):
        cov = np.zeros(M * M, bool)
        for v, o in zip(vals, offs): cov |= v == o
        ca = cov[inA].mean(); cg = cov.mean()
        best_min = min(best_min, ca); best_ratio = max(best_ratio, (1 - ca) / (1 - cg - lam))
    tail = f"{len(Hs)} " + " ".join(f"{h['alpha']} {h['beta']} {h['e']}" for h in Hs)
    mu = subprocess.run(['./minunion'], input=f"144 {a} {c} 0 {d} " + tail, capture_output=True, text=True).stdout.split()
    mr = subprocess.run(['./maxratio'], input=f"144 {a} {c} 0 {d} 485 10000 " + tail, capture_output=True, text=True).stdout.split()
    print(f"type {key}: minU exhaustive {best_min:.10f} vs B&B {int(mu[0])/int(mu[1]):.10f} | "
          f"R exhaustive {best_ratio:.10f} vs B&B {float(mr[0]):.10f}", flush=True)
