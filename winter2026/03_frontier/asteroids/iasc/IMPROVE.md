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
