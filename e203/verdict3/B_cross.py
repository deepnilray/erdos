import sys, gmpy2
from collections import Counter
M0,M1=int(sys.argv[1]),int(sys.argv[2]); minl=int(sys.argv[3])
S=sorted((2**k*3**l,k,l) for k in range(63) for l in range(41) if 2**k*3**l<2**63)
h=Counter(); surv=0
for m in range(M0,M1+1):
    if m%2==0 or m%3==0: continue
    for i,(s,k,l) in enumerate(S):
        if k==0 or l<minl: continue
        if s*m+1>=2**64: surv+=1; break
        if gmpy2.is_prime(s*m+1,30): h[i]+=1; break
print("SURV",surv); print("HIST_RANK"," ".join(f"{i}:{h[i]}" for i in sorted(h)))
