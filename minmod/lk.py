# L_k(n): min N such that exists A=D∪A'' in Z_N, |D|=k, |A''|=n-k, with: every nonzero x in Lambda with |x_l|<=1 off D
# has max>=2 and min<=-2.   brute force with incremental checks.  usage: lk.py k n Nlo Nhi
import sys, itertools
def comps_ge(k,sigma,lo):  # vectors in Z^k with entries >= lo, sum sigma
    # shift: y=x-lo>=0, sum = sigma-k*lo
    t=sigma-k*lo
    if t<0: return
    for c in itertools.combinations(range(t+k-1),k-1):
        prev=-1; y=[]
        for ci in c: y.append(ci-prev-1); prev=ci
        y.append(t+k-1-prev-1)
        yield tuple(v+lo for v in y)
def forb_values(D,N,sigma):
    # residues of sum x_d*d for x_D>=-1 with sum sigma, or x_D<=1 with sum sigma; also flag if x_D=0 among them
    k=len(D); res={}
    for x in comps_ge(k,sigma,-1):
        r=sum(a*b for a,b in zip(x,D))%N
        res.setdefault(r,set()).add(x)
    for y in comps_ge(k,-sigma,-1):
        x=tuple(-v for v in y)
        r=sum(a*b for a,b in zip(x,D))%N
        res.setdefault(r,set()).add(x)
    return res
def ok(D,App,N,cache):
    m=len(App)
    # V_s: residues of z-values by weight, track whether only z=0 gives it
    V={0:{0:1}}  # s -> {residue: count_nonzero_flag}; we store dict residue->min(nonzero count,1)+ (zero vector flag separately)
    vals={(0,0):True}  # (s,res) -> True if only reachable by z=0 so far ... handle simply by enumerating
    cur={(0,0):0}  # (s,res)-> number of nonzero z (capped 1)
    for b in App:
        nxt={}
        for (s,r),c in cur.items():
            for e in (-1,0,1):
                key=(s+e,(r+e*b)%N)
                cc=1 if (c or e!=0) else 0
                if nxt.get(key,0)<cc or key not in nxt: nxt[key]=max(nxt.get(key,0),cc)
        # need to remember if zero vector also maps there: (0,0) with c=0 always exists; mark separately
        cur=nxt
    # cur[(0,0)] may be 1 if a nonzero z has s=0,r=0 ; zero vector always present
    for (s,r),c in cur.items():
        sigma=-s
        if sigma not in cache: cache[sigma]=forb_values(D,N,sigma)
        fv=cache[sigma]
        tgt=(-r)%N
        if tgt in fv:
            xs=fv[tgt]
            if c==1: return False            # nonzero z with a forbidden x_D
            # c==0: z=0 only (s=0,r=0): forbidden unless x_D=0 only
            if any(any(v!=0 for v in x) for x in xs): return False
    return True
def search(k,n,N):
    m=n-k
    for Drest in itertools.combinations(range(1,N),k-1):
        D=(0,)+Drest; cache={}
        if not ok(D,[],N,cache): continue
        def rec(App,start):
            if len(App)==m: return App
            for b in range(start,N):
                if b in D: continue
                A2=App+[b]
                if ok(D,A2,N,cache):
                    r=rec(A2,b+1)
                    if r: return r
            return None
        r=rec([],1)
        if r is not None: return D,r
    return None
k,n,Nlo,Nhi=map(int,sys.argv[1:5])
for N in range(Nlo,Nhi+1):
    r=search(k,n,N)
    if r: print("k=%d n=%d min N=%d example D=%s A''=%s"%(k,n,N,r[0],r[1])); break
else: print("k=%d n=%d none in [%d,%d]"%(k,n,Nlo,Nhi))
