# Detector D1 completeness and false-positive rate (injection-recovery, 2026-11-20)

**What was measured.** We planted fake infrared brightening events into real NEOWISE light curves. Then we ran the unmodified hunt detector on them: `hunt.visits()`, `hunt.score()`, and the candidate cuts score > 8, redden > 0.05 and nvis >= 2. The test covers 1,723 randomly drawn stars from the near-pool definition and 137,840 injection trials. All photometry is real. Only the injected excess flux is synthetic.

## Headline

| Quantity | Result | Label |
|---|---|---|
| False positives on the untouched sample | 0 of 1,723 (highest untouched score 2.84; 99th percentile 0.96) | VERIFIED. 95% upper limit 3/1,723 = 0.17% per star |
| Hard amplitude floor | 0.1% recovery at 0.10 mag for every shape. Recovery starts at 0.12 mag | VERIFIED. The noise floor `hypot(0.01, 0.01)` = 0.0141 mag gives a score of 8 at 0.113 mag |
| 50% / 90% W2 amplitude, step-plateau, onset MJD 57250-59700 | 0.137 / 0.204 mag | VERIFIED |
| 50% / 90%, ramp (1-2 yr rise) | 0.144 / 0.239 mag | VERIFIED |
| 50% / 90%, step + 3-yr e-fold decay | 0.196 / 0.434 mag | VERIFIED |
| 50% / 90%, step + 1-yr e-fold decay | 0.343 / not reached (0.78 at 0.5 mag) | VERIFIED |
| Blind spot: onset before about MJD 57050, when the first three visits form the baseline | 0-2% recovery even at 0.5 mag | VERIFIED. The control fired. |
| Late-onset loss: onset after about MJD 59900 | ~60% at 0.5 mag; two post-onset visits are needed before the 2024 end of the mission | VERIFIED |

The thresholds come from log-amplitude linear interpolation between grid points.

## Controls

1. **Positive control, the real ASASSN-21qj light curve with no injection.** This VERIFIED control fired. The light curve was fetched by cone with `hunt.GOODQ`, and the cc_flags and finite-magnitude filters were applied. The result was score 38.04, dW2 0.738, dW1 0.332, onset MJD 58227, nvis 2 and 12 visits from 133 exposures. That matches the hunt's recorded score of 38.0 (`control_asassn21qj.json`).
2. **Zero-amplitude round trip.** This VERIFIED control fired. Every star went through the conversion from magnitude to flux and back to magnitude with zero excess. All 1,723 stars reproduced their untouched score exactly, with 0 mismatches.
3. **Large amplitude, mid-mission onset (MJD 58000-59300, amplitude >= 0.3 mag).** Recovery was step 96.7%, ramp 94.8%, decay-3yr 88.5% and decay-1yr 57.6%. This VERIFIED control fired for step and ramp. The shortfall of about 3% from 100% comes from stars with sparse coverage. Stars with more than 15 visits recover 98.8-99.7% at 0.3-0.5 mag. Stars with 6-10 visits recover 48-59% (110 stars, 6% of the sample). In a sparse star the first three surviving visits can straddle the onset, which contaminates the baseline. The fast-decay shape is lower by construction, because the score takes the minimum of two consecutive visits about 6 months apart.
4. **Early onset (the known blind spot).** In the first 1.5 years (onset < MJD 57248), recovery at 0.5 mag is 27% overall. This VERIFIED result has more structure than the expected "near 0%". Onsets before MJD 57050 are recovered at 0-2%. Recovery then climbs steeply, to 47% at MJD 57050-57150 and 84% at MJD 57150-57250, at which point the onset falls after the star's third visit. The true blind spot is therefore "before the star's third NEOWISE visit". That point falls about 12-15 months after the start of the mission, depending on position on the sky.
5. **Recovered events are the injected ones.** This is VERIFIED. No recovered trial has a detected start more than 200 days before the injected onset.

## Completeness table: recovered fraction vs injected peak W2 brightening

The first table uses onsets restricted to MJD 57250-59700, which is mid-mission. Each cell holds 2,295-2,388 trials.

| amp (mag) | step | ramp 1-2 yr | decay 3 yr | decay 1 yr |
|---|---|---|---|---|
| 0.03 | 0.000 | 0.000 | 0.000 | 0.000 |
| 0.05 | 0.000 | 0.000 | 0.000 | 0.000 |
| 0.08 | 0.000 | 0.000 | 0.000 | 0.000 |
| 0.10 | 0.001 | 0.000 | 0.000 | 0.000 |
| 0.12 | 0.198 | 0.120 | 0.000 | 0.000 |
| 0.15 | 0.709 | 0.586 | 0.102 | 0.000 |
| 0.20 | 0.897 | 0.836 | 0.533 | 0.031 |
| 0.25 | 0.939 | 0.917 | 0.730 | 0.192 |
| 0.30 | 0.952 | 0.939 | 0.836 | 0.401 |
| 0.50 | 0.963 | 0.956 | 0.925 | 0.779 |

The second table uses onsets drawn uniformly over MJD 56700-60300, the whole mission. Each cell holds 3,446 trials.

| amp (mag) | step | ramp | decay 3 yr | decay 1 yr |
|---|---|---|---|---|
| 0.10 | 0.001 | 0.000 | 0.000 | 0.000 |
| 0.12 | 0.159 | 0.096 | 0.001 | 0.000 |
| 0.15 | 0.575 | 0.443 | 0.089 | 0.000 |
| 0.20 | 0.752 | 0.647 | 0.458 | 0.026 |
| 0.30 | 0.808 | 0.763 | 0.705 | 0.355 |
| 0.50 | 0.803 | 0.811 | 0.787 | 0.669 |

Across the whole mission, the 50% amplitudes are 0.144 (step), 0.163 (ramp), 0.211 (decay 3 yr) and 0.380 mag (decay 1 yr). No shape reaches 90%, because about 20% of uniformly drawn onsets fall in the early or late blind windows. Recovery plateaus at about 0.80.

**Dependences** (step-plateau, mid-mission onset; full tables in `tables.txt`):
- **Star's noise** (hypot of baseline scatter and visit-to-visit jitter, floor 0.0141). At 0.15 mag, recovery is 95% for stars at the floor, 63% for noise 0.014-0.02, 1% for 0.02-0.03 and 0% above 0.03. A star needs about 8 times its noise. This is the dominant dependence.
- **W2 magnitude.** At 0.15 mag, recovery is 72% for W2 < 8 (saturation-affected jitter), 86-87% for W2 8-10, 74% for W2 10-11 and 49% for W2 11-12. The sample's W2 range is 8.0-11.6 from the 5th to 95th percentile, with a median of 10.4.
- **Dust temperature** (600-1300 K). The effect is weak above 0.15 mag. At 0.12 mag recovery falls from 23% at 600-775 K to 16% at 1125-1300 K. Hotter dust brightens W1 more, so the redden > 0.05 cut bites near threshold.
- **Number of visits.** Recovery at 0.3 mag is 48% for 6-10 visits, 91% for 11-15 and 99% for 16 or more. The median star has 20 visits.

**Template events placed on this grid.** These are CONJECTURED readings of the table, not separate injections. A 0.41-mag step like candidate 5792808347020475136 sits at about 96% for mid-mission onsets. A J060000-like event (0.16 mag with about a 2-yr decay) sits between the decay-1yr and decay-3yr columns, at roughly 0-20% recovery. The real detection of J060000 was therefore near threshold. ASASSN-21qj (0.74 mag) lies above the grid.

## Method

- **Sample.** We took 90 random 0.05-degree RA strips, seed 20261120 (`sample_strips.json`). Each strip covers every declination and uses the exact hunt near-pool ADQL from the Gaia DR3 TAP: parallax > 4, parallax_over_error > 10, G 8-15, BP-RP 0.55-2.2, RUWE < 1.4. We applied the hunt's absolute-G main-sequence band, which left 8,871 stars. Scaled to the full sky that is about 710k, consistent with the 699k pool. We drew 2,000 at random (`sample.csv`). The G distribution therefore follows the pool, with no stratification by G. We fetched NEOWISE `neowiser_p1bs_psd` exposures within 3 arcsec, using `hunt.GOODQ` in IRSA `run_sync` upload joins of 60 targets. All 34 chunks succeeded on the first attempt. The `hunt.harvest` filters followed, copied verbatim because `harvest` is not callable on its own: the cc_flags test, finite W1+W2 and at least 30 exposures. Of the 2,000 stars, 1,789 had at least 30 clean exposures and 1,723 had at least 6 visits. The 277 dropped stars have a G distribution similar to the kept ones.
- **Injection.** Excess flux was added to every exposure before visit binning. We converted magnitudes to Jy with the Vega zero points 309.540 Jy (W1) and 171.787 Jy (W2), added the excess, and converted back. The peak W2 excess is `(10^(0.4 A) - 1)` times the star's median W2 flux. The W1 excess equals the W2 excess flux density times `B_nu(3.35 um, T) / B_nu(4.60 um, T)`, with T uniform over 600-1300 K, giving a ratio of 0.37-1.00. The W1 response follows, including the star's own W1-W2 colour. As a sanity check, ASASSN-21qj's dW2 0.74 / dW1 0.33 corresponds to about 850 K, and the candidate's 0.41 / 0.21 corresponds to about 1050 K.
- **Shapes.** Four shapes were injected: a step-plateau, a step followed by an exp(-dt/tau) decay with tau = 1 yr or 3 yr, and a linear ramp over 1-2 yr (uniform) followed by a plateau. Onsets were drawn uniformly over MJD 56700-60300. Each star received 10 amplitudes x 4 shapes x 2 independent draws of onset, T and ramp length, for 80 trials per star.
- **Recovery.** The trial counts as recovered if `hunt.score(hunt.visits(...))` passes score > 8, redden > 0.05 and nvis >= 2. Those are the CANDIDATES.md D1 cuts.

## Limitations

- **Per-exposure errors.** The injection adds flux but leaves the per-exposure noise unchanged. A real brighter source would have slightly lower relative noise, so completeness is slightly underestimated at large amplitudes. This is CONJECTURED to be negligible.
- **Colour correction and SED.** The calculation applies no WISE colour corrections and treats the dust as a single blackbody. Real dust has a temperature distribution and emission features.
- **Real variability.** Events were injected into stars that already behave normally. Real host stars may be younger and more active, with higher jitter, which lowers completeness according to the noise table. This is CONJECTURED.
- **Untested effects.** Blending, centroid shifts and confusion from an event are not modelled.
- **Sample size and transfer.** A sample of 1,723 stars gives about ±1% binomial error per mission-wide cell and somewhat more for subsets. The figures are measured for the near pool only. The far pool (G 8-16) has fainter stars and will have lower completeness. That claim is CONJECTURED and was not measured.
- **Interpolation.** The 50% and 90% amplitudes are interpolated on a coarse grid with about ±0.01 mag resolution near the threshold.

## Files

- `completeness.py`: all stages (`sample`, `fetch`, `control`, `inject`, `report`). It imports `hunt.py` and does not modify it. Run it from a scratch directory, because the raw NEOWISE chunks, about 22 MB, are written there and are not committed.
- `sample.csv`, `sample_strips.json`: the drawn sample.
- `untouched_scores.csv`: detector output for every untouched star (the false-positive run).
- `trials.csv.gz`: all 137,840 trials (gzip-compressed CSV). Columns: uid, shape, amp_w2, onset_mjd, T_dust, ramp_days, base_w2, jitter, noise, n_visits, score, dW2, dW1, redden, nvis, start, recovered, untouched_candidate.
- `tables.txt`, `summary.json`, `run_info.json`, `control_asassn21qj.json`: tables and numbers.
- `completeness.png`: recovery vs amplitude per shape (left) and step recovery vs onset epoch (right).
