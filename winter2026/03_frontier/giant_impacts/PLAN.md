# The flagship bet: a systematic search for planetary-collision afterglows (VarWISE x Gaia DR4 x ZTF)

Written 2026-11-17 by Claude for Deepnil Ray. This is the idea in this folder with the highest ceiling that his existing
pipelines (deepnilray/SearchChev, deepnilray/varwise) are already built for.

## Why it matters
Giant impacts between planets build terrestrial planets and moons, yet only a handful of candidate afterglows are known:
ASASSN-21qj (Kenworthy et al. 2023, Nature; arXiv:2310.08360) showed an infrared brightening of 0.4 mag in W1 and 0.8 mag in
W2 about 900 days before a deep optical dimming, consistent with a 1000 K body at 4% of the stellar luminosity, followed by the
transit of the debris cloud. Others: Gaia20ehk (Gaia-GIC-1), NGC 2547-ID8, HD 166191, V488 Per (list from the Gaia20ehk
Wikipedia page, to be checked against the papers). A June 2026 modelling paper (arXiv:2606.26026, abstract read) shows impacts
should appear as a sudden brightening then gradual dimming in optical and near-infrared, and says a systematic search in large
surveys may find many more. A first systematic sample would measure how often terrestrial-planet impacts happen, a number
planet-formation theory predicts but nobody has measured.

## Why now, and why Deepnil
- VarWISE (Paz et al., ApJS 284, 41) catalogues about 1.9 million mid-infrared variables from NEOWISE (2014 to 2024).
- Gaia DR4 on 2 December 2026 releases epoch photometry for all sources for 2014.6 to 2020.0 (first time for non-variables).
- ZTF covers 2018 onward in g and r. Together these give simultaneous optical and infrared light curves over a decade.
- SearchChev already does VarWISE x Gaia DR3 x ZTF cross-matching through GitHub Actions.

## Selection (signature of an impact afterglow)
1. Host: Gaia main-sequence FGK or early-M star (DR3 astrophysical parameters, CMD position), parallax S/N > 5, RUWE < 1.4,
   no known YSO, no Galactic-plane star-forming region membership, no IR excess before the event (ALLWISE 2010 colours).
2. Infrared: a step or ramp brightening in W1 and W2 lasting hundreds to thousands of days, reddening W1-W2 consistent with
   500 to 1500 K dust, sustained (not a single-epoch outlier, not periodic).
3. Optical: flat before the IR event; aperiodic dips or a slow dimming afterwards (Gaia G, ZTF g/r), possibly wavelength
   dependent. A flat optical curve with an IR step is still interesting (impact not yet transiting).
4. Kill list: Miras and AGB (periodic, red giants), YSO dippers and outbursts, blends (Gaia neighbours within 6", the WISE beam),
   background AGN (Gaia QSO candidates, CatWISE colours), eclipsing binaries, NEOWISE artefacts near bright stars.

## Validation before any search (protocol)
- Recovery test: the pipeline must flag ASASSN-21qj and at least one other known afterglow from real data, blind.
- Planted control: none synthetic for training; recovery of the known objects is the control. Report false-positive rate on a
  random sample of 10^4 main-sequence VarWISE stars by eye-checking the top 50.
- Forecast written before the run.

## Steps
1. Now (before DR4): build on SearchChev with ZTF + NEOWISE + Gaia DR3, recover ASASSN-21qj, run on the VarWISE pure catalogue.
2. 2 Dec 2026: add Gaia DR4 epoch photometry for the survivors (DataLink per source; small) to cover 2014 to 2018.
3. Every candidate: by-eye light-curve check, Pan-STARRS/DECaLS imaging for blends, VSX/SIMBAD/ADS search, literature check.
4. Write-up: a catalogue of impact-afterglow candidates with rates; ask for spectroscopic follow-up through a professor.

## Risks, most worrying first
1. Priority: the Kenworthy group, the Gaia science-alerts team and the VarWISE team are the obvious competitors.
   A prior-art search for "systematic giant impact search WISE" beyond the two searches done on 2026-11-17 is step 0.
2. YSOs and dusty variables vastly outnumber impacts; the host-star cut is where the search lives or dies.
3. The WISE beam (6") blends neighbours, so many IR steps will belong to another star.
