# Merge of the parallel IASC tracker handoff (2026-11-22)

Source: `iasc_tracker_handoff_v2.zip`, from Deepnil's Drive folder "IASC data". It came from another Claude session. It is kept unchanged in `handoff_v2/`.

## What the handoff contained, and what was done with it
| Item | Finding | Action |
|---|---|---|
| `iasc_hunt.py` | Byte-identical to commit bdf3972, the first version here | None |
| `tracker.py` / `iasc_hunt_v2.py`: KD-tree linking | The current `iasc_hunt.find_tracklets` is already KD-tree vectorised. It also has the bench-tuned cuts, the noisy-cell mask and the motion-checked identification. | Not needed. The speed gain is already here. |
| `--sensitive` mode (2.0 sigma, S/N >= 3) | Their measurement on 40 PS1 DR2 sets: V 20.5-21.5 recovery went from 5/17 to 7/17, with about 2x the false tracklets | Added to `iasc_hunt.py` as an opt-in flag. The default is unchanged. |
| Injection database: Moffat PSF, trailed, Poisson noise, injected into the real practice chip | Useful. It is the only test on a real IASC chip rather than on PS1 warps. | Reused below, to test `synth.py` on the IASC chip |
| Their PS1 validation, 40 sets | Consistent with BENCH.md. Their untuned linker gave about 4.7 false tracklets per set (mean), against 0.23 for the tuned linker here. | Kept for reference |

## Injection test on the real IASC practice chip (VERIFIED)
`injection_test/injtest.py` uses their `make_trial`. Each trial injects 6 objects per set at w 19-24 and 0.05-15"/min, alternating between the left and right halves of the chip. 23 trials, 138 objects. Both methods run on the same injected images.

**A bug found and fixed.** In the first run, synth missed bright slow movers (it recovered 64 % at w 19-20).
- The cause: a slow mover overlaps itself between images. That biases the per-pixel median and leaves negative residuals, which triggered synth's clutter mask.
- The fix: peaks with stack S/N >= 30 are no longer removed by the clutter mask (`CLUTTER_OVERRIDE`).
- The practice-set output is unchanged: only DRY0001 is in review, and 0 scrambled hits >= 10.

After the fix, within synth's rate range (0.1-1.25"/min, 77 objects):

| w mag | n | linker | synth | either |
|---|---|---|---|---|
| 19-20 | 15 | 14 | 13 | 14 |
| 20-21 | 15 | 13 | 13 | 13 |
| 21-21.5 | 10 | 9 | 9 | 10 |
| 21.5-22 | 9 | 0 | 3 | 3 |
| > 22 | 28 | 0 | 0 | 0 |

- **Synth false alarms (S/N >= 10, not injected, not one of the 2 real objects):** 0 in 23 trials.
- **Conclusion.** With only 4 images, stacking adds about 0.3 mag on IASC chips: 3 of 9 objects at w 21.5-22, where the linker finds none. ZTF, with 7-12 images, gave about 1 mag. This matches the expected sqrt(N) gain. Both methods should be run, because the linker also covers rates above 1.25"/min.
- **Caveat.** The objects are injected into a single field. The injected magnitudes use the pipeline's own zero point, so they are good to about 0.1 mag.
