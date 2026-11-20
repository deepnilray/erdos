"""Step 1: download single-night, low-ndet NSC DR2 measurements in a region.

usage: python fetch.py REGION
Regions are defined in regions.py. Output: data/<region>_meas.parquet,
data/<region>_exposures.csv
"""
import sys, os
import numpy as np, pandas as pd
from tap import tap
from regions import REGIONS

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, '..', 'data')
os.makedirs(DATA, exist_ok=True)


def main(name):
    R = REGIONS[name]
    ra0, ra1, de0, de1 = R['box']
    t0, t1 = R['mjd']
    step = R.get('tile', 0.25)
    exp = tap(f"""SELECT exposure,expnum,instrument,ra,dec,mjd,dateobs,filter,exptime,fwhm,
        depth95,depth10sig,nmeas,elat,elon,rarms,decrms,zpterm FROM nsc_dr2.exposure
        WHERE mjd BETWEEN {t0} AND {t1} AND ra BETWEEN {ra0-1.2} AND {ra1+1.2}
        AND dec BETWEEN {de0-1.2} AND {de1+1.2}""")
    exp.to_csv(os.path.join(DATA, f'{name}_exposures.csv'), index=False)
    print('exposures', len(exp), flush=True)
    parts = []
    ras = np.arange(ra0, ra1, step)
    des = np.arange(de0, de1, step)
    for a in ras:
        for d in des:
            q = f"""SELECT m.measid,m.objectid,m.exposure,m.ccdnum,m.filter,m.mjd,m.ra,m.raerr,
              m.dec,m.decerr,m.mag_auto,m.magerr_auto,m.fwhm,m.class_star,m.flags,m.asemi,m.bsemi,
              m.theta,o.ndet,o.deltamjd FROM nsc_dr2.meas m JOIN nsc_dr2.object o ON m.objectid=o.id
              WHERE o.ra >= {a:.4f} AND o.ra < {a+step:.4f} AND o.dec >= {d:.4f} AND o.dec < {d+step:.4f}
              AND o.deltamjd < 0.6 AND o.ndet <= 20 AND m.mjd BETWEEN {t0} AND {t1}"""
            try:
                df = tap(q)
            except Exception as e:
                print('FAILED tile', a, d, e, flush=True)
                continue
            parts.append(df)
            print(f'tile {a:.2f} {d:.2f} n={len(df)}', flush=True)
    m = pd.concat(parts, ignore_index=True).drop_duplicates('measid')
    m.to_parquet(os.path.join(DATA, f'{name}_meas.parquet'))
    print('total meas', len(m), flush=True)


if __name__ == '__main__':
    main(sys.argv[1])
