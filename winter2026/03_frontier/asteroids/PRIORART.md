# Prior art and reporting rules (written before any data work)

Every source below was opened during this session (2026-11-20). Where a page did not
say something, that is stated; nothing here is cited from memory.

## 1. Who has already searched NSC DR2 / DECam archives for moving objects

| Work | What it did | Source (opened) |
|---|---|---|
| Nidever et al., NSC DR2 (AJ 161, 192, 2021) | The catalogue itself: 3.9 billion objects, 68 billion measurements, ~35,000 deg^2, ~7 mas astrometric accuracy; measurements grouped into objects with DBSCAN. Moving objects therefore show up as many small (low-ndet) "objects". | NSF PAR record https://par.nsf.gov/biblio/10349768 (abstract listing) |
| Fasbender & Nidever, "Exploring the Solar System with the NOIRLab Source Catalog I: Detecting Objects with CANFind" (AJ 162, 244, 2021; arXiv:2109.00088) | Separated stationary and moving detections in **NSC DR1**, linked single-night tracklets and multi-night tracks: **527,055 tracklets over 29,971 deg^2**. | https://export.arxiv.org/abs/2109.00088 ; https://ui.adsabs.harvard.edu/abs/2021AJ....162..244F/abstract |
| K. M. Fasbender, PhD thesis, Montana State University (2024), "Exploring the solar system with the NoirLab source catalog" | CANFind plus a "Tough Transform" search on the latest NSC release: **~4 million solar-system-object detections, of which >3 million belong to objects not previously known**. Also preparing NSC DR3. | https://scholarworks.montana.edu/items/4d450c4b-6bc3-415a-bf8c-fb59d65ef710/full |
| Moeyens et al., THOR (AJ 162, 143, 2021; arXiv:2105.01056) | Tracklet-less heliocentric linking; demonstrated on a 2-week slice of **ZTF** (not NSC): 97.4% recovery of discoverable known objects (a > 1.7 au, >= 5 obs), 10 likely new objects. | https://arxiv.org/abs/2105.01056 |
| Asteroid Institute (B612) + Google Cloud, press release 2024-04-30 | THOR on ADAM run over **NSC DR2**: "27,500 new, high-confidence asteroid discovery candidates", >100 NEAs, no new telescope time. Space.com (same announcement): the observations were "yet to be submitted to and accepted by" the MPC at that time; ~400,000 NOIRLab archival images. | https://b612foundation.org/?p=29854 ; https://www.space.com/google-cloud-ai-tool-asteroid-telescope-archive |
| DES 6-year outer solar system search; DECam Ecliptic Exploration Project (DEEP) | DECam archival / dedicated TNO searches (812 TNOs from DES, 458 new; DEEP 110 multi-night TNOs, 105 apparently new). Different population (slow TNOs), same camera. | abstracts listed at https://par.nsf.gov/biblio/10349768 |

**Added after Step 1 (field-specific prior art).** The test field T1 turned out to be the
dedicated asteroid survey of NOAO program 2014A-0496 (PI A. Heinze; image headers read via
the NOIRLab Astro Data Archive: PROPID 2014A-0496, PROGRAM "The Deepest Asteroid Survey
Ever: Collisional Processes and the Source of Near-Earth Asteroids"). Its results are
published: Heinze, Trollo & Metchev 2019, "The Flux Distribution and Sky Density of 25th
Magnitude Main Belt Asteroids", AJ 158, 232 (arXiv:1910.13015, opened): DECam, UT 2014
March 30 and 31, field centres RA 12:38:12.51 Dec -04:07:40.4 and RA 12:37:20.84
Dec -04:02:08.7; with digital tracking they "detect a total of 3234 distinct asteroids, of
which 3123 are confirmed on both nights", 95% complete to R = 25.0. The paper (both
halves read) does not mention the Minor Planet Center or reporting. Our NSC-based
tracklets reach only ~23.5, so every object we find in T1 is almost certainly among
Heinze et al.'s 3234; whether they were reported to the MPC is unknown to us.
(Methods paper for the technique: Heinze, Metchev & Trollo 2015, AJ 150, 125,
arXiv:1508.01599, opened; WIYN 0.9 m data, not this field.)

**Consequence (plain statement).** NSC DR2 has already been mined end-to-end for moving
objects by at least two professional efforts (Fasbender/Nidever CANFind on NSC; Asteroid
Institute THOR on NSC DR2). Any "unknown" tracklet found here is very likely either
(a) already among those ~27,500 THOR candidates / Fasbender's >3 million unknown-object
detections, possibly by now designated and linked at the MPC, or (b) a single-night
object that nobody can turn into an orbit. Our known-object check (SkyBoT, JPL sb_ident)
sees only objects with orbits; it does not see the THOR candidate list or the MPC's
Isolated Tracklet File (ITF). So "matches no known object" here means "no catalogued
orbit predicts it", not "never seen before".

## 2. MPC rules: designations versus discovery credit

From the MPC operations docs, "Discoveries, Credit and Naming"
(https://docs.minorplanetcenter.net/mpc-ops-docs/astrometry/discoveries-and-credit/):

- "the assignment of a new provisional designation does not mean that you will be
  credited with the discovery of the object when it is numbered."
- Provisional designations are given "when we have enough observations to compute a
  reliable orbit".
- Credit goes to "the chronologically earliest observation that is identifiable at the
  time the designation is to be assigned"; earlier observations found later
  do not change it. Linked earlier observations must be on a different night (>= 12 h).
- If a colleague obtains two nights and reports first, credit goes to the colleague.
- The discoverer of the numbered object is the discoverer of its principal designation;
  that person proposes the name after numbering (WGSBN decides).
- The page refers to MPEC 2010-U20 for the full credit rules. A summary of those rules
  (D. Rankin, with a note from G. Williams of the MPC;
  https://rankinstudio.com/Asteroid_Discovery_Credit_MPEC_2010-U20) says credit requires
  **at least 2 nights >= 12 h apart at the discovery opposition**, and goes to "the
  observatory / individual that submitted those earliest observations". This is a
  secondary source; the MPEC text itself was not opened.
- The page says nothing specific about archival data or third parties measuring others'
  images.

From "Singletons and Archival Observations Committee (SARC)"
(https://docs.minorplanetcenter.net/mpc-ops-docs/data-and-services/sarc/):

- The MPC formed SARC because "occasional erroneous measurements of images from public
  archives might be submitted by third party users".
- Anyone planning to submit archival observations from a listed archive must contact the
  corresponding SARC member "before submitting the data to the MPC". The page lists
  Tyler Linder as the contact for **Cerro Tololo / DECam** (and SDSS).
- The MPC keeps a list of users allowed to submit single measurements; observatory codes
  require a sample of observations of known objects; submitters must do their due
  diligence.

From "Reporting Observations"
(https://docs.minorplanetcenter.net/mpc-ops-docs/astrometry/reporting-observations/)
and the MPC newsletter of October 2026
(https://buttondown.com/MPC_newsletter/archive/newsletter-october-2026/):

- ADES is "strongly" preferred (XML or PSV via web form or cURL; ADES cannot be emailed).
  MPC1992 80-column is still accepted (cURL or email to obs@cfa.harvard.edu).
- From 2026-12-30 the MPC accepts only ADES version 2022 (not 2017).
- Report at least three observations per object per night if possible; archival
  astrometry should include magnitudes. Do not report preliminary measures you intend
  to replace.
- Archival programs go through SARC review; the MPC is tightening program/obs-code rules.

## 3. What a student can and cannot claim

Can claim (if the work holds up):
- "I built a pipeline that recovers X% of known asteroids in NSC DR2 field F and found
  N single-night tracklets that no catalogued orbit (SkyBoT / JPL sb_ident) predicts."
- Measurement work: archival astrometry, if accepted by the MPC via the SARC route,
  becomes MPC-published observations with the student as measurer.

Cannot claim:
- "Discovery" of anything. A single-night tracklet gets no designation at all. A
  designation needs an orbit (multi-night). Discovery credit needs >= 2 nights at the
  discovery opposition and goes to the earliest identifiable observations; for DECam
  data the observations were taken by the DECam program/observers at CTIO (observatory
  code W84), and the MPC credits observations, not later catalogue mining by itself.
  How the MPC would split credit between the original observers and a third-party
  measurer of archival data is not stated on the pages opened; this is UNRESOLVED and
  must be asked of the SARC DECam contact.
- "New" in the absolute sense, because THOR and CANFind already searched this catalogue
  and their unknown-object lists are not in SkyBoT/JPL.
