# Giant-impact afterglow hunt: log

## 2026-11-17 (Claude, interactive session)
Verdict: pipeline VALIDATED on the prototype; full-pool run in progress; no candidates yet.

- Forecast (written before the full run): almost every high-scoring star will be a blend, a saturated bright star, a young
  stellar object or an instrumental artefact; real new afterglows, if any, number zero to a few in 7e5 stars.
- Archive probe (results on branch impact-results, file probe_log.txt): VarWISE has no entry for ASASSN-21qj (see PRIORART.md).
- Pool: Gaia DR3 stars with parallax > 4 mas (within 250 pc), parallax_over_error > 10, G 8-15, BP-RP 0.55-2.2, RUWE < 1.4,
  main-sequence band in absolute G: 699,339 stars, ordered nearest first. (Young open-cluster pool from Hunt & Reffert 2023
  planned, but VizieR was unreachable from GitHub Actions; code kept behind USE_CLUSTERS=1.)
- Light curves: NEOWISE-R single exposures (IRSA table neowiser_p1bs_psd) within 3" via TAP upload join; quality cuts
  qual_frame > 0, qi_fact > 0.9, saa_sep > 5, moon_masked = '00', nb = 1, S/N > 3 in both bands, cc_flags clean.
- Detector: 6-month visit medians; baseline = first three visits (2014-2015); score = sustained W2 brightening over at least two
  consecutive visits divided by the larger of baseline scatter and visit-to-visit jitter; candidates need W2 brightening
  exceeding W1 by more than 0.05 mag (dust reddening) and score > 8.
- Validation (VERIFIED, real data, blind): ASASSN-21qj score 38.0, dW2 = 0.74, dW1 = 0.33, onset MJD 58227, while the highest of
  the first 1,584 field stars scored 2.95. NGC 2547-ID8 scored 0: its IR was already raised and fading when NEOWISE began, so
  this detector is blind to events that started before about 2015 (limitation, to be fixed with a second detector using the
  AllWISE 2010 baseline and the W1-W2 excess, which is 0.37 mag for ID8).
- Run: 4 parallel GitHub Actions shards, results on branches impacts-live-0 ... impacts-live-3, resumable.

Next: merge shards, vet the top candidates (Gaia neighbours within 6", saturation W1 < 8, SIMBAD/VSX types, YSO indicators,
images), add the second (pre-2015 onset) detector, then Gaia DR4 epoch photometry for survivors on 2 December 2026.
