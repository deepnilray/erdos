import glob, json, os, numpy as np, pandas as pd
from astropy.coordinates import SkyCoord
import astropy.units as u
import iasc_hunt as H
from tracker import Params, build_D, find_tracklets
v=pd.read_csv('validation_rows.csv'); miss=v[(v.config=='base')&(v.name!='__summary__')&(v.on_chip)&(v.recovered==0)&(v.V<21.5)]
P=Params(); reasons=[]
for sd in sorted(miss.set.unique()):
    path=f'sets/{sd}'; meta=json.load(open(path+'/known.json')); ims=H.load(path); n=len(ims)
    h0=ims[0]['hdr']; w0=H.clean_wcs(h0); ny,nx=ims[0]['data'].shape; cen=w0.pixel_to_world(nx/2,ny/2); rad=0.75*np.hypot(nx,ny)*abs(h0['CDELT1'])
    gaia=H.gaia_stars(cen.ra.deg,cen.dec.deg,rad); cache=[]
    for im in ims:
        det=H.detect(im); w,q=H.refine_wcs(im,det,gaia); cache.append(dict(w=w,zp=q['zp']))
    T=np.array([im['t'].mjd for im in ims])*1440; tm=T.mean()
    D=build_D([im['data'] for im in ims],ims,cache,P)
    # stationary flag as in tracker
    stat=[]
    for i in range(n):
        cnt=np.zeros(len(D[i]['sky']),int)
        for j in range(n):
            if i!=j: _,s,_=D[i]['sky'].match_to_catalog_sky(D[j]['sky']); cnt+=(s.arcsec<P.MATCH_ARCSEC)
        stat.append(cnt>=2)
    for _,r in miss[miss.set==sd].iterrows():
        k=[x for x in meta['known'] if x['name']==r['name']][0]; rate=np.hypot(k['dra_h'],k['ddec_h'])/60.0
        nd=0; info=[]
        for i in range(n):
            dt=(T[i]-tm)/60.0
            pos=SkyCoord((k['ra']+k['dra_h']*dt/3600/np.cos(np.radians(k['dec'])))*u.deg,(k['dec']+k['ddec_h']*dt/3600)*u.deg)
            s=pos.separation(D[i]['sky']).arcsec; j=np.argmin(s)
            if s[j]<3.0: nd+=1; info.append((round(float(D[i]['snr'][j]),1), bool(stat[i][j]), bool(D[i]['gap'][j])))
        reasons.append(dict(set=sd,name=k['name'],V=k['V'],rate=round(rate,3),n_det=nd,info=info))
df=pd.DataFrame(reasons); print(df.to_string(max_colwidth=70))
print('\nrate quantiles of missed bright:',df.rate.describe().round(3).to_dict()); print('n_det distribution:',df.n_det.value_counts().to_dict())
df.to_pickle('diag.pkl')
