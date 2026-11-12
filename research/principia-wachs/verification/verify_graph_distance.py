"""Independent graph BFS check for the graph-distance corollary, m <= 4."""
from itertools import permutations, product
from collections import deque

def inv(p):
    return sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))

def check(m):
    perms=list(permutations(range(m)))
    signs=list(product((-1,1),repeat=m))
    start=(tuple(range(m)),(-1,)*m)
    def neighbors(v):
        p,e=v
        for k in range(m-1):
            pp=tuple(k+1 if x==k else k if x==k+1 else x for x in p)
            yield (pp,e)
        for k in range(m):
            ee=list(e);ee[k]*=-1
            yield (p,tuple(ee))
    dist={start:0};queue=deque([start])
    while queue:
        v=queue.popleft()
        for w in neighbors(v):
            if w not in dist:
                dist[w]=dist[v]+1;queue.append(w)
    assert len(dist)==len(perms)*len(signs)
    for (p,e),d in dist.items():
        assert d==inv(p)+sum(x==1 for x in e),(m,p,e,d)
    assert max(dist.values())==m*(m+1)//2
    print(f'm={m}: {len(dist)} vertices; graph diameter {max(dist.values())}: PASS')

if __name__=='__main__':
    for m in range(1,5):check(m)
