# Prof. T. R. Seshadri: reading project and winter project options

Written 2026-11-16 by Claude for Deepnil Ray. Read `../README.md` first.

Labels: VERIFIED-SOURCE means the reference was seen on a primary or reference-list page on 2026-11-16, with the page named.
UNVERIFIED means it is from memory or an earlier chat and must be checked against arXiv/ADS/INSPIRE before it goes in any
email or document. Never send a citation from this file without opening the paper.

## 00. LEAD PITCH (2026-11-20): Deepnil's own systematic search found new candidates

Verdict first: lead with the data-discovery project, because Seshadri said he wants data analysis that finds undiscovered things,
and Deepnil now has results in hand. Keep section 0a (his helical magnetogenesis model) as the theory half.

What to say: "I ran what appears to be the first systematic search of NEOWISE infrared light curves for planetary-collision
afterglows: 699,341 nearby Sun-like and K-type main-sequence stars from Gaia. It recovers the known collision ASASSN-21qj blindly
(score 38; no other star in 611,091 with light curves comes close except three). Two of the three are stars with nothing in the
literature I could find, where hot dust (about 1100 K and 1300 K) appeared suddenly in 2018 and in 2021 and is still there. The
third is a known 2019 dimming star whose infrared brightening nobody seems to have reported. Could we vet these together this
winter and write it up?"

What he would do with you (a decent amount of real work, all of it his kind of thing: careful data analysis):
1. Vet the three: SIMBAD/VSX/literature; ASAS-SN and Gaia DR4 (2 December) optical light curves, looking for the dimming that marks
   debris passing in front of the star; TESS pixel-level photometry (Deepnil's skill) for dips; ages from rotation and, if a
   telescope is reachable, a lithium spectrum.
2. Measure the completeness of the search by injecting the ASASSN-21qj and J060000 light-curve shapes into real quiet stars, and
   turn the detections into the first measured rate of such events per star per year (with error bars).
3. Paper: "A systematic NEOWISE search for planetary-collision afterglows in 7 x 10^5 nearby main-sequence stars".
Evidence and files: ../03_frontier/giant_impacts/LOG.md (2026-11-20 entries), CANDIDATES.md, candidates/new_candidates_lc.png.
Honest risks: the literature gate is not passed (SIMBAD unreachable from our machines); each candidate could still be a hidden
young star, an unresolved companion, or a known variable; none is a discovery until those checks pass.

## 0a. NEW TOP RECOMMENDATION (2026-11-20): "Does the sky already constrain your 2018 helical model?"

Verdict first: the best project to ask him for is to confront HIS OWN helical inflationary magnetogenesis model
(Sharma, Subramanian & Seshadri, PRD 97, 083503 (2018), arXiv:1802.04847) with the 2025-2026 small-scale-structure data on
primordial magnetic fields (PMFs): the Lyman-alpha forest bound and hint (Pavicevic et al., arXiv:2501.06299), JWST/reionisation
(Fairbairn et al., arXiv:2604.24835) and strong-lensing substructure (Gilman et al., arXiv:2112.03293). Pilot numbers below say
the low-reheating corner of his model may already be ruled out, and the Lyman-alpha hint (B ~ 0.2 nG) would correspond to
reheating at roughly the QCD-to-GeV scale. It extends his paper rather than criticising it, it has a clean theory core (the
matter power spectrum sourced by a FULLY HELICAL field, which no paper found has computed), and it ends in a number he can quote.

Why he should care (each point checked against the source named)
- His model's table (1802.04847, Table 1, LaTeX source read 2026-11-20): maximal present-day field and coherence length
  5 MeV: 6.4 nG at 1.6 Mpc; 150 MeV: 0.99 nG at 0.58 Mpc; 100 GeV: 0.039 nG at 0.068 Mpc; 1000 GeV: 0.0071 nG at 0.032 Mpc.
  Fields of 0.1-1 nG coherent over 0.1-1 Mpc are exactly what the Lyman-alpha forest and JWST now test (k ~ 10-100 Mpc^-1).
- Lyman-alpha (2501.06299, full text read): hint of extra power fitted by B_1Mpc = 0.2 +/- 0.05 nG (n_B = -2.9); with
  conservative noise modelling, B < 0.30 nG at 3 sigma. Note: its abstract says k_peak ~ 20 Mpc^-1 for the hint, but its body
  gives k_peak = 48 Mpc^-1 for 0.2 nG and 20.1 Mpc^-1 for 0.5 nG; our code reproduces the body (47.9 and 19.9).
- JWST/reionisation (2604.24835, abstract read): sqrt<B^2> < 0.27 nG (n_B = -2) and < 0.18 nG (n_B = +2), 95%, "in Gaussian,
  non-helical scenarios". Ralegankar, Pavicevic & Viel (2402.14079, LaTeX read) likewise "focus on non-helical PMFs".
  So the helical case, which is what his model produces, is an explicit gap. OPEN as far as searched (INSPIRE citations of
  1708.08119 and 1802.04847 listed 2026-11-20, plus two alphaXiv searches); older LSS papers (e.g. Kahniashvili et al. 2013,
  arXiv:1211.2769) not yet read for helical terms.

Pilot computation (CONJECTURED as physics, VERIFIED as arithmetic): pmf_lensing/helical_model_pilot.py, output in
pmf_lensing/helical_model_pilot_output.txt. Non-helical Lorentz-force kernel of 2402.14079 integrated numerically for his
spectrum (k^4 below k_c = 2 pi/L_c, k^-2/3 assumed above, damping at lambda_D = 0.088 Mpc (B/nG)), growth from the two-fluid
equations, LCDM from CAMB. Controls fired: integrator reproduces the paper's G for n_B = -2.5 and -2.0 to 3% and 0.6%;
calibration constants from the two agree to 3%; zero field gives zero boost; k_peak of the n_B = -2.9 reference models matches
2501.06299 to 0.5%.
log10(P/P_LCDM) at k = 10, 20, 30, 50 Mpc^-1:
- Lyman-alpha reference, n_B = -2.9: 0.2 nG (hint) 0.01, 0.13, 0.33, 0.47; 0.3 nG (3 sigma bound) 0.06, 0.34, 0.50, 0.23;
  0.5 nG (strongly excluded) 0.26, 0.55, 0.28, 0.00.
- His model, T_r = 150 MeV, maximal field: 0.28, 1.37, 1.08, 0.01 -> far above the excluded 0.5 nG reference: likely ruled out.
- T_r = 150 MeV with 1% of the maximal EM energy (B = 0.10 nG): 0.00, 0.01, 0.06, 0.25 (0.56 at k = 80): hint-like.
- T_r = 5 MeV with 1%: 0.67, 1.23, 1.21, 0.39 -> likely ruled out. T_r >= 100 GeV: no visible effect.
Biggest uncertainties, each a piece of the project: the helical kernel (missing here), the damping scale for blue spectra
(kappa; 2402.14079 shows the peak power scales as kappa^-4), the small-scale tail after the inverse cascade, and mapping a
peaked spectrum onto bounds derived for n_B = -2.9 (Pavicevic and arXiv:2609.39399 say models with equal k_peak behave alike).

What the project is (winter-sized, theory plus public data)
1. Derive the scalar Lorentz-force power spectrum for a field with helical part (the antisymmetric term in <B_i B_j>), for
   his spectrum. Seshadri has done the analogous helical calculation for the CMB (Jagannathan, Sharma & Seshadri 2020,
   arXiv:2010.08836), so this is home ground for him.
2. Run his model over (T_r, epsilon) and map each case to k_peak and amplitude; compare with the Lyman-alpha, JWST and lensing
   bounds. Output: the excluded region in the (T_r, epsilon) plane and the band that would explain the Lyman-alpha hint.
3. Forecast: what DESI/ESPRESSO Lyman-alpha and JWST-era lensing samples would do.

Risks, worst first: (1) his former student Ramkishor Sharma and Subramanian are active on low-scale magnetogenesis (arXiv:2611.19721,
Nov 2026) and could do this themselves, which is a reason to propose it through Seshadri, not around him; (2) the Trieste group
(Viel, Pavicevic, Ralegankar, D'Ambrosio) owns the PMF-matter-power pipeline; (3) the pilot uses a non-helical kernel and a
guessed tail, so the "ruled out" statements may move by a lot.

How to ask (one sentence): "Sir, the 2025 Lyman-alpha forest analysis finds a hint of a 0.2 nG primordial field and a 0.3 nG
bound; your 2018 helical model gives about 1 nG at 0.6 Mpc for QCD-scale reheating. Could I work out over the winter what these
small-scale constraints imply for the reheating temperature in your model, including the helical contribution?"
Bring: the pilot table above, and the line that the helical case is explicitly left open by 2604.24835 and 2402.14079.

Second option (data, Deepnil's own pipeline): the strong-lensing route alone is EMPTY today. pmf_lensing/pmf_vs_lensing.py
shows that even the 0.5 nG model sits within 0.7 sigma of the Gilman et al. 2022 lensing constraints (log10 P/P_LCDM =
0.0 +/- 0.4 at k = 10, 0.1 +0.7/-0.6 at 25, 0.2 +1.0/-0.9 at 50 Mpc^-1, 68%). Lensing becomes decisive only with larger JWST
samples; keep it as the forecast part of step 3.

## 0. Verdict first (2026-11-16; superseded by 0a for the project, still valid for the reading list)

- Recommended approach: ask him for the **reading project** on primordial magnetic fields (section 3), and bring **one concrete
  question about his own 2017 paper** (section 4.1, now framed as a question, since its main content is already in that paper). Keep option 4.2 (Gaia streams and
  strong lensing as a magnetic-field probe) as the data-driven follow-on, since it uses the pipeline skills Deepnil already has
  (Gaia, TESS, ZTF, catalogue cross-matching). Option 4.3 (rotation measures with new survey data) was found OCCUPIED on
  2026-11-17 by arXiv:2605.16924, and option 4.1 is mostly answered inside 1708.08119 itself (see 4.1).
- Nothing in this file argues against his work or claims a flaw in it. Every option either extends his models or applies new data
  to questions he has published on.
- Publication list verified 2026-11-17 (section 2A). Prior-art checks: see sections 4.1 to 4.3.

## 1. Who he is (what was confirmed)

- Professor, Department of Physics and Astrophysics, University of Delhi; coordinator of ICARD, an IUCAA resource centre at Delhi
  University (VERIFIED-SOURCE: sites.google.com/view/icardphysics/members). Deepnil knows him as the teacher of his Ashoka course
  Physics of the Universe (PHY-2850/AST-2850), from Deepnil's own statement. His exact Ashoka position was not confirmed online.
- Stated research areas on the ICARD page: extragalactic magnetic fields from Faraday rotation measures of background quasars;
  cosmological magnetogenesis in the early universe; the CMB as a probe of primordial magnetic fields; late-time cosmic
  acceleration including higher dimensions; density perturbations from inflation; gravitational waves; astrophysical plasma and
  dynamo theory; chiral plasma and chiral MHD; QCD and electroweak phase transitions; reionization.
- A 2013 Delhi University student blog describes him as saying research in pure science is like poetry (physicsatdu.blogspot.com,
  2013). Useful only as a hint that he likes conceptually clean questions.

## 2. Papers of his seen today (rows re-checked 2026-11-17)

INSPIRE = inspirehep.net/api/literature?q=a%20T.Seshadri.1 (his INSPIRE BAI is T.Seshadri.1; the BAI T.R.Seshadri.1 returns
nothing). arXiv = the arXiv abs page of the listed id. Both were opened on 2026-11-17.

| Paper | Status |
|---|---|
| Seshadri and Subramanian, PRL 87, 101301 (2001), CMB polarisation from tangled magnetic fields, astro-ph/0012056 | VERIFIED: INSPIRE + arXiv listing |
| Subramanian, Seshadri and Barrow, MNRAS 344, L31 (2003), astro-ph/0303014 | VERIFIED: INSPIRE + arXiv listing |
| Seshadri and Subramanian, PRL 103, 081303 (2009), CMB bispectrum from primordial magnetic fields on large angular scales, arXiv:0902.4066 | VERIFIED: INSPIRE + arXiv listing |
| Trivedi, Subramanian and Seshadri, PRD 82, 123006 (2010), arXiv:1009.2724 | VERIFIED: INSPIRE + arXiv listing |
| Trivedi, Seshadri and Subramanian, PRL 108, 231301 (2012), CMB trispectrum and magnetic field limits, arXiv:1111.0744 | VERIFIED: INSPIRE + arXiv listing |
| CORRECTED. The earlier row merged two papers. (a) Atmjeet, Pahwa, Seshadri and Subramanian, "Cosmological magnetogenesis from extra-dimensional Gauss-Bonnet gravity", PRD 89, 063002 (2014), arXiv:1312.5815. (b) Atmjeet, Seshadri and Subramanian, "Helical cosmological magnetic fields from extra-dimensions", PRD 91, 103006 (2015), arXiv:1409.6840 (no Pahwa) | VERIFIED: INSPIRE + arXiv listing |
| Sharma, Jagannathan, Seshadri and Subramanian, "Challenges in inflationary magnetogenesis: constraints from strong coupling, backreaction and the Schwinger effect", PRD 96, 083511 (2017), arXiv:1708.08119 | VERIFIED: arxiv.org/abs/1708.08119 + INSPIRE |
| Sharma, Subramanian and Seshadri, "Generation of helical magnetic field in a viable scenario of inflationary magnetogenesis", PRD 97, 083503 (2018), arXiv:1802.04847 | VERIFIED: INSPIRE + arXiv listing |
| Malik, Chand and Seshadri, "Role of intervening Mg II absorbers on the rotation measure and fractional polarisation of the background quasars", ApJ 890 (2020) no. 2, arXiv:1710.10396 (first posted Oct 2017) | VERIFIED: arxiv.org/abs/1710.10396 (journal ref from that page; article number not checked). Not on his INSPIRE profile |

Reading these is the price of entry for the conversation: open the 2017 and 2018 papers and the trispectrum PRL before meeting him.

## 2A. Verified publication list, 2010 to 2026

Sources: INSPIRE (query above, 57 records, but the profile is contaminated with papers by Ranjani Seshadri, a condensed-matter
physicist; those are excluded below) and the arXiv API search au:Seshadri_T sorted by date, both run 2026-11-17. Every row
below appeared in at least one of the two. No paper dated 2025 or 2026 with T. R. Seshadri as author was found in either.

**2022 to 2026 (what he is doing now)**

| Year | Paper | Journal | arXiv | What it is about |
|---|---|---|---|---|
| 2024 | Goyal, Malik, Yadav, Seshadri, "Investigating cosmic homogeneity using multifractal analysis of the SDSS-IV eBOSS DR16 quasar catalogue" | MNRAS 530, 2866 (2024) | 2404.09197 | Scale of homogeneity from multifractal dimensions of eBOSS quasars; continues his fractal-homogeneity line from 2005 and 2007 |
| 2023 | Sharma (Rahul), Jain, Paul, Seshadri, "AstroSat observation of the magnetar SGR J1830-0645 during its first detected X-ray outburst" | MNRAS 526, 4877 (2023) | 2310.04079 | X-ray timing and spectroscopy of a magnetar with AstroSat |
| 2023 | Kaur, Nandi, Choudhury, Seshadri, "Universe bouncing its way to inflation" | IJMPD 33, 2450006 (2024) | 2302.13698 | A bounce followed by inflation in one model |
| 2022 | Sharma (Ekta), Gopinathan, Soam, Lee, Seshadri, "Core orientations and magnetic fields in isolated molecular clouds" | arXiv comment says accepted in MNRAS; volume not checked | 2209.01509 | Optical and Planck polarisation versus Herschel core orientations in eight clouds; finds random core-field alignment |

Reading of this: since 2020 his output is mostly co-supervised student papers on observational topics (homogeneity, Galactic
magnetic fields, X-ray), plus one early-universe paper. His last primordial-magnetic-field papers are 2019 to 2021. A
primordial-magnetism or rotation-measure project would revive a line he has not published on recently, which may be welcome or
may mean his students have moved on; ask him.

**2010 to 2021**

| Year | Paper | Journal | arXiv |
|---|---|---|---|
| 2021 | Bagla et al. (with Seshadri), "The life and science of Thanu Padmanabhan" | none listed | 2110.03208 |
| 2020 | Jagannathan, Sharma, Seshadri, "Imprints of the post recombination dissipation of helical magnetic field on the CMB" | IJMPD 30, 2050122 (2021) | 2010.08836 |
| 2020 | Pandey, Malik, Seshadri, "Implications of baryon-dark matter interaction on IGM temperature and tSZ effect with magnetic field" | MNRAS 500, 643 (2020) | 2006.07901 |
| 2019 | Sharma, Subramanian, Seshadri, "Gravitational wave generation in a viable scenario of inflationary magnetogenesis" | PRD 101, 103526 (2020) | 1912.12089 |
| 2019 | Jagannathan, Malik, Jain, Seshadri, "Impact of magnetic field on the gas mass fraction of galaxy clusters" | New Astron. 84, 101531 (2021) | 1909.07847 |
| 2018 | Gupta, Sharma, Seshadri, "Scalar spectral index in the presence of primordial black holes" | IJMPD 29, 2050029 (2020) | 1805.10859 |
| 2018 | Sharma, Subramanian, Seshadri, "Generation of helical magnetic field in a viable scenario of inflationary magnetogenesis" | PRD 97, 083503 (2018) | 1802.04847 |
| 2017 | Malik, Chand, Seshadri, "Role of intervening Mg II absorbers on the rotation measure and fractional polarisation of the background quasars" | ApJ 890 (2020) | 1710.10396 |
| 2017 | Sharma, Jagannathan, Seshadri, Subramanian, "Challenges in inflationary magnetogenesis..." | PRD 96, 083511 (2017) | 1708.08119 |
| 2016 | Bandyopadhyay, Choudhury, Seshadri, "Studying neutral hydrogen structures during the epoch of reionization using fractal dimensions" | MNRAS 466, 2302 (2017) | 1611.05554 |
| 2014 | Singh, Choudhary, Seshadri, "Excitation of coherent states: wave function development and analysis" | none listed | 1412.0841 |
| 2014 | Atmjeet, Seshadri, Subramanian, "Helical cosmological magnetic fields from extra-dimensions" | PRD 91, 103006 (2015) | 1409.6840 |
| 2013 | Atmjeet, Pahwa, Seshadri, Subramanian, "Cosmological magnetogenesis from extra-dimensional Gauss-Bonnet gravity" | PRD 89, 063002 (2014) | 1312.5815 |
| 2013 | Trivedi, Subramanian, Seshadri, "Primordial magnetic field limits from the CMB trispectrum: scalar modes and Planck constraints" | PRD 89, 043523 (2014) | 1312.5308 |
| 2013 | Pahwa, Choudhury, Seshadri, "Inflation in higher dimensional Gauss-Bonnet cosmology" | none listed | 1302.3977 |
| 2012 | Thakur, Nautiyal, Sen, Seshadri, "Thawing versus tracker behaviour: observational evidence" | MNRAS 427, 988 (2012) | 1204.2617 |
| 2012 | Sriramkumar, Seshadri (eds.), "Vignettes in Gravitation and Cosmology" (book) | none listed | none |
| 2011 | Trivedi, Seshadri, Subramanian, "CMB trispectrum and primordial magnetic field limits" | PRL 108, 231301 (2012) | 1111.0744 |
| 2011 | Unnikrishnan, Thakur, Seshadri, "Can f(R) gravity mimic dark energy with constant equation of state parameter?" | none listed | 1106.6353 |
| 2011 | Pahwa, Choudhury, Seshadri, "Late-time acceleration in higher dimensional cosmology" | JCAP 09 (2011) 015 | 1104.1925 |
| 2010 | Trivedi, Subramanian, Seshadri, "Primordial magnetic field limits from CMB bispectrum of magnetic passive scalar modes" | PRD 82, 123006 (2010) | 1009.2724 |
| 2010 | Thakur, Sen, Seshadri, "Non-minimally coupled f(R) cosmology" | PLB 696, 309 (2011) | 1007.5250 |
| 2010 | Deb, Singh, Seshadri, Gupta, "A CCD photometric study of the newly discovered contact binary ASAS 134738+0410.1" | BASI 38, 77 (2010) | 1005.3885 |
| 2010 | Deb, Singh, Seshadri, Gupta, "A CCD photometric study of the late type contact binary EK Comae Berenices" | New Astron. 15, 662 (2010) | 1004.5448 |
| 2010 | Deb, Tiwari, Singh, Seshadri, Chaubey, "Photometry of the delta Scuti star HD 40372" | none listed | 1001.3472 |

Status of the whole table: VERIFIED as listed on INSPIRE and/or the arXiv API on 2026-11-17 (titles, authors, ids; journal
data as given there). ADS was not queried (no API token here), so a paper absent from both INSPIRE and arXiv would be missed.
Note for the talk with him: he has variable-star photometry papers (2010), so Deepnil's TESS/ZTF variable-star work is common
ground too.

## 3. The reading project to ask for

Ask: "Sir, could I do a reading project with you on primordial magnetic fields over the winter, from generation to observational
limits?" It is cheap for him to say yes, it is squarely his field, and it ends with Deepnil able to talk to him as a colleague.

Suggested ladder (check every item before showing it to him):
1. K. Subramanian, "The origin, evolution and signatures of primordial magnetic fields", Rep. Prog. Phys. 79, 076901 (2016),
   arXiv:1504.02311 (VERIFIED-SOURCE: ar5iv page). Sections on MHD in an expanding universe, inflationary generation, CMB
   signatures. Extract: the B scaling with a, the strong-coupling and backreaction problems, the Alfvén damping scale.
2. R. Durrer and A. Neronov, "Cosmological magnetic fields: their generation, evolution and observation", A&A Rev. 21, 62 (2013)
   (VERIFIED-SOURCE: cited on a Subramanian 2024 talk slide; arXiv number not checked). Extract: the observational window,
   including blazar limits near 10^-16 G in voids.
3. Sharma, Jagannathan, Seshadri, Subramanian 2017 (his model). Extract: the rise-and-fall coupling function and why the final
   spectrum is blue.
4. Sharma, Subramanian, Seshadri 2018 (helical version). Extract: the reheating bound.
5. Seshadri and Subramanian 2009 and Trivedi, Seshadri, Subramanian 2012 (non-Gaussian CMB signatures). Extract: why the
   bispectrum and trispectrum constrain B at the nG level.
6. Jedamzik and Pogosian 2020, arXiv:2004.09487, magnetic fields and the Hubble tension (UNVERIFIED: seen only in a reference
   list). Extract: the field strength needed and the clumping mechanism.
7. Sanati et al. 2020, arXiv:2005.05401, primordial fields and dwarf galaxies (read in full on 2026-11-16). Extract: how a field
   changes the halo mass function below 10^9 solar masses.

## 4. Options for the bigger project, best first

### 4.1 "Is the k^4 spectrum a theorem?" (his own model): CHECKED 2026-11-17, mostly OCCUPIED

What arXiv:1708.08119 actually says (VERIFIED: read in the LaTeX source from arxiv.org/e-print/1708.08119, section "Solving the
strong coupling problem"):
- The model is not rise-and-fall inside inflation. f = (a/a_i)^alpha grows during de Sitter inflation from f_i = 1, and then
  f = f_f (a/a_f)^(-beta) decays during a post-inflation matter-dominated phase until reheating, with beta = alpha N / N_r so that
  f(a_r) = 1. The transition at a_f is sharp: f, A-bar and A-bar' are matched continuously there. alpha > 1/2 is assumed.
- Outside the horizon they write A-bar_2 = d_1 + d_2 ∫ dη / f_2^2 (their eq. eqa2) and state that d_1 is the decaying mode while f
  falls, so a non-zero d_2 is needed. d_2 comes from matching A-bar' at the end of inflation, and they note it is dominated by the
  higher-order (k/aH)^2 terms of the c_1 branch rather than the c_2 branch.
- Result at reheating, keeping dominant terms: dρ_B/d ln k ∝ k^(8 - 2 alpha) (a/a_f)^(4 beta + 1), and dρ_E/d ln k ∝ k^(6 - 2 alpha),
  with the electric energy dominating. For alpha = 2 (scale-invariant B and E during inflation) this is k^4. For alpha = 3 they
  state it gives k^2. So k^4 is not universal even inside their paper; the slope is set by the inflation-era exponent alpha only,
  and beta enters the amplitude.
- The words "the surviving magnetic field is the inflation-era electric field" do not appear, but the mathematics is exactly that:
  d_2 = f^2 A-bar' at a_f is the frozen electric field, and it is the only growing piece.
- The physical picture is stated explicitly elsewhere. Giovannini, "Inflationary magnetogenesis in the perturbative regime",
  CQG 38 (2021) 135018, arXiv:2012.14720 (VERIFIED: arXiv abs page) says the late-time super-horizon magnetic spectra are determined
  by the electric fields at the end of inflation when the coupling first increases, and he uses smooth (not abrupt) coupling
  evolution. Smooth and featured couplings are also studied by Tripathy, Chowdhury, Jain, Sriramkumar, PRD 105, 063519 (2022),
  arXiv:2111.01478 (VERIFIED: arXiv abs page), but those concern features during inflation.

Verdict: the "converted electric field" picture is OCCUPIED (implicit in 1708.08119, explicit in 2012.14720), and the
"k^4 lower bound" question is answered in the negative by 1708.08119 itself (alpha = 3 gives k^2; the backreaction limit on alpha
is what bounds the slope). Do not present either as new to him.
What is left, honestly small: a clean statement that the final slope 8 - 2 alpha does not depend on the shape of the transition or
on the post-inflation equation of state (sharp matching in 1708.08119; Giovannini covers smooth cases in his own setup), and an
exact Pöschl–Teller-type example. Use it as a good question showing Deepnil has read his paper ("does the slope depend only on
alpha, for any smooth fall of f?"), not as a project claim.

### 4.2 Gaia stellar streams as a test of the magnetic fix to the Hubble tension
Full write-up and first computation in `../03_frontier/FRONTIER_IDEAS.md`, section 3. Today's GD-1 and Pal 5 data are too weak
(EMPTY); measured to 0.15 dex per mass decade from 10^5 to 10^9 solar masses, streams would test fields from about 0.05 to
0.7 nG. It joins his CMB-limits work to Gaia, which Deepnil already uses. Stated honestly to him as a forecast project.

PRIOR-ART CHECK 2026-11-17: APPARENTLY OPEN for streams and for strong-lensing substructure specifically; the neighbouring
small-scale probes are crowded. Method: INSPIRE abstract searches ("primordial magnetic" with lensing, stellar stream, subhalo,
substructure, flux ratio, strong lensing, halo mass function, dwarf/satellite galaxies), run 2026-11-17; the arXiv API was
rate-limited and ADS was not queried, so this is not exhaustive.
- No paper found that uses GD-1, Pal 5 or any stellar stream, or strong-lens flux ratios, to constrain primordial magnetic fields.
- Closest, all VERIFIED on INSPIRE records or arXiv abs pages:
  - Pavicevic, Irsic, Viel, Bolton et al., PRL 135, 071001 (2025), arXiv:2501.06299: first Lyman-alpha forest PMF constraints
    from hydro simulations; a hint of extra power fitted by B ~ 0.2 nG (k_peak ~ 20/Mpc). This sits inside the 0.05 to 0.7 nG
    window of our stream forecast, which makes a stream or lensing cross-check more interesting, and also more contested.
  - D'Ambrosio and Viel, "Constraining primordial magnetic fields with weak lensing", arXiv:2610.00485 (Oct 2026): N-body plus
    convergence-spectrum emulator, forecast B_1Mpc < 0.8 to 1.6 nG.
  - Ralegankar, Garaldi, Viel, arXiv:2410.02676 (2024), and Ralegankar, Pavicevic, Viel, arXiv:2402.14079 (2024): the PMF-induced
    matter power spectrum into the non-linear regime (the input a stream or lensing analysis would need).
  - Ralegankar, PRL 131, 231002 (2023), arXiv:2303.11861: PMFs make 10^-11 to 10^3 solar-mass dark-matter minihalos.
  - Sanati et al., arXiv:2005.05401 (2020) and arXiv:2403.05672 (2024): dwarf-galaxy constraints.
  - Gilman, Benson, Bovy et al., arXiv:2112.03293 (arXiv abs page opened; journal said to be MNRAS 2022, DOI stac670, not checked): the small-scale primordial matter power spectrum from 11 quad
    lenses, parametrised generically; never mapped onto PMF parameters in that paper. Re-casting its posterior (and the GD-1
    subhalo results, e.g. arXiv:1911.02662, UNVERIFIED: seen only as a search-result title) in terms of B and n_B is the cheapest open step.
- Competition risk: the Trieste group (Viel, Ralegankar, Pavicevic, D'Ambrosio) is moving through every small-scale probe in turn;
  strong lensing or streams is a natural next paper for them. Move quickly if Seshadri likes it.

### 4.3 Rotation measures of quasars behind intervening galaxies, with the new radio and spectroscopic surveys
This is the data version of his own Faraday-rotation line of work: do sightlines through intervening Mg II absorbers show extra
rotation-measure scatter, and what field strength does that imply? New since his paper: the LoTSS DR2 rotation-measure grid,
SPICE-RACS and POSSUM from ASKAP, the Van Eck 2023 consolidated catalogue (downloaded here, 59,530 rows), and DESI and Gaia
(Quaia) quasar and absorber catalogues. It fits Deepnil's cross-matching pipeline skills exactly.
PRIOR-ART CHECK 2026-11-17: OCCUPIED. Drop this as a stand-alone proposal.
- Malik, O'Sullivan, Thomson, Anderson, Van Eck, Rudnick, Seta et al., "Magnetised CGM gas at z~1 revealed by SPICE-RACS",
  arXiv:2605.16924 (May 2026; VERIFIED: arXiv abs page). Exactly this test redone: SPICE-RACS DR2 rotation measures crossed with
  DESI DR1 quasars, 2483 sightlines (612 with Mg II), foreground-cleaned 191 Mg II versus 566 control, a 4.5 sigma excess residual-RM
  dispersion of 4.13 +/- 0.91 rad/m^2 at median absorber z ~ 1.14, implying about 0.4 to 0.8 microgauss CGM fields over 20 to 150
  kpc. First author Sunil Malik is Seshadri's own co-author on the 2017/2020 Mg II paper and three later papers; Van Eck (the 2023
  RMTable author) is a co-author. Seshadri is not an author.
- Burman, Sharma, Malik, Singh, arXiv:2405.09623 (2024; VERIFIED: arXiv abs page): radial profile of B from 59 single-Mg II
  sightlines, excess RRM dispersion falling with impact parameter (2.39 versus 1.67 microgauss inside and outside 50 kpc).
- Heesen, O'Sullivan, Brueggen, Basu et al., arXiv:2302.06617 (2023; VERIFIED: arXiv abs page): the 2461 LoTSS DR2 residual RMs
  around 183 nearby galaxies (galaxy-selected, not Mg II), no general excess at small impact parameter.
- Boeckmann, Brueggen, Heesen et al., A&A 678, A56 (2023), arXiv:2308.11391 (VERIFIED: arXiv abs page): MIGHTEE-POL RMs around
  foreground star-forming galaxies, 2.5 sigma |RM| excess at z ~ 0.46.
- Not found: a POSSUM-based or LoTSS-DR2-based Mg II absorber analysis. Those are the only gaps, and the Malik/O'Sullivan team
  (with POSSUM and SPICE-RACS members) is the obvious group to do them next, so the gap is not safe for an outsider.
What is still usable: Deepnil can tell Seshadri he has read the 2026 SPICE-RACS paper by his former collaborator, and offer
pipeline help if Seshadri's group wants a piece of it (for example the redshift evolution of the excess, or DESI DR2 absorbers).
That has to come from Seshadri, not from Deepnil.

## 5. How to approach him

1. After a lecture or in office hours, ask for the reading project (section 3). One sentence.
2. Mention that you have read his 2017 magnetogenesis paper and ask the section 4.1 question (as a question about his paper, not as a new idea). Let him react; do not pitch a big
   project in the first conversation.
3. Follow up by email with a one-page note: the reading plan, the 4.1 question written out in four lines, and a line saying you
   have Gaia and survey-data pipelines if a data project would be useful (options 4.2 or 4.3).

## 6. Still to do (for the next session)

- Publication list done 2026-11-17 from INSPIRE and arXiv (section 2A); an ADS cross-check is still worth doing.
- Prior-art search for 4.3 done 2026-11-17: OCCUPIED (arXiv:2605.16924). 4.2 done: APPARENTLY OPEN for streams and strong
  lensing (INSPIRE only); repeat the search on ADS full text and read 2501.06299 and 2112.03293 before proposing it.
- Journal volume for arXiv:2209.01509 (Ekta Sharma et al., MNRAS) and the ApJ 890 article number for arXiv:1710.10396 still
  unchecked; get them from ADS or the journal page before citing.
- 4.1 checked against 1708.08119 on 2026-11-17 (see 4.1). Remaining: read 2012.14720 in full before raising the slope question.
