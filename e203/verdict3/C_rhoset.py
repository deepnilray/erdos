"""Enumerate once the e-sets used by C_size.py's rho_max bound, as sparse prime-incidence matrices, so rho_max(delta) is a sparse matvec.
smooth set A: minimal 400-smooth e in (E0, 64 E0] (DFS stops at first product > E0): rows (e, primes>=5 dividing e, r(e)).
set Bm: all 400-smooth m <= E0 (for e = m * (large primes))."""
import sympy, numpy as np, scipy.sparse as sp, pickle
E0=800000; LIM=64*E0; qs=list(sympy.primerange(5,401)); allp=[2,3]+qs; pi={q:i for i,q in enumerate(qs)}
A=[]; 
import sys; sys.setrecursionlimit(10000)
def dfs(i,m,used):
    if m>E0: A.append((m,tuple(used))); return
    for j in range(i,len(allp)):
        q=allp[j]; mm=m
        while True:
            mm*=q
            if mm>LIM: break
            u=used+[pi[q]] if (q>=5 and (not used or used[-1]!=pi[q])) and q>=5 else used
            if q>=5: u=used+[pi[q]]
            dfs(j+1,mm,u)
            if mm>E0: break
dfs(0,1,[])
Bm=[]
def dfs2(i,m,used):
    Bm.append((m,tuple(used)))
    for j in range(i,len(allp)):
        q=allp[j]; mm=m*q
        if mm>E0: continue
        dfs2(j+1,mm,used+([pi[q]] if q>=5 else []))
dfs2(0,1,[])
print(len(A),len(Bm))
def mat(rows):
    r=[];c=[]
    for k,(m,u) in enumerate(rows):
        for x in u: r.append(k);c.append(x)
    return sp.csr_matrix((np.ones(len(r)),(r,c)),shape=(len(rows),len(qs)))
pickle.dump(dict(qs=qs,Ae=np.array([a[0] for a in A],dtype=float),AS=mat(A),Bme=np.array([b[0] for b in Bm],dtype=float),BS=mat(Bm)),open('/tmp/claude-0/-home-claude/89603433-4fa1-57e4-a8fc-4d2490c5f294/scratchpad/rhoset.pkl','wb'))
