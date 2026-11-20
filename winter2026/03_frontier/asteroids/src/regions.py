"""Search regions. box = (ra_min, ra_max, dec_min, dec_max) in deg; mjd = (start, end)."""
REGIONS = {
    # Test region: DECam VR stare centred near (189.3, -4.06), ecliptic latitude ~0,
    # 152 exposures on night label 56745 and 198 on night label 56746 (night label =
    # floor(MJD - 0.6); i.e. UT 2014-03-30 and 2014-03-31), 90 s, near opposition.
    # This is NOAO program 2014A-0496 (Heinze et al. 2019, AJ 158, 232).
    'T1': dict(box=(188.4, 190.2, -4.95, -3.15), mjd=(56745.5, 56747.6)),
    # Scale-up 1: g/r/i/u stare at (349.56, -0.60), ecliptic latitude 3.6, night MJD 57219
    'T2': dict(box=(348.65, 350.45, -1.5, 0.3), mjd=(57219.5, 57220.6)),
    # Scale-up 2: deep VR stare at (309.2, -18.2), ecliptic latitude 0.3, night MJD 58722
    'T3': dict(box=(308.3, 310.1, -19.1, -17.3), mjd=(58722.5, 58723.6)),
    # Control far from the ecliptic: chosen in select_control.py
}
