"""Independent, exact combinatorial checks (not a proof for arbitrary m)."""
from itertools import permutations, product
from math import factorial

def vertices(m):
    for p in permutations(range(1,m+1)):
        for signs in product((-1,1), repeat=m):
            x=[]
            for a,b in zip(p,signs):
                x += [2*a-1 if b==1 else 2*a, 2*a if b==1 else 2*a-1]
            yield tuple(x), p, signs

def is_wachs(x):
    n=len(x)
    inv={v:i for i,v in enumerate(x)}
    return all(abs(inv[2*i-1]-inv[2*i]) == 1 for i in range(1,n//2+1))

for m in range(1,6):
    V=list(vertices(m))
    assert len(V)==factorial(m)*2**m
    assert len(set(x for x,_,_ in V))==len(V)
    assert all(is_wachs(x) for x,_,_ in V)
    assert all(tuple((x[2*i]+x[2*i+1]+1)//4 for i in range(m))==p for x,p,s in V)
    assert all(tuple(x[2*i+1]-x[2*i] for i in range(m))==s for x,p,s in V)
    if m<=3:
        true_set={p for p in permutations(range(1,2*m+1)) if is_wachs(p)}
        assert true_set==set(x for x,_,_ in V)
    print(f'm={m}: OK, {len(V)} permutations; predicted dim={2*m-1}, edges={(2*m-1)*len(V)//2}')
