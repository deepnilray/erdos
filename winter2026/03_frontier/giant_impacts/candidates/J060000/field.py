import pyvo, sys
s = pyvo.dal.TAPService('https://irsa.ipac.caltech.edu/TAP')
q = ("SELECT mjd, ra, dec, w1mpro, w2mpro, cc_flags, nb FROM neowiser_p1bs_psd WHERE "
     "CONTAINS(POINT('ICRS',ra,dec),CIRCLE('ICRS',90.003,-31.008,0.25))=1 AND w2mpro BETWEEN 8.5 AND 12.5 AND w1snr>10 "
     "AND nb=1 AND qual_frame>0 AND qi_fact>0.9 AND saa_sep>5 AND moon_masked='00'")
t = s.run_async(q, maxrec=2000000).to_table(); t.write('field_raw.csv', format='csv', overwrite=True); print(len(t))
