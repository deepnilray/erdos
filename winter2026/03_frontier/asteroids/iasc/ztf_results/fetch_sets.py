import json, os, sys, gzip, requests, time
from concurrent.futures import ThreadPoolExecutor
ROOT=sys.argv[1]; SIZE=int(sys.argv[2]) if len(sys.argv)>2 else 2000
sets=json.load(open("sets.json"))
jobs=[]
for s in sets:
    d=os.path.join(ROOT,s["label"]); os.makedirs(os.path.join(d,"mask"),exist_ok=True)
    for ffd in s["files"]:
        base=f"ztf_{ffd}_{s['field']:06d}_{s['filt']}_c{s['ccd']:02d}_o_q{s['q']}"
        url=f"https://irsa.ipac.caltech.edu/ibe/data/ztf/products/sci/{ffd[:4]}/{ffd[4:8]}/{ffd[8:]}/{base}"
        jobs.append((url+"_sciimg.fits",os.path.join(d,base+"_sciimg.fits"),s)); jobs.append((url+"_mskimg.fits",os.path.join(d,"mask",base+"_sciimg.fits"),s))
def get(j):
    url,out,s=j
    if os.path.exists(out) and os.path.getsize(out)>100000: return out,"cached"
    for k in range(5):
        try:
            r=requests.get(url,params=dict(center=f"{s['ra']},{s['dec']}",size=f"{SIZE}pix"),timeout=600)
            if r.status_code==200:
                b=r.content
                if b[:2]==b"\x1f\x8b": b=gzip.decompress(b)
                if b[:6]==b"SIMPLE": open(out,"wb").write(b); return out,len(b)
            err=r.status_code
        except Exception as e: err=e
        time.sleep(5*(k+1))
    return out,f"FAIL {err}"
with ThreadPoolExecutor(4) as ex:
    for o,st in ex.map(get,jobs): print(os.path.basename(os.path.dirname(o)),os.path.basename(o),st,flush=True)
