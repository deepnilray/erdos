import math, itertools
def lats(e):  # all index-e sublattices of Z^2 in HNF (a,b;0,c): vectors (a,0),(b,c), 0<=b<a, a*c=e
    for a in range(1,e+1):
        if e%a==0:
            c=e//a
            for b in range(a): yield (a,b,c)
def contains(L,v):
    a,b,c=L; x,y=v
    if y%c: return False
    return (x-(y//c)*b)%a==0
bad=0; nonprim_bad=0; tot=0
for e in range(2,41):
    Ls=list(lats(e))
    for v in itertools.product(range(-8,9),repeat=2):
        if v==(0,0): continue
        S=[L for L in Ls if contains(L,v)]
        if math.gcd(abs(v[0]),abs(v[1]))==1:
            tot+=1
            if len(S)>1: bad+=1
        elif len(S)>1: nonprim_bad+=1
print("primitive v: pairs checked",tot,"cases with >1 lattice:",bad,"| non-primitive v with >1 lattice:",nonprim_bad)
