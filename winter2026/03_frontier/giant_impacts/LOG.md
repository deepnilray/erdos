# Giant-impact afterglow hunt: log

## 2026-11-20, evening (Claude): automated vetting (vet2) built and validated; far search on track
Verdict: every candidate now gets the full manual checklist automatically (vet2/vet2.py, workflow giant_impacts_vet2.yml, results on
branch impacts-vet2). On the near list it reproduces every manual result: controls pass (ASASSN-21qj survives and is found in
SIMBAD, field z 57; J060000 survives with its 0.35 mag optical dip recovered; V836 Tau flagged young), candidate 1 survives with no
flags (field z 34.3, centroid jump 1.6 sigma, no SIMBAD object, about 1040 K), candidate 2 is flagged "not plain dust". VERIFIED
(runs 44763410479 near, 44763412267 far, 44762497568 list).
Worst news first:
- Gaia DR3 246657089893122176, the strongest uncatalogued warm-dust star in the previous entry, is KILLED as a blend: a Gaia
  neighbour 4.0" away only 2.88 mag fainter.
- Candidate 1's optical check is inconclusive rather than clean: two ASAS-SN cameras give -0.05 to -0.06 mag (brighter) after the
  2018 onset, one gives +0.014, with only one 120-day bin before onset in the g cameras.
- Four of the five uncatalogued warm-dust stars survive with Class II-like colours (likely uncatalogued young stars with disks).
Far search: 154,980 of 3,303,107 scored at 16:10 UTC (about 39,000 per hour); expected to finish around 24 November. After every
far run the workflow now dispatches vet2 on the far list, so new candidates are vetted within hours of being scored.
Next: wait for the far run; read impacts-vet2/far/vet2_report.md after each run; spectra for candidate 1 and the four survivors.

## 2026-11-20, afternoon (Claude): blind spot fixed, completeness measured, far search running
Verdict: the excess-plus-variability detector (for events that began before 2014) now runs on the whole near pool and recovers
three known dusty systems blindly (NGC 2547-ID8 as the planted control, plus V488 Per (the most extreme known debris disk) and the RZ Psc system (a known dusty young star),
found without being told). It flags 37 stars: 16 are known young stars (SIMBAD TT*/Or*/Y*O), 2 are cataclysmic variables (AE Aqr,
V426 Oph) and 14 have NO SIMBAD entry within 5 arcsec. Several of those 14 have strong warm-dust colours in AllWISE 2010.
CANDIDATES, not discoveries: most likely uncatalogued young stars with disks (Class II colours: W1-W2 > 0.25 and W2-W3 > 1), a few
possibly extreme debris disks. Age (lithium, H-alpha) decides.

- Completeness (subagent, completeness/README.md, commit 3098e2c): 0 false positives in 1,723 real light curves (95% upper limit
  0.17% per star); 50%/90% recovery at 0.137/0.204 mag (step), 0.144/0.239 (ramp), 0.196/0.434 (3-yr decay); blind for onsets
  before the third visit (about the first 12-15 months) and in the last year. ASASSN-21qj control re-scored at 38.04. VERIFIED.
- Far search (250-500 pc, 3,303,105 stars, branches impacts-far-*): IRSA's async queue stalled (about 360 stars per shard in two
  hours); hunt.py now uses synchronous upload joins first (commit fa1a1e0) and the run was restarted; it then scored about
  2,000 stars per shard in 8 minutes. ETA a few days.
- Blind-spot detector on the near pool: 111 stars with W1-W2 excess > 0.10 mag and z > 5; 37 also vary (visit jitter > 3x the
  median for their W2). Control: ID8 excess 0.418, z 40, jitter ratio 10.2, recovered. SIMBAD via the IDIA mirror (CDS down;
  control ASASSN-21qj found). Files: blindspot/d2_excess_variability_near.csv, d2_vetted.csv, unknown14.csv.
  Strongest uncatalogued warm-dust stars (AllWISE 2010 colours; Gaia GSP-Phot Teff/log g):
  Gaia DR3 246657089893122176 (RA 58.83, Dec +47.35, 212 pc, K dwarf 4800 K, W1-W2 0.70, W2-W3 1.12, NEOWISE jitter 12x);
  Gaia DR3 1768914166695591296 (327.56, +14.12, 110 pc, K7 4200 K, W1-W2 0.44, W2-W3 1.07, jitter 6.6x);
  Gaia DR3 5628404318169472 (43.55, +5.88, 232 pc, K 4500 K, W1-W2 0.39, W2-W3 1.57, D1 score 4.35);
  Gaia DR3 6505057483979425024 (339.60, -56.07, 185 pc, M0 3650 K, W1-W2 0.43, W2-W3 1.92);
  Gaia DR3 1858978638770086016 (311.02, +29.66, 223 pc, log g 3.8, W1-W2 0.51, W3-W4 1.90; Cygnus direction).
  Mundane explanations still open for each: uncatalogued YSO, background galaxy or nebula in the WISE beam (ext_flg = 1 for some),
  blends. Next: light curves and field controls for these five, Gaia H-alpha and cluster membership, then spectra.

## 2026-11-20 — Catalog and publication audit

**Verdict: CANDIDATE for all three field infrared events. OCCUPIED for the ASASSN-21qj infrared event and for J060000's optical fade.**

- **VERIFIED — The catalog control fired.** The original Python script stops during SIMBAD setup because Strasbourg TAP capabilities returned HTTP 404. The same 20-arcsec cones run through the IDIA SIMBAD TAP mirror returned ASASSN-21qj at 0.12 arcsec. The Harvard VizieR all-catalog 5-arcsec cones returned the control's VSX record at 0.12 arcsec and its AllWISE record at 0.81 arcsec. All four VizieR responses include backend errors alongside usable rows, so catalog coverage remains incomplete.
- **CANDIDATE — 5808318474663998464, ambiguous.** VERIFIED by the prior run's 79-star comparison and centroid checks. The optical brightening in three ASAS-SN cameras accompanies the 2021 infrared rise. VSX records ROT (G range 0.060 mag), and TESS shows ~4-day modulation. VERIFIED youth and activity flags include UPK 612 / Theia 216 membership, GALAH lithium, rotation and an eROSITA counterpart. CONJECTURED activity or a companion contributes to the signal. No mundane cause has been established.
- **CANDIDATE — J060000's 2020 infrared brightening. OCCUPIED — its 2019 optical fade.** VERIFIED in the previous run against 75 neighboring stars and a stable centroid. SIMBAD's primary type is `EB?`, a possible eclipsing binary, and VSX has `DIP:`, an uncertain dipper classification. The binary interpretation remains CONJECTURED. Way et al. report the optical decline in [ATel 13346](https://www.astronomerstelegram.org/?read=13346). The [ASASSN-24fw paper](https://arxiv.org/abs/2507.03080) includes J060000 in its introduction, Table 6 and the Gaia/WISE comparison in Figure 12. Those sections cover its optical occultation and broad-band colors. The NEOWISE time series in that paper concerns ASASSN-24fw.
- **CANDIDATE — 5792808347020475136, strongest remaining lead.** VERIFIED in the prior run against 135 neighboring stars, with stable centroid and 2018–2024 infrared light curve. The prior ASAS-SN and TESS pixel checks place ~3% limits on the tested optical dimming and dips. VSX records ROT (G range 0.030 mag). No report of the 2018 infrared step appeared in the ADS full-text query below. Spectroscopic age, activity and multiplicity remain open.
- **OCCUPIED — ASASSN-21qj.** VERIFIED positive literature control. Kenworthy et al., *Nature* 622, 251–254 (2023), report the sustained W1/W2 rise years before the optical eclipse. Marshall et al. independently analyze the NEOWISE excess. VSX gives `NL/VY:`, an uncertain catalog classification. [Kenworthy et al. primary paper](https://arxiv.org/abs/2310.08360), [Marshall et al. primary paper](https://arxiv.org/abs/2309.16969)

**Exact next step.** Obtain a spectrum of 5792808347020475136 covering Li I 6708 Å and H-alpha, with a radial velocity measurement and a second epoch to test for a close companion. For 5808318474663998464, inspect the existing GALAH spectrum and compare repeated velocities and activity indicators against the optical and infrared time series. For J060000, retrieve the archival SPHERE epochs and review its NEOWISE images and photometry with a supervisor before drafting any note. Repeat the VizieR cones on a backend that returns each catalog successfully.

### Catalog evidence

VERIFIED from [IDIA SIMBAD TAP](https://simbad.idia.ac.za/simbad/sim-tap/capabilities) (`basic`, `otypes`, `has_ref` joined to `ref`) and the Harvard [VizieR VSX table](https://vizier.cfa.harvard.edu/viz-bin/VizieR?-source=B/vsx/vsx). The bibliography counts are the IDIA cone snapshot, and equal the number of linked bibcodes returned. Harvard Sesame independently recovered the control and gave 8 references for Candidate 2, compared with 7 at IDIA. No bibcode list was available through the Harvard resolver.

| Target | All SIMBAD objects within 20 arcsec | Primary and all reported object types | References | VSX within 5 arcsec |
|---|---|---|---:|---|
| 5792808347020475136 | Zero objects | — | — | ROT, 0.42 arcsec |
| 5808318474663998464 | TYC 9279-457-1, 0.27 arcsec | `*`; `*`, `NIR` | 7 | ROT, 0.27 arcsec |
| J060000 | ASASSN-V J060000.76-310027.8, 0.37 arcsec | `EB?`; `*`, `EB?`, `MIR`, `NIR`, `V*` | 12 | DIP:, 0.42 arcsec |
| ASASSN-21qj | 2MASS J08152329-3859234, 0.12 arcsec | `*`; `*`, `NIR` | 10 | NL/VY:, 0.12 arcsec |
| ASASSN-21qj field neighbor | 2MASS J08152298-3859244, 3.74 arcsec | `*`; `*`, `NIR` | 1 | No VSX row for this neighbor |

`*` denotes star, `NIR`/ `MIR` near-/mid-infrared source, `V*` variable star, and `EB?` eclipsing-binary candidate. Wavelength source types describe catalog associations. Evidence for excess or a companion comes from the underlying measurements.

VERIFIED via ESA Gaia DR3 TAP. RUWE in the order above is 1.0216, 1.0291, 1.0187 and 1.1036, all `non_single_star=0`. Queries by source ID returned zero rows in each of `nss_two_body_orbit`, `nss_acceleration_astro`, `nss_non_linear_spectro` and `nss_vim_fl`. An unrestricted one-row query returned a source from each table. Close companions remain possible. [Gaia Archive](https://gea.esac.esa.int/archive/)

### VizieR 5-arcsec matches

VERIFIED from the Harvard mirror with `/viz-bin/votable`, `-c=<RA Dec>`, `-c.rs=5`, `-out.max=unlimited`, `-out.add=_r` and no source filter. The structurally complete XML responses contain 39, 95, 66 and 41 nonempty tables for Candidate 1, Candidate 2, J060000 and ASASSN-21qj, respectively. The service reported examining 141, 139, 117 and 106 potential catalogs. All four report an unavailable ADQL backend, and the Candidate 2 and J060000 responses also report database connection errors, so a missing hit cannot clear a catalog category. The all-catalog control recovered ASASSN-21qj and the independent VSX query returned the same object. These are positional rows, which can include neighbors or repeated measurements.

<details>
<summary>Every nonempty VizieR table returned</summary>

- **Candidate 1** (39 tables). `I/243/out`, `I/254/out`, `I/255/out`, `I/284/out` (2 rows), `I/297/out` (2 rows), `I/305/out`, `I/312/sample`, `I/317/sample`, `I/320/spm4`, `I/322A/out`, `I/340/ucac5`, `I/347/gaia2dis`, `I/352/gedr3dis`, `I/355/gaiadr3`, `I/355/paramsup`, `I/355/epphot` (49 rows), `I/355/xpsummary`, `I/355/xpsample` (343 rows), `I/355/xpcont`, `I/358/varisum`, `I/358/vclassre`, `I/363/gaia_rv_dr3`, `II/246/out`, `II/328/allwise`, `IV/39/tic82`, `V/160/shboost`, `VI/42/out`, `B/denis/denis`, `B/vsx/vsx`, `J/ApJ/925/164/catalog`, `J/ApJ/984/58/table1`, `J/A+A/674/A25/vspursig`, `J/A+A/684/A29/extend`, `J/A+A/692/A115/pristine_ca`, `J/A+A/692/A115/pristine_gaia`, `J/A+A/695/A75/catalog`, `J/AJ/158/93/table2`, `J/AJ/159/84/table2`, `J/MNRAS/479/111/snsurvey`.
- **Candidate 2** (95 tables). `I/197A/tic`, `I/243/out`, `I/252/out`, `I/254/out` (2 rows), `I/255/out` (2 rows), `I/259/tyc2`, `I/275/ac2002`, `I/280B/ascc`, `I/284/out`, `I/297/out`, `I/305/out`, `I/312/sample`, `I/317/sample`, `I/319/xpm`, `I/320/spm4`, `I/322A/out`, `I/337/tgas`, `I/337/tgasptyc`, `I/340/ucac5`, `I/347/gaia2dis`, `I/350/tyc2tdsc`, `I/352/gedr3dis`, `I/355/gaiadr3`, `I/355/paramsup`, `I/355/epphot` (69 rows), `I/355/xpsummary`, `I/355/xpsample` (343 rows), `I/355/xpcont`, `I/358/varisum`, `I/358/vclassre`, `I/363/gaia_rv_dr3`, `II/246/out`, `II/328/allwise`, `II/336/apass9`, `II/354/tgasext`, `IV/39/tic82`, `V/136/tycall`, `V/160/shboost`, `VI/42/out`, `VI/135/table15`, `B/denis/denis`, `B/vsx/vsx`, `J/ApJ/833/119/distall`, `J/ApJ/833/119/distallw`, `J/ApJ/925/164/catalog`, `J/ApJ/935/90/table1`, `J/ApJ/961/113/table1`, `J/ApJ/984/58/table1`, `J/ApJS/265/12/table3`, `J/ApJS/276/57/table5`, `J/ApJS/281/52/table1`, `J/A+A/633/A99/members`, `J/A+A/640/A1/nodup`, `J/A+A/653/A98/aspic1_1`, `J/A+A/659/A59/table2`, `J/A+A/674/A22/catalog`, `J/A+A/674/A25/vspursig`, `J/A+A/675/A68/members`, `J/A+A/678/A75/tablec1`, `J/A+A/684/A29/extend`, `J/A+A/685/A59/catalog`, `J/A+A/686/A42/members`, `J/A+A/689/A18/members`, `J/A+A/691/A28/members`, `J/A+A/692/A115/pristine_ca`, `J/A+A/692/A115/pristine_gaia`, `J/A+A/692/A150/allskytg`, `J/A+A/695/A75/catalog`, `J/A+A/698/A295/tablea1`, `J/A+A/703/A104/catalog`, `J/A+A/704/A50/sources`, `J/A+A/706/A62/tablef2`, `J/A+A/711/A54/table1`, `J/A+A/711/A215/tableb2`, `J/A+A/712/A171/erass3-m`, `J/A+A/712/A171/dr2mc`, `J/A+A/712/A171/dr2mg`, `J/A+A/712/A171/dr2ml`, `J/AJ/154/259/table6`, `J/AJ/156/102/table9`, `J/AJ/158/93/table2`, `J/AJ/158/122/table1`, `J/AJ/159/84/table2`, `J/AJ/160/279/table1`, `J/AJ/164/137/table1`, `J/AJ/167/210/table1`, `J/AJ/170/288/table4`, `J/MNRAS/463/4210/ucac4rpm`, `J/MNRAS/471/770/table1`, `J/MNRAS/486/251/tablea1`, `J/MNRAS/503/3279/table1`, `J/MNRAS/522/29/table2`, `J/MNRAS/529/1802/targets`, `J/other/PASA/42.51/allstar`, `J/other/PASA/42.51/allspec`.
- **J060000** (66 tables). `I/243/out`, `I/252/out`, `I/254/out`, `I/255/out`, `I/284/out`, `I/297/out`, `I/305/out`, `I/312/sample`, `I/317/sample`, `I/319/xpm`, `I/320/spm4`, `I/322A/out`, `I/327/cmc15`, `I/340/ucac5`, `I/347/gaia2dis`, `I/348/catalog`, `I/352/gedr3dis`, `I/355/gaiadr3`, `I/355/paramsup`, `I/355/epphot` (50 rows), `I/355/rvsmean` (2401 rows), `I/355/xpsummary`, `I/355/xpsample` (343 rows), `I/355/xpcont`, `I/358/varisum`, `I/358/vclassre`, `I/363/gaia_rv_dr3`, `II/246/out`, `II/287/skydot` (2 rows), `II/328/allwise`, `II/336/apass9` (2 rows), `II/391/ks4dr1` (2 rows), `IV/39/tic82`, `V/160/shboost`, `VI/42/out`, `B/denis/denis`, `B/eso/eso_arc` (110 rows), `B/vsx/vsx`, `J/ApJ/925/164/catalog`, `J/ApJ/984/58/table1`, `J/ApJ/984/58/table2`, `J/ApJS/264/41/catalog`, `J/A+A/638/A76/galah`, `J/A+A/659/A95/sos`, `J/A+A/659/A95/galah`, `J/A+A/673/A155/galahdr3`, `J/A+A/674/A25/vspursig`, `J/A+A/684/A29/extend`, `J/A+A/685/A59/catalog`, `J/A+A/690/A54/g2a`, `J/A+A/692/A115/pristine_ca`, `J/A+A/692/A115/pristine_gaia`, `J/A+A/703/A104/catalog`, `J/AJ/158/93/table2`, `J/AJ/159/84/table2`, `J/MNRAS/463/4210/ucac4rpm`, `J/MNRAS/478/4513/catalog`, `J/MNRAS/500/4849/emigalah`, `J/MNRAS/506/150/stars`, `J/MNRAS/506/150/spect`, `J/MNRAS/508/4202/table1`, `J/MNRAS/513/420/ngtsrot`, `J/MNRAS/522/29/table2`, `J/MNRAS/529/1802/targets`, `J/other/PASA/42.51/allstar`, `J/other/PASA/42.51/allspec`.
- **ASASSN-21qj** (41 tables). `I/243/out`, `I/252/out`, `I/254/out`, `I/255/out`, `I/284/out`, `I/297/out` (2 rows), `I/305/out`, `I/312/sample`, `I/317/sample`, `I/319/xpm`, `I/320/spm4`, `I/322A/out`, `I/327/cmc15`, `I/340/ucac5`, `I/347/gaia2dis` (2 rows), `I/352/gedr3dis` (2 rows), `I/355/gaiadr3` (2 rows), `I/355/paramsup` (2 rows), `I/355/xpsummary` (2 rows), `I/355/xpsample` (343 rows), `I/355/xpcont` (2 rows), `I/363/gaia_rv_dr3`, `II/246/out` (2 rows), `II/328/allwise`, `II/336/apass9`, `II/374/table2` (2 rows), `II/380/splusdr4`, `II/386/vphasplus32` (9 rows), `IV/35/wn18_b10`, `IV/39/tic82` (2 rows), `V/160/shboost` (2 rows), `VI/42/out`, `B/denis/denis`, `B/vsx/vsx`, `J/ApJ/984/58/table1` (2 rows), `J/A+A/691/A242/tessobaf`, `J/A+A/692/A115/pristine_ca` (2 rows), `J/AJ/158/93/table2`, `J/AJ/159/84/table2`, `J/MNRAS/463/4210/ucac4rpm`, `J/MNRAS/522/29/table2`.

</details>

- **VERIFIED — Candidate 2 youth and activity.** The exact Gaia ID appears in the UPK 612 member table with probability 0.929 in Hunt & Reffert and 1.00 in van Groeningen et al. Vach et al. list the same TIC 364217279 as Theia 216, age 97 Myr and rotation period 4.2 d. GALAH DR4 reports [Li/Fe] = +1.457 ± 0.079 dex (flag 0). Carrasco et al. report H-alpha EW −0.226 ± 0.123 nm and no relative emission flag. The eROSITA source 3eRASS J164851.6-692505 sits 2.17 arcsec away and its published Gaia counterpart table names the exact Gaia DR3 ID. Gao et al. classify the same TIC as ROT, period 4.161855 d. The inspected Tu and Wang flare tables give zero flares for this TIC. [Membership data](https://vizier.cfa.harvard.edu/viz-bin/VizieR?-source=J/A%2BA/686/A42/members), [Vach et al.](https://doi.org/10.3847/1538-3881/ad3108), [GALAH DR4 data](https://vizier.cfa.harvard.edu/viz-bin/VizieR?-source=J/other/PASA/42.51/allstar), [eROSITA counterpart data](https://vizier.cfa.harvard.edu/viz-bin/VizieR?-source=J/A%2BA/712/A171/dr2mg), [TESS classification data](https://vizier.cfa.harvard.edu/viz-bin/VizieR?-source=J/ApJS/276/57/table5)
- **VERIFIED — Candidate 2 infrared and binary flags.** McDonald et al.'s pre-event SED row has a mean mid-IR observed/model ratio of 1.018 and catalog significance statistic 1.037. The Zerjal et al. cluster photometry gives W1−W2 = −0.046 and W2−W3 = −0.019 mag, and lists W4 = 8.910. The direct AllWISE query gives W4 quality U, S/N 0.4 and no magnitude error, so 8.910 is an upper limit on flux. The Tycho double-star cross-index row has blank system and separation columns. The Green et al. ellipsoidal-search table has score 0 for Candidate 2, J060000 and the control. [McDonald et al. catalog](https://cdsarc.cds.unistra.fr/viz-bin/ReadMe/J/MNRAS/471/770?format=html), [Zerjal et al.](https://arxiv.org/abs/2309.10862), [Tycho catalog data](https://vizier.cfa.harvard.edu/viz-bin/VizieR?-source=I/350/tyc2tdsc), [Green et al. catalog data](https://vizier.cfa.harvard.edu/viz-bin/VizieR?-source=J/MNRAS/522/29/table2)
- **VERIFIED — J060000 spectroscopy and variability flags.** GALAH DR4 reports [Li/Fe] = +0.307 ± 0.048 dex (flag 0). The GALAH emission-line catalog returns an H-alpha residual equivalent width of +0.109 Å. The NGTS rotation catalog gives 6.59927 d. Swift treated the UV measurements as upper limits and reports an X-ray upper limit. These records leave the star's age and the cause of its infrared rise open. [GALAH DR4 data](https://vizier.cfa.harvard.edu/viz-bin/VizieR?-source=J/other/PASA/42.51/allstar), [Emission-line data](https://vizier.cfa.harvard.edu/viz-bin/VizieR?-source=J/MNRAS/500/4849/emigalah), [NGTS data](https://vizier.cfa.harvard.edu/viz-bin/VizieR?-source=J/MNRAS/513/420/ngtsrot), [Swift report](https://www.astronomerstelegram.org/?read=13377)
- **VERIFIED — Candidate 1 and control flags.** The retrieved Candidate 1 rows contain optical variability and static IR photometry. No matched row in this response identifies a YSO, T Tauri star, young association member, lithium detection, UV/X-ray counterpart, disk or binary. The ASASSN-21qj TESS OBAF binary-search row has classifier score 0. The primary papers report the control's warm infrared excess. [TESS binary-search data](https://vizier.cfa.harvard.edu/viz-bin/VizieR?-source=J/A%2BA/691/A242/tessobaf), [Kenworthy et al.](https://arxiv.org/abs/2310.08360)

### SIMBAD bibliography review

VERIFIED from the IDIA TAP bibliography links for these exact object OIDs. Primary article text, primary ATels, author manuscripts or their released tables were checked for the target result.

- **Candidate 1 (zero SIMBAD objects in the cone).** The control recovered as above. The linked-bibliography check had no object to expand.
- **Candidate 2 (7 references).** [2019AJ....158..122K](https://doi.org/10.3847/1538-3881/ab339a), [2020A&A...633A..99C](https://arxiv.org/abs/1911.07075), [2020A&A...640A...1C](https://arxiv.org/abs/2004.07274), [2021MNRAS.503.3279S](https://arxiv.org/abs/2011.02533), and [2023ApJS..265...12Q](https://arxiv.org/abs/2212.11034) cover Galactic structure, open-cluster membership or spectroscopy. [2023A&A...678A..75Z](https://arxiv.org/abs/2309.10862) provides static multiband photometry in the associated machine-readable table. [2024AJ....167..210V](https://doi.org/10.3847/1538-3881/ad3108) gives the TESS population and rotation information. None of these seven sources reports the 2020–2021 W2 step in the target.
- **J060000 (12 references).** [2018MNRAS.478.4513B](https://arxiv.org/abs/1804.06041) and [2021MNRAS.506..150B](https://arxiv.org/abs/2011.02505) are GALAH spectroscopic releases. [2019ATel13346....1W](https://www.astronomerstelegram.org/?read=13346), [2019ATel13349....1B](https://www.astronomerstelegram.org/?read=13349), [2019ATel13357....1W](https://www.astronomerstelegram.org/?read=13357), [2019ATel13361....1M](https://www.astronomerstelegram.org/?read=13361), [2019ATel13377....1S](https://www.astronomerstelegram.org/?read=13377), and [2020ATel13450....1S](https://www.astronomerstelegram.org/?read=13450) cover optical fading, spectroscopy, archival SED, Swift limits or earlier optical history. [2021A&A...648A..15K](https://wrap.warwick.ac.uk/id/eprint/151792/7/WRAP-The-B-pictoris-b-hill-sphere-transit-campaign-2021.pdf) mentions J0600 as an eclipse comparison. [2021ApJS..257...42L](https://doi.org/10.3847/1538-4365/ac168a) and [2022MNRAS.514..200W](https://arxiv.org/abs/2109.07586) cite the optical event. [2022A&A...667A.114J](https://arxiv.org/abs/2204.11746) lists the target in the SPHERE adaptive-optics performance sample under 2MASS J06000075-3100276. Its Table A.1 uses archival Gaia and 2MASS magnitudes. None of the 12 reports the 2020 NEOWISE rise.
- **ASASSN-21qj (10 references).** [2023Natur.622..251K](https://doi.org/10.1038/s41586-023-06573-9) and [2023ApJ...954..140M](https://doi.org/10.3847/1538-4357/ace629) analyze the infrared event. [2025ApJ...991..118T](https://doi.org/10.3847/1538-4357/adf5bb) and [2026ApJ..1000L...5T](https://doi.org/10.3847/2041-8213/ae3ddc) discuss the precedent. [2021ATel14879....1R](https://www.astronomerstelegram.org/?read=14879), [2021ATel14900....1B](https://www.astronomerstelegram.org/?read=14900), and [2022ATel15531....1R](https://www.astronomerstelegram.org/?read=15531) cover optical fading and follow-up. [2022RNAAS...6..232J](https://doi.org/10.3847/2515-5172/aca096), [2025AJ....170...95G](https://doi.org/10.3847/1538-3881/ade4bb) and [2026A&A...707A..58H](https://arxiv.org/abs/2512.15636) cite it in other contexts. The neighbor has one linked paper, Kenworthy et al., which resolves it as a visual neighbor 3.738 arcsec from the target, with discrepant parallax and proper motion. The published infrared event belongs to ASASSN-21qj.

### ADS full-text searches

VERIFIED in the browser. ADS redirected to its SciX search interface. These are full-text queries and returned counts, with the published paper recovered by the control name.

| Target | Exact query | Results |
|---|---|---|
| 5792808347020475136 | `full:(("5792808347020475136" OR "J144351.92-761145.9") OR ("220.96632" AND "-76.19612")) AND full:(WISE OR NEOWISE OR infrared)` | 0 |
| 5808318474663998464 | `full:(("5808318474663998464" OR "J164851.45-692507.0" OR "TYC 9279-457-1") OR ("252.21435" AND "-69.41863")) AND full:(WISE OR NEOWISE OR infrared)` | 0 |
| J060000 | `full:(("J060000" OR "J0600-31" OR "2891196718939580672") OR ("90.00308" AND "-31.00781")) AND full:(WISE OR NEOWISE OR infrared)` | 6 |
| J060000 exact aliases | `full:("J060000.76-310027.83" OR "J060000.75-310027.9" OR "J06000075-3100278") AND full:(WISE OR NEOWISE OR infrared)` | 5, dropping the MeerKAT paper |
| Candidate 1 additional aliases | `full:("14435201-7611457" OR "402328069") AND full:(WISE OR NEOWISE OR infrared)` | 0 |
| Candidate 2 additional aliases | `full:("16485149-6925069" OR "364217279" OR "3eRASS J164851.6-692505" OR "210324003201117") AND full:(WISE OR NEOWISE OR infrared)` | 0 |
| J060000 additional aliases | `full:("06000075-3100276" OR "143169638" OR "NG0603-3056_27496" OR "170205003401143" OR "J060000.74-310027.9") AND full:(WISE OR NEOWISE OR infrared)` | 0 |
| J060000 broad prefix check | `full:("06000075-3100276" OR "143169638" OR "NG0603-3056_27496" OR "170205003401143" OR "J060000.74-310027.9" OR "J0600") AND full:(WISE OR NEOWISE OR infrared)` | 36. First page dominated by unrelated coordinate prefixes, e.g. MACS J0600.1−2008. |
| ASASSN-21qj name | `full:"ASASSN-21qj" AND full:(WISE OR NEOWISE OR infrared)` | 25, including Kenworthy et al. |
| ASASSN-21qj aliases | `full:("J08152329-3859234" OR "5539970601632026752") AND full:(WISE OR NEOWISE OR infrared)` | 2, Kenworthy et al. and Marshall et al. |
| ASASSN-21qj coordinates | `full:(("123.847042" AND "-38.989833")) AND full:(WISE OR NEOWISE OR infrared)` | 0 despite the published event. Exact decimal-coordinate strings have limited recall. |

Separate SciX object-index probes returned 0 for `object:"TYC 9279-457-1"`, 0 for `object:"Gaia DR3 2891196718939580672"`, 1 for `object:"ASASSN-V J060000.76-310027.8"` (ATel 13357, optical) and 12 for `object:"ASASSN-21qj"`. The TAP bibliography above is the source of the SIMBAD counts.

VERIFIED review of the six J060000 results and the additional historical ATel.

- [ASASSN-24fw](https://arxiv.org/abs/2507.03080) discusses the ~580-day optical event and includes a WISE color comparison, as noted above.
- [Way et al. on ASASSN-V J192114.84+624950.8](https://arxiv.org/abs/2109.07586) cites J060000 as an optical dimmer in its introduction. Its binary measurements are for J192114.
- [MeerKAT Galaxy Cluster Legacy Survey I](https://arxiv.org/abs/2111.05673) yielded a text-search hit. The target name and Gaia ID did not occur in the downloaded paper text. Its similarly prefixed sources have different declinations.
- [Breakthrough Listen Exotica Catalog](https://arxiv.org/abs/2006.11304) lists J060000 as entry 699 and cites the optical alert for inclusion. It describes fading and brightening episodes without reporting a WISE/NEOWISE time series for the target.
- [AAVSO Alert Notice 691](https://www.aavso.org/aavso-alert-notice-691) requests optical monitoring and cites the pre-event SED for the infrared assessment.
- [McCollum & Laine, ATel 13361](https://www.astronomerstelegram.org/?read=13361) finds no excess in archival photometry acquired through about 2016. It precedes the first bright NEOWISE visit in February 2020.
- [Schaefer, ATel 13450](https://www.astronomerstelegram.org/?read=13450) discusses the possible 1937 optical dip and the chromatic 2019–2020 optical dips. No NEOWISE brightening is reported.

## 2026-11-20, later (Claude, interactive): follow-up of the two new candidates
Verdict: candidate 1 (Gaia DR3 5792808347020475136) still looks like a clean sudden-dust event and survives every check that
could be run; candidate 2 (Gaia DR3 5808318474663998464) is now ambiguous, because it brightened in the optical too. Neither is a
discovery: SIMBAD could not be queried (CDS returns "Page unavailable" from both this sandbox and GitHub Actions on 2026-11-20).

- VSX (via the VizieR mirror at vizier.cfa.harvard.edu, B/vsx/vsx): both are listed only as Gaia DR3 rotational variables
  ("ROT", G range 0.03-0.06 mag), entries imported from the Gaia DR3 classifier; no infrared event is recorded. J060000 is listed as
  ASASSN-V J060000.76-310027.8, type "DIP:" (control: the lookup finds the known object).
- ASAS-SN Sky Patrol optical light curves (workflow giant_impacts_followup.yml, branch impacts-followup). Controls fired: the
  pipeline shows ASASSN-21qj's 2021 dimming (1.2 mag) and J060000's 2019 dip (0.4 mag in 60-day medians).
  Candidate 1: an apparent 0.6 mag "dimming" was traced to a constant zero-point offset of one camera (bF); per-camera normalised,
  cameras bF and bj stay flat within about 0.02-0.03 mag in every season 2018-2024; camera bn alone shows erratic offsets (up to
  0.2 mag late in 2024) that the other two do not, so camera-specific. Conclusion: no optical dimming above about 3% accompanies the
  46% W2 brightening. ASASSN-21qj also showed no optical change for its first 2.5 years of infrared brightening.
  Candidate 2: all three g-band cameras agree that the star got BRIGHTER in the optical by 0.02-0.04 mag from the first season after
  the infrared onset, and kept brightening to 0.05-0.09 mag by 2024, while the infrared excess decayed. The extra light is roughly
  flat in F_nu from g to W2 (about 1.3, 1.9, 1.9 mJy in g, W1, W2), which a single warm-dust blackbody cannot produce. Possible:
  a stellar activity change (its TESS spot amplitude grew from about 0.5% in 2019 to 1-2% in 2021) plus something else, or an
  unresolved companion or background source. Downgraded: probably not a simple impact afterglow (CONJECTURED).
- TESS pixel photometry for candidate 1 (TESScut 11x11, 3x3 aperture, background subtracted; sectors 12, 38, 39): only smooth
  few-percent trends that follow the spacecraft orbits and background; no transit-like dips deeper than about 3% on hour-to-day
  scales. The 10% "dip" in the QLP sector-39 curve does not appear and was a QLP systematic.

Next: SIMBAD when CDS is back; Gaia DR4 (2026-12-02) photometry and astrometry for candidate 1 (covers the 2018 onset); a spectrum of
candidate 1 (lithium for age, H-alpha, radial velocity for a companion); a short note on J060000 and candidate 1 with a supervisor.

## 2026-11-20 (Claude, interactive): HUNT COMPLETE. Two new candidates with no literature found.
Verdict: the full pool has been scored (699,341 entries, 611,091 with a usable NEOWISE light curve; run 44267373293 finished
2026-11-18, REMAINING = 0 in all four shards). Above the candidate cuts: ASASSN-21qj (validation, 38.0), J060000 (8.9, OCCUPIED as
an object, see below) and TWO NEW field stars, both with sudden, sustained, reddening mid-IR brightening and nothing found on them in
a web search. They are CANDIDATES: SIMBAD/VSX (CDS) still unreachable, so the literature gate is not passed.

1. uid 683344 = Gaia DR3 5792808347020475136 = AllWISE J144351.92-761145.9. RA 220.96632, Dec -76.19612. G 13.52, BP-RP 1.29,
   parallax 4.04 mas (247 pc), RUWE 1.02, Gaia GSP-Phot Teff 4774 K, log g 4.58 (K dwarf), Gaia classifier SOLAR_LIKE (0.66).
   NEOWISE (VERIFIED, by eye: candidates/new_candidates_lc.png): flat for 9 visits 2014-2018 (W2 11.24-11.27); between 2018-02-21
   (MJD 58178) and 2018-08-12 (58342) W2 brightens by 0.41 mag and W1 by 0.21; W1-W2 goes from -0.06 to +0.15 and STAYS there:
   a plateau for six years to 2024 (W2 10.83-10.93). AllWISE 2010: W1-W2 -0.05, W2-W3 0.21 (W3 S/N about 10): no clear prior excess.
   Excess colour gives about 1100 K if one blackbody (range about 960-1240 K; CONJECTURED as physics).
   Checks passed: field control (135 stars within 12', W2 8.5-12.5, same epochs: median step -0.012, largest other 0.034, this star
   0.411; VERIFIED, control fired); centroid moves smoothly with proper motion, no jump at the step (< 0.03"), whereas the brightest
   neighbour (Gaia G 16.4 at 7.9") would pull it by about 1.7" if it were the source; W1 11.2 (unsaturated); PSF fits unchanged.
   Caution: W1 PSF reduced chi2 is about 3 in every visit (before and after), probably the 7.9" neighbour.
   TESS: QLP light curves exist for sectors 12 (2019), 38-39 (2021), 65-66 (2023), 93, 100-102; QLP SAP flux at G 13.5 is dominated
   by scattered-light systematics. A possible 10% dip in sector 39 (BTJD 2379-2382) is UNVERIFIED (likely systematics). Needs
   pixel-level photometry (TESScut, own aperture and background).
2. uid 637541 = Gaia DR3 5808318474663998464 = AllWISE J164851.45-692507.0. RA 252.21435, Dec -69.41863. G 11.92, BP-RP 0.89,
   parallax 4.16 mas (240 pc), RUWE 1.03, Teff 5513 K, log g 4.42, [M/H] -0.34 (G dwarf), classifier SOLAR_LIKE (0.72).
   NEOWISE: flat for 14 visits 2014-2020; between 2020-08-21 (MJD 59082) and 2021-03-13 (59286) W2 brightens 0.155 mag, W1 0.086,
   W1-W2 -0.04 to +0.03, then decays over three years (W2 10.22 to 10.31 by 2024). About 1300 K if one blackbody (1130-1550 K).
   Field control (79 stars within 12'): median step 0.016, largest other 0.068, this star 0.155 (VERIFIED). Centroid: no jump.
   Faint Gaia neighbour (G 18.1, 6 mag fainter) at 5.1"; it would have to brighten to W2 about 12.4 and would shift the centroid by
   about 0.65"; not seen.
   TESS SPOC/QLP: a spot-modulated light curve with period about 4 d, amplitude about 0.5% in 2019 (sector 12, before the IR event)
   and about 1-2% in 2021 (sector 39, two months after the IR onset) and later. A G dwarf rotating in about 4 days is either young
   (roughly 100 Myr scale, CONJECTURED from typical rotation-age relations, not computed) or tidally locked in a close binary
   (RUWE 1.03 argues mildly against a wide-separation companion, not against a close one). No obvious dips by eye.

Mundane explanations still open for both (worst first): (a) a background or companion source invisible to Gaia that brightened,
co-located within about 0.3"; (b) a young star whose disk changed (no YSO flag from Gaia, no prior excess, but age unknown);
(c) a known variable listed in SIMBAD/VSX (unchecked); (d) for 637541, magnetic activity cannot make the W1-W2 colour redder by
0.07 mag at fixed photosphere, so it is not obviously spots.

Exact next steps: SIMBAD/VSX from a CDS-reachable machine; TESScut pixel photometry for 683344 (sectors 12-102) and 637541;
ASAS-SN Sky Patrol optical light curves 2014-2026 for both (dimming at onset = transit of debris, the ASASSN-21qj signature); Gaia
DR4 epoch photometry on 2026-12-02 (covers 683344's 2018 onset); lithium/H-alpha spectrum to settle ages.

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
  visit of 2019-09-24 (MJD 58750) is still flat; the next, 2020-02-26 (MJD 58905), is brighter by dW2 = 0.161, dW1 = 0.055 mag;
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
