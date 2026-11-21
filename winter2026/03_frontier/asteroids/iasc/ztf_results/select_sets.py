import json, numpy as np, sys
S=json.load(open("survey.json"))
# (field, ccd, q, filt, night-date prefix, label)
WANT=[("569","3","1","zr","2019-02-08","Z1"),("519","6","3","zr","2019-02-10","Z2"),("503","7","2","zr","2019-10-23","Z3"),
      ("504","15","3","zr","2019-10-26","Z4"),("567","11","2","zr","2019-01-28","Z5"),("563","9","3","zr","2024-01-08","Z6"),
      ("612","3","2","zr","2020-01-02","Z7"),("335","5","2","zr","2019-07-10","Z8")]
NMAX, WIN = 12, 120.0
from astropy.time import Time
sets=[]
for f,c,q,flt,date,lab in WANT:
    rows={}
    for v in S.values():
        for r in v["rows"]:
            if r["field"]==f and r["ccdid"]==c and r["qid"]==q and r["filtercode"]==flt and int(r["infobits"] or 0)==0:
                t=Time(float(r["obsjd"]),format="jd")
                if abs(t.mjd-Time(date+"T08:00").mjd)<0.5: rows[r["filefracday"]]=r
    rows=sorted(rows.values(),key=lambda r:float(r["obsjd"]))
    see=np.array([float(r["seeing"]) for r in rows]); rows=[r for r,s in zip(rows,see) if s<1.4*np.median(see)]
    t=np.array([float(r["obsjd"]) for r in rows])*1440
    best=(0,0,0)
    for i in range(len(t)):
        j=np.searchsorted(t,t[i]+WIN,side="right")
        sc=min(j-i,NMAX)*min(t[j-1]-t[i],WIN)
        if sc>best[0]: best=(sc,i,j)
    _,i,j=best; sub=rows[i:j]; tt=t[i:j]
    if len(sub)>NMAX:
        tgt=np.linspace(tt[0],tt[-1],NMAX); idx=sorted(set(int(np.argmin(abs(tt-x))) for x in tgt)); sub=[sub[k] for k in idx]
    ra=np.median([float(r["ra"]) for r in sub]); dec=np.median([float(r["dec"]) for r in sub])
    sets.append(dict(label=lab,field=int(f),ccd=int(c),q=int(q),filt=flt,ra=ra,dec=dec,files=[r["filefracday"] for r in sub],
        obsjd=[float(r["obsjd"]) for r in sub],seeing=[float(r["seeing"]) for r in sub],maglim=[float(r["maglimit"]) for r in sub],gid=sorted(set(r["ipac_gid"] for r in sub))))
    s=sets[-1]; print(lab,f,c,q,len(sub),"span %.1f min"%((s["obsjd"][-1]-s["obsjd"][0])*1440),Time(s["obsjd"][0],format="jd").iso,"see %.2f lim %.2f"%(np.median(s["seeing"]),np.median(s["maglim"])),s["gid"])
json.dump(sets,open("sets.json","w"),indent=1)
