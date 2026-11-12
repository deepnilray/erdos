"""Exact, independent facet-incidence and affine-dimension audit for Q_m.
No numerical tolerance; not a universal proof.
"""
from itertools import permutations, product, combinations
from math import factorial
from sympy import Matrix

def audit(m):
    vertices = [(tuple(p), tuple(s)) for p in permutations(range(1,m+1))
                for s in product((-1,1),repeat=m)]
    assert len(vertices)==factorial(m)*2**m
    facets=[]
    for i in range(m):
        for sign in (-1,1):
            facets.append(('cube',i,sign))
    for k in range(1,m):
        for I in combinations(range(m),k):
            facets.append(('perm',I,k*(k+1)//2))
    def slack(f,v):
        a,b=v
        if f[0]=='cube':return 1-f[2]*b[f[1]]
        return sum(a[i] for i in f[1])-f[2]
    assert all(slack(f,v)>=0 for f in facets for v in vertices)
    incidences=[sum(slack(f,v)==0 for f in facets) for v in vertices]
    assert set(incidences)=={2*m-1},(m,set(incidences))
    # Each proposed facet has an affinely independent set of dimension 2m-2.
    base=[tuple(2*a-0.5-b/2 if j%2==0 else 2*a-0.5+b/2
                for a,b in zip(v[0],v[1]) for j in (0,1)) for v in vertices]
    # Coordinate form of affine hull: sum a_i fixed; cube unconstrained.
    av=[tuple(a)+tuple(b) for a,b in vertices]
    def rank(points):
        x=points[0]
        return Matrix([[y[i]-x[i] for i in range(2*m)] for y in points[1:]]).rank()
    assert rank(av)==2*m-1
    for f in facets:
        face=[v for v in av if slack(f,(v[:m],v[m:]))==0]
        assert rank(face)==2*m-2,(m,f)
    print(f'm={m}: {len(vertices)} vertices; dimension {2*m-1}; '
          f'{len(facets)} genuine facets; {2*m-1} facets per vertex: PASS')

for m in range(1,5):audit(m)
