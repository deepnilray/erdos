# For each y: choose odd c by CRT so that 1-4c is a quadratic NON-residue mod every odd prime p<=y.
# Then q(t)=t^2+t+c is y-rough for ALL t (convex, gaps 2t+2, curvature 2).
# Control: forcing 1-4c to be a residue mod 5 must produce a term divisible by 5.
def primes(n): return [p for p in range(2,n+1) if all(p%d for d in range(2,int(p**.5)+1))]
def leg(a,p): a%=p; return 0 if a==0 else (1 if pow(a,(p-1)//2,p)==1 else -1)
def crt(ms,rs):
    M=1; x=0
    for m,r in zip(ms,rs):
        # solve x' = x mod M, x' = r mod m
        t=((r-x)*pow(M,-1,m))%m; x+=M*t; M*=m
    return x
def pick_c(y,bad=None):
    ms=[2]; rs=[1]
    for p in primes(y)[1:]:
        want = 1 if p==bad else -1
        c=next(c for c in range(p) if leg(1-4*c,p)==want); ms.append(p); rs.append(c)
    return crt(ms,rs)
def first_bad(c,y,T):
    ps=primes(y)
    for t in range(T):
        v=t*t+t+c
        for p in ps:
            if v%p==0 and v!=p: return (t,p)
    return None
for y in [7,13,29,53]:
    c=pick_c(y); print("y",y,"c",c,"first non-rough t<200000:",first_bad(c,y,200000))
    cb=pick_c(y,bad=5); print("   control c",cb,"->",first_bad(cb,y,200000))
