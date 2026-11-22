# JWST archival asteroid search (work in progress, started 2026-11-22)

Target: JWST programme 1063 (PI Sunnquist), "NIRCam (and NIRISS) External Flats, CAR NIRCam-010".
- It is a calibration programme: deep NIRCam images of sky fields on the ecliptic, taken in April 2022.
- It was not built for Solar System science, and it is not among the published JWST asteroid searches found so far:
  - Burdanov et al. 2024, TRAPPIST-1;
  - Fuentes & Bommireddy, EPSC-DPS 2025 (MIRI, 29 programmes);
  - Crouzet et al., EPSC 2026 (MIRI MINDS);
  - Trilling's programme 2211.
  This is CONJECTURED: an unpublished search cannot be ruled out.

## Code
`jwst_hunt.py <dir_with_cal_files> <out>` searches one detector of one field. It:
1. groups the exposures into sets;
2. aligns each set on a 2x2-binned grid;
3. subtracts the median of the set;
4. removes NIRCam 1/f striping;
5. clips the residuals at +-5 sigma;
6. runs a matched line-filter bank (`../iasc/fast.py`);
7. links trails, requiring the motion to agree with each trail's length and angle;
8. runs a scrambled-time control.

It only imports the IASC code; it never modifies it.

## First field: RA80-OBS112.V3+0.6DEG, LW detector A (nrcalong), 24 exposures (VERIFIED)
| set | exposures | real tracklets with >= 5 members | scrambled mean |
|---|---|---|---|
| 0, F322W2, 43 min | 7 | 1 | 0.17 |
| 1, F444W, 3.4 h | 17 | 1 | 3.0 |

There is no clear excess over the scrambled control, so nothing is claimed.

## Validation problem found (VERIFIED)
- JWST observes from L2. For a main-belt asteroid the parallax relative to Earth is ~500" (about 8000 LW px). SkyBoT treats observer code 274 as the geocentre: its positions for code 274 and code 500 agree to milliarcseconds.
- JPL Horizons with location '500@-170' (JWST) puts all 16 SkyBoT objects listed near this field off the LW detector.
- Next step: build a JWST-centric known-object list with a wide geocentric SkyBoT cone plus a Horizons check of each object. That gives true positives on the chip, to validate recovery before trusting any new tracklet.
