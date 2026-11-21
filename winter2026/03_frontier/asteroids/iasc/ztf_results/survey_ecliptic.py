import requests, csv, io, sys, json, numpy as np
from astropy.coordinates import SkyCoord, GeocentricTrueEcliptic, get_sun
from astropy.time import Time
import astropy.units as u
from concurrent.futures import ThreadPoolExecutor
URL="https://irsa.ipac.caltech.edu/ibe/search/ztf/products/sci"
def q(ra,dec):
    for t in range(3):
        try:
            r=requests.get(URL,params=dict(POS=f"{ra},{dec}",ct="csv",COLUMNS="field,ccdid,qid,fid,filtercode,obsjd,exptime,filefracday,seeing,maglimit,ipac_gid,ra,dec,infobits"),timeout=300)
            return list(csv.DictReader(io.StringIO(r.text)))
        except Exception as e: err=e
    print("fail",ra,dec,err); return []
pts=[]
for lon in np.arange(0,360,7.5):
    for lat in (-4,0,4):
        c=SkyCoord(lon*u.deg,lat*u.deg,frame=GeocentricTrueEcliptic(equinox=Time("J2000"))).icrs
        if c.dec.deg>-25: pts.append((round(c.ra.deg,3),round(c.dec.deg,3),lon,lat))
print(len(pts))
res={}
with ThreadPoolExecutor(6) as ex:
    for p,rows in zip(pts,ex.map(lambda p:q(p[0],p[1]),pts)):
        res[f"{p[0]},{p[1]}"]=dict(lon=p[2],lat=p[3],rows=rows); print(p,len(rows),flush=True)
json.dump(res,open(sys.argv[1],"w"))
