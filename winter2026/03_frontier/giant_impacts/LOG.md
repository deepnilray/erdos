# Giant-impact afterglow hunt: log

## 2026-11-20 (Claude, interactive): literature check on J060000
Verdict: NOT FOUND in print. No source read reports the NEOWISE mid-infrared brightening of ASASSN-V J060000.76-310027.83
that coincides with its 2019-2021 optical fade. Status of the IR brightening: CONJECTURED unpublished (ADS still unchecked:
it blocks automated access).
Read and checked: ATels 13346 (Way et al., discovery), 13349 (Buckley et al., SALT: "long period eclipsing binary"
speculated), 13357, 13361 (McCollum & Laine: archival, pre-event SED, no excess), 13377 (Sokolovsky et al.: "patchy dust ring",
Boyajian-like), 13450 (Schaefer, 5 Feb 2020: century of Harvard plates, possible 0.4 mag dip in 1937; the 2019/20 dip is deeper in
blue, R = A_V/E(B-V) between 2 and 4, read as occulting dust; content via a fetch-tool summary, not verbatim); AAVSO campaign page
for Alert Notice 691 (Kenworthy, Sept 2020 and June 2021: best hypothesis a ring system about 1 au across around an unseen
companion; eclipse ended about late May 2021; analysis "of the size of the dust" planned); github.com/mkenworthy/asas-sn-J060000
(optical only); arXiv:2507.03080, 2511.02581, 2507.19594 (ASAS-SN big-dipper search: J0600 not in it), 2404.07378, 2408.06744
(no WISE discussion of J0600). No ATel after 13450 refers to this star.
Why the brightening matters physically (CONJECTURED): about 800 K dust appearing at the same time as the occultation sits close
to a K dwarf (well inside 1 au), which is hard to reconcile with a cold ring around a distant companion and favours freshly made,
hot circumstellar dust. That is the content of a possible short note (RNAAS-length) with a supervisor.
Next: one manual ADS full-text search ("J060000" OR "J0600-31") AND (WISE OR NEOWISE OR infrared); if empty, draft the note.

## 2026-11-17, 04:40 UTC (Claude, scheduled run)
Verdict: no new giant-impact afterglow. The one field star above threshold, uid 211004 = Gaia DR3 2891196718939580672,
turns out to be the KNOWN 2019 optical dimmer ASASSN-V J060000.76-310027.83 (Boyajian-like 0.9 mag fade from 2019-10-25,
ATels 13346/13357/13361/13377). Our NEOWISE light curve adds something we have not found published: a W2 brightening of 0.16 mag,
with reddening, that starts at the same time as the optical fade and is still decaying. That is a lead on a known object
(OCCUPIED object, CONJECTURED new observation), not a discovery. Detector 2 as specified ("decaying excess") FAILS its control
(NGC 2547-ID8 is not recovered); an excess-plus-variability variant does recover it.

Worst news first
1. Detector 2 as specified fails its must-recover control. ID8 has W1-W2 excess 0.42 mag (z = 42 over the main-sequence locus)
   but no significant fading over 2014-2024 (W2 slope +0.55 sigma, colour slope 0.41 sigma, AllWISE 2010 colour equal to the
   2014 baseline). This agrees with Chen, Wang & Huang (arXiv:2610.10130, read in full): ID8 recurs with a 956.8 d timescale and
   no secular decline. VERIFIED (bound: 3 sigma slope test; control: ID8 itself, which failed). Variant "excess > 0.10 mag,
   z > 5, AND visit-to-visit W2 jitter > 3x the median of stars of the same W2" recovers ID8 (jitter ratio 10.2). VERIFIED on one
   control object only; its false-positive rate is unknown.
2. SIMBAD and VizieR/VSX (CDS) are unreachable from GitHub Actions AND from this sandbox (connection reset/timeouts; the Harvard
   SIMBAD mirror returned 404/504; the AAVSO VSX API returned non-JSON). The automated literature check therefore did NOT run.
   Literature for the one surviving star was done by web search and ATels instead (below). No candidate passes the literature
   gate by machine.
3. The first two vetting runs gave no output (the first hung for 60 min on unreachable CDS hosts; the second crashed when every
   AllWISE query timed out while the four hunt shards loaded IRSA). Fixed in vet.py (timeouts, dead-mirror skipping, incremental
   output, robust columns). The vetting numbers below were assembled locally from the second run's per-target output plus an
   AllWISE upload query run from this sandbox.
4. The hunt run that ended at 02:52 had silently switched to slow per-source cone queries after a transient IRSA 502 at 00:52 and
   was killed by the job timeout. 3 sources whose cones failed were written as done-without-data. Fix is on branch
   claude/impacts-hunt-fix (not merged: a run is in progress, and pushing hunt.py cancels it).
5. Rules I note but did not break: README says this sandbox cannot reach IRSA or Gaia; today both answered (IRSA TAP queries ran
   here; the Gaia TAP availability endpoint returned 200). CDS still fails.

Hunt status (VERIFIED, merged shard files at 04:10 UTC)
- 219,780 of 699,341 pool entries scored (31%), 192,173 with a usable light curve. Run 44006081044 (relaunched automatically at
  02:52 by the workflow) is in progress; the pool is processed nearest first.
- Sensitivity bound: score > 8 needs a sustained W2 brightening of at least 0.11 mag for the median star (90th percentile 0.15 mag).
- Candidates (score > 8, W2 minus W1 brightening > 0.05 mag, >= 2 consecutive visits): 2. ASASSN-21qj (validation, score 38.0,
  dW2 0.74, onset MJD 58227, rank 1) and uid 211004 (score 8.86). Next highest field star: 4.92.
- uid mapping control fired: the score recomputed from a fresh NEOWISE query reproduces the stored score for all 36 targets whose
  light curve came back (e.g. 4.427 vs 4.427), so the rebuilt Gaia pool has the same uid order.

uid 211004 = Gaia DR3 2891196718939580672 = AllWISE J060000.75-310027.9 = ASASSN-V J060000.76-310027.83
- What it is: a K dwarf (ATel 13361 fits Teff 4500 +/- 100 K; SALT spectrum "normal K type star", ATel 13377), G = 13.13,
  BP-RP = 1.52, parallax 6.39 mas (157 pc), RUWE 1.02. Gaia DR3 flags it VARIABLE, classifier SOLAR_LIKE (0.41).
- What NEOWISE shows (VERIFIED, by eye: candidates/J060000/211004_lc.png): flat for 12 visits 2014-2019 (W2 10.575-10.598); the
  visit of 2019-09-30 (MJD 58750) is still flat; the next, 2020-02-26 (MJD 58905), is brighter by dW2 = 0.161, dW1 = 0.055 mag;
  then a smooth decline to W2 = 10.55 by 2024-03, still 0.04 mag above baseline. W1-W2 went from -0.065 to +0.04. The optical fade
  began about 2019-10-25 (ATel 13377), inside the 5-month NEOWISE gap, so the IR rise and the optical fade start together within
  that resolution.
- Why it survived the checks that ran: no Gaia DR3 source within 6"; nearest AllWISE neighbours at 25.7" and 27.3", 6.3 and 7.2 mag fainter in W1;
  the NEOWISE centroid moves smoothly with proper motion and shows no jump (< 0.05") at the brightening, so any second source
  must lie within about 0.3"; PSF reduced chi2 normal in every visit; W1 = 10.5 (unsaturated); AllWISE 2010 W1-W2 = -0.09 and
  W2-W3 = 0.04 (photospheric, no prior excess, matching ATel 13361); field control: of 76 stars with W2 8.5-12.5 within 15',
  only this one steps (0.161 mag; next 0.057 at W2 = 12.0, field median 0.006). VERIFIED (control: the 75 neighbours).
- Dust temperature if the excess is one blackbody: excess flux ratio F(W1)/F(W2) = 0.62 gives about 820 K (range about
  750-900 K from the W1 error). CONJECTURED (single-temperature assumption).
- Literature (searched 2026-11-17): ATel 13346 (discovery, Way et al.), 13357 (Way et al., 2019-12-18: min g ~ 15.0 on
  2019-12-11), 13361 (McCollum & Laine, 2019-12-20: "No Infrared Excess", archival pre-event data), 13377 (Sokolovsky et al.,
  2019-12-31: decline ~0.9 mag from ~2019-10-25; favours a Boyajian-star analogue), 13450 (century photometric history; not read,
  ADS blocks automated fetch). Kenworthy has a public light-curve repository (github.com/mkenworthy/asas-sn-J060000) that models
  an opaque occulter from ASAS-SN data; its README does not mention WISE. Not to be confused with ASASSN-24fw (Gaia DR3
  3152916838954800512, 1 kpc; arXiv:2507.03080, 2511.02581). No refereed paper on J060000 found; ADS full-text not searched.
- Status: OCCUPIED (the object and its optical event are known since 2019). The coincident 0.16 mag mid-IR brightening and its
  multi-year decay: CONJECTURED unpublished, because ADS, ATel 13450 and the Kenworthy notebook were not read.

Detector 2 stage A (VERIFIED counts): 36 of 168,793 unsaturated field stars have W1-W2 excess > 0.10 mag and z > 5; 15 of these also
pass the jitter test. All 36 were vetted: the Gaia DR3 classifier calls 10 of them YSO; 6 of those sit in Upper Sco / Lupus
(RA 239-246, Dec -19 to -43) with AllWISE W2-W3 of 1.97-2.28 (disk-bearing young stars); one star is a blend (Gaia neighbour at
1.6", dG = 2.0). Remaining unkilled detector-2 variant passers: uid 74609, 52960, 166090, 55148, 41546, 78873, 41050, 57667 (CANDIDATES.md).
None has had a literature check (CDS unreachable). Most have W2-W3 of 0.4-2.0: disk-bearing stars of unknown age.

Exact next step
1. Read ATel 13450 and search ADS full text for "J060000" + WISE / NEOWISE / infrared (by hand: ADS blocks automated fetch). If
   the IR brightening is unpublished, write it up with Deepnil as a short RNAAS-style note ("coincident mid-infrared brightening
   during the 2019-2021 occultation of ASASSN-V J060000.76-310027.83"), after a professor checks it.
2. Merge claude/impacts-hunt-fix into claude/winter-2026-plan when no giant-impacts run is in progress (check
   /actions/runs first); re-run vet (push to vet/ or dispatch giant-impacts-vet) once the hunt passes 50%.
3. Get SIMBAD/VSX for the 8 detector-2 survivors from a machine that reaches CDS (Deepnil's PC), and kill the young ones.
4. On 2 December 2026, pull Gaia DR4 epoch photometry for J060000 (covers 2014.6-2020.0: the start of the optical fade).

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
