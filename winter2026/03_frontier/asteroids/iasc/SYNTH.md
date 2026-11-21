# synth.py: synthetic tracking (shift-and-stack) vs the linker (run 2026-11-21)

## Question
Is iasc_hunt.py any good next to the trackers people already use?
- iasc_hunt.py detects in single images and then links the detections.
  Astrometrica blinking and PS1's own MOPS work on the same principle.
  So anything it finds, MOPS has very likely already reported.
- Synthetic tracking, the method behind tools like Tycho Tracker, stacks the images along trial motions.
  That goes deeper than any single image.
- synth.py implements synthetic tracking. It was scored on the same PS1 warp bench, with known asteroids as ground truth.

## Method
synth.py, run as `python3 -I synth.py <set_folder> <out.json>`, works as follows:
1. Gaia WCS for each image.
2. Resample onto image 0's grid.
3. Subtract the per-pixel median, which removes static sources.
4. Apply a Gaussian matched filter and bin x2.
5. Stack along about 10-37k trial velocities, at 0.1-1.25"/min in every direction.
   The robust score is the sum of all images except the brightest, divided by sqrt(n-1).
6. Cuts:
   - Each image's signal must be at least 0.4 x the median image signal.
   - No single image may carry more than 45 % of the signal.
   - A clutter mask removes regions with many negative residuals (halos, ghosts).
7. **Control:** the same search with the image order scrambled. Real movers cannot stack in that order, so it measures the noise rate at each threshold.

## Results (VERIFIED)
The 20 held-out bench sets used are those containing a known asteroid within -0.7 to +1.2 mag of the set's depth limit.
These chips hold 61 known objects (SkyBoT). 55 of them have bench linker results, and all counts below are out of those 55 (`synth_results/synth_vs_link.txt`).

| Threshold | Found by synth | Found by linker | Synth only | Linker only | Unidentified per set | Scrambled per set (noise) |
|---|---|---|---|---|---|---|
| 8 | 20 | 13 | 9 | 2 | 5.9 | 4.4 |
| **10** | **18** | **13** | **7** | **2** | **3.1** | **2.05** |
| 12 | 15 | 13 | 4 | 2 | 2.2 | 1.25 |

- At threshold 10, linker + synth together find **20 objects vs 13 for the linker alone (+54 %)**.
  - The extra objects are about 0.3-0.5 mag fainter, e.g. 2014 MQ9 V 21.3, 2015 ML136 V 21.7 and 2014 SK183 V 21.9 at the set limit.
- The two linker-only objects are bright: Praha (V 15.8) and Caroltolin (V 18.5).
  They are lost in synth's masks, so **both tools have to be run.**
- The cost is about 3 unidentified candidates per set, of which about 2 are noise (scrambled control).
  - Each candidate needs a look at its cutout, or in Astrometrica, before anything is reported.
- IASC practice set (PS1 chip): synth's only review candidate above 10 is DRY0001 (stack S/N 24). 2018 LT is matched (S/N 62). It has no noise candidate above 10.
- Run time is 1.5-4 min per set and search on 2 CPU cores.

## Caveats
- **Biased set selection.** The sets were chosen because they contain near-limit objects, and the threshold was chosen on these same sets. The gain is therefore an upper-end estimate. (CONJECTURED, scale unknown)
- **Warps vs IASC chips.** Warps are resampled, so their noise is correlated and the noise tail is heavier than on IASC chips. The practice chip had no noise above 10. (VERIFIED for one chip only)
- **No head-to-head with Tycho Tracker.** Its own numbers are not measured here. The claim is only that the same method now runs automatically, with a measured false-alarm rate and known-object matching.
- **Positions are not report-grade.** Synth positions are good to about 0.5". For the report, remeasure in Astrometrica or re-centroid. Each candidate's per-image predicted positions are in `<out>_cutouts/` and the JSON.
