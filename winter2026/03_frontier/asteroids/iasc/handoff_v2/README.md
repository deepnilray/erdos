# IASC asteroid tracker: handoff (2026-11-22)

Run: `python iasc_hunt_v2.py <folder_with_4_fits> <outdir> --team XXX [--sensitive]`
Needs: astropy, sep, scipy, numpy, requests, pyvo. Network: Gaia TAP and SkyBoT.
Output: MPCReport.txt (Astrometrica IASC layout), tracklets.csv, known_in_field.csv, cutout PNGs, summary.json.

- iasc_hunt.py: your original file, untouched.
- iasc_hunt_v2.py: same detection and report format, vectorised linking (identical output on the practice set, much faster in crowded fields), `--sensitive` mode, crowded-field warning.
- tracker.py: linking module with tunable Params (v2 imports it, keep it in the same folder).
- injection_db/: 360 synthetic movers injected into your real PS1 practice images, truth tables and tuning results.
- validate.py, build2.py, fair.py, diag.py + validation_rows.csv, fair_rows.csv: real-data validation on 40 public PS1 DR2 sets (4 same-night exposures, ecliptic, with SkyBoT answer keys).

## Measured performance
Real PS1 DR2 sets, asteroids clear of chip gaps in all 4 images (53 objects, SkyBoT V magnitudes, g/r/i/y band):
V<19.5: 8/8 | 19.5-20.5: 8/10 | 20.5-21.5: 5/17 default, 7/17 sensitive | 21.5-22.5: 0/18
Injection test on the real IASC practice images (w band): 95% at w19-20, 84% at 20-21, 36% at 21-22, 0% beyond 22.
False (unmatched) tracklets per set: default median 1 (mean 4.7), sensitive median 2 (mean 8.8); two crowded fields gave over 100.

## Limits
- Nothing is recovered beyond about magnitude 22 in any setting. Going deeper needs shift-and-stack detection, not built.
- PS1 DR2 warps are resampled and have chip gaps, so they are a proxy for IASC chips, not identical.
- Only one real IASC set was available. Not tested on PS2 (observatory code F52).
- A candidate that matches no known object is still only a candidate: IASC decides.
