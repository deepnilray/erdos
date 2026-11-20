# vet2 report: far target list (final)

Generated 2026-11-20 15:56 UTC; 6 targets; machine-generated, the plots in plots/ still need a look by eye.

Kill rules: field-control z < 5 (detector-1 and list targets); centroid jump > 3 sigma toward a Gaia neighbour; Gaia neighbour within 6" with dG < 3; baseline W1 < 8; SIMBAD CV / confirmed eclipsing binary (counterpart within 3"); SIMBAD galaxy/QSO within 6"; young star (SIMBAD Y*O, Y*?, TT*, TT?, Or*, Ae*, Ae?, pr* within 5" or Gaia variability class YSO) kills detector-1/list targets and labels detector-2 targets 'known/likely young star'. Flags (not kills): 'not plain dust' (optical brightening at the infrared onset in >= 2 ASAS-SN cameras, none dimming, median < -0.015 mag), SIMBAD '?' candidate types, RUWE, NSS, ext_flg, colour classes.

## Controls

| Control | Result | Detail |
|---|---|---|
| ASASSN-21qj | PASS | category SURVIVOR, SIMBAD 2MASS J08152329-3859234 (10 refs), field z 57.3, missing: none |
| J060000 | PASS | category SURVIVOR, largest ASAS-SN seasonal dimming 0.35 mag at MJD 58864 |
| V836 Tau | PASS | young: SIMBAD young-star types Or*,TT*,TT?,Y*?,Y*O (V* V836 Tau) | Gaia DR3 variability class YSO(0.83) |

Counts: {'SURVIVOR': 5, 'YOUNG': 1}

## Survivors (5)

### ASASSN-21qj (uid3303105)  [CONTROL+D1]  SURVIVOR
- position 123.84704 -38.98983; Gaia DR3 5539970601632026752; G 13.37, BP-RP 0.81, plx 1.76 mas; plot `plots/ASASSN-21qj_uid3303105_.png`
- flags: centroid jump 0.349" (5.5 sigma, PA 56) away from the neighbour(s) 3.7" PA253 G16.9, as expected when the target itself brightens in a blended WISE PSF | largest seasonal optical dimming 1.11 mag (MJD 59529)
- NEOWISE: score refetch 38.04 (stored 38.04, reproduced True); dW2 0.738, dW1 0.332, 12 visits, 133 points; baseline W1 11.65, W1-W2 -0.057; onset between MJD 58072 and 58227
- field control: target step +0.803 (W1 +0.402); neighbours N=169, median -0.003, robust sigma 0.014, max +0.055; z = 57.3
- centroid: jump at onset 0.349" +- 0.063 (5.5 sigma, PA 56); largest consecutive-visit jump 0.212"; rms 0.109"; toward neighbour: none; expected shift if a neighbour were the source: 3.7" G16.9: 1.94"; 7.3" G18.7: 3.81"
- AllWISE 2010: W1-W2 -0.068, W2-W3 -0.498 (W3 S/N 2.3), W3-W4 3.219 (W4 S/N -2.6), ext_flg 0, ph_qual AACU: W3 S/N < 5: no W2-W3 class
- Gaia: RUWE 1.10, ipd_frac_multi_peak 0, NSS none, Teff 5761 K, logg 4.34, H-alpha pEW 0.112 nm, varclass none; M_G 4.60, +0.07 mag vs sequence (on the sequence); neighbours within 10": 3.7" PA253 G16.91 dG+3.54; 7.3" PA182 G18.67 dG+5.30
- SIMBAD (10"): 2MASS J08152329-3859234 [*; *,NIR] 0.15" refs=10; 2MASS J08152298-3859244 [*; *,NIR] 3.74" refs=1
- ASAS-SN: 1351 points, cameras bE(g,411); be(V,238, d=-0.018); bi(g,497); bm(g,205); change at onset (after-before, per-camera median) -0.018 mag; largest seasonal dimming 1.11 mag at MJD 59529
- dust: excess flux W1 2.72 mJy, W2 3.68 mJy, T = 953 K (16-84%: 934-972) 

### uid55937  [D2]  SURVIVOR
- position 110.89912 -33.16840; Gaia DR3 5592473072135280640; G 14.33, BP-RP 1.58, plx 3.90 mas; plot `plots/uid55937.png`
- flags: AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 0.43 (stored 0.43, reproduced True); dW2 0.032, dW1 0.025, 14 visits, 169 points; baseline W1 11.30, W1-W2 0.344; onset between MJD 59668 and 60035
- detector 2: excess 0.398 mag, z 18.8, jitter ratio 5.9
- field control: target step +0.178 (W1 +0.087); neighbours N=154, median -0.002, robust sigma 0.009, max +0.037; z = 19.4
- centroid: jump at onset 0.011" +- 0.023 (0.5 sigma, PA 179); largest consecutive-visit jump 0.054"; rms 0.028"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.260, W2-W3 1.766 (W3 S/N 33.5), W3-W4 1.345 (W4 S/N 5.4), ext_flg 0, ph_qual AAAB: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.10, ipd_frac_multi_peak 0, NSS none, Teff 4488 K, logg 4.67, H-alpha pEW -0.103 nm, varclass none; M_G 7.28, -0.03 mag vs sequence (on the sequence); neighbours within 10": none
- SIMBAD (10"): no object
- ASAS-SN: 1407 points, cameras bG(g,511, d=+0.005); bg(V,226); bk(g,480, d=+0.002); bo(g,190, d=+0.020); change at onset (after-before, per-camera median) +0.005 mag; largest seasonal dimming 0.01 mag at MJD 58194
- dust: excess flux W1 0.48 mJy, W2 0.40 mJy, T = 1695 K (16-84%: 1283-2631) 

### J060000  [CONTROL]  SURVIVOR
- position 90.00308 -31.00781; Gaia DR3 2891196718939580672; G 13.13, BP-RP 1.52, plx 6.39 mas; plot `plots/J060000.png`
- flags: SIMBAD candidate type(s) EB? (ASASSN-V J060000.76-310027.8): uncertain, not a kill | AllWISE ext_flg = 1 (extended or 2MASS XSC association) | optical dimming +0.142 mag after the infrared onset (debris transit signature) | largest seasonal optical dimming 0.35 mag (MJD 58864)
- NEOWISE: score refetch 8.86 (stored n/a, reproduced n/a); dW2 0.130, dW1 0.042, 21 visits, 253 points; baseline W1 10.52, W1-W2 -0.063; onset between MJD 58751 and 58905
- field control: target step +0.146 (W1 +0.049); neighbours N=54, median +0.003, robust sigma 0.010, max +0.054; z = 14.9
- centroid: jump at onset 0.031" +- 0.021 (1.5 sigma, PA 264); largest consecutive-visit jump 0.050"; rms 0.029"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 -0.092, W2-W3 0.039 (W3 S/N 15.2), W3-W4 1.732 (W4 S/N 1.3), ext_flg 1, ph_qual AAAU: photosphere-like (W2-W3 < 0.5)
- Gaia: RUWE 1.02, ipd_frac_multi_peak 0, NSS none, Teff 4498 K, logg 4.67, H-alpha pEW -0.051 nm, varclass SOLAR_LIKE(0.41); M_G 7.16, -0.00 mag vs sequence (on the sequence); neighbours within 10": none
- SIMBAD (10"): ASASSN-V J060000.76-310027.8 [EB?; *,EB?,MIR,NIR,V*] 0.37" refs=12
- ASAS-SN: 1581 points, cameras bE(g,355, d=+0.102); be(V,379); bi(g,415, d=+0.109); bm(g,268, d=+0.276); bq(g,164, d=+0.176); change at onset (after-before, per-camera median) +0.142 mag; largest seasonal dimming 0.35 mag at MJD 58864
- dust: excess flux W1 0.87 mJy, W2 1.44 mJy, T = 813 K (16-84%: 728-912) 

### uid137313  [D2]  SURVIVOR
- position 330.31742 -28.50241; Gaia DR3 6617669842852419712; G 13.04, BP-RP 1.06, plx 3.77 mas; plot `plots/uid137313.png`
- flags: AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 1.49 (stored 1.49, reproduced True); dW2 0.135, dW1 0.090, 17 visits, 127 points; baseline W1 11.02, W1-W2 0.217; onset between MJD 57885 and 58052
- detector 2: excess 0.272 mag, z 20.4, jitter ratio 7.0
- field control: target step +0.112 (W1 +0.058); neighbours N=29, median -0.007, robust sigma 0.019, max +0.040; z = 6.4
- centroid: jump at onset 0.025" +- 0.017 (1.4 sigma, PA 216); largest consecutive-visit jump 0.087"; rms 0.031"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.276, W2-W3 2.526 (W3 S/N 52.3), W3-W4 0.685 (W4 S/N 6.7), ext_flg 0, ph_qual AAAB: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.05, ipd_frac_multi_peak 0, NSS none, Teff 5113 K, logg 4.58, H-alpha pEW 0.009 nm, varclass SOLAR_LIKE(0.42); M_G 5.92, +0.15 mag vs sequence (on the sequence); neighbours within 10": none
- SIMBAD (10"): UCAC4 308-275485 [*; *,NIR] 0.24" refs=4
- ASAS-SN: 1157 points, cameras bE(g,256); be(V,244, d=-0.004); bi(g,275); bm(g,229); bq(g,153); change at onset (after-before, per-camera median) -0.004 mag; largest seasonal dimming 0.02 mag at MJD 59848
- dust: excess flux W1 0.69 mJy, W2 0.67 mJy, T = 1377 K (16-84%: 1139-1747) 

### uid126443  [D2]  SURVIVOR
- position 344.04495 +63.72553; Gaia DR3 2208143124690762368; G 13.42, BP-RP 1.21, plx 3.78 mas; plot `plots/uid126443.png`
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association)
- NEOWISE: score refetch 0.75 (stored 0.75, reproduced True); dW2 0.100, dW1 0.363, 13 visits, 181 points; baseline W1 11.23, W1-W2 0.117; onset between MJD 57038 and 57226
- detector 2: excess 0.179 mag, z 12.1, jitter ratio 4.4
- field control: target step -0.002 (W1 +0.016); neighbours N=194, median -0.008, robust sigma 0.010, max +0.097; z = 0.7
- centroid: jump at onset 0.234" +- 0.330 (0.7 sigma, PA 74); largest consecutive-visit jump 1.335"; rms 0.557"; toward neighbour: 5.7" PA44 G20.4 (angle 30 deg); expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 -0.326, W2-W3 0.222 (W3 S/N 15.2), W3-W4 0.806 (W4 S/N 2.2), ext_flg 1, ph_qual AAAC: photosphere-like (W2-W3 < 0.5)
- Gaia: RUWE 1.27, ipd_frac_multi_peak 0, NSS none, Teff 4885 K, logg 4.57, H-alpha pEW -0.037 nm, varclass SOLAR_LIKE(0.57); M_G 6.31, +0.04 mag vs sequence (on the sequence); neighbours within 10": 5.7" PA44 G20.42 dG+6.99; 7.6" PA258 G17.32 dG+3.90
- SIMBAD (10"): Gaia DR3 2208143124690762368 [*; *] 0.17" refs=1
- ASAS-SN: 1002 points, cameras bC(g,310); bc(V,172, d=+0.003); br(g,289); bs(g,231); change at onset (after-before, per-camera median) +0.003 mag; largest seasonal dimming 0.02 mag at MJD 59568
- dust: excess flux W1 3.50 mJy, W2 0.50 mJy, T = 8000 K (16-84%: 8000-8000) ratio bluer than an 8000 K blackbody (not dust-like)

## Known/likely young stars (detector 2) (1)

### V836 Tau  [CONTROL]  YOUNG
- position 75.77751 +25.38870; Gaia DR3 3420008412568724736; G 12.64, BP-RP 2.11, plx 5.99 mas; plot `plots/V836_Tau.png`
- **young:** SIMBAD young-star types Or*,TT*,TT?,Y*?,Y*O (V* V836 Tau) | Gaia DR3 variability class YSO(0.83)
- flags: 2.27 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | possible optical brightening at onset (-0.045 mag, one camera only)
- NEOWISE: score refetch 1.57 (stored n/a, reproduced n/a); dW2 0.286, dW1 0.325, 20 visits, 187 points; baseline W1 8.42, W1-W2 0.425; onset between MJD 57641 and 57806
- field control: target step +0.210 (W1 +0.198); neighbours N=99, median -0.003, robust sigma 0.011, max +0.164; z = 19.2
- centroid: jump at onset 0.009" +- 0.015 (0.6 sigma, PA 229); largest consecutive-visit jump 0.075"; rms 0.027"; toward neighbour: none; expected shift if a neighbour were the source: 8.8" G20.2: 1.55"
- AllWISE 2010: W1-W2 0.466, W2-W3 1.801 (W3 S/N 69.5), W3-W4 2.069 (W4 S/N 44.4), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.17, ipd_frac_multi_peak 0, NSS none, Teff 5302 K, logg 4.16, H-alpha pEW -0.770 nm, varclass YSO(0.83); M_G 6.53, -2.27 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 8.8" PA107 G20.21 dG+7.56
- SIMBAD (10"): V* V836 Tau [TT*; *,BY*,Em*,IR,MIR,NIR,Or*,TT*,TT?,V*,X,Y*?,Y*O] 0.28" refs=249; USNO-B1.0 1153-00064776 [*; *] 7.05" refs=1
- ASAS-SN: 803 points, cameras bB(g,101); bF(g,94); bb(V,205, d=-0.045); bj(g,99); bn(g,114); br(g,190); change at onset (after-before, per-camera median) -0.045 mag; largest seasonal dimming 0.09 mag at MJD 58867
- dust: excess flux W1 45.49 mJy, W2 36.20 mJy, T = 1882 K (16-84%: 1761-2023) 

