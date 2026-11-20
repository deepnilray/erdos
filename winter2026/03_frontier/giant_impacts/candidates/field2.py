import pyvo, sys, pandas as pd, numpy as np
s = pyvo.dal.TAPService('https://irsa.ipac.caltech.edu/TAP')
name, ra, dec, m0, m1 = sys.argv[1], float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]), float(sys.argv[5])
q = (f"SELECT mjd, ra, dec, w1mpro, w2mpro, cc_flags FROM neowiser_p1bs_psd WHERE CONTAINS(POINT('ICRS',ra,dec),CIRCLE('ICRS',{ra},{dec},0.2))=1 "
     f"AND mjd BETWEEN {m0} AND {m1} AND w2mpro BETWEEN 8.5 AND 12.5 AND w1snr>10 AND nb=1 AND qual_frame>0 AND qi_fact>0.9 AND saa_sep>5 AND moon_masked='00'")
t = s.run_sync(q, maxrec=500000).to_table().to_pandas(); t = t[t.cc_flags.astype(str).str[:2] == '00']
t['k'] = (np.round(t.ra * np.cos(np.radians(dec)) * 3600 / 3)).astype(int).astype(str) + '_' + (np.round(t.dec * 3600 / 3)).astype(int).astype(str)
mid = (m0 + m1) / 2; rows = []
for k, g in t.groupby('k'):
    a, b = g[g.mjd < mid], g[g.mjd >= mid]
    if len(a) >= 4 and len(b) >= 4:
        rows.append((g.ra.median(), g.dec.median(), g.w2mpro.median(), a.w2mpro.median() - b.w2mpro.median(), a.w1mpro.median() - b.w1mpro.median()))
r = pd.DataFrame(rows, columns=['ra', 'dec', 'w2', 'dW2_step', 'dW1_step']).sort_values('dW2_step')
r['sep_arcsec'] = np.hypot((r.ra - ra) * np.cos(np.radians(dec)), r.dec - dec) * 3600
r.round(4).to_csv(f'{name}_field_control.csv', index=False)
print(name, 'sources', len(r), 'median step %.4f, std %.4f' % (r.dW2_step.median(), r.dW2_step.std())); print(r.tail(5).round(3).to_string())
