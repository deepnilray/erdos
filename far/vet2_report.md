# vet2 report: far target list (final)

Generated 2026-11-22 20:45 UTC; 201 targets; machine-generated, the plots in plots/ still need a look by eye.

Kill rules: field-control z < 5 (detector-1 and list targets); centroid jump > 3 sigma toward a Gaia neighbour; Gaia neighbour within 6" with dG < 3; baseline W1 < 8; SIMBAD CV / confirmed eclipsing binary (counterpart within 3"); SIMBAD galaxy/QSO within 6"; young star (SIMBAD Y*O, Y*?, TT*, TT?, Or*, Ae*, Ae?, pr* within 5" or Gaia variability class YSO) kills detector-1/list targets and labels detector-2 targets 'known/likely young star'. Flags (not kills): 'not plain dust' (optical brightening at the infrared onset in >= 2 ASAS-SN cameras, none dimming, median < -0.015 mag), SIMBAD '?' candidate types, RUWE, NSS, ext_flg, colour classes.

## Controls

| Control | Result | Detail |
|---|---|---|
| ASASSN-21qj | PASS | category SURVIVOR, SIMBAD 2MASS J08152329-3859234 (10 refs), field z 57.3, missing: none |
| J060000 | PASS | category SURVIVOR, largest ASAS-SN seasonal dimming 0.35 mag at MJD 58864 |
| V836 Tau | PASS | young: SIMBAD young-star types Or*,TT*,TT?,Y*?,Y*O (V* V836 Tau) | Gaia DR3 variability class YSO(0.83) |

Counts: {'YOUNG': 138, 'KILLED': 32, 'SURVIVOR': 31}

## Survivors (31)

### uid269584  [D2]  SURVIVOR
- position 81.02729 +34.27504; Gaia DR3 182736942750800256; G 11.57, BP-RP 0.83, plx 3.58 mas; plot `plots/uid269584.png`
- NEOWISE: score refetch 0.90 (stored 0.90, reproduced True); dW2 0.085, dW1 0.020, 18 visits, 160 points; baseline W1 9.99, W1-W2 0.135; onset between MJD 58377 and 58535
- detector 2: excess 0.174 mag, z 16.5, jitter ratio 9.1
- field control: target step +0.031 (W1 +0.008); neighbours N=191, median -0.002, robust sigma 0.010, max +0.120; z = 3.2
- centroid: jump at onset 0.263" +- 0.221 (1.2 sigma, PA 85); largest consecutive-visit jump 0.544"; rms 0.200"; toward neighbour: 6.8" PA68 G18.5 (angle 16 deg); expected shift if a neighbour were the source: 5.5" G19.7: 0.16"; 6.8" G18.5: 0.19"
- AllWISE 2010: W1-W2 -0.046, W2-W3 -0.108 (W3 S/N 9.1), W3-W4 1.775 (W4 S/N -0.7), ext_flg 0, ph_qual AABU: photosphere-like (W2-W3 < 0.5)
- Gaia: RUWE 1.05, ipd_frac_multi_peak 0, NSS none, Teff 6026 K, logg 4.34, H-alpha pEW 0.129 nm, varclass none; M_G 4.34, -0.28 mag vs sequence (on the sequence); neighbours within 10": 5.5" PA153 G19.67 dG+8.10; 6.8" PA68 G18.46 dG+6.89
- SIMBAD (10"): TYC 2411-1146-1 [*; *,NIR] 0.49" refs=0; 2MASS J05240704+3416326 [Y*O; MIR,NIR,Y*O] 6.66" refs=1
- ASAS-SN: 1048 points, cameras bA(g,216); bB(g,95); ba(V,159); bb(V,190); bq(g,194, d=+0.005); br(g,194, d=-0.013); change at onset (after-before, per-camera median) -0.004 mag; largest seasonal dimming 0.00 mag at MJD 60640
- dust: excess flux W1 0.17 mJy, W2 1.79 mJy, T = 350 K (16-84%: 150-529) 

### uid2197550  [D2]  SURVIVOR
- position 289.25664 -52.80192; Gaia DR3 6644835648441098880; G 14.09, BP-RP 1.24, plx 2.32 mas; plot `plots/uid2197550.png`
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 19 visits, 152 points; baseline W1 11.42, W1-W2 0.331; onset between MJD 57294 and 57482
- detector 2: excess 0.392 mag, z 20.4, jitter ratio 3.1
- field control: target step +0.018 (W1 +0.000); neighbours N=72, median -0.003, robust sigma 0.012, max +0.029; z = 1.8
- centroid: jump at onset 0.424" +- 0.189 (2.2 sigma, PA 145); largest consecutive-visit jump 0.357"; rms 0.243"; toward neighbour: none; expected shift if a neighbour were the source: 5.8" G17.5: 0.10"; 6.9" G17.9: 0.11"; 6.9" G18.2: 0.11"; 8.6" G20.9: 0.14"; 9.5" G20.1: 0.16"
- AllWISE 2010: W1-W2 -0.033, W2-W3 0.714 (W3 S/N 7.6), W3-W4 2.320 (W4 S/N 0.2), ext_flg 0, ph_qual AABU: weak W3 excess (0.5 < W2-W3 < 1.0)
- Gaia: RUWE 1.05, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW 0.018 nm, varclass none; M_G 5.91, -0.47 mag vs sequence (on the sequence); neighbours within 10": 5.8" PA95 G17.54 dG+3.45; 6.9" PA315 G17.87 dG+3.78; 6.9" PA283 G18.17 dG+4.08; 8.6" PA336 G20.88 dG+6.79; 9.5" PA67 G20.08 dG+5.98
- SIMBAD (10"): no object
- ASAS-SN: 2569 points, cameras bE(g,351); bF(g,374); be(V,299, d=-0.002); bf(V,227, d=+0.010); bi(g,423); bj(g,420); bm(g,230); bn(g,245); change at onset (after-before, per-camera median) +0.004 mag; largest seasonal dimming 0.01 mag at MJD 57187
- dust: excess flux W1 -0.03 mJy, W2 -0.35 mJy, T = n/a K (16-84%: n/a-n/a) no W2 excess flux after onset

### uid456710  [D2]  SURVIVOR
- position 266.00230 -29.70248; Gaia DR3 4057049442363660800; G 12.77, BP-RP 1.13, plx 3.36 mas; plot `plots/uid456710.png`
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 9 visits, 91 points; baseline W1 9.21, W1-W2 0.360; onset between MJD 60186 and 60386
- detector 2: excess 0.417 mag, z 23.4, jitter ratio 7.7
- field control: target step +0.107 (W1 +0.078); neighbours N=33, median +0.049, robust sigma 0.050, max +0.196; z = 1.2
- centroid: jump at onset 0.203" +- 0.157 (1.3 sigma, PA 50); largest consecutive-visit jump 0.319"; rms 0.136"; toward neighbour: 8.2" PA40 G19.7 (angle 9 deg); expected shift if a neighbour were the source: 8.2" G19.7: 0.77"
- AllWISE 2010: W1-W2 0.339, W2-W3 0.192 (W3 S/N -3.0), W3-W4 3.165 (W4 S/N -2.6), ext_flg 0, ph_qual AAUU: W3 S/N < 5: no W2-W3 class; W1-W2 > 0.25
- Gaia: RUWE 0.84, ipd_frac_multi_peak 0, NSS none, Teff 5185 K, logg 4.36, H-alpha pEW 0.113 nm, varclass none; M_G 5.40, -0.60 mag vs sequence (on the sequence); neighbours within 10": 8.2" PA40 G19.75 dG+6.98
- SIMBAD (10"): no object
- ASAS-SN: 1008 points, cameras bF(g,250, d=+0.007); bf(V,196); bj(g,241, d=+0.011); bn(g,163, d=-0.000); br(g,158, d=-0.007); change at onset (after-before, per-camera median) +0.004 mag; largest seasonal dimming 0.02 mag at MJD 59324
- dust: excess flux W1 3.35 mJy, W2 2.50 mJy, T = 2169 K (16-84%: 665-8000) 

### uid260980  [D2]  SURVIVOR
- position 174.48976 -53.83442; Gaia DR3 5344918888145491200; G 12.12, BP-RP 0.85, plx 3.59 mas; plot `plots/uid260980.png`
- NEOWISE: score refetch 0.33 (stored 0.33, reproduced True); dW2 0.020, dW1 0.020, 15 visits, 162 points; baseline W1 10.45, W1-W2 0.148; onset between MJD 57040 and 57212
- detector 2: excess 0.189 mag, z 16.8, jitter ratio 3.6
- field control: target step -0.027 (W1 -0.003); neighbours N=187, median -0.002, robust sigma 0.009, max +0.032; z = -2.9
- centroid: jump at onset 0.040" +- 0.017 (2.4 sigma, PA 119); largest consecutive-visit jump 0.040"; rms 0.030"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.231, W2-W3 2.741 (W3 S/N 66.1), W3-W4 0.778 (W4 S/N 19.3), ext_flg 0, ph_qual AAAA: W3 excess only (W2-W3 > 1.0; debris-disk-like or blend)
- Gaia: RUWE 0.90, ipd_frac_multi_peak 0, NSS none, Teff 5694 K, logg 4.39, H-alpha pEW 0.114 nm, varclass SOLAR_LIKE(0.07); M_G 4.90, +0.15 mag vs sequence (on the sequence); neighbours within 10": 2.3" PA196 G19.37 dG+7.25; 5.4" PA229 G20.98 dG+8.86; 9.8" PA73 G20.66 dG+8.54
- SIMBAD (10"): UCAC4 181-077121 [*; *,NIR] 0.34" refs=2
- ASAS-SN: 1091 points, cameras bF(g,321); bf(V,216); bj(g,361); bn(g,193); change at onset (after-before, per-camera median) n/a mag; largest seasonal dimming 0.04 mag at MJD 60008
- dust: excess flux W1 2.30 mJy, W2 2.58 mJy, T = 1144 K (16-84%: 1059-1238) 
- checks missing: ASAS-SN change at onset (no camera spans the onset)

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

### uid1586996  [D2]  SURVIVOR
- position 328.43464 +51.55683; Gaia DR3 1980668325126831360; G 11.62, BP-RP 0.89, plx 2.57 mas; plot `plots/uid1586996.png`
- flags: centroid jump 0.220" (3.3 sigma, PA 100) away from the neighbour(s) 7.7" PA272 G11.0, as expected when the target itself brightens in a blended WISE PSF | 1.28 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 9 visits, 157 points; baseline W1 8.05, W1-W2 0.388; onset between MJD 58093 and 59914
- detector 2: excess 0.432 mag, z 35.2, jitter ratio 9.2
- field control: target step +0.710 (W1 +0.831); neighbours N=143, median -0.014, robust sigma 0.013, max +0.060; z = 54.2
- centroid: jump at onset 0.220" +- 0.067 (3.3 sigma, PA 100); largest consecutive-visit jump 0.122"; rms 0.050"; toward neighbour: none; expected shift if a neighbour were the source: 4.2" G19.0: 2.02"; 7.7" G11.0: 3.69"
- AllWISE 2010: W1-W2 0.469, W2-W3 1.766 (W3 S/N 94.5), W3-W4 2.169 (W4 S/N 53.3), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.05, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW -0.442 nm, varclass none; M_G 3.67, -1.28 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 4.2" PA187 G19.02 dG+7.40; 7.7" PA272 G11.04 dG-0.58
- SIMBAD (10"): IRAS 21519+5119 [*; *,IR,NIR] 0.08" refs=5; TYC 3616-1417-1 [*; *] 7.77" refs=5
- ASAS-SN: 739 points, cameras bB(g,132, d=+0.008); bb(V,194); br(g,344, d=+0.008); cB(g,69); change at onset (after-before, per-camera median) +0.008 mag; largest seasonal dimming 0.08 mag at MJD 59352
- dust: excess flux W1 164.30 mJy, W2 107.02 mJy, T = 3353 K (16-84%: 2949-3915) 

### uid2015396  [D1]  SURVIVOR
- position 221.65121 +31.17950; Gaia DR3 1283261877869284096; G 15.00, BP-RP 1.38, plx 2.38 mas; plot `plots/uid2015396.png`
- flags: centroid jump 0.153" (3.2 sigma, PA 59) not toward a Gaia neighbour | SIMBAD candidate type(s) Bz?,Q? (BWE 1444+3123): uncertain, not a kill | not plain dust: optical brightening -0.040 mag (per-camera -0.025,-0.040,-0.106,-0.072,-0.035) together with the infrared rise
- NEOWISE: score refetch 10.97 (stored 10.97, reproduced True); dW2 0.550, dW1 0.245, 13 visits, 135 points; baseline W1 12.46, W1-W2 0.016; onset between MJD 59756 and 59962
- field control: target step +0.524 (W1 +0.229); neighbours N=13, median -0.006, robust sigma 0.018, max +0.036; z = 29.8
- centroid: jump at onset 0.153" +- 0.048 (3.2 sigma, PA 59); largest consecutive-visit jump 0.280"; rms 0.083"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.063, W2-W3 1.237 (W3 S/N 10.9), W3-W4 1.919 (W4 S/N 2.6), ext_flg 0, ph_qual AAAC: W3 excess only (W2-W3 > 1.0; debris-disk-like or blend)
- Gaia: RUWE 1.00, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW -0.083 nm, varclass none; M_G 6.89, +0.10 mag vs sequence (on the sequence); neighbours within 10": none
- SIMBAD (10"): BWE 1444+3123 [Bz?; Bz?,Q?,Rad,gam] 0.88" refs=18
- ASAS-SN: 1159 points, cameras bC(g,231, d=-0.025); bG(g,102, d=-0.040); bc(V,290); bg(V,30); bk(g,132, d=-0.106); bo(g,118, d=-0.072); bs(g,256, d=-0.035); change at onset (after-before, per-camera median) -0.040 mag; largest seasonal dimming 0.03 mag at MJD 60540
- dust: excess flux W1 0.93 mJy, W2 1.45 mJy, T = 846 K (16-84%: 820-872) 

### uid2128363  [D2]  SURVIVOR
- position 57.33148 +38.74405; Gaia DR3 223834423952712960; G 13.72, BP-RP 1.69, plx 2.34 mas; plot `plots/uid2128363.png`
- flags: 2.05 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | possible optical brightening at onset (-0.033 mag, one camera only) | largest seasonal optical dimming 0.21 mag (MJD 59831)
- NEOWISE: score refetch 1.83 (stored 1.83, reproduced True); dW2 0.325, dW1 0.289, 21 visits, 210 points; baseline W1 9.49, W1-W2 0.362; onset between MJD 58151 and 58356
- detector 2: excess 0.406 mag, z 13.8, jitter ratio 10.6
- field control: target step +0.312 (W1 +0.288); neighbours N=71, median -0.003, robust sigma 0.012, max +0.030; z = 26.6
- centroid: jump at onset 0.013" +- 0.017 (0.8 sigma, PA 93); largest consecutive-visit jump 0.037"; rms 0.027"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.408, W2-W3 2.252 (W3 S/N 69.7), W3-W4 1.975 (W4 S/N 33.5), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.06, ipd_frac_multi_peak 0, NSS none, Teff 5507 K, logg 4.15, H-alpha pEW -1.590 nm, varclass none; M_G 5.57, -2.05 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): UCAC4 644-016739 [Em*; *,Em*,MIR,NIR,Opt,ev] 0.19" refs=4
- ASAS-SN: 650 points, cameras bD(g,253); bd(V,180, d=-0.033); bt(g,217); change at onset (after-before, per-camera median) -0.033 mag; largest seasonal dimming 0.21 mag at MJD 59831
- dust: excess flux W1 7.27 mJy, W2 7.19 mJy, T = 1323 K (16-84%: 1215-1455) 

### uid239897  [D2]  SURVIVOR
- position 222.73717 +36.20318; Gaia DR3 1293509154439630464; G 14.04, BP-RP 1.46, plx 3.62 mas; plot `plots/uid239897.png`
- flags: AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 1.25 (stored 1.25, reproduced True); dW2 0.095, dW1 0.073, 21 visits, 272 points; baseline W1 11.28, W1-W2 0.307; onset between MJD 57931 and 58134
- detector 2: excess 0.368 mag, z 16.9, jitter ratio 4.1
- field control: target step +0.252 (W1 +0.132); neighbours N=17, median -0.008, robust sigma 0.013, max +0.017; z = 20.6
- centroid: jump at onset 0.035" +- 0.015 (2.4 sigma, PA 100); largest consecutive-visit jump 0.042"; rms 0.032"; toward neighbour: none; expected shift if a neighbour were the source: 2.7" G17.8: 0.57"
- AllWISE 2010: W1-W2 0.303, W2-W3 1.922 (W3 S/N 43.4), W3-W4 1.252 (W4 S/N 9.4), ext_flg 0, ph_qual AAAB: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.05, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW -0.201 nm, varclass none; M_G 6.83, -0.16 mag vs sequence (on the sequence); neighbours within 10": 2.7" PA346 G17.75 dG+3.71
- SIMBAD (10"): no object
- ASAS-SN: 2310 points, cameras bB(g,172); bC(g,257); bD(g,375); bb(V,339, d=-0.009); bc(V,277, d=-0.011); bd(V,304, d=-0.016); bs(g,257); bt(g,231); cB(g,98); change at onset (after-before, per-camera median) -0.011 mag; largest seasonal dimming 0.01 mag at MJD 59847
- dust: excess flux W1 1.01 mJy, W2 1.37 mJy, T = 949 K (16-84%: 891-1012) 

### uid55937  [D2]  SURVIVOR
- position 110.89912 -33.16840; Gaia DR3 5592473072135280640; G 14.33, BP-RP 1.58, plx 3.90 mas; plot `plots/uid55937.png`
- flags: AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 0.43 (stored 0.43, reproduced True); dW2 0.032, dW1 0.025, 14 visits, 169 points; baseline W1 11.30, W1-W2 0.344; onset between MJD 59668 and 60035
- detector 2: excess 0.398 mag, z 15.7, jitter ratio 5.9
- field control: target step +0.178 (W1 +0.087); neighbours N=154, median -0.002, robust sigma 0.009, max +0.037; z = 19.4
- centroid: jump at onset 0.011" +- 0.023 (0.5 sigma, PA 179); largest consecutive-visit jump 0.054"; rms 0.028"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.260, W2-W3 1.766 (W3 S/N 33.5), W3-W4 1.345 (W4 S/N 5.4), ext_flg 0, ph_qual AAAB: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.10, ipd_frac_multi_peak 0, NSS none, Teff 4488 K, logg 4.67, H-alpha pEW -0.103 nm, varclass none; M_G 7.28, -0.03 mag vs sequence (on the sequence); neighbours within 10": none
- SIMBAD (10"): no object
- ASAS-SN: 1407 points, cameras bG(g,511, d=+0.005); bg(V,226); bk(g,480, d=+0.002); bo(g,190, d=+0.020); change at onset (after-before, per-camera median) +0.005 mag; largest seasonal dimming 0.01 mag at MJD 58194
- dust: excess flux W1 0.48 mJy, W2 0.40 mJy, T = 1695 K (16-84%: 1283-2631) 

### uid560552  [D2]  SURVIVOR
- position 154.12017 +30.34097; Gaia DR3 742228176188664832; G 12.07, BP-RP 0.84, plx 3.26 mas; plot `plots/uid560552.png`
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association)
- NEOWISE: score refetch 0.06 (stored 0.06, reproduced True); dW2 0.007, dW1 -0.018, 12 visits, 104 points; baseline W1 10.53, W1-W2 0.120; onset between MJD 58230 and 58439
- detector 2: excess 0.161 mag, z 14.7, jitter ratio 10.3
- field control: target step +0.138 (W1 +0.038); neighbours N=11, median -0.005, robust sigma 0.009, max +0.035; z = 16.0
- centroid: jump at onset 0.123" +- 0.090 (1.4 sigma, PA 73); largest consecutive-visit jump 0.126"; rms 0.101"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.155, W2-W3 1.417 (W3 S/N 33.1), W3-W4 2.426 (W4 S/N 11.4), ext_flg 1, ph_qual AAAA: W3 excess only (W2-W3 > 1.0; debris-disk-like or blend)
- Gaia: RUWE 1.07, ipd_frac_multi_peak 0, NSS none, Teff 5654 K, logg 4.36, H-alpha pEW 0.101 nm, varclass none; M_G 4.63, -0.06 mag vs sequence (on the sequence); neighbours within 10": none
- SIMBAD (10"): no object
- ASAS-SN: 1056 points, cameras bC(g,209); bG(g,80); bc(V,226, d=-0.003); bg(V,26); bk(g,180, d=+0.002); bo(g,129, d=-0.002); bs(g,206, d=-0.002); change at onset (after-before, per-camera median) -0.002 mag; largest seasonal dimming 0.01 mag at MJD 59906
- dust: excess flux W1 0.16 mJy, W2 1.10 mJy, T = 403 K (16-84%: 264-512) 

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

### uid1458786  [D2]  SURVIVOR
- position 122.68027 -55.75373; Gaia DR3 5319098678618296192; G 14.92, BP-RP 1.67, plx 2.63 mas; plot `plots/uid1458786.png`
- flags: AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | possible optical brightening at onset (-0.085 mag, one camera only) | largest seasonal optical dimming 0.28 mag (MJD 57062)
- NEOWISE: score refetch 0.66 (stored 0.66, reproduced True); dW2 0.075, dW1 0.113, 21 visits, 411 points; baseline W1 9.99, W1-W2 0.789; onset between MJD 57725 and 57887
- detector 2: excess 0.835 mag, z 29.7, jitter ratio 9.4
- field control: target step +0.113 (W1 +0.110); neighbours N=107, median -0.004, robust sigma 0.008, max +0.107; z = 14.3
- centroid: jump at onset 0.014" +- 0.026 (0.6 sigma, PA 307); largest consecutive-visit jump 0.074"; rms 0.041"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.755, W2-W3 2.495 (W3 S/N 73.8), W3-W4 2.019 (W4 S/N 42.9), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.16, ipd_frac_multi_peak 0, NSS none, Teff 6071 K, logg 4.53, H-alpha pEW -7.158 nm, varclass none; M_G 7.02, -0.54 mag vs sequence (on the sequence); neighbours within 10": none
- SIMBAD (10"): no object
- ASAS-SN: 2186 points, cameras bE(g,427); be(V,267, d=-0.085); bi(g,461); bk(g,429); bm(g,228); bo(g,374); change at onset (after-before, per-camera median) -0.085 mag; largest seasonal dimming 0.28 mag at MJD 57062
- dust: excess flux W1 3.92 mJy, W2 3.89 mJy, T = 1320 K (16-84%: 1173-1515) 

### uid1277809  [D2]  SURVIVOR
- position 280.04305 +23.47269; Gaia DR3 4532694083738109824; G 14.77, BP-RP 1.56, plx 2.73 mas; plot `plots/uid1277809.png`
- flags: AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 20 visits, 244 points; baseline W1 11.55, W1-W2 0.483; onset between MJD 59837 and 60037
- detector 2: excess 0.539 mag, z 21.8, jitter ratio 6.0
- field control: target step +0.163 (W1 +0.071); neighbours N=127, median +0.000, robust sigma 0.012, max +0.036; z = 13.7
- centroid: jump at onset 0.008" +- 0.020 (0.4 sigma, PA 297); largest consecutive-visit jump 0.037"; rms 0.034"; toward neighbour: none; expected shift if a neighbour were the source: 8.7" G17.3: 1.21"
- AllWISE 2010: W1-W2 0.485, W2-W3 2.091 (W3 S/N 36.2), W3-W4 0.834 (W4 S/N 5.0), ext_flg 0, ph_qual AAAB: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.06, ipd_frac_multi_peak 1, NSS none, Teff 4485 K, logg 4.44, H-alpha pEW -0.198 nm, varclass RS(0.34); M_G 6.95, -0.31 mag vs sequence (on the sequence); neighbours within 10": 8.7" PA213 G17.27 dG+2.51
- SIMBAD (10"): ZTF J184010.33+232821.7 [BY*; *,BY*] 0.10" refs=4
- ASAS-SN: 0 points, cameras n/a; change at onset (after-before, per-camera median) n/a mag; largest seasonal dimming n/a mag at MJD n/a
- dust: excess flux W1 -0.12 mJy, W2 0.10 mJy, T = 150 K (16-84%: 150-150) W1 excess <= 0: colder than ~150 K (upper limit)
- checks missing: ASAS-SN (no source)

### uid1678383  [D2]  SURVIVOR
- position 58.48789 +35.04418; Gaia DR3 218942765440887936; G 13.62, BP-RP 1.60, plx 2.52 mas; plot `plots/uid1678383.png`
- flags: 1.73 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | optical dimming +0.055 mag after the infrared onset (debris transit signature)
- NEOWISE: score refetch 2.11 (stored 2.11, reproduced True); dW2 0.214, dW1 0.152, 21 visits, 217 points; baseline W1 10.00, W1-W2 0.377; onset between MJD 57068 and 57261
- detector 2: excess 0.430 mag, z 16.6, jitter ratio 7.6
- field control: target step +0.139 (W1 +0.175); neighbours N=79, median -0.003, robust sigma 0.010, max +0.111; z = 13.7
- centroid: jump at onset 0.015" +- 0.014 (1.1 sigma, PA 349); largest consecutive-visit jump 0.044"; rms 0.023"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.430, W2-W3 1.812 (W3 S/N 53.4), W3-W4 2.479 (W4 S/N 26.0), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.30, ipd_frac_multi_peak 0, NSS none, Teff 4730 K, logg 4.13, H-alpha pEW -0.156 nm, varclass none; M_G 5.63, -1.73 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): LAMOST J035357.09+350239.1 [*; *,Opt,ev] 0.09" refs=9
- ASAS-SN: 653 points, cameras bA(g,262); bE(g,21); ba(V,168, d=+0.055); bq(g,202); change at onset (after-before, per-camera median) +0.055 mag; largest seasonal dimming 0.07 mag at MJD 59849
- dust: excess flux W1 5.27 mJy, W2 4.63 mJy, T = 1573 K (16-84%: 1441-1732) 

### uid325718  [D2]  SURVIVOR
- position 35.42480 +62.01116; Gaia DR3 513833673802372736; G 13.99, BP-RP 1.39, plx 3.51 mas; plot `plots/uid325718.png`
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 9 visits, 95 points; baseline W1 11.35, W1-W2 0.948; onset between MJD 57986 and 58144
- detector 2: excess 1.011 mag, z 48.7, jitter ratio 7.8
- field control: target step +0.161 (W1 +0.004); neighbours N=199, median -0.006, robust sigma 0.014, max +0.162; z = 11.9
- centroid: jump at onset 0.444" +- 0.185 (2.4 sigma, PA 181); largest consecutive-visit jump 0.331"; rms 0.389"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 1.083, W2-W3 1.507 (W3 S/N 22.3), W3-W4 2.809 (W4 S/N 21.4), ext_flg 1, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.22, ipd_frac_multi_peak 0, NSS none, Teff 4702 K, logg 4.45, H-alpha pEW -0.037 nm, varclass none; M_G 6.71, -0.11 mag vs sequence (on the sequence); neighbours within 10": none
- SIMBAD (10"): no object
- ASAS-SN: 975 points, cameras bD(g,271); bd(V,177, d=+0.004); bs(g,284); bt(g,243); change at onset (after-before, per-camera median) +0.004 mag; largest seasonal dimming 0.02 mag at MJD 60563
- dust: excess flux W1 -0.05 mJy, W2 1.12 mJy, T = 150 K (16-84%: 150-398) W1 excess <= 0: colder than ~150 K (upper limit)

### uid1103309  [D2]  SURVIVOR
- position 92.32085 -15.13572; Gaia DR3 2993153951148830336; G 13.32, BP-RP 1.01, plx 2.83 mas; plot `plots/uid1103309.png`
- flags: AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 2.00 (stored 2.00, reproduced True); dW2 0.179, dW1 0.130, 19 visits, 195 points; baseline W1 10.88, W1-W2 0.758; onset between MJD 60004 and 60213
- detector 2: excess 0.809 mag, z 54.6, jitter ratio 4.5
- field control: target step +0.112 (W1 +0.107); neighbours N=93, median -0.007, robust sigma 0.012, max +0.078; z = 10.0
- centroid: jump at onset 0.022" +- 0.026 (0.8 sigma, PA 82); largest consecutive-visit jump 0.089"; rms 0.038"; toward neighbour: none; expected shift if a neighbour were the source: 2.0" G20.1: 0.19"
- AllWISE 2010: W1-W2 0.743, W2-W3 2.058 (W3 S/N 50.1), W3-W4 1.442 (W4 S/N 17.0), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 0.96, ipd_frac_multi_peak 0, NSS none, Teff 5498 K, logg 4.59, H-alpha pEW 0.028 nm, varclass none; M_G 5.58, +0.04 mag vs sequence (on the sequence); neighbours within 10": 2.0" PA182 G20.10 dG+6.78
- SIMBAD (10"): TIC 408967891 [; ] 0.10" refs=1; 2MASS J06091701-1508085 [*; *,MIR,NIR] 0.10" refs=1; Gaia DR3 2993153951145272192 [*; *] 1.97" refs=1
- ASAS-SN: 1556 points, cameras bA(g,133, d=+0.011); bE(g,224, d=-0.026); ba(V,151); be(V,223); bi(g,403, d=+0.006); bm(g,251, d=-0.018); bq(g,171, d=-0.008); change at onset (after-before, per-camera median) -0.008 mag; largest seasonal dimming 0.04 mag at MJD 57724
- dust: excess flux W1 1.56 mJy, W2 2.22 mJy, T = 911 K (16-84%: 855-976) 

### uid2307394  [D2]  SURVIVOR
- position 196.93752 -56.41976; Gaia DR3 6066471882067153152; G 10.98, BP-RP 0.60, plx 2.28 mas; plot `plots/uid2307394.png`
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | optical dimming +0.091 mag after the infrared onset (debris transit signature) | largest seasonal optical dimming 0.16 mag (MJD 59586)
- NEOWISE: score refetch 1.02 (stored 1.02, reproduced True); dW2 0.103, dW1 0.149, 12 visits, 146 points; baseline W1 9.06, W1-W2 0.151; onset between MJD 58517 and 58881
- detector 2: excess 0.172 mag, z 17.2, jitter ratio 6.3
- field control: target step +0.133 (W1 +0.159); neighbours N=161, median -0.001, robust sigma 0.015, max +0.062; z = 9.0
- centroid: jump at onset 0.097" +- 0.092 (1.1 sigma, PA 13); largest consecutive-visit jump 0.200"; rms 0.104"; toward neighbour: 5.0" PA18 G16.9 (angle 5 deg); 6.2" PA39 G20.2 (angle 26 deg); expected shift if a neighbour were the source: 2.8" G14.9: 0.32"; 5.0" G16.9: 0.57"; 5.5" G19.7: 0.63"; 6.2" G20.2: 0.71"; 8.7" G20.8: 1.00"; 9.0" G20.2: 1.04"; 9.2" G18.0: 1.06"; 9.3" G20.1: 1.07"
- AllWISE 2010: W1-W2 0.189, W2-W3 0.355 (W3 S/N 49.5), W3-W4 0.491 (W4 S/N 6.0), ext_flg 1, ph_qual AAAB: photosphere-like (W2-W3 < 0.5)
- Gaia: RUWE 1.19, ipd_frac_multi_peak 0, NSS none, Teff 7015 K, logg 4.02, H-alpha pEW 0.282 nm, varclass none; M_G 2.77, -0.60 mag vs sequence (on the sequence); neighbours within 10": 2.8" PA75 G14.85 dG+3.87; 5.0" PA18 G16.88 dG+5.90; 5.5" PA268 G19.66 dG+8.68; 6.2" PA39 G20.15 dG+9.17; 8.7" PA327 G20.81 dG+9.83; 9.0" PA294 G20.15 dG+9.17; 9.2" PA100 G17.97 dG+6.99; 9.3" PA174 G20.07 dG+9.09
- SIMBAD (10"): TYC 8657-2183-1 [*; *,NIR] 0.24" refs=4
- ASAS-SN: 915 points, cameras bH(g,332, d=+0.147); bl(g,402, d=+0.091); bp(g,181, d=+0.073); change at onset (after-before, per-camera median) +0.091 mag; largest seasonal dimming 0.16 mag at MJD 59586
- dust: excess flux W1 13.97 mJy, W2 3.77 mJy, T = 8000 K (16-84%: 8000-8000) ratio bluer than an 8000 K blackbody (not dust-like)

### uid2105741  [D2]  SURVIVOR
- position 1.27252 +59.65045; Gaia DR3 423255218711266176; G 14.15, BP-RP 1.65, plx 2.35 mas; plot `plots/uid2105741.png`
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | 1.49 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | possible optical brightening at onset (-0.218 mag, one camera only) | largest seasonal optical dimming 0.53 mag (MJD 60638)
- NEOWISE: score refetch 1.27 (stored 1.27, reproduced True); dW2 0.333, dW1 0.271, 16 visits, 168 points; baseline W1 9.17, W1-W2 0.512; onset between MJD 57405 and 57598
- detector 2: excess 0.561 mag, z 20.5, jitter ratio 19.3
- field control: target step +0.088 (W1 +0.107); neighbours N=196, median -0.003, robust sigma 0.012, max +0.026; z = 7.4
- centroid: jump at onset 0.021" +- 0.026 (0.8 sigma, PA 340); largest consecutive-visit jump 0.046"; rms 0.035"; toward neighbour: none; expected shift if a neighbour were the source: 1.5" G18.4: 0.11"; 9.0" G20.3: 0.70"
- AllWISE 2010: W1-W2 0.765, W2-W3 1.870 (W3 S/N 69.1), W3-W4 2.739 (W4 S/N 43.7), ext_flg 1, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.36, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW -0.174 nm, varclass none; M_G 6.00, -1.49 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 1.5" PA130 G18.35 dG+4.21; 9.0" PA48 G20.25 dG+6.11
- SIMBAD (10"): V* V956 Cas [V*; *,NIR,V*] 0.11" refs=6
- ASAS-SN: 638 points, cameras bB(g,112); bb(V,191, d=-0.218); br(g,260); cB(g,75); change at onset (after-before, per-camera median) -0.218 mag; largest seasonal dimming 0.53 mag at MJD 60638
- dust: excess flux W1 17.16 mJy, W2 15.18 mJy, T = 1557 K (16-84%: 1454-1677) 

### uid137313  [D2]  SURVIVOR
- position 330.31742 -28.50241; Gaia DR3 6617669842852419712; G 13.04, BP-RP 1.06, plx 3.77 mas; plot `plots/uid137313.png`
- flags: AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 1.49 (stored 1.49, reproduced True); dW2 0.135, dW1 0.090, 17 visits, 127 points; baseline W1 11.02, W1-W2 0.217; onset between MJD 57885 and 58052
- detector 2: excess 0.271 mag, z 17.0, jitter ratio 7.0
- field control: target step +0.112 (W1 +0.058); neighbours N=29, median -0.007, robust sigma 0.019, max +0.040; z = 6.4
- centroid: jump at onset 0.025" +- 0.017 (1.4 sigma, PA 216); largest consecutive-visit jump 0.087"; rms 0.031"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.276, W2-W3 2.526 (W3 S/N 52.3), W3-W4 0.685 (W4 S/N 6.7), ext_flg 0, ph_qual AAAB: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.05, ipd_frac_multi_peak 0, NSS none, Teff 5113 K, logg 4.58, H-alpha pEW 0.009 nm, varclass SOLAR_LIKE(0.42); M_G 5.92, +0.15 mag vs sequence (on the sequence); neighbours within 10": none
- SIMBAD (10"): UCAC4 308-275485 [*; *,NIR] 0.24" refs=4
- ASAS-SN: 1157 points, cameras bE(g,256); be(V,244, d=-0.004); bi(g,275); bm(g,229); bq(g,153); change at onset (after-before, per-camera median) -0.004 mag; largest seasonal dimming 0.02 mag at MJD 59848
- dust: excess flux W1 0.69 mJy, W2 0.67 mJy, T = 1377 K (16-84%: 1139-1747) 

### uid2013931  [D2]  SURVIVOR
- position 94.49329 -10.03932; Gaia DR3 3004530769758177280; G 13.00, BP-RP 0.90, plx 2.38 mas; plot `plots/uid2013931.png`
- flags: AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 0.74 (stored 0.74, reproduced True); dW2 0.030, dW1 0.017, 21 visits, 191 points; baseline W1 11.11, W1-W2 0.584; onset between MJD 57099 and 57293
- detector 2: excess 0.629 mag, z 49.4, jitter ratio 3.6
- field control: target step +0.039 (W1 +0.005); neighbours N=89, median -0.006, robust sigma 0.010, max +0.034; z = 4.8
- centroid: jump at onset 0.025" +- 0.028 (0.9 sigma, PA 97); largest consecutive-visit jump 0.061"; rms 0.036"; toward neighbour: none; expected shift if a neighbour were the source: 8.1" G17.8: 0.29"
- AllWISE 2010: W1-W2 0.639, W2-W3 3.457 (W3 S/N 59.1), W3-W4 1.822 (W4 S/N 30.8), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 0.97, ipd_frac_multi_peak 0, NSS none, Teff 5722 K, logg 4.38, H-alpha pEW -0.757 nm, varclass none; M_G 4.88, -0.14 mag vs sequence (on the sequence); neighbours within 10": 8.1" PA4 G17.76 dG+4.77
- SIMBAD (10"): Gaia DR3 3004530769758177280 [*; *] 0.10" refs=1
- ASAS-SN: 1632 points, cameras bC(g,150); bG(g,273); bc(V,148, d=-0.005); be(V,46, d=-0.017); bg(V,183); bk(g,381); bo(g,274); bs(g,177); change at onset (after-before, per-camera median) -0.011 mag; largest seasonal dimming 0.05 mag at MJD 59536
- dust: excess flux W1 0.71 mJy, W2 0.73 mJy, T = 1262 K (16-84%: 1059-1561) 

### uid342028  [D2]  SURVIVOR
- position 225.72799 -14.21404; Gaia DR3 6308812594204740352; G 12.51, BP-RP 1.08, plx 3.49 mas; plot `plots/uid342028.png`
- flags: AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 21 visits, 163 points; baseline W1 10.23, W1-W2 0.430; onset between MJD 59779 and 59981
- detector 2: excess 0.485 mag, z 29.6, jitter ratio 4.7
- field control: target step +0.058 (W1 +0.029); neighbours N=35, median -0.003, robust sigma 0.013, max +0.032; z = 4.6
- centroid: jump at onset 0.007" +- 0.013 (0.5 sigma, PA 239); largest consecutive-visit jump 0.046"; rms 0.026"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.429, W2-W3 1.517 (W3 S/N 50.4), W3-W4 0.921 (W4 S/N 8.5), ext_flg 0, ph_qual AAAB: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.37, ipd_frac_multi_peak 0, NSS none, Teff 5461 K, logg 4.47, H-alpha pEW 0.105 nm, varclass none; M_G 5.22, -0.59 mag vs sequence (on the sequence); neighbours within 10": none
- SIMBAD (10"): UCAC4 379-068655 [*; *,MIR,NIR] 0.20" refs=1
- ASAS-SN: 1152 points, cameras bB(g,76); bF(g,124, d=-0.001); bb(V,111); bf(V,138); bj(g,281, d=+0.010); bn(g,230, d=-0.001); br(g,145, d=+0.006); cB(g,47); change at onset (after-before, per-camera median) +0.002 mag; largest seasonal dimming 0.00 mag at MJD 59039
- dust: excess flux W1 -0.14 mJy, W2 -0.01 mJy, T = n/a K (16-84%: n/a-n/a) no W2 excess flux after onset

### uid2186439  [D2]  SURVIVOR
- position 265.27899 -29.16242; Gaia DR3 4057141904419772544; G 13.63, BP-RP 1.24, plx 2.32 mas; plot `plots/uid2186439.png`
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | 0.91 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 0.39 (stored 0.39, reproduced True); dW2 0.025, dW1 0.013, 15 visits, 107 points; baseline W1 8.23, W1-W2 0.320; onset between MJD 57463 and 57634
- detector 2: excess 0.381 mag, z 19.8, jitter ratio 4.8
- field control: target step +0.082 (W1 +0.021); neighbours N=145, median -0.011, robust sigma 0.027, max +0.102; z = 3.5
- centroid: jump at onset 0.147" +- 0.061 (2.4 sigma, PA 256); largest consecutive-visit jump 0.204"; rms 0.120"; toward neighbour: none; expected shift if a neighbour were the source: 8.3" G21.1: 0.60"
- AllWISE 2010: W1-W2 0.296, W2-W3 1.211 (W3 S/N 45.2), W3-W4 1.449 (W4 S/N 18.2), ext_flg 1, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.03, ipd_frac_multi_peak 0, NSS none, Teff 5855 K, logg 4.38, H-alpha pEW 0.085 nm, varclass none; M_G 5.46, -0.91 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 8.3" PA113 G21.08 dG+7.45
- SIMBAD (10"): no object
- ASAS-SN: 1007 points, cameras bF(g,250); bf(V,194, d=-0.003); bj(g,242); bn(g,162); br(g,159); change at onset (after-before, per-camera median) -0.003 mag; largest seasonal dimming 0.01 mag at MJD 60229
- dust: excess flux W1 3.10 mJy, W2 0.05 mJy, T = 8000 K (16-84%: 8000-8000) ratio bluer than an 8000 K blackbody (not dust-like)

### uid2269181  [D2]  SURVIVOR
- position 140.82810 -43.96709; Gaia DR3 5424133817529850624; G 12.84, BP-RP 0.82, plx 2.29 mas; plot `plots/uid2269181.png`
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | Gaia ipd_frac_multi_peak 15% (resolved double?) | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 20 visits, 189 points; baseline W1 10.61, W1-W2 0.361; onset between MJD 58094 and 58253
- detector 2: excess 0.400 mag, z 38.5, jitter ratio 5.1
- field control: target step +0.033 (W1 +0.053); neighbours N=203, median -0.003, robust sigma 0.013, max +0.040; z = 2.9
- centroid: jump at onset 0.050" +- 0.019 (2.6 sigma, PA 88); largest consecutive-visit jump 0.077"; rms 0.035"; toward neighbour: none; expected shift if a neighbour were the source: 1.3" G16.6: 0.04"; 5.9" G16.9: 0.18"
- AllWISE 2010: W1-W2 0.375, W2-W3 2.701 (W3 S/N 65.0), W3-W4 2.243 (W4 S/N 35.1), ext_flg 1, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.08, ipd_frac_multi_peak 15, NSS none, Teff 5604 K, logg 4.38, H-alpha pEW -0.015 nm, varclass none; M_G 4.65, +0.07 mag vs sequence (on the sequence); neighbours within 10": 1.3" PA187 G16.57 dG+3.72; 5.9" PA244 G16.91 dG+4.07
- SIMBAD (10"): no object
- ASAS-SN: 2234 points, cameras bE(g,367); bG(g,362); be(V,180, d=-0.006); bg(V,157, d=-0.009); bi(g,403); bk(g,371); bm(g,179); bo(g,215); change at onset (after-before, per-camera median) -0.008 mag; largest seasonal dimming 0.03 mag at MJD 60374
- dust: excess flux W1 -0.05 mJy, W2 -0.40 mJy, T = n/a K (16-84%: n/a-n/a) no W2 excess flux after onset

### uid2139690  [D2]  SURVIVOR
- position 267.52173 -26.40527; Gaia DR3 4066818942476619520; G 13.02, BP-RP 1.04, plx 2.34 mas; plot `plots/uid2139690.png`
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | 0.82 mag above the main sequence at its colour
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 11 visits, 99 points; baseline W1 9.20, W1-W2 0.183; onset between MJD 60023 and 60387
- detector 2: excess 0.236 mag, z 15.3, jitter ratio 4.4
- field control: target step +0.099 (W1 +0.089); neighbours N=74, median +0.011, robust sigma 0.033, max +0.100; z = 2.6
- centroid: jump at onset 0.056" +- 0.061 (0.9 sigma, PA 286); largest consecutive-visit jump 0.234"; rms 0.135"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.131, W2-W3 -0.056 (W3 S/N 5.5), W3-W4 1.175 (W4 S/N -0.6), ext_flg 1, ph_qual AABU: photosphere-like (W2-W3 < 0.5)
- Gaia: RUWE 0.81, ipd_frac_multi_peak 0, NSS none, Teff 6005 K, logg 4.29, H-alpha pEW 0.189 nm, varclass SOLAR_LIKE(0.18); M_G 4.87, -0.82 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): no object
- ASAS-SN: 823 points, cameras bH(g,257, d=-0.000); bl(g,249, d=+0.005); bp(g,166, d=+0.024); bt(g,151, d=+0.007); change at onset (after-before, per-camera median) +0.006 mag; largest seasonal dimming 0.01 mag at MJD 59129
- dust: excess flux W1 4.90 mJy, W2 2.20 mJy, T = 8000 K (16-84%: 2294-8000) ratio bluer than an 8000 K blackbody (not dust-like)

### uid220308  [D2]  SURVIVOR
- position 274.26638 +64.56526; Gaia DR3 2161325369818713984; G 11.45, BP-RP 0.71, plx 3.65 mas; plot `plots/uid220308.png`
- flags: AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 0.99 (stored 0.99, reproduced True); dW2 0.146, dW1 0.078, 20 visits, 2456 points; baseline W1 9.67, W1-W2 0.576; onset between MJD 57143 and 57325
- detector 2: excess 0.606 mag, z 60.6, jitter ratio 3.9
- field control: target step +0.002 (W1 -0.001); neighbours N=39, median -0.009, robust sigma 0.005, max +0.002; z = 2.1
- centroid: jump at onset 0.010" +- 0.014 (0.7 sigma, PA 142); largest consecutive-visit jump 0.055"; rms 0.022"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.585, W2-W3 2.610 (W3 S/N 72.2), W3-W4 0.675 (W4 S/N 33.7), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 0.74, ipd_frac_multi_peak 1, NSS none, Teff 6006 K, logg 4.35, H-alpha pEW 0.177 nm, varclass none; M_G 4.26, +0.29 mag vs sequence (on the sequence); neighbours within 10": none
- SIMBAD (10"): TYC 4209-1322-1 [*; *,MIR,NIR] 0.20" refs=6
- ASAS-SN: 752 points, cameras bB(g,167); bb(V,264, d=+0.003); br(g,291); cB(g,30); change at onset (after-before, per-camera median) +0.003 mag; largest seasonal dimming 0.01 mag at MJD 60404
- dust: excess flux W1 3.37 mJy, W2 6.08 mJy, T = 763 K (16-84%: 714-816) 

### uid1514307  [D2]  SURVIVOR
- position 268.18821 -26.91458; Gaia DR3 4063771822109869184; G 15.80, BP-RP 1.49, plx 2.60 mas; plot `plots/uid1514307.png`
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association)
- NEOWISE: score refetch 0.25 (stored 0.25, reproduced True); dW2 0.016, dW1 0.067, 13 visits, 101 points; baseline W1 8.71, W1-W2 0.391; onset between MJD 58561 and 58928
- detector 2: excess 0.451 mag, z 19.8, jitter ratio 5.9
- field control: target step +0.072 (W1 +0.070); neighbours N=110, median +0.007, robust sigma 0.032, max +0.104; z = 2.1
- centroid: jump at onset 0.127" +- 0.107 (1.2 sigma, PA 51); largest consecutive-visit jump 0.291"; rms 0.166"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.418, W2-W3 -0.077 (W3 S/N 19.5), W3-W4 1.104 (W4 S/N 4.8), ext_flg 1, ph_qual AAAB: photosphere-like (W2-W3 < 0.5)
- Gaia: RUWE 0.95, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW -0.061 nm, varclass none; M_G 7.87, +0.79 mag vs sequence (below the sequence); neighbours within 10": none
- SIMBAD (10"): no object
- ASAS-SN: 0 points, cameras n/a; change at onset (after-before, per-camera median) n/a mag; largest seasonal dimming n/a mag at MJD n/a
- dust: excess flux W1 3.36 mJy, W2 1.20 mJy, T = 8000 K (16-84%: 430-8000) ratio bluer than an 8000 K blackbody (not dust-like)
- checks missing: ASAS-SN (no source)

### uid1599936  [D2]  SURVIVOR
- position 263.44908 -32.48313; Gaia DR3 4054634399450679552; G 15.07, BP-RP 1.66, plx 2.56 mas; plot `plots/uid1599936.png`
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association)
- NEOWISE: score refetch 0.10 (stored 0.10, reproduced True); dW2 0.006, dW1 0.012, 9 visits, 87 points; baseline W1 10.22, W1-W2 0.468; onset between MJD 56733 and 57274
- detector 2: excess 0.516 mag, z 18.7, jitter ratio 4.0
- field control: target step +0.056 (W1 -0.026); neighbours N=84, median +0.026, robust sigma 0.034, max +0.149; z = 0.9
- centroid: jump at onset 0.101" +- 0.093 (1.1 sigma, PA 282); largest consecutive-visit jump 0.114"; rms 0.095"; toward neighbour: none; expected shift if a neighbour were the source: 1.1" G18.1: 0.06"
- AllWISE 2010: W1-W2 0.470, W2-W3 0.684 (W3 S/N -2.7), W3-W4 2.320 (W4 S/N -2.0), ext_flg 1, ph_qual AAUU: W3 S/N < 5: no W2-W3 class; W1-W2 > 0.25
- Gaia: RUWE 1.06, ipd_frac_multi_peak 3, NSS none, Teff 4495 K, logg 4.52, H-alpha pEW -0.087 nm, varclass none; M_G 7.11, -0.41 mag vs sequence (on the sequence); neighbours within 10": 1.1" PA171 G18.14 dG+3.07
- SIMBAD (10"): no object
- ASAS-SN: 957 points, cameras bH(g,321); bh(V,174); bl(g,298); bp(g,164); change at onset (after-before, per-camera median) n/a mag; largest seasonal dimming 0.04 mag at MJD 60230
- dust: excess flux W1 -0.60 mJy, W2 0.46 mJy, T = 150 K (16-84%: 150-150) W1 excess <= 0: colder than ~150 K (upper limit)
- checks missing: ASAS-SN change at onset (no camera spans the onset)

### uid838651  [D2]  SURVIVOR
- position 223.47277 -34.35772; Gaia DR3 6202580185915202560; G 13.45, BP-RP 1.13, plx 3.02 mas; plot `plots/uid838651.png`
- flags: AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 18 visits, 136 points; baseline W1 11.23, W1-W2 0.254; onset between MJD 57959 and 58161
- detector 2: excess 0.311 mag, z 17.5, jitter ratio 3.5
- field control: target step +0.009 (W1 +0.002); neighbours N=73, median -0.003, robust sigma 0.019, max +0.050; z = 0.6
- centroid: jump at onset 0.045" +- 0.020 (2.3 sigma, PA 4); largest consecutive-visit jump 0.049"; rms 0.028"; toward neighbour: none; expected shift if a neighbour were the source: 4.2" G20.8: 0.03"
- AllWISE 2010: W1-W2 0.262, W2-W3 2.049 (W3 S/N 33.2), W3-W4 1.104 (W4 S/N 5.9), ext_flg 0, ph_qual AAAB: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.04, ipd_frac_multi_peak 0, NSS none, Teff 5078 K, logg 4.53, H-alpha pEW 0.016 nm, varclass SOLAR_LIKE(0.33); M_G 5.85, -0.15 mag vs sequence (on the sequence); neighbours within 10": 4.2" PA87 G20.79 dG+7.34
- SIMBAD (10"): no object
- ASAS-SN: 1269 points, cameras bH(g,335); bf(V,85); bh(V,171, d=+0.004); bl(g,388); bp(g,290); change at onset (after-before, per-camera median) +0.004 mag; largest seasonal dimming 0.02 mag at MJD 58728
- dust: excess flux W1 0.02 mJy, W2 0.02 mJy, T = 1051 K (16-84%: 150-8000) 

### uid1710168  [D2]  SURVIVOR
- position 265.70295 -30.71245; Gaia DR3 4056699174891037568; G 12.17, BP-RP 0.89, plx 2.51 mas; plot `plots/uid1710168.png`
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | 0.79 mag above the main sequence at its colour
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 17 visits, 121 points; baseline W1 9.39, W1-W2 0.234; onset between MJD 59454 and 59655
- detector 2: excess 0.278 mag, z 22.5, jitter ratio 4.7
- field control: target step -0.013 (W1 -0.036); neighbours N=115, median -0.003, robust sigma 0.028, max +0.092; z = -0.4
- centroid: jump at onset 0.072" +- 0.062 (1.2 sigma, PA 23); largest consecutive-visit jump 0.198"; rms 0.103"; toward neighbour: 1.6" PA37 G18.6 (angle 14 deg); expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.225, W2-W3 -0.032 (W3 S/N 2.7), W3-W4 2.883 (W4 S/N -0.9), ext_flg 1, ph_qual AACU: W3 S/N < 5: no W2-W3 class
- Gaia: RUWE 0.87, ipd_frac_multi_peak 0, NSS none, Teff 6503 K, logg 4.13, H-alpha pEW 0.197 nm, varclass none; M_G 4.17, -0.79 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 1.6" PA37 G18.64 dG+6.47; 6.2" PA269 G20.06 dG+7.89
- SIMBAD (10"): no object
- ASAS-SN: 984 points, cameras bF(g,249, d=-0.002); bf(V,180); bj(g,239, d=-0.006); bn(g,163, d=+0.008); br(g,153, d=-0.004); change at onset (after-before, per-camera median) -0.003 mag; largest seasonal dimming 0.01 mag at MJD 58231
- dust: excess flux W1 -1.24 mJy, W2 -0.17 mJy, T = n/a K (16-84%: n/a-n/a) no W2 excess flux after onset

### uid1471333  [D2]  SURVIVOR
- position 111.14968 -44.66924; Gaia DR3 5511851313304664704; G 15.63, BP-RP 1.96, plx 2.62 mas; plot `plots/uid1471333.png`
- flags: AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | not plain dust: optical brightening -0.156 mag (per-camera -0.158,-0.173,-0.155,-0.080,-0.202,-0.122) together with the infrared rise | largest seasonal optical dimming 0.26 mag (MJD 58512)
- NEOWISE: score refetch 2.40 (stored 2.40, reproduced True); dW2 0.299, dW1 0.232, 10 visits, 123 points; baseline W1 9.62, W1-W2 0.583; onset between MJD 58579 and 59310
- detector 2: excess 0.585 mag, z 14.2, jitter ratio 11.7
- field control: target step -0.052 (W1 -0.051); neighbours N=93, median -0.002, robust sigma 0.008, max +0.326; z = -6.2
- centroid: jump at onset 0.506" +- 0.307 (1.6 sigma, PA 109); largest consecutive-visit jump 0.994"; rms 0.329"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.661, W2-W3 2.410 (W3 S/N 62.2), W3-W4 2.177 (W4 S/N 30.0), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.11, ipd_frac_multi_peak 0, NSS none, Teff 3555 K, logg 4.16, H-alpha pEW -2.334 nm, varclass none; M_G 7.72, -0.62 mag vs sequence (on the sequence); neighbours within 10": 7.1" PA331 G17.38 dG+1.75
- SIMBAD (10"): Gaia DR3 5511851313304664704 [*; *] 0.19" refs=1; Gaia DR3 5511851309005446528 [*; *] 6.95" refs=1
- ASAS-SN: 2533 points, cameras bE(g,364, d=-0.158); bF(g,354, d=-0.173); be(V,282); bf(V,215); bi(g,412, d=-0.155); bj(g,400, d=-0.080); bm(g,340, d=-0.202); bn(g,166, d=-0.122); change at onset (after-before, per-camera median) -0.156 mag; largest seasonal dimming 0.26 mag at MJD 58512
- dust: excess flux W1 13.06 mJy, W2 12.96 mJy, T = 1318 K (16-84%: 1173-1518) 

## Known/likely young stars (detector 2) (138)

### uid1355017  [D2]  YOUNG
- position 313.27661 +74.84301; Gaia DR3 2277845423082083200; G 11.98, BP-RP 1.36, plx 2.68 mas; plot `plots/uid1355017.png`
- **young:** SIMBAD young-star types Or*,Y*O (GSC 04472-00143) | Gaia DR3 variability class YSO(0.38)
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | 2.62 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 3.26 (stored 3.26, reproduced True); dW2 1.508, dW1 1.573, 21 visits, 554 points; baseline W1 9.19, W1-W2 0.519; onset between MJD 58137 and 58343
- detector 2: excess 0.582 mag, z 28.6, jitter ratio 11.2
- field control: target step +1.577 (W1 +1.570); neighbours N=65, median -0.004, robust sigma 0.009, max +0.027; z = 177.8
- centroid: jump at onset 0.011" +- 0.020 (0.6 sigma, PA 52); largest consecutive-visit jump 0.088"; rms 0.030"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.538, W2-W3 2.490 (W3 S/N 76.6), W3-W4 2.382 (W4 S/N 54.9), ext_flg 1, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.21, ipd_frac_multi_peak 0, NSS none, Teff 5584 K, logg 4.01, H-alpha pEW 0.000 nm, varclass YSO(0.38); M_G 4.12, -2.62 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): GSC 04472-00143 [Or*; *,IR,NIR,Or*,Y*O] 0.09" refs=10
- ASAS-SN: 735 points, cameras bB(g,175); bb(V,240, d=+0.013); br(g,284, d=+0.034); cB(g,36); change at onset (after-before, per-camera median) +0.024 mag; largest seasonal dimming 0.08 mag at MJD 57515
- dust: excess flux W1 219.95 mJy, W2 185.41 mJy, T = 1687 K (16-84%: 1657-1719) 

### uid1180376  [D2]  YOUNG
- position 84.37897 -2.39523; Gaia DR3 3216133053832757632; G 15.43, BP-RP 1.89, plx 2.78 mas; plot `plots/uid1180376.png`
- **young:** SIMBAD young-star types TT*,Y*O (Haro 5-5)
- flags: AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | not plain dust: optical brightening -0.592 mag (per-camera -0.657,-0.810,-0.592,+0.006,-0.467) together with the infrared rise | largest seasonal optical dimming 0.50 mag (MJD 59436)
- NEOWISE: score refetch 4.11 (stored 4.11, reproduced True); dW2 0.528, dW1 0.521, 21 visits, 213 points; baseline W1 11.19, W1-W2 0.589; onset between MJD 59473 and 59631
- detector 2: excess 0.604 mag, z 15.5, jitter ratio 11.9
- field control: target step +1.361 (W1 +1.291); neighbours N=81, median +0.000, robust sigma 0.013, max +0.144; z = 102.0
- centroid: jump at onset 0.017" +- 0.020 (0.9 sigma, PA 130); largest consecutive-visit jump 0.109"; rms 0.037"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.548, W2-W3 2.535 (W3 S/N 55.9), W3-W4 2.286 (W4 S/N 26.9), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.14, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW -4.207 nm, varclass none; M_G 7.65, -0.51 mag vs sequence (on the sequence); neighbours within 10": none
- SIMBAD (10"): Haro 5-5 [TT*; *,Em*,NIR,TT*,Y*O] 0.04" refs=32
- ASAS-SN: 1361 points, cameras bC(g,144, d=-0.657); bG(g,211, d=-0.810); ba(V,48); bc(V,148); be(V,37); bg(V,143); bk(g,295, d=-0.592); bo(g,185, d=+0.006); bs(g,150, d=-0.467); change at onset (after-before, per-camera median) -0.592 mag; largest seasonal dimming 0.50 mag at MJD 59436
- dust: excess flux W1 8.71 mJy, W2 9.07 mJy, T = 1242 K (16-84%: 1205-1281) 

### uid984129  [D2]  YOUNG
- position 82.83596 -0.82218; Gaia DR3 3220661529910667904; G 14.53, BP-RP 1.49, plx 2.91 mas; plot `plots/uid984129.png`
- **young:** SIMBAD young-star types Or*,TT*,Y*O (Kiso A-0904   1)
- flags: AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | not plain dust: optical brightening -0.256 mag (per-camera -0.256,-0.305,-0.200) together with the infrared rise | largest seasonal optical dimming 0.24 mag (MJD 56900)
- NEOWISE: score refetch 1.08 (stored 1.08, reproduced True); dW2 0.340, dW1 0.340, 21 visits, 217 points; baseline W1 9.73, W1-W2 0.628; onset between MJD 57645 and 57810
- detector 2: excess 0.688 mag, z 30.3, jitter ratio 28.9
- field control: target step +0.796 (W1 +0.789); neighbours N=66, median -0.002, robust sigma 0.009, max +0.046; z = 86.1
- centroid: jump at onset 0.014" +- 0.015 (1.0 sigma, PA 91); largest consecutive-visit jump 0.037"; rms 0.027"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.654, W2-W3 1.750 (W3 S/N 29.1), W3-W4 2.277 (W4 S/N 20.6), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.31, ipd_frac_multi_peak 0, NSS none, Teff 5746 K, logg 4.61, H-alpha pEW -5.060 nm, varclass none; M_G 6.85, -0.23 mag vs sequence (on the sequence); neighbours within 10": none
- SIMBAD (10"): Kiso A-0904   1 [TT*; *,Em*,NIR,Or*,Pe*,TT*,Y*O] 0.03" refs=38
- ASAS-SN: 1625 points, cameras bC(g,151); bG(g,222); ba(V,51); bc(V,150, d=-0.256); bd(V,154, d=-0.305); be(V,38); bf(V,33); bg(V,152, d=-0.200); bk(g,287); bo(g,228); bs(g,159); change at onset (after-before, per-camera median) -0.256 mag; largest seasonal dimming 0.24 mag at MJD 56900
- dust: excess flux W1 23.84 mJy, W2 24.66 mJy, T = 1252 K (16-84%: 1208-1298) 

### uid1494934  [D2]  YOUNG
- position 117.33987 -34.72304; Gaia DR3 5593758469946214656; G 14.44, BP-RP 1.89, plx 2.61 mas; plot `plots/uid1494934.png`
- **young:** Gaia DR3 variability class YSO(0.34)
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | 1.63 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | optical dimming +0.216 mag after the infrared onset (debris transit signature) | largest seasonal optical dimming 0.36 mag (MJD 57448)
- NEOWISE: score refetch 2.67 (stored 2.67, reproduced True); dW2 0.697, dW1 0.708, 13 visits, 127 points; baseline W1 9.88, W1-W2 0.760; onset between MJD 57856 and 58059
- detector 2: excess 0.775 mag, z 19.8, jitter ratio 20.5
- field control: target step +0.843 (W1 +0.722); neighbours N=170, median -0.007, robust sigma 0.013, max +0.029; z = 63.7
- centroid: jump at onset 0.044" +- 0.030 (1.5 sigma, PA 35); largest consecutive-visit jump 0.053"; rms 0.038"; toward neighbour: none; expected shift if a neighbour were the source: 8.2" G19.2: 4.42"
- AllWISE 2010: W1-W2 0.699, W2-W3 1.971 (W3 S/N 71.6), W3-W4 1.717 (W4 S/N 37.4), ext_flg 1, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.23, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW -1.688 nm, varclass YSO(0.34); M_G 6.52, -1.63 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 8.2" PA122 G19.22 dG+4.78
- SIMBAD (10"): 2MASS J07492157-3443230 [LP?; *,LP?,MIR,NIR] 0.18" refs=2
- ASAS-SN: 1007 points, cameras bG(g,178); bg(V,229, d=+0.216); bk(g,418); bo(g,182); change at onset (after-before, per-camera median) +0.216 mag; largest seasonal dimming 0.36 mag at MJD 57448
- dust: excess flux W1 32.87 mJy, W2 37.23 mJy, T = 1129 K (16-84%: 1098-1163) 

### uid532798  [D2]  YOUNG
- position 79.82666 -5.72572; Gaia DR3 3208462482760921088; G 13.77, BP-RP 1.57, plx 3.28 mas; plot `plots/uid532798.png`
- **young:** SIMBAD young-star types TT*,Y*?,Y*O (Kiso A-0975  47)
- flags: 0.94 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.36 mag (MJD 60639)
- NEOWISE: score refetch 3.33 (stored 3.33, reproduced True); dW2 0.382, dW1 0.349, 20 visits, 222 points; baseline W1 9.42, W1-W2 0.426; onset between MJD 57807 and 58006
- detector 2: excess 0.481 mag, z 19.1, jitter ratio 11.2
- field control: target step +0.512 (W1 +0.427); neighbours N=43, median -0.001, robust sigma 0.008, max +0.333; z = 62.9
- centroid: jump at onset 0.024" +- 0.016 (1.5 sigma, PA 300); largest consecutive-visit jump 0.052"; rms 0.027"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.500, W2-W3 1.644 (W3 S/N 61.6), W3-W4 2.119 (W4 S/N 38.5), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.14, ipd_frac_multi_peak 0, NSS none, Teff 5850 K, logg 4.39, H-alpha pEW -2.380 nm, varclass none; M_G 6.36, -0.94 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): Kiso A-0975  47 [TT*; *,Em*,NIR,Opt,TT*,Y*?,Y*O] 0.05" refs=8
- ASAS-SN: 1303 points, cameras bB(g,85); bF(g,205); bb(V,155, d=+0.003); bf(V,171, d=-0.307); bj(g,280); bn(g,237); br(g,170); change at onset (after-before, per-camera median) -0.152 mag; largest seasonal dimming 0.36 mag at MJD 60639
- dust: excess flux W1 18.56 mJy, W2 19.39 mJy, T = 1237 K (16-84%: 1193-1284) 

### uid1048217  [D2]  YOUNG
- position 81.44487 +0.54828; Gaia DR3 3221844226465235712; G 14.20, BP-RP 1.79, plx 2.87 mas; plot `plots/uid1048217.png`
- **young:** SIMBAD young-star types Y*?,Y*O (UCAC4 453-010343)
- flags: 1.40 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | possible optical brightening at onset (-0.049 mag, one camera only) | largest seasonal optical dimming 0.27 mag (MJD 58182)
- NEOWISE: score refetch 1.59 (stored 1.59, reproduced True); dW2 0.919, dW1 0.692, 20 visits, 184 points; baseline W1 10.29, W1-W2 0.793; onset between MJD 57086 and 57280
- detector 2: excess 0.824 mag, z 24.4, jitter ratio 13.0
- field control: target step +0.612 (W1 +0.452); neighbours N=61, median -0.005, robust sigma 0.011, max +0.018; z = 55.5
- centroid: jump at onset 0.023" +- 0.019 (1.2 sigma, PA 274); largest consecutive-visit jump 0.095"; rms 0.038"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.778, W2-W3 2.477 (W3 S/N 73.7), W3-W4 2.487 (W4 S/N 43.5), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.08, ipd_frac_multi_peak 0, NSS none, Teff 4458 K, logg 4.29, H-alpha pEW -0.092 nm, varclass none; M_G 6.49, -1.40 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): UCAC4 453-010343 [Y*O; *,MIR,NIR,Y*?,Y*O] 0.02" refs=19
- ASAS-SN: 927 points, cameras bA(g,166); bE(g,69); ba(V,208, d=-0.049); be(V,56); bi(g,172); bm(g,158); bq(g,98); change at onset (after-before, per-camera median) -0.049 mag; largest seasonal dimming 0.27 mag at MJD 58182
- dust: excess flux W1 13.34 mJy, W2 22.40 mJy, T = 803 K (16-84%: 792-814) 

### uid1785863  [D2]  YOUNG
- position 85.37306 +9.12232; Gaia DR3 3336143197519784064; G 13.00, BP-RP 1.51, plx 2.48 mas; plot `plots/uid1785863.png`
- **young:** SIMBAD young-star types Y*?,Y*O (V* V515 Ori)
- flags: 2.14 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | optical dimming +0.663 mag after the infrared onset (debris transit signature) | largest seasonal optical dimming 0.66 mag (MJD 59854)
- NEOWISE: score refetch 1.51 (stored 1.51, reproduced True); dW2 0.500, dW1 0.317, 21 visits, 216 points; baseline W1 9.73, W1-W2 0.483; onset between MJD 59475 and 59633
- detector 2: excess 0.542 mag, z 23.4, jitter ratio 22.9
- field control: target step +0.717 (W1 +0.443); neighbours N=84, median +0.007, robust sigma 0.013, max +0.077; z = 54.7
- centroid: jump at onset 0.032" +- 0.024 (1.3 sigma, PA 232); largest consecutive-visit jump 0.094"; rms 0.041"; toward neighbour: 7.8" PA217 G21.0 (angle 15 deg); expected shift if a neighbour were the source: 4.5" G17.6: 2.15"; 7.8" G21.0: 3.75"
- AllWISE 2010: W1-W2 0.508, W2-W3 2.065 (W3 S/N 63.9), W3-W4 1.736 (W4 S/N 31.7), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.15, ipd_frac_multi_peak 0, NSS none, Teff 5818 K, logg 3.90, H-alpha pEW -0.592 nm, varclass none; M_G 4.97, -2.14 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 4.5" PA91 G17.62 dG+4.62; 7.8" PA217 G21.00 dG+7.99
- SIMBAD (10"): V* V515 Ori [Y*O; *,Em*,MIR,NIR,V*,Y*?,Y*O,ev] 0.05" refs=28; Gaia DR3 3336143197522028928 [*; *] 4.44" refs=3
- ASAS-SN: 936 points, cameras bA(g,181, d=+0.405); bE(g,120, d=+0.834); ba(V,156); bi(g,236, d=+0.551); bm(g,121, d=+0.757); bq(g,122, d=+0.663); change at onset (after-before, per-camera median) +0.663 mag; largest seasonal dimming 0.66 mag at MJD 59854
- dust: excess flux W1 10.88 mJy, W2 17.80 mJy, T = 818 K (16-84%: 797-840) 

### uid981812  [D2]  YOUNG
- position 88.65812 +1.49762; Gaia DR3 3315789764117572224; G 13.89, BP-RP 1.67, plx 2.91 mas; plot `plots/uid981812.png`
- **young:** SIMBAD young-star types Or*,Y*O (EM* LkHA  337) | Gaia DR3 variability class YSO(0.54)
- flags: 1.35 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | optical dimming +1.226 mag after the infrared onset (debris transit signature) | largest seasonal optical dimming 1.03 mag (MJD 58152)
- NEOWISE: score refetch 3.19 (stored 3.19, reproduced True); dW2 0.968, dW1 0.820, 20 visits, 191 points; baseline W1 9.08, W1-W2 0.571; onset between MJD 57816 and 58018
- detector 2: excess 0.617 mag, z 22.0, jitter ratio 21.6
- field control: target step +0.668 (W1 +0.626); neighbours N=93, median -0.009, robust sigma 0.013, max +0.023; z = 50.7
- centroid: jump at onset 0.001" +- 0.014 (0.1 sigma, PA 80); largest consecutive-visit jump 0.086"; rms 0.035"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.605, W2-W3 2.066 (W3 S/N 72.7), W3-W4 2.138 (W4 S/N 35.1), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.40, ipd_frac_multi_peak 4, NSS none, Teff 8489 K, logg 4.49, H-alpha pEW -2.162 nm, varclass YSO(0.54); M_G 6.21, -1.35 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): EM* LkHA  337 [Or*; *,Em*,MIR,NIR,Opt,Or*,V*,Y*O,ev] 0.08" refs=20
- ASAS-SN: 1420 points, cameras bA(g,199); bB(g,39); bE(g,156); ba(V,167, d=+1.294); bb(V,173, d=+1.158); bi(g,243); bj(g,166); bm(g,129); bq(g,148); change at onset (after-before, per-camera median) +1.226 mag; largest seasonal dimming 1.03 mag at MJD 58152
- dust: excess flux W1 78.07 mJy, W2 97.53 mJy, T = 1023 K (16-84%: 987-1062) 

### uid1797726  [D2]  YOUNG
- position 84.55481 -2.76419; Gaia DR3 3216107593266865536; G 14.62, BP-RP 2.02, plx 2.47 mas; plot `plots/uid1797726.png`
- **young:** SIMBAD young-star types TT*,Y*O (Haro 5-8) | Gaia DR3 variability class YSO(0.21)
- flags: 1.94 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | possible optical brightening at onset (-0.213 mag, one camera only) | largest seasonal optical dimming 0.15 mag (MJD 56645)
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 21 visits, 223 points; baseline W1 10.00, W1-W2 0.597; onset between MJD 56729 and 56921
- detector 2: excess 0.587 mag, z 14.2, jitter ratio 8.9
- field control: target step +0.882 (W1 +0.749); neighbours N=106, median -0.001, robust sigma 0.019, max +0.164; z = 47.6
- centroid: jump at onset 0.039" +- 0.022 (1.8 sigma, PA 46); largest consecutive-visit jump 0.073"; rms 0.027"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.479, W2-W3 1.806 (W3 S/N 44.5), W3-W4 2.063 (W4 S/N 24.3), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.10, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW -5.298 nm, varclass YSO(0.21); M_G 6.59, -1.94 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): Haro 5-8 [TT*; *,Em*,NIR,TT*,V*,V*?,Y*O] 0.03" refs=39
- ASAS-SN: 1458 points, cameras bC(g,157); bG(g,216); ba(V,49); bc(V,151, d=-0.213); be(V,38); bg(V,151); bk(g,310); bo(g,221); bs(g,165); change at onset (after-before, per-camera median) -0.213 mag; largest seasonal dimming 0.15 mag at MJD 56645
- dust: excess flux W1 15.52 mJy, W2 17.38 mJy, T = 1143 K (16-84%: 1123-1162) 

### uid416674  [D2]  YOUNG
- position 63.57807 +11.97018; Gaia DR3 3304172564776041728; G 12.10, BP-RP 1.51, plx 3.41 mas; plot `plots/uid416674.png`
- **young:** SIMBAD young-star types TT? (IRAS 04114+1150)
- flags: 2.37 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.33 mag (MJD 58902)
- NEOWISE: score refetch 1.37 (stored 1.37, reproduced True); dW2 0.115, dW1 0.133, 21 visits, 196 points; baseline W1 8.97, W1-W2 0.390; onset between MJD 58515 and 58724
- detector 2: excess 0.449 mag, z 19.2, jitter ratio 7.8
- field control: target step +0.369 (W1 +0.327); neighbours N=44, median +0.003, robust sigma 0.009, max +0.022; z = 39.4
- centroid: jump at onset 0.016" +- 0.020 (0.8 sigma, PA 100); largest consecutive-visit jump 0.071"; rms 0.034"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.369, W2-W3 2.912 (W3 S/N 74.5), W3-W4 2.063 (W4 S/N 42.7), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.36, ipd_frac_multi_peak 0, NSS none, Teff 5587 K, logg 3.88, H-alpha pEW 0.022 nm, varclass none; M_G 4.76, -2.37 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): IRAS 04114+1150 [TT?; *,IR,NIR,TT?] 0.13" refs=8
- ASAS-SN: 1989 points, cameras bB(g,96, d=+0.022); bF(g,126, d=-0.031); bG(g,147, d=+0.051); bb(V,249); bc(V,219); bf(V,33); bg(V,45); bj(g,166, d=+0.066); bk(g,247, d=+0.045); bn(g,204, d=+0.051); bo(g,205, d=+0.044); br(g,134, d=+0.036); bs(g,118, d=-0.035); change at onset (after-before, per-camera median) +0.044 mag; largest seasonal dimming 0.33 mag at MJD 58902
- dust: excess flux W1 13.69 mJy, W2 11.57 mJy, T = 1679 K (16-84%: 1475-1963) 

### uid1646554  [D2]  YOUNG
- position 87.02274 +8.59186; Gaia DR3 3335355775396960128; G 14.24, BP-RP 1.87, plx 2.54 mas; plot `plots/uid1646554.png`
- **young:** SIMBAD young-star types Y*?,Y*O (1RXS J054806.1+083523) | Gaia DR3 variability class YSO(0.41)
- flags: 1.84 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 20 visits, 203 points; baseline W1 10.29, W1-W2 0.582; onset between MJD 56732 and 56924
- detector 2: excess 0.601 mag, z 15.7, jitter ratio 17.1
- field control: target step +0.575 (W1 +0.379); neighbours N=107, median +0.001, robust sigma 0.015, max +0.047; z = 38.7
- centroid: jump at onset 0.032" +- 0.027 (1.2 sigma, PA 319); largest consecutive-visit jump 0.077"; rms 0.031"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.552, W2-W3 2.120 (W3 S/N 59.6), W3-W4 1.858 (W4 S/N 26.7), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.30, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW -0.219 nm, varclass YSO(0.41); M_G 6.26, -1.84 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): 1RXS J054806.1+083523 [BY*; *,BY*,MIR,NIR,X,Y*?,Y*O] 0.06" refs=14
- ASAS-SN: 874 points, cameras bB(g,96); bF(g,133); bb(V,197); bj(g,213); bn(g,117); br(g,118); change at onset (after-before, per-camera median) n/a mag; largest seasonal dimming 0.05 mag at MJD 58595
- dust: excess flux W1 6.88 mJy, W2 9.35 mJy, T = 948 K (16-84%: 926-971) 
- checks missing: ASAS-SN change at onset (no camera spans the onset)

### uid1175029  [D2]  YOUNG
- position 122.26036 -48.97142; Gaia DR3 5514560780536422784; G 12.97, BP-RP 0.93, plx 2.79 mas; plot `plots/uid1175029.png`
- **young:** SIMBAD young-star types Y*O (2MASS J08090250-4858172)
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 21 visits, 326 points; baseline W1 11.04, W1-W2 0.370; onset between MJD 59696 and 59906
- detector 2: excess 0.416 mag, z 31.2, jitter ratio 10.2
- field control: target step +0.285 (W1 +0.097); neighbours N=198, median +0.001, robust sigma 0.009, max +0.031; z = 33.2
- centroid: jump at onset 0.016" +- 0.010 (1.6 sigma, PA 169); largest consecutive-visit jump 0.039"; rms 0.024"; toward neighbour: none; expected shift if a neighbour were the source: 3.0" G19.4: 0.69"; 4.5" G20.4: 1.05"; 5.4" G19.0: 1.24"; 8.2" G19.0: 1.89"
- AllWISE 2010: W1-W2 0.316, W2-W3 2.446 (W3 S/N 55.2), W3-W4 0.791 (W4 S/N 8.9), ext_flg 1, ph_qual AAAB: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.04, ipd_frac_multi_peak 0, NSS none, Teff 5571 K, logg 4.47, H-alpha pEW 0.121 nm, varclass SOLAR_LIKE(0.64); M_G 5.20, +0.06 mag vs sequence (on the sequence); neighbours within 10": 3.0" PA306 G19.39 dG+6.42; 4.5" PA81 G20.42 dG+7.44; 5.4" PA253 G19.03 dG+6.06; 8.2" PA307 G19.02 dG+6.05
- SIMBAD (10"): 2MASS J08090250-4858172 [Y*O; *,IR,MIR,NIR,Y*O] 0.25" refs=45
- ASAS-SN: 1219 points, cameras bH(g,397, d=-0.002); bh(V,157); bl(g,447, d=-0.011); bp(g,218, d=-0.010); change at onset (after-before, per-camera median) -0.010 mag; largest seasonal dimming 0.02 mag at MJD 58363
- dust: excess flux W1 0.66 mJy, W2 1.40 mJy, T = 690 K (16-84%: 642-743) 

### uid1796278  [D2]  YOUNG
- position 84.68432 -2.67216; Gaia DR3 3216109861009561728; G 13.27, BP-RP 1.68, plx 2.47 mas; plot `plots/uid1796278.png`
- **young:** SIMBAD young-star types TT*,Y*O ([W96]  4771-1051) | Gaia DR3 variability class YSO(0.35)
- flags: 2.34 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.14 mag (MJD 56645)
- NEOWISE: score refetch 1.01 (stored 1.01, reproduced True); dW2 0.193, dW1 0.120, 21 visits, 225 points; baseline W1 9.72, W1-W2 0.558; onset between MJD 57647 and 57812
- detector 2: excess 0.603 mag, z 21.2, jitter ratio 10.4
- field control: target step +0.511 (W1 +0.366); neighbours N=113, median -0.003, robust sigma 0.016, max +0.668; z = 33.0
- centroid: jump at onset 0.016" +- 0.012 (1.4 sigma, PA 282); largest consecutive-visit jump 0.067"; rms 0.027"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.488, W2-W3 2.533 (W3 S/N 76.6), W3-W4 2.153 (W4 S/N 34.2), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.03, ipd_frac_multi_peak 0, NSS none, Teff 5102 K, logg 4.10, H-alpha pEW -0.357 nm, varclass YSO(0.35); M_G 5.24, -2.34 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): [W96]  4771-1051 [TT*; *,NIR,TT*,X,Y*O] 0.03" refs=42
- ASAS-SN: 1231 points, cameras bC(g,157); bG(g,221); ba(V,51); bc(V,151, d=-0.061); be(V,38); bg(V,152, d=+4.470); bk(g,231); bo(g,159); bs(g,71); change at onset (after-before, per-camera median) +2.204 mag; largest seasonal dimming 0.14 mag at MJD 56645
- dust: excess flux W1 10.86 mJy, W2 14.62 mJy, T = 956 K (16-84%: 930-982) 

### uid1627666  [D2]  YOUNG
- position 82.51589 +12.02268; Gaia DR3 3340882749767481216; G 14.34, BP-RP 2.00, plx 2.55 mas; plot `plots/uid1627666.png`
- **young:** SIMBAD young-star types Or*,Y*O ([DM99] 113) | Gaia DR3 variability class YSO(0.34)
- flags: 2.09 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | optical dimming +0.152 mag after the infrared onset (debris transit signature) | largest seasonal optical dimming 0.26 mag (MJD 57065)
- NEOWISE: score refetch 1.04 (stored 1.04, reproduced True); dW2 0.294, dW1 0.385, 16 visits, 150 points; baseline W1 9.63, W1-W2 0.669; onset between MJD 58377 and 58534
- detector 2: excess 0.664 mag, z 16.0, jitter ratio 11.4
- field control: target step +0.482 (W1 +0.444); neighbours N=109, median -0.005, robust sigma 0.016, max +0.118; z = 29.9
- centroid: jump at onset 0.043" +- 0.034 (1.3 sigma, PA 154); largest consecutive-visit jump 0.089"; rms 0.036"; toward neighbour: none; expected shift if a neighbour were the source: 4.3" G20.2: 1.53"
- AllWISE 2010: W1-W2 0.599, W2-W3 1.999 (W3 S/N 64.4), W3-W4 1.692 (W4 S/N 26.9), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.12, ipd_frac_multi_peak 0, NSS none, Teff 5656 K, logg 4.19, H-alpha pEW -1.043 nm, varclass YSO(0.34); M_G 6.37, -2.09 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 4.3" PA300 G20.24 dG+5.90
- SIMBAD (10"): [DM99] 113 [Or*; *,Em*,LP?,NIR,Or*,Y*O] 0.02" refs=22
- ASAS-SN: 1861 points, cameras bA(g,182); bB(g,91); bD(g,197); bE(g,120); bH(g,111); ba(V,160); bd(V,170); bi(g,220, d=+0.112); bl(g,181, d=+0.045); bm(g,113); bp(g,93); bq(g,120, d=+0.193); bt(g,103, d=+0.224); change at onset (after-before, per-camera median) +0.152 mag; largest seasonal dimming 0.26 mag at MJD 57065
- dust: excess flux W1 27.53 mJy, W2 24.99 mJy, T = 1495 K (16-84%: 1450-1541) 

### uid1671757  [D2]  YOUNG
- position 84.75970 +8.93677; Gaia DR3 3334817603111130752; G 11.19, BP-RP 1.05, plx 2.53 mas; plot `plots/uid1671757.png`
- **young:** SIMBAD young-star types TT? (2MASS J05390232+0856123) | Gaia DR3 variability class YSO(0.22)
- flags: 2.49 mag above the main sequence at its colour | optical dimming +0.068 mag after the infrared onset (debris transit signature)
- NEOWISE: score refetch 0.68 (stored 0.68, reproduced True); dW2 0.072, dW1 -0.015, 21 visits, 245 points; baseline W1 8.24, W1-W2 0.226; onset between MJD 58170 and 58379
- detector 2: excess 0.279 mag, z 18.1, jitter ratio 7.6
- field control: target step +0.322 (W1 +0.232); neighbours N=103, median -0.001, robust sigma 0.011, max +0.038; z = 29.0
- centroid: jump at onset 0.018" +- 0.014 (1.3 sigma, PA 235); largest consecutive-visit jump 0.039"; rms 0.022"; toward neighbour: 9.5" PA201 G17.5 (angle 34 deg); expected shift if a neighbour were the source: 9.5" G17.5: 2.44"
- AllWISE 2010: W1-W2 0.206, W2-W3 1.587 (W3 S/N 64.8), W3-W4 2.401 (W4 S/N 43.6), ext_flg 0, ph_qual AAAA: W3 excess only (W2-W3 > 1.0; debris-disk-like or blend)
- Gaia: RUWE 1.09, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW -0.023 nm, varclass YSO(0.22); M_G 3.20, -2.49 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 9.5" PA201 G17.52 dG+6.33
- SIMBAD (10"): 2MASS J05390232+0856123 [TT?; *,NIR,TT?] 0.05" refs=12
- ASAS-SN: 933 points, cameras bA(g,183); bE(g,120); ba(V,156, d=+0.068); bi(g,235); bm(g,122); bq(g,117); change at onset (after-before, per-camera median) +0.068 mag; largest seasonal dimming 0.08 mag at MJD 58873
- dust: excess flux W1 23.55 mJy, W2 24.03 mJy, T = 1273 K (16-84%: 1194-1362) 

### uid1515886  [D2]  YOUNG
- position 83.25734 -4.82182; Gaia DR3 3209608723634530944; G 15.54, BP-RP 1.40, plx 2.60 mas; plot `plots/uid1515886.png`
- **young:** SIMBAD young-star types Or*,Y*O (V* HS Ori) | Gaia DR3 variability class YSO(0.36)
- flags: AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.20 mag (MJD 59251)
- NEOWISE: score refetch 1.29 (stored 1.29, reproduced True); dW2 0.244, dW1 0.173, 20 visits, 183 points; baseline W1 10.52, W1-W2 0.830; onset between MJD 59108 and 59263
- detector 2: excess 0.893 mag, z 43.0, jitter ratio 14.9
- field control: target step +0.468 (W1 +0.418); neighbours N=90, median -0.001, robust sigma 0.016, max +0.231; z = 28.8
- centroid: jump at onset 0.038" +- 0.028 (1.4 sigma, PA 73); largest consecutive-visit jump 0.083"; rms 0.041"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.892, W2-W3 2.341 (W3 S/N 50.2), W3-W4 1.994 (W4 S/N 26.2), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.03, ipd_frac_multi_peak 0, NSS none, Teff 5077 K, logg 4.85, H-alpha pEW -6.623 nm, varclass YSO(0.36); M_G 7.62, +0.78 mag vs sequence (below the sequence); neighbours within 10": none
- SIMBAD (10"): V* HS Ori [Or*; *,Em*,MIR,NIR,Or*,V*,Y*O] 0.01" refs=39
- ASAS-SN: 1352 points, cameras bA(g,145, d=-0.047); bE(g,201, d=+0.026); ba(V,162); be(V,189); bi(g,306, d=+0.104); bm(g,202, d=-0.255); bq(g,147, d=-0.123); change at onset (after-before, per-camera median) -0.047 mag; largest seasonal dimming 0.20 mag at MJD 59251
- dust: excess flux W1 7.57 mJy, W2 9.64 mJy, T = 1005 K (16-84%: 961-1052) 

### uid1467951  [D2]  YOUNG
- position 333.52545 +70.08455; Gaia DR3 2229371258245926528; G 11.25, BP-RP 1.23, plx 2.62 mas; plot `plots/uid1467951.png`
- **young:** SIMBAD young-star types Or*,Y*O (IRAS 22129+6949) | Gaia DR3 variability class YSO(0.19)
- flags: 2.99 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 0.41 (stored 0.41, reproduced True); dW2 0.092, dW1 0.101, 21 visits, 406 points; baseline W1 8.07, W1-W2 0.350; onset between MJD 57234 and 57407
- detector 2: excess 0.411 mag, z 21.3, jitter ratio 21.3
- field control: target step +0.189 (W1 +0.243); neighbours N=117, median -0.002, robust sigma 0.007, max +0.086; z = 28.6
- centroid: jump at onset 0.027" +- 0.019 (1.4 sigma, PA 268); largest consecutive-visit jump 0.067"; rms 0.030"; toward neighbour: none; expected shift if a neighbour were the source: 6.3" G17.2: 1.00"; 8.9" G18.2: 1.42"
- AllWISE 2010: W1-W2 0.350, W2-W3 2.205 (W3 S/N 78.7), W3-W4 2.448 (W4 S/N 57.5), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 0.81, ipd_frac_multi_peak 0, NSS none, Teff 5504 K, logg 3.68, H-alpha pEW -0.382 nm, varclass YSO(0.19); M_G 3.35, -2.99 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 6.3" PA115 G17.19 dG+5.93; 8.9" PA55 G18.22 dG+6.97
- SIMBAD (10"): IRAS 22129+6949 [Or*; *,AB?,IR,MIR,NIR,Or*,Y*O] 0.08" refs=12
- ASAS-SN: 808 points, cameras bD(g,346); bd(V,187, d=-0.012); bt(g,275); change at onset (after-before, per-camera median) -0.012 mag; largest seasonal dimming 0.03 mag at MJD 58472
- dust: excess flux W1 44.62 mJy, W2 29.72 mJy, T = 3066 K (16-84%: 2620-3741) 

### uid1581737  [D2]  YOUNG
- position 116.88310 -45.51128; Gaia DR3 5530952441620701440; G 13.76, BP-RP 1.57, plx 2.57 mas; plot `plots/uid1581737.png`
- **young:** SIMBAD young-star types Y*?,Y*O (UCAC4 223-017496) | Gaia DR3 variability class YSO(0.16)
- flags: 1.47 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 1.85 (stored 1.85, reproduced True); dW2 0.240, dW1 0.168, 21 visits, 311 points; baseline W1 10.22, W1-W2 0.293; onset between MJD 57143 and 57338
- detector 2: excess 0.348 mag, z 13.9, jitter ratio 6.9
- field control: target step +0.243 (W1 +0.193); neighbours N=144, median -0.006, robust sigma 0.009, max +0.051; z = 27.9
- centroid: jump at onset 0.006" +- 0.012 (0.5 sigma, PA 141); largest consecutive-visit jump 0.026"; rms 0.027"; toward neighbour: none; expected shift if a neighbour were the source: 4.1" G20.6: 0.81"; 8.6" G16.2: 1.73"
- AllWISE 2010: W1-W2 0.297, W2-W3 1.884 (W3 S/N 56.8), W3-W4 1.977 (W4 S/N 24.0), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.05, ipd_frac_multi_peak 0, NSS none, Teff 4700 K, logg 4.15, H-alpha pEW -0.515 nm, varclass YSO(0.16); M_G 5.81, -1.47 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 4.1" PA213 G20.58 dG+6.82; 8.6" PA21 G16.21 dG+2.45
- SIMBAD (10"): UCAC4 223-017496 [Y*?; *,NIR,Y*?,Y*O] 0.17" refs=8
- ASAS-SN: 1390 points, cameras bE(g,423); be(V,231); bi(g,525); bm(g,211); change at onset (after-before, per-camera median) n/a mag; largest seasonal dimming 0.04 mag at MJD 60458
- dust: excess flux W1 3.97 mJy, W2 4.15 mJy, T = 1236 K (16-84%: 1156-1327) 
- checks missing: ASAS-SN change at onset (no camera spans the onset)

### uid1159910  [D2]  YOUNG
- position 79.80651 -3.40349; Gaia DR3 3213527348713890560; G 12.21, BP-RP 1.28, plx 2.80 mas; plot `plots/uid1159910.png`
- **young:** SIMBAD young-star types Or*,TT*,Y*?,Y*O (Kiso A-0975  45)
- flags: 2.03 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | not plain dust: optical brightening -0.047 mag (per-camera -0.068,-0.026) together with the infrared rise | largest seasonal optical dimming 0.11 mag (MJD 60503)
- NEOWISE: score refetch 1.53 (stored 1.53, reproduced True); dW2 0.354, dW1 0.287, 20 visits, 177 points; baseline W1 8.61, W1-W2 0.421; onset between MJD 57807 and 58006
- detector 2: excess 0.483 mag, z 25.1, jitter ratio 18.4
- field control: target step +0.344 (W1 +0.321); neighbours N=60, median -0.004, robust sigma 0.013, max +0.040; z = 26.0
- centroid: jump at onset 0.023" +- 0.021 (1.1 sigma, PA 261); largest consecutive-visit jump 0.091"; rms 0.039"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.537, W2-W3 1.839 (W3 S/N 71.4), W3-W4 1.731 (W4 S/N 41.2), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.31, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW -1.244 nm, varclass none; M_G 4.45, -2.03 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): Kiso A-0975  45 [TT*; *,Em*,MIR,NIR,Or*,TT*,Y*?,Y*O] 0.03" refs=9
- ASAS-SN: 1493 points, cameras bD(g,160); bH(g,206); bb(V,55); bd(V,154, d=-0.068); bf(V,36); bh(V,152, d=-0.026); bl(g,328); bp(g,229); bt(g,173); change at onset (after-before, per-camera median) -0.047 mag; largest seasonal dimming 0.11 mag at MJD 60503
- dust: excess flux W1 35.11 mJy, W2 33.90 mJy, T = 1367 K (16-84%: 1307-1433) 

### uid1116479  [D2]  YOUNG
- position 120.62778 -51.81680; Gaia DR3 5512928765979700352; G 13.31, BP-RP 1.64, plx 2.82 mas; plot `plots/uid1116479.png`
- **young:** SIMBAD young-star types Y*?,Y*O (Gaia DR3 5512928765979700352)
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | Gaia ipd_frac_multi_peak 41% (resolved double?) | 1.92 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 1.93 (stored 1.93, reproduced True); dW2 0.278, dW1 0.248, 21 visits, 478 points; baseline W1 9.54, W1-W2 0.332; onset between MJD 57156 and 57349
- detector 2: excess 0.381 mag, z 14.0, jitter ratio 13.9
- field control: target step +0.188 (W1 +0.309); neighbours N=131, median -0.003, robust sigma 0.007, max +0.021; z = 25.8
- centroid: jump at onset 0.007" +- 0.013 (0.5 sigma, PA 257); largest consecutive-visit jump 0.044"; rms 0.021"; toward neighbour: none; expected shift if a neighbour were the source: 1.0" G16.6: 0.17"; 8.2" G20.2: 1.31"
- AllWISE 2010: W1-W2 0.353, W2-W3 2.117 (W3 S/N 68.3), W3-W4 1.842 (W4 S/N 40.7), ext_flg 1, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.24, ipd_frac_multi_peak 41, NSS none, Teff 5090 K, logg 4.14, H-alpha pEW -0.651 nm, varclass none; M_G 5.56, -1.92 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 1.0" PA140 G16.57 dG+3.26; 8.2" PA121 G20.19 dG+6.88
- SIMBAD (10"): Gaia DR3 5512928765979700352 [Y*?; *,Y*?,Y*O] 0.17" refs=4; 1RXS J080230.9-514903 [X; X] 3.31" refs=0
- ASAS-SN: 0 points, cameras n/a; change at onset (after-before, per-camera median) n/a mag; largest seasonal dimming n/a mag at MJD n/a
- dust: excess flux W1 13.80 mJy, W2 10.22 mJy, T = 2212 K (16-84%: 2024-2443) 
- checks missing: ASAS-SN (no source)

### uid1061853  [D2]  YOUNG
- position 84.80421 -1.45591; Gaia DR3 3217423674325646208; G 13.13, BP-RP 1.54, plx 2.86 mas; plot `plots/uid1061853.png`
- **young:** SIMBAD young-star types Or*,Y*?,Y*O (Haro 5-17)
- flags: 1.79 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.11 mag (MJD 58484)
- NEOWISE: score refetch 3.34 (stored 3.34, reproduced True); dW2 0.397, dW1 0.418, 20 visits, 207 points; baseline W1 9.32, W1-W2 0.547; onset between MJD 57283 and 57448
- detector 2: excess 0.604 mag, z 25.0, jitter ratio 11.6
- field control: target step +0.432 (W1 +0.340); neighbours N=96, median -0.005, robust sigma 0.017, max +0.056; z = 25.1
- centroid: jump at onset 0.014" +- 0.023 (0.6 sigma, PA 198); largest consecutive-visit jump 0.068"; rms 0.034"; toward neighbour: 5.5" PA201 G21.0 (angle 3 deg); expected shift if a neighbour were the source: 5.5" G21.0: 1.81"
- AllWISE 2010: W1-W2 0.613, W2-W3 2.419 (W3 S/N 73.4), W3-W4 1.859 (W4 S/N 42.3), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.25, ipd_frac_multi_peak 0, NSS none, Teff 6192 K, logg 4.09, H-alpha pEW -1.147 nm, varclass none; M_G 5.41, -1.79 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 5.5" PA201 G21.04 dG+7.91
- SIMBAD (10"): Haro 5-17 [Or*; *,Em*,IR,NIR,Or*,V*,Y*?,Y*O,ev] 0.04" refs=28
- ASAS-SN: 1377 points, cameras bC(g,158); bG(g,222); bc(V,149, d=-0.145); be(V,38); bg(V,153, d=-0.005); bk(g,305); bo(g,193); bs(g,159); change at onset (after-before, per-camera median) -0.075 mag; largest seasonal dimming 0.11 mag at MJD 58484
- dust: excess flux W1 19.57 mJy, W2 19.47 mJy, T = 1315 K (16-84%: 1259-1374) 

### uid1096024  [D2]  YOUNG
- position 79.01677 +6.31465; Gaia DR3 3240774999197509504; G 14.11, BP-RP 2.10, plx 2.84 mas; plot `plots/uid1096024.png`
- **young:** SIMBAD young-star types TT?,Y*?,Y*O (2MASS J05160402+0618525)
- flags: Gaia ipd_frac_multi_peak 96% (resolved double?) | 2.38 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.25 mag (MJD 59818)
- NEOWISE: score refetch 0.41 (stored 0.41, reproduced True); dW2 0.096, dW1 0.069, 20 visits, 207 points; baseline W1 8.75, W1-W2 0.653; onset between MJD 57084 and 57278
- detector 2: excess 0.633 mag, z 14.7, jitter ratio 21.2
- field control: target step +0.221 (W1 +0.155); neighbours N=86, median -0.001, robust sigma 0.009, max +0.032; z = 24.9
- centroid: jump at onset 0.022" +- 0.015 (1.5 sigma, PA 269); largest consecutive-visit jump 0.063"; rms 0.034"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.631, W2-W3 1.584 (W3 S/N 67.4), W3-W4 1.939 (W4 S/N 38.4), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.37, ipd_frac_multi_peak 96, NSS none, Teff nan K, logg nan, H-alpha pEW -0.858 nm, varclass none; M_G 6.38, -2.38 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): 2MASS J05160402+0618525 [Y*O; *,NIR,TT?,Y*?,Y*O] 0.03" refs=4
- ASAS-SN: 1674 points, cameras bC(g,189); bD(g,194); bH(g,146); bc(V,246, d=+0.025); bd(V,250, d=-0.033); bh(V,52); bl(g,268); bp(g,208); bt(g,121); change at onset (after-before, per-camera median) -0.004 mag; largest seasonal dimming 0.25 mag at MJD 59818
- dust: excess flux W1 12.88 mJy, W2 16.19 mJy, T = 1017 K (16-84%: 955-1087) 

### uid1574635  [D2]  YOUNG
- position 80.10728 -5.78511; Gaia DR3 3209948335287188608; G 13.04, BP-RP 1.35, plx 2.57 mas; plot `plots/uid1574635.png`
- **young:** SIMBAD young-star types Or*,TT*,Y*O (V* V534 Ori) | Gaia DR3 variability class YSO(0.49)
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | 1.63 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | not plain dust: optical brightening -0.168 mag (per-camera -0.092,-0.168,-0.177,-0.037,-0.192) together with the infrared rise | largest seasonal optical dimming 0.22 mag (MJD 57647)
- NEOWISE: score refetch 1.82 (stored 1.82, reproduced True); dW2 0.315, dW1 0.242, 20 visits, 209 points; baseline W1 8.66, W1-W2 0.638; onset between MJD 58895 and 59102
- detector 2: excess 0.701 mag, z 34.9, jitter ratio 13.3
- field control: target step +0.325 (W1 +0.307); neighbours N=52, median -0.005, robust sigma 0.013, max +0.229; z = 24.7
- centroid: jump at onset 0.035" +- 0.026 (1.3 sigma, PA 104); largest consecutive-visit jump 0.084"; rms 0.037"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.672, W2-W3 2.033 (W3 S/N 68.4), W3-W4 1.706 (W4 S/N 36.9), ext_flg 1, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.36, ipd_frac_multi_peak 0, NSS none, Teff 5802 K, logg 4.16, H-alpha pEW -3.239 nm, varclass YSO(0.49); M_G 5.09, -1.63 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): V* V534 Ori [Or*; *,Em*,NIR,Or*,TT*,V*,Y*O] 0.03" refs=14
- ASAS-SN: 1280 points, cameras bB(g,87, d=-0.092); bF(g,204, d=-0.168); bb(V,155); bf(V,161); bj(g,276, d=-0.177); bn(g,234, d=-0.037); br(g,163, d=-0.192); change at onset (after-before, per-camera median) -0.168 mag; largest seasonal dimming 0.22 mag at MJD 57647
- dust: excess flux W1 33.93 mJy, W2 37.98 mJy, T = 1143 K (16-84%: 1086-1206) 

### uid1018261  [D2]  YOUNG
- position 328.15812 +72.57478; Gaia DR3 2272880410824048512; G 14.86, BP-RP 2.00, plx 2.89 mas; plot `plots/uid1018261.png`
- **young:** SIMBAD young-star types Y*? (UCAC4 813-029498) | Gaia DR3 variability class YSO(0.55)
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | 1.29 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | not plain dust: optical brightening -0.286 mag (per-camera -0.309,-0.263) together with the infrared rise | largest seasonal optical dimming 0.36 mag (MJD 58266)
- NEOWISE: score refetch 4.97 (stored 4.97, reproduced True); dW2 0.659, dW1 0.453, 21 visits, 394 points; baseline W1 10.58, W1-W2 0.619; onset between MJD 58336 and 58494
- detector 2: excess 0.614 mag, z 14.8, jitter ratio 13.1
- field control: target step +0.267 (W1 +0.120); neighbours N=79, median -0.003, robust sigma 0.011, max +0.023; z = 24.3
- centroid: jump at onset 0.044" +- 0.021 (2.1 sigma, PA 135); largest consecutive-visit jump 0.071"; rms 0.035"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.607, W2-W3 2.277 (W3 S/N 65.5), W3-W4 1.792 (W4 S/N 30.0), ext_flg 1, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.16, ipd_frac_multi_peak 0, NSS none, Teff 3567 K, logg 4.00, H-alpha pEW -3.516 nm, varclass YSO(0.55); M_G 7.16, -1.29 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): UCAC4 813-029498 [Y*?; *,MIR,NIR,Y*?] 0.08" refs=1
- ASAS-SN: 845 points, cameras bA(g,335); ba(V,250, d=-0.309); bq(g,260, d=-0.263); change at onset (after-before, per-camera median) -0.286 mag; largest seasonal dimming 0.36 mag at MJD 58266
- dust: excess flux W1 10.20 mJy, W2 12.35 mJy, T = 1055 K (16-84%: 1033-1077) 

### uid1050117  [D2]  YOUNG
- position 81.38490 -6.98810; Gaia DR3 3208832739004817920; G 11.44, BP-RP 0.98, plx 2.87 mas; plot `plots/uid1050117.png`
- **young:** SIMBAD young-star types Y*?,Y*O (IRAS 05231-0701)
- flags: 1.67 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | not plain dust: optical brightening -0.074 mag (per-camera -0.074,-0.074) together with the infrared rise | largest seasonal optical dimming 0.16 mag (MJD 56904)
- NEOWISE: score refetch 1.82 (stored 1.82, reproduced True); dW2 0.307, dW1 0.257, 19 visits, 188 points; baseline W1 8.24, W1-W2 0.430; onset between MJD 57444 and 57643
- detector 2: excess 0.479 mag, z 32.3, jitter ratio 13.9
- field control: target step +0.266 (W1 +0.282); neighbours N=49, median -0.005, robust sigma 0.011, max +0.024; z = 24.3
- centroid: jump at onset 0.027" +- 0.015 (1.8 sigma, PA 71); largest consecutive-visit jump 0.052"; rms 0.027"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.407, W2-W3 1.883 (W3 S/N 68.0), W3-W4 3.187 (W4 S/N 56.0), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 0.99, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW -0.019 nm, varclass none; M_G 3.73, -1.67 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): IRAS 05231-0701 [Y*O; *,IR,MIR,NIR,Opt,V*,Y*?,Y*O] 0.03" refs=10
- ASAS-SN: 1494 points, cameras bA(g,158); bE(g,220); ba(V,150, d=-0.074); be(V,195, d=-0.074); bi(g,346); bm(g,251); bq(g,174); change at onset (after-before, per-camera median) -0.074 mag; largest seasonal dimming 0.16 mag at MJD 56904
- dust: excess flux W1 49.84 mJy, W2 41.66 mJy, T = 1712 K (16-84%: 1607-1834) 

### uid1516508  [D2]  YOUNG
- position 83.50454 -6.04075; Gaia DR3 3017211128124211328; G 14.28, BP-RP 1.82, plx 2.60 mas; plot `plots/uid1516508.png`
- **young:** SIMBAD young-star types Or*,TT*,Y*?,Y*O (V* V1416 Ori) | Gaia DR3 variability class YSO(0.25)
- flags: 1.61 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | not plain dust: optical brightening -0.042 mag (per-camera -0.042,-0.005,-0.055,-0.032,-0.065) together with the infrared rise
- NEOWISE: score refetch 1.89 (stored 1.90, reproduced True); dW2 0.328, dW1 0.168, 21 visits, 192 points; baseline W1 10.73, W1-W2 0.526; onset between MJD 58535 and 58741
- detector 2: excess 0.552 mag, z 15.6, jitter ratio 17.1
- field control: target step +0.393 (W1 +0.126); neighbours N=103, median +0.000, robust sigma 0.016, max +0.193; z = 24.1
- centroid: jump at onset 0.028" +- 0.029 (1.0 sigma, PA 215); largest consecutive-visit jump 0.073"; rms 0.039"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.607, W2-W3 2.800 (W3 S/N 48.0), W3-W4 1.623 (W4 S/N 30.7), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.01, ipd_frac_multi_peak 1, NSS none, Teff 4714 K, logg 4.18, H-alpha pEW -0.513 nm, varclass YSO(0.25); M_G 6.36, -1.61 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): V* V1416 Ori [TT*; *,MIR,NIR,Or*,TT*,V*,Y*?,Y*O] 0.02" refs=39
- ASAS-SN: 1503 points, cameras bA(g,156, d=-0.042); bE(g,219, d=-0.005); ba(V,179); be(V,195); bi(g,340, d=-0.055); bm(g,246, d=-0.032); bq(g,168, d=-0.065); change at onset (after-before, per-camera median) -0.042 mag; largest seasonal dimming 0.05 mag at MJD 60235
- dust: excess flux W1 4.03 mJy, W2 7.45 mJy, T = 751 K (16-84%: 735-767) 

### uid1499154  [D2]  YOUNG
- position 84.22543 -2.88770; Gaia DR3 3216079899317606272; G 12.91, BP-RP 1.39, plx 2.61 mas; plot `plots/uid1499154.png`
- **young:** SIMBAD young-star types Or*,Y*O (V* V2715 Ori) | Gaia DR3 variability class YSO(0.65)
- flags: 1.80 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 0.13 (stored 0.14, reproduced True); dW2 0.021, dW1 0.030, 21 visits, 206 points; baseline W1 9.52, W1-W2 0.302; onset between MJD 60205 and 60362
- detector 2: excess 0.365 mag, z 17.6, jitter ratio 15.1
- field control: target step +0.288 (W1 +0.246); neighbours N=68, median -0.002, robust sigma 0.013, max +0.324; z = 22.4
- centroid: jump at onset 0.017" +- 0.025 (0.7 sigma, PA 290); largest consecutive-visit jump 0.055"; rms 0.026"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.321, W2-W3 2.314 (W3 S/N 66.3), W3-W4 2.813 (W4 S/N 41.3), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 0.98, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW -0.358 nm, varclass YSO(0.65); M_G 5.00, -1.80 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): V* V2715 Ori [Or*; *,NIR,Or*,V*,Y*O] 0.02" refs=14
- ASAS-SN: 0 points, cameras n/a; change at onset (after-before, per-camera median) n/a mag; largest seasonal dimming n/a mag at MJD n/a
- dust: excess flux W1 8.82 mJy, W2 7.47 mJy, T = 1673 K (16-84%: 1541-1829) 
- checks missing: ASAS-SN (no source)

### uid1408208  [D2]  YOUNG
- position 333.92469 +69.64908; Gaia DR3 2223295734949415168; G 11.42, BP-RP 1.11, plx 2.66 mas; plot `plots/uid1408208.png`
- **young:** SIMBAD young-star types Or*,Y*O (TYC 4467-324-1) | Gaia DR3 variability class YSO(0.20)
- flags: 2.40 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | not plain dust: optical brightening -0.033 mag (per-camera -0.043,-0.024) together with the infrared rise
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 22 visits, 413 points; baseline W1 8.35, W1-W2 0.550; onset between MJD 59584 and 59791
- detector 2: excess 0.607 mag, z 34.8, jitter ratio 7.3
- field control: target step +0.167 (W1 +0.102); neighbours N=119, median +0.004, robust sigma 0.007, max +0.039; z = 22.0
- centroid: jump at onset 0.014" +- 0.015 (0.9 sigma, PA 338); largest consecutive-visit jump 0.058"; rms 0.025"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.497, W2-W3 2.472 (W3 S/N 79.2), W3-W4 1.931 (W4 S/N 63.2), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 0.80, ipd_frac_multi_peak 0, NSS none, Teff 5633 K, logg 3.99, H-alpha pEW -0.194 nm, varclass YSO(0.20); M_G 3.54, -2.40 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): TYC 4467-324-1 [Or*; *,IR,NIR,Or*,Y*O] 0.09" refs=11
- ASAS-SN: 822 points, cameras bD(g,359, d=-0.043); bd(V,187); bt(g,276, d=-0.024); change at onset (after-before, per-camera median) -0.033 mag; largest seasonal dimming 0.09 mag at MJD 59917
- dust: excess flux W1 2.35 mJy, W2 5.39 mJy, T = 658 K (16-84%: 518-833) 

### uid1020396  [D2]  YOUNG
- position 77.87678 +10.53859; Gaia DR3 3387012794470089344; G 13.41, BP-RP 1.76, plx 2.89 mas; plot `plots/uid1020396.png`
- **young:** SIMBAD young-star types Y*?,Y*O (PEP 12)
- flags: 2.06 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 21 visits, 205 points; baseline W1 9.32, W1-W2 0.447; onset between MJD 57806 and 58005
- detector 2: excess 0.483 mag, z 15.1, jitter ratio 5.9
- field control: target step +0.230 (W1 +0.226); neighbours N=68, median -0.008, robust sigma 0.011, max +0.085; z = 20.7
- centroid: jump at onset 0.008" +- 0.015 (0.5 sigma, PA 251); largest consecutive-visit jump 0.063"; rms 0.029"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.428, W2-W3 1.881 (W3 S/N 63.4), W3-W4 2.305 (W4 S/N 40.3), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.11, ipd_frac_multi_peak 0, NSS none, Teff 5737 K, logg 4.15, H-alpha pEW -3.968 nm, varclass none; M_G 5.72, -2.06 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): PEP 12 [Y*O; *,Em*,MIR,NIR,Y*?,Y*O] 0.06" refs=8
- ASAS-SN: 1257 points, cameras bA(g,167); bE(g,140); ba(V,249, d=+0.021); be(V,48, d=+0.032); bi(g,236); bm(g,228); bq(g,189); change at onset (after-before, per-camera median) +0.027 mag; largest seasonal dimming 0.08 mag at MJD 60569
- dust: excess flux W1 4.56 mJy, W2 3.83 mJy, T = 1698 K (16-84%: 1419-2142) 

### uid993575  [D2]  YOUNG
- position 78.12654 -3.88185; Gaia DR3 3213614278852194560; G 13.68, BP-RP 1.49, plx 2.90 mas; plot `plots/uid993575.png`
- **young:** SIMBAD young-star types TT*,Y*?,Y*O (Kiso A-0975   7) | Gaia DR3 variability class YSO(0.50)
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | 1.08 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | not plain dust: optical brightening -0.033 mag (per-camera -0.026,-0.033,-0.134) together with the infrared rise | largest seasonal optical dimming 0.11 mag (MJD 60341)
- NEOWISE: score refetch 0.61 (stored 0.61, reproduced True); dW2 0.143, dW1 0.115, 21 visits, 204 points; baseline W1 9.78, W1-W2 0.442; onset between MJD 57805 and 58005
- detector 2: excess 0.502 mag, z 22.2, jitter ratio 21.4
- field control: target step +0.312 (W1 +0.324); neighbours N=44, median +0.001, robust sigma 0.015, max +0.029; z = 20.5
- centroid: jump at onset 0.011" +- 0.018 (0.6 sigma, PA 19); largest consecutive-visit jump 0.038"; rms 0.034"; toward neighbour: none; expected shift if a neighbour were the source: 6.5" G20.2: 1.63"
- AllWISE 2010: W1-W2 0.446, W2-W3 2.243 (W3 S/N 64.4), W3-W4 2.238 (W4 S/N 36.9), ext_flg 1, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.12, ipd_frac_multi_peak 0, NSS none, Teff 5684 K, logg 4.33, H-alpha pEW -4.057 nm, varclass YSO(0.50); M_G 6.00, -1.08 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 6.5" PA299 G20.25 dG+6.57
- SIMBAD (10"): Kiso A-0975   7 [TT*; *,Em*,NIR,TT*,Y*?,Y*O] 0.02" refs=8
- ASAS-SN: 2587 points, cameras bB(g,88); bC(g,177); bF(g,205); bG(g,210); ba(V,35); bb(V,155, d=-0.026); bc(V,115, d=-0.033); be(V,40); bg(V,187, d=-0.134); bj(g,270); bk(g,297); bn(g,239); bo(g,237); br(g,170); bs(g,162); change at onset (after-before, per-camera median) -0.033 mag; largest seasonal dimming 0.11 mag at MJD 60341
- dust: excess flux W1 6.78 mJy, W2 5.92 mJy, T = 1591 K (16-84%: 1425-1803) 

### uid1284783  [D2]  YOUNG
- position 84.61071 -2.20486; Gaia DR3 3216517706809394560; G 15.39, BP-RP 1.86, plx 2.72 mas; plot `plots/uid1284783.png`
- **young:** SIMBAD young-star types Or*,TT*,Y*O (V* V2730 Ori) | Gaia DR3 variability class YSO(0.53)
- flags: AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | possible optical brightening at onset (-1.124 mag, one camera only) | largest seasonal optical dimming 0.55 mag (MJD 57022)
- NEOWISE: score refetch 2.22 (stored 2.22, reproduced True); dW2 0.328, dW1 0.133, 21 visits, 218 points; baseline W1 10.33, W1-W2 0.513; onset between MJD 57089 and 57283
- detector 2: excess 0.533 mag, z 14.1, jitter ratio 13.9
- field control: target step +0.295 (W1 +0.139); neighbours N=104, median -0.004, robust sigma 0.016, max +0.201; z = 19.2
- centroid: jump at onset 0.024" +- 0.016 (1.5 sigma, PA 355); largest consecutive-visit jump 0.058"; rms 0.028"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.873, W2-W3 1.900 (W3 S/N 58.4), W3-W4 1.487 (W4 S/N 13.5), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.26, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW 0.333 nm, varclass YSO(0.53); M_G 7.57, -0.51 mag vs sequence (on the sequence); neighbours within 10": none
- SIMBAD (10"): V* V2730 Ori [TT*; *,NIR,Or*,TT*,V*,Y*O] 0.04" refs=23
- ASAS-SN: 1317 points, cameras bC(g,152); bG(g,216); ba(V,35); bc(V,115, d=-1.124); be(V,21); bg(V,86); bk(g,308); bo(g,224); bs(g,160); change at onset (after-before, per-camera median) -1.124 mag; largest seasonal dimming 0.55 mag at MJD 57022
- dust: excess flux W1 3.32 mJy, W2 7.64 mJy, T = 656 K (16-84%: 629-686) 

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

### uid1116725  [D2]  YOUNG
- position 126.98516 -34.91464; Gaia DR3 5543418498306270976; G 13.56, BP-RP 1.42, plx 2.82 mas; plot `plots/uid1116725.png`
- **young:** SIMBAD young-star types Y*?,Y*O (WRAY 15-218) | Gaia DR3 variability class YSO(0.03)
- flags: 1.09 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.20 mag (MJD 60439)
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 18 visits, 159 points; baseline W1 9.17, W1-W2 0.487; onset between MJD 56980 and 57148
- detector 2: excess 0.549 mag, z 26.4, jitter ratio 13.7
- field control: target step +0.213 (W1 +0.233); neighbours N=188, median -0.005, robust sigma 0.011, max +0.028; z = 19.0
- centroid: jump at onset 0.012" +- 0.013 (1.0 sigma, PA 357); largest consecutive-visit jump 0.059"; rms 0.028"; toward neighbour: none; expected shift if a neighbour were the source: 3.1" G20.5: 0.55"; 6.1" G17.7: 1.09"; 7.2" G18.3: 1.28"; 8.0" G19.4: 1.42"; 8.2" G17.3: 1.46"
- AllWISE 2010: W1-W2 0.563, W2-W3 1.994 (W3 S/N 76.8), W3-W4 1.711 (W4 S/N 42.8), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.33, ipd_frac_multi_peak 0, NSS none, Teff 5803 K, logg 4.34, H-alpha pEW -1.905 nm, varclass YSO(0.03); M_G 5.81, -1.09 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 3.1" PA75 G20.50 dG+6.95; 6.1" PA224 G17.71 dG+4.15; 7.2" PA45 G18.29 dG+4.73; 8.0" PA127 G19.35 dG+5.80; 8.2" PA109 G17.26 dG+3.70
- SIMBAD (10"): WRAY 15-218 [Em*; *,Em*,NIR,Y*?,Y*O] 0.21" refs=8
- ASAS-SN: 1336 points, cameras bG(g,443); bg(V,239); bk(g,464); bo(g,190); change at onset (after-before, per-camera median) n/a mag; largest seasonal dimming 0.20 mag at MJD 60439
- dust: excess flux W1 8.82 mJy, W2 9.58 mJy, T = 1183 K (16-84%: 1056-1339) 
- checks missing: ASAS-SN change at onset (no camera spans the onset)

### uid1959195  [D2]  YOUNG
- position 84.27603 +0.14864; Gaia DR3 3222331207036336000; G 13.27, BP-RP 1.49, plx 2.41 mas; plot `plots/uid1959195.png`
- **young:** SIMBAD young-star types TT*,Y*?,Y*O (Kiso A-0904  52)
- flags: 1.88 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.10 mag (MJD 60316)
- NEOWISE: score refetch 0.61 (stored 0.61, reproduced True); dW2 0.100, dW1 0.060, 21 visits, 214 points; baseline W1 9.59, W1-W2 0.344; onset between MJD 57088 and 57283
- detector 2: excess 0.404 mag, z 17.9, jitter ratio 14.3
- field control: target step +0.205 (W1 +0.192); neighbours N=75, median -0.005, robust sigma 0.011, max +0.089; z = 18.8
- centroid: jump at onset 0.016" +- 0.021 (0.8 sigma, PA 342); largest consecutive-visit jump 0.045"; rms 0.034"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.380, W2-W3 1.882 (W3 S/N 57.4), W3-W4 2.434 (W4 S/N 35.2), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.02, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW -0.771 nm, varclass RS(0.54); M_G 5.18, -1.88 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): Kiso A-0904  52 [TT*; *,Em*,NIR,TT*,Y*?,Y*O] 0.01" refs=11
- ASAS-SN: 1919 points, cameras bA(g,161); bC(g,151); bE(g,178); ba(V,259, d=+0.023); bc(V,151, d=+0.026); be(V,94, d=+0.011); bi(g,286); bm(g,212); bo(g,163); bq(g,131); bs(g,133); change at onset (after-before, per-camera median) +0.023 mag; largest seasonal dimming 0.10 mag at MJD 60316
- dust: excess flux W1 5.18 mJy, W2 5.92 mJy, T = 1120 K (16-84%: 1037-1213) 

### uid1374460  [D2]  YOUNG
- position 83.85204 -6.02956; Gaia DR3 3017184808564584192; G 15.97, BP-RP 1.83, plx 2.67 mas; plot `plots/uid1374460.png`
- **young:** SIMBAD young-star types Or*,TT*,Y*O (V* NS Ori)
- flags: AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.25 mag (MJD 57044)
- NEOWISE: score refetch 3.00 (stored 3.00, reproduced True); dW2 0.564, dW1 0.465, 19 visits, 172 points; baseline W1 11.21, W1-W2 0.566; onset between MJD 57088 and 57447
- detector 2: excess 0.591 mag, z 16.5, jitter ratio 9.6
- field control: target step +0.374 (W1 +0.340); neighbours N=150, median -0.008, robust sigma 0.020, max +0.370; z = 18.7
- centroid: jump at onset 0.013" +- 0.021 (0.6 sigma, PA 331); largest consecutive-visit jump 0.062"; rms 0.033"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.584, W2-W3 2.260 (W3 S/N 12.2), W3-W4 2.433 (W4 S/N 17.5), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.14, ipd_frac_multi_peak 1, NSS none, Teff 3950 K, logg 4.65, H-alpha pEW -1.429 nm, varclass none; M_G 8.10, +0.12 mag vs sequence (on the sequence); neighbours within 10": none
- SIMBAD (10"): V* NS Ori [TT*; *,Em*,Er*,MIR,NIR,Or*,TT*,V*,Y*O] 0.02" refs=61
- ASAS-SN: 577 points, cameras bA(g,145); bE(g,36); ba(V,122, d=-0.347); be(V,145, d=+0.129); bi(g,79); bm(g,20); bq(g,30); change at onset (after-before, per-camera median) -0.109 mag; largest seasonal dimming 0.25 mag at MJD 57044
- dust: excess flux W1 4.19 mJy, W2 4.19 mJy, T = 1307 K (16-84%: 1250-1368) 

### uid1371630  [D2]  YOUNG
- position 334.22531 +70.06251; Gaia DR3 2229359472855896832; G 11.40, BP-RP 0.83, plx 2.68 mas; plot `plots/uid1371630.png`
- **young:** SIMBAD young-star types Ae*,Or*,Y*O (V* BO Cep) | Gaia DR3 variability class YSO(0.51)
- flags: binary type in SIMBAD (SB*, V* BO Cep) | Gaia DR3 NSS solution: nss_two_body_orbit | 1.10 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 0.55 (stored 0.55, reproduced True); dW2 0.122, dW1 0.102, 21 visits, 432 points; baseline W1 8.96, W1-W2 0.335; onset between MJD 57044 and 57234
- detector 2: excess 0.375 mag, z 35.1, jitter ratio 20.9
- field control: target step +0.156 (W1 +0.130); neighbours N=120, median -0.003, robust sigma 0.009, max +0.020; z = 18.7
- centroid: jump at onset 0.013" +- 0.025 (0.5 sigma, PA 286); largest consecutive-visit jump 0.053"; rms 0.053"; toward neighbour: none; expected shift if a neighbour were the source: 8.2" G15.2: 1.10"; 8.3" G19.2: 1.11"
- AllWISE 2010: W1-W2 0.352, W2-W3 1.495 (W3 S/N 70.7), W3-W4 3.151 (W4 S/N 54.7), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 0.97, ipd_frac_multi_peak 0, NSS nss_two_body_orbit, Teff 6382 K, logg 3.84, H-alpha pEW -0.102 nm, varclass YSO(0.51); M_G 3.54, -1.10 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 8.2" PA27 G15.18 dG+3.77; 8.3" PA176 G19.15 dG+7.75
- SIMBAD (10"): V* BO Cep [Ae*; *,Ae*,Em*,IR,NIR,Or*,SB*,V*,Y*O] 0.10" refs=79
- ASAS-SN: 806 points, cameras bD(g,346); bd(V,187, d=+0.007); bt(g,273); change at onset (after-before, per-camera median) +0.007 mag; largest seasonal dimming 0.01 mag at MJD 59457
- dust: excess flux W1 8.98 mJy, W2 8.47 mJy, T = 1414 K (16-84%: 1272-1595) 

### uid1630021  [D2]  YOUNG
- position 85.14672 +9.90422; Gaia DR3 3336442990534596864; G 13.58, BP-RP 1.58, plx 2.55 mas; plot `plots/uid1630021.png`
- **young:** SIMBAD young-star types Or*,Y*?,Y*O ([DM99] 214) | Gaia DR3 variability class YSO(0.68)
- flags: 1.69 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | possible optical brightening at onset (-0.055 mag, one camera only)
- NEOWISE: score refetch 4.23 (stored 4.23, reproduced True); dW2 0.314, dW1 0.279, 21 visits, 204 points; baseline W1 10.29, W1-W2 0.319; onset between MJD 57284 and 57449
- detector 2: excess 0.374 mag, z 14.8, jitter ratio 7.2
- field control: target step +0.169 (W1 +0.138); neighbours N=92, median -0.002, robust sigma 0.009, max +0.049; z = 18.4
- centroid: jump at onset 0.012" +- 0.011 (1.0 sigma, PA 69); largest consecutive-visit jump 0.059"; rms 0.026"; toward neighbour: none; expected shift if a neighbour were the source: 9.2" G16.8: 1.33"
- AllWISE 2010: W1-W2 0.314, W2-W3 2.369 (W3 S/N 58.3), W3-W4 2.624 (W4 S/N 41.7), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.07, ipd_frac_multi_peak 0, NSS none, Teff 4586 K, logg 4.13, H-alpha pEW -0.326 nm, varclass YSO(0.68); M_G 5.61, -1.69 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 9.2" PA245 G16.81 dG+3.24
- SIMBAD (10"): [DM99] 214 [Or*; *,NIR,Or*,Y*?,Y*O] 0.04" refs=24
- ASAS-SN: 923 points, cameras bA(g,175); bE(g,120); ba(V,154, d=-0.055); bi(g,236); bm(g,122); bq(g,116); change at onset (after-before, per-camera median) -0.055 mag; largest seasonal dimming 0.04 mag at MJD 57065
- dust: excess flux W1 5.17 mJy, W2 4.06 mJy, T = 1931 K (16-84%: 1757-2145) 

### uid310080  [D2]  YOUNG
- position 78.56621 -1.64957; Gaia DR3 3215095114856015232; G 11.95, BP-RP 1.44, plx 3.53 mas; plot `plots/uid310080.png`
- **young:** SIMBAD young-star types Y*?,Y*O (IRAS 05117-0142)
- flags: 2.25 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 0.42 (stored 0.41, reproduced True); dW2 0.089, dW1 0.094, 20 visits, 236 points; baseline W1 8.71, W1-W2 0.263; onset between MJD 57806 and 58005
- detector 2: excess 0.325 mag, z 15.4, jitter ratio 14.8
- field control: target step +0.189 (W1 +0.189); neighbours N=51, median -0.001, robust sigma 0.010, max +0.091; z = 18.4
- centroid: jump at onset 0.017" +- 0.018 (0.9 sigma, PA 267); largest consecutive-visit jump 0.040"; rms 0.028"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.293, W2-W3 2.464 (W3 S/N 76.3), W3-W4 2.564 (W4 S/N 49.5), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.05, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW -0.519 nm, varclass RS(0.53); M_G 4.69, -2.25 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): IRAS 05117-0142 [Y*O; *,IR,NIR,Y*?,Y*O] 0.05" refs=7
- ASAS-SN: 2647 points, cameras bC(g,183); bD(g,166); bG(g,211); bH(g,206); bc(V,119, d=+0.055); be(V,40); bg(V,185, d=+0.030); bh(V,152, d=+0.032); bk(g,298); bl(g,323); bo(g,233); bp(g,213); bs(g,143); bt(g,175); change at onset (after-before, per-camera median) +0.032 mag; largest seasonal dimming 0.03 mag at MJD 59282
- dust: excess flux W1 15.81 mJy, W2 10.53 mJy, T = 3066 K (16-84%: 2490-4061) 

### uid1683160  [D2]  YOUNG
- position 83.25872 +11.61985; Gaia DR3 3340612888382794752; G 14.93, BP-RP 1.20, plx 2.52 mas; plot `plots/uid1683160.png`
- **young:** SIMBAD young-star types Or*,Y*O (Haro 6-70)
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | possible optical brightening at onset (-0.150 mag, one camera only) | largest seasonal optical dimming 0.18 mag (MJD 58873)
- NEOWISE: score refetch 2.96 (stored 2.96, reproduced True); dW2 0.422, dW1 0.459, 21 visits, 194 points; baseline W1 10.47, W1-W2 0.784; onset between MJD 58168 and 58377
- detector 2: excess 0.844 mag, z 45.8, jitter ratio 12.5
- field control: target step +0.291 (W1 +0.276); neighbours N=92, median -0.008, robust sigma 0.016, max +0.058; z = 18.3
- centroid: jump at onset 0.020" +- 0.029 (0.7 sigma, PA 338); largest consecutive-visit jump 0.091"; rms 0.040"; toward neighbour: none; expected shift if a neighbour were the source: 8.4" G17.6: 1.97"
- AllWISE 2010: W1-W2 0.733, W2-W3 1.874 (W3 S/N 60.6), W3-W4 1.753 (W4 S/N 19.6), ext_flg 1, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.21, ipd_frac_multi_peak 0, NSS none, Teff 5962 K, logg 4.73, H-alpha pEW -6.270 nm, varclass none; M_G 6.94, +0.72 mag vs sequence (on the sequence); neighbours within 10": 8.4" PA136 G17.62 dG+2.69
- SIMBAD (10"): Haro 6-70 [Or*; *,Em*,NIR,Opt,Or*,Pu*,V*,V*?,Y*O] 0.05" refs=23
- ASAS-SN: 922 points, cameras bA(g,182); bE(g,118); ba(V,156, d=-0.150); bi(g,228); bm(g,117); bq(g,121); change at onset (after-before, per-camera median) -0.150 mag; largest seasonal dimming 0.18 mag at MJD 58873
- dust: excess flux W1 8.37 mJy, W2 8.09 mJy, T = 1364 K (16-84%: 1235-1524) 

### uid1789100  [D2]  YOUNG
- position 83.92820 -6.58105; Gaia DR3 3016940235945174400; G 14.62, BP-RP 1.62, plx 2.48 mas; plot `plots/uid1789100.png`
- **young:** SIMBAD young-star types Or*,Y*O (V* V573 Ori)
- flags: 0.81 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.58 mag (MJD 60012)
- NEOWISE: score refetch 3.24 (stored 3.24, reproduced True); dW2 0.650, dW1 0.668, 20 visits, 198 points; baseline W1 10.26, W1-W2 0.602; onset between MJD 58535 and 58742
- detector 2: excess 0.654 mag, z 24.8, jitter ratio 18.3
- field control: target step +0.388 (W1 +0.323); neighbours N=113, median -0.003, robust sigma 0.021, max +0.793; z = 18.2
- centroid: jump at onset 0.011" +- 0.018 (0.6 sigma, PA 135); largest consecutive-visit jump 0.066"; rms 0.029"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.558, W2-W3 1.424 (W3 S/N 10.4), W3-W4 2.116 (W4 S/N 7.9), ext_flg 0, ph_qual AAAB: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.24, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW -5.091 nm, varclass none; M_G 6.59, -0.81 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): V* V573 Ori [Or*; *,Em*,IR,MIR,NIR,Opt,Or*,V*,Y*O] 0.02" refs=58
- ASAS-SN: 1107 points, cameras bA(g,134, d=+0.627); bE(g,191, d=-0.142); ba(V,137); be(V,193); bi(g,177, d=-0.675); bm(g,154, d=-0.314); bq(g,121, d=-0.097); change at onset (after-before, per-camera median) -0.142 mag; largest seasonal dimming 0.58 mag at MJD 60012
- dust: excess flux W1 16.10 mJy, W2 14.14 mJy, T = 1573 K (16-84%: 1521-1628) 

### uid1481782  [D2]  YOUNG
- position 83.44367 -5.95351; Gaia DR3 3017214869037692800; G 11.81, BP-RP 1.12, plx 2.62 mas; plot `plots/uid1481782.png`
- **young:** SIMBAD young-star types Or*,Y*?,Y*O (Brun 141; Gaia DR3 3017214873335520896) | Gaia DR3 variability class YSO(0.55)
- flags: 2.07 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 0.62 (stored 0.62, reproduced True); dW2 0.092, dW1 0.062, 21 visits, 202 points; baseline W1 8.51, W1-W2 0.328; onset between MJD 59630 and 59837
- detector 2: excess 0.385 mag, z 21.8, jitter ratio 10.7
- field control: target step +0.272 (W1 +0.190); neighbours N=86, median +0.001, robust sigma 0.016, max +0.292; z = 17.4
- centroid: jump at onset 0.002" +- 0.020 (0.1 sigma, PA 44); largest consecutive-visit jump 0.085"; rms 0.038"; toward neighbour: none; expected shift if a neighbour were the source: 3.8" G15.4: 0.84"
- AllWISE 2010: W1-W2 0.338, W2-W3 2.268 (W3 S/N 66.6), W3-W4 2.056 (W4 S/N 42.6), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.13, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW -0.289 nm, varclass YSO(0.55); M_G 3.90, -2.07 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 3.8" PA258 G15.44 dG+3.64
- SIMBAD (10"): Brun 141 [Or*; *,Em*,MIR,NIR,Or*,Rad,X,Y*O] 0.03" refs=47; Gaia DR3 3017214873335520896 [Y*?; *,Y*?] 3.80" refs=6
- ASAS-SN: 1487 points, cameras bA(g,153, d=+0.042); bE(g,218, d=+0.039); ba(V,177); be(V,195); bi(g,336, d=+0.032); bm(g,242, d=+0.011); bq(g,166, d=+0.035); change at onset (after-before, per-camera median) +0.035 mag; largest seasonal dimming 0.06 mag at MJD 60654
- dust: excess flux W1 11.44 mJy, W2 13.05 mJy, T = 1121 K (16-84%: 1024-1234) 

### uid1376645  [D2]  YOUNG
- position 82.95572 -6.00537; Gaia DR3 3016848735963141760; G 13.27, BP-RP 1.43, plx 2.67 mas; plot `plots/uid1376645.png`
- **young:** SIMBAD young-star types Or*,TT*,Y*?,Y*O (V* V1207 Ori)
- flags: 1.51 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 2.16 (stored 2.16, reproduced True); dW2 0.183, dW1 0.185, 19 visits, 218 points; baseline W1 10.21, W1-W2 0.274; onset between MJD 57446 and 57645
- detector 2: excess 0.336 mag, z 16.1, jitter ratio 8.3
- field control: target step +0.219 (W1 +0.193); neighbours N=57, median +0.000, robust sigma 0.013, max +0.053; z = 17.4
- centroid: jump at onset 0.007" +- 0.013 (0.5 sigma, PA 237); largest consecutive-visit jump 0.035"; rms 0.023"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.287, W2-W3 1.963 (W3 S/N 50.3), W3-W4 3.193 (W4 S/N 33.3), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.32, ipd_frac_multi_peak 0, NSS none, Teff 4752 K, logg 4.17, H-alpha pEW -0.233 nm, varclass none; M_G 5.40, -1.51 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): V* V1207 Ori [TT*; *,Er*,MIR,NIR,Or*,TT*,V*,Y*?,Y*O] 0.01" refs=16
- ASAS-SN: 1499 points, cameras bA(g,155); bE(g,216); ba(V,177, d=+0.023); be(V,195, d=+0.001); bi(g,341); bm(g,246); bq(g,169); change at onset (after-before, per-camera median) +0.012 mag; largest seasonal dimming 0.08 mag at MJD 60315
- dust: excess flux W1 5.56 mJy, W2 3.86 mJy, T = 2658 K (16-84%: 2312-3137) 

### uid1528618  [D2]  YOUNG
- position 85.02804 -6.27194; Gaia DR3 3017010295452313984; G 12.94, BP-RP 1.55, plx 2.59 mas; plot `plots/uid1528618.png`
- **young:** SIMBAD young-star types Or*,Y*?,Y*O (V* BH Ori)
- flags: 2.22 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.38 mag (MJD 59858)
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 21 visits, 242 points; baseline W1 9.03, W1-W2 0.345; onset between MJD 56730 and 56921
- detector 2: excess 0.402 mag, z 16.4, jitter ratio 9.2
- field control: target step +0.286 (W1 +0.315); neighbours N=67, median +0.003, robust sigma 0.016, max +0.062; z = 17.4
- centroid: jump at onset 0.018" +- 0.017 (1.0 sigma, PA 322); largest consecutive-visit jump 0.039"; rms 0.023"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.347, W2-W3 1.971 (W3 S/N 68.0), W3-W4 2.754 (W4 S/N 40.4), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.21, ipd_frac_multi_peak 0, NSS none, Teff 4904 K, logg 4.09, H-alpha pEW -0.221 nm, varclass none; M_G 5.01, -2.22 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): V* BH Ori [Or*; *,Em*,MIR,NIR,Or*,RR*,V*,Y*?,Y*O,ev] 0.05" refs=16
- ASAS-SN: 1128 points, cameras bB(g,93); bF(g,189); ba(V,30); bb(V,129); bf(V,144); bj(g,262); bn(g,114); br(g,167); change at onset (after-before, per-camera median) n/a mag; largest seasonal dimming 0.38 mag at MJD 59858
- dust: excess flux W1 18.01 mJy, W2 13.56 mJy, T = 2125 K (16-84%: 1955-2330) 
- checks missing: ASAS-SN change at onset (no camera spans the onset)

### uid1418968  [D2]  YOUNG
- position 82.38512 +13.18382; Gaia DR3 3389153818487630848; G 15.53, BP-RP 2.01, plx 2.65 mas; plot `plots/uid1418968.png`
- **young:** SIMBAD young-star types Y*?,Y*O (UCAC4 516-012684)
- flags: 0.86 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 1.53 (stored 1.53, reproduced True); dW2 0.138, dW1 0.152, 20 visits, 170 points; baseline W1 10.89, W1-W2 0.756; onset between MJD 57281 and 57446
- detector 2: excess 0.748 mag, z 18.0, jitter ratio 7.6
- field control: target step +0.191 (W1 +0.156); neighbours N=86, median -0.001, robust sigma 0.011, max +0.026; z = 17.3
- centroid: jump at onset 0.012" +- 0.020 (0.6 sigma, PA 281); largest consecutive-visit jump 0.048"; rms 0.037"; toward neighbour: none; expected shift if a neighbour were the source: 6.6" G21.0: 1.06"; 7.3" G17.6: 1.18"
- AllWISE 2010: W1-W2 0.706, W2-W3 1.344 (W3 S/N 38.0), W3-W4 1.147 (W4 S/N 7.1), ext_flg 0, ph_qual AAAB: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.03, ipd_frac_multi_peak 0, NSS none, Teff 3645 K, logg 4.12, H-alpha pEW 0.091 nm, varclass none; M_G 7.65, -0.86 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 6.6" PA338 G21.01 dG+5.48; 7.3" PA111 G17.58 dG+2.05
- SIMBAD (10"): UCAC4 516-012684 [Y*O; *,MIR,NIR,Y*?,Y*O] 0.08" refs=3
- ASAS-SN: 756 points, cameras bD(g,184); bH(g,96); bd(V,170, d=-0.001); bl(g,145); bp(g,77); bt(g,84); change at onset (after-before, per-camera median) -0.001 mag; largest seasonal dimming 0.07 mag at MJD 59140
- dust: excess flux W1 2.23 mJy, W2 2.07 mJy, T = 1445 K (16-84%: 1289-1651) 

### uid1513819  [D2]  YOUNG
- position 78.08555 -2.93124; Gaia DR3 3214585594296140416; G 12.69, BP-RP 1.33, plx 2.60 mas; plot `plots/uid1513819.png`
- **young:** SIMBAD young-star types Or* (V* V531 Ori) | Gaia DR3 variability class YSO(0.68)
- flags: 1.88 mag above the main sequence at its colour | optical dimming +0.113 mag after the infrared onset (debris transit signature) | largest seasonal optical dimming 0.26 mag (MJD 59281)
- NEOWISE: score refetch 1.50 (stored 1.50, reproduced True); dW2 0.215, dW1 0.161, 21 visits, 220 points; baseline W1 8.61, W1-W2 0.391; onset between MJD 57640 and 57805
- detector 2: excess 0.454 mag, z 23.3, jitter ratio 12.7
- field control: target step +0.246 (W1 +0.178); neighbours N=53, median -0.004, robust sigma 0.015, max +0.349; z = 16.9
- centroid: jump at onset 0.012" +- 0.018 (0.7 sigma, PA 115); largest consecutive-visit jump 0.042"; rms 0.025"; toward neighbour: 5.8" PA139 G20.3 (angle 24 deg); expected shift if a neighbour were the source: 5.8" G20.3: 1.19"
- AllWISE 2010: W1-W2 0.405, W2-W3 0.780 (W3 S/N 64.1), W3-W4 2.808 (W4 S/N 35.5), ext_flg 0, ph_qual AAAA: weak W3 excess (0.5 < W2-W3 < 1.0)
- Gaia: RUWE 1.35, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW 0.003 nm, varclass YSO(0.68); M_G 4.77, -1.88 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 5.8" PA139 G20.32 dG+7.63
- SIMBAD (10"): V* V531 Ori [Or*; *,Er*,NIR,Or*,Pe*,V*,X] 0.02" refs=18
- ASAS-SN: 1444 points, cameras bC(g,183); bG(g,213); bc(V,119, d=+0.131); be(V,40); bg(V,187, d=+0.094); bk(g,299); bo(g,241); bs(g,162); change at onset (after-before, per-camera median) +0.113 mag; largest seasonal dimming 0.26 mag at MJD 59281
- dust: excess flux W1 21.46 mJy, W2 21.49 mJy, T = 1304 K (16-84%: 1230-1388) 

### uid2074984  [D2]  YOUNG
- position 85.32719 -7.43925; Gaia DR3 3016017333372618240; G 15.09, BP-RP 1.84, plx 2.36 mas; plot `plots/uid2074984.png`
- **young:** SIMBAD young-star types Y*?,Y*O (Haro 4-485)
- flags: 1.07 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.23 mag (MJD 59167)
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 21 visits, 227 points; baseline W1 10.03, W1-W2 0.576; onset between MJD 56922 and 57089
- detector 2: excess 0.599 mag, z 16.4, jitter ratio 10.3
- field control: target step +0.162 (W1 +0.172); neighbours N=64, median -0.007, robust sigma 0.010, max +0.058; z = 16.3
- centroid: jump at onset 0.026" +- 0.017 (1.5 sigma, PA 73); largest consecutive-visit jump 0.063"; rms 0.038"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.578, W2-W3 2.370 (W3 S/N 58.2), W3-W4 1.882 (W4 S/N 30.0), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.19, ipd_frac_multi_peak 0, NSS none, Teff 3825 K, logg 4.23, H-alpha pEW -2.386 nm, varclass none; M_G 6.96, -1.07 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): Haro 4-485 [Y*O; *,Em*,MIR,NIR,Y*?,Y*O] 0.01" refs=21
- ASAS-SN: 981 points, cameras bB(g,93); bF(g,180); ba(V,28); bb(V,125); bf(V,139); bj(g,241); bn(g,23); br(g,152); change at onset (after-before, per-camera median) n/a mag; largest seasonal dimming 0.23 mag at MJD 59167
- dust: excess flux W1 4.47 mJy, W2 3.81 mJy, T = 1650 K (16-84%: 1420-2001) 
- checks missing: ASAS-SN change at onset (no camera spans the onset)

### uid1694582  [D2]  YOUNG
- position 84.81338 +9.83455; Gaia DR3 3336450446597891584; G 11.55, BP-RP 1.08, plx 2.52 mas; plot `plots/uid1694582.png`
- **young:** SIMBAD young-star types Y*O (SS  30)
- flags: 2.26 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | not plain dust: optical brightening -0.016 mag (per-camera -0.011,-0.020) together with the infrared rise
- NEOWISE: score refetch 0.61 (stored 0.61, reproduced True); dW2 0.055, dW1 0.071, 21 visits, 215 points; baseline W1 8.63, W1-W2 0.326; onset between MJD 58379 and 58537
- detector 2: excess 0.381 mag, z 23.2, jitter ratio 7.9
- field control: target step +0.233 (W1 +0.236); neighbours N=94, median +0.000, robust sigma 0.014, max +0.052; z = 16.1
- centroid: jump at onset 0.005" +- 0.018 (0.3 sigma, PA 61); largest consecutive-visit jump 0.041"; rms 0.028"; toward neighbour: 3.1" PA92 G19.1 (angle 32 deg); expected shift if a neighbour were the source: 2.1" G18.5: 0.41"; 3.1" G19.1: 0.61"; 8.7" G17.6: 1.68"
- AllWISE 2010: W1-W2 0.297, W2-W3 2.295 (W3 S/N 69.9), W3-W4 2.179 (W4 S/N 46.7), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.23, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW -0.532 nm, varclass none; M_G 3.55, -2.26 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 2.1" PA128 G18.54 dG+6.99; 3.1" PA92 G19.08 dG+7.53; 8.7" PA250 G17.56 dG+6.01
- SIMBAD (10"): SS  30 [Y*O; *,Em*,MIR,NIR,X,Y*O] 0.04" refs=22
- ASAS-SN: 937 points, cameras bA(g,184); bE(g,120); ba(V,155); bi(g,235, d=-0.011); bm(g,122); bq(g,121, d=-0.020); change at onset (after-before, per-camera median) -0.016 mag; largest seasonal dimming 0.08 mag at MJD 60567
- dust: excess flux W1 18.72 mJy, W2 11.21 mJy, T = 5369 K (16-84%: 3714-8000) 

### uid878866  [D2]  YOUNG
- position 88.42049 +1.63723; Gaia DR3 3315801583867579392; G 13.11, BP-RP 1.77, plx 2.99 mas; plot `plots/uid878866.png`
- **young:** SIMBAD young-star types Or*,TT*,Y*O (EM* LkHA  334) | Gaia DR3 variability class YSO(0.69)
- flags: 2.33 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.25 mag (MJD 59133)
- NEOWISE: score refetch 3.76 (stored 3.76, reproduced True); dW2 0.224, dW1 0.240, 21 visits, 211 points; baseline W1 8.27, W1-W2 0.562; onset between MJD 57287 and 57452
- detector 2: excess 0.597 mag, z 18.4, jitter ratio 5.2
- field control: target step +0.187 (W1 +0.144); neighbours N=96, median -0.002, robust sigma 0.012, max +0.123; z = 15.9
- centroid: jump at onset 0.008" +- 0.018 (0.4 sigma, PA 294); largest consecutive-visit jump 0.045"; rms 0.039"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.619, W2-W3 1.849 (W3 S/N 77.1), W3-W4 1.734 (W4 S/N 44.2), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.35, ipd_frac_multi_peak 0, NSS none, Teff 5744 K, logg 3.91, H-alpha pEW -0.695 nm, varclass YSO(0.69); M_G 5.49, -2.33 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): EM* LkHA  334 [TT*; *,Em*,IR,NIR,Or*,TT*,V*,Y*O,ev] 0.08" refs=24
- ASAS-SN: 890 points, cameras bA(g,91); bB(g,91); bE(g,69); bF(g,54); bi(g,125); bj(g,118); bm(g,80); bn(g,74); bq(g,104); br(g,84); change at onset (after-before, per-camera median) n/a mag; largest seasonal dimming 0.25 mag at MJD 59133
- dust: excess flux W1 23.86 mJy, W2 20.40 mJy, T = 1646 K (16-84%: 1476-1866) 
- checks missing: ASAS-SN change at onset (no camera spans the onset)

### uid1726162  [D2]  YOUNG
- position 88.06969 +1.04786; Gaia DR3 3219704297663377536; G 12.83, BP-RP 1.60, plx 2.50 mas; plot `plots/uid1726162.png`
- **young:** SIMBAD young-star types Y*O (IRAS 05497+0102) | Gaia DR3 variability class YSO(0.76)
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | 2.56 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 0.43 (stored 0.43, reproduced True); dW2 0.074, dW1 0.090, 12 visits, 173 points; baseline W1 8.37, W1-W2 0.487; onset between MJD 58539 and 58904
- detector 2: excess 0.540 mag, z 20.7, jitter ratio 13.1
- field control: target step +0.195 (W1 +0.215); neighbours N=97, median -0.002, robust sigma 0.013, max +0.042; z = 15.6
- centroid: jump at onset 0.025" +- 0.025 (1.0 sigma, PA 249); largest consecutive-visit jump 0.058"; rms 0.025"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.487, W2-W3 1.837 (W3 S/N 63.1), W3-W4 3.204 (W4 S/N 50.8), ext_flg 1, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.18, ipd_frac_multi_peak 0, NSS none, Teff 5808 K, logg 4.04, H-alpha pEW -0.157 nm, varclass YSO(0.76); M_G 4.82, -2.56 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): IRAS 05497+0102 [Y*O; *,Em*,IR,MIR,NIR,Y*O] 0.02" refs=4
- ASAS-SN: 455 points, cameras bB(g,98, d=-0.084); bF(g,61); bj(g,125, d=+0.012); bn(g,78); br(g,93, d=-0.030); change at onset (after-before, per-camera median) -0.030 mag; largest seasonal dimming 0.07 mag at MJD 59497
- dust: excess flux W1 12.22 mJy, W2 10.19 mJy, T = 1720 K (16-84%: 1440-2164) 

### uid1117853  [D2]  YOUNG
- position 82.34693 -1.42096; Gaia DR3 3220241585188156032; G 14.29, BP-RP 1.70, plx 2.82 mas; plot `plots/uid1117853.png`
- **young:** SIMBAD young-star types Or*,TT*,Y*?,Y*O (Kiso A-0903 176) | Gaia DR3 variability class YSO(0.57)
- flags: 1.07 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 1.04 (stored 1.04, reproduced True); dW2 0.134, dW1 0.128, 20 visits, 240 points; baseline W1 9.51, W1-W2 0.532; onset between MJD 58167 and 58376
- detector 2: excess 0.576 mag, z 19.6, jitter ratio 7.6
- field control: target step +0.184 (W1 +0.131); neighbours N=81, median -0.007, robust sigma 0.013, max +0.123; z = 15.1
- centroid: jump at onset 0.006" +- 0.017 (0.4 sigma, PA 213); largest consecutive-visit jump 0.053"; rms 0.024"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.539, W2-W3 1.888 (W3 S/N 61.6), W3-W4 2.095 (W4 S/N 40.3), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.20, ipd_frac_multi_peak 0, NSS none, Teff 5746 K, logg 4.35, H-alpha pEW -2.136 nm, varclass YSO(0.57); M_G 6.55, -1.07 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): Kiso A-0903 176 [TT*; *,Em*,NIR,Opt,Or*,Pu*,TT*,Y*?,Y*O] 0.03" refs=51
- ASAS-SN: 0 points, cameras n/a; change at onset (after-before, per-camera median) n/a mag; largest seasonal dimming n/a mag at MJD n/a
- dust: excess flux W1 4.26 mJy, W2 5.52 mJy, T = 989 K (16-84%: 839-1188) 
- checks missing: ASAS-SN (no source)

### uid1384448  [D2]  YOUNG
- position 122.09315 -47.18316; Gaia DR3 5519261437566810112; G 14.42, BP-RP 1.77, plx 2.67 mas; plot `plots/uid1384448.png`
- **young:** SIMBAD young-star types Or*,Y*?,Y*O (2MASS J08082235-4710594) | Gaia DR3 variability class YSO(0.50)
- flags: 1.27 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.17 mag (MJD 58084)
- NEOWISE: score refetch 0.80 (stored 0.80, reproduced True); dW2 0.111, dW1 0.184, 18 visits, 236 points; baseline W1 9.45, W1-W2 0.573; onset between MJD 59695 and 59904
- detector 2: excess 0.607 mag, z 18.7, jitter ratio 7.5
- field control: target step +0.214 (W1 +0.192); neighbours N=182, median +0.003, robust sigma 0.014, max +0.071; z = 15.0
- centroid: jump at onset 0.007" +- 0.022 (0.3 sigma, PA 326); largest consecutive-visit jump 0.078"; rms 0.031"; toward neighbour: none; expected shift if a neighbour were the source: 2.8" G18.1: 0.50"
- AllWISE 2010: W1-W2 0.546, W2-W3 1.183 (W3 S/N 64.3), W3-W4 2.061 (W4 S/N 34.3), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.03, ipd_frac_multi_peak 0, NSS none, Teff 5052 K, logg 4.27, H-alpha pEW -0.759 nm, varclass YSO(0.50); M_G 6.55, -1.27 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 2.8" PA183 G18.07 dG+3.65
- SIMBAD (10"): 2MASS J08082235-4710594 [Or*; *,NIR,Or*,Y*?,Y*O] 0.17" refs=17
- ASAS-SN: 2405 points, cameras bE(g,391, d=-0.080); bF(g,371, d=+0.064); be(V,221); bf(V,187); bi(g,500, d=+0.074); bj(g,395, d=+0.115); bm(g,162, d=-0.188); bn(g,178, d=-0.162); change at onset (after-before, per-camera median) -0.008 mag; largest seasonal dimming 0.17 mag at MJD 58084
- dust: excess flux W1 9.50 mJy, W2 8.26 mJy, T = 1600 K (16-84%: 1445-1787) 

### uid1575501  [D2]  YOUNG
- position 56.92898 +35.01225; Gaia DR3 219832339066395776; G 12.56, BP-RP 1.19, plx 2.57 mas; plot `plots/uid1575501.png`
- **young:** Gaia DR3 variability class YSO(0.25)
- flags: 1.59 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.15 mag (MJD 59619)
- NEOWISE: score refetch 0.29 (stored 0.29, reproduced True); dW2 0.043, dW1 0.113, 21 visits, 224 points; baseline W1 9.40, W1-W2 0.475; onset between MJD 58150 and 58355
- detector 2: excess 0.535 mag, z 29.4, jitter ratio 10.4
- field control: target step +0.195 (W1 +0.232); neighbours N=59, median -0.002, robust sigma 0.013, max +0.035; z = 14.8
- centroid: jump at onset 0.035" +- 0.014 (2.4 sigma, PA 79); largest consecutive-visit jump 0.040"; rms 0.031"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.459, W2-W3 1.929 (W3 S/N 61.6), W3-W4 1.584 (W4 S/N 29.8), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 0.99, ipd_frac_multi_peak 0, NSS none, Teff 5266 K, logg 4.14, H-alpha pEW 0.094 nm, varclass YSO(0.25); M_G 4.61, -1.59 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): NSV  1302 [V*; *,NIR,V*] 0.09" refs=11
- ASAS-SN: 415 points, cameras bB(g,135); bb(V,59, d=+0.049); br(g,221); change at onset (after-before, per-camera median) +0.049 mag; largest seasonal dimming 0.15 mag at MJD 59619
- dust: excess flux W1 7.08 mJy, W2 4.55 mJy, T = 3572 K (16-84%: 2581-6282) 

### uid1768213  [D2]  YOUNG
- position 85.05360 -2.36729; Gaia DR3 3216496923462354176; G 12.85, BP-RP 1.74, plx 2.48 mas; plot `plots/uid1768213.png`
- **young:** SIMBAD young-star types TT*,Y*O (Haro 5-38)
- flags: 2.90 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | not plain dust: optical brightening -0.034 mag (per-camera -0.027,-0.037,-0.036,-0.034,-0.004) together with the infrared rise
- NEOWISE: score refetch 1.66 (stored 1.67, reproduced True); dW2 0.312, dW1 0.268, 20 visits, 199 points; baseline W1 8.77, W1-W2 0.554; onset between MJD 59110 and 59265
- detector 2: excess 0.593 mag, z 18.8, jitter ratio 15.1
- field control: target step +0.277 (W1 +0.214); neighbours N=112, median -0.001, robust sigma 0.019, max +0.053; z = 14.7
- centroid: jump at onset 0.023" +- 0.020 (1.1 sigma, PA 164); largest consecutive-visit jump 0.074"; rms 0.032"; toward neighbour: none; expected shift if a neighbour were the source: 9.1" G20.9: 2.04"
- AllWISE 2010: W1-W2 0.521, W2-W3 1.746 (W3 S/N 63.0), W3-W4 1.700 (W4 S/N 39.0), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 0.97, ipd_frac_multi_peak 0, NSS none, Teff 5140 K, logg 3.66, H-alpha pEW -0.795 nm, varclass none; M_G 4.83, -2.90 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 9.1" PA84 G20.87 dG+8.02
- SIMBAD (10"): Haro 5-38 [TT*; *,Em*,IR,NIR,TT*,X,Y*O] 0.08" refs=26
- ASAS-SN: 1403 points, cameras bC(g,159, d=-0.027); bG(g,223, d=-0.037); bc(V,151); be(V,38); bg(V,153); bk(g,305, d=-0.036); bo(g,215, d=-0.034); bs(g,159, d=-0.004); change at onset (after-before, per-camera median) -0.034 mag; largest seasonal dimming 0.05 mag at MJD 58729
- dust: excess flux W1 21.98 mJy, W2 26.29 mJy, T = 1067 K (16-84%: 1022-1116) 

### uid1911695  [D2]  YOUNG
- position 85.49918 +0.59084; Gaia DR3 3219454845962435328; G 12.51, BP-RP 1.35, plx 2.42 mas; plot `plots/uid1911695.png`
- **young:** SIMBAD young-star types Y*?,Y*O (2MASS J05415980+0035270)
- flags: 2.28 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | optical dimming +0.066 mag after the infrared onset (debris transit signature) | largest seasonal optical dimming 0.57 mag (MJD 58152)
- NEOWISE: score refetch 0.76 (stored 0.76, reproduced True); dW2 0.104, dW1 0.065, 20 visits, 232 points; baseline W1 8.70, W1-W2 0.357; onset between MJD 57449 and 57648
- detector 2: excess 0.420 mag, z 20.9, jitter ratio 7.9
- field control: target step +0.170 (W1 +0.138); neighbours N=75, median -0.003, robust sigma 0.012, max +0.031; z = 14.5
- centroid: jump at onset 0.016" +- 0.012 (1.4 sigma, PA 112); largest consecutive-visit jump 0.048"; rms 0.027"; toward neighbour: 1.8" PA121 G19.6 (angle 10 deg); expected shift if a neighbour were the source: 1.8" G19.6: 0.26"
- AllWISE 2010: W1-W2 0.363, W2-W3 1.835 (W3 S/N 67.5), W3-W4 1.842 (W4 S/N 40.3), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.14, ipd_frac_multi_peak 0, NSS none, Teff 5394 K, logg 3.79, H-alpha pEW -0.247 nm, varclass none; M_G 4.43, -2.28 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 1.8" PA121 G19.61 dG+7.10
- SIMBAD (10"): 2MASS J05415980+0035270 [Y*O; *,NIR,Y*?,Y*O] 0.02" refs=14
- ASAS-SN: 1014 points, cameras bB(g,99); bF(g,151); bb(V,181, d=+0.066); bj(g,197); bn(g,133); br(g,177); cB(g,76); change at onset (after-before, per-camera median) +0.066 mag; largest seasonal dimming 0.57 mag at MJD 58152
- dust: excess flux W1 8.54 mJy, W2 11.35 mJy, T = 967 K (16-84%: 880-1069) 

### uid2209125  [D2]  YOUNG
- position 126.75697 -46.41083; Gaia DR3 5516553684028849920; G 13.63, BP-RP 1.51, plx 2.31 mas; plot `plots/uid2209125.png`
- **young:** SIMBAD young-star types Y*?,Y*O (Gaia DR3 5516553684028849920)
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | 1.67 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 1.41 (stored 1.41, reproduced True); dW2 0.156, dW1 0.172, 17 visits, 210 points; baseline W1 9.69, W1-W2 0.408; onset between MJD 58240 and 58604
- detector 2: excess 0.467 mag, z 20.1, jitter ratio 9.8
- field control: target step +0.172 (W1 +0.186); neighbours N=176, median -0.001, robust sigma 0.012, max +0.050; z = 14.1
- centroid: jump at onset 0.014" +- 0.018 (0.7 sigma, PA 30); largest consecutive-visit jump 0.041"; rms 0.026"; toward neighbour: 9.2" PA3 G20.8 (angle 26 deg); expected shift if a neighbour were the source: 2.2" G19.9: 0.32"; 4.1" G20.9: 0.60"; 4.5" G20.6: 0.65"; 7.0" G19.4: 1.02"; 9.1" G17.1: 1.34"; 9.2" G20.8: 1.34"
- AllWISE 2010: W1-W2 0.412, W2-W3 1.767 (W3 S/N 62.6), W3-W4 1.926 (W4 S/N 32.3), ext_flg 1, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.08, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW -1.254 nm, varclass RS(0.42); M_G 5.45, -1.67 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 2.2" PA102 G19.94 dG+6.32; 4.1" PA295 G20.89 dG+7.27; 4.5" PA287 G20.61 dG+6.98; 7.0" PA167 G19.41 dG+5.78; 9.1" PA114 G17.10 dG+3.47; 9.2" PA3 G20.82 dG+7.20
- SIMBAD (10"): Gaia DR3 5516553684028849920 [Y*?; *,Y*?,Y*O] 0.15" refs=2
- ASAS-SN: 1221 points, cameras bE(g,395); be(V,186); bi(g,439); bm(g,201); change at onset (after-before, per-camera median) n/a mag; largest seasonal dimming 0.07 mag at MJD 60264
- dust: excess flux W1 7.26 mJy, W2 5.19 mJy, T = 2423 K (16-84%: 1969-3237) 
- checks missing: ASAS-SN change at onset (no camera spans the onset)

### uid1604479  [D2]  YOUNG
- position 83.85466 -6.79903; Gaia DR3 3016548431848965888; G 13.94, BP-RP 1.53, plx 2.56 mas; plot `plots/uid1604479.png`
- **young:** SIMBAD young-star types Or*,Y*O (V* NT Ori) | Gaia DR3 variability class YSO(0.43)
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | 1.20 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.48 mag (MJD 59514)
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 20 visits, 196 points; baseline W1 9.04, W1-W2 0.613; onset between MJD 58377 and 58535
- detector 2: excess 0.671 mag, z 28.1, jitter ratio 22.2
- field control: target step +0.254 (W1 +0.281); neighbours N=95, median -0.007, robust sigma 0.019, max +0.138; z = 14.1
- centroid: jump at onset 0.025" +- 0.017 (1.5 sigma, PA 154); largest consecutive-visit jump 0.069"; rms 0.028"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.563, W2-W3 1.663 (W3 S/N 57.8), W3-W4 1.923 (W4 S/N 26.9), ext_flg 1, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.21, ipd_frac_multi_peak 0, NSS none, Teff 6110 K, logg 4.31, H-alpha pEW -3.954 nm, varclass YSO(0.43); M_G 5.98, -1.20 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): V* NT Ori [Or*; *,Em*,Er*,MIR,NIR,Opt,Or*,V*,V*?,Y*O] 0.01" refs=52
- ASAS-SN: 998 points, cameras bA(g,145); bE(g,117, d=-0.222); ba(V,136); be(V,194); bi(g,203, d=-0.259); bm(g,150, d=-0.180); bq(g,53, d=+0.054); change at onset (after-before, per-camera median) -0.201 mag; largest seasonal dimming 0.48 mag at MJD 59514
- dust: excess flux W1 1.70 mJy, W2 0.24 mJy, T = 8000 K (16-84%: 8000-8000) ratio bluer than an 8000 K blackbody (not dust-like)

### uid1760111  [D2]  YOUNG
- position 83.84041 -5.57969; Gaia DR3 3017252943925578752; G 13.33, BP-RP 1.27, plx 2.49 mas; plot `plots/uid1760111.png`
- **young:** SIMBAD young-star types Or*,TT*,TT?,Y*O (V* AG Ori) | Gaia DR3 variability class YSO(0.40)
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | 1.15 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | not plain dust: optical brightening -0.214 mag (per-camera -0.214,-0.237,-0.134) together with the infrared rise | largest seasonal optical dimming 0.33 mag (MJD 60046)
- NEOWISE: score refetch 1.21 (stored 1.21, reproduced True); dW2 0.241, dW1 0.253, 14 visits, 113 points; baseline W1 8.98, W1-W2 0.784; onset between MJD 58168 and 58377
- detector 2: excess 0.846 mag, z 43.9, jitter ratio 13.0
- field control: target step +0.445 (W1 +0.459); neighbours N=109, median -0.005, robust sigma 0.033, max +0.260; z = 13.5
- centroid: jump at onset 0.022" +- 0.029 (0.8 sigma, PA 146); largest consecutive-visit jump 0.069"; rms 0.032"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.803, W2-W3 2.282 (W3 S/N 48.1), W3-W4 2.543 (W4 S/N 22.2), ext_flg 1, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.34, ipd_frac_multi_peak 0, NSS none, Teff 5777 K, logg 4.24, H-alpha pEW -4.097 nm, varclass YSO(0.40); M_G 5.31, -1.15 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): V* AG Ori [TT*; *,Em*,FIR,MIR,NIR,Or*,Rad,TT*,TT?,V*,X,Y*O] 0.02" refs=65
- ASAS-SN: 1220 points, cameras bA(g,145); bE(g,211); ba(V,136); be(V,194); bi(g,291, d=-0.214); bm(g,147, d=-0.237); bq(g,96, d=-0.134); change at onset (after-before, per-camera median) -0.214 mag; largest seasonal dimming 0.33 mag at MJD 60046
- dust: excess flux W1 26.02 mJy, W2 25.18 mJy, T = 1364 K (16-84%: 1240-1528) 

### uid979261  [D2]  YOUNG
- position 83.41595 -0.64834; Gaia DR3 3220685100690997632; G 13.66, BP-RP 1.73, plx 2.91 mas; plot `plots/uid979261.png`
- **young:** SIMBAD young-star types Or*,TT*,Y*O (V* V543 Ori) | Gaia DR3 variability class YSO(0.24)
- flags: 1.74 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.26 mag (MJD 58885)
- NEOWISE: score refetch 0.98 (stored 0.98, reproduced True); dW2 0.155, dW1 0.127, 20 visits, 211 points; baseline W1 9.53, W1-W2 0.420; onset between MJD 59263 and 59473
- detector 2: excess 0.459 mag, z 14.6, jitter ratio 15.8
- field control: target step +0.186 (W1 +0.119); neighbours N=77, median -0.003, robust sigma 0.014, max +0.053; z = 13.4
- centroid: jump at onset 0.004" +- 0.013 (0.3 sigma, PA 88); largest consecutive-visit jump 0.063"; rms 0.026"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.380, W2-W3 1.873 (W3 S/N 59.9), W3-W4 2.123 (W4 S/N 27.8), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.12, ipd_frac_multi_peak 0, NSS none, Teff 5602 K, logg 4.20, H-alpha pEW -0.885 nm, varclass YSO(0.24); M_G 5.98, -1.74 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): V* V543 Ori [TT*; *,NIR,Or*,TT*,V*,V*?,Y*O] 0.03" refs=26
- ASAS-SN: 1465 points, cameras bC(g,151, d=+0.036); bG(g,221, d=-0.003); ba(V,51); bc(V,151); be(V,38); bg(V,153); bk(g,307, d=-0.057); bo(g,233, d=-0.130); bs(g,160, d=-0.181); change at onset (after-before, per-camera median) -0.057 mag; largest seasonal dimming 0.26 mag at MJD 58885
- dust: excess flux W1 8.16 mJy, W2 7.76 mJy, T = 1398 K (16-84%: 1248-1582) 

### uid1016323  [D2]  YOUNG
- position 333.30125 +73.54962; Gaia DR3 2278977408959483264; G 13.42, BP-RP 1.73, plx 2.89 mas; plot `plots/uid1016323.png`
- **young:** SIMBAD young-star types Or*,Y*?,Y*O (2MASS J22131219+7332585) | Gaia DR3 variability class YSO(0.81)
- flags: 1.97 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.16 mag (MJD 60438)
- NEOWISE: score refetch 0.01 (stored 0.01, reproduced True); dW2 0.002, dW1 0.003, 10 visits, 100 points; baseline W1 8.75, W1-W2 0.446; onset between MJD 60165 and 60324
- detector 2: excess 0.486 mag, z 15.6, jitter ratio 13.0
- field control: target step +0.199 (W1 +0.234); neighbours N=84, median +0.007, robust sigma 0.014, max +0.053; z = 13.3
- centroid: jump at onset 0.147" +- 0.224 (0.7 sigma, PA 176); largest consecutive-visit jump 0.137"; rms 0.101"; toward neighbour: none; expected shift if a neighbour were the source: 1.8" G17.8: 0.31"; 2.5" G18.6: 0.41"
- AllWISE 2010: W1-W2 0.412, W2-W3 1.853 (W3 S/N 68.4), W3-W4 2.190 (W4 S/N 42.0), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.12, ipd_frac_multi_peak 0, NSS none, Teff 5506 K, logg 4.16, H-alpha pEW -1.443 nm, varclass YSO(0.81); M_G 5.73, -1.97 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 1.8" PA263 G17.78 dG+4.35; 2.5" PA76 G18.60 dG+5.18
- SIMBAD (10"): 2MASS J22131219+7332585 [Or*; *,Em*,NIR,Or*,Y*?,Y*O] 0.09" refs=9
- ASAS-SN: 1361 points, cameras bA(g,325, d=-0.035); bB(g,110); ba(V,250); bb(V,163); bq(g,262, d=+0.072); br(g,251, d=+0.030); change at onset (after-before, per-camera median) +0.030 mag; largest seasonal dimming 0.16 mag at MJD 60438
- dust: excess flux W1 1.79 mJy, W2 3.35 mJy, T = 746 K (16-84%: 540-1035) 

### uid1673027  [D2]  YOUNG
- position 84.02119 -6.49228; Gaia DR3 3016947206676163968; G 13.91, BP-RP 1.67, plx 2.53 mas; plot `plots/uid1673027.png`
- **young:** SIMBAD young-star types Or*,TT*,Y*O (V* AW Ori) | Gaia DR3 variability class YSO(0.45)
- flags: 1.65 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | optical dimming +1.028 mag after the infrared onset (debris transit signature) | largest seasonal optical dimming 1.41 mag (MJD 60406)
- NEOWISE: score refetch 3.04 (stored 3.04, reproduced True); dW2 0.267, dW1 0.078, 20 visits, 182 points; baseline W1 9.37, W1-W2 0.450; onset between MJD 59473 and 59631
- detector 2: excess 0.496 mag, z 17.6, jitter ratio 8.4
- field control: target step +0.215 (W1 -0.060); neighbours N=123, median +0.003, robust sigma 0.016, max +0.565; z = 13.0
- centroid: jump at onset 0.026" +- 0.016 (1.6 sigma, PA 276); largest consecutive-visit jump 0.030"; rms 0.029"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.506, W2-W3 1.730 (W3 S/N 54.1), W3-W4 1.840 (W4 S/N 29.3), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.03, ipd_frac_multi_peak 0, NSS none, Teff 5552 K, logg 4.24, H-alpha pEW -1.187 nm, varclass YSO(0.45); M_G 5.92, -1.65 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): V* AW Ori [TT*; *,Em*,MIR,NIR,Opt,Or*,TT*,V*,X,Y*O] 0.02" refs=44
- ASAS-SN: 1155 points, cameras bA(g,130, d=+1.447); bE(g,166, d=+1.147); ba(V,163); be(V,194); bi(g,195, d=+0.725); bm(g,169); bq(g,138, d=+0.909); change at onset (after-before, per-camera median) +1.028 mag; largest seasonal dimming 1.41 mag at MJD 60406
- dust: excess flux W1 10.22 mJy, W2 15.02 mJy, T = 888 K (16-84%: 840-944) 

### uid1988767  [D2]  YOUNG
- position 84.68362 -11.23644; Gaia DR3 3010160441090944128; G 11.10, BP-RP 0.86, plx 2.39 mas; plot `plots/uid1988767.png`
- **young:** SIMBAD young-star types Y*O (IRAS 05363-1115)
- flags: 1.80 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 0.99 (stored 0.99, reproduced True); dW2 0.148, dW1 0.120, 21 visits, 220 points; baseline W1 8.93, W1-W2 0.488; onset between MJD 57447 and 57647
- detector 2: excess 0.530 mag, z 46.1, jitter ratio 11.8
- field control: target step +0.189 (W1 +0.207); neighbours N=45, median -0.003, robust sigma 0.015, max +0.025; z = 13.0
- centroid: jump at onset 0.013" +- 0.018 (0.7 sigma, PA 47); largest consecutive-visit jump 0.072"; rms 0.032"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.503, W2-W3 2.667 (W3 S/N 72.1), W3-W4 1.831 (W4 S/N 53.8), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.13, ipd_frac_multi_peak 0, NSS none, Teff 5846 K, logg 3.75, H-alpha pEW 0.032 nm, varclass none; M_G 3.00, -1.80 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): IRAS 05363-1115 [Y*O; *,IR,NIR,Y*O] 0.02" refs=2
- ASAS-SN: 1494 points, cameras bC(g,124); bG(g,256); ba(V,27); bc(V,112, d=+0.029); be(V,35); bg(V,214, d=+0.028); bk(g,339); bo(g,263); bs(g,124); change at onset (after-before, per-camera median) +0.028 mag; largest seasonal dimming 0.04 mag at MJD 60311
- dust: excess flux W1 13.60 mJy, W2 11.49 mJy, T = 1681 K (16-84%: 1520-1888) 

### uid1078155  [D2]  YOUNG
- position 329.63689 +80.33781; Gaia DR3 2285488987399269376; G 13.20, BP-RP 1.56, plx 2.85 mas; plot `plots/uid1078155.png`
- **young:** SIMBAD young-star types Y*? (UCAC4 852-015443) | Gaia DR3 variability class YSO(0.56)
- flags: centroid jump 0.065" (4.4 sigma, PA 130) not toward a Gaia neighbour | AllWISE ext_flg = 1 (extended or 2MASS XSC association) | 1.77 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | possible optical brightening at onset (-0.062 mag, one camera only)
- NEOWISE: score refetch 0.55 (stored 0.55, reproduced True); dW2 0.083, dW1 0.082, 11 visits, 115 points; baseline W1 9.11, W1-W2 0.334; onset between MJD 59453 and 59612
- detector 2: excess 0.390 mag, z 15.8, jitter ratio 14.1
- field control: target step +0.127 (W1 +0.121); neighbours N=43, median +0.003, robust sigma 0.010, max +0.038; z = 12.8
- centroid: jump at onset 0.065" +- 0.015 (4.4 sigma, PA 130); largest consecutive-visit jump 0.075"; rms 0.028"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.343, W2-W3 1.564 (W3 S/N 63.7), W3-W4 2.195 (W4 S/N 39.2), ext_flg 1, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.12, ipd_frac_multi_peak 0, NSS none, Teff 5023 K, logg 4.14, H-alpha pEW -0.835 nm, varclass YSO(0.56); M_G 5.48, -1.77 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): UCAC4 852-015443 [Y*?; *,MIR,NIR,Y*?] 0.15" refs=1
- ASAS-SN: 591 points, cameras bB(g,115); bb(V,142); br(g,251, d=-0.062); cB(g,83); change at onset (after-before, per-camera median) -0.062 mag; largest seasonal dimming 0.05 mag at MJD 60226
- dust: excess flux W1 6.72 mJy, W2 5.39 mJy, T = 1852 K (16-84%: 1554-2315) 

### uid1272657  [D2]  YOUNG
- position 79.85380 -7.34706; Gaia DR3 3207445881182172928; G 13.73, BP-RP 1.59, plx 2.73 mas; plot `plots/uid1272657.png`
- **young:** SIMBAD young-star types Y*O (UCAC4 414-008437) | Gaia DR3 variability class YSO(0.14)
- flags: 1.43 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.20 mag (MJD 59828)
- NEOWISE: score refetch 0.37 (stored 0.37, reproduced True); dW2 0.034, dW1 0.006, 10 visits, 129 points; baseline W1 9.62, W1-W2 0.409; onset between MJD 57642 and 58006
- detector 2: excess 0.463 mag, z 18.0, jitter ratio 7.9
- field control: target step +0.108 (W1 +0.044); neighbours N=39, median -0.007, robust sigma 0.009, max +0.019; z = 12.8
- centroid: jump at onset 0.014" +- 0.024 (0.6 sigma, PA 277); largest consecutive-visit jump 0.038"; rms 0.021"; toward neighbour: none; expected shift if a neighbour were the source: 9.8" G17.3: 0.92"
- AllWISE 2010: W1-W2 0.466, W2-W3 1.548 (W3 S/N 53.6), W3-W4 1.448 (W4 S/N 17.6), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.33, ipd_frac_multi_peak 0, NSS none, Teff 4818 K, logg 4.20, H-alpha pEW -0.671 nm, varclass YSO(0.14); M_G 5.91, -1.43 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 9.8" PA206 G17.35 dG+3.62
- SIMBAD (10"): UCAC4 414-008437 [Y*O; *,MIR,NIR,Y*O] 0.02" refs=3
- ASAS-SN: 1293 points, cameras bB(g,84); bF(g,207); bb(V,154, d=+0.165); bf(V,171, d=-0.149); bj(g,277); bn(g,237); br(g,163); change at onset (after-before, per-camera median) +0.008 mag; largest seasonal dimming 0.20 mag at MJD 59828
- dust: excess flux W1 2.11 mJy, W2 1.32 mJy, T = 4011 K (16-84%: 1588-8000) 

### uid1800505  [D2]  YOUNG
- position 86.10824 +9.11684; Gaia DR3 3336105028148587904; G 13.64, BP-RP 1.78, plx 2.47 mas; plot `plots/uid1800505.png`
- **young:** SIMBAD young-star types Or*,Y*?,Y*O ([DM99] 249)
- flags: 2.24 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 1.08 (stored 1.08, reproduced True); dW2 0.173, dW1 0.198, 20 visits, 214 points; baseline W1 9.26, W1-W2 0.535; onset between MJD 58902 and 59111
- detector 2: excess 0.568 mag, z 17.3, jitter ratio 12.1
- field control: target step +0.184 (W1 +0.263); neighbours N=127, median -0.006, robust sigma 0.015, max +0.582; z = 12.8
- centroid: jump at onset 0.007" +- 0.020 (0.3 sigma, PA 80); largest consecutive-visit jump 0.088"; rms 0.030"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.628, W2-W3 1.316 (W3 S/N 51.0), W3-W4 1.162 (W4 S/N 13.9), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.06, ipd_frac_multi_peak 0, NSS none, Teff 5443 K, logg 4.02, H-alpha pEW -0.463 nm, varclass none; M_G 5.61, -2.24 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): [DM99] 249 [Or*; *,MIR,NIR,Or*,X,Y*?,Y*O,ev] 0.06" refs=25
- ASAS-SN: 0 points, cameras n/a; change at onset (after-before, per-camera median) n/a mag; largest seasonal dimming n/a mag at MJD n/a
- dust: excess flux W1 18.90 mJy, W2 13.93 mJy, T = 2241 K (16-84%: 2042-2491) 
- checks missing: ASAS-SN (no source)

### uid1553860  [D2]  YOUNG
- position 88.38748 +2.28893; Gaia DR3 3316101819261702400; G 15.37, BP-RP 2.02, plx 2.58 mas; plot `plots/uid1553860.png`
- **young:** SIMBAD young-star types Or*,Y*O (Kiso A-0905   2)
- flags: 1.08 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.26 mag (MJD 58598)
- NEOWISE: score refetch 1.00 (stored 1.00, reproduced True); dW2 0.171, dW1 0.245, 20 visits, 193 points; baseline W1 10.91, W1-W2 0.655; onset between MJD 57451 and 57651
- detector 2: excess 0.646 mag, z 15.6, jitter ratio 14.6
- field control: target step +0.154 (W1 +0.183); neighbours N=101, median -0.005, robust sigma 0.013, max +0.036; z = 12.7
- centroid: jump at onset 0.041" +- 0.024 (1.7 sigma, PA 13); largest consecutive-visit jump 0.100"; rms 0.036"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.651, W2-W3 2.854 (W3 S/N 56.3), W3-W4 1.975 (W4 S/N 31.8), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.20, ipd_frac_multi_peak 0, NSS none, Teff 3518 K, logg 4.02, H-alpha pEW -7.205 nm, varclass none; M_G 7.43, -1.08 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): Kiso A-0905   2 [Or*; *,Em*,NIR,Or*,Y*O] 0.05" refs=7
- ASAS-SN: 1691 points, cameras bA(g,174); bB(g,89); bE(g,127); bF(g,120); ba(V,150, d=+0.025); bb(V,167, d=-0.019); bi(g,200); bj(g,152); bm(g,100); bn(g,86); bq(g,130); br(g,132); cB(g,64); change at onset (after-before, per-camera median) +0.003 mag; largest seasonal dimming 0.26 mag at MJD 58598
- dust: excess flux W1 2.95 mJy, W2 2.16 mJy, T = 2269 K (16-84%: 1970-2698) 

### uid1846306  [D2]  YOUNG
- position 82.71543 +12.14354; Gaia DR3 3340890480708559104; G 14.02, BP-RP 1.78, plx 2.45 mas; plot `plots/uid1846306.png`
- **young:** SIMBAD young-star types Or*,Y*O (V* V448 Ori)
- flags: 1.89 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 0.38 (stored 0.38, reproduced True); dW2 0.107, dW1 0.096, 18 visits, 156 points; baseline W1 9.94, W1-W2 0.618; onset between MJD 57282 and 57446
- detector 2: excess 0.650 mag, z 19.6, jitter ratio 26.4
- field control: target step +0.188 (W1 +0.165); neighbours N=113, median -0.005, robust sigma 0.016, max +0.121; z = 12.3
- centroid: jump at onset 0.031" +- 0.019 (1.6 sigma, PA 187); largest consecutive-visit jump 0.071"; rms 0.029"; toward neighbour: none; expected shift if a neighbour were the source: 7.4" G20.9: 1.18"
- AllWISE 2010: W1-W2 0.484, W2-W3 2.175 (W3 S/N 36.1), W3-W4 1.657 (W4 S/N 18.2), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.11, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW -1.368 nm, varclass none; M_G 5.97, -1.89 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 7.4" PA96 G20.89 dG+6.87
- SIMBAD (10"): V* V448 Ori [Or*; *,Em*,EmO,NIR,Or*,RS*,V*,Y*O,ev] 0.04" refs=33
- ASAS-SN: 1108 points, cameras bD(g,198); bE(g,120); bH(g,113); bd(V,170, d=+0.013); bl(g,185); bp(g,91); bq(g,124); bt(g,107); change at onset (after-before, per-camera median) +0.013 mag; largest seasonal dimming 0.08 mag at MJD 59489
- dust: excess flux W1 14.70 mJy, W2 13.79 mJy, T = 1423 K (16-84%: 1358-1493) 

### uid1550526  [D2]  YOUNG
- position 118.56172 -46.43338; Gaia DR3 5518967386922303616; G 12.84, BP-RP 1.38, plx 2.58 mas; plot `plots/uid1550526.png`
- **young:** SIMBAD young-star types Y*?,Y*O (Gaia DR3 5518967386922303616) | Gaia DR3 variability class YSO(0.78)
- flags: 1.89 mag above the main sequence at its colour | largest seasonal optical dimming 0.30 mag (MJD 57448)
- NEOWISE: score refetch 1.16 (stored 1.16, reproduced True); dW2 0.171, dW1 0.140, 21 visits, 316 points; baseline W1 8.40, W1-W2 0.474; onset between MJD 58436 and 58593
- detector 2: excess 0.537 mag, z 25.9, jitter ratio 14.0
- field control: target step +0.113 (W1 +0.053); neighbours N=147, median -0.003, robust sigma 0.010, max +0.044; z = 12.1
- centroid: jump at onset 0.011" +- 0.021 (0.5 sigma, PA 188); largest consecutive-visit jump 0.069"; rms 0.026"; toward neighbour: 9.3" PA195 G19.6 (angle 6 deg); expected shift if a neighbour were the source: 7.2" G17.9: 0.71"; 9.3" G19.6: 0.92"
- AllWISE 2010: W1-W2 0.469, W2-W3 0.936 (W3 S/N 67.8), W3-W4 2.121 (W4 S/N 40.4), ext_flg 0, ph_qual AAAA: weak W3 excess (0.5 < W2-W3 < 1.0)
- Gaia: RUWE 1.12, ipd_frac_multi_peak 1, NSS none, Teff 5485 K, logg 3.98, H-alpha pEW -0.706 nm, varclass YSO(0.78); M_G 4.90, -1.89 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 7.2" PA107 G17.90 dG+5.07; 9.3" PA195 G19.64 dG+6.80
- SIMBAD (10"): Gaia DR3 5518967386922303616 [Y*?; *,Y*?,Y*O] 0.16" refs=7
- ASAS-SN: 1376 points, cameras bE(g,423, d=-0.023); be(V,231); bi(g,510, d=-0.004); bm(g,212); change at onset (after-before, per-camera median) -0.014 mag; largest seasonal dimming 0.30 mag at MJD 57448
- dust: excess flux W1 7.31 mJy, W2 13.48 mJy, T = 753 K (16-84%: 654-868) 

### uid1837155  [D2]  YOUNG
- position 84.97774 -2.77615; Gaia DR3 3216421091519854464; G 13.52, BP-RP 1.76, plx 2.45 mas; plot `plots/uid1837155.png`
- **young:** SIMBAD young-star types Or*,TT*,Y*O (Haro 5-34) | Gaia DR3 variability class YSO(0.34)
- flags: 2.33 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 1.12 (stored 1.12, reproduced True); dW2 0.146, dW1 0.067, 21 visits, 223 points; baseline W1 9.43, W1-W2 0.486; onset between MJD 58536 and 58743
- detector 2: excess 0.521 mag, z 16.2, jitter ratio 6.5
- field control: target step +0.141 (W1 +0.141); neighbours N=81, median -0.002, robust sigma 0.012, max +0.119; z = 12.1
- centroid: jump at onset 0.017" +- 0.019 (0.9 sigma, PA 103); largest consecutive-visit jump 0.051"; rms 0.034"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.470, W2-W3 2.375 (W3 S/N 71.9), W3-W4 1.530 (W4 S/N 35.8), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.01, ipd_frac_multi_peak 0, NSS none, Teff 5690 K, logg 4.11, H-alpha pEW -0.884 nm, varclass YSO(0.34); M_G 5.47, -2.33 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): Haro 5-34 [TT*; *,Em*,NIR,Or*,TT*,V*,Y*O] 0.04" refs=40; HGBS J053954.9-024634 [cor; IR,cor] 3.95" refs=1
- ASAS-SN: 0 points, cameras n/a; change at onset (after-before, per-camera median) n/a mag; largest seasonal dimming n/a mag at MJD n/a
- dust: excess flux W1 3.86 mJy, W2 5.70 mJy, T = 885 K (16-84%: 814-962) 
- checks missing: ASAS-SN (no source)

### uid1717828  [D2]  YOUNG
- position 83.84831 -4.28730; Gaia DR3 3215658511486884864; G 14.98, BP-RP 1.96, plx 2.51 mas; plot `plots/uid1717828.png`
- **young:** SIMBAD young-star types Or*,Y*O (V* V561 Ori)
- flags: centroid jump 0.123" (4.2 sigma, PA 92) not toward a Gaia neighbour | in the Gaia DR3 QSO candidate table (low purity) | AllWISE ext_flg = 1 (extended or 2MASS XSC association) | 1.35 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.21 mag (MJD 58180)
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 20 visits, 194 points; baseline W1 9.63, W1-W2 0.593; onset between MJD 58742 and 58899
- detector 2: excess 0.596 mag, z 14.6, jitter ratio 12.4
- field control: target step +0.133 (W1 +0.100); neighbours N=114, median -0.004, robust sigma 0.011, max +0.075; z = 11.9
- centroid: jump at onset 0.123" +- 0.029 (4.2 sigma, PA 92); largest consecutive-visit jump 0.165"; rms 0.049"; toward neighbour: none; expected shift if a neighbour were the source: 8.5" G14.6: 0.98"
- AllWISE 2010: W1-W2 0.604, W2-W3 2.404 (W3 S/N 56.8), W3-W4 2.014 (W4 S/N 33.3), ext_flg 1, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.14, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW -1.943 nm, varclass none; M_G 6.97, -1.35 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 8.5" PA250 G14.58 dG-0.39
- SIMBAD (10"): V* V561 Ori [Or*; *,Em*,MIR,NIR,Or*,V*,Y*O] 0.02" refs=23; V* V2404 Ori [Or*; *,BY*,Er*,NIR,Or*,V*,Y*O] 8.51" refs=27
- ASAS-SN: 1035 points, cameras bA(g,144, d=-0.001); bE(g,118, d=-0.092); ba(V,136); be(V,194); bi(g,210, d=-0.098); bm(g,136, d=+0.181); bq(g,97, d=-0.020); change at onset (after-before, per-camera median) -0.020 mag; largest seasonal dimming 0.21 mag at MJD 58180
- dust: excess flux W1 1.47 mJy, W2 -0.35 mJy, T = n/a K (16-84%: n/a-n/a) no W2 excess flux after onset

### uid1479092  [D2]  YOUNG
- position 85.40209 -6.34590; Gaia DR3 3016249811363341568; G 13.78, BP-RP 1.72, plx 2.62 mas; plot `plots/uid1479092.png`
- **young:** SIMBAD young-star types Y*?,Y*O (Haro 4-487)
- flags: 1.82 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 0.61 (stored 0.61, reproduced True); dW2 0.060, dW1 0.073, 21 visits, 268 points; baseline W1 10.22, W1-W2 0.544; onset between MJD 57648 and 57813
- detector 2: excess 0.585 mag, z 19.0, jitter ratio 9.7
- field control: target step +0.143 (W1 +0.037); neighbours N=61, median -0.004, robust sigma 0.013, max +0.024; z = 11.7
- centroid: jump at onset 0.015" +- 0.014 (1.1 sigma, PA 245); largest consecutive-visit jump 0.057"; rms 0.031"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.510, W2-W3 2.483 (W3 S/N 61.0), W3-W4 1.911 (W4 S/N 31.7), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.04, ipd_frac_multi_peak 0, NSS none, Teff 5555 K, logg 4.20, H-alpha pEW -2.167 nm, varclass RS(0.30); M_G 5.87, -1.82 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): Haro 4-487 [Y*O; *,Em*,MIR,NIR,PM*,Y*?,Y*O] 0.05" refs=9
- ASAS-SN: 0 points, cameras n/a; change at onset (after-before, per-camera median) n/a mag; largest seasonal dimming n/a mag at MJD n/a
- dust: excess flux W1 1.52 mJy, W2 2.44 mJy, T = 827 K (16-84%: 750-914) 
- checks missing: ASAS-SN (no source)

### uid1685096  [D2]  YOUNG
- position 83.10696 -3.72047; Gaia DR3 3209935003708198016; G 14.18, BP-RP 1.61, plx 2.52 mas; plot `plots/uid1685096.png`
- **young:** SIMBAD young-star types Or*,TT*,Y*?,Y*O (V* V1165 Ori)
- flags: 1.19 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | not plain dust: optical brightening -0.201 mag (per-camera -0.183,-0.229,-0.205,-0.197) together with the infrared rise | largest seasonal optical dimming 0.22 mag (MJD 59187)
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 21 visits, 217 points; baseline W1 10.42, W1-W2 0.334; onset between MJD 59994 and 60204
- detector 2: excess 0.386 mag, z 14.8, jitter ratio 10.5
- field control: target step +0.179 (W1 +0.135); neighbours N=71, median -0.002, robust sigma 0.016, max +0.062; z = 11.6
- centroid: jump at onset 0.014" +- 0.021 (0.7 sigma, PA 117); largest consecutive-visit jump 0.056"; rms 0.028"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.352, W2-W3 2.218 (W3 S/N 49.2), W3-W4 1.984 (W4 S/N 23.4), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.07, ipd_frac_multi_peak 0, NSS none, Teff 5849 K, logg 4.33, H-alpha pEW -3.116 nm, varclass none; M_G 6.19, -1.19 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): V* V1165 Ori [TT*; *,Em*,Er*,MIR,NIR,Opt,Or*,TT*,V*,Y*?,Y*O] 0.02" refs=19
- ASAS-SN: 1331 points, cameras bC(g,156, d=-0.183); bG(g,222, d=-0.229); ba(V,50); bc(V,151); be(V,38); bg(V,153); bk(g,264, d=-0.205); bo(g,161); bs(g,136, d=-0.197); change at onset (after-before, per-camera median) -0.201 mag; largest seasonal dimming 0.22 mag at MJD 59187
- dust: excess flux W1 -0.42 mJy, W2 -0.01 mJy, T = n/a K (16-84%: n/a-n/a) no W2 excess flux after onset

### uid1117149  [D2]  YOUNG
- position 80.48922 +0.19505; Gaia DR3 3221444107311671936; G 14.96, BP-RP 1.71, plx 2.82 mas; plot `plots/uid1117149.png`
- **young:** SIMBAD young-star types TT*,Y*O (Kiso A-0903  80) | Gaia DR3 variability class YSO(0.55)
- flags: AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | possible optical brightening at onset (-0.201 mag, one camera only) | largest seasonal optical dimming 0.24 mag (MJD 59262)
- NEOWISE: score refetch 1.20 (stored 1.20, reproduced True); dW2 0.155, dW1 0.130, 20 visits, 174 points; baseline W1 10.13, W1-W2 0.407; onset between MJD 57085 and 57279
- detector 2: excess 0.448 mag, z 14.7, jitter ratio 12.5
- field control: target step +0.161 (W1 +0.146); neighbours N=58, median -0.007, robust sigma 0.014, max +0.109; z = 11.6
- centroid: jump at onset 0.029" +- 0.017 (1.7 sigma, PA 41); largest consecutive-visit jump 0.033"; rms 0.029"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.440, W2-W3 1.446 (W3 S/N 48.3), W3-W4 1.942 (W4 S/N 17.3), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.19, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW -2.158 nm, varclass YSO(0.55); M_G 7.22, -0.45 mag vs sequence (on the sequence); neighbours within 10": none
- SIMBAD (10"): Kiso A-0903  80 [TT*; *,Em*,NIR,TT*,Y*O] 0.03" refs=17
- ASAS-SN: 1112 points, cameras bB(g,84); bF(g,152); bb(V,297, d=-0.201); bf(V,55); bj(g,198); bn(g,204); br(g,122); change at onset (after-before, per-camera median) -0.201 mag; largest seasonal dimming 0.24 mag at MJD 59262
- dust: excess flux W1 3.87 mJy, W2 3.49 mJy, T = 1507 K (16-84%: 1352-1706) 

### uid909402  [D2]  YOUNG
- position 83.83334 -0.28097; Gaia DR3 3220792887190091136; G 15.81, BP-RP 2.01, plx 2.96 mas; plot `plots/uid909402.png`
- **young:** SIMBAD young-star types TT*,Y*O (2MASS J05352000-0016514)
- flags: in the Gaia DR3 QSO candidate table (low purity) | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.33 mag (MJD 58084)
- NEOWISE: score refetch 0.45 (stored 0.45, reproduced True); dW2 0.048, dW1 0.032, 20 visits, 215 points; baseline W1 11.25, W1-W2 0.605; onset between MJD 57282 and 57447
- detector 2: excess 0.598 mag, z 14.4, jitter ratio 8.0
- field control: target step +0.128 (W1 +0.121); neighbours N=87, median -0.007, robust sigma 0.012, max +0.113; z = 11.4
- centroid: jump at onset 0.028" +- 0.016 (1.8 sigma, PA 344); largest consecutive-visit jump 0.072"; rms 0.036"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.580, W2-W3 2.260 (W3 S/N 43.4), W3-W4 2.141 (W4 S/N 18.8), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.16, ipd_frac_multi_peak 0, NSS none, Teff 3440 K, logg 4.09, H-alpha pEW -6.515 nm, varclass none; M_G 8.17, -0.32 mag vs sequence (on the sequence); neighbours within 10": none
- SIMBAD (10"): 2MASS J05352000-0016514 [TT*; *,Em*,NIR,TT*,Y*O] 0.03" refs=7
- ASAS-SN: 457 points, cameras ba(V,36); bc(V,92, d=-0.138); be(V,24); bg(V,90, d=+0.147); bk(g,89); bo(g,70); bs(g,56); change at onset (after-before, per-camera median) +0.004 mag; largest seasonal dimming 0.33 mag at MJD 58084
- dust: excess flux W1 0.77 mJy, W2 0.84 mJy, T = 1183 K (16-84%: 1018-1405) 

### uid844587  [D2]  YOUNG
- position 83.70380 -0.62131; Gaia DR3 3217774723475861376; G 13.11, BP-RP 1.59, plx 3.01 mas; plot `plots/uid844587.png`
- **young:** SIMBAD young-star types Or*,Y*O (Haro 5-71)
- flags: 1.82 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.14 mag (MJD 58194)
- NEOWISE: score refetch 1.37 (stored 1.37, reproduced True); dW2 0.083, dW1 0.062, 21 visits, 214 points; baseline W1 8.91, W1-W2 0.364; onset between MJD 57088 and 57282
- detector 2: excess 0.418 mag, z 16.4, jitter ratio 5.8
- field control: target step +0.122 (W1 +0.083); neighbours N=94, median -0.003, robust sigma 0.011, max +0.093; z = 11.3
- centroid: jump at onset 0.024" +- 0.013 (1.9 sigma, PA 61); largest consecutive-visit jump 0.029"; rms 0.028"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.341, W2-W3 2.086 (W3 S/N 57.3), W3-W4 2.253 (W4 S/N 36.5), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.33, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW -0.720 nm, varclass none; M_G 5.51, -1.82 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): Haro 5-71 [Or*; *,Em*,Er*,NIR,Opt,Or*,V*,Y*O] 0.03" refs=19
- ASAS-SN: 1441 points, cameras bC(g,157); bG(g,222); ba(V,50); bc(V,151, d=+0.154); be(V,38, d=-0.206); bg(V,153); bk(g,298); bo(g,212); bs(g,160); change at onset (after-before, per-camera median) -0.026 mag; largest seasonal dimming 0.14 mag at MJD 58194
- dust: excess flux W1 7.29 mJy, W2 6.51 mJy, T = 1531 K (16-84%: 1303-1873) 

### uid1717992  [D2]  YOUNG
- position 84.61357 -2.75270; Gaia DR3 3216107490187638784; G 14.52, BP-RP 1.87, plx 2.51 mas; plot `plots/uid1717992.png`
- **young:** SIMBAD young-star types Or*,TT*,Y*O (V* V505 Ori)
- flags: 1.59 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | not plain dust: optical brightening -0.210 mag (per-camera -0.132,-0.289) together with the infrared rise | largest seasonal optical dimming 0.28 mag (MJD 60520)
- NEOWISE: score refetch 0.44 (stored 0.43, reproduced True); dW2 0.058, dW1 0.037, 21 visits, 230 points; baseline W1 8.82, W1-W2 0.627; onset between MJD 57448 and 57647
- detector 2: excess 0.646 mag, z 16.8, jitter ratio 13.0
- field control: target step +0.159 (W1 +0.161); neighbours N=113, median -0.003, robust sigma 0.015, max +0.686; z = 10.9
- centroid: jump at onset 0.004" +- 0.017 (0.3 sigma, PA 337); largest consecutive-visit jump 0.054"; rms 0.025"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.559, W2-W3 1.817 (W3 S/N 63.2), W3-W4 2.025 (W4 S/N 36.8), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.20, ipd_frac_multi_peak 1, NSS none, Teff nan K, logg nan, H-alpha pEW -1.879 nm, varclass none; M_G 6.51, -1.59 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): V* V505 Ori [TT*; *,Em*,NIR,Or*,TT*,V*,Y*O] 0.02" refs=65; WBIS J053826.8-024514.0 [LM*; LM*,NIR] 7.70" refs=1
- ASAS-SN: 1449 points, cameras bC(g,151); bG(g,218); ba(V,50); bc(V,150, d=-0.132); be(V,38); bg(V,150, d=-0.289); bk(g,311); bo(g,223); bs(g,158); change at onset (after-before, per-camera median) -0.210 mag; largest seasonal dimming 0.28 mag at MJD 60520
- dust: excess flux W1 15.30 mJy, W2 12.98 mJy, T = 1667 K (16-84%: 1394-2078) 

### uid1616401  [D2]  YOUNG
- position 83.25932 -5.44034; Gaia DR3 3209420947662499712; G 11.93, BP-RP 1.21, plx 2.55 mas; plot `plots/uid1616401.png`
- **young:** SIMBAD young-star types Or*,Y*O (V* V466 Ori) | Gaia DR3 variability class YSO(0.68)
- flags: Gaia ipd_frac_multi_peak 12% (resolved double?) | 2.29 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 2.57 (stored 2.57, reproduced True); dW2 0.324, dW1 0.292, 20 visits, 184 points; baseline W1 8.46, W1-W2 0.441; onset between MJD 57446 and 57646
- detector 2: excess 0.502 mag, z 26.8, jitter ratio 11.4
- field control: target step +0.280 (W1 +0.259); neighbours N=101, median -0.001, robust sigma 0.027, max +0.151; z = 10.5
- centroid: jump at onset 0.032" +- 0.017 (1.9 sigma, PA 312); largest consecutive-visit jump 0.085"; rms 0.032"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.422, W2-W3 2.428 (W3 S/N 73.7), W3-W4 2.009 (W4 S/N 35.8), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.09, ipd_frac_multi_peak 12, NSS none, Teff nan K, logg nan, H-alpha pEW -1.070 nm, varclass YSO(0.68); M_G 3.96, -2.29 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): V* V466 Ori [Or*; *,Em*,IR,MIR,NIR,Opt,Or*,V*,Y*O] 0.02" refs=44
- ASAS-SN: 1517 points, cameras bA(g,156); bE(g,220); ba(V,177, d=+0.033); be(V,195, d=+0.045); bi(g,345); bm(g,251); bq(g,173); change at onset (after-before, per-camera median) +0.039 mag; largest seasonal dimming 0.05 mag at MJD 60234
- dust: excess flux W1 38.51 mJy, W2 39.02 mJy, T = 1284 K (16-84%: 1232-1341) 

### uid1574722  [D2]  YOUNG
- position 84.03369 -4.68908; Gaia DR3 3209581682520242560; G 14.54, BP-RP 1.87, plx 2.57 mas; plot `plots/uid1574722.png`
- **young:** SIMBAD young-star types Or*,TT*,Y*O (V* CH Ori)
- flags: 1.52 mag above the main sequence at its colour | not plain dust: optical brightening -0.087 mag (per-camera -0.094,-0.081) together with the infrared rise | largest seasonal optical dimming 0.21 mag (MJD 56892)
- NEOWISE: score refetch 1.48 (stored 1.48, reproduced True); dW2 0.232, dW1 0.169, 20 visits, 187 points; baseline W1 9.77, W1-W2 0.538; onset between MJD 57282 and 57447
- detector 2: excess 0.556 mag, z 14.5, jitter ratio 12.6
- field control: target step +0.217 (W1 +0.216); neighbours N=124, median -0.007, robust sigma 0.021, max +0.574; z = 10.4
- centroid: jump at onset 0.027" +- 0.023 (1.2 sigma, PA 291); largest consecutive-visit jump 0.095"; rms 0.039"; toward neighbour: none; expected shift if a neighbour were the source: 8.5" G16.9: 1.54"
- AllWISE 2010: W1-W2 0.505, W2-W3 1.729 (W3 S/N 2.0), W3-W4 2.159 (W4 S/N 2.6), ext_flg 0, ph_qual AAUC: W3 S/N < 5: no W2-W3 class; W1-W2 > 0.25
- Gaia: RUWE 1.09, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW -0.568 nm, varclass none; M_G 6.59, -1.52 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 8.5" PA100 G16.90 dG+2.37
- SIMBAD (10"): V* CH Ori [TT*; *,Em*,Er*,MIR,NIR,Or*,TT*,V*,V*?,Y*O] 0.02" refs=51
- ASAS-SN: 1209 points, cameras bA(g,122); bE(g,205); ba(V,160, d=-0.094); be(V,195, d=-0.081); bi(g,221); bm(g,168); bq(g,138); change at onset (after-before, per-camera median) -0.087 mag; largest seasonal dimming 0.21 mag at MJD 56892
- dust: excess flux W1 4.08 mJy, W2 5.67 mJy, T = 929 K (16-84%: 847-1019) 

### uid1508447  [D2]  YOUNG
- position 83.99022 -5.95512; Gaia DR3 3017186251673566208; G 14.57, BP-RP 1.78, plx 2.60 mas; plot `plots/uid1508447.png`
- **young:** SIMBAD young-star types Or*,TT*,Y*?,Y*O (V* AU Ori)
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | 1.20 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.35 mag (MJD 60565)
- NEOWISE: score refetch 0.52 (stored 0.52, reproduced True); dW2 0.047, dW1 0.067, 18 visits, 183 points; baseline W1 10.21, W1-W2 0.470; onset between MJD 59473 and 59631
- detector 2: excess 0.503 mag, z 15.3, jitter ratio 6.8
- field control: target step +0.221 (W1 +0.198); neighbours N=140, median +0.002, robust sigma 0.021, max +0.396; z = 10.2
- centroid: jump at onset 0.032" +- 0.022 (1.4 sigma, PA 309); largest consecutive-visit jump 0.080"; rms 0.034"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.498, W2-W3 2.466 (W3 S/N 56.6), W3-W4 2.412 (W4 S/N 38.7), ext_flg 1, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.10, ipd_frac_multi_peak 0, NSS none, Teff 6048 K, logg 4.38, H-alpha pEW -4.057 nm, varclass none; M_G 6.65, -1.20 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): V* AU Ori [TT*; *,Em*,MIR,NIR,Or*,TT*,V*,V*?,Y*?,Y*O] 0.02" refs=55
- ASAS-SN: 1261 points, cameras bA(g,153, d=-0.040); bE(g,217, d=+0.020); ba(V,164); be(V,194); bi(g,204); bm(g,187, d=-0.222); bq(g,142, d=-0.237); change at onset (after-before, per-camera median) -0.131 mag; largest seasonal dimming 0.35 mag at MJD 60565
- dust: excess flux W1 4.54 mJy, W2 4.41 mJy, T = 1357 K (16-84%: 1212-1539) 

### uid1192683  [D2]  YOUNG
- position 94.43232 -1.85737; Gaia DR3 3118092797442942976; G 15.50, BP-RP 1.98, plx 2.78 mas; plot `plots/uid1192683.png`
- **young:** SIMBAD young-star types Y*? (2MASS J06174375-0151264)
- flags: AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.76 mag (MJD 60288)
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 20 visits, 189 points; baseline W1 10.79, W1-W2 0.580; onset between MJD 56931 and 57098
- detector 2: excess 0.580 mag, z 14.0, jitter ratio 11.0
- field control: target step +0.116 (W1 +0.094); neighbours N=143, median -0.003, robust sigma 0.012, max +0.036; z = 10.0
- centroid: jump at onset 0.019" +- 0.027 (0.7 sigma, PA 200); largest consecutive-visit jump 0.054"; rms 0.034"; toward neighbour: none; expected shift if a neighbour were the source: 7.2" G19.1: 0.73"; 7.5" G18.5: 0.76"
- AllWISE 2010: W1-W2 0.577, W2-W3 1.969 (W3 S/N 49.1), W3-W4 2.231 (W4 S/N 21.8), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.25, ipd_frac_multi_peak 0, NSS none, Teff 3518 K, logg 4.08, H-alpha pEW -5.812 nm, varclass none; M_G 7.72, -0.67 mag vs sequence (on the sequence); neighbours within 10": 7.2" PA123 G19.11 dG+3.60; 7.5" PA259 G18.54 dG+3.04
- SIMBAD (10"): 2MASS J06174375-0151264 [Y*?; *,NIR,Y*?] 0.08" refs=1
- ASAS-SN: 1567 points, cameras bC(g,111); bD(g,102); bG(g,120); bH(g,98); bc(V,120); bd(V,121); bg(V,122); bh(V,136); bk(g,165); bl(g,128); bo(g,77); bp(g,67); bs(g,100); bt(g,100); change at onset (after-before, per-camera median) n/a mag; largest seasonal dimming 0.76 mag at MJD 60288
- dust: excess flux W1 0.38 mJy, W2 0.51 mJy, T = 966 K (16-84%: 751-1334) 
- checks missing: ASAS-SN change at onset (no camera spans the onset)

### uid1511208  [D2]  YOUNG
- position 84.44069 -4.72421; Gaia DR3 3215570722355435904; G 14.30, BP-RP 1.69, plx 2.60 mas; plot `plots/uid1511208.png`
- **young:** SIMBAD young-star types Y*?,Y*O (UCAC4 427-010287)
- flags: 1.24 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 2.68 (stored 2.68, reproduced True); dW2 0.257, dW1 0.313, 20 visits, 215 points; baseline W1 10.78, W1-W2 0.505; onset between MJD 57448 and 57647
- detector 2: excess 0.549 mag, z 18.7, jitter ratio 9.2
- field control: target step +0.138 (W1 +0.236); neighbours N=58, median -0.003, robust sigma 0.014, max +0.574; z = 10.0
- centroid: jump at onset 0.019" +- 0.018 (1.1 sigma, PA 334); largest consecutive-visit jump 0.058"; rms 0.028"; toward neighbour: none; expected shift if a neighbour were the source: 9.6" G17.6: 1.15"
- AllWISE 2010: W1-W2 0.550, W2-W3 2.508 (W3 S/N 51.1), W3-W4 1.739 (W4 S/N 13.6), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 0.98, ipd_frac_multi_peak 0, NSS none, Teff 4153 K, logg 4.16, H-alpha pEW -0.240 nm, varclass RS(0.72); M_G 6.38, -1.24 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 9.6" PA50 G17.57 dG+3.26
- SIMBAD (10"): UCAC4 427-010287 [Y*O; *,MIR,NIR,Y*?,Y*O] 0.02" refs=10
- ASAS-SN: 0 points, cameras n/a; change at onset (after-before, per-camera median) n/a mag; largest seasonal dimming n/a mag at MJD n/a
- dust: excess flux W1 3.68 mJy, W2 2.59 mJy, T = 2557 K (16-84%: 2236-2997) 
- checks missing: ASAS-SN (no source)

### uid1806802  [D2]  YOUNG
- position 82.81728 +11.42533; Gaia DR3 3340627869228903424; G 14.50, BP-RP 1.84, plx 2.47 mas; plot `plots/uid1806802.png`
- **young:** SIMBAD young-star types Or*,TT*,Y*O (V* V449 Ori)
- flags: 1.56 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.17 mag (MJD 59324)
- NEOWISE: score refetch 0.34 (stored 0.34, reproduced True); dW2 0.055, dW1 0.048, 19 visits, 183 points; baseline W1 9.32, W1-W2 0.702; onset between MJD 57646 and 57811
- detector 2: excess 0.726 mag, z 19.9, jitter ratio 14.8
- field control: target step +0.106 (W1 +0.036); neighbours N=88, median -0.003, robust sigma 0.011, max +0.058; z = 9.8
- centroid: jump at onset 0.014" +- 0.025 (0.5 sigma, PA 161); largest consecutive-visit jump 0.071"; rms 0.039"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.675, W2-W3 2.214 (W3 S/N 63.1), W3-W4 1.894 (W4 S/N 37.4), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.20, ipd_frac_multi_peak 0, NSS none, Teff 5833 K, logg 4.33, H-alpha pEW -0.957 nm, varclass none; M_G 6.46, -1.56 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): V* V449 Ori [Or*; *,Em*,NIR,Or*,TT*,V*,Y*O] 0.03" refs=32
- ASAS-SN: 912 points, cameras bA(g,182); bE(g,120); ba(V,156, d=+0.018); bi(g,221); bm(g,116); bq(g,117); change at onset (after-before, per-camera median) +0.018 mag; largest seasonal dimming 0.17 mag at MJD 59324
- dust: excess flux W1 1.52 mJy, W2 4.10 mJy, T = 602 K (16-84%: 520-695) 

### uid1594699  [D2]  YOUNG
- position 84.15389 -6.55668; Gaia DR3 3016933432717079296; G 15.52, BP-RP 2.10, plx 2.56 mas; plot `plots/uid1594699.png`
- **young:** SIMBAD young-star types Or*,Y*O (V* V585 Ori)
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | 1.19 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.26 mag (MJD 56983)
- NEOWISE: score refetch 0.54 (stored 0.54, reproduced True); dW2 0.110, dW1 0.033, 21 visits, 196 points; baseline W1 8.70, W1-W2 0.830; onset between MJD 57088 and 57282
- detector 2: excess 0.809 mag, z 18.8, jitter ratio 8.2
- field control: target step +0.213 (W1 +0.233); neighbours N=91, median -0.002, robust sigma 0.022, max +0.329; z = 9.7
- centroid: jump at onset 0.031" +- 0.023 (1.4 sigma, PA 4); largest consecutive-visit jump 0.134"; rms 0.041"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.822, W2-W3 1.689 (W3 S/N 62.3), W3-W4 1.583 (W4 S/N 32.5), ext_flg 1, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.14, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW -5.078 nm, varclass none; M_G 7.57, -1.19 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): V* V585 Ori [Or*; *,Em*,LP?,MIR,NIR,Opt,Or*,V*,X,Y*O] 0.00" refs=41
- ASAS-SN: 1188 points, cameras bA(g,126); bE(g,164); ba(V,165, d=+0.015); be(V,159, d=-0.216); bi(g,280); bm(g,156); bq(g,138); change at onset (after-before, per-camera median) -0.101 mag; largest seasonal dimming 0.26 mag at MJD 56983
- dust: excess flux W1 19.94 mJy, W2 23.60 mJy, T = 1079 K (16-84%: 978-1197) 

### uid1789599  [D2]  YOUNG
- position 83.90149 -5.52719; Gaia DR3 3017347089620157440; G 15.59, BP-RP 2.11, plx 2.48 mas; plot `plots/uid1789599.png`
- **young:** SIMBAD young-star types Or*,TT*,TT?,Y*O (V* V2551 Ori)
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | 1.26 mag above the main sequence at its colour
- NEOWISE: score refetch 1.81 (stored 1.81, reproduced True); dW2 0.333, dW1 0.359, 17 visits, 160 points; baseline W1 10.43, W1-W2 0.693; onset between MJD 57447 and 57646
- detector 2: excess 0.670 mag, z 15.6, jitter ratio 13.3
- field control: target step +0.370 (W1 +0.364); neighbours N=90, median -0.012, robust sigma 0.040, max +0.392; z = 9.6
- centroid: jump at onset 0.017" +- 0.024 (0.7 sigma, PA 229); largest consecutive-visit jump 0.089"; rms 0.037"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.639, W2-W3 0.192 (W3 S/N -0.9), W3-W4 2.446 (W4 S/N -41.2), ext_flg 1, ph_qual AAUU: W3 S/N < 5: no W2-W3 class; W1-W2 > 0.25
- Gaia: RUWE 1.03, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW -5.914 nm, varclass none; M_G 7.56, -1.26 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): V* V2551 Ori [TT*; *,Em*,Ir*,MIR,NIR,Or*,TT*,TT?,V*,X,Y*O] 0.03" refs=48; [H97b] 20719 [*; *] 6.93" refs=1; [RRS2008] 359-3141 [*; *,Y*O] 7.02" refs=1
- ASAS-SN: 232 points, cameras bA(g,68); bi(g,20); bm(g,144); change at onset (after-before, per-camera median) n/a mag; largest seasonal dimming 0.08 mag at MJD 58723
- dust: excess flux W1 8.45 mJy, W2 8.24 mJy, T = 1350 K (16-84%: 1288-1416) 
- checks missing: ASAS-SN change at onset (no camera spans the onset)

### uid1806829  [D2]  YOUNG
- position 83.46034 +10.91364; Gaia DR3 3339787979784483968; G 13.89, BP-RP 1.61, plx 2.47 mas; plot `plots/uid1806829.png`
- **young:** SIMBAD young-star types Y*?,Y*O (2MASS J05335048+1054491) | Gaia DR3 variability class YSO(0.23)
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | 1.54 mag above the main sequence at its colour
- NEOWISE: score refetch 0.39 (stored 0.39, reproduced True); dW2 0.053, dW1 0.044, 20 visits, 223 points; baseline W1 10.66, W1-W2 0.313; onset between MJD 57646 and 57811
- detector 2: excess 0.365 mag, z 13.9, jitter ratio 12.0
- field control: target step +0.111 (W1 +0.126); neighbours N=95, median -0.007, robust sigma 0.013, max +0.034; z = 9.4
- centroid: jump at onset 0.159" +- 0.064 (2.5 sigma, PA 23); largest consecutive-visit jump 0.349"; rms 0.116"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.320, W2-W3 0.810 (W3 S/N 22.7), W3-W4 1.734 (W4 S/N 5.7), ext_flg 1, ph_qual AAAB: weak W3 excess (0.5 < W2-W3 < 1.0)
- Gaia: RUWE 1.02, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW -0.080 nm, varclass YSO(0.23); M_G 5.85, -1.54 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): 2MASS J05335048+1054491 [Y*O; *,NIR,Y*?,Y*O] 0.03" refs=24
- ASAS-SN: 935 points, cameras bA(g,183); bE(g,120); ba(V,156, d=-0.008); bi(g,237); bm(g,122); bq(g,117); change at onset (after-before, per-camera median) -0.008 mag; largest seasonal dimming 0.08 mag at MJD 60567
- dust: excess flux W1 1.03 mJy, W2 0.91 mJy, T = 1548 K (16-84%: 1266-2011) 

### uid1454537  [D2]  YOUNG
- position 83.37789 -5.03743; Gaia DR3 3209542409339494656; G 14.99, BP-RP 2.20, plx 2.63 mas; plot `plots/uid1454537.png`
- **young:** SIMBAD young-star types Or*,Y*O (V* V721 Ori)
- flags: 1.97 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.60 mag (MJD 59961)
- NEOWISE: score refetch 1.10 (stored 1.10, reproduced True); dW2 0.113, dW1 0.136, 20 visits, 182 points; baseline W1 10.96, W1-W2 0.641; onset between MJD 57811 and 58013
- detector 2: excess 0.610 mag, z 14.2, jitter ratio 7.6
- field control: target step +0.128 (W1 +0.181); neighbours N=105, median -0.009, robust sigma 0.015, max +0.264; z = 9.2
- centroid: jump at onset 0.027" +- 0.018 (1.6 sigma, PA 122); largest consecutive-visit jump 0.056"; rms 0.034"; toward neighbour: 10.0" PA114 G20.9 (angle 8 deg); expected shift if a neighbour were the source: 10.0" G20.9: 1.11"
- AllWISE 2010: W1-W2 0.701, W2-W3 3.065 (W3 S/N 48.0), W3-W4 2.205 (W4 S/N 24.2), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.06, ipd_frac_multi_peak 0, NSS none, Teff 6011 K, logg 4.34, H-alpha pEW -0.576 nm, varclass none; M_G 7.09, -1.97 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 10.0" PA114 G20.88 dG+5.89
- SIMBAD (10"): V* V721 Ori [Or*; *,Er*,MIR,NIR,Or*,V*,Y*O] 0.02" refs=26
- ASAS-SN: 1073 points, cameras bA(g,88); bE(g,129); ba(V,175, d=+0.000); be(V,193, d=-0.029); bi(g,243); bm(g,125); bq(g,120); change at onset (after-before, per-camera median) -0.015 mag; largest seasonal dimming 0.60 mag at MJD 59961
- dust: excess flux W1 2.31 mJy, W2 1.66 mJy, T = 2415 K (16-84%: 1939-3341) 

### uid961709  [D2]  YOUNG
- position 82.54790 -6.56916; Gaia DR3 3016799154860928128; G 11.64, BP-RP 1.58, plx 2.93 mas; plot `plots/uid961709.png`
- **young:** SIMBAD young-star types Or*,Y*O (V* HH Ori)
- flags: 3.33 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | optical dimming +0.151 mag after the infrared onset (debris transit signature) | largest seasonal optical dimming 1.04 mag (MJD 57804)
- NEOWISE: score refetch 1.22 (stored 1.22, reproduced True); dW2 0.170, dW1 0.185, 18 visits, 187 points; baseline W1 8.49, W1-W2 0.763; onset between MJD 57280 and 57445
- detector 2: excess 0.818 mag, z 32.3, jitter ratio 5.8
- field control: target step +0.122 (W1 +0.154); neighbours N=72, median -0.004, robust sigma 0.014, max +0.067; z = 9.2
- centroid: jump at onset 0.027" +- 0.019 (1.4 sigma, PA 232); largest consecutive-visit jump 0.053"; rms 0.034"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.789, W2-W3 2.984 (W3 S/N 74.3), W3-W4 1.623 (W4 S/N 59.6), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.34, ipd_frac_multi_peak 1, NSS none, Teff 4792 K, logg 3.64, H-alpha pEW 0.220 nm, varclass none; M_G 3.97, -3.33 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): V* HH Ori [Or*; *,IR,NIR,Or*,V*,Y*O] 0.01" refs=13
- ASAS-SN: 1521 points, cameras bA(g,159); bE(g,220); ba(V,180, d=+0.233); be(V,195, d=+0.068); bi(g,343); bm(g,251); bq(g,173); change at onset (after-before, per-camera median) +0.151 mag; largest seasonal dimming 1.04 mag at MJD 57804
- dust: excess flux W1 15.24 mJy, W2 13.60 mJy, T = 1534 K (16-84%: 1342-1809) 

### uid1572724  [D2]  YOUNG
- position 84.08235 -4.74869; Gaia DR3 3209568797618582144; G 13.68, BP-RP 1.61, plx 2.57 mas; plot `plots/uid1572724.png`
- **young:** SIMBAD young-star types Or*,TT*,Y*O (V* V2664 Ori) | Gaia DR3 variability class YSO(0.53)
- flags: centroid jump 0.052" (4.5 sigma, PA 19) not toward a Gaia neighbour | Gaia ipd_frac_multi_peak 52% (resolved double?) | 1.67 mag above the main sequence at its colour
- NEOWISE: score refetch 2.94 (stored 2.94, reproduced True); dW2 0.119, dW1 0.133, 19 visits, 187 points; baseline W1 10.08, W1-W2 0.364; onset between MJD 57646 and 57811
- detector 2: excess 0.416 mag, z 15.8, jitter ratio 3.9
- field control: target step +0.157 (W1 +0.234); neighbours N=106, median -0.002, robust sigma 0.017, max +0.264; z = 9.2
- centroid: jump at onset 0.052" +- 0.012 (4.5 sigma, PA 19); largest consecutive-visit jump 0.049"; rms 0.026"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.371, W2-W3 0.655 (W3 S/N 0.5), W3-W4 2.409 (W4 S/N 1.3), ext_flg 0, ph_qual AAUU: W3 S/N < 5: no W2-W3 class; W1-W2 > 0.25
- Gaia: RUWE 1.32, ipd_frac_multi_peak 52, NSS none, Teff nan K, logg nan, H-alpha pEW -0.092 nm, varclass YSO(0.53); M_G 5.73, -1.67 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): V* V2664 Ori [TT*; *,MIR,NIR,Or*,TT*,V*,Y*O] 0.02" refs=34
- ASAS-SN: 1470 points, cameras bA(g,155); bE(g,218); ba(V,179, d=+0.029); be(V,195, d=-0.017); bi(g,321); bm(g,239); bq(g,163); change at onset (after-before, per-camera median) +0.006 mag; largest seasonal dimming 0.06 mag at MJD 57707
- dust: excess flux W1 4.88 mJy, W2 3.00 mJy, T = 4463 K (16-84%: 3166-8000) 

### uid1394555  [D2]  YOUNG
- position 81.41583 -4.18394; Gaia DR3 3210586361269300992; G 14.79, BP-RP 1.61, plx 2.66 mas; plot `plots/uid1394555.png`
- **young:** SIMBAD young-star types Or*,TT*,Y*?,Y*O (Kiso A-0975  86) | Gaia DR3 variability class YSO(0.26)
- flags: AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.50 mag (MJD 57116)
- NEOWISE: score refetch 0.74 (stored 0.74, reproduced True); dW2 0.143, dW1 0.193, 15 visits, 204 points; baseline W1 10.88, W1-W2 0.558; onset between MJD 57809 and 58011
- detector 2: excess 0.610 mag, z 23.1, jitter ratio 15.6
- field control: target step +0.124 (W1 +0.145); neighbours N=58, median -0.003, robust sigma 0.014, max +0.042; z = 8.8
- centroid: jump at onset 0.009" +- 0.022 (0.4 sigma, PA 144); largest consecutive-visit jump 0.102"; rms 0.032"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.472, W2-W3 2.516 (W3 S/N 51.3), W3-W4 1.808 (W4 S/N 21.1), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.35, ipd_frac_multi_peak 0, NSS none, Teff 5889 K, logg 4.52, H-alpha pEW -3.032 nm, varclass YSO(0.26); M_G 6.92, -0.48 mag vs sequence (on the sequence); neighbours within 10": none
- SIMBAD (10"): Kiso A-0975  86 [TT*; *,Em*,MIR,NIR,Opt,Or*,TT*,Y*?,Y*O] 0.03" refs=9
- ASAS-SN: 1803 points, cameras bA(g,155); bE(g,218); bH(g,195); ba(V,147, d=+0.169); be(V,191, d=-0.099); bf(V,37); bh(V,147, d=+0.155); bi(g,320); bm(g,231); bq(g,162); change at onset (after-before, per-camera median) +0.155 mag; largest seasonal dimming 0.50 mag at MJD 57116
- dust: excess flux W1 3.68 mJy, W2 3.04 mJy, T = 1748 K (16-84%: 1546-2020) 

### uid1675293  [D2]  YOUNG
- position 82.65063 +10.51506; Gaia DR3 3338281610197395712; G 13.02, BP-RP 1.33, plx 2.53 mas; plot `plots/uid1675293.png`
- **young:** SIMBAD young-star types Or*,Y*?,Y*O ([DM99] 122) | Gaia DR3 variability class YSO(0.45)
- flags: 1.62 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 0.51 (stored 0.51, reproduced True); dW2 0.073, dW1 0.088, 21 visits, 218 points; baseline W1 9.86, W1-W2 0.324; onset between MJD 57446 and 57646
- detector 2: excess 0.387 mag, z 19.9, jitter ratio 10.4
- field control: target step +0.086 (W1 +0.134); neighbours N=97, median -0.003, robust sigma 0.010, max +0.026; z = 8.5
- centroid: jump at onset 0.005" +- 0.013 (0.4 sigma, PA 273); largest consecutive-visit jump 0.068"; rms 0.028"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.343, W2-W3 2.548 (W3 S/N 60.5), W3-W4 1.927 (W4 S/N 30.5), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.14, ipd_frac_multi_peak 0, NSS none, Teff 4911 K, logg 4.14, H-alpha pEW -0.332 nm, varclass YSO(0.45); M_G 5.03, -1.62 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): [DM99] 122 [Or*; *,Em*,NIR,Opt,Or*,Y*?,Y*O] 0.02" refs=27
- ASAS-SN: 939 points, cameras bA(g,184); bE(g,120); ba(V,156, d=+0.028); bi(g,236); bm(g,122); bq(g,121); change at onset (after-before, per-camera median) +0.028 mag; largest seasonal dimming 0.05 mag at MJD 57788
- dust: excess flux W1 3.90 mJy, W2 2.17 mJy, T = 8000 K (16-84%: 4443-8000) ratio bluer than an 8000 K blackbody (not dust-like)

### uid1684980  [D2]  YOUNG
- position 84.91595 -2.52274; Gaia DR3 3216493758070824064; G 13.69, BP-RP 1.43, plx 2.52 mas; plot `plots/uid1684980.png`
- **young:** SIMBAD young-star types Or*,TT*,Y*O (Haro 5-27) | Gaia DR3 variability class YSO(0.41)
- flags: 1.23 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.19 mag (MJD 58729)
- NEOWISE: score refetch 0.27 (stored 0.27, reproduced True); dW2 0.048, dW1 0.003, 21 visits, 218 points; baseline W1 8.83, W1-W2 0.704; onset between MJD 57647 and 57812
- detector 2: excess 0.766 mag, z 36.5, jitter ratio 14.6
- field control: target step +0.118 (W1 +0.108); neighbours N=121, median -0.001, robust sigma 0.014, max +0.339; z = 8.4
- centroid: jump at onset 0.011" +- 0.021 (0.5 sigma, PA 133); largest consecutive-visit jump 0.077"; rms 0.034"; toward neighbour: none; expected shift if a neighbour were the source: 4.0" G20.8: 0.42"
- AllWISE 2010: W1-W2 0.721, W2-W3 2.636 (W3 S/N 71.1), W3-W4 2.340 (W4 S/N 58.1), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.23, ipd_frac_multi_peak 1, NSS none, Teff 5770 K, logg 4.30, H-alpha pEW -4.722 nm, varclass YSO(0.41); M_G 5.70, -1.23 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 4.0" PA287 G20.76 dG+7.07
- SIMBAD (10"): Haro 5-27 [TT*; *,Em*,HH,IR,NIR,Or*,TT*,V*,Y*O] 0.03" refs=93
- ASAS-SN: 1392 points, cameras bC(g,156); bG(g,223); bc(V,151, d=-0.118); be(V,38); bg(V,152, d=+0.022); bk(g,296); bo(g,216); bs(g,160); change at onset (after-before, per-camera median) -0.048 mag; largest seasonal dimming 0.19 mag at MJD 58729
- dust: excess flux W1 3.10 mJy, W2 4.03 mJy, T = 987 K (16-84%: 715-1662) 

### uid1990636  [D2]  YOUNG
- position 83.43026 -1.14298; Gaia DR3 3217625915746195328; G 13.05, BP-RP 1.56, plx 2.39 mas; plot `plots/uid1990636.png`
- **young:** SIMBAD young-star types Or*,TT*,Y*?,Y*O (Haro 5-67) | Gaia DR3 variability class YSO(0.68)
- flags: Gaia ipd_frac_multi_peak 51% (resolved double?) | 2.31 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.11 mag (MJD 58355)
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 20 visits, 192 points; baseline W1 8.75, W1-W2 0.492; onset between MJD 57447 and 57646
- detector 2: excess 0.548 mag, z 22.2, jitter ratio 17.4
- field control: target step +0.115 (W1 +0.122); neighbours N=78, median -0.002, robust sigma 0.014, max +0.039; z = 8.3
- centroid: jump at onset 0.014" +- 0.014 (1.0 sigma, PA 94); largest consecutive-visit jump 0.081"; rms 0.031"; toward neighbour: none; expected shift if a neighbour were the source: 0.8" G16.0: 0.08"
- AllWISE 2010: W1-W2 0.469, W2-W3 2.105 (W3 S/N 72.9), W3-W4 2.178 (W4 S/N 37.2), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.23, ipd_frac_multi_peak 51, NSS none, Teff 5894 K, logg 3.84, H-alpha pEW -1.511 nm, varclass YSO(0.68); M_G 4.94, -2.31 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 0.8" PA353 G16.05 dG+3.00
- SIMBAD (10"): Haro 5-67 [TT*; *,Em*,NIR,Or*,TT*,V*,Y*?,Y*O] 0.02" refs=27
- ASAS-SN: 1444 points, cameras bC(g,149); bG(g,218); ba(V,50); bc(V,135, d=-0.039); be(V,38); bg(V,153, d=-0.007); bk(g,310); bo(g,234); bs(g,157); change at onset (after-before, per-camera median) -0.023 mag; largest seasonal dimming 0.11 mag at MJD 58355
- dust: excess flux W1 1.59 mJy, W2 2.80 mJy, T = 776 K (16-84%: 573-1077) 

### uid1791181  [D2]  YOUNG
- position 83.93147 -5.09483; Gaia DR3 3209529936754510208; G 14.54, BP-RP 1.92, plx 2.47 mas; plot `plots/uid1791181.png`
- **young:** SIMBAD young-star types Or*,TT*,TT?,Y*O (V* AO Ori) | Gaia DR3 variability class YSO(0.22)
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | 1.73 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.34 mag (MJD 60413)
- NEOWISE: score refetch 3.63 (stored 3.63, reproduced True); dW2 0.318, dW1 0.226, 18 visits, 156 points; baseline W1 9.49, W1-W2 0.622; onset between MJD 59631 and 59995
- detector 2: excess 0.631 mag, z 15.8, jitter ratio 8.4
- field control: target step +0.248 (W1 +0.243); neighbours N=89, median +0.004, robust sigma 0.030, max +0.432; z = 8.1
- centroid: jump at onset 0.012" +- 0.022 (0.5 sigma, PA 52); largest consecutive-visit jump 0.053"; rms 0.035"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.655, W2-W3 2.104 (W3 S/N 26.6), W3-W4 2.348 (W4 S/N 15.1), ext_flg 1, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.22, ipd_frac_multi_peak 0, NSS none, Teff 6055 K, logg 4.23, H-alpha pEW -0.784 nm, varclass YSO(0.22); M_G 6.51, -1.73 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): V* AO Ori [TT*; *,Em*,IR,MIR,NIR,Or*,TT*,TT?,V*,V*?,X,Y*O] 0.01" refs=49
- ASAS-SN: 1137 points, cameras bA(g,141, d=-0.165); bE(g,213, d=+0.055); ba(V,137); be(V,194); bi(g,197); bm(g,135); bq(g,120, d=+0.007); change at onset (after-before, per-camera median) +0.007 mag; largest seasonal dimming 0.34 mag at MJD 60413
- dust: excess flux W1 15.45 mJy, W2 17.86 mJy, T = 1105 K (16-84%: 1067-1145) 

### uid1804779  [D2]  YOUNG
- position 83.45645 -5.60580; Gaia DR3 3017261327701775488; G 15.62, BP-RP 2.01, plx 2.47 mas; plot `plots/uid1804779.png`
- **young:** SIMBAD young-star types Or*,TT*,TT?,Y*O (V* V354 Ori)
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | 0.92 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.28 mag (MJD 60409)
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 19 visits, 193 points; baseline W1 9.73, W1-W2 0.582; onset between MJD 58377 and 58535
- detector 2: excess 0.574 mag, z 13.8, jitter ratio 10.6
- field control: target step +0.184 (W1 +0.113); neighbours N=118, median -0.003, robust sigma 0.024, max +0.550; z = 7.9
- centroid: jump at onset 0.014" +- 0.022 (0.6 sigma, PA 168); largest consecutive-visit jump 0.061"; rms 0.039"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.548, W2-W3 1.706 (W3 S/N 31.5), W3-W4 2.369 (W4 S/N 13.6), ext_flg 1, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.18, ipd_frac_multi_peak 0, NSS none, Teff 3658 K, logg 4.10, H-alpha pEW -1.682 nm, varclass none; M_G 7.58, -0.92 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): V* V354 Ori [TT*; *,Em*,MIR,NIR,Or*,TT*,TT?,V*,Y*O,ev] 0.04" refs=34
- ASAS-SN: 1421 points, cameras bA(g,156); bE(g,217, d=-0.050); ba(V,179); be(V,195); bi(g,341, d=-0.143); bm(g,166, d=+0.266); bq(g,167, d=-0.278); change at onset (after-before, per-camera median) -0.096 mag; largest seasonal dimming 0.28 mag at MJD 60409
- dust: excess flux W1 2.91 mJy, W2 2.75 mJy, T = 1406 K (16-84%: 1211-1684) 

### uid1754877  [D2]  YOUNG
- position 84.86000 -2.25096; Gaia DR3 3216514172050881408; G 13.95, BP-RP 1.71, plx 2.49 mas; plot `plots/uid1754877.png`
- **young:** SIMBAD young-star types Or*,TT*,Y*O (Haro 5-22)
- flags: 1.72 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.14 mag (MJD 60552)
- NEOWISE: score refetch 1.33 (stored 1.33, reproduced True); dW2 0.194, dW1 0.158, 21 visits, 214 points; baseline W1 9.67, W1-W2 0.543; onset between MJD 57283 and 57448
- detector 2: excess 0.585 mag, z 19.5, jitter ratio 14.1
- field control: target step +0.111 (W1 +0.187); neighbours N=98, median -0.005, robust sigma 0.015, max +0.395; z = 7.8
- centroid: jump at onset 0.035" +- 0.015 (2.4 sigma, PA 305); largest consecutive-visit jump 0.070"; rms 0.028"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.564, W2-W3 2.534 (W3 S/N 68.6), W3-W4 2.111 (W4 S/N 38.8), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.07, ipd_frac_multi_peak 0, NSS none, Teff 5680 K, logg 4.20, H-alpha pEW -0.730 nm, varclass RS(0.25); M_G 5.93, -1.72 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): Haro 5-22 [TT*; *,Em*,NIR,Or*,TT*,V*,Y*O] 0.02" refs=22
- ASAS-SN: 1363 points, cameras bC(g,157); bG(g,223); bc(V,151, d=-0.028); be(V,38); bg(V,152, d=+0.026); bk(g,303); bo(g,179); bs(g,160); change at onset (after-before, per-camera median) -0.001 mag; largest seasonal dimming 0.14 mag at MJD 60552
- dust: excess flux W1 9.97 mJy, W2 7.44 mJy, T = 2177 K (16-84%: 1925-2529) 

### uid1424151  [D2]  YOUNG
- position 85.02105 -6.49019; Gaia DR3 3016991122718336128; G 14.81, BP-RP 1.93, plx 2.65 mas; plot `plots/uid1424151.png`
- **young:** SIMBAD young-star types Or*,Y*?,Y*O (V* V1188 Ori)
- flags: 1.33 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.56 mag (MJD 60680)
- NEOWISE: score refetch 1.00 (stored 1.00, reproduced True); dW2 0.205, dW1 0.202, 21 visits, 241 points; baseline W1 10.11, W1-W2 0.586; onset between MJD 58536 and 58743
- detector 2: excess 0.594 mag, z 14.8, jitter ratio 12.0
- field control: target step +0.119 (W1 +0.059); neighbours N=65, median +0.000, robust sigma 0.016, max +0.117; z = 7.6
- centroid: jump at onset 0.007" +- 0.020 (0.4 sigma, PA 360); largest consecutive-visit jump 0.067"; rms 0.026"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.613, W2-W3 2.168 (W3 S/N 56.2), W3-W4 1.952 (W4 S/N 25.6), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.11, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW -1.105 nm, varclass none; M_G 6.93, -1.33 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): V* V1188 Ori [Or*; *,Em*,MIR,NIR,Or*,V*,Y*?,Y*O] 0.05" refs=23
- ASAS-SN: 1073 points, cameras bB(g,91, d=+0.454); bF(g,179, d=-0.175); ba(V,30); bb(V,129); bf(V,141); bj(g,245, d=+0.197); bn(g,108); br(g,150, d=+0.032); change at onset (after-before, per-camera median) +0.114 mag; largest seasonal dimming 0.56 mag at MJD 60680
- dust: excess flux W1 6.46 mJy, W2 5.10 mJy, T = 1913 K (16-84%: 1720-2162) 

### uid1607366  [D2]  YOUNG
- position 83.55263 -4.84019; Gaia DR3 3209598587511657216; G 12.51, BP-RP 1.44, plx 2.56 mas; plot `plots/uid1607366.png`
- **young:** SIMBAD young-star types Or*,TT*,Y*O (V* V1169 Ori)
- flags: binary type in SIMBAD (**, V* V1169 Ori) | 2.40 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | not plain dust: optical brightening -0.042 mag (per-camera -0.048,-0.042,-0.045,-0.038,-0.014) together with the infrared rise | largest seasonal optical dimming 0.13 mag (MJD 60563)
- NEOWISE: score refetch 1.82 (stored 1.82, reproduced True); dW2 0.237, dW1 0.143, 20 visits, 167 points; baseline W1 8.74, W1-W2 0.359; onset between MJD 58741 and 58899
- detector 2: excess 0.421 mag, z 19.8, jitter ratio 9.4
- field control: target step +0.166 (W1 +0.175); neighbours N=164, median -0.005, robust sigma 0.023, max +0.441; z = 7.6
- centroid: jump at onset 0.031" +- 0.011 (2.8 sigma, PA 190); largest consecutive-visit jump 0.062"; rms 0.023"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.357, W2-W3 1.471 (W3 S/N 59.1), W3-W4 1.981 (W4 S/N 23.6), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.03, ipd_frac_multi_peak 0, NSS none, Teff 5111 K, logg 3.79, H-alpha pEW -0.251 nm, varclass RS(0.49); M_G 4.54, -2.40 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): V* V1169 Ori [TT*; *,**,MIR,NIR,Or*,TT*,V*,V*?,Y*O] 0.02" refs=54
- ASAS-SN: 1511 points, cameras bA(g,159, d=-0.048); bE(g,219, d=-0.042); ba(V,177); be(V,195); bi(g,344, d=-0.045); bm(g,250, d=-0.038); bq(g,167, d=-0.014); change at onset (after-before, per-camera median) -0.042 mag; largest seasonal dimming 0.13 mag at MJD 60563
- dust: excess flux W1 35.82 mJy, W2 29.76 mJy, T = 1732 K (16-84%: 1640-1834) 

### uid1262405  [D2]  YOUNG
- position 84.55883 -2.26661; Gaia DR3 3216511182753680512; G 10.31, BP-RP 0.73, plx 2.74 mas; plot `plots/uid1262405.png`
- **young:** SIMBAD young-star types Y*O (HD 294268)
- flags: centroid jump 0.050" (5.1 sigma, PA 69) not toward a Gaia neighbour | 1.57 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | optical dimming +0.064 mag after the infrared onset (debris transit signature) | largest seasonal optical dimming 0.44 mag (MJD 56542)
- NEOWISE: score refetch 0.51 (stored 0.51, reproduced True); dW2 0.083, dW1 0.058, 21 visits, 209 points; baseline W1 8.56, W1-W2 0.315; onset between MJD 57089 and 57283
- detector 2: excess 0.347 mag, z 34.5, jitter ratio 12.5
- field control: target step +0.111 (W1 +0.118); neighbours N=98, median -0.003, robust sigma 0.015, max +0.295; z = 7.5
- centroid: jump at onset 0.050" +- 0.010 (5.1 sigma, PA 69); largest consecutive-visit jump 0.097"; rms 0.024"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.291, W2-W3 4.195 (W3 S/N 73.2), W3-W4 2.794 (W4 S/N 68.0), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 0.83, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW -0.007 nm, varclass none; M_G 2.50, -1.57 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): HD 294268 [Y*O; *,IR,NIR,X,Y*O] 0.04" refs=48
- ASAS-SN: 1466 points, cameras bC(g,150); bG(g,223); ba(V,51); bc(V,148, d=+0.076); be(V,38, d=+0.052); bg(V,153); bk(g,311); bo(g,230); bs(g,162); change at onset (after-before, per-camera median) +0.064 mag; largest seasonal dimming 0.44 mag at MJD 56542
- dust: excess flux W1 16.51 mJy, W2 14.92 mJy, T = 1505 K (16-84%: 1370-1669) 

### uid1738747  [D2]  YOUNG
- position 85.35564 -8.09853; Gaia DR3 3015417682922382336; G 12.48, BP-RP 1.56, plx 2.50 mas; plot `plots/uid1738747.png`
- **young:** SIMBAD young-star types Or*,TT*,Y*O (V* DL Ori) | Gaia DR3 variability class YSO(0.39)
- flags: 2.79 mag above the main sequence at its colour | AllWISE 2010 Class I-like colour cuts (W1-W2 > 1.0, W2-W3 > 2.0)
- NEOWISE: score refetch 3.78 (stored 3.78, reproduced True); dW2 0.304, dW1 0.171, 21 visits, 214 points; baseline W1 8.04, W1-W2 1.155; onset between MJD 58015 and 58170
- detector 2: excess 1.211 mag, z 48.9, jitter ratio 7.3
- field control: target step +0.175 (W1 +0.148); neighbours N=86, median -0.006, robust sigma 0.025, max +0.398; z = 7.3
- centroid: jump at onset 0.062" +- 0.031 (2.0 sigma, PA 136); largest consecutive-visit jump 0.166"; rms 0.053"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 1.112, W2-W3 3.070 (W3 S/N 70.1), W3-W4 2.211 (W4 S/N 73.4), ext_flg 0, ph_qual AAAA: Class I-like colour cuts (W1-W2 > 1.0, W2-W3 > 2.0)
- Gaia: RUWE 1.17, ipd_frac_multi_peak 0, NSS none, Teff 5902 K, logg 3.65, H-alpha pEW -3.620 nm, varclass YSO(0.39); M_G 4.47, -2.79 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): V* DL Ori [Or*; *,Em*,IR,MIR,NIR,Or*,TT*,V*,X,Y*O] 0.01" refs=74
- ASAS-SN: 2242 points, cameras bC(g,129); bF(g,189); bG(g,256); ba(V,28); bc(V,119, d=+0.024); be(V,35); bf(V,143, d=+0.059); bg(V,214, d=+0.003); bj(g,259); bk(g,366, d=+0.033); bn(g,118); bo(g,261); bs(g,125, d=-0.039); change at onset (after-before, per-camera median) +0.024 mag; largest seasonal dimming 0.05 mag at MJD 60652
- dust: excess flux W1 28.94 mJy, W2 83.72 mJy, T = 581 K (16-84%: 555-609) 

### uid1709237  [D2]  YOUNG
- position 83.69806 -5.96582; Gaia DR3 3017188931733323776; G 13.10, BP-RP 1.40, plx 2.51 mas; plot `plots/uid1709237.png`
- **young:** SIMBAD young-star types Or*,TT*,Y*O (V* YY Ori; [SRB2015] p10) | Gaia DR3 variability class YSO(0.48)
- flags: 1.75 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.19 mag (MJD 58702)
- NEOWISE: score refetch 0.36 (stored 0.35, reproduced True); dW2 0.045, dW1 0.019, 20 visits, 184 points; baseline W1 8.66, W1-W2 0.471; onset between MJD 58741 and 58899
- detector 2: excess 0.533 mag, z 25.7, jitter ratio 10.3
- field control: target step +0.128 (W1 +0.083); neighbours N=148, median -0.002, robust sigma 0.018, max +0.203; z = 7.2
- centroid: jump at onset 0.001" +- 0.022 (0.0 sigma, PA 162); largest consecutive-visit jump 0.058"; rms 0.028"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.516, W2-W3 1.293 (W3 S/N 38.8), W3-W4 1.825 (W4 S/N 23.0), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.36, ipd_frac_multi_peak 0, NSS none, Teff 6006 K, logg 4.17, H-alpha pEW -2.474 nm, varclass YSO(0.48); M_G 5.10, -1.75 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): V* YY Ori [TT*; *,Em*,MIR,Mas,NIR,Or*,TT*,V*,X,Y*O,ev] 0.01" refs=144; [SRB2015] p10 [Y*O; Y*O,cor] 1.81" refs=1
- ASAS-SN: 1439 points, cameras bA(g,149, d=+0.113); bE(g,218, d=-0.080); ba(V,177); be(V,194); bi(g,329, d=-0.072); bm(g,220, d=-0.135); bq(g,152, d=+0.076); change at onset (after-before, per-camera median) -0.072 mag; largest seasonal dimming 0.19 mag at MJD 58702
- dust: excess flux W1 14.06 mJy, W2 14.93 mJy, T = 1213 K (16-84%: 1053-1425) 

### uid1544243  [D2]  YOUNG
- position 84.25994 -5.60825; Gaia DR3 3017295962329600640; G 12.22, BP-RP 1.09, plx 2.59 mas; plot `plots/uid1544243.png`
- **young:** SIMBAD young-star types Or*,Y*O (V* V381 Ori) | Gaia DR3 variability class YSO(0.47)
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | 1.59 mag above the main sequence at its colour
- NEOWISE: score refetch 0.16 (stored 0.16, reproduced True); dW2 0.070, dW1 0.090, 20 visits, 191 points; baseline W1 8.90, W1-W2 0.378; onset between MJD 58014 and 58168
- detector 2: excess 0.434 mag, z 25.7, jitter ratio 34.3
- field control: target step +0.109 (W1 +0.114); neighbours N=97, median -0.007, robust sigma 0.016, max +0.113; z = 7.1
- centroid: jump at onset 0.044" +- 0.029 (1.5 sigma, PA 87); largest consecutive-visit jump 0.075"; rms 0.044"; toward neighbour: none; expected shift if a neighbour were the source: 8.5" G16.3: 0.81"; 8.7" G20.3: 0.83"
- AllWISE 2010: W1-W2 0.306, W2-W3 0.365 (W3 S/N 14.6), W3-W4 3.493 (W4 S/N 10.1), ext_flg 1, ph_qual AAAA: photosphere-like (W2-W3 < 0.5)
- Gaia: RUWE 1.21, ipd_frac_multi_peak 1, NSS none, Teff 5666 K, logg 3.97, H-alpha pEW -0.769 nm, varclass YSO(0.47); M_G 4.28, -1.59 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 8.5" PA280 G16.31 dG+4.09; 8.7" PA6 G20.33 dG+8.11
- SIMBAD (10"): V* V381 Ori [Or*; *,Em*,MIR,NIR,Or*,Rad,V*,X,Y*O] 0.03" refs=44; 2MASS J05370182-0536282 [Y*O; *,Em*,G,MIR,NIR,Y*O] 8.52" refs=19
- ASAS-SN: 1511 points, cameras bA(g,157); bE(g,220); ba(V,179, d=+0.069); be(V,195, d=+0.041); bi(g,343, d=-0.025); bm(g,247); bq(g,170, d=-0.009); change at onset (after-before, per-camera median) +0.016 mag; largest seasonal dimming 0.08 mag at MJD 58435
- dust: excess flux W1 17.21 mJy, W2 14.03 mJy, T = 1794 K (16-84%: 1646-1972) 

### uid1136791  [D2]  YOUNG
- position 12.29503 +50.66562; Gaia DR3 414993900651024896; G 13.14, BP-RP 1.53, plx 2.81 mas; plot `plots/uid1136791.png`
- **young:** SIMBAD young-star types Y*? (UCAC4 704-006265)
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | 1.79 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | possible optical brightening at onset (-0.075 mag, one camera only)
- NEOWISE: score refetch 0.76 (stored 0.76, reproduced True); dW2 0.110, dW1 0.087, 21 visits, 255 points; baseline W1 9.69, W1-W2 0.370; onset between MJD 59789 and 59949
- detector 2: excess 0.428 mag, z 17.9, jitter ratio 13.0
- field control: target step +0.110 (W1 +0.079); neighbours N=102, median +0.000, robust sigma 0.016, max +0.214; z = 7.1
- centroid: jump at onset 0.023" +- 0.019 (1.2 sigma, PA 211); largest consecutive-visit jump 0.062"; rms 0.031"; toward neighbour: 4.7" PA206 G19.7 (angle 5 deg); expected shift if a neighbour were the source: 4.7" G19.7: 0.45"; 6.6" G16.5: 0.64"; 6.9" G19.2: 0.66"
- AllWISE 2010: W1-W2 0.407, W2-W3 1.479 (W3 S/N 65.4), W3-W4 1.528 (W4 S/N 24.7), ext_flg 1, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.09, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW -0.771 nm, varclass RS(0.83); M_G 5.39, -1.79 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 4.7" PA206 G19.73 dG+6.58; 6.6" PA70 G16.47 dG+3.33; 6.9" PA285 G19.18 dG+6.03
- SIMBAD (10"): UCAC4 704-006265 [Y*?; *,MIR,NIR,Y*?] 0.09" refs=1; Gaia DR3 414993900651024768 [Y*?; *,Y*?] 6.52" refs=1
- ASAS-SN: 623 points, cameras bB(g,177); bb(V,168); br(g,278, d=-0.075); change at onset (after-before, per-camera median) -0.075 mag; largest seasonal dimming 0.04 mag at MJD 59575
- dust: excess flux W1 4.59 mJy, W2 4.18 mJy, T = 1487 K (16-84%: 1292-1759) 

### uid1581123  [D2]  YOUNG
- position 84.61530 -6.91488; Gaia DR3 3016860173458220544; G 13.35, BP-RP 1.65, plx 2.57 mas; plot `plots/uid1581123.png`
- **young:** SIMBAD young-star types Or*,Y*O (V* V594 Ori) | Gaia DR3 variability class YSO(0.46)
- flags: 2.10 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | optical dimming +0.124 mag after the infrared onset (debris transit signature)
- NEOWISE: score refetch 1.25 (stored 1.25, reproduced True); dW2 0.208, dW1 0.075, 21 visits, 203 points; baseline W1 9.86, W1-W2 0.434; onset between MJD 58536 and 58742
- detector 2: excess 0.483 mag, z 17.6, jitter ratio 15.3
- field control: target step +0.146 (W1 +0.148); neighbours N=113, median -0.004, robust sigma 0.021, max +0.240; z = 7.0
- centroid: jump at onset 0.016" +- 0.014 (1.1 sigma, PA 277); largest consecutive-visit jump 0.056"; rms 0.029"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.384, W2-W3 2.306 (W3 S/N 59.0), W3-W4 2.424 (W4 S/N 37.0), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.25, ipd_frac_multi_peak 0, NSS none, Teff 5876 K, logg 4.14, H-alpha pEW -1.452 nm, varclass YSO(0.46); M_G 5.40, -2.10 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): V* V594 Ori [Or*; *,Em*,MIR,NIR,Opt,Or*,V*,X,Y*O] 0.02" refs=43
- ASAS-SN: 2602 points, cameras bA(g,150); bB(g,96, d=+0.123); bE(g,220, d=+0.098); bF(g,191, d=+0.063); ba(V,179); bb(V,129); be(V,195); bf(V,144); bi(g,341, d=+0.126); bj(g,260, d=+0.068); bm(g,247, d=+0.133); bn(g,116); bq(g,170, d=+0.177); br(g,164, d=+0.155); change at onset (after-before, per-camera median) +0.124 mag; largest seasonal dimming 0.08 mag at MJD 56892
- dust: excess flux W1 2.14 mJy, W2 2.17 mJy, T = 1283 K (16-84%: 1086-1572) 

### uid1592930  [D2]  YOUNG
- position 84.13493 -6.32217; Gaia DR3 3016976485469132800; G 12.93, BP-RP 1.39, plx 2.56 mas; plot `plots/uid1592930.png`
- **young:** SIMBAD young-star types Or*,Y*O (V* BD Ori) | Gaia DR3 variability class YSO(0.39)
- flags: 1.84 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | optical dimming +0.059 mag after the infrared onset (debris transit signature) | largest seasonal optical dimming 0.44 mag (MJD 59157)
- NEOWISE: score refetch 0.97 (stored 0.97, reproduced True); dW2 0.090, dW1 0.166, 20 visits, 191 points; baseline W1 9.51, W1-W2 0.373; onset between MJD 58013 and 58168
- detector 2: excess 0.436 mag, z 21.0, jitter ratio 7.7
- field control: target step +0.127 (W1 +0.126); neighbours N=110, median -0.003, robust sigma 0.019, max +0.189; z = 6.9
- centroid: jump at onset 0.027" +- 0.019 (1.4 sigma, PA 136); largest consecutive-visit jump 0.062"; rms 0.031"; toward neighbour: 5.1" PA121 G18.8 (angle 15 deg); expected shift if a neighbour were the source: 5.1" G18.8: 0.57"
- AllWISE 2010: W1-W2 0.341, W2-W3 1.381 (W3 S/N 44.4), W3-W4 1.658 (W4 S/N 19.0), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.09, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW -0.052 nm, varclass YSO(0.39); M_G 4.97, -1.84 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 5.1" PA121 G18.83 dG+5.90
- SIMBAD (10"): V* BD Ori [Or*; *,Em*,IR,MIR,NIR,Opt,Or*,V*,Y*O] 0.02" refs=60
- ASAS-SN: 1518 points, cameras bA(g,158); bE(g,220); ba(V,180, d=+0.058); be(V,195, d=+0.061); bi(g,343, d=+0.052); bm(g,250); bq(g,172, d=+0.454); change at onset (after-before, per-camera median) +0.059 mag; largest seasonal dimming 0.44 mag at MJD 59157
- dust: excess flux W1 6.87 mJy, W2 5.16 mJy, T = 2131 K (16-84%: 1828-2578) 

### uid1665622  [D2]  YOUNG
- position 83.92964 -4.41548; Gaia DR3 3209637139137932288; G 13.12, BP-RP 1.67, plx 2.53 mas; plot `plots/uid1665622.png`
- **young:** SIMBAD young-star types Or*,TT*,Y*O (V* BO Ori) | Gaia DR3 variability class YSO(0.37)
- flags: binary type in SIMBAD (SB*, V* BO Ori) | 2.43 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 1.24 (stored 1.24, reproduced True); dW2 0.155, dW1 0.181, 21 visits, 180 points; baseline W1 8.75, W1-W2 0.629; onset between MJD 57447 and 57646
- detector 2: excess 0.675 mag, z 24.0, jitter ratio 9.6
- field control: target step +0.137 (W1 +0.153); neighbours N=124, median -0.004, robust sigma 0.021, max +0.168; z = 6.7
- centroid: jump at onset 0.039" +- 0.018 (2.2 sigma, PA 321); largest consecutive-visit jump 0.088"; rms 0.032"; toward neighbour: none; expected shift if a neighbour were the source: 8.6" G18.2: 1.02"
- AllWISE 2010: W1-W2 0.613, W2-W3 2.479 (W3 S/N 73.0), W3-W4 1.827 (W4 S/N 46.0), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.36, ipd_frac_multi_peak 0, NSS none, Teff 6046 K, logg 3.78, H-alpha pEW -1.832 nm, varclass YSO(0.37); M_G 5.14, -2.43 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 8.6" PA84 G18.24 dG+5.12
- SIMBAD (10"): V* BO Ori [TT*; *,Em*,IR,MIR,NIR,Opt,Or*,Pu*,SB*,TT*,V*,X,Y*O] 0.02" refs=62; 2MASS J05354368-0424547 [Y*O; *,NIR,Y*O] 8.55" refs=5
- ASAS-SN: 1164 points, cameras bA(g,148); bE(g,214); ba(V,137, d=+0.053); be(V,194, d=-0.060); bi(g,197); bm(g,156); bq(g,118); change at onset (after-before, per-camera median) -0.004 mag; largest seasonal dimming 0.09 mag at MJD 58702
- dust: excess flux W1 19.01 mJy, W2 15.80 mJy, T = 1730 K (16-84%: 1531-1986) 

### uid1564349  [D2]  YOUNG
- position 83.72103 -5.05754; Gaia DR3 3209533166569829504; G 14.24, BP-RP 1.79, plx 2.58 mas; plot `plots/uid1564349.png`
- **young:** SIMBAD young-star types Or*,TT*,TT?,Y*O (V* YZ Ori) | Gaia DR3 variability class YSO(0.40)
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | 1.59 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.19 mag (MJD 59627)
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 19 visits, 176 points; baseline W1 10.08, W1-W2 0.577; onset between MJD 57646 and 57811
- detector 2: excess 0.608 mag, z 18.0, jitter ratio 4.9
- field control: target step +0.181 (W1 +0.181); neighbours N=150, median -0.002, robust sigma 0.029, max +0.169; z = 6.3
- centroid: jump at onset 0.010" +- 0.013 (0.8 sigma, PA 276); largest consecutive-visit jump 0.039"; rms 0.023"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.611, W2-W3 2.093 (W3 S/N 40.3), W3-W4 1.932 (W4 S/N 22.5), ext_flg 1, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.12, ipd_frac_multi_peak 0, NSS none, Teff 5785 K, logg 4.26, H-alpha pEW -1.683 nm, varclass YSO(0.40); M_G 6.30, -1.59 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): V* YZ Ori [TT*; *,Em*,Er*,IR,MIR,NIR,Or*,Rad,TT*,TT?,V*,X,Y*O] 0.01" refs=72
- ASAS-SN: 1307 points, cameras bA(g,149); bE(g,216); ba(V,165, d=-0.049); be(V,194, d=+0.019); bi(g,272); bm(g,181); bq(g,130); change at onset (after-before, per-camera median) -0.015 mag; largest seasonal dimming 0.19 mag at MJD 59627
- dust: excess flux W1 0.14 mJy, W2 -1.85 mJy, T = n/a K (16-84%: n/a-n/a) no W2 excess flux after onset

### uid1640594  [D2]  YOUNG
- position 84.03042 -5.70603; Gaia DR3 3017200510964946048; G 13.23, BP-RP 1.51, plx 2.54 mas; plot `plots/uid1640594.png`
- **young:** SIMBAD young-star types Or*,TT*,TT?,Y*O (V* V501 Ori)
- flags: 1.87 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 1.28 (stored 1.28, reproduced True); dW2 0.193, dW1 0.185, 18 visits, 168 points; baseline W1 9.10, W1-W2 0.550; onset between MJD 57646 and 57811
- detector 2: excess 0.609 mag, z 26.1, jitter ratio 5.9
- field control: target step +0.163 (W1 +0.135); neighbours N=126, median -0.010, robust sigma 0.029, max +0.170; z = 6.1
- centroid: jump at onset 0.026" +- 0.016 (1.7 sigma, PA 130); largest consecutive-visit jump 0.084"; rms 0.028"; toward neighbour: 6.3" PA170 G20.3 (angle 40 deg); expected shift if a neighbour were the source: 6.3" G20.3: 0.88"; 9.5" G20.8: 1.32"
- AllWISE 2010: W1-W2 0.599, W2-W3 2.466 (W3 S/N 30.2), W3-W4 2.101 (W4 S/N 21.4), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.09, ipd_frac_multi_peak 0, NSS none, Teff 5322 K, logg 4.16, H-alpha pEW -1.141 nm, varclass RS(0.70); M_G 5.26, -1.87 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 6.3" PA170 G20.35 dG+7.12; 9.5" PA319 G20.84 dG+7.61
- SIMBAD (10"): V* V501 Ori [TT*; *,Em*,MIR,NIR,Or*,TT*,TT?,V*,Y*O] 0.03" refs=45
- ASAS-SN: 1307 points, cameras bA(g,151); bE(g,217); ba(V,160, d=+0.018); be(V,195, d=-0.056); bi(g,235); bm(g,195); bq(g,154); change at onset (after-before, per-camera median) -0.019 mag; largest seasonal dimming 0.09 mag at MJD 59685
- dust: excess flux W1 10.77 mJy, W2 10.92 mJy, T = 1283 K (16-84%: 1186-1397) 

### uid1838957  [D2]  YOUNG
- position 84.11897 +0.07934; Gaia DR3 3220829441656781824; G 11.87, BP-RP 0.75, plx 2.45 mas; plot `plots/uid1838957.png`
- **young:** SIMBAD young-star types Or*,Y*?,Y*O (TYC  114-2239-1)
- flags: AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 2.08 mag (MJD 58441)
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 21 visits, 213 points; baseline W1 9.35, W1-W2 0.901; onset between MJD 59840 and 59995
- detector 2: excess 0.934 mag, z 91.4, jitter ratio 3.7
- field control: target step +0.085 (W1 +0.071); neighbours N=91, median +0.002, robust sigma 0.014, max +0.234; z = 5.9
- centroid: jump at onset 0.025" +- 0.019 (1.3 sigma, PA 98); largest consecutive-visit jump 0.133"; rms 0.048"; toward neighbour: none; expected shift if a neighbour were the source: 2.1" G16.8: 0.16"
- AllWISE 2010: W1-W2 0.889, W2-W3 2.235 (W3 S/N 68.6), W3-W4 1.753 (W4 S/N 39.3), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.06, ipd_frac_multi_peak 0, NSS none, Teff 6161 K, logg 4.22, H-alpha pEW 0.221 nm, varclass none; M_G 3.82, -0.37 mag vs sequence (on the sequence); neighbours within 10": 2.1" PA242 G16.76 dG+4.88
- SIMBAD (10"): TYC  114-2239-1 [Or*; *,NIR,Or*,Y*?,Y*O] 0.03" refs=16; Gaia DR3 3220829445951633152 [*; *] 2.12" refs=1
- ASAS-SN: 2583 points, cameras bA(g,166, d=+0.040); bC(g,157, d=-0.001); bE(g,179, d=-0.007); bG(g,220, d=+0.045); ba(V,262); bc(V,151); be(V,94); bg(V,152); bi(g,284, d=+0.008); bk(g,269, d=+0.016); bm(g,207, d=-0.023); bo(g,168, d=-0.089); bq(g,133, d=+0.039); bs(g,141, d=-0.022); change at onset (after-before, per-camera median) +0.004 mag; largest seasonal dimming 2.08 mag at MJD 58441
- dust: excess flux W1 0.45 mJy, W2 2.78 mJy, T = 420 K (16-84%: 265-549) 

### uid1706516  [D2]  YOUNG
- position 84.12298 +9.06740; Gaia DR3 3334861995892958720; G 12.72, BP-RP 1.30, plx 2.51 mas; plot `plots/uid1706516.png`
- **young:** SIMBAD young-star types Y*O (UCAC4 496-013474)
- flags: 1.83 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 1.86 (stored 1.86, reproduced True); dW2 0.270, dW1 0.255, 21 visits, 218 points; baseline W1 9.54, W1-W2 0.332; onset between MJD 58014 and 58169
- detector 2: excess 0.394 mag, z 20.5, jitter ratio 11.1
- field control: target step +0.084 (W1 +0.089); neighbours N=85, median -0.003, robust sigma 0.015, max +0.171; z = 5.8
- centroid: jump at onset 0.013" +- 0.015 (0.9 sigma, PA 122); largest consecutive-visit jump 0.041"; rms 0.026"; toward neighbour: 1.8" PA111 G19.1 (angle 11 deg); expected shift if a neighbour were the source: 1.8" G19.1: 0.13"
- AllWISE 2010: W1-W2 0.324, W2-W3 1.499 (W3 S/N 52.7), W3-W4 1.851 (W4 S/N 20.9), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.04, ipd_frac_multi_peak 1, NSS none, Teff 5012 K, logg 4.12, H-alpha pEW -0.101 nm, varclass RS(0.44); M_G 4.72, -1.83 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 1.8" PA111 G19.14 dG+6.42
- SIMBAD (10"): UCAC4 496-013474 [Y*O; *,MIR,NIR,Y*O] 0.04" refs=24
- ASAS-SN: 934 points, cameras bA(g,182); bE(g,120); ba(V,156, d=+0.002); bi(g,236); bm(g,122); bq(g,118); change at onset (after-before, per-camera median) +0.002 mag; largest seasonal dimming 0.03 mag at MJD 59970
- dust: excess flux W1 9.80 mJy, W2 8.49 mJy, T = 1609 K (16-84%: 1483-1759) 

### uid1252374  [D2]  YOUNG
- position 121.98109 -47.12941; Gaia DR3 5519263533510676224; G 13.10, BP-RP 1.37, plx 2.74 mas; plot `plots/uid1252374.png`
- **young:** SIMBAD young-star types Or*,Y*?,Y*O (2MASS J08075546-4707460) | Gaia DR3 variability class YSO(0.20)
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | 1.47 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 0.37 (stored 0.37, reproduced True); dW2 0.077, dW1 0.078, 14 visits, 167 points; baseline W1 9.90, W1-W2 0.335; onset between MJD 57152 and 57346
- detector 2: excess 0.398 mag, z 19.3, jitter ratio 16.9
- field control: target step +0.058 (W1 +0.085); neighbours N=200, median -0.005, robust sigma 0.011, max +0.227; z = 5.8
- centroid: jump at onset 0.037" +- 0.022 (1.7 sigma, PA 120); largest consecutive-visit jump 0.073"; rms 0.037"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.319, W2-W3 1.508 (W3 S/N 63.8), W3-W4 2.797 (W4 S/N 42.3), ext_flg 1, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.08, ipd_frac_multi_peak 0, NSS none, Teff 4721 K, logg 4.15, H-alpha pEW -0.274 nm, varclass YSO(0.20); M_G 5.29, -1.47 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): 2MASS J08075546-4707460 [Or*; *,NIR,Or*,Y*?,Y*O] 0.17" refs=28
- ASAS-SN: 2553 points, cameras bE(g,421); bF(g,373); be(V,231); bf(V,186); bi(g,526); bj(g,427); bm(g,207); bn(g,182); change at onset (after-before, per-camera median) n/a mag; largest seasonal dimming 0.04 mag at MJD 60256
- dust: excess flux W1 2.89 mJy, W2 1.80 mJy, T = 4152 K (16-84%: 2094-8000) 
- checks missing: ASAS-SN change at onset (no camera spans the onset)

### uid1393011  [D2]  YOUNG
- position 82.63189 +2.05143; Gaia DR3 3223556647106159232; G 14.40, BP-RP 1.77, plx 2.66 mas; plot `plots/uid1393011.png`
- **young:** SIMBAD young-star types TT*,TT?,Y*?,Y*O (Kiso A-0903 195) | Gaia DR3 variability class YSO(0.52)
- flags: 1.30 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | possible optical brightening at onset (-0.061 mag, one camera only) | largest seasonal optical dimming 0.25 mag (MJD 60603)
- NEOWISE: score refetch 0.87 (stored 0.87, reproduced True); dW2 0.142, dW1 0.190, 21 visits, 239 points; baseline W1 9.96, W1-W2 0.431; onset between MJD 57087 and 57281
- detector 2: excess 0.466 mag, z 14.3, jitter ratio 13.5
- field control: target step +0.052 (W1 +0.109); neighbours N=82, median -0.003, robust sigma 0.010, max +0.028; z = 5.5
- centroid: jump at onset 0.009" +- 0.015 (0.6 sigma, PA 18); largest consecutive-visit jump 0.044"; rms 0.025"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.371, W2-W3 1.929 (W3 S/N 58.5), W3-W4 2.228 (W4 S/N 28.8), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.18, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW -2.268 nm, varclass YSO(0.52); M_G 6.53, -1.30 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): Kiso A-0903 195 [TT*; *,Em*,MIR,NIR,TT*,TT?,V*,Y*?,Y*O] 0.03" refs=21
- ASAS-SN: 1232 points, cameras bA(g,168); bE(g,175); ba(V,210, d=-0.061); be(V,56); bi(g,279); bm(g,213); bq(g,131); change at onset (after-before, per-camera median) -0.061 mag; largest seasonal dimming 0.25 mag at MJD 60603
- dust: excess flux W1 6.09 mJy, W2 2.72 mJy, T = 8000 K (16-84%: 8000-8000) ratio bluer than an 8000 K blackbody (not dust-like)

### uid2214731  [D2]  YOUNG
- position 2.53407 +59.21642; Gaia DR3 423041020101545600; G 11.91, BP-RP 0.93, plx 2.31 mas; plot `plots/uid2214731.png`
- **young:** SIMBAD young-star types Or* (V* BE Cas)
- flags: 1.46 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.30 mag (MJD 58402)
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 6 visits, 72 points; baseline W1 8.64, W1-W2 0.640; onset between MJD 56870 and 57232
- detector 2: excess 0.687 mag, z 50.5, jitter ratio 4.6
- field control: target step +0.078 (W1 +0.073); neighbours N=123, median -0.003, robust sigma 0.015, max +0.037; z = 5.5
- centroid: jump at onset 0.050" +- 0.037 (1.4 sigma, PA 135); largest consecutive-visit jump 0.093"; rms 0.035"; toward neighbour: 6.1" PA173 G18.8 (angle 37 deg); 8.3" PA146 G19.9 (angle 11 deg); expected shift if a neighbour were the source: 6.1" G18.8: 0.42"; 8.3" G19.9: 0.58"
- AllWISE 2010: W1-W2 0.564, W2-W3 2.694 (W3 S/N 77.6), W3-W4 1.782 (W4 S/N 66.8), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.09, ipd_frac_multi_peak 0, NSS none, Teff 7489 K, logg 4.24, H-alpha pEW 0.057 nm, varclass none; M_G 3.73, -1.46 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 6.1" PA173 G18.76 dG+6.84; 8.3" PA146 G19.86 dG+7.95
- SIMBAD (10"): V* BE Cas [Or*; *,IR,NIR,Opt,Or*,V*] 0.14" refs=18
- ASAS-SN: 610 points, cameras bB(g,112); bb(V,192, d=+0.009); br(g,229); cB(g,77); change at onset (after-before, per-camera median) +0.009 mag; largest seasonal dimming 0.30 mag at MJD 58402
- dust: excess flux W1 8.51 mJy, W2 7.28 mJy, T = 1643 K (16-84%: 1314-2306) 

### uid1616399  [D2]  YOUNG
- position 84.00076 -6.70943; Gaia DR3 3016926045373231616; G 13.74, BP-RP 1.78, plx 2.55 mas; plot `plots/uid1616399.png`
- **young:** SIMBAD young-star types Or*,TT*,Y*O (V* AV Ori) | Gaia DR3 variability class YSO(0.45)
- flags: binary type in SIMBAD (**, V* AV Ori) | 2.06 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.69 mag (MJD 56618)
- NEOWISE: score refetch 0.23 (stored 0.23, reproduced True); dW2 0.029, dW1 0.069, 20 visits, 192 points; baseline W1 8.61, W1-W2 0.558; onset between MJD 58899 and 59109
- detector 2: excess 0.592 mag, z 18.1, jitter ratio 11.0
- field control: target step +0.060 (W1 +0.106); neighbours N=103, median +0.000, robust sigma 0.011, max +0.233; z = 5.4
- centroid: jump at onset 0.017" +- 0.037 (0.5 sigma, PA 49); largest consecutive-visit jump 0.084"; rms 0.053"; toward neighbour: none; expected shift if a neighbour were the source: 6.1" G17.0: 0.33"
- AllWISE 2010: W1-W2 0.507, W2-W3 1.412 (W3 S/N 48.4), W3-W4 1.695 (W4 S/N 17.9), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.29, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW -2.171 nm, varclass YSO(0.45); M_G 5.77, -2.06 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 6.1" PA304 G17.03 dG+3.29
- SIMBAD (10"): V* AV Ori [Or*; *,**,Em*,IR,MIR,NIR,Opt,Or*,TT*,V*,Y*O] 0.02" refs=72; V* V819 Ori [Or*; *,**,Em*,G,MIR,NIR,Opt,Or*,V*,Y*O] 6.08" refs=22
- ASAS-SN: 1253 points, cameras bA(g,151, d=+0.033); bE(g,215, d=+0.145); ba(V,167); be(V,193); bi(g,207, d=+0.516); bm(g,176); bq(g,144, d=-0.426); change at onset (after-before, per-camera median) +0.089 mag; largest seasonal dimming 0.69 mag at MJD 56618
- dust: excess flux W1 9.69 mJy, W2 2.92 mJy, T = 8000 K (16-84%: 8000-8000) ratio bluer than an 8000 K blackbody (not dust-like)

### uid869035  [D2]  YOUNG
- position 88.58373 +1.71571; Gaia DR3 3315809486607381248; G 13.45, BP-RP 2.03, plx 2.99 mas; plot `plots/uid869035.png`
- **young:** SIMBAD young-star types Or*,TT*,Y*O (EM* LkHA  336) | Gaia DR3 variability class YSO(0.61)
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | 2.73 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.22 mag (MJD 59226)
- NEOWISE: score refetch 0.40 (stored 0.40, reproduced True); dW2 0.021, dW1 -0.069, 18 visits, 156 points; baseline W1 8.24, W1-W2 0.587; onset between MJD 57093 and 57287
- detector 2: excess 0.576 mag, z 13.8, jitter ratio 3.6
- field control: target step +0.055 (W1 +0.049); neighbours N=94, median -0.006, robust sigma 0.012, max +0.893; z = 5.1
- centroid: jump at onset 0.109" +- 0.050 (2.2 sigma, PA 299); largest consecutive-visit jump 0.166"; rms 0.067"; toward neighbour: none; expected shift if a neighbour were the source: 5.8" G17.0: 0.29"
- AllWISE 2010: W1-W2 0.618, W2-W3 2.569 (W3 S/N 68.3), W3-W4 2.609 (W4 S/N 47.1), ext_flg 1, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.14, ipd_frac_multi_peak 0, NSS none, Teff 6157 K, logg 4.05, H-alpha pEW -1.264 nm, varclass YSO(0.61); M_G 5.83, -2.73 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 5.8" PA144 G16.98 dG+3.53
- SIMBAD (10"): EM* LkHA  336 [Or*; *,Em*,NIR,Or*,RS*,TT*,V*,Y*O] 0.07" refs=28; EM* LkHA  336C [Or*; *,Em*,NIR,Or*,Y*O] 5.76" refs=6
- ASAS-SN: 2092 points, cameras bA(g,203); bB(g,100); bE(g,161); bF(g,147); ba(V,170, d=+0.019); bb(V,181, d=-0.002); bi(g,268); bj(g,201); bm(g,146); bn(g,137); bq(g,157); br(g,154); cB(g,67); change at onset (after-before, per-camera median) +0.008 mag; largest seasonal dimming 0.22 mag at MJD 59226
- dust: excess flux W1 5.93 mJy, W2 3.54 mJy, T = 5487 K (16-84%: 1775-8000) 

### uid2072594  [D2]  YOUNG
- position 84.32853 -0.34492; Gaia DR3 3217794965658580608; G 13.47, BP-RP 1.46, plx 2.36 mas; plot `plots/uid2072594.png`
- **young:** SIMBAD young-star types Or*,TT*,Y*?,Y*O (Haro 5-79) | Gaia DR3 variability class YSO(0.43)
- flags: 1.65 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | optical dimming +0.050 mag after the infrared onset (debris transit signature)
- NEOWISE: score refetch 0.89 (stored 0.89, reproduced True); dW2 0.098, dW1 0.129, 19 visits, 199 points; baseline W1 9.64, W1-W2 0.333; onset between MJD 57647 and 57812
- detector 2: excess 0.394 mag, z 18.2, jitter ratio 9.0
- field control: target step +0.062 (W1 +0.073); neighbours N=105, median +0.000, robust sigma 0.013, max +0.124; z = 4.6
- centroid: jump at onset 0.031" +- 0.012 (2.5 sigma, PA 189); largest consecutive-visit jump 0.054"; rms 0.030"; toward neighbour: none; expected shift if a neighbour were the source: 6.7" G19.0: 0.37"
- AllWISE 2010: W1-W2 0.301, W2-W3 1.884 (W3 S/N 55.9), W3-W4 2.301 (W4 S/N 32.7), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.06, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW -0.691 nm, varclass YSO(0.43); M_G 5.33, -1.65 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 6.7" PA20 G19.03 dG+5.56
- SIMBAD (10"): Haro 5-79 [TT*; *,Em*,NIR,Or*,TT*,Y*?,Y*O] 0.04" refs=21
- ASAS-SN: 1379 points, cameras bC(g,151); bG(g,221); ba(V,51); bc(V,151, d=+0.048); be(V,38); bg(V,153, d=+0.053); bk(g,300); bo(g,173); bs(g,141); change at onset (after-before, per-camera median) +0.050 mag; largest seasonal dimming 0.04 mag at MJD 58819
- dust: excess flux W1 6.34 mJy, W2 3.70 mJy, T = 6749 K (16-84%: 3914-8000) 

### uid1616156  [D2]  YOUNG
- position 83.96928 -5.08489; Gaia DR3 3209530280351892096; G 11.35, BP-RP 1.10, plx 2.55 mas; plot `plots/uid1616156.png`
- **young:** SIMBAD young-star types Or*,Y*O (V* V815 Ori) | Gaia DR3 variability class YSO(0.79)
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | 2.51 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 0.21 (stored 0.21, reproduced True); dW2 0.027, dW1 -0.016, 19 visits, 160 points; baseline W1 8.00, W1-W2 0.328; onset between MJD 58899 and 59109
- detector 2: excess 0.384 mag, z 22.5, jitter ratio 9.5
- field control: target step +0.126 (W1 +0.116); neighbours N=110, median -0.008, robust sigma 0.030, max +0.294; z = 4.4
- centroid: jump at onset 0.026" +- 0.019 (1.4 sigma, PA 105); largest consecutive-visit jump 0.114"; rms 0.027"; toward neighbour: none; expected shift if a neighbour were the source: 2.8" G15.8: 0.30"
- AllWISE 2010: W1-W2 0.353, W2-W3 1.832 (W3 S/N 39.4), W3-W4 2.424 (W4 S/N 25.2), ext_flg 1, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.12, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW -0.298 nm, varclass YSO(0.79); M_G 3.38, -2.51 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 2.8" PA153 G15.80 dG+4.45
- SIMBAD (10"): V* V815 Ori [Or*; *,Em*,IR,MIR,NIR,Or*,V*,X,Y*O] 0.01" refs=64; V* V815 Ori B [V*; *,V*] 2.76" refs=2
- ASAS-SN: 1297 points, cameras bA(g,151, d=+0.051); bE(g,217, d=+0.028); ba(V,161); be(V,194); bi(g,242, d=+0.032); bm(g,191, d=+0.028); bq(g,141, d=-0.001); change at onset (after-before, per-camera median) +0.028 mag; largest seasonal dimming 0.08 mag at MJD 56892
- dust: excess flux W1 8.22 mJy, W2 4.57 mJy, T = 8000 K (16-84%: 2398-8000) ratio bluer than an 8000 K blackbody (not dust-like)

### uid1666435  [D2]  YOUNG
- position 83.87874 -4.92166; Gaia DR3 3209559486129350912; G 14.14, BP-RP 1.67, plx 2.53 mas; plot `plots/uid1666435.png`
- **young:** SIMBAD young-star types Or*,TT*,Y*O (V* AL Ori) | Gaia DR3 variability class YSO(0.28)
- flags: 1.41 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | optical dimming +0.067 mag after the infrared onset (debris transit signature) | largest seasonal optical dimming 0.12 mag (MJD 56618)
- NEOWISE: score refetch 1.59 (stored 1.59, reproduced True); dW2 0.129, dW1 0.109, 17 visits, 159 points; baseline W1 10.13, W1-W2 0.465; onset between MJD 57811 and 58013
- detector 2: excess 0.511 mag, z 18.1, jitter ratio 7.6
- field control: target step +0.151 (W1 +0.128); neighbours N=62, median -0.011, robust sigma 0.039, max +0.438; z = 4.1
- centroid: jump at onset 0.037" +- 0.025 (1.5 sigma, PA 59); largest consecutive-visit jump 0.076"; rms 0.034"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.503, W2-W3 3.147 (W3 S/N 16.0), W3-W4 3.616 (W4 S/N 9.5), ext_flg 0, ph_qual AAAB: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.05, ipd_frac_multi_peak 0, NSS none, Teff 5778 K, logg 4.28, H-alpha pEW -2.929 nm, varclass YSO(0.28); M_G 6.15, -1.41 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): V* AL Ori [TT*; *,Em*,IR,MIR,NIR,Or*,TT*,V*,X,Y*O] 0.04" refs=69
- ASAS-SN: 1138 points, cameras bA(g,148); bE(g,214); ba(V,139); be(V,194, d=+0.067); bi(g,179); bm(g,152); bq(g,112); change at onset (after-before, per-camera median) +0.067 mag; largest seasonal dimming 0.12 mag at MJD 56618
- dust: excess flux W1 4.04 mJy, W2 3.16 mJy, T = 1951 K (16-84%: 1535-2684) 

### uid1809868  [D2]  YOUNG
- position 83.95364 -6.20219; Gaia DR3 3017166907140902912; G 13.23, BP-RP 1.60, plx 2.47 mas; plot `plots/uid1809868.png`
- **young:** SIMBAD young-star types Or*,TT*,Y*O (V* V1001 Ori) | Gaia DR3 variability class YSO(0.55)
- flags: 2.16 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 0.79 (stored 0.79, reproduced True); dW2 0.139, dW1 0.095, 20 visits, 183 points; baseline W1 9.50, W1-W2 0.382; onset between MJD 59473 and 59631
- detector 2: excess 0.435 mag, z 16.9, jitter ratio 9.7
- field control: target step +0.072 (W1 +0.070); neighbours N=144, median +0.005, robust sigma 0.016, max +0.778; z = 4.1
- centroid: jump at onset 0.015" +- 0.017 (0.9 sigma, PA 173); largest consecutive-visit jump 0.072"; rms 0.030"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.457, W2-W3 1.906 (W3 S/N 48.6), W3-W4 2.070 (W4 S/N 32.1), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.18, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW -1.595 nm, varclass YSO(0.55); M_G 5.19, -2.16 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): V* V1001 Ori [TT*; *,Em*,MIR,NIR,Opt,Or*,TT*,V*,X,Y*O] 0.01" refs=47
- ASAS-SN: 1204 points, cameras bA(g,149, d=+0.025); bE(g,215, d=-0.037); ba(V,141); be(V,194); bi(g,207); bm(g,161); bq(g,137, d=-0.061); change at onset (after-before, per-camera median) -0.037 mag; largest seasonal dimming 0.08 mag at MJD 60651
- dust: excess flux W1 6.42 mJy, W2 5.80 mJy, T = 1504 K (16-84%: 1356-1690) 

### uid1928292  [D2]  YOUNG
- position 84.79800 -2.51850; Gaia DR3 3216488844628237056; G 14.51, BP-RP 1.98, plx 2.42 mas; plot `plots/uid1928292.png`
- **young:** SIMBAD young-star types Or*,TT*,Y*O (Haro 5-20)
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | 1.98 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.40 mag (MJD 58125)
- NEOWISE: score refetch 0.26 (stored 0.26, reproduced True); dW2 0.089, dW1 0.102, 21 visits, 223 points; baseline W1 9.88, W1-W2 0.708; onset between MJD 57089 and 57283
- detector 2: excess 0.706 mag, z 17.0, jitter ratio 31.7
- field control: target step +0.075 (W1 +0.063); neighbours N=128, median -0.005, robust sigma 0.020, max +0.341; z = 4.0
- centroid: jump at onset 0.019" +- 0.017 (1.1 sigma, PA 45); largest consecutive-visit jump 0.061"; rms 0.029"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.641, W2-W3 2.695 (W3 S/N 66.0), W3-W4 2.064 (W4 S/N 26.5), ext_flg 1, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.27, ipd_frac_multi_peak 0, NSS none, Teff 6035 K, logg 4.24, H-alpha pEW -1.004 nm, varclass none; M_G 6.43, -1.98 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): Haro 5-20 [TT*; *,Em*,NIR,Or*,RR*,TT*,V*,Y*O,ev] 0.03" refs=43
- ASAS-SN: 591 points, cameras bC(g,137); bG(g,83); bc(V,149, d=+0.162); be(V,38, d=-0.047); bg(V,152); bs(g,32); change at onset (after-before, per-camera median) +0.058 mag; largest seasonal dimming 0.40 mag at MJD 58125
- dust: excess flux W1 3.42 mJy, W2 4.51 mJy, T = 973 K (16-84%: 902-1057) 

### uid1749579  [D2]  YOUNG
- position 84.66781 -2.50516; Gaia DR3 3216491151026233472; G 14.01, BP-RP 1.96, plx 2.49 mas; plot `plots/uid1749579.png`
- **young:** SIMBAD young-star types TT*,Y*O (Haro 5-13)
- flags: 2.35 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.17 mag (MJD 56550)
- NEOWISE: score refetch 1.12 (stored 1.12, reproduced True); dW2 0.055, dW1 0.092, 21 visits, 223 points; baseline W1 9.94, W1-W2 0.594; onset between MJD 58378 and 58536
- detector 2: excess 0.596 mag, z 14.5, jitter ratio 4.3
- field control: target step +0.065 (W1 +0.044); neighbours N=117, median +0.002, robust sigma 0.016, max +0.509; z = 3.9
- centroid: jump at onset 0.010" +- 0.018 (0.5 sigma, PA 241); largest consecutive-visit jump 0.057"; rms 0.029"; toward neighbour: 9.6" PA255 G17.5 (angle 14 deg); expected shift if a neighbour were the source: 9.6" G17.5: 0.56"
- AllWISE 2010: W1-W2 0.558, W2-W3 2.303 (W3 S/N 67.7), W3-W4 2.063 (W4 S/N 30.3), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.12, ipd_frac_multi_peak 0, NSS none, Teff 5509 K, logg 3.98, H-alpha pEW -0.287 nm, varclass none; M_G 5.99, -2.35 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 9.6" PA255 G17.48 dG+3.47
- SIMBAD (10"): Haro 5-13 [TT*; *,Em*,LM*,NIR,TT*,Y*O] 0.02" refs=41; 2MASS J05383965-0230210 [Y*O; *,NIR,Y*O] 9.67" refs=2
- ASAS-SN: 1325 points, cameras bC(g,151); bG(g,223, d=-0.073); ba(V,50); bc(V,151); be(V,38); bg(V,153); bk(g,180, d=+0.273); bo(g,225, d=-0.038); bs(g,154, d=+0.003); change at onset (after-before, per-camera median) -0.018 mag; largest seasonal dimming 0.17 mag at MJD 56550
- dust: excess flux W1 1.75 mJy, W2 2.14 mJy, T = 1044 K (16-84%: 897-1239) 

### uid1357327  [D2]  YOUNG
- position 83.65061 -6.09298; Gaia DR3 3017163539886560768; G 14.72, BP-RP 1.68, plx 2.68 mas; plot `plots/uid1357327.png`
- **young:** SIMBAD young-star types Or*,TT*,Y*O (V* XX Ori) | Gaia DR3 variability class YSO(0.35)
- flags: AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | optical dimming +0.102 mag after the infrared onset (debris transit signature) | largest seasonal optical dimming 0.25 mag (MJD 57974)
- NEOWISE: score refetch 0.59 (stored 0.59, reproduced True); dW2 0.075, dW1 0.138, 20 visits, 183 points; baseline W1 10.17, W1-W2 0.484; onset between MJD 57087 and 57282
- detector 2: excess 0.529 mag, z 18.4, jitter ratio 9.8
- field control: target step +0.063 (W1 +0.088); neighbours N=127, median -0.003, robust sigma 0.019, max +0.177; z = 3.4
- centroid: jump at onset 0.010" +- 0.019 (0.5 sigma, PA 259); largest consecutive-visit jump 0.115"; rms 0.033"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.491, W2-W3 1.812 (W3 S/N 42.9), W3-W4 1.881 (W4 S/N 23.1), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.15, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW -2.942 nm, varclass YSO(0.35); M_G 6.86, -0.73 mag vs sequence (on the sequence); neighbours within 10": none
- SIMBAD (10"): V* XX Ori [TT*; *,Em*,Er*,MIR,NIR,Opt,Or*,TT*,V*,X,Y*O,ev] 0.03" refs=59
- ASAS-SN: 1452 points, cameras bA(g,146); bE(g,212); ba(V,179, d=+0.107); be(V,195, d=+0.098); bi(g,337); bm(g,220); bq(g,163); change at onset (after-before, per-camera median) +0.102 mag; largest seasonal dimming 0.25 mag at MJD 57974
- dust: excess flux W1 2.80 mJy, W2 1.81 mJy, T = 3441 K (16-84%: 2193-8000) 

### uid1713922  [D2]  YOUNG
- position 85.10405 -8.12587; Gaia DR3 3015414629201592576; G 13.18, BP-RP 1.86, plx 2.51 mas; plot `plots/uid1713922.png`
- **young:** SIMBAD young-star types Or*,Y*?,Y*O (V* V1304 Ori) | Gaia DR3 variability class YSO(0.53)
- flags: 2.90 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 1.09 (stored 1.09, reproduced True); dW2 0.092, dW1 0.062, 21 visits, 189 points; baseline W1 8.15, W1-W2 0.615; onset between MJD 57089 and 57283
- detector 2: excess 0.635 mag, z 16.8, jitter ratio 5.8
- field control: target step +0.050 (W1 +0.045); neighbours N=58, median -0.007, robust sigma 0.017, max +0.227; z = 3.3
- centroid: jump at onset 0.043" +- 0.017 (2.5 sigma, PA 105); largest consecutive-visit jump 0.060"; rms 0.028"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.603, W2-W3 2.330 (W3 S/N 73.7), W3-W4 1.942 (W4 S/N 50.3), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.16, ipd_frac_multi_peak 0, NSS none, Teff 5673 K, logg 3.77, H-alpha pEW -1.712 nm, varclass YSO(0.53); M_G 5.17, -2.90 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): V* V1304 Ori [Or*; *,Em*,IR,MIR,NIR,Or*,V*,Y*?,Y*O] 0.01" refs=48; IRAS C05380-0808 [*; *,IR] 7.54" refs=1
- ASAS-SN: 2243 points, cameras bC(g,128); bF(g,190); bG(g,257); ba(V,28); bc(V,119, d=-0.041); be(V,35, d=-0.005); bf(V,143); bg(V,213); bj(g,259); bk(g,355); bn(g,122); bo(g,263); bs(g,131); change at onset (after-before, per-camera median) -0.023 mag; largest seasonal dimming 0.08 mag at MJD 59692
- dust: excess flux W1 4.73 mJy, W2 8.14 mJy, T = 790 K (16-84%: 652-967) 

### uid1817699  [D2]  YOUNG
- position 85.03704 -2.55939; Gaia DR3 3216445899250910976; G 14.32, BP-RP 1.85, plx 2.46 mas; plot `plots/uid1817699.png`
- **young:** SIMBAD young-star types Or*,TT*,Y*O (V* V608 Ori)
- flags: 1.76 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | optical dimming +0.120 mag after the infrared onset (debris transit signature) | largest seasonal optical dimming 0.17 mag (MJD 60201)
- NEOWISE: score refetch 0.18 (stored 0.18, reproduced True); dW2 0.030, dW1 0.004, 21 visits, 208 points; baseline W1 9.15, W1-W2 0.559; onset between MJD 58901 and 59110
- detector 2: excess 0.581 mag, z 15.8, jitter ratio 13.3
- field control: target step +0.044 (W1 +0.073); neighbours N=112, median -0.002, robust sigma 0.016, max +0.462; z = 3.0
- centroid: jump at onset 0.008" +- 0.025 (0.3 sigma, PA 3); largest consecutive-visit jump 0.058"; rms 0.032"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.593, W2-W3 2.087 (W3 S/N 66.1), W3-W4 2.116 (W4 S/N 38.6), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.16, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW -1.718 nm, varclass none; M_G 6.28, -1.76 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): V* V608 Ori [TT*; *,Em*,HH,NIR,Or*,TT*,V*,Y*O] 0.04" refs=51
- ASAS-SN: 1405 points, cameras bC(g,150, d=+0.172); bG(g,220, d=+0.136); bc(V,148); be(V,36); bg(V,144); bk(g,313, d=+0.088); bo(g,229, d=+0.033); bs(g,165, d=+0.120); change at onset (after-before, per-camera median) +0.120 mag; largest seasonal dimming 0.17 mag at MJD 60201
- dust: excess flux W1 9.05 mJy, W2 8.64 mJy, T = 1389 K (16-84%: 1266-1540) 

### uid1450875  [D2]  YOUNG
- position 83.54366 -4.84309; Gaia DR3 3209598548853143680; G 12.65, BP-RP 1.31, plx 2.63 mas; plot `plots/uid1450875.png`
- **young:** SIMBAD young-star types Or*,TT*,Y*O (V* V1931 Ori) | Gaia DR3 variability class YSO(0.41)
- flags: binary type in SIMBAD (**, V* V1931 Ori) | 1.84 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | not plain dust: optical brightening -0.026 mag (per-camera -0.023,-0.029) together with the infrared rise
- NEOWISE: score refetch 0.28 (stored 0.28, reproduced True); dW2 0.048, dW1 0.046, 19 visits, 165 points; baseline W1 9.23, W1-W2 0.349; onset between MJD 57282 and 57446
- detector 2: excess 0.412 mag, z 21.4, jitter ratio 15.4
- field control: target step +0.073 (W1 +0.049); neighbours N=166, median -0.001, robust sigma 0.026, max +0.363; z = 2.9
- centroid: jump at onset 0.010" +- 0.020 (0.5 sigma, PA 160); largest consecutive-visit jump 0.072"; rms 0.032"; toward neighbour: none; expected shift if a neighbour were the source: 7.7" G16.5: 0.50"
- AllWISE 2010: W1-W2 0.377, W2-W3 1.255 (W3 S/N 39.4), W3-W4 1.952 (W4 S/N 9.3), ext_flg 0, ph_qual AAAB: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.03, ipd_frac_multi_peak 0, NSS none, Teff 5460 K, logg 4.01, H-alpha pEW -0.171 nm, varclass YSO(0.41); M_G 4.75, -1.84 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 7.7" PA359 G16.51 dG+3.86
- SIMBAD (10"): V* V1931 Ori [TT*; *,**,MIR,NIR,Or*,TT*,V*,X,Y*O] 0.02" refs=36; 2E 0531.7-0452 [X; X] 5.16" refs=0; 2MASS J05341046-0450275 [TT*; *,MIR,NIR,TT*,Y*O] 7.69" refs=10
- ASAS-SN: 1511 points, cameras bA(g,159); bE(g,219); ba(V,177, d=-0.023); be(V,195, d=-0.029); bi(g,344); bm(g,250); bq(g,167); change at onset (after-before, per-camera median) -0.026 mag; largest seasonal dimming 0.07 mag at MJD 60563
- dust: excess flux W1 4.99 mJy, W2 5.50 mJy, T = 1164 K (16-84%: 1025-1344) 

### uid1618943  [D2]  YOUNG
- position 83.65611 -5.58110; Gaia DR3 3017263939041875712; G 14.09, BP-RP 1.74, plx 2.55 mas; plot `plots/uid1618943.png`
- **young:** SIMBAD young-star types Or*,TT?,Y*O (V* IV Ori)
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | 1.61 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.11 mag (MJD 56892)
- NEOWISE: score refetch 0.40 (stored 0.41, reproduced True); dW2 0.052, dW1 0.047, 20 visits, 179 points; baseline W1 9.47, W1-W2 0.491; onset between MJD 58899 and 59108
- detector 2: excess 0.529 mag, z 16.8, jitter ratio 7.2
- field control: target step +0.066 (W1 +0.098); neighbours N=133, median -0.001, robust sigma 0.024, max +0.471; z = 2.8
- centroid: jump at onset 0.055" +- 0.031 (1.8 sigma, PA 66); largest consecutive-visit jump 0.040"; rms 0.042"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.464, W2-W3 2.148 (W3 S/N 59.3), W3-W4 3.204 (W4 S/N 21.3), ext_flg 1, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.11, ipd_frac_multi_peak 0, NSS none, Teff 4939 K, logg 4.17, H-alpha pEW -1.278 nm, varclass none; M_G 6.12, -1.61 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): V* IV Ori [Or*; *,Em*,MIR,NIR,Or*,TT?,V*,Y*O] 0.02" refs=58
- ASAS-SN: 1503 points, cameras bA(g,153, d=-0.004); bE(g,219, d=+0.059); ba(V,179); be(V,195); bi(g,344, d=+0.003); bm(g,248, d=-0.069); bq(g,165, d=-0.021); change at onset (after-before, per-camera median) -0.004 mag; largest seasonal dimming 0.11 mag at MJD 56892
- dust: excess flux W1 3.83 mJy, W2 3.05 mJy, T = 1881 K (16-84%: 1465-2696) 

### uid1761616  [D2]  YOUNG
- position 82.67238 +10.50902; Gaia DR3 3338281335319489024; G 11.71, BP-RP 1.12, plx 2.49 mas; plot `plots/uid1761616.png`
- **young:** SIMBAD young-star types Y*O (2MASS J05304136+1030325)
- flags: 2.26 mag above the main sequence at its colour
- NEOWISE: score refetch 1.41 (stored 1.41, reproduced True); dW2 0.106, dW1 0.126, 21 visits, 215 points; baseline W1 8.99, W1-W2 0.191; onset between MJD 57446 and 57646
- detector 2: excess 0.248 mag, z 14.1, jitter ratio 7.0
- field control: target step +0.024 (W1 +0.047); neighbours N=103, median -0.003, robust sigma 0.010, max +0.086; z = 2.6
- centroid: jump at onset 0.029" +- 0.016 (1.9 sigma, PA 289); largest consecutive-visit jump 0.017"; rms 0.026"; toward neighbour: none; expected shift if a neighbour were the source: 4.3" G19.7: 0.10"
- AllWISE 2010: W1-W2 0.167, W2-W3 0.766 (W3 S/N 47.0), W3-W4 2.752 (W4 S/N 30.6), ext_flg 0, ph_qual AAAA: weak W3 excess (0.5 < W2-W3 < 1.0)
- Gaia: RUWE 1.08, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW -0.329 nm, varclass RS(0.27); M_G 3.69, -2.26 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 4.3" PA185 G19.72 dG+8.01
- SIMBAD (10"): 2MASS J05304136+1030325 [Y*O; *,NIR,Y*O] 0.04" refs=17; IRAS 05279+1028 [FIR; FIR,IR] 3.88" refs=1
- ASAS-SN: 928 points, cameras bA(g,184); bE(g,120); ba(V,156, d=-0.015); bi(g,236); bm(g,122); bq(g,110); change at onset (after-before, per-camera median) -0.015 mag; largest seasonal dimming 0.03 mag at MJD 59324
- dust: excess flux W1 7.87 mJy, W2 3.88 mJy, T = 8000 K (16-84%: 8000-8000) ratio bluer than an 8000 K blackbody (not dust-like)

### uid1511589  [D2]  YOUNG
- position 80.08108 -5.76540; Gaia DR3 3209947132696346752; G 12.10, BP-RP 1.37, plx 2.60 mas; plot `plots/uid1511589.png`
- **young:** SIMBAD young-star types Or*,TT*,Y*O (EM* StHA   37) | Gaia DR3 variability class YSO(0.28)
- flags: 2.58 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 20 visits, 213 points; baseline W1 8.09, W1-W2 0.421; onset between MJD 58006 and 58164
- detector 2: excess 0.484 mag, z 23.4, jitter ratio 8.4
- field control: target step +0.034 (W1 -0.021); neighbours N=51, median -0.004, robust sigma 0.016, max +0.081; z = 2.4
- centroid: jump at onset 0.021" +- 0.015 (1.4 sigma, PA 212); largest consecutive-visit jump 0.054"; rms 0.024"; toward neighbour: none; expected shift if a neighbour were the source: 7.0" G20.5: 0.21"
- AllWISE 2010: W1-W2 0.435, W2-W3 2.431 (W3 S/N 72.0), W3-W4 2.179 (W4 S/N 48.8), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.09, ipd_frac_multi_peak 0, NSS none, Teff 5604 K, logg 4.02, H-alpha pEW -1.403 nm, varclass YSO(0.28); M_G 4.18, -2.58 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 7.0" PA282 G20.54 dG+8.44
- SIMBAD (10"): EM* StHA   37 [TT*; *,Em*,IR,MIR,NIR,Or*,TT*,Y*O] 0.03" refs=21
- ASAS-SN: 0 points, cameras n/a; change at onset (after-before, per-camera median) n/a mag; largest seasonal dimming n/a mag at MJD n/a
- dust: excess flux W1 -8.97 mJy, W2 -6.00 mJy, T = n/a K (16-84%: n/a-n/a) no W2 excess flux after onset
- checks missing: ASAS-SN (no source)

### uid1505343  [D2]  YOUNG
- position 83.15619 -5.21142; Gaia DR3 3209492072320894080; G 14.83, BP-RP 2.12, plx 2.61 mas; plot `plots/uid1505343.png`
- **young:** SIMBAD young-star types Or*,TT*,Y*O (V* V383 Ori)
- flags: 1.93 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | not plain dust: optical brightening -0.069 mag (per-camera -0.066,-0.072) together with the infrared rise
- NEOWISE: score refetch 0.84 (stored 0.84, reproduced True); dW2 0.190, dW1 0.173, 20 visits, 181 points; baseline W1 10.57, W1-W2 0.740; onset between MJD 57446 and 57645
- detector 2: excess 0.715 mag, z 16.6, jitter ratio 20.2
- field control: target step +0.038 (W1 -0.054); neighbours N=75, median +0.002, robust sigma 0.016, max +0.524; z = 2.3
- centroid: jump at onset 0.006" +- 0.022 (0.3 sigma, PA 276); largest consecutive-visit jump 0.106"; rms 0.036"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.691, W2-W3 2.171 (W3 S/N 56.9), W3-W4 1.803 (W4 S/N 24.2), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.07, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW -0.091 nm, varclass none; M_G 6.91, -1.93 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): V* V383 Ori [TT*; *,BY*,Er*,MIR,NIR,Or*,TT*,V*,Y*O] 0.01" refs=24
- ASAS-SN: 1460 points, cameras bA(g,153); bE(g,217); ba(V,174, d=-0.066); be(V,194, d=-0.072); bi(g,331); bm(g,226); bq(g,165); change at onset (after-before, per-camera median) -0.069 mag; largest seasonal dimming 0.06 mag at MJD 59252
- dust: excess flux W1 5.15 mJy, W2 4.67 mJy, T = 1496 K (16-84%: 1405-1601) 

### uid2027333  [D2]  YOUNG
- position 86.64178 +9.91437; Gaia DR3 3336303180759424640; G 13.70, BP-RP 1.79, plx 2.38 mas; plot `plots/uid2027333.png`
- **young:** SIMBAD young-star types Y*O (1RXS J054634.2+095452) | Gaia DR3 variability class YSO(0.53)
- flags: 2.29 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | optical dimming +0.154 mag after the infrared onset (debris transit signature) | largest seasonal optical dimming 0.34 mag (MJD 57319)
- NEOWISE: score refetch 1.18 (stored 1.18, reproduced True); dW2 0.045, dW1 0.051, 20 visits, 188 points; baseline W1 9.11, W1-W2 0.699; onset between MJD 57091 and 57285
- detector 2: excess 0.731 mag, z 22.0, jitter ratio 3.2
- field control: target step +0.025 (W1 +0.053); neighbours N=122, median -0.005, robust sigma 0.014, max +0.029; z = 2.2
- centroid: jump at onset 0.031" +- 0.030 (1.0 sigma, PA 324); largest consecutive-visit jump 0.109"; rms 0.044"; toward neighbour: none; expected shift if a neighbour were the source: 1.7" G16.9: 0.04"; 4.1" G19.2: 0.09"
- AllWISE 2010: W1-W2 0.701, W2-W3 2.408 (W3 S/N 76.8), W3-W4 1.699 (W4 S/N 44.9), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.14, ipd_frac_multi_peak 0, NSS none, Teff 4895 K, logg 4.12, H-alpha pEW -0.406 nm, varclass YSO(0.53); M_G 5.58, -2.29 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 1.7" PA211 G16.88 dG+3.19; 4.1" PA69 G19.17 dG+5.47
- SIMBAD (10"): 1RXS J054634.2+095452 [Y*O; *,MIR,NIR,X,Y*O] 0.05" refs=12; Gaia DR3 3336303180759424512 [*; *] 1.72" refs=1
- ASAS-SN: 913 points, cameras bB(g,111); bF(g,139); bb(V,197, d=+0.154); bj(g,220); bn(g,123); br(g,123); change at onset (after-before, per-camera median) +0.154 mag; largest seasonal dimming 0.34 mag at MJD 57319
- dust: excess flux W1 3.73 mJy, W2 3.49 mJy, T = 1427 K (16-84%: 1130-2021) 

### uid1493976  [D2]  YOUNG
- position 83.56914 -3.95624; Gaia DR3 3215869922660573568; G 12.91, BP-RP 1.39, plx 2.61 mas; plot `plots/uid1493976.png`
- **young:** SIMBAD young-star types Or*,Y*?,Y*O (V* V1937 Ori)
- flags: 1.82 mag above the main sequence at its colour | not plain dust: optical brightening -0.053 mag (per-camera -0.035,-0.045,-0.061,-0.072) together with the infrared rise
- NEOWISE: score refetch 0.86 (stored 0.86, reproduced True); dW2 0.088, dW1 0.088, 21 visits, 208 points; baseline W1 9.68, W1-W2 0.227; onset between MJD 57447 and 57646
- detector 2: excess 0.290 mag, z 14.0, jitter ratio 8.9
- field control: target step +0.012 (W1 +0.043); neighbours N=76, median -0.006, robust sigma 0.010, max +0.034; z = 1.8
- centroid: jump at onset 0.014" +- 0.014 (1.0 sigma, PA 265); largest consecutive-visit jump 0.025"; rms 0.023"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.231, W2-W3 1.614 (W3 S/N 50.2), W3-W4 3.224 (W4 S/N 36.6), ext_flg 0, ph_qual AAAA: W3 excess only (W2-W3 > 1.0; debris-disk-like or blend)
- Gaia: RUWE 1.14, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW -0.821 nm, varclass none; M_G 4.99, -1.82 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): V* V1937 Ori [Or*; *,Em*,MIR,NIR,Or*,V*,Y*?,Y*O] 0.02" refs=16
- ASAS-SN: 2942 points, cameras bA(g,158); bC(g,142); bE(g,221); bG(g,222); ba(V,229, d=-0.035); bc(V,135, d=-0.045); be(V,233, d=-0.061); bg(V,152, d=-0.072); bi(g,341); bk(g,300); bm(g,251); bo(g,229); bq(g,168); bs(g,161); change at onset (after-before, per-camera median) -0.053 mag; largest seasonal dimming 0.05 mag at MJD 60563
- dust: excess flux W1 4.75 mJy, W2 3.35 mJy, T = 2527 K (16-84%: 2025-3425) 

### uid1681049  [D2]  YOUNG
- position 84.80285 +9.26448; Gaia DR3 3336345374518372992; G 13.74, BP-RP 1.43, plx 2.52 mas; plot `plots/uid1681049.png`
- **young:** SIMBAD young-star types Or*,TT*,Y*O (Haro 6-74)
- flags: 1.18 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | possible optical brightening at onset (-0.047 mag, one camera only) | largest seasonal optical dimming 0.19 mag (MJD 60644)
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 21 visits, 226 points; baseline W1 9.59, W1-W2 0.674; onset between MJD 57812 and 58015
- detector 2: excess 0.736 mag, z 35.0, jitter ratio 16.2
- field control: target step +0.006 (W1 +0.049); neighbours N=88, median -0.007, robust sigma 0.011, max +0.024; z = 1.1
- centroid: jump at onset 0.024" +- 0.016 (1.4 sigma, PA 118); largest consecutive-visit jump 0.070"; rms 0.034"; toward neighbour: none; expected shift if a neighbour were the source: 6.4" G20.0: 0.04"
- AllWISE 2010: W1-W2 0.658, W2-W3 3.023 (W3 S/N 68.9), W3-W4 1.919 (W4 S/N 49.0), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.10, ipd_frac_multi_peak 0, NSS none, Teff 5794 K, logg 4.29, H-alpha pEW -6.022 nm, varclass none; M_G 5.75, -1.18 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 6.4" PA344 G20.01 dG+6.26
- SIMBAD (10"): Haro 6-74 [TT*; *,NIR,Or*,TT*,Y*O] 0.04" refs=24
- ASAS-SN: 928 points, cameras bA(g,183); bE(g,120); ba(V,154, d=-0.047); bi(g,230); bm(g,122); bq(g,119); change at onset (after-before, per-camera median) -0.047 mag; largest seasonal dimming 0.19 mag at MJD 60644
- dust: excess flux W1 -0.19 mJy, W2 -2.04 mJy, T = n/a K (16-84%: n/a-n/a) no W2 excess flux after onset

### uid1356608  [D2]  YOUNG
- position 56.42745 +34.77553; Gaia DR3 218336625295850624; G 13.84, BP-RP 1.65, plx 2.68 mas; plot `plots/uid1356608.png`
- **young:** Gaia DR3 variability class YSO(0.20)
- flags: 1.52 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 1.09 (stored 1.09, reproduced True); dW2 0.144, dW1 0.102, 21 visits, 218 points; baseline W1 9.18, W1-W2 0.400; onset between MJD 57425 and 57626
- detector 2: excess 0.448 mag, z 16.3, jitter ratio 11.6
- field control: target step +0.006 (W1 +0.016); neighbours N=89, median -0.003, robust sigma 0.011, max +0.029; z = 0.9
- centroid: jump at onset 0.014" +- 0.012 (1.2 sigma, PA 274); largest consecutive-visit jump 0.061"; rms 0.027"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.469, W2-W3 1.139 (W3 S/N 58.1), W3-W4 1.729 (W4 S/N 18.3), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.34, ipd_frac_multi_peak 1, NSS none, Teff nan K, logg nan, H-alpha pEW -3.526 nm, varclass YSO(0.20); M_G 5.98, -1.52 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): 2MASS J03454257+3446320 [Em*; *,Em*,MIR,NIR,Opt,V*,ev] 0.09" refs=13
- ASAS-SN: 0 points, cameras n/a; change at onset (after-before, per-camera median) n/a mag; largest seasonal dimming n/a mag at MJD n/a
- dust: excess flux W1 6.32 mJy, W2 6.55 mJy, T = 1248 K (16-84%: 1112-1423) 
- checks missing: ASAS-SN (no source)

### uid1569617  [D2]  YOUNG
- position 94.13963 +22.51922; Gaia DR3 3377028472978159232; G 15.64, BP-RP 1.71, plx 2.57 mas; plot `plots/uid1569617.png`
- **young:** SIMBAD young-star types Y*? (WISEA J061633.49+223110.4)
- flags: AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 0.57 (stored 0.57, reproduced True); dW2 0.030, dW1 0.017, 11 visits, 98 points; baseline W1 12.21, W1-W2 0.952; onset between MJD 58545 and 58909
- detector 2: excess 0.994 mag, z 33.0, jitter ratio 3.8
- field control: target step +0.017 (W1 +0.009); neighbours N=183, median +0.009, robust sigma 0.020, max +0.099; z = 0.4
- centroid: jump at onset 0.297" +- 0.119 (2.5 sigma, PA 24); largest consecutive-visit jump 0.285"; rms 0.171"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.929, W2-W3 2.793 (W3 S/N 27.9), W3-W4 1.267 (W4 S/N 7.5), ext_flg 3, ph_qual AAAB: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.18, ipd_frac_multi_peak 0, NSS none, Teff 4182 K, logg 4.66, H-alpha pEW -0.077 nm, varclass none; M_G 7.69, +0.04 mag vs sequence (on the sequence); neighbours within 10": none
- SIMBAD (10"): WISEA J061633.49+223110.4 [Y*?; MIR,Y*?] 1.26" refs=1; WISEA J061633.23+223103.7 [Y*?; MIR,Y*?] 6.76" refs=1
- ASAS-SN: 828 points, cameras bD(g,194, d=+0.019); bH(g,93); bd(V,187); bl(g,165, d=+0.006); bp(g,55); bt(g,134, d=+0.053); change at onset (after-before, per-camera median) +0.019 mag; largest seasonal dimming 0.08 mag at MJD 57048
- dust: excess flux W1 0.03 mJy, W2 0.22 mJy, T = 412 K (16-84%: 150-631) 

### uid1486857  [D2]  YOUNG
- position 0.26380 +47.02299; Gaia DR3 387155327088745728; G 13.25, BP-RP 1.55, plx 2.62 mas; plot `plots/uid1486857.png`
- **young:** SIMBAD young-star types Y*? (UCAC4 686-000123) | Gaia DR3 variability class YSO(0.48)
- flags: 1.90 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 22 visits, 246 points; baseline W1 9.00, W1-W2 0.431; onset between MJD 58680 and 58840
- detector 2: excess 0.487 mag, z 19.8, jitter ratio 13.2
- field control: target step -0.041 (W1 -0.042); neighbours N=82, median -0.011, robust sigma 0.016, max +0.041; z = -1.8
- centroid: jump at onset 0.007" +- 0.021 (0.3 sigma, PA 138); largest consecutive-visit jump 0.084"; rms 0.034"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.402, W2-W3 2.113 (W3 S/N 69.0), W3-W4 1.917 (W4 S/N 38.7), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.23, ipd_frac_multi_peak 0, NSS none, Teff 5188 K, logg 4.14, H-alpha pEW -1.360 nm, varclass YSO(0.48); M_G 5.34, -1.90 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): UCAC4 686-000123 [Y*?; *,MIR,NIR,Y*?] 0.05" refs=1
- ASAS-SN: 1438 points, cameras bC(g,258, d=-0.014); bD(g,232, d=+0.178); bc(V,263); bd(V,197); bs(g,194, d=-0.010); bt(g,294, d=-0.001); change at onset (after-before, per-camera median) -0.005 mag; largest seasonal dimming 0.09 mag at MJD 59517
- dust: excess flux W1 2.05 mJy, W2 0.97 mJy, T = 8000 K (16-84%: 2473-8000) ratio bluer than an 8000 K blackbody (not dust-like)

### uid800756  [D2]  YOUNG
- position 133.13021 -43.18291; Gaia DR3 5523872681948712960; G 12.51, BP-RP 1.37, plx 3.05 mas; plot `plots/uid800756.png`
- **young:** SIMBAD young-star types Y*? (2MASS J08523126-4310586) | Gaia DR3 variability class YSO(0.10)
- flags: 1.83 mag above the main sequence at its colour
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 16 visits, 167 points; baseline W1 9.01, W1-W2 0.329; onset between MJD 57161 and 57355
- detector 2: excess 0.392 mag, z 19.0, jitter ratio 16.1
- field control: target step -0.028 (W1 +0.018); neighbours N=182, median -0.006, robust sigma 0.011, max +0.134; z = -1.9
- centroid: jump at onset 0.029" +- 0.015 (1.9 sigma, PA 32); largest consecutive-visit jump 0.040"; rms 0.026"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.342, W2-W3 0.617 (W3 S/N 40.7), W3-W4 2.646 (W4 S/N 31.7), ext_flg 0, ph_qual AAAA: weak W3 excess (0.5 < W2-W3 < 1.0)
- Gaia: RUWE 1.02, ipd_frac_multi_peak 0, NSS none, Teff 5147 K, logg 4.13, H-alpha pEW -0.666 nm, varclass YSO(0.10); M_G 4.93, -1.83 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 5.2" PA309 G20.91 dG+8.40; 7.3" PA327 G18.20 dG+5.69
- SIMBAD (10"): 2MASS J08523126-4310586 [Y*?; *,NIR,Y*?] 0.19" refs=2
- ASAS-SN: 0 points, cameras n/a; change at onset (after-before, per-camera median) n/a mag; largest seasonal dimming n/a mag at MJD n/a
- dust: excess flux W1 -5.52 mJy, W2 -5.81 mJy, T = n/a K (16-84%: n/a-n/a) no W2 excess flux after onset
- checks missing: ASAS-SN (no source)

### uid1169402  [D2]  YOUNG
- position 82.51542 -1.92967; Gaia DR3 3217194357432201216; G 14.81, BP-RP 2.18, plx 2.79 mas; plot `plots/uid1169402.png`
- **young:** SIMBAD young-star types TT*,Y*?,Y*O (ZTF J053003.70-015546.7)
- flags: 1.97 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | optical dimming +0.137 mag after the infrared onset (debris transit signature) | largest seasonal optical dimming 0.11 mag (MJD 59281)
- NEOWISE: score refetch 1.38 (stored 1.38, reproduced True); dW2 0.128, dW1 0.005, 20 visits, 227 points; baseline W1 10.85, W1-W2 0.700; onset between MJD 59107 and 59262
- detector 2: excess 0.669 mag, z 15.6, jitter ratio 8.5
- field control: target step -0.028 (W1 -0.052); neighbours N=87, median -0.000, robust sigma 0.012, max +0.044; z = -2.4
- centroid: jump at onset 0.033" +- 0.022 (1.5 sigma, PA 225); largest consecutive-visit jump 0.086"; rms 0.036"; toward neighbour: 6.9" PA226 G20.5 (angle 1 deg); expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.702, W2-W3 3.273 (W3 S/N 58.3), W3-W4 2.548 (W4 S/N 34.3), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.06, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW 0.033 nm, varclass none; M_G 7.04, -1.97 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 6.9" PA226 G20.46 dG+5.65
- SIMBAD (10"): ZTF J053003.70-015546.7 [TT*; *,BY*,NIR,TT*,Y*?,Y*O] 0.03" refs=30
- ASAS-SN: 2263 points, cameras bD(g,159, d=+0.165); bG(g,202, d=+0.092); bH(g,194, d=+0.174); ba(V,50); bd(V,156); be(V,37); bf(V,34); bg(V,148); bh(V,151); bk(g,281, d=+0.136); bl(g,297, d=+0.129); bo(g,187, d=+0.175); bp(g,205, d=+0.137); bt(g,162, d=+0.059); change at onset (after-before, per-camera median) +0.137 mag; largest seasonal dimming 0.11 mag at MJD 59281
- dust: excess flux W1 1.01 mJy, W2 2.57 mJy, T = 620 K (16-84%: 587-655) 

### uid1643271  [D2]  YOUNG
- position 84.07077 -5.19522; Gaia DR3 3017371588112037248; G 12.60, BP-RP 1.80, plx 2.54 mas; plot `plots/uid1643271.png`
- **young:** SIMBAD young-star types Or*,Y*O (V* AZ Ori)
- flags: 3.29 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.72 mag (MJD 59629)
- NEOWISE: score refetch 0.05 (stored 0.05, reproduced True); dW2 0.008, dW1 0.020, 19 visits, 189 points; baseline W1 8.95, W1-W2 0.443; onset between MJD 58899 and 59109
- detector 2: excess 0.472 mag, z 13.8, jitter ratio 14.5
- field control: target step -0.058 (W1 -0.050); neighbours N=113, median -0.004, robust sigma 0.021, max +0.314; z = -2.6
- centroid: jump at onset 0.008" +- 0.017 (0.4 sigma, PA 222); largest consecutive-visit jump 0.062"; rms 0.026"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.481, W2-W3 2.224 (W3 S/N 43.7), W3-W4 2.087 (W4 S/N 27.4), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.15, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW -0.277 nm, varclass none; M_G 4.62, -3.29 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 7.9" PA322 G20.92 dG+8.32
- SIMBAD (10"): V* AZ Ori [Or*; *,Em*,Er*,IR,MIR,NIR,Opt,Or*,Rad,V*,X,Y*O,cC*] 0.05" refs=83; [H97b] 21534 [*; *] 7.94" refs=1
- ASAS-SN: 1454 points, cameras bA(g,155, d=+0.517); bE(g,217, d=-0.128); ba(V,173); be(V,195); bi(g,309, d=+0.568); bm(g,233, d=+0.006); bq(g,172, d=+0.372); change at onset (after-before, per-camera median) +0.372 mag; largest seasonal dimming 0.72 mag at MJD 59629
- dust: excess flux W1 0.85 mJy, W2 0.34 mJy, T = 8000 K (16-84%: 794-8000) ratio bluer than an 8000 K blackbody (not dust-like)

### uid712994  [D2]  YOUNG
- position 84.12785 -0.31222; Gaia DR3 3217809564250552704; G 12.33, BP-RP 1.75, plx 3.12 mas; plot `plots/uid712994.png`
- **young:** SIMBAD young-star types Or*,Y*?,Y*O (UCAC4 449-011147) | Gaia DR3 variability class YSO(0.73)
- flags: 2.96 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 0.30 (stored 0.30, reproduced True); dW2 0.019, dW1 0.027, 20 visits, 199 points; baseline W1 8.14, W1-W2 0.444; onset between MJD 57447 and 57647
- detector 2: excess 0.481 mag, z 15.2, jitter ratio 4.9
- field control: target step -0.047 (W1 -0.057); neighbours N=105, median -0.003, robust sigma 0.015, max +0.065; z = -3.0
- centroid: jump at onset 0.012" +- 0.023 (0.5 sigma, PA 89); largest consecutive-visit jump 0.042"; rms 0.031"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.435, W2-W3 2.230 (W3 S/N 52.3), W3-W4 1.631 (W4 S/N 28.6), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.04, ipd_frac_multi_peak 0, NSS none, Teff 5244 K, logg 3.72, H-alpha pEW -0.201 nm, varclass YSO(0.73); M_G 4.80, -2.96 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): UCAC4 449-011147 [Or*; *,MIR,NIR,Or*,Y*?,Y*O] 0.06" refs=11
- ASAS-SN: 0 points, cameras n/a; change at onset (after-before, per-camera median) n/a mag; largest seasonal dimming n/a mag at MJD n/a
- dust: excess flux W1 -3.68 mJy, W2 -1.52 mJy, T = n/a K (16-84%: n/a-n/a) no W2 excess flux after onset
- checks missing: ASAS-SN (no source)

### uid956198  [D2]  YOUNG
- position 84.49603 -1.09800; Gaia DR3 3217495859839297152; G 13.03, BP-RP 1.51, plx 2.93 mas; plot `plots/uid956198.png`
- **young:** SIMBAD young-star types Or*,Y*O (V* V993 Ori)
- flags: 1.77 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.60 mag (MJD 58885)
- NEOWISE: score refetch 0.18 (stored 0.18, reproduced True); dW2 0.042, dW1 0.127, 20 visits, 198 points; baseline W1 8.57, W1-W2 0.507; onset between MJD 57089 and 57283
- detector 2: excess 0.566 mag, z 24.2, jitter ratio 15.7
- field control: target step -0.091 (W1 -0.017); neighbours N=92, median -0.005, robust sigma 0.013, max +0.118; z = -6.4
- centroid: jump at onset 0.015" +- 0.013 (1.1 sigma, PA 327); largest consecutive-visit jump 0.041"; rms 0.023"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.466, W2-W3 1.336 (W3 S/N 63.3), W3-W4 2.503 (W4 S/N 41.5), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.36, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW -0.211 nm, varclass none; M_G 5.36, -1.77 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): V* V993 Ori [Or*; *,MIR,NIR,Or*,V*,Y*O] 0.04" refs=13
- ASAS-SN: 1456 points, cameras bC(g,155); bG(g,219); ba(V,51); bc(V,151, d=-0.308); be(V,38, d=+0.027); bg(V,153); bk(g,308); bo(g,220); bs(g,161); change at onset (after-before, per-camera median) -0.140 mag; largest seasonal dimming 0.60 mag at MJD 58885
- dust: excess flux W1 12.55 mJy, W2 5.32 mJy, T = 8000 K (16-84%: 8000-8000) ratio bluer than an 8000 K blackbody (not dust-like)

## Killed (32)

### uid1894418  [D1+D2]  KILLED
- position 86.12184 -1.37132; Gaia DR3 3218175740278049664; G 14.06, BP-RP 2.04, plx 2.43 mas; plot `plots/uid1894418.png`
- **KILL:** young star (SIMBAD young-star types Or*,Y*O (Haro 5-94)): disk variability expected, not an afterglow candidate
- **young:** SIMBAD young-star types Or*,Y*O (Haro 5-94)
- flags: 2.60 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | not plain dust: optical brightening -2.594 mag (per-camera -2.581,-2.607) together with the infrared rise | largest seasonal optical dimming 0.34 mag (MJD 57647)
- NEOWISE: score refetch 9.59 (stored 9.59, reproduced True); dW2 4.190, dW1 3.664, 21 visits, 257 points; baseline W1 8.31, W1-W2 0.833; onset between MJD 57813 and 58016
- field control: target step +4.149 (W1 +3.812); neighbours N=77, median -0.004, robust sigma 0.009, max +0.097; z = 466.8
- centroid: jump at onset 0.005" +- 0.055 (0.1 sigma, PA 112); largest consecutive-visit jump 1.061"; rms 0.307"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.680, W2-W3 2.603 (W3 S/N 76.3), W3-W4 2.234 (W4 S/N 58.1), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.15, ipd_frac_multi_peak 0, NSS none, Teff 6345 K, logg 3.93, H-alpha pEW -3.388 nm, varclass none; M_G 5.99, -2.60 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): Haro 5-94 [Or*; *,Em*,IR,NIR,Or*,V*,Y*O] 0.03" refs=30
- ASAS-SN: 1418 points, cameras bC(g,155); bG(g,222); bc(V,151, d=-2.581); be(V,38); bg(V,153, d=-2.607); bk(g,310); bo(g,224); bs(g,165); change at onset (after-before, per-camera median) -2.594 mag; largest seasonal dimming 0.34 mag at MJD 57647
- dust: excess flux W1 3782.66 mJy, W2 5736.22 mJy, T = 866 K (16-84%: 817-924) 

### uid1918148  [D1]  KILLED
- position 82.66003 -5.42880; Gaia DR3 3209455719717625216; G 14.77, BP-RP 2.04, plx 2.42 mas; plot `plots/uid1918148.png`
- **KILL:** young star (SIMBAD young-star types Or*,TT*,Y*?,Y*O (V* V538 Ori)): disk variability expected, not an afterglow candidate
- **young:** SIMBAD young-star types Or*,TT*,Y*?,Y*O (V* V538 Ori)
- flags: binary type in SIMBAD (SB*, V* V538 Ori) | 1.89 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | not plain dust: optical brightening -0.226 mag (per-camera -0.281,-0.172) together with the infrared rise | largest seasonal optical dimming 0.19 mag (MJD 56241)
- NEOWISE: score refetch 14.53 (stored 14.53, reproduced True); dW2 1.280, dW1 1.123, 20 visits, 190 points; baseline W1 10.70, W1-W2 0.428; onset between MJD 57086 and 57281
- field control: target step +1.135 (W1 +0.964); neighbours N=60, median -0.005, robust sigma 0.013, max +0.043; z = 87.9
- centroid: jump at onset 0.027" +- 0.017 (1.6 sigma, PA 100); largest consecutive-visit jump 0.126"; rms 0.036"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.420, W2-W3 2.070 (W3 S/N 45.9), W3-W4 2.043 (W4 S/N 23.4), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.33, ipd_frac_multi_peak 0, NSS none, Teff 3819 K, logg 4.09, H-alpha pEW -2.035 nm, varclass none; M_G 6.69, -1.89 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): V* V538 Ori [TT*; *,Em*,Er*,MIR,NIR,Or*,SB*,TT*,V*,Y*?,Y*O] 0.02" refs=20
- ASAS-SN: 1498 points, cameras bA(g,157); bE(g,218); ba(V,177, d=-0.281); be(V,193, d=-0.172); bi(g,340); bm(g,244); bq(g,169); change at onset (after-before, per-camera median) -0.226 mag; largest seasonal dimming 0.19 mag at MJD 56241
- dust: excess flux W1 17.03 mJy, W2 19.22 mJy, T = 1133 K (16-84%: 1117-1150) 

### uid1722578  [D2]  KILLED
- position 82.78675 +9.75762; Gaia DR3 3338170078487804288; G 15.45, BP-RP 2.07, plx 2.50 mas; plot `plots/uid1722578.png`
- **KILL:** cataclysmic variable / X-ray binary in SIMBAD (CV*, V* V650 Ori)
- **young:** SIMBAD young-star types Y*?,Y*O (V* V650 Ori)
- flags: in the Gaia DR3 QSO candidate table (low purity) | 1.24 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | not plain dust: optical brightening -0.791 mag (per-camera -0.688,-0.879,-0.791,-0.903,-0.769) together with the infrared rise | largest seasonal optical dimming 0.47 mag (MJD 58022)
- NEOWISE: score refetch 0.83 (stored 0.83, reproduced True); dW2 0.320, dW1 0.319, 19 visits, 151 points; baseline W1 10.61, W1-W2 0.650; onset between MJD 59109 and 59263
- detector 2: excess 0.633 mag, z 14.7, jitter ratio 36.2
- field control: target step +0.965 (W1 +0.929); neighbours N=78, median -0.001, robust sigma 0.013, max +0.033; z = 76.7
- centroid: jump at onset 0.032" +- 0.027 (1.2 sigma, PA 146); largest consecutive-visit jump 0.087"; rms 0.046"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.572, W2-W3 2.463 (W3 S/N 55.5), W3-W4 2.575 (W4 S/N 31.9), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.07, ipd_frac_multi_peak 0, NSS none, Teff 3542 K, logg 4.02, H-alpha pEW -1.104 nm, varclass none; M_G 7.45, -1.24 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): V* V650 Ori [CV*; *,CV*,MIR,NIR,Opt,V*,Y*?,Y*O] 0.03" refs=34
- ASAS-SN: 782 points, cameras bA(g,170, d=-0.688); bE(g,103, d=-0.879); ba(V,147); bi(g,177, d=-0.791); bm(g,91, d=-0.903); bq(g,94, d=-0.769); change at onset (after-before, per-camera median) -0.791 mag; largest seasonal dimming 0.47 mag at MJD 58022
- dust: excess flux W1 18.14 mJy, W2 18.18 mJy, T = 1302 K (16-84%: 1262-1346) 

### uid1991772  [D1]  KILLED
- position 85.62757 -8.54869; Gaia DR3 3012342181396446080; G 12.88, BP-RP 1.52, plx 2.39 mas; plot `plots/uid1991772.png`
- **KILL:** young star (SIMBAD young-star types Or*,Y*?,Y*O (2MASS J05423061-0832552); Gaia DR3 variability class YSO(0.58)): disk variability expected, not an afterglow candidate
- **young:** SIMBAD young-star types Or*,Y*?,Y*O (2MASS J05423061-0832552) | Gaia DR3 variability class YSO(0.58)
- flags: centroid jump 0.074" (4.0 sigma, PA 103) not toward a Gaia neighbour | 2.37 mag above the main sequence at its colour
- NEOWISE: score refetch 40.63 (stored 40.63, reproduced True); dW2 1.059, dW1 0.880, 20 visits, 201 points; baseline W1 10.11, W1-W2 0.012; onset between MJD 58170 and 58379
- field control: target step +0.948 (W1 +0.663); neighbours N=75, median -0.001, robust sigma 0.016, max +0.358; z = 58.2
- centroid: jump at onset 0.074" +- 0.018 (4.0 sigma, PA 103); largest consecutive-visit jump 0.057"; rms 0.030"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.368, W2-W3 0.730 (W3 S/N 55.6), W3-W4 3.840 (W4 S/N 52.4), ext_flg 0, ph_qual AAAA: weak W3 excess (0.5 < W2-W3 < 1.0)
- Gaia: RUWE 1.01, ipd_frac_multi_peak 0, NSS none, Teff 5311 K, logg 4.08, H-alpha pEW -0.045 nm, varclass YSO(0.58); M_G 4.78, -2.37 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): 2MASS J05423061-0832552 [Or*; *,MIR,NIR,Or*,X,Y*?,Y*O] 0.01" refs=28
- ASAS-SN: 1511 points, cameras bC(g,129); bG(g,254); ba(V,27); bc(V,119, d=+0.063); be(V,35); bg(V,214, d=+0.038); bk(g,346, d=+0.013); bo(g,259, d=+0.011); bs(g,128, d=+0.022); change at onset (after-before, per-camera median) +0.022 mag; largest seasonal dimming 0.06 mag at MJD 58431
- dust: excess flux W1 23.54 mJy, W2 22.16 mJy, T = 1416 K (16-84%: 1384-1449) 

### uid1987032  [D2]  KILLED
- position 62.70490 +38.07936; Gaia DR3 226027159377149440; G 14.20, BP-RP 2.11, plx 2.39 mas; plot `plots/uid1987032.png`
- **KILL:** eclipsing binary in SIMBAD (EB*, ZTF J041049.17+380445.7)
- **young:** SIMBAD young-star types Y*?,Y*O (ZTF J041049.17+380445.7)
- flags: 2.70 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | optical dimming +0.135 mag after the infrared onset (debris transit signature) | largest seasonal optical dimming 0.12 mag (MJD 57780)
- NEOWISE: score refetch 3.16 (stored 3.16, reproduced True); dW2 0.548, dW1 0.470, 21 visits, 193 points; baseline W1 9.25, W1-W2 0.801; onset between MJD 57265 and 57430
- detector 2: excess 0.778 mag, z 18.1, jitter ratio 15.5
- field control: target step +0.432 (W1 +0.365); neighbours N=87, median +0.001, robust sigma 0.012, max +0.071; z = 36.4
- centroid: jump at onset 0.029" +- 0.025 (1.2 sigma, PA 213); largest consecutive-visit jump 0.089"; rms 0.040"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.752, W2-W3 2.365 (W3 S/N 73.9), W3-W4 1.810 (W4 S/N 43.4), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.12, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW -1.534 nm, varclass none; M_G 6.10, -2.70 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): ZTF J041049.17+380445.7 [EB*; *,EB*,Em*,FIR,NIR,Y*?,Y*O] 0.19" refs=11
- ASAS-SN: 531 points, cameras bC(g,266); bc(V,174, d=+0.135); bs(g,91); change at onset (after-before, per-camera median) +0.135 mag; largest seasonal dimming 0.12 mag at MJD 57780
- dust: excess flux W1 32.46 mJy, W2 45.57 mJy, T = 922 K (16-84%: 905-939) 

### uid1090282  [D1]  KILLED
- position 281.80894 +19.66649; Gaia DR3 4518641122550725504; G 13.24, BP-RP 1.17, plx 2.84 mas; plot `plots/uid1090282.png`
- **KILL:** centroid jump 0.100" (4.4 sigma) at the onset toward a neighbour: 4.0" PA224 G20.3 (angle 23 deg); 8.3" PA247 G16.7 (angle 1 deg); 9.2" PA217 G21.1 (angle 29 deg) | blend: Gaia neighbour within 6" only 1.85 mag fainter in G (4.0" PA224 G20.31 dG+7.07; 4.4" PA64 G15.09 dG+1.85; 6.3" PA75 G19.33 dG+6.09; 7.9" PA187 G18.91 dG+5.67; 8.3" PA247 G16.74 dG+3.50; 9.2" PA217 G21.15 dG+7.91; 9.8" PA175 G21.06 dG+7.82)
- flags: not plain dust: optical brightening -0.065 mag (per-camera -0.055,-0.072,-0.065,-0.038,-0.066) together with the infrared rise
- NEOWISE: score refetch 12.83 (stored 12.83, reproduced True); dW2 0.245, dW1 0.132, 19 visits, 187 points; baseline W1 10.93, W1-W2 -0.019; onset between MJD 59310 and 59471
- field control: target step +0.256 (W1 +0.135); neighbours N=189, median -0.000, robust sigma 0.011, max +0.206; z = 23.1
- centroid: jump at onset 0.100" +- 0.022 (4.4 sigma, PA 246); largest consecutive-visit jump 0.136"; rms 0.054"; toward neighbour: 4.0" PA224 G20.3 (angle 23 deg); 8.3" PA247 G16.7 (angle 1 deg); 9.2" PA217 G21.1 (angle 29 deg); expected shift if a neighbour were the source: 4.0" G20.3: 0.83"; 4.4" G15.1: 0.93"; 6.3" G19.3: 1.33"; 7.9" G18.9: 1.66"; 8.3" G16.7: 1.75"; 9.2" G21.1: 1.94"; 9.8" G21.1: 2.05"
- AllWISE 2010: W1-W2 -0.002, W2-W3 0.090 (W3 S/N 8.3), W3-W4 2.526 (W4 S/N 2.6), ext_flg 0, ph_qual AABC: photosphere-like (W2-W3 < 0.5)
- Gaia: RUWE 1.33, ipd_frac_multi_peak 0, NSS none, Teff 5862 K, logg 4.51, H-alpha pEW 0.061 nm, varclass none; M_G 5.51, -0.64 mag vs sequence (on the sequence); neighbours within 10": 4.0" PA224 G20.31 dG+7.07; 4.4" PA64 G15.09 dG+1.85; 6.3" PA75 G19.33 dG+6.09; 7.9" PA187 G18.91 dG+5.67; 8.3" PA247 G16.74 dG+3.50; 9.2" PA217 G21.15 dG+7.91; 9.8" PA175 G21.06 dG+7.82
- SIMBAD (10"): no object
- ASAS-SN: 1035 points, cameras bA(g,236, d=-0.055); bE(g,112, d=-0.072); ba(V,218); bi(g,158, d=-0.065); bm(g,110, d=-0.038); bq(g,201, d=-0.066); change at onset (after-before, per-camera median) -0.065 mag; largest seasonal dimming 0.05 mag at MJD 58582
- dust: excess flux W1 1.90 mJy, W2 2.28 mJy, T = 1061 K (16-84%: 1005-1122) 

### uid1871307  [D2]  KILLED
- position 86.36275 -0.66485; Gaia DR3 3218992574339113600; G 13.33, BP-RP 1.68, plx 2.44 mas; plot `plots/uid1871307.png`
- **KILL:** blend: Gaia neighbour within 6" only 1.39 mag fainter in G (3.4" PA21 G14.72 dG+1.39)
- **young:** SIMBAD young-star types Y*?,Y*O (Kiso A-0904 168; 2MASS J05452713-0039502) | Gaia DR3 variability class YSO(0.47)
- flags: 2.32 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 0.50 (stored 0.50, reproduced True); dW2 0.043, dW1 0.119, 21 visits, 195 points; baseline W1 8.83, W1-W2 0.508; onset between MJD 57814 and 58016
- detector 2: excess 0.553 mag, z 19.3, jitter ratio 7.0
- field control: target step +0.221 (W1 +0.271); neighbours N=62, median -0.006, robust sigma 0.011, max +0.124; z = 19.7
- centroid: jump at onset 0.102" +- 0.106 (1.0 sigma, PA 355); largest consecutive-visit jump 0.192"; rms 0.147"; toward neighbour: 3.4" PA21 G14.7 (angle 26 deg); expected shift if a neighbour were the source: 3.4" G14.7: 0.63"
- AllWISE 2010: W1-W2 0.501, W2-W3 1.663 (W3 S/N 41.7), W3-W4 1.630 (W4 S/N 18.9), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.05, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW -0.494 nm, varclass YSO(0.47); M_G 5.27, -2.32 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 3.4" PA21 G14.72 dG+1.39
- SIMBAD (10"): Kiso A-0904 168 [Y*O; *,Em*,NIR,Y*O] 0.02" refs=5; 2MASS J05452713-0039502 [Y*O; *,NIR,Y*?,Y*O] 3.46" refs=12
- ASAS-SN: 0 points, cameras ; change at onset (after-before, per-camera median) n/a mag; largest seasonal dimming n/a mag at MJD n/a
- dust: excess flux W1 12.58 mJy, W2 10.16 mJy, T = 1827 K (16-84%: 1602-2137) 
- checks missing: ASAS-SN change at onset (no camera spans the onset)

### uid1148744  [D2]  KILLED
- position 126.62254 -34.58555; Gaia DR3 5543488248577017344; G 15.38, BP-RP 1.48, plx 2.80 mas; plot `plots/uid1148744.png`
- **KILL:** blend: Gaia neighbour within 6" only 1.46 mag fainter in G (3.8" PA197 G20.28 dG+4.90; 5.9" PA46 G16.84 dG+1.46; 7.6" PA254 G16.25 dG+0.87; 7.9" PA343 G19.80 dG+4.42; 9.1" PA42 G21.16 dG+5.78; 9.6" PA241 G19.02 dG+3.63)
- flags: AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.47 mag (MJD 60639)
- NEOWISE: score refetch 0.54 (stored 0.54, reproduced True); dW2 0.088, dW1 0.046, 17 visits, 143 points; baseline W1 10.45, W1-W2 0.632; onset between MJD 57867 and 58073
- detector 2: excess 0.693 mag, z 30.8, jitter ratio 11.0
- field control: target step +0.225 (W1 +0.252); neighbours N=170, median -0.005, robust sigma 0.013, max +0.048; z = 17.3
- centroid: jump at onset 0.032" +- 0.039 (0.8 sigma, PA 50); largest consecutive-visit jump 0.105"; rms 0.052"; toward neighbour: 5.9" PA46 G16.8 (angle 4 deg); 9.1" PA42 G21.2 (angle 8 deg); expected shift if a neighbour were the source: 3.8" G20.3: 0.71"; 5.9" G16.8: 1.10"; 7.6" G16.3: 1.43"; 7.9" G19.8: 1.49"; 9.1" G21.2: 1.72"; 9.6" G19.0: 1.80"
- AllWISE 2010: W1-W2 0.642, W2-W3 2.107 (W3 S/N 63.6), W3-W4 1.970 (W4 S/N 27.0), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.21, ipd_frac_multi_peak 0, NSS none, Teff 5870 K, logg 4.73, H-alpha pEW -3.254 nm, varclass none; M_G 7.62, +0.56 mag vs sequence (on the sequence); neighbours within 10": 3.8" PA197 G20.28 dG+4.90; 5.9" PA46 G16.84 dG+1.46; 7.6" PA254 G16.25 dG+0.87; 7.9" PA343 G19.80 dG+4.42; 9.1" PA42 G21.16 dG+5.78; 9.6" PA241 G19.02 dG+3.63
- SIMBAD (10"): 2MASS J08262942-3435081 [Em*; *,Em*,NIR] 0.20" refs=4
- ASAS-SN: 1314 points, cameras bG(g,442); bg(V,239, d=-0.014); bk(g,448); bo(g,185); change at onset (after-before, per-camera median) -0.014 mag; largest seasonal dimming 0.47 mag at MJD 60639
- dust: excess flux W1 2.94 mJy, W2 3.55 mJy, T = 1058 K (16-84%: 954-1179) 

### uid1613134  [D2]  KILLED
- position 82.65082 +12.61456; Gaia DR3 3341051967182318208; G 14.30, BP-RP 1.70, plx 2.55 mas; plot `plots/uid1613134.png`
- **KILL:** blend: Gaia neighbour within 6" only 1.69 mag fainter in G (5.0" PA34 G15.98 dG+1.69)
- **young:** SIMBAD young-star types Or*,Y*O (V* V447 Ori)
- flags: binary type in SIMBAD (**, V* V447 Ori) | 1.31 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.39 mag (MJD 60044)
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 21 visits, 184 points; baseline W1 9.38, W1-W2 0.447; onset between MJD 58899 and 59108
- detector 2: excess 0.490 mag, z 16.4, jitter ratio 7.2
- field control: target step +0.247 (W1 +0.212); neighbours N=89, median +0.005, robust sigma 0.015, max +0.227; z = 16.3
- centroid: jump at onset 0.103" +- 0.097 (1.1 sigma, PA 324); largest consecutive-visit jump 0.502"; rms 0.167"; toward neighbour: none; expected shift if a neighbour were the source: 5.0" G16.0: 1.02"
- AllWISE 2010: W1-W2 0.517, W2-W3 2.339 (W3 S/N 46.7), W3-W4 2.066 (W4 S/N 19.4), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.11, ipd_frac_multi_peak 0, NSS none, Teff 3854 K, logg 4.04, H-alpha pEW -4.051 nm, varclass none; M_G 6.33, -1.31 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 5.0" PA34 G15.98 dG+1.69
- SIMBAD (10"): V* V447 Ori [Or*; *,**,Em*,MIR,NIR,Or*,V*,Y*O] 0.05" refs=29; V* V447 Ori B [Y*O; *,**,Em*,MIR,NIR,V*,Y*?,Y*O] 5.06" refs=19
- ASAS-SN: 853 points, cameras bD(g,197, d=-0.119); bH(g,114, d=+0.109); bd(V,170); bl(g,179, d=+0.087); bp(g,92, d=-0.022); bt(g,101, d=-0.027); change at onset (after-before, per-camera median) -0.022 mag; largest seasonal dimming 0.39 mag at MJD 60044
- dust: excess flux W1 6.57 mJy, W2 5.94 mJy, T = 1502 K (16-84%: 1361-1676) 

### uid1273358  [D2]  KILLED
- position 83.02660 -1.18337; Gaia DR3 3217634157789741952; G 14.45, BP-RP 1.84, plx 2.73 mas; plot `plots/uid1273358.png`
- **KILL:** blend: Gaia neighbour within 6" only 0.13 mag fainter in G (2.4" PA110 G14.59 dG+0.13; 8.0" PA10 G20.34 dG+5.89; 8.6" PA140 G17.65 dG+3.20)
- **young:** SIMBAD young-star types Or*,TT*,Y*O (Haro 5-64; Gaia DR3 3217634162083288320)
- flags: binary type in SIMBAD (**,SB*, NAME Haro 5-64A) | 1.40 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 0.98 (stored 0.97, reproduced True); dW2 0.098, dW1 0.116, 20 visits, 224 points; baseline W1 9.75, W1-W2 0.498; onset between MJD 58899 and 59108
- detector 2: excess 0.521 mag, z 14.2, jitter ratio 8.5
- field control: target step +0.175 (W1 +0.138); neighbours N=76, median -0.001, robust sigma 0.012, max +0.025; z = 14.4
- centroid: jump at onset 0.018" +- 0.020 (0.9 sigma, PA 308); largest consecutive-visit jump 0.050"; rms 0.027"; toward neighbour: none; expected shift if a neighbour were the source: 2.4" G14.6: 0.36"; 8.0" G20.3: 1.19"; 8.6" G17.7: 1.27"
- AllWISE 2010: W1-W2 0.495, W2-W3 1.644 (W3 S/N 58.1), W3-W4 1.989 (W4 S/N 27.8), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.23, ipd_frac_multi_peak 0, NSS none, Teff 6477 K, logg 4.26, H-alpha pEW -3.212 nm, varclass none; M_G 6.64, -1.40 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 2.4" PA110 G14.59 dG+0.13; 8.0" PA10 G20.34 dG+5.89; 8.6" PA140 G17.65 dG+3.20
- SIMBAD (10"): NAME Haro 5-64A [*; *,**] 0.03" refs=1; Haro 5-64 [TT*; *,**,Em*,MIR,NIR,SB*,TT*,V*,Y*O] 0.03" refs=40; NAME Haro 5-64B [*; *,**] 2.27" refs=0; Gaia DR3 3217634162083288320 [Or*; *,Or*] 2.27" refs=2
- ASAS-SN: 1388 points, cameras bC(g,141, d=-0.047); bG(g,218, d=-0.056); ba(V,51); bc(V,137); be(V,38); bg(V,153); bk(g,296, d=+0.042); bo(g,205, d=-0.075); bs(g,149, d=+0.078); change at onset (after-before, per-camera median) -0.047 mag; largest seasonal dimming 0.08 mag at MJD 56897
- dust: excess flux W1 4.44 mJy, W2 3.79 mJy, T = 1653 K (16-84%: 1339-2171) 

### uid1760310  [D2]  KILLED
- position 87.65415 +4.79638; Gaia DR3 3320081948274119936; G 13.50, BP-RP 1.79, plx 2.49 mas; plot `plots/uid1760310.png`
- **KILL:** blend: Gaia neighbour within 6" only 1.42 mag fainter in G (1.2" PA200 G14.91 dG+1.42)
- **young:** SIMBAD young-star types Y*O (Kiso A-0832   3)
- flags: binary type in SIMBAD (**, Gaia DR3 3320081948274119936) | in the Gaia DR3 QSO candidate table (low purity) | Gaia ipd_frac_multi_peak 22% (resolved double?) | 2.39 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 1.28 (stored 1.28, reproduced True); dW2 0.159, dW1 0.146, 21 visits, 190 points; baseline W1 9.11, W1-W2 0.609; onset between MJD 57092 and 57286
- detector 2: excess 0.641 mag, z 19.3, jitter ratio 7.0
- field control: target step +0.134 (W1 +0.130); neighbours N=91, median -0.004, robust sigma 0.011, max +0.043; z = 12.4
- centroid: jump at onset 0.037" +- 0.022 (1.7 sigma, PA 2); largest consecutive-visit jump 0.068"; rms 0.035"; toward neighbour: none; expected shift if a neighbour were the source: 1.2" G14.9: 0.13"
- AllWISE 2010: W1-W2 0.647, W2-W3 2.639 (W3 S/N 73.0), W3-W4 1.605 (W4 S/N 38.6), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.22, ipd_frac_multi_peak 22, NSS none, Teff 6129 K, logg 4.06, H-alpha pEW -2.670 nm, varclass none; M_G 5.47, -2.39 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 1.2" PA200 G14.91 dG+1.42
- SIMBAD (10"): Gaia DR3 3320081948274119936 [*; *] 0.03" refs=0; Kiso A-0832   3 [Y*O; *,**,Em*,MIR,NIR,Y*O,ev] 0.12" refs=5; Gaia DR3 3320081948273117440 [*; *] 1.14" refs=0
- ASAS-SN: 0 points, cameras n/a; change at onset (after-before, per-camera median) n/a mag; largest seasonal dimming n/a mag at MJD n/a
- dust: excess flux W1 12.16 mJy, W2 11.81 mJy, T = 1357 K (16-84%: 1259-1474) 
- checks missing: ASAS-SN (no source)

### uid1790675  [D2]  KILLED
- position 83.66661 -5.50122; Gaia DR3 3017268921203931776; G 15.53, BP-RP 1.83, plx 2.47 mas; plot `plots/uid1790675.png`
- **KILL:** blend: Gaia neighbour within 6" only -0.53 mag fainter in G (3.0" PA219 G15.00 dG-0.53) | galaxy/QSO within 6" in SIMBAD: V* IW Ori B [G] 0.0"; V* IW Ori A [G] 3.0"
- **young:** SIMBAD young-star types Or*,TT*,TT?,Y*O (V* IW Ori B; V* IW Ori; V* IW Ori A)
- flags: binary type in SIMBAD (**, V* IW Ori B) | AllWISE ext_flg = 1 (extended or 2MASS XSC association) | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 20 visits, 182 points; baseline W1 9.21, W1-W2 0.473; onset between MJD 59995 and 60204
- detector 2: excess 0.498 mag, z 13.9, jitter ratio 11.1
- field control: target step +0.292 (W1 +0.281); neighbours N=119, median -0.001, robust sigma 0.026, max +0.317; z = 11.3
- centroid: jump at onset 0.106" +- 0.091 (1.2 sigma, PA 9); largest consecutive-visit jump 0.285"; rms 0.155"; toward neighbour: none; expected shift if a neighbour were the source: 3.0" G15.0: 0.70"
- AllWISE 2010: W1-W2 0.485, W2-W3 2.049 (W3 S/N 30.2), W3-W4 3.358 (W4 S/N 0.9), ext_flg 1, ph_qual AAAU: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.13, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW -3.803 nm, varclass none; M_G 7.50, -0.49 mag vs sequence (on the sequence); neighbours within 10": 3.0" PA219 G15.00 dG-0.53
- SIMBAD (10"): V* IW Ori B [Or*; *,**,Em*,G,Ir*,NIR,Or*,TT?,V*,Y*O] 0.04" refs=17; V* IW Ori [TT*; *,**,MIR,Or*,TT*,V*,V*?,X,Y*O] 1.67" refs=27; V* IW Ori A [Or*; *,Em*,G,NIR,Or*,TT?,V*,Y*O] 2.96" refs=27
- ASAS-SN: 1493 points, cameras bA(g,153, d=+0.009); bE(g,219, d=+0.010); ba(V,179); be(V,195); bi(g,342, d=+0.029); bm(g,244, d=+0.011); bq(g,161, d=+0.039); change at onset (after-before, per-camera median) +0.011 mag; largest seasonal dimming 0.04 mag at MJD 57083
- dust: excess flux W1 4.55 mJy, W2 3.91 mJy, T = 1634 K (16-84%: 1339-2107) 

### uid1639002  [D2]  KILLED
- position 128.80091 -50.51295; Gaia DR3 5322740776530753280; G 15.06, BP-RP 1.73, plx 2.54 mas; plot `plots/uid1639002.png`
- **KILL:** blend: Gaia neighbour within 6" only 2.11 mag fainter in G (2.7" PA288 G17.17 dG+2.11; 3.6" PA233 G20.97 dG+5.90; 9.0" PA282 G20.06 dG+5.00)
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 0.69 (stored 0.69, reproduced True); dW2 0.115, dW1 0.055, 18 visits, 234 points; baseline W1 11.35, W1-W2 0.407; onset between MJD 57164 and 57358
- detector 2: excess 0.446 mag, z 14.2, jitter ratio 12.2
- field control: target step +0.101 (W1 +0.060); neighbours N=190, median -0.001, robust sigma 0.009, max +0.050; z = 11.0
- centroid: jump at onset 0.022" +- 0.021 (1.0 sigma, PA 23); largest consecutive-visit jump 0.105"; rms 0.060"; toward neighbour: none; expected shift if a neighbour were the source: 2.7" G17.2: 0.24"; 3.6" G21.0: 0.32"; 9.0" G20.1: 0.80"
- AllWISE 2010: W1-W2 0.379, W2-W3 2.566 (W3 S/N 44.8), W3-W4 0.998 (W4 S/N 7.7), ext_flg 1, ph_qual AAAB: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 0.98, ipd_frac_multi_peak 0, NSS none, Teff 4486 K, logg 4.38, H-alpha pEW -0.247 nm, varclass RS(0.34); M_G 7.09, -0.63 mag vs sequence (on the sequence); neighbours within 10": 2.7" PA288 G17.17 dG+2.11; 3.6" PA233 G20.97 dG+5.90; 9.0" PA282 G20.06 dG+5.00
- SIMBAD (10"): Gaia DR2 5322740776530753280 [*; *] 0.23" refs=3; Gaia DR3 5322740776530752000 [*; *] 2.53" refs=2
- ASAS-SN: 2388 points, cameras bG(g,416); bH(g,334); bg(V,174); bh(V,188); bk(g,397); bl(g,443); bo(g,214); bp(g,222); change at onset (after-before, per-camera median) n/a mag; largest seasonal dimming 0.10 mag at MJD 59726
- dust: excess flux W1 0.58 mJy, W2 1.24 mJy, T = 688 K (16-84%: 639-744) 
- checks missing: ASAS-SN change at onset (no camera spans the onset)

### uid1556586  [D2]  KILLED
- position 84.02773 -6.24055; Gaia DR3 3017165670190318976; G 13.77, BP-RP 1.75, plx 2.58 mas; plot `plots/uid1556586.png`
- **KILL:** blend: Gaia neighbour within 6" only 2.49 mag fainter in G (3.6" PA27 G16.27 dG+2.49) | galaxy/QSO within 6" in SIMBAD: ESO-HA 1435 [G] 3.6"
- **young:** SIMBAD young-star types Or*,TT*,Y*O (V* AX Ori) | Gaia DR3 variability class YSO(0.22)
- flags: binary type in SIMBAD (**, V* AX Ori) | AllWISE ext_flg = 1 (extended or 2MASS XSC association) | 1.93 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.14 mag (MJD 59998)
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 20 visits, 179 points; baseline W1 8.83, W1-W2 0.626; onset between MJD 60204 and 60362
- detector 2: excess 0.663 mag, z 20.8, jitter ratio 11.5
- field control: target step +0.281 (W1 +0.270); neighbours N=114, median -0.004, robust sigma 0.027, max +0.262; z = 10.7
- centroid: jump at onset 0.178" +- 0.084 (2.1 sigma, PA 214); largest consecutive-visit jump 0.105"; rms 0.101"; toward neighbour: none; expected shift if a neighbour were the source: 3.6" G16.3: 0.83"
- AllWISE 2010: W1-W2 0.637, W2-W3 1.636 (W3 S/N 60.5), W3-W4 1.870 (W4 S/N 33.7), ext_flg 1, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.32, ipd_frac_multi_peak 0, NSS none, Teff 5806 K, logg 4.16, H-alpha pEW -1.229 nm, varclass YSO(0.22); M_G 5.83, -1.93 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 3.6" PA27 G16.27 dG+2.49
- SIMBAD (10"): V* AX Ori [TT*; *,**,Em*,MIR,NIR,Opt,Or*,TT*,V*,V*?,X,Y*O] 0.01" refs=48; ESO-HA 1435 [Em*; *,**,Em*,G,NIR,Opt] 3.64" refs=1
- ASAS-SN: 1300 points, cameras bA(g,151, d=-0.065); bE(g,216, d=+0.066); ba(V,163); be(V,195); bi(g,228, d=+0.023); bm(g,193, d=-0.086); bq(g,154, d=+0.132); change at onset (after-before, per-camera median) +0.023 mag; largest seasonal dimming 0.14 mag at MJD 59998
- dust: excess flux W1 27.34 mJy, W2 28.29 mJy, T = 1252 K (16-84%: 1209-1296) 

### uid438254  [D2]  KILLED
- position 52.35804 +31.44442; Gaia DR3 121412854238659712; G 15.05, BP-RP 2.14, plx 3.38 mas; plot `plots/uid438254.png`
- **KILL:** blend: Gaia neighbour within 6" only 2.67 mag fainter in G (4.4" PA40 G17.73 dG+2.67)
- **young:** SIMBAD young-star types Or*,Y*?,Y*O (ATO J052.3580+31.4444; [HL2013] 052.35902+31.44538)
- flags: 1.19 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | optical dimming +0.086 mag after the infrared onset (debris transit signature) | largest seasonal optical dimming 0.15 mag (MJD 59967)
- NEOWISE: score refetch 1.72 (stored 1.72, reproduced True); dW2 0.140, dW1 0.052, 21 visits, 223 points; baseline W1 8.49, W1-W2 0.701; onset between MJD 58510 and 58715
- detector 2: excess 0.674 mag, z 15.7, jitter ratio 7.0
- field control: target step +0.216 (W1 +0.261); neighbours N=87, median +0.003, robust sigma 0.020, max +0.181; z = 10.6
- centroid: jump at onset 0.045" +- 0.024 (1.9 sigma, PA 258); largest consecutive-visit jump 0.099"; rms 0.045"; toward neighbour: none; expected shift if a neighbour were the source: 4.4" G17.7: 0.80"
- AllWISE 2010: W1-W2 0.743, W2-W3 2.312 (W3 S/N 73.2), W3-W4 1.398 (W4 S/N 47.4), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.05, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW 0.025 nm, varclass none; M_G 7.70, -1.19 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 4.4" PA40 G17.73 dG+2.67
- SIMBAD (10"): ATO J052.3580+31.4444 [Or*; *,IR,MIR,NIR,Opt,Or*,V*,X,Y*?,Y*O] 0.19" refs=49; [HL2013] 052.35902+31.44538 [Y*?; *,IR,Y*?] 4.46" refs=8
- ASAS-SN: 2220 points, cameras bC(g,253, d=+0.042); bD(g,288, d=+0.070); bG(g,70, d=+0.295); bH(g,86, d=+0.150); ba(V,40); bc(V,272); bd(V,251); bg(V,22); bh(V,33); bk(g,130, d=+0.065); bl(g,163, d=+0.126); bo(g,126, d=+0.150); bp(g,126, d=-0.010); bs(g,172, d=+0.103); bt(g,188, d=+0.065); change at onset (after-before, per-camera median) +0.086 mag; largest seasonal dimming 0.15 mag at MJD 59967
- dust: excess flux W1 22.87 mJy, W2 21.36 mJy, T = 1433 K (16-84%: 1326-1562) 

### uid1743225  [D2]  KILLED
- position 157.84276 +74.69845; Gaia DR3 1126525224017094400; G 15.33, BP-RP 1.57, plx 2.50 mas; plot `plots/uid1743225.png`
- **KILL:** blend: Gaia neighbour within 6" only 1.98 mag fainter in G (4.1" PA347 G17.31 dG+1.98) | galaxy/QSO within 6" in SIMBAD: 6C 102716+745713 [AGN,BLL,Bla,G,QSO,Sy1] 4.1"
- flags: optical dimming +0.070 mag after the infrared onset (debris transit signature)
- NEOWISE: score refetch 1.27 (stored 1.27, reproduced True); dW2 0.184, dW1 0.093, 20 visits, 379 points; baseline W1 11.78, W1-W2 0.471; onset between MJD 59143 and 59300
- detector 2: excess 0.526 mag, z 20.9, jitter ratio 8.0
- field control: target step +0.062 (W1 +0.049); neighbours N=31, median +0.001, robust sigma 0.006, max +0.028; z = 10.4
- centroid: jump at onset 0.142" +- 0.116 (1.2 sigma, PA 17); largest consecutive-visit jump 0.165"; rms 0.132"; toward neighbour: 4.1" PA347 G17.3 (angle 31 deg); expected shift if a neighbour were the source: 4.1" G17.3: 0.22"
- AllWISE 2010: W1-W2 -0.048, W2-W3 0.801 (W3 S/N 0.7), W3-W4 3.322 (W4 S/N -0.6), ext_flg 0, ph_qual AAUU: W3 S/N < 5: no W2-W3 class
- Gaia: RUWE 0.96, ipd_frac_multi_peak 0, NSS none, Teff 4453 K, logg 4.61, H-alpha pEW -0.152 nm, varclass none; M_G 7.32, +0.02 mag vs sequence (on the sequence); neighbours within 10": 4.1" PA347 G17.31 dG+1.98
- SIMBAD (10"): 6C 102716+745713 [BLL; *,AGN,BL?,BLL,Bla,Bz?,G,MIR,QSO,Rad,Sy1,X,gam] 4.05" refs=97
- ASAS-SN: 664 points, cameras bA(g,241, d=+0.064); ba(V,218); bq(g,205, d=+0.076); change at onset (after-before, per-camera median) +0.070 mag; largest seasonal dimming 0.09 mag at MJD 59636
- dust: excess flux W1 0.81 mJy, W2 1.09 mJy, T = 957 K (16-84%: 896-1025) 

### uid1713962  [D2]  KILLED
- position 266.16122 -30.58143; Gaia DR3 4056679972099704320; G 14.03, BP-RP 1.35, plx 2.51 mas; plot `plots/uid1713962.png`
- **KILL:** centroid jump 0.394" (5.2 sigma) at the onset toward a neighbour: 4.4" PA147 G19.6 (angle 3 deg)
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association)
- NEOWISE: score refetch 0.86 (stored 0.86, reproduced True); dW2 0.256, dW1 0.216, 7 visits, 60 points; baseline W1 8.61, W1-W2 0.648; onset between MJD 58560 and 59291
- detector 2: excess 0.711 mag, z 35.3, jitter ratio 21.4
- field control: target step +0.274 (W1 +0.274); neighbours N=141, median -0.007, robust sigma 0.029, max +0.068; z = 9.7
- centroid: jump at onset 0.394" +- 0.076 (5.2 sigma, PA 144); largest consecutive-visit jump 0.267"; rms 0.131"; toward neighbour: 4.4" PA147 G19.6 (angle 3 deg); expected shift if a neighbour were the source: 4.4" G19.6: 0.98"
- AllWISE 2010: W1-W2 0.692, W2-W3 0.764 (W3 S/N 15.8), W3-W4 0.123 (W4 S/N 2.2), ext_flg 1, ph_qual AAAC: weak W3 excess (0.5 < W2-W3 < 1.0)
- Gaia: RUWE 0.98, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW 0.065 nm, varclass none; M_G 6.03, -0.69 mag vs sequence (on the sequence); neighbours within 10": 4.4" PA147 G19.64 dG+5.61
- SIMBAD (10"): no object
- ASAS-SN: 1003 points, cameras bF(g,250, d=+0.006); bf(V,196); bj(g,243, d=-0.019); bn(g,162, d=-0.009); br(g,152, d=+0.006); change at onset (after-before, per-camera median) -0.002 mag; largest seasonal dimming 0.02 mag at MJD 58012
- dust: excess flux W1 33.76 mJy, W2 35.91 mJy, T = 1211 K (16-84%: 1126-1314) 

### uid1197479  [D2]  KILLED
- position 81.41972 -5.88013; Gaia DR3 3209147822102195072; G 13.79, BP-RP 1.61, plx 2.77 mas; plot `plots/uid1197479.png`
- **KILL:** blend: Gaia neighbour within 6" only 2.44 mag fainter in G (3.1" PA192 G16.22 dG+2.44; 8.3" PA0 G19.06 dG+5.28) | galaxy/QSO within 6" in SIMBAD: ESO-HA  593 [G] 3.1"
- **young:** SIMBAD young-star types TT*,Y*?,Y*O (Kiso A-0975  87)
- flags: binary type in SIMBAD (**, Kiso A-0975  87) | AllWISE ext_flg = 1 (extended or 2MASS XSC association) | 1.38 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 0.63 (stored 0.63, reproduced True); dW2 0.076, dW1 0.057, 16 visits, 163 points; baseline W1 9.80, W1-W2 0.458; onset between MJD 57808 and 58009
- detector 2: excess 0.510 mag, z 19.5, jitter ratio 11.2
- field control: target step +0.106 (W1 +0.095); neighbours N=43, median -0.002, robust sigma 0.012, max +0.032; z = 9.1
- centroid: jump at onset 0.082" +- 0.151 (0.5 sigma, PA 206); largest consecutive-visit jump 0.334"; rms 0.152"; toward neighbour: 3.1" PA192 G16.2 (angle 14 deg); expected shift if a neighbour were the source: 3.1" G16.2: 0.29"; 8.3" G19.1: 0.78"
- AllWISE 2010: W1-W2 0.442, W2-W3 2.047 (W3 S/N 57.3), W3-W4 2.054 (W4 S/N 29.0), ext_flg 1, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.36, ipd_frac_multi_peak 2, NSS none, Teff 4880 K, logg 4.22, H-alpha pEW -0.267 nm, varclass none; M_G 6.00, -1.38 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 3.1" PA192 G16.22 dG+2.44; 8.3" PA0 G19.06 dG+5.28
- SIMBAD (10"): Kiso A-0975  87 [TT*; *,**,Em*,NIR,TT*,Y*?,Y*O] 0.04" refs=7; ESO-HA  593 [Em*; *,**,Em*,G] 3.07" refs=2
- ASAS-SN: 1477 points, cameras bA(g,158); bE(g,219); ba(V,149, d=-0.028); be(V,195, d=+0.039); bi(g,338); bm(g,249); bq(g,169); change at onset (after-before, per-camera median) +0.006 mag; largest seasonal dimming 0.04 mag at MJD 58001
- dust: excess flux W1 2.38 mJy, W2 2.37 mJy, T = 1311 K (16-84%: 1095-1629) 

### uid1609975  [D2]  KILLED
- position 83.72523 -6.39741; Gaia DR3 3017134471547930624; G 14.12, BP-RP 1.59, plx 2.56 mas; plot `plots/uid1609975.png`
- **KILL:** blend: Gaia neighbour within 6" only 0.25 mag fainter in G (3.4" PA235 G14.37 dG+0.25) | galaxy/QSO within 6" in SIMBAD: 2MASS J05345386-0623526 [G] 3.4"
- **young:** SIMBAD young-star types Or*,TT*,Y*O (V* BW Ori; 2MASS J05345386-0623526)
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | 1.18 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | not plain dust: optical brightening -0.087 mag (per-camera -0.087,-0.119,+0.003,-0.020,-0.140) together with the infrared rise | largest seasonal optical dimming 0.23 mag (MJD 59841)
- NEOWISE: score refetch 1.81 (stored 1.81, reproduced True); dW2 0.133, dW1 0.178, 20 visits, 191 points; baseline W1 9.29, W1-W2 0.544; onset between MJD 58741 and 58899
- detector 2: excess 0.598 mag, z 23.3, jitter ratio 6.8
- field control: target step +0.132 (W1 +0.104); neighbours N=119, median +0.003, robust sigma 0.015, max +0.291; z = 8.7
- centroid: jump at onset 0.051" +- 0.056 (0.9 sigma, PA 60); largest consecutive-visit jump 0.153"; rms 0.111"; toward neighbour: none; expected shift if a neighbour were the source: 3.4" G14.4: 0.39"
- AllWISE 2010: W1-W2 0.516, W2-W3 1.832 (W3 S/N 44.1), W3-W4 1.992 (W4 S/N 29.0), ext_flg 1, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.28, ipd_frac_multi_peak 0, NSS none, Teff 5777 K, logg 4.30, H-alpha pEW -3.126 nm, varclass none; M_G 6.15, -1.18 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 3.4" PA235 G14.37 dG+0.25
- SIMBAD (10"): V* BW Ori [TT*; *,Em*,Er*,MIR,NIR,Opt,Or*,TT*,V*,Y*O,ev] 0.01" refs=48; SOXS 105 [X; X] 2.87" refs=1; 2MASS J05345386-0623526 [TT*; *,Em*,G,NIR,Opt,Or*,TT*,Y*O] 3.40" refs=12
- ASAS-SN: 1322 points, cameras bA(g,150, d=-0.087); bE(g,217, d=-0.119); ba(V,172); be(V,194); bi(g,272, d=+0.003); bm(g,192, d=-0.020); bq(g,125, d=-0.140); change at onset (after-before, per-camera median) -0.087 mag; largest seasonal dimming 0.23 mag at MJD 59841
- dust: excess flux W1 4.97 mJy, W2 6.72 mJy, T = 952 K (16-84%: 845-1080) 

### uid1841794  [D2]  KILLED
- position 83.97537 -5.07069; Gaia DR3 3209530379132223360; G 13.57, BP-RP 1.61, plx 2.45 mas; plot `plots/uid1841794.png`
- **KILL:** blend: Gaia neighbour within 6" only 0.88 mag fainter in G (2.0" PA240 G14.45 dG+0.88)
- **young:** SIMBAD young-star types Or*,TT?,Y*O (V* AR Ori A; V* AR Ori) | Gaia DR3 variability class YSO(0.36)
- flags: centroid jump 0.077" (3.4 sigma, PA 61) away from the neighbour(s) 2.0" PA240 G14.4, as expected when the target itself brightens in a blended WISE PSF | binary type in SIMBAD (**, V* AR Ori A) | 1.88 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 0.30 (stored 0.30, reproduced True); dW2 0.025, dW1 0.029, 19 visits, 165 points; baseline W1 9.00, W1-W2 0.437; onset between MJD 58013 and 58168
- detector 2: excess 0.489 mag, z 18.7, jitter ratio 8.3
- field control: target step +0.246 (W1 +0.155); neighbours N=106, median -0.006, robust sigma 0.030, max +0.481; z = 8.4
- centroid: jump at onset 0.077" +- 0.023 (3.4 sigma, PA 61); largest consecutive-visit jump 0.042"; rms 0.040"; toward neighbour: none; expected shift if a neighbour were the source: 2.0" G14.4: 0.41"
- AllWISE 2010: W1-W2 0.473, W2-W3 1.132 (W3 S/N 28.8), W3-W4 1.567 (W4 S/N 1.8), ext_flg 0, ph_qual AAAU: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.17, ipd_frac_multi_peak 0, NSS none, Teff 5515 K, logg 4.16, H-alpha pEW -1.460 nm, varclass YSO(0.36); M_G 5.51, -1.88 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 2.0" PA240 G14.45 dG+0.88
- SIMBAD (10"): V* AR Ori A [Or*; *,**,Or*,V*] 0.04" refs=5; V* AR Ori [Or*; *,Em*,IR,MIR,NIR,Opt,Or*,Rad,TT?,V*,X,Y*O,ev] 0.21" refs=49; V* AR Ori B [*; *,**,V*] 2.04" refs=1; [YKS96] 50 [X; X] 7.06" refs=1
- ASAS-SN: 1284 points, cameras bA(g,150); bE(g,217); ba(V,164, d=+0.100); be(V,194, d=+0.000); bi(g,223, d=-0.082); bm(g,194); bq(g,142, d=-0.085); change at onset (after-before, per-camera median) -0.041 mag; largest seasonal dimming 0.09 mag at MJD 57974
- dust: excess flux W1 7.15 mJy, W2 6.15 mJy, T = 1625 K (16-84%: 1394-1967) 

### uid2131980  [D2]  KILLED
- position 83.71045 -5.39314; Gaia DR3 3017364578727008256; G 15.87, BP-RP 1.70, plx 2.34 mas; plot `plots/uid2131980.png`
- **KILL:** galaxy/QSO within 6" in SIMBAD: V* V475 Ori [G] 0.0"
- **young:** SIMBAD young-star types Or*,TT*,TT?,Y*?,Y*O (V* V475 Ori)
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association)
- NEOWISE: score refetch 0.70 (stored 0.70, reproduced True); dW2 0.070, dW1 0.121, 14 visits, 108 points; baseline W1 10.77, W1-W2 0.400; onset between MJD 59631 and 59995
- detector 2: excess 0.443 mag, z 15.0, jitter ratio 6.7
- field control: target step +0.214 (W1 +0.217); neighbours N=103, median -0.006, robust sigma 0.028, max +0.223; z = 7.8
- centroid: jump at onset 0.051" +- 0.042 (1.2 sigma, PA 353); largest consecutive-visit jump 0.079"; rms 0.048"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.389, W2-W3 4.003 (W3 S/N -0.2), W3-W4 nan (W4 S/N nan), ext_flg 1, ph_qual AAUZ: W3 S/N < 5: no W2-W3 class; W1-W2 > 0.25
- Gaia: RUWE 1.08, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW -2.587 nm, varclass none; M_G 7.72, +0.09 mag vs sequence (on the sequence); neighbours within 10": none
- SIMBAD (10"): V* V475 Ori [TT*; *,Em*,G,MIR,NIR,Or*,TT*,TT?,V*,X,Y*?,Y*O] 0.04" refs=56
- ASAS-SN: 0 points, cameras n/a; change at onset (after-before, per-camera median) n/a mag; largest seasonal dimming n/a mag at MJD n/a
- dust: excess flux W1 2.01 mJy, W2 1.36 mJy, T = 2922 K (16-84%: 2110-5196) 
- checks missing: ASAS-SN (no source)

### uid958315  [D2]  KILLED
- position 334.77944 +73.83737; Gaia DR3 2279011077205275136; G 12.61, BP-RP 1.48, plx 2.93 mas; plot `plots/uid958315.png`
- **KILL:** blend: Gaia neighbour within 6" only 2.66 mag fainter in G (1.6" PA173 G15.27 dG+2.66)
- **young:** SIMBAD young-star types Y*?,Y*O (UCAC4 820-027202) | Gaia DR3 variability class YSO(0.73)
- flags: 2.11 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.10 mag (MJD 60533)
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 21 visits, 409 points; baseline W1 8.66, W1-W2 0.381; onset between MJD 57776 and 57974
- detector 2: excess 0.441 mag, z 19.6, jitter ratio 7.8
- field control: target step +0.052 (W1 +0.052); neighbours N=98, median -0.002, robust sigma 0.007, max +0.409; z = 7.7
- centroid: jump at onset 0.055" +- 0.023 (2.3 sigma, PA 336); largest consecutive-visit jump 0.101"; rms 0.038"; toward neighbour: none; expected shift if a neighbour were the source: 1.6" G15.3: 0.08"
- AllWISE 2010: W1-W2 0.378, W2-W3 2.373 (W3 S/N 88.0), W3-W4 1.881 (W4 S/N 54.5), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.19, ipd_frac_multi_peak 9, NSS none, Teff 5218 K, logg 3.96, H-alpha pEW -0.897 nm, varclass YSO(0.73); M_G 4.95, -2.11 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 1.6" PA173 G15.27 dG+2.66
- SIMBAD (10"): UCAC4 820-027202 [Y*O; *,MIR,NIR,Y*?,Y*O] 0.09" refs=6; Gaia DR3 2279011081503333376 [*; *] 1.62" refs=0; IRAS F22181+7335 [Y*O; IR,Y*O] 7.95" refs=3
- ASAS-SN: 1385 points, cameras bA(g,337); bB(g,119); ba(V,249, d=+0.024); bb(V,163, d=-0.029); bq(g,266); br(g,251); change at onset (after-before, per-camera median) -0.003 mag; largest seasonal dimming 0.10 mag at MJD 60533
- dust: excess flux W1 -1.36 mJy, W2 -1.30 mJy, T = n/a K (16-84%: n/a-n/a) no W2 excess flux after onset

### uid1822358  [D2]  KILLED
- position 83.61887 -5.41608; Gaia DR3 3209424035744296192; G 13.43, BP-RP 1.68, plx 2.46 mas; plot `plots/uid1822358.png`
- **KILL:** galaxy/QSO within 6" in SIMBAD: V* V976 Ori [G] 0.0"
- **young:** SIMBAD young-star types Or*,TT?,Y*O (V* V976 Ori)
- flags: 2.19 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | not plain dust: optical brightening -0.100 mag (per-camera -0.065,-0.065,-0.142,-0.100,-0.166) together with the infrared rise
- NEOWISE: score refetch 1.06 (stored 1.06, reproduced True); dW2 0.116, dW1 0.066, 20 visits, 191 points; baseline W1 9.14, W1-W2 0.491; onset between MJD 59995 and 60204
- detector 2: excess 0.536 mag, z 18.8, jitter ratio 10.9
- field control: target step +0.193 (W1 +0.085); neighbours N=112, median +0.000, robust sigma 0.032, max +0.292; z = 6.0
- centroid: jump at onset 0.018" +- 0.019 (1.0 sigma, PA 25); largest consecutive-visit jump 0.066"; rms 0.025"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.495, W2-W3 2.055 (W3 S/N 26.4), W3-W4 2.691 (W4 S/N -0.6), ext_flg 3, ph_qual AAAU: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.13, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW -0.624 nm, varclass none; M_G 5.39, -2.19 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): V* V976 Ori [Or*; *,Em*,Er*,G,MIR,NIR,Or*,Rad,TT?,V*,X,Y*O] 0.02" refs=61
- ASAS-SN: 1508 points, cameras bA(g,157, d=-0.065); bE(g,220, d=-0.065); ba(V,176); be(V,195); bi(g,341, d=-0.142); bm(g,250, d=-0.100); bq(g,169, d=-0.166); change at onset (after-before, per-camera median) -0.100 mag; largest seasonal dimming 0.07 mag at MJD 59498
- dust: excess flux W1 11.22 mJy, W2 13.30 mJy, T = 1076 K (16-84%: 1025-1132) 

### uid1989676  [D2]  KILLED
- position 112.84104 -46.96217; Gaia DR3 5507467904041566592; G 13.70, BP-RP 1.78, plx 2.39 mas; plot `plots/uid1989676.png`
- **KILL:** blend: Gaia neighbour within 6" only 2.77 mag fainter in G (2.5" PA153 G16.47 dG+2.77)
- **young:** SIMBAD young-star types Or*,Y*?,Y*O ([RP93] 4)
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | 2.24 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | possible optical brightening at onset (-0.164 mag, one camera only) | largest seasonal optical dimming 0.17 mag (MJD 60622)
- NEOWISE: score refetch 0.45 (stored 0.45, reproduced True); dW2 0.055, dW1 -0.027, 21 visits, 374 points; baseline W1 9.13, W1-W2 0.495; onset between MJD 58219 and 58428
- detector 2: excess 0.529 mag, z 16.1, jitter ratio 8.8
- field control: target step +0.064 (W1 +0.042); neighbours N=103, median -0.002, robust sigma 0.011, max +0.226; z = 5.9
- centroid: jump at onset 0.240" +- 0.085 (2.8 sigma, PA 338); largest consecutive-visit jump 0.398"; rms 0.117"; toward neighbour: none; expected shift if a neighbour were the source: 2.5" G16.5: 0.14"
- AllWISE 2010: W1-W2 0.638, W2-W3 1.398 (W3 S/N 67.1), W3-W4 1.539 (W4 S/N 26.4), ext_flg 1, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.06, ipd_frac_multi_peak 0, NSS none, Teff 4960 K, logg 4.11, H-alpha pEW -0.733 nm, varclass none; M_G 5.60, -2.24 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 2.5" PA153 G16.47 dG+2.77
- SIMBAD (10"): [RP93] 4 [Or*; *,Em*,NIR,Or*,Y*?,Y*O] 0.16" refs=6; Gaia DR3 5507467904038766976 [*; *] 2.64" refs=2
- ASAS-SN: 1315 points, cameras bF(g,396); bf(V,227, d=-0.164); bj(g,494); bn(g,198); change at onset (after-before, per-camera median) -0.164 mag; largest seasonal dimming 0.17 mag at MJD 60622
- dust: excess flux W1 -0.18 mJy, W2 3.62 mJy, T = 150 K (16-84%: 150-379) W1 excess <= 0: colder than ~150 K (upper limit)

### uid1657002  [D2]  KILLED
- position 83.71486 -5.42027; Gaia DR3 3017269883276585088; G 13.96, BP-RP 1.79, plx 2.53 mas; plot `plots/uid1657002.png`
- **KILL:** galaxy/QSO within 6" in SIMBAD: V* V401 Ori [G] 0.0"
- **young:** SIMBAD young-star types Or*,TT*,TT?,Y*?,Y*O (V* V401 Ori)
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | 1.91 mag above the main sequence at its colour | AllWISE 2010 Class I-like colour cuts (W1-W2 > 1.0, W2-W3 > 2.0)
- NEOWISE: score refetch 1.65 (stored 1.65, reproduced True); dW2 0.244, dW1 0.154, 15 visits, 110 points; baseline W1 8.74, W1-W2 0.540; onset between MJD 59109 and 59473
- detector 2: excess 0.571 mag, z 17.0, jitter ratio 10.9
- field control: target step +0.234 (W1 +0.220); neighbours N=103, median +0.002, robust sigma 0.044, max +0.180; z = 5.3
- centroid: jump at onset 0.040" +- 0.018 (2.2 sigma, PA 353); largest consecutive-visit jump 0.100"; rms 0.036"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 1.073, W2-W3 3.000 (W3 S/N 16.8), W3-W4 3.034 (W4 S/N nan), ext_flg 1, ph_qual AAAZ: Class I-like colour cuts (W1-W2 > 1.0, W2-W3 > 2.0)
- Gaia: RUWE 1.06, ipd_frac_multi_peak 0, NSS none, Teff 5908 K, logg 4.14, H-alpha pEW -1.149 nm, varclass none; M_G 5.98, -1.91 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): V* V401 Ori [TT*; *,Em*,G,NIR,Or*,TT*,TT?,V*,X,Y*?,Y*O] 0.03" refs=65
- ASAS-SN: 0 points, cameras n/a; change at onset (after-before, per-camera median) n/a mag; largest seasonal dimming n/a mag at MJD n/a
- dust: excess flux W1 22.92 mJy, W2 26.09 mJy, T = 1123 K (16-84%: 1072-1178) 
- checks missing: ASAS-SN (no source)

### uid1363385  [D2]  KILLED
- position 85.04659 -7.16449; Gaia DR3 3016086740044032512; G 14.97, BP-RP 1.97, plx 2.68 mas; plot `plots/uid1363385.png`
- **KILL:** blend: Gaia neighbour within 6" only 1.55 mag fainter in G (2.7" PA128 G16.52 dG+1.55)
- **young:** SIMBAD young-star types Or*,Y*O (V* DK Ori)
- flags: centroid jump 0.222" (3.7 sigma, PA 298) away from the neighbour(s) 2.7" PA128 G16.5, as expected when the target itself brightens in a blended WISE PSF | binary type in SIMBAD (**, V* DK Ori A) | AllWISE ext_flg = 1 (extended or 2MASS XSC association) | 1.27 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | optical dimming +0.124 mag after the infrared onset (debris transit signature) | largest seasonal optical dimming 0.35 mag (MJD 60055)
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 21 visits, 216 points; baseline W1 9.53, W1-W2 0.594; onset between MJD 57089 and 57283
- detector 2: excess 0.594 mag, z 14.3, jitter ratio 10.2
- field control: target step +0.050 (W1 +0.042); neighbours N=72, median -0.002, robust sigma 0.010, max +0.064; z = 5.0
- centroid: jump at onset 0.222" +- 0.060 (3.7 sigma, PA 298); largest consecutive-visit jump 0.124"; rms 0.103"; toward neighbour: none; expected shift if a neighbour were the source: 2.7" G16.5: 0.12"
- AllWISE 2010: W1-W2 0.569, W2-W3 1.444 (W3 S/N 42.8), W3-W4 1.696 (W4 S/N 19.9), ext_flg 1, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.04, ipd_frac_multi_peak 0, NSS none, Teff 3661 K, logg 4.03, H-alpha pEW -0.068 nm, varclass none; M_G 7.11, -1.27 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 2.7" PA128 G16.52 dG+1.55
- SIMBAD (10"): V* DK Ori A [*; *,**,V*] 0.02" refs=3; V* DK Ori [Or*; *,**,Em*,MIR,NIR,Opt,Or*,V*,Y*O] 0.33" refs=17; V* DK Ori B [*; *,**,V*] 2.66" refs=2
- ASAS-SN: 1098 points, cameras bB(g,93); bF(g,187); ba(V,30); bb(V,129, d=+0.124); bf(V,143); bj(g,250); bn(g,107); br(g,159); change at onset (after-before, per-camera median) +0.124 mag; largest seasonal dimming 0.35 mag at MJD 60055
- dust: excess flux W1 -2.46 mJy, W2 -1.80 mJy, T = n/a K (16-84%: n/a-n/a) no W2 excess flux after onset

### uid2294196  [D2]  KILLED
- position 87.17303 +4.59704; Gaia DR3 3319709042032553728; G 15.39, BP-RP 1.73, plx 2.28 mas; plot `plots/uid2294196.png`
- **KILL:** blend: Gaia neighbour within 6" only -0.47 mag fainter in G (2.8" PA101 G14.92 dG-0.47)
- **young:** SIMBAD young-star types Y*O (Kiso A-0832   2)
- flags: binary type in SIMBAD (**, Gaia DR2 3319709042032553728) | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 0.22 (stored 0.22, reproduced True); dW2 0.021, dW1 0.001, 19 visits, 188 points; baseline W1 8.79, W1-W2 0.627; onset between MJD 57650 and 57815
- detector 2: excess 0.666 mag, z 21.3, jitter ratio 8.3
- field control: target step +0.053 (W1 +0.036); neighbours N=83, median -0.003, robust sigma 0.012, max +0.067; z = 4.7
- centroid: jump at onset 0.021" +- 0.078 (0.3 sigma, PA 105); largest consecutive-visit jump 0.096"; rms 0.117"; toward neighbour: 2.8" PA101 G14.9 (angle 4 deg); expected shift if a neighbour were the source: 2.8" G14.9: 0.13"
- AllWISE 2010: W1-W2 0.690, W2-W3 1.666 (W3 S/N 45.6), W3-W4 2.023 (W4 S/N 21.3), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.14, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW -12.551 nm, varclass none; M_G 7.18, -0.52 mag vs sequence (on the sequence); neighbours within 10": 2.8" PA101 G14.92 dG-0.47
- SIMBAD (10"): Gaia DR2 3319709042032553728 [*; *] 0.05" refs=1; Kiso A-0832   2 [Y*O; *,**,Em*,MIR,NIR,Y*O] 2.39" refs=2; Gaia DR2 3319709042033751936 [*; *] 2.84" refs=1
- ASAS-SN: 0 points, cameras n/a; change at onset (after-before, per-camera median) n/a mag; largest seasonal dimming n/a mag at MJD n/a
- dust: excess flux W1 2.74 mJy, W2 5.85 mJy, T = 686 K (16-84%: 467-978) 
- checks missing: ASAS-SN (no source)

### uid2331494  [D2]  KILLED
- position 267.46174 -28.13089; Gaia DR3 4057643006854955008; G 15.32, BP-RP 1.79, plx 2.27 mas; plot `plots/uid2331494.png`
- **KILL:** blend: Gaia neighbour within 6" only 2.19 mag fainter in G (2.2" PA79 G17.51 dG+2.19; 4.7" PA10 G19.26 dG+3.94; 4.9" PA294 G20.31 dG+4.99; 5.0" PA136 G20.33 dG+5.02; 5.2" PA154 G18.16 dG+2.84; 6.4" PA238 G21.06 dG+5.74; 9.7" PA166 G18.49 dG+3.17)
- flags: 0.78 mag above the main sequence at its colour
- NEOWISE: score refetch 0.53 (stored 0.53, reproduced True); dW2 0.034, dW1 0.064, 19 visits, 137 points; baseline W1 9.41, W1-W2 0.696; onset between MJD 58927 and 59091
- detector 2: excess 0.728 mag, z 21.8, jitter ratio 6.0
- field control: target step +0.103 (W1 +0.113); neighbours N=115, median +0.002, robust sigma 0.027, max +0.116; z = 3.7
- centroid: jump at onset 0.089" +- 0.062 (1.4 sigma, PA 295); largest consecutive-visit jump 0.154"; rms 0.093"; toward neighbour: 4.9" PA294 G20.3 (angle 1 deg); expected shift if a neighbour were the source: 2.2" G17.5: 0.20"; 4.7" G19.3: 0.43"; 4.9" G20.3: 0.44"; 5.0" G20.3: 0.45"; 5.2" G18.2: 0.47"; 6.4" G21.1: 0.58"; 9.7" G18.5: 0.88"
- AllWISE 2010: W1-W2 0.694, W2-W3 -0.246 (W3 S/N -2.4), W3-W4 2.193 (W4 S/N -2.2), ext_flg 0, ph_qual AAUU: W3 S/N < 5: no W2-W3 class; W1-W2 > 0.25
- Gaia: RUWE 1.21, ipd_frac_multi_peak 0, NSS none, Teff 4507 K, logg 4.34, H-alpha pEW -0.121 nm, varclass none; M_G 7.10, -0.78 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 2.2" PA79 G17.51 dG+2.19; 4.7" PA10 G19.26 dG+3.94; 4.9" PA294 G20.31 dG+4.99; 5.0" PA136 G20.33 dG+5.02; 5.2" PA154 G18.16 dG+2.84; 6.4" PA238 G21.06 dG+5.74; 9.7" PA166 G18.49 dG+3.17
- SIMBAD (10"): Gaia DR3 4057643006854955008 [*; *] 0.08" refs=1
- ASAS-SN: 1199 points, cameras bF(g,241, d=-0.017); bH(g,225, d=+0.006); bf(V,194); bj(g,236, d=-0.026); bn(g,154, d=+0.073); br(g,149, d=+0.057); change at onset (after-before, per-camera median) +0.006 mag; largest seasonal dimming 0.04 mag at MJD 60434
- dust: excess flux W1 4.08 mJy, W2 3.84 mJy, T = 1415 K (16-84%: 1093-2018) 

### uid1763891  [D2]  KILLED
- position 147.34330 -60.12873; Gaia DR3 5257080553484632448; G 14.56, BP-RP 1.43, plx 2.49 mas; plot `plots/uid1763891.png`
- **KILL:** blend: Gaia neighbour within 6" only 0.75 mag fainter in G (1.2" PA201 G19.75 dG+5.19; 2.9" PA200 G20.63 dG+6.06; 4.4" PA63 G15.31 dG+0.75; 6.2" PA80 G16.29 dG+1.73; 7.5" PA322 G20.67 dG+6.11; 8.0" PA138 G20.39 dG+5.83; 8.3" PA5 G20.71 dG+6.15; 9.6" PA203 G20.33 dG+5.77)
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association)
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 18 visits, 235 points; baseline W1 11.10, W1-W2 0.231; onset between MJD 59217 and 59583
- detector 2: excess 0.293 mag, z 13.9, jitter ratio 4.6
- field control: target step +0.043 (W1 +0.035); neighbours N=132, median -0.002, robust sigma 0.021, max +0.052; z = 2.1
- centroid: jump at onset 0.259" +- 0.088 (2.9 sigma, PA 261); largest consecutive-visit jump 0.192"; rms 0.114"; toward neighbour: none; expected shift if a neighbour were the source: 1.2" G19.8: 0.05"; 2.9" G20.6: 0.11"; 4.4" G15.3: 0.17"; 6.2" G16.3: 0.24"; 7.5" G20.7: 0.29"; 8.0" G20.4: 0.31"; 8.3" G20.7: 0.32"; 9.6" G20.3: 0.37"
- AllWISE 2010: W1-W2 0.220, W2-W3 1.557 (W3 S/N 36.7), W3-W4 1.160 (W4 S/N 6.9), ext_flg 1, ph_qual AAAB: W3 excess only (W2-W3 > 1.0; debris-disk-like or blend)
- Gaia: RUWE 1.03, ipd_frac_multi_peak 1, NSS none, Teff nan K, logg nan, H-alpha pEW -0.152 nm, varclass RS(0.51); M_G 6.54, -0.39 mag vs sequence (on the sequence); neighbours within 10": 1.2" PA201 G19.75 dG+5.19; 2.9" PA200 G20.63 dG+6.06; 4.4" PA63 G15.31 dG+0.75; 6.2" PA80 G16.29 dG+1.73; 7.5" PA322 G20.67 dG+6.11; 8.0" PA138 G20.39 dG+5.83; 8.3" PA5 G20.71 dG+6.15; 9.6" PA203 G20.33 dG+5.77
- SIMBAD (10"): no object
- ASAS-SN: 2121 points, cameras bE(g,382, d=-0.008); bG(g,381, d=-0.011); bg(V,226); bi(g,424, d=-0.025); bk(g,388, d=-0.015); bm(g,241, d=-0.006); bo(g,79, d=-0.008); change at onset (after-before, per-camera median) -0.009 mag; largest seasonal dimming 0.03 mag at MJD 59291
- dust: excess flux W1 -0.12 mJy, W2 -0.07 mJy, T = n/a K (16-84%: n/a-n/a) no W2 excess flux after onset

### uid999033  [D2]  KILLED
- position 267.53313 -28.86257; Gaia DR3 4057393138528809088; G 14.94, BP-RP 1.58, plx 2.90 mas; plot `plots/uid999033.png`
- **KILL:** blend: Gaia neighbour within 6" only 2.16 mag fainter in G (2.1" PA37 G19.53 dG+4.58; 2.8" PA22 G20.43 dG+5.48; 3.1" PA238 G18.28 dG+3.34; 3.9" PA176 G20.69 dG+5.75; 4.6" PA231 G17.10 dG+2.16; 5.8" PA89 G20.58 dG+5.64; 7.8" PA179 G19.69 dG+4.74; 8.5" PA27 G18.40 dG+3.46; 9.4" PA175 G19.94 dG+5.00)
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 16 visits, 114 points; baseline W1 9.69, W1-W2 0.571; onset between MJD 60187 and 60387
- detector 2: excess 0.626 mag, z 24.7, jitter ratio 4.1
- field control: target step +0.048 (W1 +0.014); neighbours N=73, median +0.018, robust sigma 0.047, max +0.179; z = 0.6
- centroid: jump at onset 0.262" +- 0.111 (2.4 sigma, PA 41); largest consecutive-visit jump 0.344"; rms 0.171"; toward neighbour: 2.1" PA37 G19.5 (angle 3 deg); 2.8" PA22 G20.4 (angle 19 deg); 8.5" PA27 G18.4 (angle 13 deg); expected shift if a neighbour were the source: 2.1" G19.5: 0.09"; 2.8" G20.4: 0.12"; 3.1" G18.3: 0.13"; 3.9" G20.7: 0.17"; 4.6" G17.1: 0.20"; 5.8" G20.6: 0.25"; 7.8" G19.7: 0.33"; 8.5" G18.4: 0.36"; 9.4" G19.9: 0.40"
- AllWISE 2010: W1-W2 0.502, W2-W3 1.316 (W3 S/N 12.1), W3-W4 3.261 (W4 S/N 20.3), ext_flg 1, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.02, ipd_frac_multi_peak 0, NSS none, Teff 4497 K, logg 4.64, H-alpha pEW -0.029 nm, varclass none; M_G 7.26, -0.05 mag vs sequence (on the sequence); neighbours within 10": 2.1" PA37 G19.53 dG+4.58; 2.8" PA22 G20.43 dG+5.48; 3.1" PA238 G18.28 dG+3.34; 3.9" PA176 G20.69 dG+5.75; 4.6" PA231 G17.10 dG+2.16; 5.8" PA89 G20.58 dG+5.64; 7.8" PA179 G19.69 dG+4.74; 8.5" PA27 G18.40 dG+3.46; 9.4" PA175 G19.94 dG+5.00
- SIMBAD (10"): no object
- ASAS-SN: 0 points, cameras n/a; change at onset (after-before, per-camera median) n/a mag; largest seasonal dimming n/a mag at MJD n/a
- dust: excess flux W1 0.43 mJy, W2 1.76 mJy, T = 493 K (16-84%: 150-771) 
- checks missing: ASAS-SN (no source)

### uid1967034  [D2]  KILLED
- position 85.92534 +10.03906; Gaia DR3 3336492915234886912; G 13.64, BP-RP 1.73, plx 2.40 mas; plot `plots/uid1967034.png`
- **KILL:** blend: Gaia neighbour within 6" only 2.59 mag fainter in G (1.3" PA9 G16.23 dG+2.59)
- **young:** SIMBAD young-star types Or*,Y*?,Y*O (Gaia DR2 3336492915234886912; [DM99] 234)
- flags: binary type in SIMBAD (**, Gaia DR2 3336492915234886912) | 2.17 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | optical dimming +0.080 mag after the infrared onset (debris transit signature) | largest seasonal optical dimming 0.18 mag (MJD 60407)
- NEOWISE: score refetch 0.26 (stored 0.26, reproduced True); dW2 0.045, dW1 0.018, 20 visits, 204 points; baseline W1 9.37, W1-W2 0.493; onset between MJD 57449 and 57649
- detector 2: excess 0.532 mag, z 17.0, jitter ratio 16.0
- field control: target step -0.029 (W1 -0.066); neighbours N=93, median -0.001, robust sigma 0.010, max +0.065; z = -2.9
- centroid: jump at onset 0.009" +- 0.013 (0.7 sigma, PA 87); largest consecutive-visit jump 0.090"; rms 0.033"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.491, W2-W3 1.236 (W3 S/N 56.5), W3-W4 1.386 (W4 S/N 15.3), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.12, ipd_frac_multi_peak 0, NSS none, Teff 4756 K, logg 4.11, H-alpha pEW -0.260 nm, varclass none; M_G 5.54, -2.17 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 1.3" PA9 G16.23 dG+2.59
- SIMBAD (10"): Gaia DR2 3336492915234886912 [Or*; *,Or*,Y*?] 0.04" refs=13; [DM99] 234 [Y*O; *,**,MIR,NIR,Y*O] 0.05" refs=11; Gaia DR2 3336492915232557312 [*; *] 1.28" refs=6
- ASAS-SN: 940 points, cameras bA(g,183); bE(g,120); ba(V,156, d=+0.080); bi(g,236); bm(g,122); bq(g,123); change at onset (after-before, per-camera median) +0.080 mag; largest seasonal dimming 0.18 mag at MJD 60407
- dust: excess flux W1 2.30 mJy, W2 3.61 mJy, T = 842 K (16-84%: 733-973) 

### uid2280632  [D2]  KILLED
- position 86.43608 -9.32089; Gaia DR3 3012048886670499968; G 13.80, BP-RP 1.64, plx 2.29 mas; plot `plots/uid2280632.png`
- **KILL:** blend: Gaia neighbour within 6" only 1.89 mag fainter in G (2.5" PA333 G15.69 dG+1.89)
- **young:** SIMBAD young-star types Y*O (2MASS J05454464-0919149; 2MASS J05454459-0919136) | Gaia DR3 variability class YSO(0.65)
- flags: 1.87 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 19 visits, 179 points; baseline W1 8.85, W1-W2 0.604; onset between MJD 57813 and 58016
- detector 2: excess 0.654 mag, z 24.2, jitter ratio 6.3
- field control: target step -0.057 (W1 -0.160); neighbours N=52, median -0.005, robust sigma 0.013, max +0.065; z = -3.9
- centroid: jump at onset 0.033" +- 0.032 (1.0 sigma, PA 144); largest consecutive-visit jump 0.112"; rms 0.047"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.619, W2-W3 2.139 (W3 S/N 70.7), W3-W4 2.179 (W4 S/N 41.4), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.14, ipd_frac_multi_peak 0, NSS none, Teff 4956 K, logg 4.15, H-alpha pEW -0.140 nm, varclass YSO(0.65); M_G 5.60, -1.87 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 2.5" PA333 G15.69 dG+1.89
- SIMBAD (10"): 2MASS J05454464-0919149 [Y*O; *,NIR,Y*O] 0.02" refs=9; 2MASS J05454459-0919136 [Y*O; *,MIR,NIR,Y*O] 2.50" refs=4
- ASAS-SN: 1537 points, cameras bC(g,130); bG(g,254); ba(V,27); bc(V,119, d=-0.012); be(V,34); bg(V,214, d=+0.006); bk(g,368); bo(g,263); bs(g,128); change at onset (after-before, per-camera median) -0.003 mag; largest seasonal dimming 0.09 mag at MJD 59230
- dust: excess flux W1 -3.48 mJy, W2 1.38 mJy, T = 150 K (16-84%: 150-150) W1 excess <= 0: colder than ~150 K (upper limit)

