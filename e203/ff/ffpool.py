# Function-field analogue of Erdos 203: base primes P=T, Q=T+1 over F_q[T].
# pi irreducible, pi not in {T, T+1}; H_pi = <T,T+1> mod pi (cyclic), e_pi = |H_pi|,
# Lambda_pi = {(k,l): T^k (T+1)^l = 1 mod pi}, index e_pi; coset choice is free (CRT on m).
import sys, math, itertools, json
from sympy import Poly, symbols, GF, factor_list
T=symbols('T')
def pool_for_N(q,N):
    f=Poly(T**N-1,T,modulus=q)
    out=[]
    for fac,mult in f.factor_list()[1]:
        d=fac.degree()
        if fac==Poly(T,T,modulus=q) or fac==Poly(T+1,T,modulus=q): continue
        a=Poly(T,T,modulus=q); b=Poly(T+1,T,modulus=q)
        one=Poly(1,T,modulus=q)
        def pw(x,n):
            r=one; x=x.rem(fac)
            while n:
                if n&1: r=(r*x).rem(fac)
                x=(x*x).rem(fac); n>>=1
            return r
        if pw(b,N)!=one: continue
        # order group: find H = <a,b>; enumerate by powers
        els={}
        # generate subgroup by BFS
        gens=[a.rem(fac),b.rem(fac)]
        H={tuple(one.all_coeffs()):0}
        frontier=[one]
        elems=[one]
        seen={tuple(one.all_coeffs())}
        while frontier:
            nf=[]
            for x in frontier:
                for g in gens:
                    y=(x*g).rem(fac)
                    k=tuple(y.all_coeffs())
                    if k not in seen: seen.add(k); nf.append(y); elems.append(y)
            frontier=nf
        e=len(elems)
        # find generator of cyclic H
        gen=None
        for x in elems:
            r=x;o=1
            while r!=one: r=(r*x).rem(fac); o+=1
            if o==e: gen=x;break
        dl={}
        r=one
        for i in range(e): dl[tuple(r.all_coeffs())]=i; r=(r*gen).rem(fac)
        A=dl[tuple(gens[0].all_coeffs())]; B=dl[tuple(gens[1].all_coeffs())]
        out.append(dict(deg=d,e=e,alpha=A,beta=B,poly=str(fac.as_expr())))
    return out
if __name__=="__main__":
    q=int(sys.argv[1]); Ns=[int(x) for x in sys.argv[2:]]
    for N in Ns:
        P=pool_for_N(q,N)
        s=sum(1/p['e'] for p in P)
        from collections import Counter
        print(f"q={q} N={N}: {len(P)} primes with e|N, sum 1/e = {s:.4f}, e-hist {sorted(Counter(p['e'] for p in P).items())}",flush=True)
        json.dump(P,open(f"pool_q{q}_N{N}.json","w"))
