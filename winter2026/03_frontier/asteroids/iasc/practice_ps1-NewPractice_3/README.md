# IASC practice set ps1-NewPractice_3 (XY54_p10), run 2026-11-21

Four Pan-STARRS 1 (F51) w-band chip images, 2025-09-16 10:01-10:50 UT, 45 s each, field centre RA 00h12m, Dec -10.74.

## Result

| Tracklet | Images | Rate ("/min) | PA (deg) | R mag | Identification |
|---|---|---|---|---|---|
| T001 | 3 of 4 | 0.714 | 211.6 | 19.8 | 2018 LT (Mars-crosser), packed K18L00T |
| T000 | 4 of 4 | 0.569 | 240.8 | 21.3 | No match in SkyBoT or MPChecker (V < 24, 10' radius, 1,582,571 objects checked). Reported as DRY0001 |

Report: `MPCReport.txt` (Astrometrica layout, CRLF line ends).

## Checks (VERIFIED)
- Astrometry: Gaia DR3 (proper-motion corrected) TAN+SIP refit, 45-52 stars per image, RMS 0.20-0.34".
- 2018 LT positions against JPL Horizons for site F51: O-C <= 0.09" in all three points (Horizons 3-sigma 0.17"/0.13").
  This also checks the timing (mid-exposure = DATE-OBS + EXPTIME/2).
- 2018 LT photometry: 19.8 R vs Horizons V 20.0 (V-R ~0.2-0.4 is typical for asteroids).
- The other two SkyBoT/MPChecker objects (610588, 683089) fall outside the chip (pixel positions off the image).
- Rejected artefacts: two "tracklets" on cell gaps and one satellite-trail fragment (removed by the gap mask).

## Status of DRY0001 (CONJECTURED, not a discovery)
Real moving source in all four frames (see T000.png), main-belt-like motion. Not in the MPC orbit catalogue.
It may already be among Pan-STARRS's own one-night tracklets (the ITF), which MPChecker does not search.
For a practice set, IASC will tell us whether it was expected.

## Report format sources
- Astrometrica IASC report example: M. Neta, "Pesquisar asteroides com o Astrometrica" (Jan 2026), pp. 11-12.
  https://www.miguelneta.pt/images/atividades/iasc/pesquisar-asteroides-com-o-Astrometrica.pdf
  This gives the header order (COD, OBS, MEA, TEL, ACK, NET), the observation line, and the "----- end -----" line.
  Its observation line, character for character:
  `     DEF0001  C2021 01 07.46073308 12 41.425+08 39 47.50         22.1 R      F51`
- MPC1992 columns: https://docs.minorplanetcenter.net/mpc-ops-docs/observations/mpc1992-format/
- Naming (3 letters + 4 digits), the known-object rule, "No moving objects detected", and submission on the IASC team page:
  the Neta guide and the StAnD quickstart.

## Differences from a real Astrometrica report (all deliberate)
- `NET Gaia DR3`: the catalogue actually used. The 2021 example config says PPMXL.
- The `ACK` timestamp is the run time.
- OBS/MEA/TEL copied from the example PS1 config. Astrometrica fills these from the PS1.cfg on your machine, so use yours if they differ.
