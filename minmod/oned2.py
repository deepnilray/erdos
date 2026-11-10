import sys, itertools
def check(betas,N):
    m=len(betas); P=[]
    for mask in range(1<<m):
        P.append((sum(betas[i] for i in range(m) if mask>>i&1)%N, bin(mask).count('1')))
    for (p,w) in P:
        for (q,v) in P:
            if (p,w)==(q,v): continue
            if v>=w:
                d=(q-p)%N
                if d<v-w+2 or d>N-2: return None
    return sorted(P)
def allsol(m,N):
    out=[]
    def rec(bs,start):
        if len(bs)==m:
            out.append(tuple(bs)); return
        for b in range(start,N):
            if check(bs+[b],N): rec(bs+[b],b+1)
    rec([],1); return out
m=int(sys.argv[1]); 
for N in range(int(sys.argv[2]),int(sys.argv[3])+1):
    sols=allsol(m,N)
    print("m",m,"N",N,"#sol",len(sols))
    for s in sols[:int(sys.argv[4])]:
        P=check(list(s),N); gaps=[(P[(i+1)%len(P)][0]-P[i][0])%N for i in range(len(P))]
        print("   ",s,"w:",[w for p,w in P],"gaps:",gaps)
