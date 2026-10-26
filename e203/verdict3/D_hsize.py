import math, sys
from sympy import primerange, n_order, primitive_root
from math import gcd
for w in [13,17,19,23,29,31,37]:
    P=list(primerange(5,w))
    # |H| = |<2,3> in prod F_p^x| computed via lattice index: smallest... use exact: order group generated; compute via enumeration of orders
    # |H| = [Z^2 : Lambda], Lambda = {(i,j): 2^i 3^j = 1 mod p all p}. Compute via dlog vectors and Smith/HNF
    from sympy import Matrix, ZZ
    from sympy.matrices.normalforms import smith_normal_form
    k=len(P)
    a=[];b=[]
    for p in P:
        g=primitive_root(p)
        dl={pow(g,e,p):e for e in range(p-1)}
        a.append(dl[2%p]); b.append(dl[3%p])
    # H = image of Z^2 -> prod Z/(p-1): |H| = |<a,b>| in G
    # compute by orders: |<a,b>| = |<a>||<b>|/|<a>cap<b>| ; brute force via set for moderate size
    mods=[p-1 for p in P]
    L=1
    for m in mods: L=L*m//gcd(L,m)
    oa=1;ob=1
    for p in P: oa=oa*n_order(2,p)//gcd(oa,n_order(2,p)); ob=ob*n_order(3,p)//gcd(ob,n_order(3,p))
    # count <a,b> by BFS over i in range(oa): elements a*i + b*j ; |H|=oa*ob/|<a>cap<b>|, find intersection: smallest j>0 with b*j in <a>
    A=set()
    cur=tuple([0]*k)
    for i in range(oa):
        A.add(cur); cur=tuple((x+y)%m for x,y,m in zip(cur,a,mods))
    j=0;cur=tuple([0]*k);jj=None
    for j in range(1,ob+1):
        cur=tuple((x+y)%m for x,y,m in zip(cur,b,mods))
        if cur in A: jj=j;break
    Hsz=oa*jj
    tot=1
    for m in mods: tot*=m
    print(w,P,"ord2",oa,"ord3",ob,"|H|",Hsz,"prod(p-1)",tot,"index",tot//Hsz,"W",math.prod(P))
