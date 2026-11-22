# New variable stars from ZTF public data (started 2026-11-22)

Goal: find variable stars that no catalogue lists. With AAVSO approval, such a star can be submitted to VSX as a new variable with discoverer credit.

## Pipeline
1. `ztf_query.py RA DEC R`: IRSA TAP on `ztf_objects_dr24`, r band. Cuts:
   - >= 150 good epochs;
   - median 14-19.5 mag;
   - chisq > 8;
   - 5-95 % amplitude > 0.15 mag;
   - star-like reference profile.
   (`stetsonj` in DR24 is NaN or 0, so it cannot be used.)
2. `xknown.py`: cross-match within 3" against six catalogues: VSX, ZTF periodic (Chen+2020), ATLAS, Gaia DR3 vari classifications (VizieR GET on the CfA/IDIA mirrors; CDS Strasbourg is unreachable), and Gaia DR3 `vari_summary` through the ESA TAP. The ASAS-SN and WISE catalogue IDs returned 0 rows and need fixing.
3. `lc.py`: fetches the light curves by object ID (cone queries time out). It:
   - drops bad nights;
   - measures nightly-median variability;
   - runs Lomb-Scargle;
   - plots each light curve.

## Results so far (VERIFIED)
| Field | Area | Strong variables | Already catalogued | Uncatalogued | After light-curve vetting |
|---|---|---|---|---|---|
| RA 300, Dec +25 (Galactic plane, b ~ -2) | 0.8 deg2 | 83 | 27 | 56 | All consistent with crowding/blending artefacts and one bad high-cadence night: ~1-2 mag scatter, 1-day aliases |
| RA 230, Dec +30 (high latitude) | 12.6 deg2 | 19 | 14 | 5 | 0 credible |

Details of the 5 high-latitude objects:
- Three objects 1.6' apart brighten on the same nights (nightly correlation 0.5-0.6), so they share an artefact.
- One has a 1-day alias.
- One shows irregular ~1 mag variability at high latitude, probably a quasar rather than a variable star.

Lesson: an amplitude/chi-square selection on ZTF statistics mostly finds artefacts and quasars once the catalogued stars are removed. A periodicity-first search is next: eclipsing binaries and pulsators, with alias, neighbour and colour checks. NOTHING is claimed.
