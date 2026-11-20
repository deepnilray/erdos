"""Fetch NSC DR2 chip footprints (vertices) for a region's night window."""
import sys, os
from tap import tap
from regions import REGIONS
HERE = os.path.dirname(os.path.abspath(__file__))
reg = sys.argv[1]
R = REGIONS[reg]
ra0, ra1, de0, de1 = R['box']
t0, t1 = R['mjd']
c = tap(f"""SELECT exposure,ccdnum,ra,dec,mjd,dateobs,exptime,filter,fwhm,depth95,depth10sig,rarms,decrms,
  vertex_ra1,vertex_ra2,vertex_ra3,vertex_ra4,vertex_dec1,vertex_dec2,vertex_dec3,vertex_dec4
  FROM nsc_dr2.chip WHERE mjd BETWEEN {t0} AND {t1} AND ra BETWEEN {ra0-1.4} AND {ra1+1.4}
  AND dec BETWEEN {de0-1.4} AND {de1+1.4}""")
c.to_csv(os.path.join(HERE, '..', 'data', f'{reg}_chips.csv'), index=False)
print(reg, len(c))
