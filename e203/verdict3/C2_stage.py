# C2_stage.py: stage first moments mu_l = sum_{p: P+(e_p)=l} 1/(e_p/l^v) in pool, vs sqrt(l); lattice occupancy.
import json, math, collections
from sympy import factorint
rows=[json.loads(l) for l in open('poolE800000.jsonl')]
mu=collections.defaultdict(float); cnt=collections.Counter(); M2=0.0
ce=collections.Counter(r['e'] for r in rows)
for r in rows:
    e=r['e']
    if e<5: continue
    f=factorint(e); l=max(f)
    if l<5: continue
    mu[l]+=l**f[l]/e   # 1/e'
    cnt[l]+=1
print('stages',len(mu))
tot=sum((m/l)**2 for l,m in mu.items())
print('sum_l (mu_l/l)^2 over pool stages l>=5 = %.5f'%tot)
for lo,hi in ((5,30),(30,100),(100,1000),(1000,10**4),(10**4,10**5),(10**5,10**7)):
    s=[(l,m) for l,m in mu.items() if lo<=l<hi]
    if s: print('l in [%d,%d): stages %d, max mu/sqrt(l)=%.4f, max mu/l=%.5f, sum (mu/l)^2=%.3e'%(lo,hi,len(s),max(m/l**.5 for l,m in s),max(m/l for l,m in s),sum((m/l)**2 for l,m in s)))
# lattice occupancy
def psi(e):
    r=e
    for q in factorint(e): r=r*(q+1)//q
    return r
import random; random.seed(2)
samp=random.sample(rows,3000)
occ=sum(1/psi(r['e']) for r in rows)
print('sum over pool primes of 1/psi(e) = %.2f (primes %d): mean lattice occupancy prob scale'%(occ,len(rows)))
print('c(e)=1 for 88.5%%; max c(e)=%d'%max(ce.values()))
