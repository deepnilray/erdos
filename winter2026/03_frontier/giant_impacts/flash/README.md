# Flash detector (Gaia DR4 epoch photometry)
Verdict: VALIDATED on simulated Gaia-like light curves only. Real-data null test (DR3/DR4 light curves) still to do on 2 Dec.
- `flash.py`: fits flat vs c + A exp(-(t-t_k)/tau) (tau 1-3000 d, onset at every visit), subtracts the best sinusoid
  (periods 0.5-3000 d), needs >= 3 visits before onset and >= 2 separate visits above 3 sigma after. Negative A = fade (side scan).
- `inject.py`: Gaia cadence (visits every 20-60 d, 2-4 transits each, 2014.6-2020.0), per-transit noise 1.5/3/8 mmag at G 13/15/17,
  half the stars with rotation (P 1-40 d, 0.5-5 mmag). Results in `inject_summary.json`.
- Null (VERIFIED, 2,000 stars per magnitude, seed 7): max score 0.0 / 0.7 / 3.7 at G 13/15/17; threshold 30.
- Recovery (40 injections per cell), fraction found at A = 0.5/1/2/5/10 %:
  G13 tau 300 d: 0.35 0.78 1 1 1 | tau 2000 d: 0.75 0.98 1 1 1 | tau 30 d: 0 0.03 0.38 0.85 0.9
  G15 tau 300 d: 0 0.55 1 1 1 | G17 tau 300 d: 0 0 0.05 1 1 | tau 3 d: blind at every magnitude (cadence ~30 d).
- Limits: a 6,000-star null cannot prove a false-alarm rate small enough for 10^8 stars; the real-data null decides the threshold.
