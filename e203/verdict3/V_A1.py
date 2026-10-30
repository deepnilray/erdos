# A(1) = sum_{d | 5*7*...*29} g(d)/e(d), e(d) = |<2,3> mod d| computed as |<a,b>| in prod Z/e_p (forms), exact
import math, itertools, json
from fractions import Fraction as Fr
from sympy.ntheory import n_order, discrete_log
from sympy import primitive_root
ps=[5,7,11,13,17,19,23,29]
form={}
for p in ps:
    e=math.lcm(n_order(2,p),n_order(3,p)); g=primitive_root(p); h=pow(g,(p-1)//e,p)
    form[p]=(int(discrete_log(p,2,h))%e,int(discrete_log(p,3,h))%e,e)
def esize(S):
    if not S: return 1
    E=[form[p][2] for p in S]; a=tuple(form[p][0]%form[p][2] for p in S); b=tuple(form[p][1]%form[p][2] for p in S)
    A=set(); x=tuple(0 for _ in S)
    while x not in A:
        A.add(x); x=tuple((xi+ai)%ei for xi,ai,ei in zip(x,a,E))
    t=1; y=b
    while y not in A:
        t+=1; y=tuple((yi+bi)%ei for yi,bi,ei in zip(y,b,E))
    return len(A)*t
# check against brute force <2,3> mod d for small d
for S in [(5,7),(5,7,11),(7,13),(5,13,17)]:
    d=math.prod(S); G={1}; fr=[1]
    while fr:
        x=fr.pop()
        for m in (2,3):
            y=x*m%d
            if y not in G: G.add(y); fr.append(y)
    assert len(G)==esize(S),(S,len(G),esize(S))
tot=Fr(0)
for k in range(len(ps)+1):
    for S in itertools.combinations(ps,k):
        g=Fr(1)
        for p in S: g*=Fr(1,p-2)
        tot+=g/esize(S)
print("|H_W| =",esize(tuple(ps)),"  A(1) =",float(tot))
