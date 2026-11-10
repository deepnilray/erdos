# Brute-force test of Lettl-Sun Thm1.3 (irredundant coset t of a cover of G=(Z/N)^2: k >= 1+f([G:G_t]), [G:G_t]<=2^(k-1))
import random, itertools, math
from sympy import factorint
random.seed(3)
def f(n): return sum(v*(p-1) for p,v in factorint(n).items())
def subgroup(gens,N):
    S={(0,0)}; fr=[(0,0)]
    while fr:
        x=fr.pop()
        for g in gens:
            y=((x[0]+g[0])%N,(x[1]+g[1])%N)
            if y not in S: S.add(y); fr.append(y)
    return frozenset(S)
viol=0; tested=0; tight=0; ks=set()
for N in (6,12,8,9,10):
  pts=[(i,j) for i in range(N) for j in range(N)]
  subs=set()
  for _ in range(400):
      subs.add(subgroup([(random.randrange(N),random.randrange(N)) for _ in range(random.choice([1,2]))],N))
  subs=[s for s in subs if len(s)<N*N]
  for trial in range(600):
      cos=[]; cov=set()
      while len(cov)<N*N:
          H=random.choice(subs); a=random.choice(pts)
          C=frozenset(((a[0]+h[0])%N,(a[1]+h[1])%N) for h in H)
          if C-cov: cos.append((C,len(H))); cov|=C
      # prune to minimal
      random.shuffle(cos); i=0
      while i<len(cos):
          rest=set().union(*[c for j,(c,_) in enumerate(cos) if j!=i]) if len(cos)>1 else set()
          if len(rest)==N*N: cos.pop(i)
          else: i+=1
      k=len(cos)
      for C,h in cos:
          idx=N*N//h; tested+=1
          if not(k>=1+f(idx) and idx<=2**(k-1)): viol+=1; print("VIOL",N,k,idx)
          if k==1+f(idx): tight+=1
print("tested",tested,"violations",viol,"tight",tight)
# planted failure: weaker (wrong) bound k>=2+f must fail on tight cases
