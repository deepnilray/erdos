# Does "uniform uncovered density >= 1 - B(E)" hold? (claimed in B_noside 3.3 and used in D sec.4)  Test: find real offsets whose UNIFORM covered density exceeds B(E).
import json, numpy as np, sys, math
N=int(sys.argv[1]); Emax=int(sys.argv[2]); sweeps=int(sys.argv[3])
pool=[json.loads(l) for l in open('/home/claude/e203wt/e203/poolE800000.jsonl')]
P=[p for p in pool if p['e']<=Emax and N%p['e']==0]
P.sort(key=lambda p:p['e'])
print("N",N,"primes with e|N, e<=%d: %d, sum 1/e = %.3f"%(Emax,len(P),sum(1/p['e'] for p in P)),flush=True)
K=np.arange(N,dtype=np.int64)
cnt=np.zeros((N,N),dtype=np.uint8)
off=[None]*len(P)
def psi(p): return ((p['alpha']*K[:,None]+p['beta']*K[None,:])%p['e']).astype(np.int32)
rng=np.random.default_rng(1)
for sw in range(sweeps):
    order=list(range(len(P))) if sw==0 else list(rng.permutation(len(P)))
    for i in order:
        p=P[i]; ps=psi(p)
        if off[i] is not None: cnt-= (ps==off[i]).astype(np.uint8)
        unc=(cnt==0)
        b=np.bincount(ps[unc],minlength=p['e']); c=int(b.argmax())
        off[i]=c; cnt+= (ps==c).astype(np.uint8)
    cov=(cnt>0).mean(); print("sweep",sw,"uniform covered density %.5f"%cov,flush=True)
