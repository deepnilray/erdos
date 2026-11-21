import json, sys, numpy as np, collections
from astropy.coordinates import SkyCoord, get_sun, GeocentricTrueEcliptic
from astropy.time import Time
import astropy.units as u
S=json.load(open(sys.argv[1])); out=[]
for key,v in S.items():
    ra,dec=map(float,key.split(","))
    G=collections.defaultdict(list)
    for r in v["rows"]:
        if int(r["infobits"] or 0)!=0: continue
        jd=float(r["obsjd"]); G[(r["field"],r["ccdid"],r["qid"],r["filtercode"],int(np.floor(jd-0.2)))].append(r)
    for k,rows in G.items():
        if len(rows)<6: continue
        rows=sorted(rows,key=lambda r:float(r["obsjd"])); t=np.array([float(r["obsjd"]) for r in rows])
        best=(0,0,0)
        for i in range(len(t)):
            j=np.searchsorted(t,t[i]+3/24,side="right"); 
            if j-i>best[0]: best=(j-i,i,j)
        nb,i,j=best; sub=rows[i:j]; span=(t[j-1]-t[i])*1440
        if nb<6 or span<50: continue
        tm=Time(np.mean(t[i:j]),format="jd")
        sun=get_sun(tm); c=SkyCoord(ra*u.deg,dec*u.deg)
        elong=c.separation(SkyCoord(sun.ra,sun.dec)).deg
        out.append(dict(pt=key,lon=v["lon"],lat=v["lat"],field=k[0],ccd=k[1],q=k[2],filt=k[3],n=int(nb),span_min=round(span,1),date=tm.iso[:16],
            elong=round(elong,1),seeing=round(float(np.median([float(r["seeing"]) for r in sub])),2),maglim=round(float(np.median([float(r["maglimit"]) for r in sub])),2),
            gid=sorted(set(r["ipac_gid"] for r in sub)),files=[r["filefracday"] for r in sub],ra_img=float(sub[0]["ra"]),dec_img=float(sub[0]["dec"])))
json.dump(out,open(sys.argv[2],"w"))
print(len(out))
for o in sorted(out,key=lambda o:-o["elong"]):
    if o["elong"]>130: print({k:v for k,v in o.items() if k!="files"})
