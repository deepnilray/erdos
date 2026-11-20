# Unidentified moving objects in NSC DR2 (archival DECam) — pipeline and first results

Status, 2026-11-20. Nothing here is a discovery. The candidates are **unidentified
moving-object tracklets**: no catalogued orbit (SkyBoT, MPC MPChecker) predicts them.
They would only become objects with designations after orbit linking and MPC acceptance,
and (see `PRIORART.md`) the test field was published by its observers in 2019, so these
objects are almost certainly among the 3,234 asteroids that Heinze et al. detected there.

Labels: **VERIFIED** means computed here, with a control that fired. **CONJECTURED** means an
interpretation that was not tested.

## What was built

`src/` holds a reproducible pipeline. Every network call is cached in `cache/`, retried,
and given a timeout.

| step | script | what it does |
|---|---|---|
| 1 data | `fetch.py`, `fetch_chips.py` | Queries NOIRLab Data Lab TAP (`nsc_dr2.meas` JOIN `nsc_dr2.object`) in 0.25 deg tiles. Keeps measurements of objects with `deltamjd < 0.6` d and `ndet <= 20` (single-night objects) inside the night window. Also fetches the exposure list and the chip footprints. |
| 2 link | `link.py` | Single-night tracklets: gnomonic projection; removal of stationary sources; seed pairs (same filter, 6–30 min apart, 0.05–2 deg/day, dmag < 1); scoring by predicted hits through a 3-D KD-tree on (x, y, t); greedy growth with linear or quadratic fits (quadratic absorbs topocentric-parallax curvature over many hours); sigma clipping; acceptance on n, rms <= max(0.35", 3x median error), rate and magnitude scatter. Also applies detection-quality cuts: no deblended fragments, FWHM within 0.5–2x the exposure's seeing. |
| 2b | `link_nights.py` | Optional cross-night linking. Linear extrapolation to the next night, with windows calibrated on known objects plus a shifted-null test. |
| 3 known | `skybot_run.py`, `topo.py`, `classify.py` | Runs one SkyBoT cone search per exposure at mid-exposure and converts the result to topocentric W84 (see the bug note below). Merges tracklet fragments. A detection matches a known object if it lies within max(3", 3σ_ephem) of the object, capped at 60"; a tracklet matches if at least half its detections match the same object. Recovery control uses the chip polygons. |
| 3 control | `link.py --scramble rotate`, `make_exclude.py` + `link.py --scramble times --exclude` | Two false-tracklet tests (below). |
| 4 | `candidates.py`, `check_candidates.py`, `cutouts.py`, `ades_draft.py` | Ranked candidate list; MPChecker (and optional JPL `sb_ident`) checks; image cutouts from the NOIRLab Astro Data Archive (the exact instcal HDU that NSC measured); an ADES PSV **draft**. |
| | `diagnose_missed.py`, `plots.py`, `summary.py` | Explains why known objects were missed; makes the figures; prints every number quoted here. |

To rerun: `cd src; python fetch.py T1; python fetch_chips.py T1; python skybot_run.py T1; python link.py T1;
python classify.py T1; python link_nights.py T1; python candidates.py T1; python check_candidates.py T1 --tiers A`.

## Regions

| id | centre | ecl. lat | night(s) (UT) | exposures | data | control result |
|---|---|---|---|---|---|---|
| **T1** | RA 189.3, Dec -4.06; box 188.4–190.2 x -4.95–-3.15 (3.24 deg²) | ~0 (opposition) | 2014-03-30, 2014-03-31 | 152 + 198 x 90 s VR | 224,881 single-night measurements | **passed** |
| T2 | RA 349.56, Dec -0.60 (3.24 deg²) | 3.6 | 2015-07-17 | 135 (g, r, i, u) | 26,832 | **failed**: 22.8% (50.5% for rate >= 0.05) |
| T3 | RA 309.2, Dec -18.2 (3.24 deg²) | 0.3 | 2019-08-28 | 130 x 120 s VR | 90,350 | **failed**: 7.5% |

The regions were chosen from `nsc_dr2.exposure` as ecliptic fields with the largest number
of DECam exposures in one night (`regions.py`). T1 is NOAO program 2014A-0496 (PI A. Heinze),
"The Deepest Asteroid Survey Ever", read from the image headers, and is published as
Heinze, Trollo & Metchev 2019 (AJ 158, 232). T2 and T3 were the attempts to scale up. **Their
recovery controls did not fire, so no candidates from T2 or T3 are claimed.**

## Results for T1

### Control 1: recovery of known objects — VERIFIED

Known objects come from SkyBoT, queried for each of the 350 exposures. An object counts as
expected if its predicted position lies at least 20" inside a CCD in at least 3 exposures of a night.
"Recovered" means a tracklet that night matches it.

| sample (per night and object) | recovered |
|---|---|
| ephemeris σ < 10", rate >= 0.05 deg/day, V < 22 | **456 / 460 = 99.1%** |
| ephemeris σ < 10", rate >= 0.05 deg/day, V < 23 | **639 / 654 = 97.7%** |
| ephemeris σ < 10", any V | 679 / 737 = 92.1% |
| all predicted on chips (including σ up to 10^7") | 823 / 965 = 85.3% |

Recovery against magnitude (σ < 10"): V < 22: 99%; 22–22.5: 94%; 22.5–23: 86%; 23–23.5: 73%;
23.5–24: 24%. The median depth95 of the exposures is 23.5. See `plots/T1_recovery.png`.

Why objects are missed (`data/T1_missed_diagnosis.csv`). This covers every missed object with
V < 23; each was checked against the full `nsc_dr2.meas`, with no pre-selection, at up to
3 on-chip epochs:
- No NSC DR2 measurement within 3" of the prediction: 26 (16 of them have ephemeris
  σ >= 10", so the prediction itself is poor).
- The measurement exists but belongs to an NSC object with ndet > 20 or a multi-night span,
  so our selection excluded it: 7.
- The measurement exists in our data but was not linked: 5.
- Rate below our 0.05 deg/day floor: 2.

**The control caught a bug (VERIFIED).** The first control run recovered only 59%. Every
NSC detection sat about 2.1" north of its SkyBoT prediction. The SkyBoT conesearch API
ignores `-loc` (the observer parameter is `-observer`), so the returned positions were
geocentric. `topo.py` converts them to W84 topocentric. That conversion reproduces
SkyBoT's own `-observer=W84` answer to 0.5 mas.

### Control 2: false-tracklet rate — VERIFIED

Two scrambles were run, three seeds each. `link.py` raw tracklets are counted before fragment
merging; see `plots/T1_false_rate.png`.

| detections per tracklet | real data | each exposure rotated by a random angle | known and n>=5 movers removed, exposure times shuffled |
|---|---|---|---|
| 3 | 216 | 434 / 397 / 453 | 85 / 21 / 14 |
| 4 | 109 | 2 / 3 / 1 | 0 / 0 / 0 |
| >= 5 | 3,034 | 0 / 0 / 0 | 0 / 0 / 0 |

The rotation scramble keeps the detection density but destroys all coherent motion. The
second test keeps the static clutter (detections around bright stars and galaxies) but
destroys motion. Conclusion:
- **n >= 5: no false tracklets in 6 scrambled runs**, so fewer than about 0.5 per run, against
  3,034 real ones.
- n = 4: about 2 per run, against 109 real ones (about 2%).
- **n = 3: dominated by false tracklets. These are not candidates.**

An earlier version without the deblending and FWHM cuts gave 1,682 three-point
"tracklets" in T3. They were tightly clustered (median nearest-neighbour separation 6" against
79" for a random distribution) and made of SExtractor-deblended fragments around bright
sources. The quality cuts in `prepare()` remove them.

### Cross-night linking — VERIFIED

There are 413 known objects with n >= 5 tracklets on both nights. Linear extrapolation over
about 24 h misses the true position by a median of 23" (90th percentile 36"). With windows
of 107" and 0.65"/h, blind linking pairs 413 known-known tracklets and gets **412 correct (99.8%)**.
In the null test (night-2 tracklets shifted by ±600" or ±1200") there are 2–5 chance links per
run, against about 800 linkable tracklets.

### Candidates

Of 1,991 merged T1 tracklets, 910 match a known object and 1,081 do not. Candidates are
the unmatched tracklets with n >= 4:

| tier | definition | tracklets | objects |
|---|---|---|---|
| A | unmatched on **both** nights and linked (both n >= 5) | 752 | **376** |
| B | unmatched, single night, n >= 5 | 197 | 197 |
| C | unmatched, single night, n = 4 (about 2% false) | 26 | 26 |

36 candidate objects are flagged `poor_orbit_known`: a catalogued object with ephemeris
σ > 30" lies within min(2σ, 300") and moves within 5% + 1.5"/h of the same velocity. These
are probably known objects whose orbits are poor. Example: T1-C0046 and 2022 AL40, which has a
28-day arc and moves at the identical rate, 73" from the prediction.

MPChecker results (independent of SkyBoT), at the night-1 mid-time with a 2' radius, V <= 25.5 and station W84. MPChecker was run on the top 150 tier-A objects: 4 identified with a catalogued object (<= 30" and motion within 3"/h), 17 possibly a poor-orbit catalogued object (same motion within 2"/h inside 2', or the SkyBoT poor-orbit flag), 129 with no catalogued match. VERIFIED as queries; whether these count as "unknown" depends on the caveats in PRIORART.md. The other 226 tier-A objects and all tier-B objects have not been run through MPChecker yet. The full merged list is in `data/T1_shortlist.csv`, one row per object with a `status` column.

- `data/T1_candidates.csv`: one row per candidate tracklet, with positions, times, rate,
  PA, magnitudes, fit rms and links.
- `data/T1_candidate_detections.csv`: every detection, with NSC measid, exposure, CCD, RA/Dec
  and errors, mag.
- `data/T1_candidate_checks.csv`: MPChecker results.
- `data/T1_shortlist.csv`: one row per candidate object, with MPChecker status.

Best candidates, ranked by tier, then number of detections, then fit quality:

| id | tier | nights | detections | RA, Dec (median of first-listed tracklet) | UT span | rate deg/day | PA deg | VR mag | fit rms " |
|---|---|---|---|---|---|---|---|---|---|
| T1-C0004 | A | 2 | 305 | 190.1486, -3.6792 | 2014-03-30 01:13 – 2014-03-31 08:36 | 0.221 | 278 | 22.35 | 0.12 |
| T1-C0000 | A | 2 | 301 | 188.7654, -3.9659 | 2014-03-30 01:10 – 2014-03-31 08:38 | 0.254 | 281 | 22.56 | 0.15 |
| T1-C0017 | A | 2 | 296 | 189.1974, -3.6093 | 2014-03-30 01:10 – 2014-03-31 08:38 | 0.257 | 294 | 22.20 | 0.14 |
| T1-C0009 | A | 2 | 294 | 188.9548, -4.0199 | 2014-03-30 01:17 – 2014-03-31 08:38 | 0.208 | 282 | 21.65 | 0.10 |
| T1-C0003 | A | 2 | 286 | 189.1457, -3.3300 | 2014-03-30 01:10 – 2014-03-31 08:38 | 0.261 | 294 | 21.82 | 0.18 |
| T1-C0034 | A | 2 | 280 | 188.4628, -3.9341 | 2014-03-30 01:10 – 2014-03-31 08:38 | 0.221 | 304 | 22.25 | 0.13 |
| T1-C0038 | A | 2 | 278 | 189.1680, -3.9694 | 2014-03-30 01:10 – 2014-03-31 08:38 | 0.205 | 294 | 22.60 | 0.14 |
| T1-C0001 | A | 2 | 277 | 189.1411, -3.6469 | 2014-03-30 01:13 – 2014-03-31 08:38 | 0.249 | 301 | 22.30 | 0.15 |
| T1-C0025 | A | 2 | 274 | 188.9966, -4.0654 | 2014-03-30 01:10 – 2014-03-31 08:38 | 0.239 | 288 | 22.93 | 0.16 |
| T1-C0016 | A | 2 | 273 | 188.7878, -4.0038 | 2014-03-30 01:10 – 2014-03-31 08:36 | 0.204 | 293 | 22.75 | 0.14 |

All ten are tier A: unmatched on both nights, about 7 h per night, rms 0.10–0.18". Rates of 0.20–0.26 deg/day at PA 278–304 are typical of main-belt objects at opposition.

Visual check: `plots/cutout_T1-C0017.png`, `cutout_T1-C0003.png`, `cutout_T1-C0038.png` and
`cutout_T1-C0023.png` are 24" cutouts from the archive instcal images, centred on each
detection. Each shows a point source that stays centred while the stars move, and is gone
from its first position at the last epoch. `cutout_T1-C0081.png` is the same view of a
candidate that MPChecker identified as (catalogued) 2015 RZ22. SkyBoT's catalogue does not
contain that object, which is why a second known-object service is needed.

What the T1 candidates most probably are (CONJECTURED): main-belt asteroids with V ≈ 21.6–23.8.
Their rates (0.20–0.27 deg/day) and position angles match the known objects in the field
(`plots/T1_rate_mag.png`). Near opposition, V ≈ 22.5 corresponds to H ≈ 19–20, where the
catalogue of known main-belt asteroids is incomplete. All of them lie within the published
Heinze et al. (2019) sample of 3,234 asteroids in this field. Whether those were reported to
the MPC, and therefore sit in the MPC's Isolated Tracklet File or were linked under some
designation, could not be checked from here.

## Scale-up attempts: T2 and T3 failed the control

- **T2** (2015, g/r/i/u stare at elongation where rates are slow): the median known-object rate
  is 0.048 deg/day, below the 0.05 floor. Among objects faster than that, 50% were recovered.
  The diagnosis run (stopped part-way) checked 55 missed objects with V < 23 and
  ephemeris σ < 2". 46 have **no NSC DR2 measurement at all** within 3" of the prediction,
  and 7 are slower than the rate floor (`data/T2_missed_diagnosis.csv`).
- **T3** (2019 deep VR stare): 7.5% recovered, and 0% for V < 21. For 1998 FL28 (V = 18.4) the
  position was checked against JPL Horizons (agrees to 0.1"). The full `nsc_dr2.meas` table
  has no detection there, even with no object selection at all. Of the 26 missed objects
  with V < 20.5 that were checked before the diagnosis run was stopped, 23 look the same
  (`data/T3_missed_diagnosis.csv`).
- CONJECTURED cause: in dense stares where a mover's step between consecutive exposures is
  smaller than about 1" (slow rates, or a short cadence), NSC DR2's DBSCAN object building
  chains the detections. The measurements seem to get lost; they are not just merged into
  other objects. This fits the magnitude dependence seen in T3: faint objects, which are
  detected intermittently so their chains break, are recovered at 40–57%, while bright ones
  are recovered at about 0%. In T1 the step was about 1.2", and bright objects are recovered at
  99%. **Untested.** It needs NSC documentation or a check against the images. Until then,
  NSC DR2 should not be used for slow movers in dense stares.

## What does not work yet

1. Linking beyond two consecutive nights, and orbits. No orbit is fitted. `link_nights.py`
   uses calibrated linear extrapolation only. The next step is an IOD/orbit fit on the 376
   tier-A pairs (for example `find_orb`, or a Gauss IOD with least-squares refinement).
2. JPL `sb_ident` (two-pass) times out after more than 110 s per query from this sandbox. One
   10-minute attempt is coded (`--jpl`) but has not run successfully. MPChecker (MPC) was used
   instead.
3. The MPC's Isolated Tracklet File and the THOR/NSC candidate list are not queryable from
   here, so "matches no catalogued orbit" does not mean "never reported".
4. T2 and T3 scale-up: the control failed (above). Only T1 has trustworthy candidates.
5. Cutouts exist only for 5 candidates. The SIA `vohdu` service does not index the 2014
   files; `adv_search` by `caldat` and filename does.
6. The rate floor of 0.05 deg/day and same-filter seed pairs miss slow objects and pairs
   across filters. The 2"/h tolerance in the parallax-limited cross-night extrapolation
   (median 23") is calibrated only for main-belt objects near opposition.

## The exact next step for reporting (nothing has been submitted)

From the MPC pages opened in `PRIORART.md`:
1. **Do not submit directly.** For archival data from a listed archive (DECam / Cerro Tololo),
   first contact the MPC's **SARC** member for that archive. The SARC page lists Tyler Linder
   for Cerro Tololo/DECam. Ask (a) whether third-party measurements of 2014A-0496 data are
   acceptable, (b) whether Heinze et al. already reported these detections, and (c) how
   observer and measurer credit should be recorded.
2. Format: ADES is strongly preferred; MPC1992 80-column is still accepted. From
   2026-12-30 only **ADES version 2022** is accepted. Submit through the ADES web form or cURL
   (ADES cannot be emailed). Include magnitudes, and give at least 3 observations per object
   per night. Do not send preliminary positions that you will replace later. Re-measure the
   astrometry from the images rather than using catalogue positions blindly.
3. A draft is in `data/ADES_DRAFT_NOT_SUBMITTED_T1-C0017.psv`: station W84, astCat `Gaia2`,
   band `VR`, observation times at mid-exposure (UTC). It has placeholder observer, measurer and
   submitter blocks. It is a template, not a submission. The one `r`-band row needs its
   ADES band code checked against the MPC's valid-values list.
4. Credit: a single-night tracklet gets no designation. A designation requires an orbit.
   Discovery credit (MPEC 2010-U20, as summarised on the MPC page) requires at least 2 nights
   at the discovery opposition and goes to the earliest identifiable observations. Here those
   are the 2014 DECam observations by program 2014A-0496. How the MPC would split credit
   between the original observers and a third-party measurer is not stated on the pages that
   were opened; ask SARC. A student can claim the pipeline, the control results and (if
   accepted) the measurements, **not a discovery**.

## Files

- `PRIORART.md`: prior art and MPC rules, from opened sources only.
- `plots/T1_recovery.png`, `T1_false_rate.png`, `T1_skymap.png`, `T1_rate_mag.png`,
  `cutout_*.png`.
- `data/T*_tracklets_classified.csv`, `T*_control.csv`, `T*_missed_diagnosis.csv`,
  `T1_night_links*.csv`, `T*_candidates.csv`, `T*_candidate_detections.csv`,
  `T1_candidate_checks.csv`, `T*_skybot.parquet` (raw geocentric SkyBoT output),
  `T*_exposures.csv`.
- The raw NSC downloads and the caches are git-ignored; the scripts regenerate them.
