# Tracker improvement log (scoreboard-gated)

Rule: a change is kept only if it beats the previous version on the frozen scoreboard with no more false alarms,
and the practice-set report (2018 LT + DRY0001) is unchanged.

Scoreboard:
- **Injections into the real IASC practice chip.** The injector is `injection_test/`, built from the parallel handoff's `make_trial`.
- **Real known asteroids** on PS1 warps and ZTF (BENCH.md, SYNTH.md, ZTF.md).
- **Practice-set regression.**

## 1. Clutter-mask override for bright slow movers: KEPT (VERIFIED)
See MERGE.md. At w 19-20, synth recovery went from 64 % to 13/15. False alarms stayed at 0 / 23 trials.

## 2. PS1 deep-stack template subtraction: REJECTED (VERIFIED)
`template.py` contains three versions, each tried in turn:
1. Gaussian PSF match.
2. Alard-Lupton kernel.
3. A colour-aware kernel per g/r/i (`kernel_match2`), with the stack WCS refitted to Gaia. Alignment is good to 0.06/0.12 px median.

The best version still leaves 12-18 % of star flux. Near bright stars, 77-80 % of pixels are > 5 sigma, against 61-81 % for the existing median-of-4-images estimate. So it does not remove stars better on IASC chips, and it costs a network fetch and about 60 s.

Probable cause (CONJECTURED): a w-band frame against g+r+i stacks with a variable PSF, plus 13 years of stellar proper motion. Kept in the code but off (`SYNTH_TEMPLATE=0`).

## 3. Trailed fast-mover search (`fast.py`): KEPT (VERIFIED)
How it works:
- A line-filter bank (6 lengths x 15 angles) runs on synth's static-subtracted residuals.
- Linking requires the trail length to match rate x 45 s within 45 % and the trail direction to match the motion within 20 deg.

A first version ran on the raw frames and gave 111 false tracklets on the practice set. Running on the residuals brings that to 0.

Injection test, 25 trials planned (21 completed), 126 movers at 1.25-15"/min, w 19-22.5:

| w | n | linker | fast | either |
|---|---|---|---|---|
| 19-20 | 42 | 42 | 38 | 42 |
| 20-20.5 | 19 | 16 | 15 | 17 |
| 20.5-21 | 9 | 6 | 6 | 7 |
| 21-21.5 | 20 | 3 | 9 | 10 |
| 21.5-22 | 13 | 0 | 6 | 6 |
| 22-22.5 | 23 | 0 | 0 | 0 |

- **False fast tracklets:** 0 in 21 trials, and 0 on the real practice set.
- **Gain:** for fast movers (the NEO regime), the combined search reaches about 0.7 mag deeper than the linker alone. At w 21-22 it finds 16/33 against 3/33.

## 4. One command, `run_set.py`, with PSF-fitted candidate positions: KEPT (VERIFIED)
`python3 -I run_set.py <folder> <out> --team ABC` runs the linker, synth and the fast search. It writes:
- `MPCReport.txt`: byte-identical to the linker report. On the practice set it holds 2018 LT and DRY0001.
- `candidates_review.csv`, `candidates_MPC.txt` and cutouts for the faint and fast candidates.
- `summary.txt`.

Each candidate's position in every image comes from an elliptical-Gaussian fit to the original frame.

End-to-end injection test (`injection_test/injrun.py`): 16 sets, 96 movers at w 19.5-22.3 and 0.1-10"/min. The real report files are parsed and compared with the truth.

| rate | w | n | found | in MPCReport | as candidate |
|---|---|---|---|---|---|
| 0.1-1.25 | 19.5-20.5 | 26 | 26 | 26 | 0 |
| 0.1-1.25 | 20.5-21 | 13 | 13 | 13 | 0 |
| 0.1-1.25 | 21-21.5 | 12 | 10 | 9 | 1 |
| 0.1-1.25 | 21.5-22 | 11 | 9 | 1 | 8 |
| 0.1-1.25 | 22-22.3 | 9 | 1 | 0 | 1 |
| 1.25-10 | 19.5-20.5 | 11 | 11 | 10 | 1 |
| 1.25-10 | 20.5-21 | 3 | 3 | 1 | 2 |
| 1.25-10 | 21-21.5 | 6 | 3 | 1 | 2 |
| 1.25-10 | > 21.5 | 5 | 0 | 0 | 0 |

- **Positions against the truth:**
  - Linker lines: median 0.04", worst 0.72".
  - PSF-fitted candidate lines: median 0.10", worst 0.34".
- **False candidates:** 0. 15 candidates were listed in 16 sets, and all 15 are injected movers.
- **Practice set:** report unchanged, and 0 extra candidates (DRY0001 is already in the report).

## 5. digest2 NEO score: KEPT
digest2 2.8.2 (PyPI) was installed with the user's approval. It reads `digest2_data/ObsCodes.html`, a copy of the MPC list taken 2026-11-22.

`run_set.py` now scores every tracklet, both the report lines and the candidate lines. Results go in `digest2_scores.csv`. Any team tracklet scoring >= 65 is flagged in `summary.txt` as "POSSIBLE NEO".

The step is optional: if digest2 is missing, it is skipped and nothing else changes.

On the practice set (VERIFIED):
- DRY0001 scores NEO 2 (main-belt-like).
- 2018 LT (a Mars-crosser) scores 11.
- The report is unchanged apart from the ACK timestamp.
