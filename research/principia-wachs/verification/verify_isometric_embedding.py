"""Exact graph-distance check, independent BFS versus inversion/sign Hamming formula."""
from itertools import permutations, product
from collections import deque

def signature(p,s):
    pos={v:i for i,v in enumerate(p)}
    return tuple(pos[a]<pos[b] for a in range(1,len(p)+1) for b in range(a+1,len(p)+1))+tuple(s)

def audit(m):
    vertices=list(product(permutations(range(1,m+1)),product((0,1),repeat=m)))
    index={v:i for i,v in enumerate(vertices)}
    adj=[]
    for p,s in vertices:
        nbr=[]
        for j in range(m-1):
            q=list(p);q[j],q[j+1]=q[j+1],q[j]
            nbr.append(index[(tuple(q),s)])
        for j in range(m):
            t=list(s);t[j]^=1
            nbr.append(index[(p,tuple(t))])
        adj.append(nbr)
    signatures=[signature(*v) for v in vertices]
    diameter=0
    for start in range(len(vertices)):
        dist=[-1]*len(vertices);dist[start]=0
        queue=deque([start])
        while queue:
            v=queue.popleft()
            for w in adj[v]:
                if dist[w]<0:
                    dist[w]=dist[v]+1;queue.append(w)
        assert -1 not in dist
        for j,d in enumerate(dist):
            h=sum(a!=b for a,b in zip(signatures[start],signatures[j]))
            assert d==h,(m,start,j,d,h)
        diameter=max(diameter,max(dist))
    assert diameter==m*(m+1)//2
    print(f'm={m}: {len(vertices)} vertices; {len(vertices)**2} ordered vertex pairs; diameter {diameter}; PASS')

if __name__=='__main__':
    for m in range(1,5):audit(m)
