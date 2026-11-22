import sys, numpy as np, json, requests; sys.path.insert(0,'/home/claude/erdos/winter2026/03_frontier/asteroids/jwst'); sys.path.insert(0,'/home/claude/erdos/winter2026/03_frontier/asteroids/iasc')
import jwst_hunt as J, iasc_hunt as H
from astroquery.jplhorizons import Horizons
from astropy.coordinates import SkyCoord; import astropy.units as u
ims=J.load('dl'); sets=J.group_sets(ims); out=[]
for si,S in enumerate(sets):
    ny,nx=S[0]['sci'].shape; c=S[0]['w'].pixel_to_world(nx/2,ny/2)
    tm=np.mean([im['tmid'].jd for im in S])
    rows,_=H.skybot(c.ra.deg,c.dec.deg,tm,0.35)
    print('set',si,'skybot geocentric within 0.35 deg:',len(rows), flush=True)
    for r in rows:
        nm=r['num'] if r['num'] not in ('-','') else r['name']
        try: e=Horizons(id=nm,location='500@-170',epochs=[im['tmid'].jd for im in S],id_type='smallbody').ephemerides()
        except Exception as ex: continue
        on=0; pix=[]
        for row,im in zip(e,S):
            x,y=im['w'].world_to_pixel(SkyCoord(row['RA']*u.deg,row['DEC']*u.deg)); x,y=float(x),float(y)
            pix.append((round(x),round(y)))
            if 0<=x<nx and 0<=y<ny: on+=1
        if on: 
            print('  ON CHIP', r['name'], 'V', r['V'], 'exposures on chip', on, '/', len(S), 'pix', pix[0], pix[-1], 'rate"/h', round(float(np.hypot(e['RA_rate'][0],e['DEC_rate'][0])),1), flush=True)
            out.append(dict(set=si,name=r['name'],num=r['num'],V=r['V'],on=on,radec=[(float(a),float(b)) for a,b in zip(e['RA'],e['DEC'])],jd=[im['tmid'].jd for im in S]))
json.dump(out,open('known_on_chip.json','w'),indent=1)
