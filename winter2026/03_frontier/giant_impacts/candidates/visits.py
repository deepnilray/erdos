import pandas as pd, numpy as np, sys
name, ra0, dec0 = sys.argv[1], float(sys.argv[2]), float(sys.argv[3])
t = pd.read_csv(f'{name}_raw.csv', dtype={'cc_flags': str, 'moon_masked': str})
g = t[(t.qual_frame > 0) & (t.qi_fact > 0.9) & (t.saa_sep > 5) & (t.moon_masked == '00') & (t.nb == 1) & (t.cc_flags.str[:2] == '00')].sort_values('mjd')
g['v'] = np.cumsum(np.r_[0, np.diff(g.mjd) > 30])
a = g.groupby('v').agg(mjd=('mjd', 'median'), n=('mjd', 'size'), w1=('w1mpro', 'median'), w2=('w2mpro', 'median'), ra=('ra', 'median'), dec=('dec', 'median'), chi1=('w1rchi2', 'median'), chi2=('w2rchi2', 'median'))
a['dra'] = (a.ra - ra0) * 3600 * np.cos(np.radians(dec0)); a['ddec'] = (a.dec - dec0) * 3600; a['w12'] = a.w1 - a.w2
print(name, len(t), 'raw ->', len(g)); print(a.round(3).to_string())
print(pd.read_csv(f'{name}_allwise.csv').to_string())
