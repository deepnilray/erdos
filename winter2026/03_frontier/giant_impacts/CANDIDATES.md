# Giant-impact afterglow candidates (updated 2026-11-17 04:40 UTC by Claude, scheduled run)

Verdict: zero new impact afterglows. Detector 1 found one field star above threshold; it is the known 2019 occultation star
ASASSN-V J060000.76-310027.83 (OCCUPIED as an object), with a coincident mid-IR brightening that we have not found published
(CONJECTURED new). Detector 2 has 8 unkilled stars, none of them checked against the literature. A candidate stays a candidate
until it passes by-eye, blend and literature checks; nothing here is a discovery.

Detectors. D1: sustained W2 brightening against the 2014-2015 baseline (score > 8, W2 brightening exceeding W1 by > 0.05 mag,
>= 2 consecutive 6-month visits; about 0.11 mag W2 for the median star). D2 (variant that recovers NGC 2547-ID8): baseline W1-W2
excess > 0.10 mag and > 5 sigma above the Gaia BP-RP main-sequence locus, visit-to-visit W2 jitter > 3x the median at that W2,
W1 > 8. Coverage: 219,780 of 699,341 pool stars (31%, nearest first).

## Validation objects (controls)
| Object | Detector | Result | Label |
|---|---|---|---|
| ASASSN-21qj | D1 | score 38.0, dW2 0.74, dW1 0.33, onset MJD 58227, rank 1 of 192,173 | VERIFIED recovered blind |
| ASASSN-21qj | kill rules | not killed by the rules that ran (blend, saturation, Gaia class, AllWISE) | VERIFIED (literature rule could not run) |
| NGC 2547-ID8 | D2 "decaying" (as specified) | W2 fading 0.55 sigma, colour decline 0.41 sigma: NOT recovered | VERIFIED failure; ID8 recurs without secular decline (arXiv:2610.10130) |
| NGC 2547-ID8 | D2 excess + variability | excess 0.42 mag (z 42), jitter x10.2: recovered | VERIFIED on this one object |

## Surviving candidates
| Det | uid | Gaia DR3 | RA | Dec | G | BP-RP | plx (mas) | Signal | Status |
|---|---|---|---|---|---|---|---|---|---|
| D1 | 211004 | 2891196718939580672 | 90.00308 | -31.00781 | 13.13 | 1.52 | 6.39 | W2 -0.161, W1 -0.055 mag between 2019-09-30 and 2020-02-26, decaying to -0.04 by 2024-03; W1-W2 -0.065 to +0.04; about 820 K if one blackbody (CONJECTURED) | OCCUPIED object = ASASSN-V J060000.76-310027.83 (optical fade from 2019-10-25, ATels 13346/13357/13361/13377). Passed blend (Gaia 6", centroid, field control of 75 stars), saturation, AllWISE (no prior excess), by-eye. IR brightening CONJECTURED unpublished: ADS and ATel 13450 not yet read. Files: candidates/J060000/ |
| D2 | 74609 | 1768914166695591296 | 327.55699 | 14.11477 | 13.07 | 1.78 | 9.06 | W1-W2 excess 0.42 (z 15), jitter x6.6, AllWISE W2-W3 1.07 | CANDIDATE, unvetted literature (CDS unreachable); disk-bearing star of unknown age |
| D2 | 52960 | 5247128354025136128 | 141.34135 | -67.54018 | 11.55 | 1.44 | 10.11 | W1-W2 excess 0.16 (z 11), jitter x5.0, AllWISE W2-W3 0.97 | CANDIDATE, unvetted literature (CDS unreachable); disk-bearing star of unknown age |
| D2 | 166090 | 4055204702374928000 | 265.12366 | -30.86442 | 13.25 | 1.60 | 6.94 | W1-W2 excess 0.23 (z 12), jitter x3.6, AllWISE W2-W3 1.09 | CANDIDATE, unvetted literature; 2.5 deg from the Galactic centre, crowded field, blend risk beyond Gaia |
| D2 | 55148 | 2342601748810281088 | 13.18917 | -27.47577 | 11.89 | 1.46 | 9.98 | W1-W2 excess 0.15 (z 10), jitter x6.1, AllWISE W2-W3 0.40 | CANDIDATE, unvetted literature (CDS unreachable); disk-bearing star of unknown age |
| D2 | 41546 | 4226332451596335616 | 310.03848 | -0.87079 | 10.95 | 1.22 | 10.91 | W1-W2 excess 0.11 (z 10), jitter x4.8, AllWISE W2-W3 0.74 | CANDIDATE, unvetted literature (CDS unreachable); disk-bearing star of unknown age |
| D2 | 78873 | 6110141563309613056 | 212.04213 | -41.39804 | 11.61 | 1.67 | 8.90 | W1-W2 excess 0.21 (z 9), jitter x13.3, AllWISE W2-W3 1.99 | CANDIDATE, unvetted literature; position in Upper Centaurus-Lupus, so most likely a young disk star (to kill or keep once SIMBAD is reachable) |
| D2 | 41050 | 4055707037451698176 | 267.43690 | -31.63687 | 12.13 | 1.45 | 10.95 | W1-W2 excess 0.10 (z 7), jitter x3.8, AllWISE W2-W3 0.51 | CANDIDATE, unvetted literature; 3.5 deg from the Galactic centre, crowded field, blend risk beyond Gaia |
| D2 | 57667 | 3166948080502189696 | 110.17110 | 14.30193 | 11.81 | 1.58 | 9.84 | W1-W2 excess 0.13 (z 7), jitter x4.0, AllWISE W2-W3 -0.55 | CANDIDATE, unvetted literature; no W3 excess, so the W1-W2 excess may be a photometry or binary effect |
## Killed (D1 near-threshold exercise targets and D2 stage A), with reason
Full per-target table: candidates/vet_table_2026-11-17.csv (columns kill, gaia_varclass, nb_list, aw_*).
- W1 saturation (baseline W1 < 8): uid 94591, 141048.
- Gaia DR3 neighbour within 6" less than 3 mag fainter: uid 47551 (1.7", G 16.2 vs 13.4), 169180 (1.6", dG 2.0).
- Gaia DR3 variability classifier YSO: uid 131042, 148153, 141048, 72157, 137372, 190587, 162954, 85276, 220686, 171672, 122962,
  138206, 144763, 71944. Six of these lie in Upper Sco / Lupus with AllWISE W2-W3 of 1.97-2.28.
- D2 stage A but no excess variability (jitter ratio <= 3): not candidates under the variant (listed in the table).
- D1 near-threshold stars (scores 3.5-4.9): below threshold, vetted only to exercise the pipeline; not candidates.
