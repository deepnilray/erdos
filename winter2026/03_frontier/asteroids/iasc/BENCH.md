# iasc_hunt.py benchmark on public Pan-STARRS1 DR2 warps (run 2026-11-21)

Ground truth = known asteroids from SkyBoT (observer F51) at each set's mid-time.
Every claim is labelled **VERIFIED** (measured here, numbers in `bench_results/`) or **CONJECTURED** (reasoned, not measured).

## Data (VERIFIED)
- **70 sets**, each from one PS1 skycell on one night, 2010-02 to 2014-12 (MJD 55238-57001).
  - Positions were sampled at random with |ecliptic latitude| < 10 deg, Dec > -25 deg and |b| > 12 deg (the Galactic plane was skipped to save runtime).
  - One set per skycell.
- **63 sets have 4 images and 7 have 3.** Images are >= 8 min apart, and the whole set spans 30-87 min (median 53 min).
- **Filters:** 56 sets in i, 8 in g, 2 in r, and 4 mixed-filter sets. The mixed sets were allowed by the brief and are kept in the scores.
- **Cutouts:** 2400 x 2400 px (0.25"/px, 10') from `fitscut.cgi`.
  - The window is the one with the most pixel coverage common to all images. It was found on 256 px previews (`output_size`), and every set needed >= 80 % common coverage.
  - The fitscut output is linear float32. The raw warps use plain BZERO/BSCALE and have no BSOFTEN. `iasc_hunt.load()` still linearizes if BSOFTEN/BOFFSET are present.
- **Split:** sets sorted by md5(id). The first 35 are the train sets and the last 35 the held-out test sets. The set list is in `bench_results/sets.json`.
- **Warp timing:** the header has `MJD-OBS` (exposure start) and `EXPTIME`, and the code uses mid-time = MJD-OBS + EXPTIME/2.
  - `MJD-OBS` is in **TAI**. It is exactly 35 s (TAI-UTC) later than the listing's mjd.
  - With the TAI reading, O-C vs JPL Horizons is 0.064" median. A UTC reading would leave a 35 s along-track offset, about 0.3" at 0.55"/min.

## Results on the 35 held-out sets (VERIFIED)
"Default" = the original parameters. "Tuned" = the parameters now in `iasc_hunt.py`.

| V bin (SkyBoT) | n | default recovered | tuned recovered |
|---|---|---|---|
| 15.8 (one object) | 1 | 1 | 1 |
| 17.5-20.0 | 11 | 11 (100 %) | 11 (100 %) |
| 20.0-20.5 | 6 | 2 (33 %) | 2 (33 %) |
| 20.5-21.0 | 10 | 4 (40 %) | 4 (40 %) |
| 21.0-21.5 | 8 | 2 (25 %) | 2 (25 %) |
| 21.5-22.0 | 8 | 1 (12 %) | 0 |
| > 22.0 | 24 | 0 | 0 |
| **V < 21 total** | 28 | 18 (64 %) | 18 (64 %) |
| **V < 21.5 total** | 36 | 20 (56 %) | 20 (56 %) |
| **False (unidentified) tracklets per set, mean** | | **2.17** (76 in total) | **0.23** (8 in total) |

- **Plot:** `bench_results/recovery_vs_mag.png`. It shows held-out recovery vs V and vs V minus the set's 5σ limit.
- **Depth is what limits recovery, not linking.**
  - Objects at least 0.5 mag brighter than the set's own limit: 15 of 18 recovered.
  - Objects at or fainter than the limit: 0 of 35.
  - The warps are shallow. Their median 5σ limit is 21.1 (R-equivalent), so the V = 20-21.5 bins already sit at the limit.
- **Recovery vs rate** (tuned, held-out; table in `summary.json` under `by_rate`).
  - Nothing slower than 0.1"/min was recovered (0 of 5). One of those is 1494 T-2, V = 20.0 at 0.05"/min, which looks stationary under both configs.
  - From 0.1 to 1.2"/min, recovery is 11-60 % per bin, and the bins follow the magnitude mix.
  - There was one object faster than 1.2"/min, and it was not recovered.
- **Astrometry:**
  - Measured positions vs **JPL Horizons** (F51): 20 numbered held-out objects, 73 positions, **median O-C 0.064"**, worst 0.58". Data: `bench_results/horizons_check_test.csv`.
  - The O-C against SkyBoT's own predictions has a median of 0.23". That figure is dominated by SkyBoT, whose positions differ from Horizons by 0.19" median.
- **Gaia refit RMS:** 0.14" median per warp image. This is in-sample (a SIP-3 fit to 50-370 stars), so it is optimistic.
- **Bright misses** (V < 21, held-out, tuned): 10 objects.
  - **Gap, 3 objects:** 1998 SV130, 2010 LO53 and 2005 JH35. Each was on a cell gap or chip edge, or missing from one image's footprint, in two images, which left fewer than 3 usable detections.
  - **Stationary or blend, 2 objects.** 1494 T-2 moves at 0.05"/min, so it sits inside the stationary radius. 2011 BS165 merged with a star in one image and was undetected in another.
  - **Too faint, 5 objects.** In each case the object was missing from 2 or more images, and V was within 0.5 mag of the set's limit or fainter. Examples: 2007 TG41 at V 20.5 with limit 20.5 in g, and 2007 GW80 at V 20.2 with limit 19.5.
  - **Trail:** none. The fastest object moved 1.2"/min, which is < 1" in 45 s.
  - **Linking tolerance:** none. No missed object had >= 3 linkable detections.
  - The train sets show the same pattern: 2 gap and 3 faint.
- **Tuning cost:** one held-out object was lost. 2014 SK183 (V 21.9) failed the tighter MAX_RESID = 0.4" and had been recovered by the default parameters.

## Parameter changes (VERIFIED on train, then scored on test)
The tuning was coordinate descent on the 35 train sets. The objective was to maximise the number of recovered known objects with false tracklets per set no higher than at the start; ties went to fewer false tracklets.
- The start point was the defaults plus the noisy-cell mask (see below).
- Every evaluation is logged in `bench_results/tune_log.csv`.
- Train recovery stayed at 13/63 for every link setting. NSIG = 3.0 lost 2 objects, and NSIG = 2.0 or MIN_SNR = 3 gained none. So the parameters changed only the false-tracklet count, which fell from 72 to 5 (from 844 with no noisy mask).
- When train values tied, I kept the less restrictive value: MIN_RATE 0.1 rather than 0.15, LINK_TOL 1.2 rather than 0.8, and MIN_SNR 4 rather than 5.
- The adopted configuration is in `bench_results/adopted_config.json`.

| parameter | old | new | why |
|---|---|---|---|
| NOISY_FACTOR (new gap-mask term) | off | 1.5 | Masks regions whose local background RMS is > 1.5x the median (noisy PS1 cells). One g-band set with a noisy cell gave 772 false tracklets and took 390 s; with the mask it gives 0. |
| STAT_MIN | 2 | 1 | A source matched in any other image counts as stationary. This removes "star + noise blip" tracklets when depth varies between images. Biggest single FP cut (12 → 5 on train). |
| MATCH_ARCSEC | 1.0 | 1.3 | Fewer star residuals leaking into the moving list. |
| MAX_RESID | 0.6" | 0.4" | Warp and IASC astrometry RMS is 0.14-0.34", and 4 points rarely exceed 0.4". |
| MAG_SPREAD | 1.2 | 0.8 | Also replaces the hard-coded 0.6 in the drop rule (now MAG_SPREAD/2). |
| MIN_RATE | 0.03"/min | 0.1"/min | With STAT_MIN = 1 and MATCH 1.3", anything slower than about 0.09"/min looks stationary at 15 min spacing anyway. **This sets a rate floor of about 0.1"/min** (Hildas and Trojans near stationary points can be slower). |
| NSIG, LINK_TOL, MIN_SNR, GAP_DILATE | 2.5, 1.2", 4, 8 px | unchanged | No gain on train. GAP_DILATE = 3 raised false tracklets from 5 to 51. |

Other changes, which the tuning did not choose:
- **Identification now also requires matching motion:** the tracklet velocity must be within max(0.1"/min, 25 %) of SkyBoT's. Without this, a 10"/min false tracklet passing within 10" of 2002 HW was counted as a recovery.
- **The linker is vectorised** (KD-trees in a tangent plane). It produces the same tracklets and MPC report as the old per-pair loop.

## IASC practice set regression (VERIFIED)
`XY54_p10` with the new defaults gives the same `MPCReport.txt` as the original code, apart from the ACK timestamp.
- 2018 LT (K18L00T): 3 points.
- DRY0001: 4 points.
- No other tracklets, so no gap or trail artefacts.

The only change in `tracklets.csv` is `known_sep_arcsec` for the unknown tracklet (299 → 336). That column now gives the distance to the nearest object whose *motion* matches.

## Domain shift: bench warps vs the IASC chip (VERIFIED numbers, `bench_results/domain_shift.csv`)
| metric (per image, median) | IASC XY54 (w, 4 images) | warps (273 images; p10-p90) |
|---|---|---|
| FWHM (2 x half-light radius) | 1.49" | 1.47" (1.12-2.19") |
| 5σ limit, 5 px aperture, empirical noise, R-equiv. | **22.16** | **21.11** (20.44-21.49) |
| aperture noise / (pixel RMS x sqrt(area)) | 1.08 | **1.27** (1.19-1.41) |
| detections with S/N > 5 per arcmin² | 2.5 | 5.3 (3.8-8.3) |
| Gaia DR3 matches / refit RMS (in-sample) | 48 / 0.27" | 87 / 0.14" |

- **Depth:** the IASC w-band chip is about 1 mag deeper than a 45 s i-band warp. On held-out warps, recovery is 100 % for V < 20 and falls to 0 near the warp limit (about 21.1). On IASC chips the same fall-off should therefore sit about 1 mag fainter, at V of roughly 21.5-22 (**CONJECTURED**: one IASC set only). The depth-normalised panel of the plot is the one that should carry over.
- **Correlated noise:** warp noise is 27 % above the white-noise value, because resampling correlates neighbouring pixels. A given sep threshold is therefore less significant on warps, and warps produce more spurious detections. The tuned linking cuts were chosen in that harsher regime. On the IASC chip they removed 33-50 % of the non-stationary detections (30/33/22/17 → 19/20/16/15) and changed no tracklet.
- **Detection density:** about 2x higher on warps. The bench fields are at lower ecliptic latitude and closer to the Milky Way than XY54 (Dec -11, near the south Galactic cap).
- **Astrometry:** the warp RMS is lower, probably because the warps are already distortion-corrected by IPP and have more Gaia stars (**CONJECTURED**). For the IASC chip, the validated O-C ≤ 0.09" vs Horizons remains the relevant number.

### Caveats
- Warps are single exposures resampled onto skycells and masked by IPP. They are not raw chips.
  - Cell gaps are NaN, not a constant fill. The equal-neighbour gap detector is therefore exercised mainly on IASC data.
  - The resampling smooths the PSF and correlates noise.
- 3π nights usually give pairs, not quads. The bench takes the quads that do exist (mostly 2014 i-band nights), so these sets favour well-sampled nights. Sets with only 3 images (7 of 70) have no redundancy.
- Ground truth is SkyBoT at the mid-time, propagated linearly with SkyBoT's rates. SkyBoT V can be off by a few tenths of a magnitude, and its positions are about 0.2" from Horizons.
- An object counts toward truth if it lands on finite pixels in >= 3 images.
- "False tracklets" = tracklets matching no SkyBoT object. A few could be real objects missing from the catalogue (**CONJECTURED**: none were checked).
- The sample is small: 36 held-out objects at V < 21.5, so each 0.5 mag bin has a Wilson 68 % error of about ±15-25 %.
- The g-band sets and the poor-seeing nights are shallower. They lower the V-binned recovery; the depth-normalised panel corrects for this.

## Commands (exact)
```
cd winter2026/03_frontier/asteroids/iasc
R=<scratch>/ps1bench          # downloads + caches, never in the repo
python3 -I bench.py select   --root $R --npoints 200 --nsets 70        # listing + previews -> $R/sets.json
python3 -I bench.py fetch    --root $R                                 # 2400 px cutouts, 3 parallel requests
python3 -I bench.py measure  --root $R                                 # stage 1 (original defaults) + SkyBoT cache
python3 -I bench.py measure  --root $R --det '{"NOISY_FACTOR":1.5}'    # stage 1 with the noisy-cell mask
python3 -I bench.py tune     --root $R --out <scratch>/tune --start '{"NOISY_FACTOR":1.5}'
python3 -I bench.py report   --root $R --best bench_results/adopted_config.json --out bench_results
python3 -I bench.py evaluate --root $R --which test --det '{"NOISY_FACTOR":1.5}' \
   --link '{"MIN_RATE":0.1,"MATCH_ARCSEC":1.3,"LINK_TOL":1.2,"MAX_RESID":0.4,"MAG_SPREAD":0.8,"MIN_SNR":4.0,"STAT_MIN":1}' --out <scratch>/ev_tuned_test
python3 -I bench.py horizons --objects <scratch>/ev_tuned_test/objects.csv --out bench_results/horizons_check_test.csv --n 20
python3 -I iasc_hunt.py <scratch>/iasc/p3/x/XY54_p10 <scratch>/out --team DRY    # regression check
```
Runtime on 2 CPUs:
- Stage 1: about 10 s per set.
- Default evaluation of the train half: about 7 min, of which 390 s is the one noisy-cell set.
- Evaluation with the tuned (or noisy-masked) parameters: a few seconds per half.
- Disk: about 6.3 GB of FITS (273 cutouts) plus caches, 12 GB in total.

## Files
- `bench.py`: the benchmark.
- `bench_results/`:
  - `objects_*.csv`: per known object, with recovery and the failure reason (`why`, `per_image`).
  - `tracklets_*.csv`.
  - `summary.json`: binned recovery by V, by rate and by V − limit.
  - `image_stats.csv`, `domain_shift.csv`.
  - `tune_log.csv`, `adopted_config.json`.
  - `horizons_check_test.csv`, `sets.json`.
  - `recovery_vs_mag.png`.
