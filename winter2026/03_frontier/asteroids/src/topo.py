"""Geocentric -> topocentric (DECam, W84) correction for SkyBoT positions.

The SkyBoT conesearch API silently ignores '-loc' (the observer parameter is
'-observer'); our cached queries are therefore GEOCENTRIC. The recovery control
exposed this as a ~2" northward offset of every NSC detection relative to its
SkyBoT prediction (topocentric parallax of a main-belt asteroid seen from
latitude -30). We correct exactly: subtract the observer's GCRS position from the
object's geocentric position vector (distance Dg from SkyBoT).
"""
import numpy as np
import astropy.units as u
from astropy.coordinates import EarthLocation
from astropy.time import Time

# Blanco 4-m / DECam, MPC code W84 (geodetic, approximate to ~10 m)
W84 = EarthLocation.from_geodetic(lon=-70.8064 * u.deg, lat=-30.1690 * u.deg, height=2200 * u.m)
AU_KM = 149597870.7


def to_topo(ra, dec, dg_au, jd_utc):
    ra, dec, dg = np.radians(np.asarray(ra, float)), np.radians(np.asarray(dec, float)), np.asarray(dg_au, float)
    t = Time(np.asarray(jd_utc, float), format='jd', scale='utc')
    pos, _ = W84.get_gcrs_posvel(t)
    ox, oy, oz = (pos.x.to(u.km).value / AU_KM, pos.y.to(u.km).value / AU_KM,
                  pos.z.to(u.km).value / AU_KM)
    x = dg * np.cos(dec) * np.cos(ra) - ox
    y = dg * np.cos(dec) * np.sin(ra) - oy
    z = dg * np.sin(dec) - oz
    r = np.sqrt(x * x + y * y + z * z)
    return np.degrees(np.arctan2(y, x)) % 360, np.degrees(np.arcsin(z / r))


if __name__ == '__main__':
    # check against SkyBoT's own topocentric answer (-observer=W84), 476576 at JD 2456746.7
    h = lambda a, b, c: 15 * (a + b / 60 + c / 3600)
    d = lambda a, b, c: -(a + b / 60 + c / 3600)
    ra_g, de_g = h(12, 37, 0.5985), d(3, 59, 28.258)
    ra_t, de_t = h(12, 37, 0.6025), d(3, 59, 25.963)
    r, dd = to_topo([ra_g], [de_g], [1.67470921354], [2456746.7])
    print('corrected - SkyBoT(W84) arcsec: dRA*cos', (r[0] - ra_t) * 3600 * np.cos(np.radians(de_t)),
          'dDec', (dd[0] - de_t) * 3600)
    print('uncorrected offset: dDec', (de_g - de_t) * 3600)


def correct_df(sb):
    """Return a copy of a SkyBoT table with topocentric ra/dec (geocentric kept)."""
    sb = sb.copy()
    sb['ra_geo'], sb['dec_geo'] = sb.ra, sb.dec
    sb['ra'], sb['dec'] = to_topo(sb.ra_geo, sb.dec_geo, sb.dg, sb.jd_mid)
    return sb
