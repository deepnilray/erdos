import glob,re,math,sys
tot=0; h={}; best=(0,0,0,0)
for f in sorted(glob.glob('search_l1_*.log')):
    t=open(f).read()
    if '\nDONE' not in '\n'+t: continue
    tot+=int(re.search(r'count=(\d+)',t).group(1))
    for k,v in re.findall(r'(\d+):(\d+)',re.search(r'HIST_LOG2S(.*)',t).group(1)): h[int(k)]=h.get(int(k),0)+int(v)
    b=re.search(r'BEST_S m=(\d+) k=(\d+) l=(\d+) s=(\d+)',t); s=int(b.group(4))
    if s>best[0]: best=(s,int(b.group(1)),int(b.group(2)),int(b.group(3)))
print("files m-count",tot); print("best",best,"log2 s=%.2f"%math.log2(best[0]))
cum=0
for b in sorted(h,reverse=True):
    cum+=h[b]; print(b,h[b],"P(floor log2 s>=b)=%.3e"%(cum/tot))
