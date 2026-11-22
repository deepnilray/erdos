import requests, json, numpy as np, pandas as pd, time, sys
from astropy.coordinates import SkyCoord, GeocentricTrueEcliptic; import astropy.units as u
URL = "https://astroarchive.noirlab.edu/api/adv_search/find/?format=json&limit=400000"
F = ["md5sum","archive_filename","proposal","caldat","dateobs_center","ra_center","dec_center","exposure","ifilter","release_date"]
rows = []
for ra0 in range(0, 360, 10):
    # ecliptic dec at this RA (approx), box +-14 deg
    lam = SkyCoord(ra=(ra0 + 5) * u.deg, dec=0 * u.deg).transform_to(GeocentricTrueEcliptic()).lon
    dc = SkyCoord(lon=lam, lat=0 * u.deg, frame=GeocentricTrueEcliptic()).icrs.dec.deg
    body = {"outfields": F, "search": [["instrument", "decam"], ["proc_type", "instcal"], ["prod_type", "image"],
            ["ra_center", ra0, ra0 + 10], ["dec_center", max(-90, dc - 14), min(90, dc + 14)], ["exposure", 30, 2000]]}
    for att in range(3):
        try:
            r = requests.post(URL, json=body, timeout=600); j = r.json(); break
        except Exception as e: print("retry", ra0, e); time.sleep(10); j = None
    if not j: continue
    rec = j[1:]; rows += rec; print(ra0, len(rec), flush=True)
d = pd.DataFrame(rows); d.to_parquet("decam_ecliptic.parquet"); print("total", len(d))
