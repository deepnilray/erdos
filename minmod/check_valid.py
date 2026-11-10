#!/usr/bin/env python3
"""Independent checker (pure Python, exact integer arithmetic).
valid(A,N): Fonollosa validity by brute-force DP over multisets of size n.
sign_condition(A,N,box): checks the sign characterization on all relation vectors in a box.
Controls: planted invalid set must be rejected; planted valid set must be accepted."""
import sys, itertools
def valid(A,N):
    n=len(A); p=sum(A)%N
    cnt=[[0]*N for _ in range(n+1)]; cnt[0][0]=1
    for a in A:
        for j in range(1,n+1):
            row=cnt[j]; prev=cnt[j-1]
            for r in range(N):
                row[r]+=prev[(r-a)%N]
    return cnt[n][p]==1
def sign_condition(A,N,box=3):
    n=len(A)
    for x in itertools.product(range(-box,box+1),repeat=n):
        if sum(x)!=0 or not any(x): continue
        if sum(xi*a for xi,a in zip(x,A))%N: continue
        if max(x)<=1 or min(x)>=-1: return False,x
    return True,None
if __name__=="__main__":
    # controls
    assert valid([1,2,4,8],12) and valid([0,1,3,10],15) and valid([1,2,4,8,16],28)
    assert not valid([1,2,4,8],13) and not valid([1,2,4,8,16],24) and not valid([0,1,2],5)
    assert sign_condition([1,2,4,8],12)[0] and not sign_condition([1,2,4,8],13)[0]
    print("controls OK (3 valid accepted, 3 invalid rejected, sign condition agrees)")
    for line in sys.stdin:
        line=line.strip()
        if not line: continue
        N,rest=line.split(":"); N=int(N); A=list(map(int,rest.split()))
        print(N,A,"valid" if valid(A,N) else "INVALID")
