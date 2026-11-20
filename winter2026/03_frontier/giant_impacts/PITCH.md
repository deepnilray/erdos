# A systematic search for planetary-collision afterglows in NEOWISE

Deepnil Ray, Ashoka University. One-page summary, 20 November 2026.

**The question.** Rocky planets are thought to finish forming through giant impacts between planet-sized bodies, the kind of
collision that made our Moon. Such a collision fills the inner system with hot dust, which shows up as a sudden, lasting
brightening in the mid-infrared. Only a handful of such events are known, most found by chance, and no one has measured how often
they happen.

**What I did.** I searched the 2014-2024 NEOWISE single-exposure light curves (3.4 and 4.6 micrometres, one visit every six months)
of 699,341 Gaia DR3 main-sequence stars within 250 pc, looking for a sustained brightening that is stronger at 4.6 than at
3.4 micrometres (warm dust). The search ran end to end on public archives through GitHub Actions.

**Validation.** Without being told where to look, the search finds the best-known collision afterglow, ASASSN-21qj
(Kenworthy et al. 2023, Nature 622, 251), with the highest score of all 611,091 stars that have usable light curves.

**Candidates.** Three field stars pass every archival check (comparison with 75-135 neighbouring stars observed at the same times,
centroid stability, saturation, pre-event colours, optical and TESS light curves, SIMBAD, VizieR and ADS full-text searches):

| Star | Event | Literature |
|---|---|---|
| Gaia DR3 5792808347020475136 (K dwarf, 247 pc) | 2018: 4.6 um flux up 46%, dust about 1100 K, steady for six years; no optical change above ~3% | No SIMBAD entry; no paper |
| Gaia DR3 2891196718939580672 = ASASSN-V J060000.76-310027.83 (K dwarf, 157 pc) | 2020: 4.6 um flux up 16%, dust about 800 K, coincident with its known 2019 optical dimming, now fading | The dimming is known (ATels 13346-13450); the infrared brightening is not reported |
| Gaia DR3 5808318474663998464 (G dwarf, 240 pc, member of a ~97 Myr old group) | 2021: 4.6 um flux up 15%, about 1300 K, but the optical flux also rose | Not reported; ambiguous (stellar activity possible) |

**None of these is a confirmed collision.** The remaining tests need a spectrum (lithium for age, radial velocities for a hidden
companion) and Gaia DR4 epoch photometry and astrometry, released 2 December 2026.

**What I would like to do with you this winter.**
1. Vet the candidates, including a spectrum of the first star from a southern telescope (declination -76 deg).
2. Extend the search to 250-500 pc (about 3 million stars; already running).
3. Measure the search's completeness by injecting the shapes of known events into real light curves, and turn the detections
   into the first measured rate of such events per star per year.
4. Write it up as a paper.

All data, code and checks: github.com/deepnilray/erdos, branch claude/winter-2026-plan, folder winter2026/03_frontier/giant_impacts.
