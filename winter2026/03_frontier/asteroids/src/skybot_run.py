"""Step 3a: SkyBoT cone search for every exposure in a region (cached).

Epoch = exposure mid-time (mjd + exptime/2), observer code W84 (DECam, CTIO).
Output: data/<region>_skybot.parquet with one row per (exposure, known object).
"""
import sys, os
import pandas as pd
from tap import skybot

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, '..', 'data')


def main(name, only_used=True):
    exp = pd.read_csv(os.path.join(DATA, f'{name}_exposures.csv'))
    if only_used and os.path.exists(os.path.join(DATA, f'{name}_meas.parquet')):
        used = set(pd.read_parquet(os.path.join(DATA, f'{name}_meas.parquet'),
                                   columns=['exposure']).exposure)
        exp = exp[exp.exposure.isin(used)]
    out = []
    from concurrent.futures import ThreadPoolExecutor

    def one(e):
        jd = 2400000.5 + e.mjd + e.exptime / 2 / 86400
        try:
            return e, jd, skybot(jd, e.ra, e.dec, 1.15, loc='W84')
        except Exception as ex:
            print('FAILED', e.exposure, ex, flush=True)
            return e, jd, None
    with ThreadPoolExecutor(4) as ex:
        res = list(ex.map(one, list(exp.itertuples())))
    for i, (e, jd, d) in enumerate(res):
        if d is None:
            continue
        if len(d):
            d = d[['Num', 'Name', 'ra', 'dec', 'Class', 'Mv', 'Err(arcsec)',
                   'dRA(arcsec/h)', 'dDEC(arcsec/h)', 'Dg(ua)', 'Dh(ua)']].copy()
            d['exposure'] = e.exposure
            d['jd_mid'] = jd
            out.append(d)
        print(i, e.exposure, len(d), flush=True)
    sb = pd.concat(out, ignore_index=True)
    sb.columns = ['num', 'name', 'ra', 'dec', 'cls', 'mv', 'poserr', 'dra', 'ddec',
                  'dg', 'dh', 'exposure', 'jd_mid']
    sb.to_parquet(os.path.join(DATA, f'{name}_skybot.parquet'))
    print('done', len(sb))


if __name__ == '__main__':
    main(sys.argv[1])
