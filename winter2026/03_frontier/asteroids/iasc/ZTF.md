# iasc_hunt.py + synth.py on public ZTF science images (run 2026-11-21)

Both moving-object methods were run on 8 one-night ZTF image sets near opposition, with known asteroids (SkyBoT, observer I41) as ground truth.
Every claim is labelled **VERIFIED** (measured here; numbers in `ztf_results/`) or **CONJECTURED** (reasoned, not measured).
**Nothing here is a discovery claim, and nothing was submitted anywhere.**

## Data (VERIFIED)
- **Source:** public ZTF science images (`_sciimg.fits`) and bad-pixel masks (`_mskimg.fits`) from IRSA IBE.
  - Every file downloaded without credentials. That includes partnership (ipac_gid 2) and Caltech (gid 3) exposures from 2019-2020, which are now public.
  - Each image is a 2000 x 2000 px cutout (33.7' x 33.7') of one CCD quadrant, centred on the quadrant's median centre (`?center=ra,dec&size=2000pix`).
- **How the sets were selected:**
  - IBE metadata was searched at 144 points on the ecliptic (every 7.5° in longitude, at β = -4°, 0°, +4°): `ztf_results/survey_ecliptic.py`.
  - Exposures were grouped by night, field, CCD, quadrant and filter, keeping only exposures with infobits = 0: `group_nights.py`.
  - Within each group, the best ≤ 120 min window was kept, up to 12 exposures spread evenly across it. Exposures with seeing > 1.4 x the night's median were dropped: `select_sets.py`.
  - Downloads: `fetch_sets.py`.
- **Most of the high-cadence nights found** belong to the 2019 partnership programme ("Asteroid_Lightcurve", PROGRMID 2), which observed 20-160 exposures per night of the same fields.
- **Sets** (all ZTF r band, 30 s exposures; β = ecliptic latitude, b = Galactic latitude, elong = solar elongation):

| set | start (UTC) | field/CCD/quad | RA Dec | β | b | elong | n img | span min | seeing " (hdr) | MAGLIM (hdr) | 5σ lim (ours, r) | gid |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Z1 | 2019-02-08 06:19 | 569/c03/q1 | 137.49 +16.52 | +0.2 | +37.9 | 176 | 12 | 120 | 1.75 | 21.08 | 20.91 | 2 |
| Z2 | 2019-02-10 07:16 | 519/c06/q3 | 143.63 +10.37 | -3.8 | +40.8 | 176 | 12 | 119 | 1.95 | 20.88 | 20.90 | 2 |
| Z3 | 2019-10-23 06:35 | 503/c07/q2 | 28.35 +11.20 | -0.4 | -48.8 | 179 | 8 | 120 | 1.73 | 20.65 | 20.66 | 1,2 |
| Z4 | 2019-10-26 08:10 | 504/c15/q3 | 35.31 +14.16 | +0.1 | -43.3 | 175 | 8 | 120 | 1.89 | 20.55 | 20.60 | 2 |
| Z5 | 2019-01-28 06:28 | 567/c11/q2 | 122.45 +20.34 | +0.2 | +26.0 | 172 | 12 | 120 | 1.91 | 21.09 | 20.85 | 2 |
| Z6 | 2024-01-08 03:55 | 563/c09/q3 | 98.08 +19.49 | -3.7 | +4.7 | 170 | 12 | 119 | 2.60 | 20.37 | 20.16 | 1 |
| Z7 | 2020-01-02 03:21 | 612/c03/q2 | 89.79 +23.70 | +0.3 | -0.1 | 169 | 7 | 118 | 2.33 | 20.45 | 20.25 | 1,3 |
| Z8 | 2019-07-10 08:40 | 335/c05/q2 | 293.30 -17.57 | +4.1 | -16.9 | 174 | 11* | 85 | 1.68 | 20.74 | 20.07 | 3 |

\* Z8 has 11 images: one exposure (`ztf_20190710372234`) kept returning HTTP 503 after 4 tries.
- **Field types:** Z6 and Z7 lie in the Galactic plane and Z8 is towards the bulge, so these three are crowded. The other five are at high Galactic latitude.
- **Exposure lists:** `ztf_results/sets.json`. The FITS files (about 2.2 GB) stayed in the scratchpad and were never committed.

## ZTF adaptations (VERIFIED that PS1 behaviour is unchanged; see Regression)
**`iasc_hunt.py`** has a new header style, `ztf`. It is detected by ORIGIN = "Zwicky..." or by FIELDID + SHUTOPEN. When it is detected, `measure()` loads `ZTF_PARAMS`; the PS1 styles keep every old default.
- **Time:** mid-exposure = midpoint of SHUTOPEN/SHUTCLSD (UTC).
  - `OBSMJD` is the exposure **start**: 0.2-0.8 s before SHUTOPEN on the headers inspected. It is used, plus EXPTIME/2, only if the shutter keys are missing.
  - Check against Horizons: the median along-track O−C is −0.045". With a start-time reading it would be about −0.15" at 0.6"/min.
- **Masks:** pixels with `_mskimg` bits 0, 2-10 or 12 (= 6141: tracks, bad responsivity, noisy, ghosts, spikes, saturated, dead, NaN, halos) are masked.
  - Bits 1 and 11 only mark detected sources and are not masked.
  - Pixels ≥ 0.9 x SATURATE are also masked, dilated by 2 px.
  - The mask cutout is stored at `<set>/mask/<science file name>`.
- **WCS:** the header TPV WCS is used only as the starting guess (a plain TAN from CD). The refit is the existing Gaia DR3 SIP-3 fit.
- **Photometry:** the zero point comes from Gaia G converted to SDSS r (or g/i), following Riello et al. 2021, Table C.2.
- **Scaled parameters:** aperture radius 2.5 px (PS1: 5 px = 1.25"), MINAREA 3, GAP_DILATE 3 px, MATCH 1.5", LINK_TOL 2.0", MAX_RESID 1.0", MAG_SPREAD 1.5, MAX_RATE 10"/min, observatory I41.
- **Linker changes needed for many images:**
  - **Stationary test:** only images ≥ 30 min apart are compared (`STAT_DT_MIN`).
    - Reason: at 10 min spacing, a 0.1"/min mover moves only 1" between neighbouring images, so it would match itself and be removed as stationary.
  - **Minimum length:** a tracklet needs ≥ max(3, ⌈0.5 n⌉) images (`MIN_NFRAC`). PS1 keeps 3.
  - **Seeds:** every pair of images at least n/2 apart. The PS1 rule of the first and last images stays for n ≤ 4.
    - Reason: Franzrosenzweig (V 18.4, Z6) sits on a star in images 0-2. It was lost under a first-3/last-3 seed rule and is recovered with this one.
- **New output:** `detections.csv` (the per-image positions of every tracklet).
- **MPC report for ZTF:** the file says it is archival and "not for submission". No PS1 IASC header is written for ZTF.

**`synth.py`:** BIN = 1, and the matched-filter FWHM = median header SEEING (1.7-2.6"). Additional rules apply only when n > 4:
- **Score:** a per-image clip at 5σ before stacking. One image can then add at most 5/√n, and the search needs a single pass.
  - Sum-minus-max would double the cost: 17 000 velocities x 12 images x 4 Mpx already takes about 25 min per set.
  - The clipped stack saturates on bright objects, which gives plateaus with many tied maxima. So each candidate is **reported and thresholded on the unclipped robust score** (sum − max)/√(n−1), the PS1 definition, at its velocity, with non-maximum suppression within 10 px.
- **Per-image cuts replaced:**
  - The old cut "every image ≥ 2σ" would remove about 15 % of the images of a real S/N ≈ 3-per-image mover by chance.
  - The replacements:
    - ≥ 75 % of unmasked images positive.
    - Each time-half significant on its own (≥ 3σ).
    - Each time-third ≥ 0.35 x the mean.
    - Per-image std ≤ max(1.8, 0.65 x mean).
    - No image > 30 % of the total.
  - The third/std cuts were added after seeing partial alignments in Z1/Z2 (signal in only 4-5 images, at rates at the 1.25"/min edge). **They were chosen on Z1/Z2 and are in-sample.**
- **Time origin** at the mean time. The same grid step then has half the worst-case position error.
- **Scrambled control:** a seeded random permutation with ~0 correlation to the true order.
  - For n ≠ 4 the old code reversed the order. With even spacing that is just v → −v, so real movers still stack.
  - That caveat also applies to the 7 three-image PS1 bench sets in SYNTH.md (**CONJECTURED** impact: their noise counts may include real movers).
- **Clutter cut** scaled by n/4. Known objects absorb every candidate within 6".
- **Cache:** `--maps` caches the two search maps, so the candidate stage can be re-run without the search.

## Results (VERIFIED, `ztf_results/summary.json`, `objects_all.csv`)
- **Truth:** SkyBoT objects (I41, set mid-time) that land on unmasked pixels in ≥ ⌈n/2⌉ images. That gives 214 objects in 8 sets.
- **Recovery:**
  - linker = identified tracklet (position and motion match);
  - synth = review-level candidate (robust S/N ≥ 10) within 6" and 0.15"/min of the prediction.

| V (SkyBoT) | n | linker | synth S/N ≥ 10 | either | synth S/N ≥ 7 |
|---|---|---|---|---|---|
| < 19 | 8 | 8 (100 %) | 7 | 8 | 7 |
| 19.0-19.5 | 10 | 10 (100 %) | 10 | 10 | 10 |
| 19.5-20.0 | 21 | 16 (76 %) | 18 (86 %) | 19 (90 %) | 18 |
| 20.0-20.5 | 16 | 13 (81 %) | 16 (100 %) | 16 | 16 |
| 20.5-21.0 | 36 | 12 (33 %) | 32 (89 %) | 32 | 34 |
| 21.0-21.5 | 43 | 0 | 30 (70 %) | 30 | 35 |
| 21.5-22.0 | 37 | 0 | 10 (27 %) | 10 | 24 |
| > 22 | 42 | 0 | 0 | 0 | 0 |

- **Depth:**
  - The linker reaches about the single-image limit, r ≈ 20.9 (V ≈ 21.1). Its 50 % point is at V ≈ 20.7.
  - Synthetic tracking over 8-12 images goes about **1 mag deeper**: 70 % at V 21.0-21.5 and 27 % at 21.5-22.
  - This depth gain is larger than on PS1 (SYNTH.md: +0.3-0.5 mag with 4 images), as expected from √n with n = 12. The gain is only partly limited by the trials penalty.
- **Linker misses at V < 20.5** (8 of 55):
  - 4 undetected (crowded Z7 or Z6 frames, at their limits of 20.2);
  - 3 with < ⌈n/2⌉ linkable detections;
  - 1 with max residual 1.1".
  - The linker recovers only 1 of 22 objects in Z7 (Galactic plane, 2.3" seeing), against 11 for synth.
- **Synth misses at V < 19:** 1, Franzrosenzweig (V 18.4, Z6). It crosses a bright star in images 0-2, where the star mask and the per-image consistency cuts reject it. The linker recovers it. The PS1 lesson holds: run both.
- **Astrometry (linker positions vs JPL Horizons, location I41):** 25 numbered recovered objects, 237 positions (`horizons_check.csv`).
  - Median O−C **0.14"**, with 90 % below 0.33" and a maximum of 0.85".
  - By brightness: 0.12" for V < 19.5 and 0.18" for fainter objects.
  - Median along-track −0.045" and median cross-track −0.077". So the time convention is right, and a common offset of about 0.08" remains (**CONJECTURED** cause: differential colour refraction or Gaia-fit systematics).
  - SkyBoT itself differs from Horizons by 0.12" median.
  - The Gaia refit RMS is 0.16-0.18" at high latitude and 0.23-0.24" in crowded fields (in-sample, 600-13 000 stars).
- **Photometry check:** median V(Horizons) − r(ours) = +0.18, which matches typical asteroid V−r.
  - The two MPChecker-identified synth objects also agree: measured r 21.38 for 2021 PW236 (V 21.4) and r 21.15 for 2019 TU55 (V 21.3).
- **Runtime (2 CPUs):**
  - Stage 1 + linking: 12-34 s per set.
  - synth: 22-26 min per 12-image set (17 000 velocities), and 11-13 min for Z7 (7 images) and Z8 (85 min span).
  - Re-running only the candidate stage from cached maps: 1-2.5 min.

### Unidentified candidates and noise per set (VERIFIED)
| set | linker tracklets | linker unidentified | synth unidentified S/N ≥ 10 | **scrambled control S/N ≥ 10 (noise)** | scrambled ≥ 7 |
|---|---|---|---|---|---|
| Z1 | 11 | 0 | 3 | 0 | 0 |
| Z2 | 10 | 1 | 3 | 0 | 0 |
| Z3 | 9 | 0 | 1 | 0 | 0 |
| Z4 | 6 | 0 | 0 | 0 | 0 |
| Z5 | 10 | 0 | 0 | 1 | 1 |
| Z6 | 7 | 0 | 0 | 0 | 0 |
| Z7 | 1 | 0 | 0 | 0 | 0 |
| Z8 | 6 | 0 | 0 | 0 | 0 |
| total | 60 | 1 | 7 | **1 (0.12 / set)** | 1 |

- **Linker:** with ⌈n/2⌉ required detections it produced 1 unidentified tracklet in 8 sets, and that one is an artefact.
  - Requiring only 40 % of images recovers 5 more objects, but gives 84 unidentified tracklets. That sweep was in-sample, and the 0.5 setting was kept.
- **Synth noise:** about 0.1 per set at S/N ≥ 10. On PS1 4-image warps it was 2.05 per set.

### Candidate review (cutouts: `ztf_results/cutouts/`)
- **Inspection:** each review PNG shows every image smoothed by the PSF along the candidate's motion, the **co-moving stack**, and a **static stack** at the mid-time position (a star would show there). All were inspected by eye.
- **Catalogue check:** MPChecker queries used observatory I41, a 5' radius and V < 24, at the reference (mean) time (`mpcheck.csv`).
- **Magnitudes:** forced aperture photometry (2.5 px radius, inverse-variance mean over unmasked images) with our Gaia-based r zero point.

| id | method | time (UTC, ref.) | RA (deg) | Dec (deg) | r | rate "/min | PA° | S/N | cutout verdict | MPChecker (5', V < 24) | label |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Z1_S000 | synth | 2019-02-08 07:19:58 | 137.61564 | +16.45655 | 21.46 ± 0.11 | 0.50 | 262 | 12.2 | point source in co-moving stack, nothing static; faint dot visible in most single images | nearest: 2004 BM52, 264" away | **real-looking mover, not in MPC orbit catalogue (CONJECTURED new; may be in the ITF)** |
| Z1_S001 | synth | 2019-02-08 07:19:58 | 137.64257 | +16.34323 | 21.69 ± 0.13 | 0.73 | 267 | 11.5 | clean co-moving point source, empty static stack | nearest: 2005 QW10, 275" away | **real-looking, not in MPC orbit catalogue (CONJECTURED new)** |
| Z1_S002 | synth | 2019-02-08 07:19:58 | 137.42796 | +16.35851 | 21.67 ± 0.13 | 0.55 | 244 | 10.2 | co-moving point source; a static star about 4" away at mid-time | nearest: 2006 AG45, 192" away | **possible mover, lower confidence (star nearby); not in MPC orbit catalogue (CONJECTURED)** |
| Z2_S001 | synth | 2019-02-10 08:15:46 | 143.56979 | +10.38488 | 21.40 ± 0.10 | 0.74 | 273 | 13.8 | co-moving point source with flat per-image S/N (≈ 4.4 in 11 of 12 images); faint static sources 2-3" away | "No known minor planets" within 5' | **real-looking, not in MPC orbit catalogue (CONJECTURED new)** |
| Z2_S000 | synth | 2019-02-10 08:15:46 | 143.35003 | +10.60680 | 21.38 ± 0.11 | 0.64 | 265 | 14.1 | clean mover (masked in the last 2 images) | **2021 PW236**, 1.4", V 21.4, 0.62"/min | known (SkyBoT did not return it) |
| Z3_S000 | synth | 2019-10-23 07:38:59 | 28.16433 | +11.10629 | 21.15 ± 0.13 | 0.68 | 305 | 10.4 | faint co-moving source; stars cross the path in image 3 | **2019 TU55**, 4.1", V 21.3, 0.67"/min | known (SkyBoT did not return it) |
| Z2_S002 | synth | 2019-02-10 08:15:46 | 143.43251 | +10.43748 | - | 0.13 | 86 | 12.7 | a bright star's bleed column next to a masked band; no point source | nothing matching | **artefact** |
| Z2_T009 | linker | 2019-02-10 08:15:46 | 143.41034 | +10.46162 | 19.4 | 0.13 | 91 | 6/12 | horizontal bleed trail from a bright star along a masked column | nothing matching | **artefact** |

- **Four real-looking candidates.** Z1_S000, Z1_S001 and Z2_S001 look like real faint moving point sources; Z1_S002 is weaker.
  - All four move west at main-belt rates (0.5-0.74"/min) and are r ≈ 21.4-21.7, which is about 0.5-0.8 mag below the single-image limit. That is why the ZTF and MPC pipelines would not have linked them from single detections.
  - MPChecker lists no catalogued object near any of them.
  - This is **not** evidence that they are new:
    - they could be in the MPC's Isolated Tracklet File, or be objects with poor orbits more than 5' from their predicted position (not checked);
    - each one rests on a single 2-hour arc from one night;
    - the positions come from the synth grid and are good to about 1": not report-grade.
- **Pipeline check (VERIFIED):** the two synth-only objects that MPChecker identified (2021 PW236 and 2019 TU55) are missing from SkyBoT's response, yet synth found them. These two independent catalogue matches support synth's sub-limit detections.
- **Artefacts:** both are bleed trails near bright stars in Z2, around RA 143.41-143.43, Dec +10.44-10.46. A mask-bit/bleed-column veto would remove them.

## Differences vs Pan-STARRS (BENCH.md / SYNTH.md)
- **Depth:**
  - A single 30 s ZTF r frame reaches 5σ ≈ 20.9 (r) at high latitude and 20.1-20.3 in crowded or poor-seeing fields. A 45 s PS1 i-band warp reaches about 21.1 (R-equiv), and the IASC w chip about 22.2.
  - ZTF compensates with numbers: 8-12 frames per night. Synthetic tracking therefore reaches V ≈ 21.5 (≥ 70 % recovery) on ZTF, against about 21.3 at the PS1 warp limit (VERIFIED, different object samples).
- **PSF:**
  - ZTF is 1.01"/px with 1.7-2.6" FWHM, so a star is about 2 px FWHM (marginally sampled). PS1 is 0.25"/px with about 1.5" FWHM.
  - So BIN = 1 (not 2), a 2.5 px aperture, and centroid errors about 2x larger.
  - Linker O−C is nevertheless 0.14" median vs Horizons (PS1 warps: 0.064"). The 12-point tracklets average down the per-point error.
- **False-alarm rate:**
  - Linker: 1 unidentified tracklet in 8 sets (0.12 per set; an artefact), against 0.23 per set on PS1 held-out warps. The main reason is that requiring ≥ 50 % of 8-12 images is a much stronger constraint than 3 of 4.
  - Synth: the scrambled control gives about 0.1 noise per set at S/N ≥ 10, against 2.05 per set on PS1.
    - ZTF pixels are not resampled: the aperture noise ratio is 0.9-1.0 at high latitude, against 1.27 on warps.
    - With 12 images the consistency cuts have far more power.
  - Crowded Galactic-plane fields:
    - raise the noise ratio to 1.3-1.5;
    - cut synth's candidate count through clutter and star masks (Z6-Z8: 700-2 200 candidates at S/N ≥ 5, against 6 700-11 000 elsewhere);
    - cut linker recovery sharply (Z7: 1 of 22).
- **Rate floor:** the linker still needs ≥ 0.1"/min. Synth covers 0.1-1.25"/min, so faster movers (NEOs) are linker-only.

## Caveats
- **Thresholds were not tuned on held-out data.** The linker's MIN_NFRAC/MAX_RESID sweep (4 settings) and synth's third/std cuts were chosen on these same sets, and synth's on Z1/Z2 only. With only 8 sets there was no held-out split.
- **Truth comes from SkyBoT.** It missed at least two real V ≈ 21.3 objects that MPChecker lists. So "unidentified" here first means "not in SkyBoT", and MPChecker is the second check.
- **Recovery counts depend on the truth definition.** They are counted only for objects on unmasked pixels in ≥ ⌈n/2⌉ images.
  - Synth "found" means a S/N ≥ 10 candidate within 6" and 0.15"/min of the prediction. At S/N ≥ 5 the scrambled control yields as many candidates as the real search (about 700-11 000 per set), so recovery is quoted only at 7 and 10.
- **SkyBoT V** can be off by a few tenths of a magnitude.

## Regression (VERIFIED)
- `python3 -I iasc_hunt.py <scratch>/iasc/p3/x/XY54_p10 <scratch>/iasc/p3/out_check --team DRY` gives an `MPCReport.txt` identical to the earlier runs (`out/`, `out2/`), apart from the ACK line:
  - 2018 LT (K18L00T), 3 points;
  - DRY0001, 4 points, starting at RA 3.10760, Dec -10.73065;
  - no other tracklet.
- `python3 -I synth.py <scratch>/iasc/p3/x/XY54_p10 <out>.json` reproduces the earlier run exactly:
  - review list = S000 only (RA 3.10759, Dec -10.73069, S/N 24.3, the DRY0001 object);
  - 2018 LT matched at S/N 62.0;
  - 22 candidates and 24 scrambled, the same scores as before.

## Commands (exact)
```
cd winter2026/03_frontier/asteroids/iasc
R=<scratch>/ztf; O=<scratch>/ztfout
python3 ztf_results/survey_ecliptic.py survey.json            # IBE metadata at 144 ecliptic points (metadata only)
python3 ztf_results/group_nights.py survey.json groups.json   # nights with >= 6 exposures of one quadrant within 3 h
python3 ztf_results/select_sets.py                            # -> sets.json (8 sets, <= 12 exposures over <= 120 min); copy to $R
python3 ztf_results/fetch_sets.py $R 2000                     # 2000 px sci + mask cutouts (rerun until no FAIL)
python3 -I ztf_bench.py link  --root $R --out $O             # stage 1 + linker + truth (cached measurements in $R/cache)
python3 -I ztf_bench.py synth --root $R --out $O             # synth.py per set (--maps cache); --force re-runs the candidate stage only
python3 -I ztf_bench.py report   --out $O                     # summary.json, objects_all.csv, candidates.csv
python3 -I ztf_bench.py horizons --out $O --n 25              # O-C vs JPL Horizons (I41)
python3 -I ztf_bench.py mpcheck  --out $O                     # MPChecker for every unidentified candidate
python3 -I ztf_review.py $R ztf_results/cutouts Z1 $O/Z1/synth.json   # review PNGs (likewise Z2, Z3)
python3 -I iasc_hunt.py $R/Z1 <out> --team ZTF                # the plain single-set CLI also works on a ZTF folder
```
The scripts in `ztf_results/` were run from a scratch directory. They read and write their JSON files in the current directory.

## Files
- `iasc_hunt.py`: the `ztf` style, mask/saturation handling, many-image linking and `detections.csv`.
- `synth.py`: the n > 4 rules and `--maps`.
- `ztf_bench.py`: the run/score/report/Horizons/MPChecker driver.
- `ztf_review.py`: the review cutouts.
- `ztf_results/`:
  - `summary.json`: per-set and per-V tables;
  - `objects_all.csv`: every truth object, with linker/synth recovery, miss reasons and the measured positions;
  - `candidates.csv`, `mpcheck.csv`, `horizons_check.csv`, `sets.json`;
  - the selection/fetch scripts;
  - `cutouts/*.png`.
