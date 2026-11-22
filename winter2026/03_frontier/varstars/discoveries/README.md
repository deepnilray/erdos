# Candidate new variable stars: not in any catalogue checked (2026-11-22)

Found by `period_search.py` in a 1.5-deg-radius region at RA 250, Dec +40 (high Galactic latitude), using ZTF DR24 public data.

Catalogues checked (all with 0 matches within 5"):
- VSX (B/vsx);
- GCVS;
- ZTF periodic variables (Chen+2020);
- ATLAS variables;
- ASAS-SN variables (II/366);
- Gaia DR3 variability classifications and `vari_summary`;
- Milliquas (VII/294, VII/290).

The VizieR copies were read from the CfA mirror and may lag the live VSX. **Search VSX by coordinates on aavso.org right before submitting.**

## A. Gaia DR3 1355639086191753216: periodic, rotational (most likely a spotted M dwarf)
| item | value |
|---|---|
| Position (Gaia DR3, ICRS) | RA 250.611524, Dec +39.423143 (16:42:26.77 +39:25:23.3) |
| Other IDs | ZTF DR24 oid 723207300001757 (r), 723107300006279 (g), 723307300002238 (i); AllWISE J164226.77+392522.9 |
| Gaia DR3 | G 16.77, BP-RP 2.89, Teff 3280 K, parallax 7.37 +- 0.04 mas (~136 pc), RUWE 1.01, no NSS solution |
| Period | **1.27476 d** (+- ~0.00005). Same period in g, r and i. Folding at 2P gives equal minima (17.409 vs 17.414 +- 0.003 r), so P is not doubled. |
| Range for VSX (binned mean curve) | r 17.29-17.42; g 18.76-18.90. Individual points (5-95 %): r 17.27-17.42, g 18.69-18.93, i 15.72-15.83 |
| Epoch of maximum | HJD 2458198.731 (r) |
| Coherence | stable phase and amplitude over 7.5 yr (2018-2025, ~2150 cycles) |
| Suggested VSX type | ROT (BY Dra-type spot modulation of an M dwarf). An ellipsoidal binary at 2P = 2.5495 d is less likely given RUWE 1.0 and equal minima. |
| Data | ZTF DR24 (Masci et al. 2019; Bellm et al. 2019), IRSA |
| Plot | A_GaiaDR3_1355639086191753216.png |

## B. Gaia DR3 1355878947229358336: irregular deep dips (classification open)
| item | value |
|---|---|
| Position (Gaia DR3) | RA 249.771625, Dec +39.850356 (16:39:05.19 +39:51:01.3) |
| Other IDs | ZTF DR24 oid 723208100006322 (r); AllWISE J163905.27+395100.9 |
| Gaia DR3 | G 19.59, BP-RP 1.21, parallax 0.27 +- 0.26 mas (distant), RUWE 0.96; DSC star probability 0.9995 |
| Behaviour | Baseline r ~19.2 (g ~20.2), with repeated dips of 1-2 mag lasting ~10-25 d, several per season, 2018-2025. Not strictly periodic: the LS peak is at 83 d, but dip spacing varies (~100-425 d). |
| Range | r 18.86-21.40 (2-98 %: 19.14-20.72); g 19.49-21.87 (19.98-21.39) |
| Checks | dips do not track limiting magnitude, airmass or zero-point scatter (|r| < 0.15); 5 neighbouring stars on the same CCD do not dip (correlations ~0.0); no Gaia neighbour within 6"; no mid-IR excess in AllWISE (W1-W2 0.25; W3/W4 upper limits) |
| Suggested VSX type | VAR (dipping variable; nature unknown). Spectroscopy is needed. |
| Plots | B_GaiaDR3_1355878947229358336_seasons.png, B_ZTF_overview.png |

Labels: the variability and periods are VERIFIED from ZTF data. "New" is VERIFIED only against the catalogues listed above. The physical classifications are CONJECTURED.

## Submission log
- 2026-11-22 16:45 UTC: Star A submitted to VSX by Deepnil Ray as ZTF J164226.77+392523.3. Status "New", awaiting moderator review.
- Star B: not yet submitted (VSX allows one submission per day).
- 2026-11-22 18:22 UTC: VSX revision history shows revision 1 by "Admin, VSX", checked as the approved revision ("Initial database population."). This looks like approval, to be confirmed on the star's VSX page.
