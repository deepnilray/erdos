import glob, json, os, numpy as np, pandas as pd
from scipy import ndimage
from astropy.coordinates import SkyCoord
import astropy.units as u
import iasc_hunt as H
v=pd.read_csv('validation_rows.csv'); rows=[]
for sd in sorted(v.set.unique()):
    meta=json.load(open(f'sets/{sd}/known.json')); ims=H.load(f'sets/{sd}'); n=len(ims)
    T=np.array([im['t'].mjd for im in ims])*1440; tm=T.mean(); bad=[]
    for im in ims:
        d=im['data']; m=(d<=0)|~np.isfinite(d); bad.append(ndimage.binary_dilation(m,iterations=14))
    for k in meta['known']:
        ok=True
        for i,im in enumerate(ims):
            dt=(T[i]-tm)/60.0
            pos=SkyCoord((k['ra']+k['dra_h']*dt/3600/np.cos(np.radians(k['dec'])))*u.deg,(k['dec']+k['ddec_h']*dt/3600)*u.deg)
            x,y=H.clean_wcs(im['hdr']).world_to_pixel(pos); ny,nx=bad[i].shape
            if not(60<x<nx-60 and 60<y<ny-60) or bad[i][int(y),int(x)]: ok=False; break
        rows.append(dict(set=sd,name=k['name'],clear=ok))
f=pd.DataFrame(rows); d=v[(v.name!='__summary__')].merge(f,on=['set','name']); d=d[d.clear]
print('objects clear of gaps/edges in all 4 images:',d.groupby('config').size().to_dict())
for c in ['base','sens']:
    dd=d[d.config==c].assign(mb=lambda x: pd.cut(x.V,[0,19.5,20.5,21.5,22.5]))
    print('==',c,'overall',round(dd.recovered.mean(),2),int(dd.recovered.sum()),'/',len(dd)); print(dd.groupby('mb',observed=True).recovered.agg(['mean','sum','count']).round(2).to_string())
d.to_csv('fair_rows.csv',index=False)
