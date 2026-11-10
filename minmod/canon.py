import sys
from math import gcd
def canon(A,N):
    best=None
    for u in range(1,N):
        if gcd(u,N)!=1: continue
        Bm=[(u*a)%N for a in A]
        for t in Bm:
            C=tuple(sorted((b-t)%N for b in Bm))
            if best is None or C<best: best=C
    return best
N=int(sys.argv[1]); S=set()
for line in sys.stdin:
    A=list(map(int,line.split())); S.add(canon(A,N))
for c in sorted(S): print(N,c)
