#!/usr/bin/env python3
r"""Check the cyclic-order lemma on explicit sets.
For a set A in Z_N and every ordered pair (c,a) whose difference b=a-c is a unit, and all S != S' subsets of A\{a,c}
with |S'| >= |S|, the integer i in [0,N) with x_{S'} - x_S = i*b must satisfy |S'|-|S|+2 <= i <= N-2.
Returns number of violating (pair, S, S') triples."""
import sys, itertools
from math import gcd
def violations(A,N):
    A=list(A); n=len(A); bad=0; tested=0
    for c in A:
        for a in A:
            if a==c: continue
            b=(a-c)%N
            if gcd(b,N)!=1: continue
            binv=pow(b,-1,N)
            rest=[e for e in A if e!=a and e!=c]; m=len(rest)
            pts=[]
            for mask in range(1<<m):
                x=sum((rest[i]-c) for i in range(m) if mask>>i&1)%N
                pts.append(((x*binv)%N, bin(mask).count('1')))
            for (p,w) in pts:
                for (q,v) in pts:
                    if (p,w) is (q,v): continue
                    if v>=w and not (p==q and v==w):
                        i=(q-p)%N; tested+=1
                        if i<v-w+2 or i>N-2: bad+=1
    return bad,tested
if __name__=="__main__":
    tot=0
    for line in sys.stdin:
        line=line.strip()
        if not line: continue
        N,rest=line.split(":"); N=int(N); A=list(map(int,rest.split()))
        bad,t=violations(A,N); tot+=1
        if bad or "-v" in sys.argv: print(N,A,"violations",bad,"of",t)
    print("sets checked:",tot)
