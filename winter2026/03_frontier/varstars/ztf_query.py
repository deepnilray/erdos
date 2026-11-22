import pyvo, time
s=pyvo.dal.TAPService('https://irsa.ipac.caltech.edu/TAP')
ra,dec,r=float(__import__('sys').argv[1]),float(__import__('sys').argv[2]),float(__import__('sys').argv[3])
q=f"""SELECT oid, ra, dec, filtercode, ngoodobs, medianmag, magrms, medmagerr, stetsonj, vonneumannratio, percentiles_05, percentiles_95, refsharp, refchi, refmag, skewness
FROM ztf_objects_dr24 WHERE CONTAINS(POINT('ICRS',ra,dec),CIRCLE('ICRS',{ra},{dec},{r}))=1
AND filtercode='zr' AND ngoodobs>=150 AND medianmag BETWEEN 14 AND 19.5 AND chisq > 8 AND (percentiles_05-percentiles_95)>0.15 AND refsharp BETWEEN -0.3 AND 0.3 AND refchi < 3"""
t=time.time(); res=s.run_sync(q, maxrec=200000).to_table(); print(len(res),'rows',round(time.time()-t),'s')
res.write(f'zr_{ra}_{dec}.csv',format='csv',overwrite=True)
