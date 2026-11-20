import pyvo, sys
s = pyvo.dal.TAPService('https://irsa.ipac.caltech.edu/TAP')
name, ra, dec = sys.argv[1], float(sys.argv[2]), float(sys.argv[3])
t = s.run_sync(f"SELECT mjd, ra, dec, w1mpro, w1sigmpro, w2mpro, w2sigmpro, w1rchi2, w2rchi2, nb, na, cc_flags, qual_frame, qi_fact, saa_sep, moon_masked FROM neowiser_p1bs_psd WHERE CONTAINS(POINT('ICRS',ra,dec),CIRCLE('ICRS',{ra},{dec},0.00083))=1", maxrec=20000).to_table()
t.write(f'{name}_raw.csv', format='csv', overwrite=True); print(name, 'raw', len(t), flush=True)
a = s.run_sync(f"SELECT designation, ra, dec, w1mpro, w1sigmpro, w2mpro, w2sigmpro, w3mpro, w3sigmpro, w4mpro, w4sigmpro, cc_flags, ext_flg, ph_qual FROM allwise_p3as_psd WHERE CONTAINS(POINT('ICRS',ra,dec),CIRCLE('ICRS',{ra},{dec},0.01))=1").to_table()
a.write(f'{name}_allwise.csv', format='csv', overwrite=True); print(name, 'allwise', len(a), flush=True)
q = ("SELECT mjd, ra, dec, w1mpro, w2mpro, cc_flags, nb FROM neowiser_p1bs_psd WHERE "
     f"CONTAINS(POINT('ICRS',ra,dec),CIRCLE('ICRS',{ra},{dec},0.25))=1 AND w2mpro BETWEEN 8.5 AND 12.5 AND w1snr>10 "
     "AND nb=1 AND qual_frame>0 AND qi_fact>0.9 AND saa_sep>5 AND moon_masked='00'")
f = s.run_async(q, maxrec=3000000).to_table(); f.write(f'{name}_field.csv', format='csv', overwrite=True); print(name, 'field', len(f), flush=True)
