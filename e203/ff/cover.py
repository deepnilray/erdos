import json, sys, random, numpy as np
def run(poolfile,N,iters=200000,seed=1):
    random.seed(seed)
    P=json.load(open(poolfile)); n=len(P)
    k,l=np.meshgrid(np.arange(N),np.arange(N),indexing='ij')
    lab=[((p['alpha']*k+p['beta']*l)%p['e']).ravel() for p in P]
    cnt=np.zeros(N*N,dtype=np.int32); ch=[random.randrange(p['e']) for p in P]
    for i,p in enumerate(P): cnt+= (lab[i]==ch[i])
    def unc(): return int((cnt==0).sum())
    cur=unc(); best=cur
    for it in range(iters):
        i=random.randrange(n); old=ch[i]; new=random.randrange(P[i]['e'])
        if new==old: continue
        cnt-= (lab[i]==old); cnt+= (lab[i]==new)
        u=unc()
        if u<=cur or random.random()<np.exp((cur-u)/max(1.0,(0.002*N*N)*(1-it/iters)+1e-9)):
            cur=u; ch[i]=new; best=min(best,cur)
        else:
            cnt-= (lab[i]==new); cnt+= (lab[i]==old)
        if best==0: break
    return n, sum(1/p['e'] for p in P), best, N*N
if __name__=="__main__":
    f=sys.argv[1]; N=int(sys.argv[2])
    print(f, run(f,N,int(sys.argv[3]) if len(sys.argv)>3 else 20000))
