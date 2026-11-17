# Prior art: systematic searches for planetary-collision afterglows (checked 2026-11-17)

Verdict: APPARENTLY OPEN for a blind time-domain search (sustained mid-infrared brightening on main-sequence stars in NEOWISE
single exposures). PARTLY OCCUPIED around it. Search depth: four web searches (two extended) on 2026-11-16/17, abstracts only.
Not yet searched: ADS full-text for "NEOWISE" + "giant impact" + "brightening"; the Moór et al. EDD variability papers;
Kenworthy group 2024-2026 papers; Gaia science alerts papers on Gaia-GIC-1. Do these before writing a paper.

Closest work found:
- Static infrared excess, not time domain: Contardo & Hogg, arXiv:2403.18941, data-driven search for extreme mid-IR excess
  among 4,898,812 main-sequence FGK stars with Gaia DR3, 2MASS and unWISE (abstract read). Moór et al. 2021 (ApJ, AllWISE
  warm extreme debris disks around F5-K7 stars; abstract read).
- Optical time domain, not infrared: systematic search for main-sequence dipper stars in ZTF over 63 million FGK stars, 81
  promising candidates (ApJ 2025, arXiv:2508.03964; abstract read).
- Individual events: ASASSN-21qj (Kenworthy et al. 2023, Nature, arXiv:2310.08360), found after an enthusiast looked at its
  light curve; Gaia20ehk (Gaia-GIC-1); NGC 2547-ID8; HD 166191; V488 Per (list from a Wikipedia page, unverified).
- Theory: arXiv:2606.26026 (June 2026) models impact afterglows and says a systematic survey search may find many more.

Key new fact from our own probe (VERIFIED, 2026-11-17): ASASSN-21qj is absent from both VarWISE catalogues (pure, 457,080 rows;
extended, 1,918,082 rows) on IRSA, although its NEOWISE light curve shows a sustained step of -0.42 mag in W1 and -0.83 mag in W2
beginning near MJD 58227. A VarWISE-based search therefore misses the prototype; the hunt runs on raw NEOWISE photometry.
Unchecked: whether VarWISE simply excludes this sky region (b about -3 deg) rather than missing the event.

## Update 2026-11-17 (scheduled run; alphaXiv search "NGC 2547-ID8 giant impact infrared variability", 13 results)
Verdict unchanged: APPARENTLY OPEN for a blind NEOWISE time-domain search on main-sequence stars. No paper in the results
describes one. New items, each checked against the arXiv text as stated:
- Su, Moór, Kóspál et al., arXiv:2607.06684 (July 2026), JWST + Spitzer spectra of 21 known extreme debris disks (EDDs).
  Full text grepped: it monitors KNOWN EDDs (warm Spitzer 3-5 um, "a sample of two dozen EDDs"), not a blind search. It lists
  ID 8 as J080902.49-485817.2, matching our validation position (RA 122.260417, Dec -48.971444) to < 0.1".
  OCCUPIED: the known-EDD sample and its mineralogy. Not occupied: discovery of new events in NEOWISE.
- Taylor, Lock, Carter & Leinhardt, arXiv:2610.08273 (Oct 2026), "Blinding Lights": SPH post-processing; first days after an
  impact the ejecta can match an M dwarf in temperature and luminosity; proposes Rubin to constrain impact rates. Theory, days
  timescale, optical: does not overlap a NEOWISE multi-year infrared search. (Abstract and full-text grep read.)
- Chen, Wang & Huang, arXiv:2610.10130 (Oct 2026), "A Recurrent Infrared Modulation in the Warm Post-impact Debris Disk NGC 2547
  ID8" (full text read). Its 4.5 um excess shows six recurrent high states with a mean recurrence of 956.8 d and NO secular
  decline (high-minus-low contrast slope -0.015 +/- 0.028 mJy/yr). Consequence for us: a detector that demands decay over the
  NEOWISE mission is not guaranteed to recover ID8; an excess-plus-variability test is the better match (see LOG.md).
- Tzanidakis & Davenport, arXiv:2603.10952 (March 2026), Gaia-GIC-1 = Gaia20ehk (full text read): found through Gaia Photometric
  Science Alerts, not a WISE search; F5 star at about 3.5 kpc with G about 18.8, so outside our pool (parallax > 4 mas,
  G 8-15). IR brightening plus optical dimming from MJD about 58,700; dust about 900 K. They cite Tzanidakis et al. 2025, ApJ 991,
  118 for a systematic main-sequence dipper search (optical). This verifies the Gaia20ehk entry in PLAN.md.
- Citation check: Kenworthy et al. 2023 for ASASSN-21qj is Nature 622, 251, doi:10.1038/s41586-023-06573-9 (as cited in
  2610.10130 and 2603.10952; arXiv:2310.08360 title "A planetary collision afterglow and transit of the resultant debris cloud"
  confirmed). NGC 2547-ID8 impact papers: Meng et al. 2014, Science 345, 1032 (doi:10.1126/science.1255153), Su et al. 2019,
  AJ 157, 202 (as listed in 2610.10130; not opened directly).
