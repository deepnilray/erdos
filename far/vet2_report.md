# vet2 report: far target list (final)

Generated 2026-11-22 06:15 UTC; 202 targets; machine-generated, the plots in plots/ still need a look by eye.

Kill rules: field-control z < 5 (detector-1 and list targets); centroid jump > 3 sigma toward a Gaia neighbour; Gaia neighbour within 6" with dG < 3; baseline W1 < 8; SIMBAD CV / confirmed eclipsing binary (counterpart within 3"); SIMBAD galaxy/QSO within 6"; young star (SIMBAD Y*O, Y*?, TT*, TT?, Or*, Ae*, Ae?, pr* within 5" or Gaia variability class YSO) kills detector-1/list targets and labels detector-2 targets 'known/likely young star'. Flags (not kills): 'not plain dust' (optical brightening at the infrared onset in >= 2 ASAS-SN cameras, none dimming, median < -0.015 mag), SIMBAD '?' candidate types, RUWE, NSS, ext_flg, colour classes.

## Controls

| Control | Result | Detail |
|---|---|---|
| ASASSN-21qj | PASS | category SURVIVOR, SIMBAD 2MASS J08152329-3859234 (10 refs), field z 57.3, missing: none |
| J060000 | PASS | category SURVIVOR, largest ASAS-SN seasonal dimming 0.35 mag at MJD 58864 |
| V836 Tau | PASS | young: SIMBAD young-star types Or*,TT*,TT?,Y*?,Y*O (V* V836 Tau) | Gaia DR3 variability class YSO(0.83) |

Counts: {'YOUNG': 140, 'KILLED': 35, 'SURVIVOR': 27}

## Survivors (27)

### uid1144163  [D2]  SURVIVOR
- position 266.89948 -29.63303; Gaia DR3 4057203850731922560; G 12.79, BP-RP 1.03, plx 2.81 mas; plot `plots/uid1144163.png`
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 16 visits, 125 points; baseline W1 8.33, W1-W2 0.136; onset between MJD 58560 and 58927
- detector 2: excess 0.188 mag, z 12.6, jitter ratio 4.2
- field control: target step +0.123 (W1 -0.064); neighbours N=111, median +0.008, robust sigma 0.027, max +0.102; z = 4.3
- centroid: jump at onset 0.358" +- 0.411 (0.9 sigma, PA 172); largest consecutive-visit jump 0.627"; rms 0.294"; toward neighbour: none; expected shift if a neighbour were the source: 2.9" G19.9: 0.32"; 3.5" G19.8: 0.37"; 4.9" G20.7: 0.52"; 6.7" G20.8: 0.72"; 9.4" G19.5: 1.01"; 9.9" G17.8: 1.06"
- AllWISE 2010: W1-W2 -0.039, W2-W3 0.484 (W3 S/N 11.4), W3-W4 1.506 (W4 S/N 4.1), ext_flg 0, ph_qual AAAB: photosphere-like (W2-W3 < 0.5)
- Gaia: RUWE 0.85, ipd_frac_multi_peak 0, NSS none, Teff 5679 K, logg 4.36, H-alpha pEW 0.095 nm, varclass none; M_G 5.03, -0.60 mag vs sequence (on the sequence); neighbours within 10": 2.9" PA224 G19.95 dG+7.16; 3.5" PA77 G19.79 dG+6.99; 4.9" PA345 G20.71 dG+7.92; 6.7" PA351 G20.77 dG+7.98; 9.4" PA352 G19.53 dG+6.74; 9.9" PA224 G17.76 dG+4.97
- SIMBAD (10"): no object
- ASAS-SN: 1003 points, cameras bF(g,250, d=-0.003); bf(V,196); bj(g,241, d=+0.001); bn(g,163, d=-0.008); br(g,153, d=-0.003); change at onset (after-before, per-camera median) -0.003 mag; largest seasonal dimming 0.01 mag at MJD 59874
- dust: excess flux W1 -10.54 mJy, W2 5.73 mJy, T = 150 K (16-84%: 150-150) W1 excess <= 0: colder than ~150 K (upper limit)

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

### uid456710  [D2]  SURVIVOR
- position 266.00230 -29.70248; Gaia DR3 4057049442363660800; G 12.77, BP-RP 1.13, plx 3.36 mas; plot `plots/uid456710.png`
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 9 visits, 91 points; baseline W1 9.21, W1-W2 0.360; onset between MJD 60186 and 60386
- detector 2: excess 0.418 mag, z 25.6, jitter ratio 7.7
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

### uid959202  [D2]  SURVIVOR
- position 123.56894 -34.93364; Gaia DR3 5546268776043673984; G 13.83, BP-RP 1.89, plx 2.93 mas; plot `plots/uid959202.png`
- flags: 1.99 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.61 mag (MJD 60691)
- NEOWISE: score refetch 1.96 (stored 1.96, reproduced True); dW2 0.366, dW1 0.067, 10 visits, 138 points; baseline W1 10.10, W1-W2 0.410; onset between MJD 57144 and 57338
- detector 2: excess 0.422 mag, z 11.2, jitter ratio 15.8
- field control: target step +0.482 (W1 +0.122); neighbours N=179, median -0.005, robust sigma 0.011, max +0.063; z = 43.7
- centroid: jump at onset 0.010" +- 0.038 (0.3 sigma, PA 281); largest consecutive-visit jump 0.118"; rms 0.041"; toward neighbour: 6.3" PA291 G17.1 (angle 11 deg); expected shift if a neighbour were the source: 6.3" G17.1: 2.25"
- AllWISE 2010: W1-W2 0.433, W2-W3 2.056 (W3 S/N 61.1), W3-W4 2.037 (W4 S/N 26.4), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.36, ipd_frac_multi_peak 0, NSS none, Teff 5103 K, logg 4.17, H-alpha pEW -1.052 nm, varclass none; M_G 6.17, -1.99 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 6.3" PA291 G17.06 dG+3.23
- SIMBAD (10"): Gaia DR3 5546268776043673984 [*; *] 0.23" refs=1
- ASAS-SN: 1268 points, cameras bH(g,353); bh(V,219); bl(g,487); bp(g,209); change at onset (after-before, per-camera median) n/a mag; largest seasonal dimming 0.61 mag at MJD 60691
- dust: excess flux W1 4.28 mJy, W2 17.10 mJy, T = 500 K (16-84%: 489-511) 
- checks missing: ASAS-SN change at onset (no camera spans the onset)

### uid1272600  [D2]  SURVIVOR
- position 126.59789 -70.52863; Gaia DR3 5221762453262444544; G 14.09, BP-RP 1.33, plx 2.73 mas; plot `plots/uid1272600.png`
- flags: possible optical brightening at onset (-0.068 mag, one camera only) | largest seasonal optical dimming 0.29 mag (MJD 58530)
- NEOWISE: score refetch 1.60 (stored 1.60, reproduced True); dW2 0.178, dW1 0.138, 22 visits, 510 points; baseline W1 11.37, W1-W2 0.160; onset between MJD 57579 and 57777
- detector 2: excess 0.223 mag, z 11.6, jitter ratio 8.1
- field control: target step +0.360 (W1 +0.265); neighbours N=72, median -0.002, robust sigma 0.009, max +0.057; z = 42.5
- centroid: jump at onset 0.017" +- 0.012 (1.4 sigma, PA 131); largest consecutive-visit jump 0.040"; rms 0.021"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.217, W2-W3 0.788 (W3 S/N 30.5), W3-W4 0.991 (W4 S/N 3.6), ext_flg 0, ph_qual AAAB: weak W3 excess (0.5 < W2-W3 < 1.0)
- Gaia: RUWE 1.13, ipd_frac_multi_peak 0, NSS none, Teff 6241 K, logg 4.50, H-alpha pEW -1.487 nm, varclass none; M_G 6.28, -0.36 mag vs sequence (on the sequence); neighbours within 10": none
- SIMBAD (10"): no object
- ASAS-SN: 1426 points, cameras bF(g,371); bf(V,279, d=-0.068); bj(g,444); bn(g,332); change at onset (after-before, per-camera median) -0.068 mag; largest seasonal dimming 0.29 mag at MJD 58530
- dust: excess flux W1 1.59 mJy, W2 1.18 mJy, T = 2204 K (16-84%: 1886-2686) 

### uid239897  [D2]  SURVIVOR
- position 222.73717 +36.20318; Gaia DR3 1293509154439630464; G 14.04, BP-RP 1.46, plx 3.62 mas; plot `plots/uid239897.png`
- flags: AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 1.25 (stored 1.25, reproduced True); dW2 0.095, dW1 0.073, 21 visits, 272 points; baseline W1 11.28, W1-W2 0.307; onset between MJD 57931 and 58134
- detector 2: excess 0.368 mag, z 17.7, jitter ratio 4.1
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
- detector 2: excess 0.398 mag, z 16.5, jitter ratio 5.9
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
- detector 2: excess 0.834 mag, z 29.7, jitter ratio 9.4
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
- detector 2: excess 0.539 mag, z 23.1, jitter ratio 6.0
- field control: target step +0.163 (W1 +0.071); neighbours N=127, median +0.000, robust sigma 0.012, max +0.036; z = 13.7
- centroid: jump at onset 0.008" +- 0.020 (0.4 sigma, PA 297); largest consecutive-visit jump 0.037"; rms 0.034"; toward neighbour: none; expected shift if a neighbour were the source: 8.7" G17.3: 1.21"
- AllWISE 2010: W1-W2 0.485, W2-W3 2.091 (W3 S/N 36.2), W3-W4 0.834 (W4 S/N 5.0), ext_flg 0, ph_qual AAAB: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.06, ipd_frac_multi_peak 1, NSS none, Teff 4485 K, logg 4.44, H-alpha pEW -0.198 nm, varclass RS(0.34); M_G 6.95, -0.31 mag vs sequence (on the sequence); neighbours within 10": 8.7" PA213 G17.27 dG+2.51
- SIMBAD (10"): ZTF J184010.33+232821.7 [BY*; *,BY*] 0.10" refs=4
- ASAS-SN: 0 points, cameras n/a; change at onset (after-before, per-camera median) n/a mag; largest seasonal dimming n/a mag at MJD n/a
- dust: excess flux W1 -0.12 mJy, W2 0.10 mJy, T = 150 K (16-84%: 150-150) W1 excess <= 0: colder than ~150 K (upper limit)
- checks missing: ASAS-SN (no source)

### uid325718  [D2]  SURVIVOR
- position 35.42480 +62.01116; Gaia DR3 513833673802372736; G 13.99, BP-RP 1.39, plx 3.51 mas; plot `plots/uid325718.png`
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 9 visits, 95 points; baseline W1 11.35, W1-W2 0.948; onset between MJD 57986 and 58144
- detector 2: excess 1.011 mag, z 51.1, jitter ratio 7.8
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
- detector 2: excess 0.809 mag, z 56.2, jitter ratio 4.5
- field control: target step +0.112 (W1 +0.107); neighbours N=93, median -0.007, robust sigma 0.012, max +0.078; z = 10.0
- centroid: jump at onset 0.022" +- 0.026 (0.8 sigma, PA 82); largest consecutive-visit jump 0.089"; rms 0.038"; toward neighbour: none; expected shift if a neighbour were the source: 2.0" G20.1: 0.19"
- AllWISE 2010: W1-W2 0.743, W2-W3 2.058 (W3 S/N 50.1), W3-W4 1.442 (W4 S/N 17.0), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 0.96, ipd_frac_multi_peak 0, NSS none, Teff 5498 K, logg 4.59, H-alpha pEW 0.028 nm, varclass none; M_G 5.58, +0.04 mag vs sequence (on the sequence); neighbours within 10": 2.0" PA182 G20.10 dG+6.78
- SIMBAD (10"): TIC 408967891 [; ] 0.10" refs=1; 2MASS J06091701-1508085 [*; *,MIR,NIR] 0.10" refs=1; Gaia DR3 2993153951145272192 [*; *] 1.97" refs=1
- ASAS-SN: 1556 points, cameras bA(g,133, d=+0.011); bE(g,224, d=-0.026); ba(V,151); be(V,223); bi(g,403, d=+0.006); bm(g,251, d=-0.018); bq(g,171, d=-0.008); change at onset (after-before, per-camera median) -0.008 mag; largest seasonal dimming 0.04 mag at MJD 57724
- dust: excess flux W1 1.56 mJy, W2 2.22 mJy, T = 911 K (16-84%: 855-976) 

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

### uid342028  [D2]  SURVIVOR
- position 225.72799 -14.21404; Gaia DR3 6308812594204740352; G 12.51, BP-RP 1.08, plx 3.49 mas; plot `plots/uid342028.png`
- flags: AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 21 visits, 163 points; baseline W1 10.23, W1-W2 0.430; onset between MJD 59779 and 59981
- detector 2: excess 0.485 mag, z 29.7, jitter ratio 4.7
- field control: target step +0.058 (W1 +0.029); neighbours N=35, median -0.003, robust sigma 0.013, max +0.032; z = 4.6
- centroid: jump at onset 0.007" +- 0.013 (0.5 sigma, PA 239); largest consecutive-visit jump 0.046"; rms 0.026"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.429, W2-W3 1.517 (W3 S/N 50.4), W3-W4 0.921 (W4 S/N 8.5), ext_flg 0, ph_qual AAAB: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.37, ipd_frac_multi_peak 0, NSS none, Teff 5461 K, logg 4.47, H-alpha pEW 0.105 nm, varclass none; M_G 5.22, -0.59 mag vs sequence (on the sequence); neighbours within 10": none
- SIMBAD (10"): UCAC4 379-068655 [*; *,MIR,NIR] 0.20" refs=1
- ASAS-SN: 1152 points, cameras bB(g,76); bF(g,124, d=-0.001); bb(V,111); bf(V,138); bj(g,281, d=+0.010); bn(g,230, d=-0.001); br(g,145, d=+0.006); cB(g,47); change at onset (after-before, per-camera median) +0.002 mag; largest seasonal dimming 0.00 mag at MJD 59039
- dust: excess flux W1 -0.14 mJy, W2 -0.01 mJy, T = n/a K (16-84%: n/a-n/a) no W2 excess flux after onset

### uid1474845  [D2]  SURVIVOR
- position 110.95000 -25.63462; Gaia DR3 5616572649029724416; G 11.61, BP-RP 1.11, plx 2.62 mas; plot `plots/uid1474845.png`
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | 2.21 mag above the main sequence at its colour
- NEOWISE: score refetch 0.89 (stored 0.89, reproduced True); dW2 0.030, dW1 0.003, 13 visits, 107 points; baseline W1 9.58, W1-W2 0.171; onset between MJD 57317 and 57482
- detector 2: excess 0.228 mag, z 14.0, jitter ratio 3.1
- field control: target step +0.057 (W1 +0.006); neighbours N=100, median -0.003, robust sigma 0.021, max +0.218; z = 2.8
- centroid: jump at onset 0.029" +- 0.023 (1.2 sigma, PA 64); largest consecutive-visit jump 0.078"; rms 0.031"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.061, W2-W3 1.091 (W3 S/N 31.9), W3-W4 4.350 (W4 S/N 38.3), ext_flg 1, ph_qual AAAA: W3 excess only (W2-W3 > 1.0; debris-disk-like or blend)
- Gaia: RUWE 1.07, ipd_frac_multi_peak 0, NSS none, Teff 5103 K, logg 4.03, H-alpha pEW 0.042 nm, varclass none; M_G 3.70, -2.21 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): no object
- ASAS-SN: 1194 points, cameras bG(g,318); bg(V,225); bk(g,361); bo(g,167); bs(g,123); change at onset (after-before, per-camera median) n/a mag; largest seasonal dimming 0.01 mag at MJD 58816
- dust: excess flux W1 0.22 mJy, W2 1.24 mJy, T = 436 K (16-84%: 150-659) 
- checks missing: ASAS-SN change at onset (no camera spans the onset)

### uid902493  [D2]  SURVIVOR
- position 96.96592 +5.52192; Gaia DR3 3131660633490179456; G 11.58, BP-RP 0.76, plx 2.97 mas; plot `plots/uid902493.png`
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association)
- NEOWISE: score refetch 0.35 (stored 0.35, reproduced True); dW2 0.023, dW1 -0.033, 16 visits, 121 points; baseline W1 10.00, W1-W2 0.083; onset between MJD 57662 and 57825
- detector 2: excess 0.117 mag, z 11.4, jitter ratio 5.9
- field control: target step +0.050 (W1 +0.069); neighbours N=187, median -0.006, robust sigma 0.021, max +0.117; z = 2.7
- centroid: jump at onset 0.224" +- 0.107 (2.1 sigma, PA 75); largest consecutive-visit jump 0.268"; rms 0.180"; toward neighbour: 6.7" PA70 G18.3 (angle 4 deg); 8.5" PA41 G19.7 (angle 34 deg); expected shift if a neighbour were the source: 6.7" G18.3: 0.30"; 8.5" G19.7: 0.38"
- AllWISE 2010: W1-W2 0.219, W2-W3 1.532 (W3 S/N 39.6), W3-W4 3.092 (W4 S/N 27.1), ext_flg 1, ph_qual AAAA: W3 excess only (W2-W3 > 1.0; debris-disk-like or blend)
- Gaia: RUWE 0.86, ipd_frac_multi_peak 0, NSS none, Teff 5910 K, logg 4.16, H-alpha pEW 0.172 nm, varclass none; M_G 3.94, -0.26 mag vs sequence (on the sequence); neighbours within 10": 6.7" PA70 G18.30 dG+6.72; 8.5" PA41 G19.69 dG+8.11
- SIMBAD (10"): TYC  141-925-1 [*; *,NIR] 0.37" refs=0
- ASAS-SN: 1063 points, cameras bD(g,180); bH(g,171); bd(V,177, d=+0.001); bl(g,240); bp(g,141); bt(g,154); change at onset (after-before, per-camera median) +0.001 mag; largest seasonal dimming 0.01 mag at MJD 59847
- dust: excess flux W1 0.06 mJy, W2 0.83 mJy, T = 320 K (16-84%: 150-692) 

### uid428084  [D2]  SURVIVOR
- position 0.04097 -25.32254; Gaia DR3 2335010480014243328; G 9.91, BP-RP 0.69, plx 3.39 mas; plot `plots/uid428084.png`
- flags: binary type in SIMBAD (**, CD-26 16866B) | AllWISE ext_flg = 1 (extended or 2MASS XSC association) | 1.24 mag above the main sequence at its colour | largest seasonal optical dimming 0.26 mag (MJD 59566)
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 9 visits, 87 points; baseline W1 8.09, W1-W2 0.082; onset between MJD 59538 and 59903
- detector 2: excess 0.111 mag, z 11.1, jitter ratio 7.8
- field control: target step +0.029 (W1 -0.079); neighbours N=11, median -0.014, robust sigma 0.018, max +0.006; z = 2.4
- centroid: jump at onset 0.176" +- 0.390 (0.5 sigma, PA 211); largest consecutive-visit jump 0.501"; rms 0.410"; toward neighbour: 8.4" PA191 G9.9 (angle 20 deg); expected shift if a neighbour were the source: 8.4" G9.9: 0.22"
- AllWISE 2010: W1-W2 0.116, W2-W3 -0.716 (W3 S/N 38.4), W3-W4 0.221 (W4 S/N 4.1), ext_flg 1, ph_qual AAAB: photosphere-like (W2-W3 < 0.5)
- Gaia: RUWE 1.14, ipd_frac_multi_peak 0, NSS none, Teff 6067 K, logg 3.89, H-alpha pEW 0.143 nm, varclass none; M_G 2.57, -1.24 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 8.4" PA191 G9.86 dG-0.06
- SIMBAD (10"): CD-26 16866B [*; *,**,MIR,NIR] 0.19" refs=6; CD-26 16866A [*; *,**,NIR] 8.31" refs=11
- ASAS-SN: 1289 points, cameras bG(g,250, d=-0.322); be(V,70); bg(V,174); bk(g,374, d=-0.116); bo(g,243, d=+0.228); bs(g,178, d=+0.024); change at onset (after-before, per-camera median) -0.046 mag; largest seasonal dimming 0.26 mag at MJD 59566
- dust: excess flux W1 -2.33 mJy, W2 -0.86 mJy, T = n/a K (16-84%: n/a-n/a) no W2 excess flux after onset

### uid220308  [D2]  SURVIVOR
- position 274.26638 +64.56526; Gaia DR3 2161325369818713984; G 11.45, BP-RP 0.71, plx 3.65 mas; plot `plots/uid220308.png`
- flags: AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 0.99 (stored 0.99, reproduced True); dW2 0.146, dW1 0.078, 20 visits, 2456 points; baseline W1 9.67, W1-W2 0.576; onset between MJD 57143 and 57325
- detector 2: excess 0.607 mag, z 60.7, jitter ratio 3.9
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
- detector 2: excess 0.451 mag, z 21.1, jitter ratio 5.9
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
- detector 2: excess 0.515 mag, z 18.6, jitter ratio 4.0
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
- detector 2: excess 0.312 mag, z 19.1, jitter ratio 3.5
- field control: target step +0.009 (W1 +0.002); neighbours N=73, median -0.003, robust sigma 0.019, max +0.050; z = 0.6
- centroid: jump at onset 0.045" +- 0.020 (2.3 sigma, PA 4); largest consecutive-visit jump 0.049"; rms 0.028"; toward neighbour: none; expected shift if a neighbour were the source: 4.2" G20.8: 0.03"
- AllWISE 2010: W1-W2 0.262, W2-W3 2.049 (W3 S/N 33.2), W3-W4 1.104 (W4 S/N 5.9), ext_flg 0, ph_qual AAAB: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.04, ipd_frac_multi_peak 0, NSS none, Teff 5078 K, logg 4.53, H-alpha pEW 0.016 nm, varclass SOLAR_LIKE(0.33); M_G 5.85, -0.15 mag vs sequence (on the sequence); neighbours within 10": 4.2" PA87 G20.79 dG+7.34
- SIMBAD (10"): no object
- ASAS-SN: 1269 points, cameras bH(g,335); bf(V,85); bh(V,171, d=+0.004); bl(g,388); bp(g,290); change at onset (after-before, per-camera median) +0.004 mag; largest seasonal dimming 0.02 mag at MJD 58728
- dust: excess flux W1 0.02 mJy, W2 0.02 mJy, T = 1051 K (16-84%: 150-8000) 

### uid1439035  [D2]  SURVIVOR
- position 96.02016 +12.41270; Gaia DR3 3332136920745563392; G 14.91, BP-RP 1.42, plx 2.64 mas; plot `plots/uid1439035.png`
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 10 visits, 90 points; baseline W1 12.14, W1-W2 0.166; onset between MJD 56740 and 56932
- detector 2: excess 0.228 mag, z 11.1, jitter ratio 3.7
- field control: target step -0.003 (W1 -0.010); neighbours N=173, median +0.003, robust sigma 0.016, max +0.065; z = -0.4
- centroid: jump at onset 0.184" +- 0.098 (1.9 sigma, PA 310); largest consecutive-visit jump 0.270"; rms 0.082"; toward neighbour: 7.5" PA267 G20.0 (angle 42 deg); expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.279, W2-W3 1.901 (W3 S/N 19.5), W3-W4 3.442 (W4 S/N 17.7), ext_flg 1, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 0.98, ipd_frac_multi_peak 0, NSS none, Teff 4498 K, logg 4.55, H-alpha pEW 0.134 nm, varclass none; M_G 7.02, +0.13 mag vs sequence (on the sequence); neighbours within 10": 7.5" PA267 G19.97 dG+5.06; 8.4" PA124 G16.59 dG+1.69; 8.9" PA92 G20.29 dG+5.38
- SIMBAD (10"): no object
- ASAS-SN: 995 points, cameras bC(g,220); bG(g,155); bc(V,188); bk(g,160); bo(g,137); bs(g,135); change at onset (after-before, per-camera median) n/a mag; largest seasonal dimming 0.02 mag at MJD 60654
- dust: excess flux W1 -0.03 mJy, W2 0.03 mJy, T = 150 K (16-84%: 150-633) W1 excess <= 0: colder than ~150 K (upper limit)
- checks missing: ASAS-SN change at onset (no camera spans the onset)

### uid1471333  [D2]  SURVIVOR
- position 111.14968 -44.66924; Gaia DR3 5511851313304664704; G 15.63, BP-RP 1.96, plx 2.62 mas; plot `plots/uid1471333.png`
- flags: AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | not plain dust: optical brightening -0.156 mag (per-camera -0.158,-0.173,-0.155,-0.080,-0.202,-0.122) together with the infrared rise | largest seasonal optical dimming 0.26 mag (MJD 58512)
- NEOWISE: score refetch 2.40 (stored 2.40, reproduced True); dW2 0.299, dW1 0.232, 10 visits, 123 points; baseline W1 9.62, W1-W2 0.583; onset between MJD 58579 and 59310
- detector 2: excess 0.584 mag, z 14.3, jitter ratio 11.7
- field control: target step -0.052 (W1 -0.051); neighbours N=93, median -0.002, robust sigma 0.008, max +0.326; z = -6.2
- centroid: jump at onset 0.506" +- 0.307 (1.6 sigma, PA 109); largest consecutive-visit jump 0.994"; rms 0.329"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.661, W2-W3 2.410 (W3 S/N 62.2), W3-W4 2.177 (W4 S/N 30.0), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.11, ipd_frac_multi_peak 0, NSS none, Teff 3555 K, logg 4.16, H-alpha pEW -2.334 nm, varclass none; M_G 7.72, -0.62 mag vs sequence (on the sequence); neighbours within 10": 7.1" PA331 G17.38 dG+1.75
- SIMBAD (10"): Gaia DR3 5511851313304664704 [*; *] 0.19" refs=1; Gaia DR3 5511851309005446528 [*; *] 6.95" refs=1
- ASAS-SN: 2533 points, cameras bE(g,364, d=-0.158); bF(g,354, d=-0.173); be(V,282); bf(V,215); bi(g,412, d=-0.155); bj(g,400, d=-0.080); bm(g,340, d=-0.202); bn(g,166, d=-0.122); change at onset (after-before, per-camera median) -0.156 mag; largest seasonal dimming 0.26 mag at MJD 58512
- dust: excess flux W1 13.06 mJy, W2 12.96 mJy, T = 1318 K (16-84%: 1173-1518) 

## Known/likely young stars (detector 2) (140)

### uid1355017  [D2]  YOUNG
- position 313.27661 +74.84301; Gaia DR3 2277845423082083200; G 11.98, BP-RP 1.36, plx 2.68 mas; plot `plots/uid1355017.png`
- **young:** SIMBAD young-star types Or*,Y*O (GSC 04472-00143) | Gaia DR3 variability class YSO(0.38)
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | 2.62 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 3.26 (stored 3.26, reproduced True); dW2 1.508, dW1 1.573, 21 visits, 554 points; baseline W1 9.19, W1-W2 0.519; onset between MJD 58137 and 58343
- detector 2: excess 0.582 mag, z 30.2, jitter ratio 11.2
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
- detector 2: excess 0.601 mag, z 16.0, jitter ratio 11.9
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
- detector 2: excess 0.688 mag, z 32.4, jitter ratio 28.9
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
- detector 2: excess 0.772 mag, z 20.6, jitter ratio 20.5
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
- detector 2: excess 0.481 mag, z 20.3, jitter ratio 11.2
- field control: target step +0.512 (W1 +0.427); neighbours N=43, median -0.001, robust sigma 0.008, max +0.333; z = 62.9
- centroid: jump at onset 0.024" +- 0.016 (1.5 sigma, PA 300); largest consecutive-visit jump 0.052"; rms 0.027"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.500, W2-W3 1.644 (W3 S/N 61.6), W3-W4 2.119 (W4 S/N 38.5), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.14, ipd_frac_multi_peak 0, NSS none, Teff 5850 K, logg 4.39, H-alpha pEW -2.380 nm, varclass none; M_G 6.36, -0.94 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): Kiso A-0975  47 [TT*; *,Em*,NIR,Opt,TT*,Y*?,Y*O] 0.05" refs=8
- ASAS-SN: 1303 points, cameras bB(g,85); bF(g,205); bb(V,155, d=+0.003); bf(V,171, d=-0.307); bj(g,280); bn(g,237); br(g,170); change at onset (after-before, per-camera median) -0.152 mag; largest seasonal dimming 0.36 mag at MJD 60639
- dust: excess flux W1 18.56 mJy, W2 19.39 mJy, T = 1237 K (16-84%: 1193-1284) 

### uid1673830  [D2]  YOUNG
- position 83.74308 -5.90803; Gaia DR3 3017236554330564224; G 14.95, BP-RP 2.04, plx 2.53 mas; plot `plots/uid1673830.png`
- **young:** SIMBAD young-star types Or*,TT*,Y*O (V* BX Ori) | Gaia DR3 variability class YSO(0.17)
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | 1.63 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | not plain dust: optical brightening -1.336 mag (per-camera -1.277,-0.687,-1.394,-1.482) together with the infrared rise | largest seasonal optical dimming 0.68 mag (MJD 58541)
- NEOWISE: score refetch 3.14 (stored 3.14, reproduced True); dW2 1.064, dW1 0.858, 19 visits, 180 points; baseline W1 10.68, W1-W2 0.472; onset between MJD 58899 and 59109
- detector 2: excess 0.459 mag, z 10.9, jitter ratio 16.4
- field control: target step +1.275 (W1 +1.023); neighbours N=122, median -0.002, robust sigma 0.023, max +0.147; z = 55.5
- centroid: jump at onset 0.021" +- 0.020 (1.1 sigma, PA 221); largest consecutive-visit jump 0.075"; rms 0.030"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.655, W2-W3 1.817 (W3 S/N 41.1), W3-W4 1.075 (W4 S/N 6.5), ext_flg 1, ph_qual AAAB: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.36, ipd_frac_multi_peak 0, NSS none, Teff 3676 K, logg 4.09, H-alpha pEW -0.566 nm, varclass YSO(0.17); M_G 6.96, -1.63 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): V* BX Ori [TT*; *,Em*,MIR,NIR,Opt,Or*,TT*,V*,V*?,Y*O] 0.02" refs=40
- ASAS-SN: 821 points, cameras bE(g,191, d=-1.277); ba(V,61); be(V,152); bi(g,255, d=-0.687); bm(g,95, d=-1.394); bq(g,67, d=-1.482); change at onset (after-before, per-camera median) -1.336 mag; largest seasonal dimming 0.68 mag at MJD 58541
- dust: excess flux W1 22.81 mJy, W2 26.62 mJy, T = 1094 K (16-84%: 1082-1106) 

### uid1048217  [D2]  YOUNG
- position 81.44487 +0.54828; Gaia DR3 3221844226465235712; G 14.20, BP-RP 1.79, plx 2.87 mas; plot `plots/uid1048217.png`
- **young:** SIMBAD young-star types Y*?,Y*O (UCAC4 453-010343)
- flags: 1.40 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | possible optical brightening at onset (-0.049 mag, one camera only) | largest seasonal optical dimming 0.27 mag (MJD 58182)
- NEOWISE: score refetch 1.59 (stored 1.59, reproduced True); dW2 0.919, dW1 0.692, 20 visits, 184 points; baseline W1 10.29, W1-W2 0.793; onset between MJD 57086 and 57280
- detector 2: excess 0.821 mag, z 24.3, jitter ratio 13.0
- field control: target step +0.612 (W1 +0.452); neighbours N=61, median -0.005, robust sigma 0.011, max +0.018; z = 55.5
- centroid: jump at onset 0.023" +- 0.019 (1.2 sigma, PA 274); largest consecutive-visit jump 0.095"; rms 0.038"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.778, W2-W3 2.477 (W3 S/N 73.7), W3-W4 2.487 (W4 S/N 43.5), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.08, ipd_frac_multi_peak 0, NSS none, Teff 4458 K, logg 4.29, H-alpha pEW -0.092 nm, varclass none; M_G 6.49, -1.40 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): UCAC4 453-010343 [Y*O; *,MIR,NIR,Y*?,Y*O] 0.02" refs=19
- ASAS-SN: 927 points, cameras bA(g,166); bE(g,69); ba(V,208, d=-0.049); be(V,56); bi(g,172); bm(g,158); bq(g,98); change at onset (after-before, per-camera median) -0.049 mag; largest seasonal dimming 0.27 mag at MJD 58182
- dust: excess flux W1 13.34 mJy, W2 22.40 mJy, T = 803 K (16-84%: 792-814) 

### uid1020158  [D2]  YOUNG
- position 83.83405 -0.70383; Gaia DR3 3217769470732793856; G 13.24, BP-RP 1.57, plx 2.89 mas; plot `plots/uid1020158.png`
- **young:** SIMBAD young-star types Or*,Y*?,Y*O (Haro 5-72)
- flags: 1.75 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.12 mag (MJD 59650)
- NEOWISE: score refetch 0.04 (stored 0.04, reproduced True); dW2 0.010, dW1 0.012, 20 visits, 209 points; baseline W1 9.69, W1-W2 0.277; onset between MJD 58535 and 58742
- detector 2: excess 0.332 mag, z 14.0, jitter ratio 21.9
- field control: target step +0.681 (W1 +0.569); neighbours N=89, median +0.003, robust sigma 0.013, max +0.302; z = 50.8
- centroid: jump at onset 0.028" +- 0.015 (1.9 sigma, PA 315); largest consecutive-visit jump 0.047"; rms 0.020"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.265, W2-W3 1.950 (W3 S/N 53.8), W3-W4 2.090 (W4 S/N 28.7), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.02, ipd_frac_multi_peak 0, NSS none, Teff 4610 K, logg 4.12, H-alpha pEW -0.445 nm, varclass RS(0.62); M_G 5.54, -1.75 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): Haro 5-72 [Or*; *,Em*,NIR,Or*,RS*,V*,X,Y*?,Y*O] 0.03" refs=25
- ASAS-SN: 1356 points, cameras bC(g,150, d=+0.064); bG(g,222, d=-0.003); ba(V,50); bc(V,151); be(V,38); bg(V,152); bk(g,284, d=-0.007); bo(g,170, d=-0.005); bs(g,139, d=+0.070); change at onset (after-before, per-camera median) -0.003 mag; largest seasonal dimming 0.12 mag at MJD 59650
- dust: excess flux W1 -0.37 mJy, W2 0.16 mJy, T = 150 K (16-84%: 150-150) W1 excess <= 0: colder than ~150 K (upper limit)

### uid981812  [D2]  YOUNG
- position 88.65812 +1.49762; Gaia DR3 3315789764117572224; G 13.89, BP-RP 1.67, plx 2.91 mas; plot `plots/uid981812.png`
- **young:** SIMBAD young-star types Or*,Y*O (EM* LkHA  337) | Gaia DR3 variability class YSO(0.54)
- flags: 1.35 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | optical dimming +1.226 mag after the infrared onset (debris transit signature) | largest seasonal optical dimming 1.03 mag (MJD 58152)
- NEOWISE: score refetch 3.19 (stored 3.19, reproduced True); dW2 0.968, dW1 0.820, 20 visits, 191 points; baseline W1 9.08, W1-W2 0.571; onset between MJD 57816 and 58018
- detector 2: excess 0.616 mag, z 22.0, jitter ratio 21.6
- field control: target step +0.668 (W1 +0.626); neighbours N=93, median -0.009, robust sigma 0.013, max +0.023; z = 50.7
- centroid: jump at onset 0.001" +- 0.014 (0.1 sigma, PA 80); largest consecutive-visit jump 0.086"; rms 0.035"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.605, W2-W3 2.066 (W3 S/N 72.7), W3-W4 2.138 (W4 S/N 35.1), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.40, ipd_frac_multi_peak 4, NSS none, Teff 8489 K, logg 4.49, H-alpha pEW -2.162 nm, varclass YSO(0.54); M_G 6.21, -1.35 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): EM* LkHA  337 [Or*; *,Em*,MIR,NIR,Opt,Or*,V*,Y*O,ev] 0.08" refs=20
- ASAS-SN: 1420 points, cameras bA(g,199); bB(g,39); bE(g,156); ba(V,167, d=+1.294); bb(V,173, d=+1.158); bi(g,243); bj(g,166); bm(g,129); bq(g,148); change at onset (after-before, per-camera median) +1.226 mag; largest seasonal dimming 1.03 mag at MJD 58152
- dust: excess flux W1 78.07 mJy, W2 97.53 mJy, T = 1023 K (16-84%: 987-1062) 

### uid1373972  [D2]  YOUNG
- position 82.59108 +9.92732; Gaia DR3 3338223134220001152; G 15.12, BP-RP 2.19, plx 2.67 mas; plot `plots/uid1373972.png`
- **young:** SIMBAD young-star types Y*O (2MASS J05302185+0955383)
- flags: 1.79 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.34 mag (MJD 58024)
- NEOWISE: score refetch 1.36 (stored 1.36, reproduced True); dW2 0.354, dW1 0.194, 20 visits, 224 points; baseline W1 9.33, W1-W2 0.585; onset between MJD 58377 and 58535
- detector 2: excess 0.553 mag, z 12.9, jitter ratio 14.4
- field control: target step +0.600 (W1 +0.493); neighbours N=88, median +0.000, robust sigma 0.015, max +0.155; z = 39.5
- centroid: jump at onset 0.022" +- 0.021 (1.0 sigma, PA 114); largest consecutive-visit jump 0.057"; rms 0.030"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.601, W2-W3 2.175 (W3 S/N 67.6), W3-W4 2.538 (W4 S/N 41.9), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.18, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW -0.670 nm, varclass none; M_G 7.25, -1.79 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): 2MASS J05302185+0955383 [Y*O; *,MIR,NIR,Y*O,ev] 0.06" refs=8
- ASAS-SN: 493 points, cameras bA(g,126); bE(g,58); ba(V,145); bi(g,71); bm(g,40); bq(g,53); change at onset (after-before, per-camera median) n/a mag; largest seasonal dimming 0.34 mag at MJD 58024
- dust: excess flux W1 26.91 mJy, W2 39.23 mJy, T = 894 K (16-84%: 881-906) 
- checks missing: ASAS-SN change at onset (no camera spans the onset)

### uid416674  [D2]  YOUNG
- position 63.57807 +11.97018; Gaia DR3 3304172564776041728; G 12.10, BP-RP 1.51, plx 3.41 mas; plot `plots/uid416674.png`
- **young:** SIMBAD young-star types TT? (IRAS 04114+1150)
- flags: 2.37 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.33 mag (MJD 58902)
- NEOWISE: score refetch 1.37 (stored 1.37, reproduced True); dW2 0.115, dW1 0.133, 21 visits, 196 points; baseline W1 8.97, W1-W2 0.390; onset between MJD 58515 and 58724
- detector 2: excess 0.449 mag, z 20.5, jitter ratio 7.8
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
- detector 2: excess 0.598 mag, z 16.2, jitter ratio 17.1
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

### uid1686133  [D2]  YOUNG
- position 83.38457 +10.49167; Gaia DR3 3339723830153084544; G 14.41, BP-RP 1.84, plx 2.52 mas; plot `plots/uid1686133.png`
- **young:** SIMBAD young-star types Y*?,Y*O (ZTF J053332.29+102930.0)
- flags: 1.59 mag above the main sequence at its colour | possible optical brightening at onset (-0.096 mag, one camera only)
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 21 visits, 219 points; baseline W1 9.94, W1-W2 0.376; onset between MJD 57282 and 57447
- detector 2: excess 0.397 mag, z 11.1, jitter ratio 22.6
- field control: target step +0.422 (W1 +0.304); neighbours N=111, median -0.003, robust sigma 0.013, max +0.031; z = 31.8
- centroid: jump at onset 0.012" +- 0.011 (1.1 sigma, PA 83); largest consecutive-visit jump 0.050"; rms 0.026"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.367, W2-W3 0.538 (W3 S/N 29.1), W3-W4 3.142 (W4 S/N 19.6), ext_flg 0, ph_qual AAAA: weak W3 excess (0.5 < W2-W3 < 1.0)
- Gaia: RUWE 1.10, ipd_frac_multi_peak 1, NSS none, Teff 4898 K, logg 4.22, H-alpha pEW -0.703 nm, varclass RS(0.53); M_G 6.42, -1.59 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): ZTF J053332.29+102930.0 [BY*; *,BY*,NIR,Y*?,Y*O] 0.03" refs=22
- ASAS-SN: 933 points, cameras bA(g,183); bE(g,120); ba(V,156, d=-0.096); bi(g,234); bm(g,120); bq(g,120); change at onset (after-before, per-camera median) -0.096 mag; largest seasonal dimming 0.07 mag at MJD 57065
- dust: excess flux W1 1.40 mJy, W2 1.57 mJy, T = 1139 K (16-84%: 958-1389) 

### uid835189  [D2]  YOUNG
- position 78.18641 -1.09027; Gaia DR3 3215349651798096768; G 12.98, BP-RP 1.38, plx 3.02 mas; plot `plots/uid835189.png`
- **young:** SIMBAD young-star types Y*? (UCAC4 445-008861)
- flags: 1.41 mag above the main sequence at its colour
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 18 visits, 210 points; baseline W1 10.15, W1-W2 0.187; onset between MJD 56720 and 56912
- detector 2: excess 0.250 mag, z 12.8, jitter ratio 14.4
- field control: target step +0.370 (W1 +0.233); neighbours N=56, median -0.002, robust sigma 0.012, max +0.050; z = 31.3
- centroid: jump at onset 0.021" +- 0.032 (0.7 sigma, PA 316); largest consecutive-visit jump 0.080"; rms 0.028"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.113, W2-W3 0.929 (W3 S/N 32.5), W3-W4 3.568 (W4 S/N 25.9), ext_flg 0, ph_qual AAAA: weak W3 excess (0.5 < W2-W3 < 1.0)
- Gaia: RUWE 1.25, ipd_frac_multi_peak 1, NSS none, Teff 4717 K, logg 4.17, H-alpha pEW -0.200 nm, varclass none; M_G 5.38, -1.41 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): UCAC4 445-008861 [Y*?; *,NIR,Y*?] 0.02" refs=5
- ASAS-SN: 0 points, cameras n/a; change at onset (after-before, per-camera median) n/a mag; largest seasonal dimming n/a mag at MJD n/a
- dust: excess flux W1 5.20 mJy, W2 5.28 mJy, T = 1282 K (16-84%: 1219-1350) 
- checks missing: ASAS-SN (no source)

### uid1329365  [D2]  YOUNG
- position 120.56626 -48.25475; Gaia DR3 5517611723444569984; G 13.72, BP-RP 1.58, plx 2.70 mas; plot `plots/uid1329365.png`
- **young:** SIMBAD young-star types Y*?,Y*O (Gaia DR3 5517611723444569984) | Gaia DR3 variability class YSO(0.30)
- flags: 1.43 mag above the main sequence at its colour
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 21 visits, 344 points; baseline W1 10.52, W1-W2 0.213; onset between MJD 58598 and 58806
- detector 2: excess 0.267 mag, z 11.1, jitter ratio 15.4
- field control: target step +0.275 (W1 +0.224); neighbours N=148, median -0.003, robust sigma 0.009, max +0.037; z = 31.2
- centroid: jump at onset 0.013" +- 0.013 (1.0 sigma, PA 232); largest consecutive-visit jump 0.028"; rms 0.019"; toward neighbour: none; expected shift if a neighbour were the source: 7.6" G16.2: 1.71"; 8.9" G20.5: 1.99"
- AllWISE 2010: W1-W2 0.140, W2-W3 2.398 (W3 S/N 60.4), W3-W4 2.376 (W4 S/N 32.2), ext_flg 0, ph_qual AAAA: W3 excess only (W2-W3 > 1.0; debris-disk-like or blend)
- Gaia: RUWE 1.36, ipd_frac_multi_peak 2, NSS none, Teff 4728 K, logg 4.16, H-alpha pEW -0.692 nm, varclass YSO(0.30); M_G 5.88, -1.43 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 7.6" PA353 G16.18 dG+2.46; 8.9" PA280 G20.49 dG+6.77
- SIMBAD (10"): Gaia DR3 5517611723444569984 [Y*?; *,Y*?,Y*O] 0.16" refs=5
- ASAS-SN: 0 points, cameras n/a; change at onset (after-before, per-camera median) n/a mag; largest seasonal dimming n/a mag at MJD n/a
- dust: excess flux W1 1.19 mJy, W2 0.79 mJy, T = 3082 K (16-84%: 1532-8000) 
- checks missing: ASAS-SN (no source)

### uid351866  [D2]  YOUNG
- position 79.09382 -7.94732; Gaia DR3 3207022466127209472; G 15.18, BP-RP 2.13, plx 3.48 mas; plot `plots/uid351866.png`
- **young:** SIMBAD young-star types Or*,TT*,Y*O (2MASS J05162251-0756503)
- flags: 0.97 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | optical dimming +0.202 mag after the infrared onset (debris transit signature) | largest seasonal optical dimming 0.34 mag (MJD 56920)
- NEOWISE: score refetch 3.01 (stored 3.01, reproduced True); dW2 0.238, dW1 0.260, 18 visits, 192 points; baseline W1 9.26, W1-W2 0.561; onset between MJD 58005 and 58163
- detector 2: excess 0.534 mag, z 12.4, jitter ratio 7.2
- field control: target step +0.316 (W1 +0.245); neighbours N=44, median +0.002, robust sigma 0.010, max +0.031; z = 30.3
- centroid: jump at onset 0.017" +- 0.021 (0.8 sigma, PA 165); largest consecutive-visit jump 0.034"; rms 0.031"; toward neighbour: none; expected shift if a neighbour were the source: 8.5" G21.9: 2.15"
- AllWISE 2010: W1-W2 0.538, W2-W3 1.633 (W3 S/N 61.3), W3-W4 2.380 (W4 S/N 41.2), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.20, ipd_frac_multi_peak 0, NSS none, Teff 5699 K, logg 4.50, H-alpha pEW -2.313 nm, varclass none; M_G 7.89, -0.97 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 8.5" PA250 G21.91 dG+6.73
- SIMBAD (10"): 2MASS J05162251-0756503 [TT*; *,NIR,Or*,TT*,Y*O] 0.01" refs=5
- ASAS-SN: 2460 points, cameras bB(g,74); bC(g,92); bF(g,190); bG(g,270); bb(V,133, d=+0.075); bc(V,134, d=+0.470); be(V,32); bf(V,164); bg(V,155, d=+0.279); bj(g,252); bk(g,353); bn(g,145); bo(g,220); br(g,144, d=+0.125); bs(g,102); change at onset (after-before, per-camera median) +0.202 mag; largest seasonal dimming 0.34 mag at MJD 56920
- dust: excess flux W1 16.44 mJy, W2 15.23 mJy, T = 1450 K (16-84%: 1370-1540) 

### uid1627666  [D2]  YOUNG
- position 82.51589 +12.02268; Gaia DR3 3340882749767481216; G 14.34, BP-RP 2.00, plx 2.55 mas; plot `plots/uid1627666.png`
- **young:** SIMBAD young-star types Or*,Y*O ([DM99] 113) | Gaia DR3 variability class YSO(0.34)
- flags: 2.09 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | optical dimming +0.152 mag after the infrared onset (debris transit signature) | largest seasonal optical dimming 0.26 mag (MJD 57065)
- NEOWISE: score refetch 1.04 (stored 1.04, reproduced True); dW2 0.294, dW1 0.385, 16 visits, 150 points; baseline W1 9.63, W1-W2 0.669; onset between MJD 58377 and 58534
- detector 2: excess 0.663 mag, z 16.0, jitter ratio 11.4
- field control: target step +0.482 (W1 +0.444); neighbours N=109, median -0.005, robust sigma 0.016, max +0.118; z = 29.9
- centroid: jump at onset 0.043" +- 0.034 (1.3 sigma, PA 154); largest consecutive-visit jump 0.089"; rms 0.036"; toward neighbour: none; expected shift if a neighbour were the source: 4.3" G20.2: 1.53"
- AllWISE 2010: W1-W2 0.599, W2-W3 1.999 (W3 S/N 64.4), W3-W4 1.692 (W4 S/N 26.9), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.12, ipd_frac_multi_peak 0, NSS none, Teff 5656 K, logg 4.19, H-alpha pEW -1.043 nm, varclass YSO(0.34); M_G 6.37, -2.09 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 4.3" PA300 G20.24 dG+5.90
- SIMBAD (10"): [DM99] 113 [Or*; *,Em*,LP?,NIR,Or*,Y*O] 0.02" refs=22
- ASAS-SN: 1861 points, cameras bA(g,182); bB(g,91); bD(g,197); bE(g,120); bH(g,111); ba(V,160); bd(V,170); bi(g,220, d=+0.112); bl(g,181, d=+0.045); bm(g,113); bp(g,93); bq(g,120, d=+0.193); bt(g,103, d=+0.224); change at onset (after-before, per-camera median) +0.152 mag; largest seasonal dimming 0.26 mag at MJD 57065
- dust: excess flux W1 27.53 mJy, W2 24.99 mJy, T = 1495 K (16-84%: 1450-1541) 

### uid1197713  [D2]  YOUNG
- position 81.73074 +1.67289; Gaia DR3 3222237885987655424; G 15.31, BP-RP 1.93, plx 2.77 mas; plot `plots/uid1197713.png`
- **young:** SIMBAD young-star types TT?,Y*?,Y*O (Kiso A-0903 134) | Gaia DR3 variability class YSO(0.43)
- flags: AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | not plain dust: optical brightening -0.089 mag (per-camera -0.106,-0.180,-0.059,-0.089,-0.016) together with the infrared rise
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 21 visits, 223 points; baseline W1 10.61, W1-W2 0.417; onset between MJD 58740 and 58898
- detector 2: excess 0.424 mag, z 11.0, jitter ratio 11.6
- field control: target step +0.347 (W1 +0.244); neighbours N=87, median -0.001, robust sigma 0.012, max +0.040; z = 29.3
- centroid: jump at onset 0.063" +- 0.021 (3.0 sigma, PA 247); largest consecutive-visit jump 0.118"; rms 0.034"; toward neighbour: none; expected shift if a neighbour were the source: 6.9" G16.1: 1.88"
- AllWISE 2010: W1-W2 0.438, W2-W3 1.512 (W3 S/N 44.8), W3-W4 2.529 (W4 S/N 23.1), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.11, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW -2.490 nm, varclass YSO(0.43); M_G 7.53, -0.72 mag vs sequence (on the sequence); neighbours within 10": 6.9" PA96 G16.12 dG+0.81
- SIMBAD (10"): Kiso A-0903 134 [Y*O; *,Em*,IR,MIR,NIR,TT?,V*,Y*?,Y*O] 0.03" refs=31
- ASAS-SN: 1215 points, cameras bA(g,168, d=-0.106); bE(g,177, d=-0.180); ba(V,210); be(V,56); bi(g,284, d=-0.059); bm(g,193, d=-0.089); bq(g,127, d=-0.016); change at onset (after-before, per-camera median) -0.089 mag; largest seasonal dimming 0.09 mag at MJD 58880
- dust: excess flux W1 -0.07 mJy, W2 0.19 mJy, T = 150 K (16-84%: 150-588) W1 excess <= 0: colder than ~150 K (upper limit)

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

### uid1435805  [D2]  YOUNG
- position 80.47611 -2.29051; Gaia DR3 3214120329078892544; G 14.37, BP-RP 1.78, plx 2.64 mas; plot `plots/uid1435805.png`
- **young:** SIMBAD young-star types TT*,Y*?,Y*O (CVSO 504)
- flags: centroid jump 0.061" (3.0 sigma, PA 337) away from the neighbour(s) 6.5" PA153 G15.4, as expected when the target itself brightens in a blended WISE PSF | AllWISE ext_flg = 1 (extended or 2MASS XSC association) | 1.39 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | not plain dust: optical brightening -0.249 mag (per-camera -0.398,-0.099) together with the infrared rise | largest seasonal optical dimming 0.46 mag (MJD 59787)
- NEOWISE: score refetch 2.18 (stored 2.19, reproduced True); dW2 0.214, dW1 0.194, 21 visits, 229 points; baseline W1 9.33, W1-W2 0.368; onset between MJD 57808 and 58007
- detector 2: excess 0.397 mag, z 12.0, jitter ratio 9.6
- field control: target step +0.273 (W1 +0.271); neighbours N=53, median -0.005, robust sigma 0.010, max +0.037; z = 28.9
- centroid: jump at onset 0.061" +- 0.020 (3.0 sigma, PA 337); largest consecutive-visit jump 0.090"; rms 0.041"; toward neighbour: none; expected shift if a neighbour were the source: 6.5" G15.4: 1.45"
- AllWISE 2010: W1-W2 0.413, W2-W3 1.292 (W3 S/N 58.7), W3-W4 2.225 (W4 S/N 30.3), ext_flg 1, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.23, ipd_frac_multi_peak 1, NSS none, Teff nan K, logg nan, H-alpha pEW -1.026 nm, varclass none; M_G 6.48, -1.39 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 6.5" PA153 G15.45 dG+1.08
- SIMBAD (10"): CVSO 504 [TT*; *,NIR,TT*,Y*?,Y*O] 0.02" refs=10; Gaia DR3 3214120329078892800 [Y*?; *,Y*?] 6.48" refs=3
- ASAS-SN: 1482 points, cameras bD(g,160); bH(g,205); bb(V,55); bd(V,156, d=-0.398); bf(V,40); bh(V,152, d=-0.099); bl(g,326); bp(g,216); bt(g,172); change at onset (after-before, per-camera median) -0.249 mag; largest seasonal dimming 0.46 mag at MJD 59787
- dust: excess flux W1 13.82 mJy, W2 12.07 mJy, T = 1587 K (16-84%: 1478-1712) 

### uid1515886  [D2]  YOUNG
- position 83.25734 -4.82182; Gaia DR3 3209608723634530944; G 15.54, BP-RP 1.40, plx 2.60 mas; plot `plots/uid1515886.png`
- **young:** SIMBAD young-star types Or*,Y*O (V* HS Ori) | Gaia DR3 variability class YSO(0.36)
- flags: AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.20 mag (MJD 59251)
- NEOWISE: score refetch 1.29 (stored 1.29, reproduced True); dW2 0.244, dW1 0.173, 20 visits, 183 points; baseline W1 10.52, W1-W2 0.830; onset between MJD 59108 and 59263
- detector 2: excess 0.893 mag, z 44.7, jitter ratio 14.9
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
- detector 2: excess 0.411 mag, z 23.1, jitter ratio 21.3
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
- detector 2: excess 0.348 mag, z 14.8, jitter ratio 6.9
- field control: target step +0.243 (W1 +0.193); neighbours N=144, median -0.006, robust sigma 0.009, max +0.051; z = 27.9
- centroid: jump at onset 0.006" +- 0.012 (0.5 sigma, PA 141); largest consecutive-visit jump 0.026"; rms 0.027"; toward neighbour: none; expected shift if a neighbour were the source: 4.1" G20.6: 0.81"; 8.6" G16.2: 1.73"
- AllWISE 2010: W1-W2 0.297, W2-W3 1.884 (W3 S/N 56.8), W3-W4 1.977 (W4 S/N 24.0), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.05, ipd_frac_multi_peak 0, NSS none, Teff 4700 K, logg 4.15, H-alpha pEW -0.515 nm, varclass YSO(0.16); M_G 5.81, -1.47 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 4.1" PA213 G20.58 dG+6.82; 8.6" PA21 G16.21 dG+2.45
- SIMBAD (10"): UCAC4 223-017496 [Y*?; *,NIR,Y*?,Y*O] 0.17" refs=8
- ASAS-SN: 1390 points, cameras bE(g,423); be(V,231); bi(g,525); bm(g,211); change at onset (after-before, per-camera median) n/a mag; largest seasonal dimming 0.04 mag at MJD 60458
- dust: excess flux W1 3.97 mJy, W2 4.15 mJy, T = 1236 K (16-84%: 1156-1327) 
- checks missing: ASAS-SN change at onset (no camera spans the onset)

### uid869353  [D2]  YOUNG
- position 77.24052 -1.48782; Gaia DR3 3214993066432968448; G 14.96, BP-RP 2.19, plx 2.99 mas; plot `plots/uid869353.png`
- **young:** SIMBAD young-star types TT*,Y*?,Y*O (Kiso A-0902   3) | Gaia DR3 variability class YSO(0.36)
- flags: 1.69 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.16 mag (MJD 59811)
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 21 visits, 221 points; baseline W1 10.27, W1-W2 0.489; onset between MJD 59257 and 59466
- detector 2: excess 0.457 mag, z 10.6, jitter ratio 26.5
- field control: target step +0.308 (W1 +0.257); neighbours N=49, median -0.002, robust sigma 0.012, max +0.030; z = 26.2
- centroid: jump at onset 0.005" +- 0.017 (0.3 sigma, PA 117); largest consecutive-visit jump 0.065"; rms 0.031"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.537, W2-W3 1.770 (W3 S/N 52.3), W3-W4 1.565 (W4 S/N 15.4), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.21, ipd_frac_multi_peak 0, NSS none, Teff 3644 K, logg 4.05, H-alpha pEW -0.315 nm, varclass YSO(0.36); M_G 7.34, -1.69 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): Kiso A-0902   3 [TT*; *,Em*,MIR,NIR,RS*,TT*,Y*?,Y*O] 0.03" refs=11
- ASAS-SN: 1308 points, cameras bC(g,174, d=+0.021); bG(g,194, d=+0.025); bc(V,119); be(V,39); bg(V,184); bk(g,273, d=-0.040); bo(g,203, d=+0.146); bs(g,122, d=+0.142); change at onset (after-before, per-camera median) +0.025 mag; largest seasonal dimming 0.16 mag at MJD 59811
- dust: excess flux W1 1.15 mJy, W2 1.09 mJy, T = 1398 K (16-84%: 1156-1788) 

### uid1159910  [D2]  YOUNG
- position 79.80651 -3.40349; Gaia DR3 3213527348713890560; G 12.21, BP-RP 1.28, plx 2.80 mas; plot `plots/uid1159910.png`
- **young:** SIMBAD young-star types Or*,TT*,Y*?,Y*O (Kiso A-0975  45)
- flags: 2.03 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | not plain dust: optical brightening -0.047 mag (per-camera -0.068,-0.026) together with the infrared rise | largest seasonal optical dimming 0.11 mag (MJD 60503)
- NEOWISE: score refetch 1.53 (stored 1.53, reproduced True); dW2 0.354, dW1 0.287, 20 visits, 177 points; baseline W1 8.61, W1-W2 0.421; onset between MJD 57807 and 58006
- detector 2: excess 0.483 mag, z 27.0, jitter ratio 18.4
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
- detector 2: excess 0.380 mag, z 14.0, jitter ratio 13.9
- field control: target step +0.188 (W1 +0.309); neighbours N=131, median -0.003, robust sigma 0.007, max +0.021; z = 25.8
- centroid: jump at onset 0.007" +- 0.013 (0.5 sigma, PA 257); largest consecutive-visit jump 0.044"; rms 0.021"; toward neighbour: none; expected shift if a neighbour were the source: 1.0" G16.6: 0.17"; 8.2" G20.2: 1.31"
- AllWISE 2010: W1-W2 0.353, W2-W3 2.117 (W3 S/N 68.3), W3-W4 1.842 (W4 S/N 40.7), ext_flg 1, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.24, ipd_frac_multi_peak 41, NSS none, Teff 5090 K, logg 4.14, H-alpha pEW -0.651 nm, varclass none; M_G 5.56, -1.92 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 1.0" PA140 G16.57 dG+3.26; 8.2" PA121 G20.19 dG+6.88
- SIMBAD (10"): Gaia DR3 5512928765979700352 [Y*?; *,Y*?,Y*O] 0.17" refs=4; 1RXS J080230.9-514903 [X; X] 3.31" refs=0
- ASAS-SN: 0 points, cameras n/a; change at onset (after-before, per-camera median) n/a mag; largest seasonal dimming n/a mag at MJD n/a
- dust: excess flux W1 13.80 mJy, W2 10.22 mJy, T = 2212 K (16-84%: 2024-2443) 
- checks missing: ASAS-SN (no source)

### uid1598653  [D2]  YOUNG
- position 83.63212 -3.86423; Gaia DR3 3215872396561733504; G 12.34, BP-RP 1.49, plx 2.56 mas; plot `plots/uid1598653.png`
- **young:** SIMBAD young-star types Y*O (2MASS J05343170-0351513) | Gaia DR3 variability class YSO(0.35)
- flags: 2.69 mag above the main sequence at its colour
- NEOWISE: score refetch 0.39 (stored 0.39, reproduced True); dW2 0.084, dW1 0.058, 21 visits, 206 points; baseline W1 9.16, W1-W2 0.214; onset between MJD 57087 and 57282
- detector 2: excess 0.274 mag, z 13.0, jitter ratio 17.2
- field control: target step +0.319 (W1 +0.229); neighbours N=65, median -0.006, robust sigma 0.013, max +0.064; z = 25.8
- centroid: jump at onset 0.007" +- 0.014 (0.5 sigma, PA 335); largest consecutive-visit jump 0.046"; rms 0.025"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.203, W2-W3 1.297 (W3 S/N 48.5), W3-W4 2.065 (W4 S/N 17.1), ext_flg 0, ph_qual AAAA: W3 excess only (W2-W3 > 1.0; debris-disk-like or blend)
- Gaia: RUWE 1.15, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW -0.111 nm, varclass YSO(0.35); M_G 4.39, -2.69 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): 2MASS J05343170-0351513 [Y*O; *,MIR,NIR,Y*O] 0.07" refs=7
- ASAS-SN: 2649 points, cameras bC(g,154); bE(g,220); bG(g,222); ba(V,79); bc(V,148, d=-0.001); be(V,233, d=+0.022); bg(V,153); bi(g,338); bk(g,307); bm(g,248); bo(g,220); bq(g,163); bs(g,164); change at onset (after-before, per-camera median) +0.011 mag; largest seasonal dimming 0.07 mag at MJD 60655
- dust: excess flux W1 4.96 mJy, W2 4.83 mJy, T = 1354 K (16-84%: 1174-1592) 

### uid1061853  [D2]  YOUNG
- position 84.80421 -1.45591; Gaia DR3 3217423674325646208; G 13.13, BP-RP 1.54, plx 2.86 mas; plot `plots/uid1061853.png`
- **young:** SIMBAD young-star types Or*,Y*?,Y*O (Haro 5-17)
- flags: 1.79 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.11 mag (MJD 58484)
- NEOWISE: score refetch 3.34 (stored 3.34, reproduced True); dW2 0.397, dW1 0.418, 20 visits, 207 points; baseline W1 9.32, W1-W2 0.547; onset between MJD 57283 and 57448
- detector 2: excess 0.604 mag, z 26.6, jitter ratio 11.6
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
- detector 2: excess 0.632 mag, z 14.7, jitter ratio 21.2
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
- detector 2: excess 0.701 mag, z 36.4, jitter ratio 13.3
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
- detector 2: excess 0.479 mag, z 35.7, jitter ratio 13.9
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
- detector 2: excess 0.549 mag, z 15.5, jitter ratio 17.1
- field control: target step +0.393 (W1 +0.126); neighbours N=103, median +0.000, robust sigma 0.016, max +0.193; z = 24.1
- centroid: jump at onset 0.028" +- 0.029 (1.0 sigma, PA 215); largest consecutive-visit jump 0.073"; rms 0.039"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.607, W2-W3 2.800 (W3 S/N 48.0), W3-W4 1.623 (W4 S/N 30.7), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.01, ipd_frac_multi_peak 1, NSS none, Teff 4714 K, logg 4.18, H-alpha pEW -0.513 nm, varclass YSO(0.25); M_G 6.36, -1.61 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): V* V1416 Ori [TT*; *,MIR,NIR,Or*,TT*,V*,Y*?,Y*O] 0.02" refs=39
- ASAS-SN: 1503 points, cameras bA(g,156, d=-0.042); bE(g,219, d=-0.005); ba(V,179); be(V,195); bi(g,340, d=-0.055); bm(g,246, d=-0.032); bq(g,168, d=-0.065); change at onset (after-before, per-camera median) -0.042 mag; largest seasonal dimming 0.05 mag at MJD 60235
- dust: excess flux W1 4.03 mJy, W2 7.45 mJy, T = 751 K (16-84%: 735-767) 

### uid1315434  [D2]  YOUNG
- position 82.70000 -7.52567; Gaia DR3 3016413501156518400; G 14.29, BP-RP 1.79, plx 2.71 mas; plot `plots/uid1315434.png`
- **young:** SIMBAD young-star types Y*?,Y*O (2MASS J05304799-0731323)
- flags: 1.44 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | not plain dust: optical brightening -0.065 mag (per-camera -0.103,-0.028) together with the infrared rise
- NEOWISE: score refetch 1.02 (stored 1.01, reproduced True); dW2 0.194, dW1 0.206, 20 visits, 214 points; baseline W1 10.60, W1-W2 0.332; onset between MJD 57445 and 57645
- detector 2: excess 0.360 mag, z 10.7, jitter ratio 15.3
- field control: target step +0.240 (W1 +0.087); neighbours N=66, median -0.003, robust sigma 0.011, max +0.023; z = 22.6
- centroid: jump at onset 0.017" +- 0.015 (1.2 sigma, PA 249); largest consecutive-visit jump 0.045"; rms 0.035"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.315, W2-W3 2.277 (W3 S/N 53.9), W3-W4 1.561 (W4 S/N 15.2), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.18, ipd_frac_multi_peak 0, NSS none, Teff 4448 K, logg 4.15, H-alpha pEW -0.107 nm, varclass none; M_G 6.45, -1.44 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): 2MASS J05304799-0731323 [Y*O; *,NIR,Y*?,Y*O] 0.01" refs=7
- ASAS-SN: 1515 points, cameras bA(g,158); bE(g,220); ba(V,179, d=-0.103); be(V,195, d=-0.028); bi(g,345); bm(g,247); bq(g,171); change at onset (after-before, per-camera median) -0.065 mag; largest seasonal dimming 0.09 mag at MJD 59496
- dust: excess flux W1 0.78 mJy, W2 2.51 mJy, T = 551 K (16-84%: 510-594) 

### uid1499154  [D2]  YOUNG
- position 84.22543 -2.88770; Gaia DR3 3216079899317606272; G 12.91, BP-RP 1.39, plx 2.61 mas; plot `plots/uid1499154.png`
- **young:** SIMBAD young-star types Or*,Y*O (V* V2715 Ori) | Gaia DR3 variability class YSO(0.65)
- flags: 1.80 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 0.13 (stored 0.14, reproduced True); dW2 0.021, dW1 0.030, 21 visits, 206 points; baseline W1 9.52, W1-W2 0.302; onset between MJD 60205 and 60362
- detector 2: excess 0.365 mag, z 18.6, jitter ratio 15.1
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
- detector 2: excess 0.607 mag, z 37.2, jitter ratio 7.3
- field control: target step +0.167 (W1 +0.102); neighbours N=119, median +0.004, robust sigma 0.007, max +0.039; z = 22.0
- centroid: jump at onset 0.014" +- 0.015 (0.9 sigma, PA 338); largest consecutive-visit jump 0.058"; rms 0.025"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.497, W2-W3 2.472 (W3 S/N 79.2), W3-W4 1.931 (W4 S/N 63.2), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 0.80, ipd_frac_multi_peak 0, NSS none, Teff 5633 K, logg 3.99, H-alpha pEW -0.194 nm, varclass YSO(0.20); M_G 3.54, -2.40 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): TYC 4467-324-1 [Or*; *,IR,NIR,Or*,Y*O] 0.09" refs=11
- ASAS-SN: 822 points, cameras bD(g,359, d=-0.043); bd(V,187); bt(g,276, d=-0.024); change at onset (after-before, per-camera median) -0.033 mag; largest seasonal dimming 0.09 mag at MJD 59917
- dust: excess flux W1 2.35 mJy, W2 5.39 mJy, T = 658 K (16-84%: 518-833) 

### uid1661343  [D2]  YOUNG
- position 84.85502 -2.63946; Gaia DR3 3216439847641330816; G 13.95, BP-RP 1.90, plx 2.53 mas; plot `plots/uid1661343.png`
- **young:** SIMBAD young-star types Or*,TT*,Y*O (V* BG Ori)
- flags: 2.21 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 3.46 (stored 3.46, reproduced True); dW2 0.301, dW1 0.245, 21 visits, 218 points; baseline W1 9.52, W1-W2 0.451; onset between MJD 57089 and 57283
- detector 2: excess 0.462 mag, z 12.2, jitter ratio 8.3
- field control: target step +0.341 (W1 +0.327); neighbours N=120, median -0.005, robust sigma 0.016, max +0.183; z = 21.2
- centroid: jump at onset 0.015" +- 0.011 (1.4 sigma, PA 277); largest consecutive-visit jump 0.037"; rms 0.026"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.431, W2-W3 1.936 (W3 S/N 67.5), W3-W4 2.139 (W4 S/N 36.1), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.19, ipd_frac_multi_peak 0, NSS none, Teff 5919 K, logg 4.12, H-alpha pEW -1.779 nm, varclass none; M_G 5.97, -2.21 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): V* BG Ori [TT*; *,Em*,NIR,Or*,TT*,V*,V*?,Y*O] 0.03" refs=49
- ASAS-SN: 1357 points, cameras bC(g,143); bG(g,221); bc(V,151, d=+0.043); be(V,38, d=+0.052); bg(V,153); bk(g,304); bo(g,189); bs(g,158); change at onset (after-before, per-camera median) +0.048 mag; largest seasonal dimming 0.10 mag at MJD 57759
- dust: excess flux W1 15.52 mJy, W2 13.01 mJy, T = 1705 K (16-84%: 1605-1818) 

### uid1565709  [D2]  YOUNG
- position 82.65033 +12.11127; Gaia DR3 3340889106319040896; G 15.94, BP-RP 2.16, plx 2.58 mas; plot `plots/uid1565709.png`
- **young:** SIMBAD young-star types Or*,Y*O (Haro 6-51)
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | 0.97 mag above the main sequence at its colour | largest seasonal optical dimming 0.16 mag (MJD 58869)
- NEOWISE: score refetch 1.06 (stored 1.06, reproduced True); dW2 0.288, dW1 0.281, 18 visits, 157 points; baseline W1 11.10, W1-W2 0.486; onset between MJD 57087 and 57282
- detector 2: excess 0.455 mag, z 10.6, jitter ratio 15.2
- field control: target step +0.290 (W1 +0.337); neighbours N=115, median -0.005, robust sigma 0.014, max +0.632; z = 20.9
- centroid: jump at onset 0.014" +- 0.020 (0.7 sigma, PA 52); largest consecutive-visit jump 0.050"; rms 0.032"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.620, W2-W3 0.418 (W3 S/N 13.6), W3-W4 2.609 (W4 S/N 8.6), ext_flg 1, ph_qual AAAB: photosphere-like (W2-W3 < 0.5)
- Gaia: RUWE 1.08, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW -6.993 nm, varclass none; M_G 7.99, -0.97 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): Haro 6-51 [Or*; *,Em*,NIR,Or*,V*,V*?,Y*O] 0.01" refs=21
- ASAS-SN: 771 points, cameras bA(g,108); bD(g,124); bE(g,46); bH(g,64); ba(V,106, d=+0.066); bd(V,124, d=-0.118); bl(g,76); bp(g,33); bq(g,29); bt(g,61); change at onset (after-before, per-camera median) -0.026 mag; largest seasonal dimming 0.16 mag at MJD 58869
- dust: excess flux W1 3.85 mJy, W2 2.76 mJy, T = 2409 K (16-84%: 2149-2739) 

### uid1020396  [D2]  YOUNG
- position 77.87678 +10.53859; Gaia DR3 3387012794470089344; G 13.41, BP-RP 1.76, plx 2.89 mas; plot `plots/uid1020396.png`
- **young:** SIMBAD young-star types Y*?,Y*O (PEP 12)
- flags: 2.06 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 21 visits, 205 points; baseline W1 9.32, W1-W2 0.447; onset between MJD 57806 and 58005
- detector 2: excess 0.481 mag, z 15.0, jitter ratio 5.9
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
- detector 2: excess 0.502 mag, z 23.7, jitter ratio 21.4
- field control: target step +0.312 (W1 +0.324); neighbours N=44, median +0.001, robust sigma 0.015, max +0.029; z = 20.5
- centroid: jump at onset 0.011" +- 0.018 (0.6 sigma, PA 19); largest consecutive-visit jump 0.038"; rms 0.034"; toward neighbour: none; expected shift if a neighbour were the source: 6.5" G20.2: 1.63"
- AllWISE 2010: W1-W2 0.446, W2-W3 2.243 (W3 S/N 64.4), W3-W4 2.238 (W4 S/N 36.9), ext_flg 1, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.12, ipd_frac_multi_peak 0, NSS none, Teff 5684 K, logg 4.33, H-alpha pEW -4.057 nm, varclass YSO(0.50); M_G 6.00, -1.08 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 6.5" PA299 G20.25 dG+6.57
- SIMBAD (10"): Kiso A-0975   7 [TT*; *,Em*,NIR,TT*,Y*?,Y*O] 0.02" refs=8
- ASAS-SN: 2587 points, cameras bB(g,88); bC(g,177); bF(g,205); bG(g,210); ba(V,35); bb(V,155, d=-0.026); bc(V,115, d=-0.033); be(V,40); bg(V,187, d=-0.134); bj(g,270); bk(g,297); bn(g,239); bo(g,237); br(g,170); bs(g,162); change at onset (after-before, per-camera median) -0.033 mag; largest seasonal dimming 0.11 mag at MJD 60341
- dust: excess flux W1 6.78 mJy, W2 5.92 mJy, T = 1591 K (16-84%: 1425-1803) 

### uid1238823  [D2]  YOUNG
- position 326.13460 +70.13699; Gaia DR3 2224123461044918784; G 13.96, BP-RP 1.80, plx 2.75 mas; plot `plots/uid1238823.png`
- **young:** SIMBAD young-star types Or*,Y*? (GSC 04466-01532) | Gaia DR3 variability class YSO(0.64)
- flags: 1.75 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 0.70 (stored 0.70, reproduced True); dW2 0.052, dW1 0.131, 21 visits, 520 points; baseline W1 10.06, W1-W2 0.330; onset between MJD 57598 and 57766
- detector 2: excess 0.357 mag, z 10.4, jitter ratio 5.9
- field control: target step +0.118 (W1 +0.113); neighbours N=109, median -0.003, robust sigma 0.006, max +0.086; z = 20.5
- centroid: jump at onset 0.015" +- 0.014 (1.1 sigma, PA 88); largest consecutive-visit jump 0.045"; rms 0.021"; toward neighbour: none; expected shift if a neighbour were the source: 1.5" G18.6: 0.15"
- AllWISE 2010: W1-W2 0.276, W2-W3 1.959 (W3 S/N 55.2), W3-W4 2.827 (W4 S/N 37.9), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.12, ipd_frac_multi_peak 1, NSS none, Teff 5653 K, logg 4.21, H-alpha pEW -2.601 nm, varclass YSO(0.64); M_G 6.16, -1.75 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 1.5" PA306 G18.65 dG+4.69
- SIMBAD (10"): GSC 04466-01532 [Or*; *,Em*,NIR,Or*,Y*?] 0.07" refs=6
- ASAS-SN: 1698 points, cameras bC(g,398); bD(g,357); bc(V,189, d=-0.039); bd(V,187, d=+0.008); bs(g,290); bt(g,277); change at onset (after-before, per-camera median) -0.015 mag; largest seasonal dimming 0.07 mag at MJD 59834
- dust: excess flux W1 3.26 mJy, W2 2.00 mJy, T = 4588 K (16-84%: 2914-8000) 

### uid983581  [D2]  YOUNG
- position 334.75724 +73.76869; Gaia DR3 2279007370651605888; G 14.01, BP-RP 1.83, plx 2.91 mas; plot `plots/uid983581.png`
- **young:** SIMBAD young-star types Or*,Y*?,Y*O ([K98c] Em* 109) | Gaia DR3 variability class YSO(0.79)
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | 1.64 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.17 mag (MJD 59886)
- NEOWISE: score refetch 0.18 (stored 0.18, reproduced True); dW2 0.021, dW1 0.020, 21 visits, 421 points; baseline W1 9.46, W1-W2 0.417; onset between MJD 58865 and 59069
- detector 2: excess 0.440 mag, z 12.4, jitter ratio 11.5
- field control: target step +0.204 (W1 +0.194); neighbours N=103, median -0.002, robust sigma 0.010, max +0.102; z = 19.8
- centroid: jump at onset 0.031" +- 0.017 (1.8 sigma, PA 114); largest consecutive-visit jump 0.080"; rms 0.026"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.458, W2-W3 1.770 (W3 S/N 63.6), W3-W4 1.992 (W4 S/N 29.1), ext_flg 1, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.16, ipd_frac_multi_peak 0, NSS none, Teff 4972 K, logg 4.20, H-alpha pEW -2.262 nm, varclass YSO(0.79); M_G 6.33, -1.64 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): [K98c] Em* 109 [Or*; *,Em*,LP*,NIR,Or*,Y*?,Y*O] 0.09" refs=11
- ASAS-SN: 1366 points, cameras bA(g,331, d=+0.014); bB(g,110, d=+0.027); ba(V,250); bb(V,163); bq(g,261, d=-0.042); br(g,251, d=-0.010); change at onset (after-before, per-camera median) +0.002 mag; largest seasonal dimming 0.17 mag at MJD 59886
- dust: excess flux W1 -0.24 mJy, W2 0.22 mJy, T = 150 K (16-84%: 150-531) W1 excess <= 0: colder than ~150 K (upper limit)

### uid1508362  [D2]  YOUNG
- position 85.55729 +8.73234; Gaia DR3 3336066717040247040; G 14.29, BP-RP 1.88, plx 2.60 mas; plot `plots/uid1508362.png`
- **young:** SIMBAD young-star types Y*?,Y*O (V* V516 Ori)
- flags: 1.75 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.18 mag (MJD 60644)
- NEOWISE: score refetch 1.15 (stored 1.15, reproduced True); dW2 0.174, dW1 0.093, 21 visits, 186 points; baseline W1 10.07, W1-W2 0.399; onset between MJD 58170 and 58380
- detector 2: excess 0.414 mag, z 11.1, jitter ratio 12.9
- field control: target step +0.227 (W1 +0.207); neighbours N=103, median -0.003, robust sigma 0.012, max +0.026; z = 19.4
- centroid: jump at onset 0.031" +- 0.023 (1.4 sigma, PA 32); largest consecutive-visit jump 0.078"; rms 0.034"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.314, W2-W3 2.404 (W3 S/N 74.6), W3-W4 2.268 (W4 S/N 41.2), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.12, ipd_frac_multi_peak 0, NSS none, Teff 5983 K, logg 4.25, H-alpha pEW -1.354 nm, varclass none; M_G 6.37, -1.75 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): V* V516 Ori [Y*O; *,Em*,LP*,LP?,MIR,NIR,V*,Y*?,Y*O] 0.06" refs=29
- ASAS-SN: 939 points, cameras bA(g,183); bE(g,120); ba(V,156, d=-0.019); bi(g,236); bm(g,122); bq(g,122); change at onset (after-before, per-camera median) -0.019 mag; largest seasonal dimming 0.18 mag at MJD 60644
- dust: excess flux W1 3.80 mJy, W2 4.71 mJy, T = 1031 K (16-84%: 974-1093) 

### uid1284783  [D2]  YOUNG
- position 84.61071 -2.20486; Gaia DR3 3216517706809394560; G 15.39, BP-RP 1.86, plx 2.72 mas; plot `plots/uid1284783.png`
- **young:** SIMBAD young-star types Or*,TT*,Y*O (V* V2730 Ori) | Gaia DR3 variability class YSO(0.53)
- flags: AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | possible optical brightening at onset (-1.124 mag, one camera only) | largest seasonal optical dimming 0.55 mag (MJD 57022)
- NEOWISE: score refetch 2.22 (stored 2.22, reproduced True); dW2 0.328, dW1 0.133, 21 visits, 218 points; baseline W1 10.33, W1-W2 0.513; onset between MJD 57089 and 57283
- detector 2: excess 0.530 mag, z 14.5, jitter ratio 13.9
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
- detector 2: excess 0.549 mag, z 26.5, jitter ratio 13.7
- field control: target step +0.213 (W1 +0.233); neighbours N=188, median -0.005, robust sigma 0.011, max +0.028; z = 19.0
- centroid: jump at onset 0.012" +- 0.013 (1.0 sigma, PA 357); largest consecutive-visit jump 0.059"; rms 0.028"; toward neighbour: none; expected shift if a neighbour were the source: 3.1" G20.5: 0.55"; 6.1" G17.7: 1.09"; 7.2" G18.3: 1.28"; 8.0" G19.4: 1.42"; 8.2" G17.3: 1.46"
- AllWISE 2010: W1-W2 0.563, W2-W3 1.994 (W3 S/N 76.8), W3-W4 1.711 (W4 S/N 42.8), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.33, ipd_frac_multi_peak 0, NSS none, Teff 5803 K, logg 4.34, H-alpha pEW -1.905 nm, varclass YSO(0.03); M_G 5.81, -1.09 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 3.1" PA75 G20.50 dG+6.95; 6.1" PA224 G17.71 dG+4.15; 7.2" PA45 G18.29 dG+4.73; 8.0" PA127 G19.35 dG+5.80; 8.2" PA109 G17.26 dG+3.70
- SIMBAD (10"): WRAY 15-218 [Em*; *,Em*,NIR,Y*?,Y*O] 0.21" refs=8
- ASAS-SN: 1336 points, cameras bG(g,443); bg(V,239); bk(g,464); bo(g,190); change at onset (after-before, per-camera median) n/a mag; largest seasonal dimming 0.20 mag at MJD 60439
- dust: excess flux W1 8.82 mJy, W2 9.58 mJy, T = 1183 K (16-84%: 1056-1339) 
- checks missing: ASAS-SN change at onset (no camera spans the onset)

### uid1374460  [D2]  YOUNG
- position 83.85204 -6.02956; Gaia DR3 3017184808564584192; G 15.97, BP-RP 1.83, plx 2.67 mas; plot `plots/uid1374460.png`
- **young:** SIMBAD young-star types Or*,TT*,Y*O (V* NS Ori)
- flags: AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.25 mag (MJD 57044)
- NEOWISE: score refetch 3.00 (stored 3.00, reproduced True); dW2 0.564, dW1 0.465, 19 visits, 172 points; baseline W1 11.21, W1-W2 0.566; onset between MJD 57088 and 57447
- detector 2: excess 0.588 mag, z 16.5, jitter ratio 9.6
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
- detector 2: excess 0.374 mag, z 15.7, jitter ratio 7.2
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
- detector 2: excess 0.325 mag, z 15.6, jitter ratio 14.8
- field control: target step +0.189 (W1 +0.189); neighbours N=51, median -0.001, robust sigma 0.010, max +0.091; z = 18.4
- centroid: jump at onset 0.017" +- 0.018 (0.9 sigma, PA 267); largest consecutive-visit jump 0.040"; rms 0.028"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.293, W2-W3 2.464 (W3 S/N 76.3), W3-W4 2.564 (W4 S/N 49.5), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.05, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW -0.519 nm, varclass RS(0.53); M_G 4.69, -2.25 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): IRAS 05117-0142 [Y*O; *,IR,NIR,Y*?,Y*O] 0.05" refs=7
- ASAS-SN: 2647 points, cameras bC(g,183); bD(g,166); bG(g,211); bH(g,206); bc(V,119, d=+0.055); be(V,40); bg(V,185, d=+0.030); bh(V,152, d=+0.032); bk(g,298); bl(g,323); bo(g,233); bp(g,213); bs(g,143); bt(g,175); change at onset (after-before, per-camera median) +0.032 mag; largest seasonal dimming 0.03 mag at MJD 59282
- dust: excess flux W1 15.81 mJy, W2 10.53 mJy, T = 3066 K (16-84%: 2490-4061) 

### uid1477549  [D2]  YOUNG
- position 82.07155 -7.61818; Gaia DR3 3015083779282240256; G 14.58, BP-RP 1.90, plx 2.62 mas; plot `plots/uid1477549.png`
- **young:** SIMBAD young-star types Y*?,Y*O (Haro 4-260) | Gaia DR3 variability class YSO(0.12)
- flags: 1.49 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | optical dimming +0.078 mag after the infrared onset (debris transit signature) | largest seasonal optical dimming 0.34 mag (MJD 57621)
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 16 visits, 194 points; baseline W1 9.19, W1-W2 0.524; onset between MJD 56918 and 57086
- detector 2: excess 0.536 mag, z 14.2, jitter ratio 17.6
- field control: target step +0.234 (W1 +0.246); neighbours N=54, median -0.001, robust sigma 0.013, max +0.076; z = 17.6
- centroid: jump at onset 0.038" +- 0.017 (2.2 sigma, PA 265); largest consecutive-visit jump 0.038"; rms 0.025"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.566, W2-W3 1.919 (W3 S/N 65.2), W3-W4 2.150 (W4 S/N 37.7), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.37, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW -2.185 nm, varclass YSO(0.12); M_G 6.67, -1.49 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): Haro 4-260 [Y*O; *,Em*,LP?,MIR,NIR,Y*?,Y*O] 0.05" refs=7
- ASAS-SN: 1420 points, cameras bA(g,151); bE(g,210); ba(V,149, d=-0.003); be(V,191, d=+0.159); bi(g,332); bm(g,236); bq(g,151); change at onset (after-before, per-camera median) +0.078 mag; largest seasonal dimming 0.34 mag at MJD 57621
- dust: excess flux W1 10.10 mJy, W2 11.35 mJy, T = 1138 K (16-84%: 1044-1248) 

### uid1481782  [D2]  YOUNG
- position 83.44367 -5.95351; Gaia DR3 3017214869037692800; G 11.81, BP-RP 1.12, plx 2.62 mas; plot `plots/uid1481782.png`
- **young:** SIMBAD young-star types Or*,Y*?,Y*O (Brun 141; Gaia DR3 3017214873335520896) | Gaia DR3 variability class YSO(0.55)
- flags: 2.07 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 0.62 (stored 0.62, reproduced True); dW2 0.092, dW1 0.062, 21 visits, 202 points; baseline W1 8.51, W1-W2 0.328; onset between MJD 59630 and 59837
- detector 2: excess 0.386 mag, z 23.6, jitter ratio 10.7
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
- detector 2: excess 0.336 mag, z 16.2, jitter ratio 8.3
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
- detector 2: excess 0.402 mag, z 17.5, jitter ratio 9.2
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
- detector 2: excess 0.454 mag, z 23.6, jitter ratio 12.7
- field control: target step +0.246 (W1 +0.178); neighbours N=53, median -0.004, robust sigma 0.015, max +0.349; z = 16.9
- centroid: jump at onset 0.012" +- 0.018 (0.7 sigma, PA 115); largest consecutive-visit jump 0.042"; rms 0.025"; toward neighbour: 5.8" PA139 G20.3 (angle 24 deg); expected shift if a neighbour were the source: 5.8" G20.3: 1.19"
- AllWISE 2010: W1-W2 0.405, W2-W3 0.780 (W3 S/N 64.1), W3-W4 2.808 (W4 S/N 35.5), ext_flg 0, ph_qual AAAA: weak W3 excess (0.5 < W2-W3 < 1.0)
- Gaia: RUWE 1.35, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW 0.003 nm, varclass YSO(0.68); M_G 4.77, -1.88 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 5.8" PA139 G20.32 dG+7.63
- SIMBAD (10"): V* V531 Ori [Or*; *,Er*,NIR,Or*,Pe*,V*,X] 0.02" refs=18
- ASAS-SN: 1444 points, cameras bC(g,183); bG(g,213); bc(V,119, d=+0.131); be(V,40); bg(V,187, d=+0.094); bk(g,299); bo(g,241); bs(g,162); change at onset (after-before, per-camera median) +0.113 mag; largest seasonal dimming 0.26 mag at MJD 59281
- dust: excess flux W1 21.46 mJy, W2 21.49 mJy, T = 1304 K (16-84%: 1230-1388) 

### uid1585215  [D2]  YOUNG
- position 83.60786 -4.94096; Gaia DR3 3209550037201361024; G 14.74, BP-RP 1.96, plx 2.57 mas; plot `plots/uid1585215.png`
- **young:** SIMBAD young-star types Or*,TT*,Y*O (V* IP Ori)
- flags: 1.55 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | not plain dust: optical brightening -0.183 mag (per-camera -0.203,-0.086,-0.127,-0.183,-0.293) together with the infrared rise | largest seasonal optical dimming 0.35 mag (MJD 60654)
- NEOWISE: score refetch 1.10 (stored 1.10, reproduced True); dW2 0.184, dW1 0.024, 18 visits, 162 points; baseline W1 10.48, W1-W2 0.445; onset between MJD 58741 and 58899
- detector 2: excess 0.446 mag, z 11.0, jitter ratio 12.9
- field control: target step +0.441 (W1 +0.351); neighbours N=162, median -0.004, robust sigma 0.027, max +0.465; z = 16.2
- centroid: jump at onset 0.043" +- 0.022 (2.0 sigma, PA 272); largest consecutive-visit jump 0.072"; rms 0.027"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.629, W2-W3 2.775 (W3 S/N 47.4), W3-W4 2.031 (W4 S/N 21.8), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.21, ipd_frac_multi_peak 0, NSS none, Teff 3848 K, logg 4.13, H-alpha pEW -1.785 nm, varclass none; M_G 6.79, -1.55 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): V* IP Ori [TT*; *,Em*,Er*,MIR,NIR,Or*,TT*,V*,V*?,Y*O] 0.02" refs=48
- ASAS-SN: 1496 points, cameras bA(g,156, d=-0.203); bE(g,219, d=-0.086); ba(V,177); be(V,195); bi(g,343, d=-0.127); bm(g,240, d=-0.183); bq(g,166, d=-0.293); change at onset (after-before, per-camera median) -0.183 mag; largest seasonal dimming 0.35 mag at MJD 60654
- dust: excess flux W1 2.68 mJy, W2 5.26 mJy, T = 723 K (16-84%: 696-751) 

### uid878866  [D2]  YOUNG
- position 88.42049 +1.63723; Gaia DR3 3315801583867579392; G 13.11, BP-RP 1.77, plx 2.99 mas; plot `plots/uid878866.png`
- **young:** SIMBAD young-star types Or*,TT*,Y*O (EM* LkHA  334) | Gaia DR3 variability class YSO(0.69)
- flags: 2.33 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.25 mag (MJD 59133)
- NEOWISE: score refetch 3.76 (stored 3.76, reproduced True); dW2 0.224, dW1 0.240, 21 visits, 211 points; baseline W1 8.27, W1-W2 0.562; onset between MJD 57287 and 57452
- detector 2: excess 0.594 mag, z 18.3, jitter ratio 5.2
- field control: target step +0.187 (W1 +0.144); neighbours N=96, median -0.002, robust sigma 0.012, max +0.123; z = 15.9
- centroid: jump at onset 0.008" +- 0.018 (0.4 sigma, PA 294); largest consecutive-visit jump 0.045"; rms 0.039"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.619, W2-W3 1.849 (W3 S/N 77.1), W3-W4 1.734 (W4 S/N 44.2), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.35, ipd_frac_multi_peak 0, NSS none, Teff 5744 K, logg 3.91, H-alpha pEW -0.695 nm, varclass YSO(0.69); M_G 5.49, -2.33 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): EM* LkHA  334 [TT*; *,Em*,IR,NIR,Or*,TT*,V*,Y*O,ev] 0.08" refs=24
- ASAS-SN: 890 points, cameras bA(g,91); bB(g,91); bE(g,69); bF(g,54); bi(g,125); bj(g,118); bm(g,80); bn(g,74); bq(g,104); br(g,84); change at onset (after-before, per-camera median) n/a mag; largest seasonal dimming 0.25 mag at MJD 59133
- dust: excess flux W1 23.86 mJy, W2 20.40 mJy, T = 1646 K (16-84%: 1476-1866) 
- checks missing: ASAS-SN change at onset (no camera spans the onset)

### uid1669869  [D2]  YOUNG
- position 84.20421 -5.94698; Gaia DR3 3017180960273832576; G 14.78, BP-RP 2.15, plx 2.53 mas; plot `plots/uid1669869.png`
- **young:** SIMBAD young-star types Or*,TT*,Y*O (V* V1136 Ori)
- flags: 2.14 mag above the main sequence at its colour | not plain dust: optical brightening -0.105 mag (per-camera -0.097,-0.113) together with the infrared rise | largest seasonal optical dimming 0.23 mag (MJD 56893)
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 20 visits, 192 points; baseline W1 10.90, W1-W2 0.478; onset between MJD 57647 and 57811
- detector 2: excess 0.449 mag, z 10.4, jitter ratio 15.7
- field control: target step +0.237 (W1 +0.191); neighbours N=112, median -0.006, robust sigma 0.016, max +0.352; z = 15.7
- centroid: jump at onset 0.027" +- 0.020 (1.3 sigma, PA 296); largest consecutive-visit jump 0.091"; rms 0.033"; toward neighbour: none; expected shift if a neighbour were the source: 8.0" G20.7: 1.57"; 8.1" G20.3: 1.59"
- AllWISE 2010: W1-W2 0.151, W2-W3 2.337 (W3 S/N 26.1), W3-W4 2.832 (W4 S/N 22.7), ext_flg 0, ph_qual AAAA: W3 excess only (W2-W3 > 1.0; debris-disk-like or blend)
- Gaia: RUWE 1.02, ipd_frac_multi_peak 0, NSS none, Teff 5789 K, logg 4.23, H-alpha pEW -0.546 nm, varclass none; M_G 6.79, -2.14 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 8.0" PA239 G20.66 dG+5.88; 8.1" PA148 G20.25 dG+5.47
- SIMBAD (10"): V* V1136 Ori [TT*; *,Er*,MIR,NIR,Or*,TT*,V*,V*?,Y*O] 0.05" refs=24
- ASAS-SN: 1470 points, cameras bA(g,153); bE(g,217); ba(V,173, d=-0.097); be(V,194, d=-0.113); bi(g,332); bm(g,236); bq(g,165); change at onset (after-before, per-camera median) -0.105 mag; largest seasonal dimming 0.23 mag at MJD 56893
- dust: excess flux W1 -0.18 mJy, W2 -0.10 mJy, T = n/a K (16-84%: n/a-n/a) no W2 excess flux after onset

### uid1117853  [D2]  YOUNG
- position 82.34693 -1.42096; Gaia DR3 3220241585188156032; G 14.29, BP-RP 1.70, plx 2.82 mas; plot `plots/uid1117853.png`
- **young:** SIMBAD young-star types Or*,TT*,Y*?,Y*O (Kiso A-0903 176) | Gaia DR3 variability class YSO(0.57)
- flags: 1.07 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 1.04 (stored 1.04, reproduced True); dW2 0.134, dW1 0.128, 20 visits, 240 points; baseline W1 9.51, W1-W2 0.532; onset between MJD 58167 and 58376
- detector 2: excess 0.574 mag, z 19.5, jitter ratio 7.6
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
- detector 2: excess 0.605 mag, z 18.6, jitter ratio 7.5
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
- detector 2: excess 0.535 mag, z 32.0, jitter ratio 10.4
- field control: target step +0.195 (W1 +0.232); neighbours N=59, median -0.002, robust sigma 0.013, max +0.035; z = 14.8
- centroid: jump at onset 0.035" +- 0.014 (2.4 sigma, PA 79); largest consecutive-visit jump 0.040"; rms 0.031"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.459, W2-W3 1.929 (W3 S/N 61.6), W3-W4 1.584 (W4 S/N 29.8), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 0.99, ipd_frac_multi_peak 0, NSS none, Teff 5266 K, logg 4.14, H-alpha pEW 0.094 nm, varclass YSO(0.25); M_G 4.61, -1.59 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): NSV  1302 [V*; *,NIR,V*] 0.09" refs=11
- ASAS-SN: 415 points, cameras bB(g,135); bb(V,59, d=+0.049); br(g,221); change at onset (after-before, per-camera median) +0.049 mag; largest seasonal dimming 0.15 mag at MJD 59619
- dust: excess flux W1 7.08 mJy, W2 4.55 mJy, T = 3572 K (16-84%: 2581-6282) 

### uid984249  [D2]  YOUNG
- position 81.04666 +3.58933; Gaia DR3 3236174230229658240; G 13.83, BP-RP 1.67, plx 2.91 mas; plot `plots/uid984249.png`
- **young:** SIMBAD young-star types TT*,Y*O (CVSO 662)
- flags: centroid jump 0.042" (3.1 sigma, PA 280) not toward a Gaia neighbour | 1.40 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.32 mag (MJD 58709)
- NEOWISE: score refetch 1.83 (stored 1.83, reproduced True); dW2 0.223, dW1 0.287, 20 visits, 220 points; baseline W1 10.14, W1-W2 0.312; onset between MJD 57085 and 57280
- detector 2: excess 0.358 mag, z 12.8, jitter ratio 11.5
- field control: target step +0.165 (W1 +0.187); neighbours N=57, median -0.005, robust sigma 0.012, max +0.019; z = 14.3
- centroid: jump at onset 0.042" +- 0.013 (3.1 sigma, PA 280); largest consecutive-visit jump 0.028"; rms 0.023"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.276, W2-W3 1.841 (W3 S/N 52.7), W3-W4 2.161 (W4 S/N 27.9), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.18, ipd_frac_multi_peak 1, NSS none, Teff 4449 K, logg 4.13, H-alpha pEW -0.092 nm, varclass none; M_G 6.15, -1.40 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): CVSO 662 [TT*; *,MIR,NIR,TT*,Y*O] 0.02" refs=19
- ASAS-SN: 1238 points, cameras bA(g,167); bE(g,179); ba(V,210, d=+0.007); be(V,56); bi(g,286); bm(g,209); bq(g,131); change at onset (after-before, per-camera median) +0.007 mag; largest seasonal dimming 0.32 mag at MJD 58709
- dust: excess flux W1 5.55 mJy, W2 4.55 mJy, T = 1772 K (16-84%: 1550-2079) 

### uid1604479  [D2]  YOUNG
- position 83.85466 -6.79903; Gaia DR3 3016548431848965888; G 13.94, BP-RP 1.53, plx 2.56 mas; plot `plots/uid1604479.png`
- **young:** SIMBAD young-star types Or*,Y*O (V* NT Ori) | Gaia DR3 variability class YSO(0.43)
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | 1.20 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.48 mag (MJD 59514)
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 20 visits, 196 points; baseline W1 9.04, W1-W2 0.613; onset between MJD 58377 and 58535
- detector 2: excess 0.671 mag, z 29.9, jitter ratio 22.2
- field control: target step +0.254 (W1 +0.281); neighbours N=95, median -0.007, robust sigma 0.019, max +0.138; z = 14.1
- centroid: jump at onset 0.025" +- 0.017 (1.5 sigma, PA 154); largest consecutive-visit jump 0.069"; rms 0.028"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.563, W2-W3 1.663 (W3 S/N 57.8), W3-W4 1.923 (W4 S/N 26.9), ext_flg 1, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.21, ipd_frac_multi_peak 0, NSS none, Teff 6110 K, logg 4.31, H-alpha pEW -3.954 nm, varclass YSO(0.43); M_G 5.98, -1.20 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): V* NT Ori [Or*; *,Em*,Er*,MIR,NIR,Opt,Or*,V*,V*?,Y*O] 0.01" refs=52
- ASAS-SN: 998 points, cameras bA(g,145); bE(g,117, d=-0.222); ba(V,136); be(V,194); bi(g,203, d=-0.259); bm(g,150, d=-0.180); bq(g,53, d=+0.054); change at onset (after-before, per-camera median) -0.201 mag; largest seasonal dimming 0.48 mag at MJD 59514
- dust: excess flux W1 1.70 mJy, W2 0.24 mJy, T = 8000 K (16-84%: 8000-8000) ratio bluer than an 8000 K blackbody (not dust-like)

### uid941546  [D2]  YOUNG
- position 81.59023 +3.81044; Gaia DR3 3236266005091323008; G 14.90, BP-RP 2.19, plx 2.94 mas; plot `plots/uid941546.png`
- **young:** SIMBAD young-star types Y*?,Y*O (UCAC4 470-010975)
- flags: in the Gaia DR3 QSO candidate table (low purity) | 1.78 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 1.44 (stored 1.44, reproduced True); dW2 0.236, dW1 0.132, 21 visits, 210 points; baseline W1 10.71, W1-W2 0.533; onset between MJD 57809 and 58011
- detector 2: excess 0.501 mag, z 11.7, jitter ratio 12.4
- field control: target step +0.139 (W1 +0.077); neighbours N=69, median -0.006, robust sigma 0.010, max +0.120; z = 13.9
- centroid: jump at onset 0.039" +- 0.022 (1.8 sigma, PA 15); largest consecutive-visit jump 0.042"; rms 0.033"; toward neighbour: none; expected shift if a neighbour were the source: 8.6" G14.6: 1.03"
- AllWISE 2010: W1-W2 0.554, W2-W3 2.455 (W3 S/N 59.4), W3-W4 1.302 (W4 S/N 16.7), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.03, ipd_frac_multi_peak 0, NSS none, Teff 3672 K, logg 4.01, H-alpha pEW -0.073 nm, varclass none; M_G 7.25, -1.78 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 8.6" PA160 G14.59 dG-0.32
- SIMBAD (10"): UCAC4 470-010975 [Y*O; *,MIR,NIR,Y*?,Y*O] 0.03" refs=18
- ASAS-SN: 1465 points, cameras bA(g,170); bE(g,179); bH(g,159); ba(V,211, d=+0.005); be(V,56, d=-0.027); bh(V,52, d=+0.007); bi(g,285); bm(g,215); bq(g,138); change at onset (after-before, per-camera median) +0.005 mag; largest seasonal dimming 0.05 mag at MJD 58334
- dust: excess flux W1 1.15 mJy, W2 1.91 mJy, T = 808 K (16-84%: 746-876) 

### uid1275537  [D2]  YOUNG
- position 83.37939 -3.28927; Gaia DR3 3215980462236023936; G 15.26, BP-RP 2.15, plx 2.73 mas; plot `plots/uid1275537.png`
- **young:** SIMBAD young-star types TT*,Y*?,Y*O (UCAC4 434-010624)
- flags: 1.49 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | not plain dust: optical brightening -0.062 mag (per-camera -0.039,-0.085) together with the infrared rise | largest seasonal optical dimming 0.13 mag (MJD 56636)
- NEOWISE: score refetch 1.51 (stored 1.51, reproduced True); dW2 0.214, dW1 0.228, 20 visits, 176 points; baseline W1 11.32, W1-W2 0.498; onset between MJD 57087 and 57282
- detector 2: excess 0.469 mag, z 10.9, jitter ratio 11.2
- field control: target step +0.188 (W1 +0.199); neighbours N=67, median -0.007, robust sigma 0.014, max +0.119; z = 13.8
- centroid: jump at onset 0.009" +- 0.016 (0.6 sigma, PA 299); largest consecutive-visit jump 0.052"; rms 0.029"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.417, W2-W3 1.647 (W3 S/N 32.8), W3-W4 2.410 (W4 S/N 13.9), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.02, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW -0.185 nm, varclass none; M_G 7.44, -1.49 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): UCAC4 434-010624 [TT*; *,MIR,NIR,TT*,Y*?,Y*O] 0.03" refs=14
- ASAS-SN: 1200 points, cameras bC(g,116); bG(g,182); ba(V,45); bc(V,129, d=-0.039); be(V,34, d=-0.085); bg(V,147); bk(g,249); bo(g,167); bs(g,131); change at onset (after-before, per-camera median) -0.062 mag; largest seasonal dimming 0.13 mag at MJD 56636
- dust: excess flux W1 1.83 mJy, W2 1.65 mJy, T = 1508 K (16-84%: 1397-1639) 

### uid979261  [D2]  YOUNG
- position 83.41595 -0.64834; Gaia DR3 3220685100690997632; G 13.66, BP-RP 1.73, plx 2.91 mas; plot `plots/uid979261.png`
- **young:** SIMBAD young-star types Or*,TT*,Y*O (V* V543 Ori) | Gaia DR3 variability class YSO(0.24)
- flags: 1.74 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.26 mag (MJD 58885)
- NEOWISE: score refetch 0.98 (stored 0.98, reproduced True); dW2 0.155, dW1 0.127, 20 visits, 211 points; baseline W1 9.53, W1-W2 0.420; onset between MJD 59263 and 59473
- detector 2: excess 0.457 mag, z 14.5, jitter ratio 15.8
- field control: target step +0.186 (W1 +0.119); neighbours N=77, median -0.003, robust sigma 0.014, max +0.053; z = 13.4
- centroid: jump at onset 0.004" +- 0.013 (0.3 sigma, PA 88); largest consecutive-visit jump 0.063"; rms 0.026"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.380, W2-W3 1.873 (W3 S/N 59.9), W3-W4 2.123 (W4 S/N 27.8), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.12, ipd_frac_multi_peak 0, NSS none, Teff 5602 K, logg 4.20, H-alpha pEW -0.885 nm, varclass YSO(0.24); M_G 5.98, -1.74 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): V* V543 Ori [TT*; *,NIR,Or*,TT*,V*,V*?,Y*O] 0.03" refs=26
- ASAS-SN: 1465 points, cameras bC(g,151, d=+0.036); bG(g,221, d=-0.003); ba(V,51); bc(V,151); be(V,38); bg(V,153); bk(g,307, d=-0.057); bo(g,233, d=-0.130); bs(g,160, d=-0.181); change at onset (after-before, per-camera median) -0.057 mag; largest seasonal dimming 0.26 mag at MJD 58885
- dust: excess flux W1 8.16 mJy, W2 7.76 mJy, T = 1398 K (16-84%: 1248-1582) 

### uid1173802  [D2]  YOUNG
- position 81.92501 -1.73942; Gaia DR3 3220135757194960896; G 13.55, BP-RP 1.54, plx 2.79 mas; plot `plots/uid1173802.png`
- **young:** SIMBAD young-star types Or*,TT*,Y*?,Y*O (Kiso A-0903 143) | Gaia DR3 variability class YSO(0.44)
- flags: 1.43 mag above the main sequence at its colour | optical dimming +0.076 mag after the infrared onset (debris transit signature)
- NEOWISE: score refetch 0.58 (stored 0.58, reproduced True); dW2 0.068, dW1 0.037, 21 visits, 248 points; baseline W1 10.36, W1-W2 0.191; onset between MJD 57644 and 57809
- detector 2: excess 0.248 mag, z 10.9, jitter ratio 8.4
- field control: target step +0.125 (W1 +0.087); neighbours N=67, median -0.005, robust sigma 0.010, max +0.045; z = 13.4
- centroid: jump at onset 0.001" +- 0.015 (0.0 sigma, PA 354); largest consecutive-visit jump 0.058"; rms 0.026"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.174, W2-W3 2.365 (W3 S/N 55.5), W3-W4 2.565 (W4 S/N 37.3), ext_flg 0, ph_qual AAAA: W3 excess only (W2-W3 > 1.0; debris-disk-like or blend)
- Gaia: RUWE 1.17, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW -0.617 nm, varclass YSO(0.44); M_G 5.77, -1.43 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): Kiso A-0903 143 [TT*; *,Em*,NIR,Or*,TT*,Y*?,Y*O] 0.03" refs=26
- ASAS-SN: 1483 points, cameras bD(g,166); bH(g,207); ba(V,51); bd(V,156, d=+0.042); bf(V,40); bh(V,152, d=+0.109); bl(g,324); bp(g,212); bt(g,175); change at onset (after-before, per-camera median) +0.076 mag; largest seasonal dimming 0.05 mag at MJD 59085
- dust: excess flux W1 1.73 mJy, W2 1.77 mJy, T = 1267 K (16-84%: 1124-1443) 

### uid1016323  [D2]  YOUNG
- position 333.30125 +73.54962; Gaia DR3 2278977408959483264; G 13.42, BP-RP 1.73, plx 2.89 mas; plot `plots/uid1016323.png`
- **young:** SIMBAD young-star types Or*,Y*?,Y*O (2MASS J22131219+7332585) | Gaia DR3 variability class YSO(0.81)
- flags: 1.97 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.16 mag (MJD 60438)
- NEOWISE: score refetch 0.01 (stored 0.01, reproduced True); dW2 0.002, dW1 0.003, 10 visits, 100 points; baseline W1 8.75, W1-W2 0.446; onset between MJD 60165 and 60324
- detector 2: excess 0.484 mag, z 15.5, jitter ratio 13.0
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
- detector 2: excess 0.495 mag, z 17.6, jitter ratio 8.4
- field control: target step +0.215 (W1 -0.060); neighbours N=123, median +0.003, robust sigma 0.016, max +0.565; z = 13.0
- centroid: jump at onset 0.026" +- 0.016 (1.6 sigma, PA 276); largest consecutive-visit jump 0.030"; rms 0.029"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.506, W2-W3 1.730 (W3 S/N 54.1), W3-W4 1.840 (W4 S/N 29.3), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.03, ipd_frac_multi_peak 0, NSS none, Teff 5552 K, logg 4.24, H-alpha pEW -1.187 nm, varclass YSO(0.45); M_G 5.92, -1.65 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): V* AW Ori [TT*; *,Em*,MIR,NIR,Opt,Or*,TT*,V*,X,Y*O] 0.02" refs=44
- ASAS-SN: 1155 points, cameras bA(g,130, d=+1.447); bE(g,166, d=+1.147); ba(V,163); be(V,194); bi(g,195, d=+0.725); bm(g,169); bq(g,138, d=+0.909); change at onset (after-before, per-camera median) +1.028 mag; largest seasonal dimming 1.41 mag at MJD 60406
- dust: excess flux W1 10.22 mJy, W2 15.02 mJy, T = 888 K (16-84%: 840-944) 

### uid1078155  [D2]  YOUNG
- position 329.63689 +80.33781; Gaia DR3 2285488987399269376; G 13.20, BP-RP 1.56, plx 2.85 mas; plot `plots/uid1078155.png`
- **young:** SIMBAD young-star types Y*? (UCAC4 852-015443) | Gaia DR3 variability class YSO(0.56)
- flags: centroid jump 0.065" (4.4 sigma, PA 130) not toward a Gaia neighbour | AllWISE ext_flg = 1 (extended or 2MASS XSC association) | 1.77 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | possible optical brightening at onset (-0.062 mag, one camera only)
- NEOWISE: score refetch 0.55 (stored 0.55, reproduced True); dW2 0.083, dW1 0.082, 11 visits, 115 points; baseline W1 9.11, W1-W2 0.334; onset between MJD 59453 and 59612
- detector 2: excess 0.390 mag, z 16.8, jitter ratio 14.1
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
- detector 2: excess 0.462 mag, z 18.6, jitter ratio 7.9
- field control: target step +0.108 (W1 +0.044); neighbours N=39, median -0.007, robust sigma 0.009, max +0.019; z = 12.8
- centroid: jump at onset 0.014" +- 0.024 (0.6 sigma, PA 277); largest consecutive-visit jump 0.038"; rms 0.021"; toward neighbour: none; expected shift if a neighbour were the source: 9.8" G17.3: 0.92"
- AllWISE 2010: W1-W2 0.466, W2-W3 1.548 (W3 S/N 53.6), W3-W4 1.448 (W4 S/N 17.6), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.33, ipd_frac_multi_peak 0, NSS none, Teff 4818 K, logg 4.20, H-alpha pEW -0.671 nm, varclass YSO(0.14); M_G 5.91, -1.43 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 9.8" PA206 G17.35 dG+3.62
- SIMBAD (10"): UCAC4 414-008437 [Y*O; *,MIR,NIR,Y*O] 0.02" refs=3
- ASAS-SN: 1293 points, cameras bB(g,84); bF(g,207); bb(V,154, d=+0.165); bf(V,171, d=-0.149); bj(g,277); bn(g,237); br(g,163); change at onset (after-before, per-camera median) +0.008 mag; largest seasonal dimming 0.20 mag at MJD 59828
- dust: excess flux W1 2.11 mJy, W2 1.32 mJy, T = 4011 K (16-84%: 1588-8000) 

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

### uid1478701  [D2]  YOUNG
- position 83.99272 -6.61198; Gaia DR3 3016927763360145536; G 15.00, BP-RP 2.09, plx 2.62 mas; plot `plots/uid1478701.png`
- **young:** SIMBAD young-star types Or*,Y*O (V* OY Ori)
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | 1.65 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | optical dimming +0.161 mag after the infrared onset (debris transit signature) | largest seasonal optical dimming 0.41 mag (MJD 58870)
- NEOWISE: score refetch 0.47 (stored 0.47, reproduced True); dW2 0.100, dW1 0.061, 20 visits, 192 points; baseline W1 9.80, W1-W2 0.516; onset between MJD 58168 and 58377
- detector 2: excess 0.495 mag, z 11.5, jitter ratio 17.5
- field control: target step +0.198 (W1 +0.156); neighbours N=108, median -0.003, robust sigma 0.016, max +0.243; z = 12.3
- centroid: jump at onset 0.022" +- 0.019 (1.2 sigma, PA 14); largest consecutive-visit jump 0.098"; rms 0.031"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.547, W2-W3 1.907 (W3 S/N 21.3), W3-W4 2.001 (W4 S/N 13.9), ext_flg 1, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.17, ipd_frac_multi_peak 0, NSS none, Teff 5343 K, logg 4.28, H-alpha pEW -1.640 nm, varclass none; M_G 7.09, -1.65 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): V* OY Ori [Or*; *,Em*,MIR,NIR,Opt,Or*,V*,V*?,Y*O] 0.02" refs=46
- ASAS-SN: 1069 points, cameras bA(g,124); bE(g,180); ba(V,149); be(V,179); bi(g,189, d=+0.161); bm(g,115, d=+0.703); bq(g,133, d=+0.109); change at onset (after-before, per-camera median) +0.161 mag; largest seasonal dimming 0.41 mag at MJD 58870
- dust: excess flux W1 3.58 mJy, W2 5.04 mJy, T = 919 K (16-84%: 849-998) 

### uid1550526  [D2]  YOUNG
- position 118.56172 -46.43338; Gaia DR3 5518967386922303616; G 12.84, BP-RP 1.38, plx 2.58 mas; plot `plots/uid1550526.png`
- **young:** SIMBAD young-star types Y*?,Y*O (Gaia DR3 5518967386922303616) | Gaia DR3 variability class YSO(0.78)
- flags: 1.89 mag above the main sequence at its colour | largest seasonal optical dimming 0.30 mag (MJD 57448)
- NEOWISE: score refetch 1.16 (stored 1.16, reproduced True); dW2 0.171, dW1 0.140, 21 visits, 316 points; baseline W1 8.40, W1-W2 0.474; onset between MJD 58436 and 58593
- detector 2: excess 0.537 mag, z 27.5, jitter ratio 14.0
- field control: target step +0.113 (W1 +0.053); neighbours N=147, median -0.003, robust sigma 0.010, max +0.044; z = 12.1
- centroid: jump at onset 0.011" +- 0.021 (0.5 sigma, PA 188); largest consecutive-visit jump 0.069"; rms 0.026"; toward neighbour: 9.3" PA195 G19.6 (angle 6 deg); expected shift if a neighbour were the source: 7.2" G17.9: 0.71"; 9.3" G19.6: 0.92"
- AllWISE 2010: W1-W2 0.469, W2-W3 0.936 (W3 S/N 67.8), W3-W4 2.121 (W4 S/N 40.4), ext_flg 0, ph_qual AAAA: weak W3 excess (0.5 < W2-W3 < 1.0)
- Gaia: RUWE 1.12, ipd_frac_multi_peak 1, NSS none, Teff 5485 K, logg 3.98, H-alpha pEW -0.706 nm, varclass YSO(0.78); M_G 4.90, -1.89 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 7.2" PA107 G17.90 dG+5.07; 9.3" PA195 G19.64 dG+6.80
- SIMBAD (10"): Gaia DR3 5518967386922303616 [Y*?; *,Y*?,Y*O] 0.16" refs=7
- ASAS-SN: 1376 points, cameras bE(g,423, d=-0.023); be(V,231); bi(g,510, d=-0.004); bm(g,212); change at onset (after-before, per-camera median) -0.014 mag; largest seasonal dimming 0.30 mag at MJD 57448
- dust: excess flux W1 7.31 mJy, W2 13.48 mJy, T = 753 K (16-84%: 654-868) 

### uid1108316  [D2]  YOUNG
- position 84.21799 -1.35686; Gaia DR3 3217396701931361792; G 13.60, BP-RP 1.61, plx 2.83 mas; plot `plots/uid1108316.png`
- **young:** SIMBAD young-star types Y*?,Y*O (CRTS J053652.2-012124)
- flags: 1.54 mag above the main sequence at its colour
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 14 visits, 119 points; baseline W1 10.56, W1-W2 0.237; onset between MJD 56921 and 57088
- detector 2: excess 0.288 mag, z 11.2, jitter ratio 11.6
- field control: target step +0.135 (W1 +0.045); neighbours N=88, median -0.003, robust sigma 0.011, max +0.035; z = 11.9
- centroid: jump at onset 0.036" +- 0.029 (1.2 sigma, PA 196); largest consecutive-visit jump 0.080"; rms 0.042"; toward neighbour: 7.4" PA169 G18.3 (angle 26 deg); expected shift if a neighbour were the source: 7.4" G18.3: 0.86"
- AllWISE 2010: W1-W2 0.205, W2-W3 1.372 (W3 S/N 31.8), W3-W4 2.085 (W4 S/N 10.3), ext_flg 0, ph_qual AAAA: W3 excess only (W2-W3 > 1.0; debris-disk-like or blend)
- Gaia: RUWE 0.98, ipd_frac_multi_peak 0, NSS none, Teff 4581 K, logg 4.14, H-alpha pEW -0.164 nm, varclass RS(0.55); M_G 5.86, -1.54 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 7.4" PA169 G18.27 dG+4.67
- SIMBAD (10"): CRTS J053652.2-012124 [RS*; *,NIR,RS*,Y*?,Y*O] 0.03" refs=14; 2E 0534.3-0123 [X; X] 3.91" refs=0
- ASAS-SN: 1371 points, cameras bC(g,158); bG(g,221); ba(V,51); bc(V,151, d=+0.016); be(V,38, d=-0.010); bg(V,153); bk(g,287); bo(g,165); bs(g,147); change at onset (after-before, per-camera median) +0.003 mag; largest seasonal dimming 0.05 mag at MJD 57629
- dust: excess flux W1 0.52 mJy, W2 1.47 mJy, T = 589 K (16-84%: 522-663) 

### uid1479092  [D2]  YOUNG
- position 85.40209 -6.34590; Gaia DR3 3016249811363341568; G 13.78, BP-RP 1.72, plx 2.62 mas; plot `plots/uid1479092.png`
- **young:** SIMBAD young-star types Y*?,Y*O (Haro 4-487)
- flags: 1.82 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 0.61 (stored 0.61, reproduced True); dW2 0.060, dW1 0.073, 21 visits, 268 points; baseline W1 10.22, W1-W2 0.544; onset between MJD 57648 and 57813
- detector 2: excess 0.583 mag, z 18.9, jitter ratio 9.7
- field control: target step +0.143 (W1 +0.037); neighbours N=61, median -0.004, robust sigma 0.013, max +0.024; z = 11.7
- centroid: jump at onset 0.015" +- 0.014 (1.1 sigma, PA 245); largest consecutive-visit jump 0.057"; rms 0.031"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.510, W2-W3 2.483 (W3 S/N 61.0), W3-W4 1.911 (W4 S/N 31.7), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.04, ipd_frac_multi_peak 0, NSS none, Teff 5555 K, logg 4.20, H-alpha pEW -2.167 nm, varclass RS(0.30); M_G 5.87, -1.82 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): Haro 4-487 [Y*O; *,Em*,MIR,NIR,PM*,Y*?,Y*O] 0.05" refs=9
- ASAS-SN: 0 points, cameras n/a; change at onset (after-before, per-camera median) n/a mag; largest seasonal dimming n/a mag at MJD n/a
- dust: excess flux W1 1.52 mJy, W2 2.44 mJy, T = 827 K (16-84%: 750-914) 
- checks missing: ASAS-SN (no source)

### uid1117149  [D2]  YOUNG
- position 80.48922 +0.19505; Gaia DR3 3221444107311671936; G 14.96, BP-RP 1.71, plx 2.82 mas; plot `plots/uid1117149.png`
- **young:** SIMBAD young-star types TT*,Y*O (Kiso A-0903  80) | Gaia DR3 variability class YSO(0.55)
- flags: AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | possible optical brightening at onset (-0.201 mag, one camera only) | largest seasonal optical dimming 0.24 mag (MJD 59262)
- NEOWISE: score refetch 1.20 (stored 1.20, reproduced True); dW2 0.155, dW1 0.130, 20 visits, 174 points; baseline W1 10.13, W1-W2 0.407; onset between MJD 57085 and 57279
- detector 2: excess 0.446 mag, z 14.6, jitter ratio 12.5
- field control: target step +0.161 (W1 +0.146); neighbours N=58, median -0.007, robust sigma 0.014, max +0.109; z = 11.6
- centroid: jump at onset 0.029" +- 0.017 (1.7 sigma, PA 41); largest consecutive-visit jump 0.033"; rms 0.029"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.440, W2-W3 1.446 (W3 S/N 48.3), W3-W4 1.942 (W4 S/N 17.3), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.19, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW -2.158 nm, varclass YSO(0.55); M_G 7.22, -0.45 mag vs sequence (on the sequence); neighbours within 10": none
- SIMBAD (10"): Kiso A-0903  80 [TT*; *,Em*,NIR,TT*,Y*O] 0.03" refs=17
- ASAS-SN: 1112 points, cameras bB(g,84); bF(g,152); bb(V,297, d=-0.201); bf(V,55); bj(g,198); bn(g,204); br(g,122); change at onset (after-before, per-camera median) -0.201 mag; largest seasonal dimming 0.24 mag at MJD 59262
- dust: excess flux W1 3.87 mJy, W2 3.49 mJy, T = 1507 K (16-84%: 1352-1706) 

### uid880869  [D2]  YOUNG
- position 83.10743 -0.61483; Gaia DR3 3220694442244758784; G 14.16, BP-RP 1.80, plx 2.98 mas; plot `plots/uid880869.png`
- **young:** SIMBAD young-star types Or*,TT*,Y*O (Kiso A-0904   4) | Gaia DR3 variability class YSO(0.60)
- flags: 1.35 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | not plain dust: optical brightening -0.068 mag (per-camera -0.195,-0.009,-0.102,-0.017,-0.068) together with the infrared rise | largest seasonal optical dimming 0.18 mag (MJD 57824)
- NEOWISE: score refetch 0.88 (stored 0.88, reproduced True); dW2 0.144, dW1 0.062, 21 visits, 213 points; baseline W1 9.78, W1-W2 0.399; onset between MJD 58741 and 58899
- detector 2: excess 0.427 mag, z 12.6, jitter ratio 14.0
- field control: target step +0.167 (W1 +0.104); neighbours N=106, median -0.002, robust sigma 0.015, max +0.061; z = 11.4
- centroid: jump at onset 0.031" +- 0.015 (2.0 sigma, PA 244); largest consecutive-visit jump 0.062"; rms 0.027"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.448, W2-W3 2.010 (W3 S/N 51.5), W3-W4 2.291 (W4 S/N 26.8), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.16, ipd_frac_multi_peak 0, NSS none, Teff 5784 K, logg 4.31, H-alpha pEW -2.604 nm, varclass YSO(0.60); M_G 6.54, -1.35 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): Kiso A-0904   4 [TT*; *,Em*,NIR,Opt,Or*,TT*,V*,Y*O] 0.03" refs=42
- ASAS-SN: 1300 points, cameras bC(g,148, d=-0.195); bG(g,222, d=-0.009); ba(V,51); bc(V,151); be(V,38); bg(V,146); bk(g,257, d=-0.102); bo(g,154, d=-0.017); bs(g,133, d=-0.068); change at onset (after-before, per-camera median) -0.068 mag; largest seasonal dimming 0.18 mag at MJD 57824
- dust: excess flux W1 3.95 mJy, W2 4.17 mJy, T = 1224 K (16-84%: 1095-1379) 

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
- detector 2: excess 0.418 mag, z 17.2, jitter ratio 5.8
- field control: target step +0.122 (W1 +0.083); neighbours N=94, median -0.003, robust sigma 0.011, max +0.093; z = 11.3
- centroid: jump at onset 0.024" +- 0.013 (1.9 sigma, PA 61); largest consecutive-visit jump 0.029"; rms 0.028"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.341, W2-W3 2.086 (W3 S/N 57.3), W3-W4 2.253 (W4 S/N 36.5), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.33, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW -0.720 nm, varclass none; M_G 5.51, -1.82 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): Haro 5-71 [Or*; *,Em*,Er*,NIR,Opt,Or*,V*,Y*O] 0.03" refs=19
- ASAS-SN: 1441 points, cameras bC(g,157); bG(g,222); ba(V,50); bc(V,151, d=+0.154); be(V,38, d=-0.206); bg(V,153); bk(g,298); bo(g,212); bs(g,160); change at onset (after-before, per-camera median) -0.026 mag; largest seasonal dimming 0.14 mag at MJD 58194
- dust: excess flux W1 7.29 mJy, W2 6.51 mJy, T = 1531 K (16-84%: 1303-1873) 

### uid991402  [D2]  YOUNG
- position 340.91377 +75.10840; Gaia DR3 2231524617408985472; G 12.83, BP-RP 1.50, plx 2.91 mas; plot `plots/uid991402.png`
- **young:** SIMBAD young-star types Or*,Y*O (GSC 04601-03483; Gaia DR3 2231524617408985728) | Gaia DR3 variability class YSO(0.43)
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | 1.95 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 0.98 (stored 0.98, reproduced True); dW2 0.210, dW1 0.151, 21 visits, 512 points; baseline W1 9.25, W1-W2 0.231; onset between MJD 57250 and 57417
- detector 2: excess 0.290 mag, z 13.5, jitter ratio 17.0
- field control: target step +0.097 (W1 +0.104); neighbours N=114, median -0.002, robust sigma 0.009, max +0.104; z = 10.7
- centroid: jump at onset 0.110" +- 0.045 (2.4 sigma, PA 234); largest consecutive-visit jump 0.079"; rms 0.102"; toward neighbour: none; expected shift if a neighbour were the source: 5.0" G16.7: 0.43"; 5.5" G19.7: 0.47"
- AllWISE 2010: W1-W2 0.283, W2-W3 2.317 (W3 S/N 75.1), W3-W4 2.665 (W4 S/N 43.0), ext_flg 1, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.31, ipd_frac_multi_peak 0, NSS none, Teff 4827 K, logg 4.11, H-alpha pEW -0.228 nm, varclass YSO(0.43); M_G 5.15, -1.95 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 5.0" PA65 G16.66 dG+3.83; 5.5" PA175 G19.67 dG+6.84
- SIMBAD (10"): GSC 04601-03483 [Or*; *,IR,NIR,Or*,Y*O] 0.11" refs=13; Gaia DR3 2231524617408985728 [Y*O; *,Y*O] 4.94" refs=3
- ASAS-SN: 533 points, cameras bB(g,119); bb(V,163, d=-0.000); br(g,251); change at onset (after-before, per-camera median) -0.000 mag; largest seasonal dimming 0.05 mag at MJD 58028
- dust: excess flux W1 9.22 mJy, W2 8.35 mJy, T = 1499 K (16-84%: 1372-1654) 

### uid1616401  [D2]  YOUNG
- position 83.25932 -5.44034; Gaia DR3 3209420947662499712; G 11.93, BP-RP 1.21, plx 2.55 mas; plot `plots/uid1616401.png`
- **young:** SIMBAD young-star types Or*,Y*O (V* V466 Ori) | Gaia DR3 variability class YSO(0.68)
- flags: Gaia ipd_frac_multi_peak 12% (resolved double?) | 2.29 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 2.57 (stored 2.57, reproduced True); dW2 0.324, dW1 0.292, 20 visits, 184 points; baseline W1 8.46, W1-W2 0.441; onset between MJD 57446 and 57646
- detector 2: excess 0.502 mag, z 29.1, jitter ratio 11.4
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
- detector 2: excess 0.553 mag, z 14.9, jitter ratio 12.6
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
- detector 2: excess 0.500 mag, z 15.2, jitter ratio 6.8
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
- detector 2: excess 0.579 mag, z 13.9, jitter ratio 11.0
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
- detector 2: excess 0.547 mag, z 18.7, jitter ratio 9.2
- field control: target step +0.138 (W1 +0.236); neighbours N=58, median -0.003, robust sigma 0.014, max +0.574; z = 10.0
- centroid: jump at onset 0.019" +- 0.018 (1.1 sigma, PA 334); largest consecutive-visit jump 0.058"; rms 0.028"; toward neighbour: none; expected shift if a neighbour were the source: 9.6" G17.6: 1.15"
- AllWISE 2010: W1-W2 0.550, W2-W3 2.508 (W3 S/N 51.1), W3-W4 1.739 (W4 S/N 13.6), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 0.98, ipd_frac_multi_peak 0, NSS none, Teff 4153 K, logg 4.16, H-alpha pEW -0.240 nm, varclass RS(0.72); M_G 6.38, -1.24 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 9.6" PA50 G17.57 dG+3.26
- SIMBAD (10"): UCAC4 427-010287 [Y*O; *,MIR,NIR,Y*?,Y*O] 0.02" refs=10
- ASAS-SN: 0 points, cameras n/a; change at onset (after-before, per-camera median) n/a mag; largest seasonal dimming n/a mag at MJD n/a
- dust: excess flux W1 3.68 mJy, W2 2.59 mJy, T = 2557 K (16-84%: 2236-2997) 
- checks missing: ASAS-SN (no source)

### uid1570932  [D2]  YOUNG
- position 83.70143 -6.50749; Gaia DR3 3017131134355299200; G 14.73, BP-RP 2.10, plx 2.57 mas; plot `plots/uid1570932.png`
- **young:** SIMBAD young-star types Or*,Y*?,Y*O (V* V374 Ori)
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | 1.97 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.25 mag (MJD 60655)
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 21 visits, 203 points; baseline W1 10.42, W1-W2 0.543; onset between MJD 59109 and 59263
- detector 2: excess 0.522 mag, z 12.1, jitter ratio 11.3
- field control: target step +0.146 (W1 +0.127); neighbours N=95, median -0.002, robust sigma 0.015, max +0.474; z = 10.0
- centroid: jump at onset 0.027" +- 0.024 (1.1 sigma, PA 187); largest consecutive-visit jump 0.081"; rms 0.034"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.532, W2-W3 1.989 (W3 S/N 41.2), W3-W4 1.855 (W4 S/N 14.8), ext_flg 1, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.06, ipd_frac_multi_peak 0, NSS none, Teff 5911 K, logg 4.26, H-alpha pEW -1.417 nm, varclass none; M_G 6.78, -1.97 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): V* V374 Ori [Or*; *,Em*,MIR,NIR,Opt,Or*,V*,V*?,X,Y*?,Y*O] 0.01" refs=44
- ASAS-SN: 1374 points, cameras bA(g,144, d=-0.070); bE(g,214, d=+0.020); ba(V,179); be(V,193); bi(g,305, d=-0.052); bm(g,205, d=-0.033); bq(g,134, d=-0.000); change at onset (after-before, per-camera median) -0.033 mag; largest seasonal dimming 0.25 mag at MJD 60655
- dust: excess flux W1 0.40 mJy, W2 0.10 mJy, T = 8000 K (16-84%: 3367-8000) ratio bluer than an 8000 K blackbody (not dust-like)

### uid1594699  [D2]  YOUNG
- position 84.15389 -6.55668; Gaia DR3 3016933432717079296; G 15.52, BP-RP 2.10, plx 2.56 mas; plot `plots/uid1594699.png`
- **young:** SIMBAD young-star types Or*,Y*O (V* V585 Ori)
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | 1.19 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.26 mag (MJD 56983)
- NEOWISE: score refetch 0.54 (stored 0.54, reproduced True); dW2 0.110, dW1 0.033, 21 visits, 196 points; baseline W1 8.70, W1-W2 0.830; onset between MJD 57088 and 57282
- detector 2: excess 0.808 mag, z 18.8, jitter ratio 8.2
- field control: target step +0.213 (W1 +0.233); neighbours N=91, median -0.002, robust sigma 0.022, max +0.329; z = 9.7
- centroid: jump at onset 0.031" +- 0.023 (1.4 sigma, PA 4); largest consecutive-visit jump 0.134"; rms 0.041"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.822, W2-W3 1.689 (W3 S/N 62.3), W3-W4 1.583 (W4 S/N 32.5), ext_flg 1, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.14, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW -5.078 nm, varclass none; M_G 7.57, -1.19 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): V* V585 Ori [Or*; *,Em*,LP?,MIR,NIR,Opt,Or*,V*,X,Y*O] 0.00" refs=41
- ASAS-SN: 1188 points, cameras bA(g,126); bE(g,164); ba(V,165, d=+0.015); be(V,159, d=-0.216); bi(g,280); bm(g,156); bq(g,138); change at onset (after-before, per-camera median) -0.101 mag; largest seasonal dimming 0.26 mag at MJD 56983
- dust: excess flux W1 19.94 mJy, W2 23.60 mJy, T = 1079 K (16-84%: 978-1197) 

### uid1454537  [D2]  YOUNG
- position 83.37789 -5.03743; Gaia DR3 3209542409339494656; G 14.99, BP-RP 2.20, plx 2.63 mas; plot `plots/uid1454537.png`
- **young:** SIMBAD young-star types Or*,Y*O (V* V721 Ori)
- flags: 1.97 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.60 mag (MJD 59961)
- NEOWISE: score refetch 1.10 (stored 1.10, reproduced True); dW2 0.113, dW1 0.136, 20 visits, 182 points; baseline W1 10.96, W1-W2 0.641; onset between MJD 57811 and 58013
- detector 2: excess 0.609 mag, z 14.2, jitter ratio 7.6
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
- detector 2: excess 0.818 mag, z 34.1, jitter ratio 5.8
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
- detector 2: excess 0.415 mag, z 15.9, jitter ratio 3.9
- field control: target step +0.157 (W1 +0.234); neighbours N=106, median -0.002, robust sigma 0.017, max +0.264; z = 9.2
- centroid: jump at onset 0.052" +- 0.012 (4.5 sigma, PA 19); largest consecutive-visit jump 0.049"; rms 0.026"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.371, W2-W3 0.655 (W3 S/N 0.5), W3-W4 2.409 (W4 S/N 1.3), ext_flg 0, ph_qual AAUU: W3 S/N < 5: no W2-W3 class; W1-W2 > 0.25
- Gaia: RUWE 1.32, ipd_frac_multi_peak 52, NSS none, Teff nan K, logg nan, H-alpha pEW -0.092 nm, varclass YSO(0.53); M_G 5.73, -1.67 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): V* V2664 Ori [TT*; *,MIR,NIR,Or*,TT*,V*,Y*O] 0.02" refs=34
- ASAS-SN: 1470 points, cameras bA(g,155); bE(g,218); ba(V,179, d=+0.029); be(V,195, d=-0.017); bi(g,321); bm(g,239); bq(g,163); change at onset (after-before, per-camera median) +0.006 mag; largest seasonal dimming 0.06 mag at MJD 57707
- dust: excess flux W1 4.88 mJy, W2 3.00 mJy, T = 4463 K (16-84%: 3166-8000) 

### uid1549324  [D2]  YOUNG
- position 83.10680 +12.60979; Gaia DR3 3341024964724305152; G 13.93, BP-RP 1.71, plx 2.58 mas; plot `plots/uid1549324.png`
- **young:** SIMBAD young-star types Or*,Y*O (Haro 6-65) | Gaia DR3 variability class YSO(0.42)
- flags: 1.67 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | possible optical brightening at onset (-0.104 mag, one camera only) | largest seasonal optical dimming 0.22 mag (MJD 60044)
- NEOWISE: score refetch 0.90 (stored 0.90, reproduced True); dW2 0.075, dW1 0.060, 18 visits, 160 points; baseline W1 9.84, W1-W2 0.346; onset between MJD 57282 and 57447
- detector 2: excess 0.386 mag, z 12.8, jitter ratio 7.6
- field control: target step +0.159 (W1 +0.160); neighbours N=105, median -0.006, robust sigma 0.019, max +0.129; z = 8.9
- centroid: jump at onset 0.022" +- 0.016 (1.4 sigma, PA 157); largest consecutive-visit jump 0.068"; rms 0.030"; toward neighbour: none; expected shift if a neighbour were the source: 6.3" G20.9: 0.85"
- AllWISE 2010: W1-W2 0.331, W2-W3 2.073 (W3 S/N 52.3), W3-W4 2.064 (W4 S/N 30.5), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.02, ipd_frac_multi_peak 0, NSS none, Teff 5020 K, logg 4.17, H-alpha pEW -1.413 nm, varclass YSO(0.42); M_G 5.99, -1.67 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 6.3" PA280 G20.89 dG+6.95
- SIMBAD (10"): Haro 6-65 [Or*; *,Em*,NIR,Or*,V*,Y*O] 0.05" refs=29
- ASAS-SN: 863 points, cameras bD(g,201); bH(g,111); bd(V,170, d=-0.104); bl(g,182); bp(g,94); bt(g,105); change at onset (after-before, per-camera median) -0.104 mag; largest seasonal dimming 0.22 mag at MJD 60044
- dust: excess flux W1 3.57 mJy, W2 2.51 mJy, T = 2533 K (16-84%: 1960-3709) 

### uid1427668  [D2]  YOUNG
- position 83.83302 +10.04348; Gaia DR3 3338005877593749120; G 15.17, BP-RP 2.19, plx 2.65 mas; plot `plots/uid1427668.png`
- **young:** SIMBAD young-star types Or*,Y*O ([DM99]  33)
- flags: 1.74 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | not plain dust: optical brightening -0.299 mag (per-camera -0.176,-0.261,-0.337,-0.451) together with the infrared rise | largest seasonal optical dimming 0.22 mag (MJD 58438)
- NEOWISE: score refetch 1.30 (stored 1.30, reproduced True); dW2 0.213, dW1 0.168, 21 visits, 235 points; baseline W1 10.69, W1-W2 0.609; onset between MJD 58536 and 58742
- detector 2: excess 0.577 mag, z 13.4, jitter ratio 14.2
- field control: target step +0.118 (W1 +0.086); neighbours N=121, median +0.000, robust sigma 0.013, max +0.069; z = 8.8
- centroid: jump at onset 0.022" +- 0.020 (1.1 sigma, PA 296); largest consecutive-visit jump 0.057"; rms 0.036"; toward neighbour: none; expected shift if a neighbour were the source: 6.0" G20.5: 0.61"
- AllWISE 2010: W1-W2 0.591, W2-W3 2.284 (W3 S/N 56.7), W3-W4 1.667 (W4 S/N 25.6), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.12, ipd_frac_multi_peak 0, NSS none, Teff 3620 K, logg 4.01, H-alpha pEW -0.642 nm, varclass none; M_G 7.29, -1.74 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 6.0" PA47 G20.50 dG+5.33
- SIMBAD (10"): [DM99]  33 [Or*; *,LM*,NIR,Or*,Y*O,ev] 0.07" refs=35
- ASAS-SN: 909 points, cameras bA(g,179, d=-0.176); bE(g,120, d=-0.261); ba(V,153); bi(g,227, d=-0.337); bm(g,114); bq(g,116, d=-0.451); change at onset (after-before, per-camera median) -0.299 mag; largest seasonal dimming 0.22 mag at MJD 58438
- dust: excess flux W1 3.37 mJy, W2 3.74 mJy, T = 1156 K (16-84%: 1075-1247) 

### uid1394555  [D2]  YOUNG
- position 81.41583 -4.18394; Gaia DR3 3210586361269300992; G 14.79, BP-RP 1.61, plx 2.66 mas; plot `plots/uid1394555.png`
- **young:** SIMBAD young-star types Or*,TT*,Y*?,Y*O (Kiso A-0975  86) | Gaia DR3 variability class YSO(0.26)
- flags: AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.50 mag (MJD 57116)
- NEOWISE: score refetch 0.74 (stored 0.74, reproduced True); dW2 0.143, dW1 0.193, 15 visits, 204 points; baseline W1 10.88, W1-W2 0.558; onset between MJD 57809 and 58011
- detector 2: excess 0.609 mag, z 23.4, jitter ratio 15.6
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
- detector 2: excess 0.387 mag, z 20.1, jitter ratio 10.4
- field control: target step +0.086 (W1 +0.134); neighbours N=97, median -0.003, robust sigma 0.010, max +0.026; z = 8.5
- centroid: jump at onset 0.005" +- 0.013 (0.4 sigma, PA 273); largest consecutive-visit jump 0.068"; rms 0.028"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.343, W2-W3 2.548 (W3 S/N 60.5), W3-W4 1.927 (W4 S/N 30.5), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.14, ipd_frac_multi_peak 0, NSS none, Teff 4911 K, logg 4.14, H-alpha pEW -0.332 nm, varclass YSO(0.45); M_G 5.03, -1.62 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): [DM99] 122 [Or*; *,Em*,NIR,Opt,Or*,Y*?,Y*O] 0.02" refs=27
- ASAS-SN: 939 points, cameras bA(g,184); bE(g,120); ba(V,156, d=+0.028); bi(g,236); bm(g,122); bq(g,121); change at onset (after-before, per-camera median) +0.028 mag; largest seasonal dimming 0.05 mag at MJD 57788
- dust: excess flux W1 3.90 mJy, W2 2.17 mJy, T = 8000 K (16-84%: 4443-8000) ratio bluer than an 8000 K blackbody (not dust-like)

### uid1573660  [D2]  YOUNG
- position 83.76547 -4.84807; Gaia DR3 3209575600846656128; G 14.54, BP-RP 2.07, plx 2.57 mas; plot `plots/uid1573660.png`
- **young:** SIMBAD young-star types Or*,TT*,Y*O (V* BY Ori)
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | 2.08 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | optical dimming +0.069 mag after the infrared onset (debris transit signature) | largest seasonal optical dimming 0.13 mag (MJD 57707)
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 9 visits, 81 points; baseline W1 8.39, W1-W2 0.540; onset between MJD 57088 and 57811
- detector 2: excess 0.523 mag, z 12.2, jitter ratio 25.4
- field control: target step +0.460 (W1 +0.353); neighbours N=80, median -0.007, robust sigma 0.057, max +0.441; z = 8.2
- centroid: jump at onset 0.092" +- 0.037 (2.4 sigma, PA 41); largest consecutive-visit jump 0.075"; rms 0.048"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.463, W2-W3 1.933 (W3 S/N 33.9), W3-W4 1.629 (W4 S/N 2.0), ext_flg 1, ph_qual AAAC: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.26, ipd_frac_multi_peak 0, NSS none, Teff 5823 K, logg 4.17, H-alpha pEW -1.738 nm, varclass none; M_G 6.60, -2.08 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): V* BY Ori [TT*; *,Em*,MIR,NIR,Or*,TT*,V*,X,Y*O] 0.02" refs=38
- ASAS-SN: 1250 points, cameras bA(g,151); bE(g,214); ba(V,161, d=+0.058); be(V,194, d=+0.080); bi(g,234); bm(g,177); bq(g,119); change at onset (after-before, per-camera median) +0.069 mag; largest seasonal dimming 0.13 mag at MJD 57707
- dust: excess flux W1 40.18 mJy, W2 45.03 mJy, T = 1142 K (16-84%: 1105-1180) 

### uid1614572  [D2]  YOUNG
- position 83.90185 -5.56977; Gaia DR3 3017346127547506048; G 14.32, BP-RP 2.05, plx 2.55 mas; plot `plots/uid1614572.png`
- **young:** SIMBAD young-star types Or*,TT*,TT?,Y*O (V* V568 Ori) | Gaia DR3 variability class YSO(0.19)
- flags: 2.25 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 0.56 (stored 0.56, reproduced True); dW2 0.169, dW1 0.206, 19 visits, 174 points; baseline W1 9.84, W1-W2 0.589; onset between MJD 58168 and 58377
- detector 2: excess 0.575 mag, z 13.6, jitter ratio 18.3
- field control: target step +0.260 (W1 +0.360); neighbours N=112, median -0.001, robust sigma 0.032, max +0.349; z = 8.1
- centroid: jump at onset 0.046" +- 0.023 (2.0 sigma, PA 22); largest consecutive-visit jump 0.092"; rms 0.032"; toward neighbour: 8.8" PA345 G20.6 (angle 37 deg); expected shift if a neighbour were the source: 8.2" G19.5: 1.74"; 8.3" G18.2: 1.77"; 8.8" G20.6: 1.88"
- AllWISE 2010: W1-W2 0.577, W2-W3 2.013 (W3 S/N 8.9), W3-W4 2.712 (W4 S/N -0.3), ext_flg 0, ph_qual AABU: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.19, ipd_frac_multi_peak 0, NSS none, Teff 6069 K, logg 4.16, H-alpha pEW -2.171 nm, varclass YSO(0.19); M_G 6.36, -2.25 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 8.2" PA166 G19.46 dG+5.14; 8.3" PA174 G18.15 dG+3.83; 8.8" PA345 G20.64 dG+6.32
- SIMBAD (10"): V* V568 Ori [TT*; *,Em*,MIR,NIR,Or*,Rad,TT*,TT?,V*,X,Y*O] 0.03" refs=63; 2MASS J05353652-0534193 [*; *,Em*,NIR,Y*O] 8.22" refs=11; [DRS2009] 2110 [*; *,NIR] 8.87" refs=2
- ASAS-SN: 1149 points, cameras bA(g,148); bE(g,215); ba(V,140); be(V,194); bi(g,179, d=-0.021); bm(g,155, d=+0.061); bq(g,118, d=+0.037); change at onset (after-before, per-camera median) +0.037 mag; largest seasonal dimming 0.03 mag at MJD 59156
- dust: excess flux W1 9.56 mJy, W2 7.00 mJy, T = 2284 K (16-84%: 2020-2636) 

### uid1424151  [D2]  YOUNG
- position 85.02105 -6.49019; Gaia DR3 3016991122718336128; G 14.81, BP-RP 1.93, plx 2.65 mas; plot `plots/uid1424151.png`
- **young:** SIMBAD young-star types Or*,Y*?,Y*O (V* V1188 Ori)
- flags: 1.33 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.56 mag (MJD 60680)
- NEOWISE: score refetch 1.00 (stored 1.00, reproduced True); dW2 0.205, dW1 0.202, 21 visits, 241 points; baseline W1 10.11, W1-W2 0.586; onset between MJD 58536 and 58743
- detector 2: excess 0.592 mag, z 15.2, jitter ratio 12.0
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
- detector 2: excess 0.421 mag, z 20.3, jitter ratio 9.4
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
- detector 2: excess 0.347 mag, z 34.6, jitter ratio 12.5
- field control: target step +0.111 (W1 +0.118); neighbours N=98, median -0.003, robust sigma 0.015, max +0.295; z = 7.5
- centroid: jump at onset 0.050" +- 0.010 (5.1 sigma, PA 69); largest consecutive-visit jump 0.097"; rms 0.024"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.291, W2-W3 4.195 (W3 S/N 73.2), W3-W4 2.794 (W4 S/N 68.0), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 0.83, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW -0.007 nm, varclass none; M_G 2.50, -1.57 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): HD 294268 [Y*O; *,IR,NIR,X,Y*O] 0.04" refs=48
- ASAS-SN: 1466 points, cameras bC(g,150); bG(g,223); ba(V,51); bc(V,148, d=+0.076); be(V,38, d=+0.052); bg(V,153); bk(g,311); bo(g,230); bs(g,162); change at onset (after-before, per-camera median) +0.064 mag; largest seasonal dimming 0.44 mag at MJD 56542
- dust: excess flux W1 16.51 mJy, W2 14.92 mJy, T = 1505 K (16-84%: 1370-1669) 

### uid1544243  [D2]  YOUNG
- position 84.25994 -5.60825; Gaia DR3 3017295962329600640; G 12.22, BP-RP 1.09, plx 2.59 mas; plot `plots/uid1544243.png`
- **young:** SIMBAD young-star types Or*,Y*O (V* V381 Ori) | Gaia DR3 variability class YSO(0.47)
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | 1.59 mag above the main sequence at its colour
- NEOWISE: score refetch 0.16 (stored 0.16, reproduced True); dW2 0.070, dW1 0.090, 20 visits, 191 points; baseline W1 8.90, W1-W2 0.378; onset between MJD 58014 and 58168
- detector 2: excess 0.434 mag, z 26.6, jitter ratio 34.3
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
- detector 2: excess 0.428 mag, z 19.1, jitter ratio 13.0
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
- detector 2: excess 0.482 mag, z 17.6, jitter ratio 15.3
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
- detector 2: excess 0.436 mag, z 22.1, jitter ratio 7.7
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
- detector 2: excess 0.674 mag, z 23.9, jitter ratio 9.6
- field control: target step +0.137 (W1 +0.153); neighbours N=124, median -0.004, robust sigma 0.021, max +0.168; z = 6.7
- centroid: jump at onset 0.039" +- 0.018 (2.2 sigma, PA 321); largest consecutive-visit jump 0.088"; rms 0.032"; toward neighbour: none; expected shift if a neighbour were the source: 8.6" G18.2: 1.02"
- AllWISE 2010: W1-W2 0.613, W2-W3 2.479 (W3 S/N 73.0), W3-W4 1.827 (W4 S/N 46.0), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.36, ipd_frac_multi_peak 0, NSS none, Teff 6046 K, logg 3.78, H-alpha pEW -1.832 nm, varclass YSO(0.37); M_G 5.14, -2.43 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 8.6" PA84 G18.24 dG+5.12
- SIMBAD (10"): V* BO Ori [TT*; *,Em*,IR,MIR,NIR,Opt,Or*,Pu*,SB*,TT*,V*,X,Y*O] 0.02" refs=62; 2MASS J05354368-0424547 [Y*O; *,NIR,Y*O] 8.55" refs=5
- ASAS-SN: 1164 points, cameras bA(g,148); bE(g,214); ba(V,137, d=+0.053); be(V,194, d=-0.060); bi(g,197); bm(g,156); bq(g,118); change at onset (after-before, per-camera median) -0.004 mag; largest seasonal dimming 0.09 mag at MJD 58702
- dust: excess flux W1 19.01 mJy, W2 15.80 mJy, T = 1730 K (16-84%: 1531-1986) 

### uid1369970  [D2]  YOUNG
- position 82.39255 +12.93931; Gaia DR3 3389113514514547840; G 13.93, BP-RP 2.11, plx 2.68 mas; plot `plots/uid1369970.png`
- **young:** SIMBAD young-star types Or*,Y*?,Y*O (V* V442 Ori) | Gaia DR3 variability class YSO(0.32)
- flags: 2.73 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | not plain dust: optical brightening -0.023 mag (per-camera -0.046,-0.023,-0.001) together with the infrared rise
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 21 visits, 181 points; baseline W1 9.15, W1-W2 0.488; onset between MJD 58534 and 58741
- detector 2: excess 0.465 mag, z 10.8, jitter ratio 7.0
- field control: target step +0.090 (W1 +0.077); neighbours N=95, median +0.001, robust sigma 0.013, max +0.059; z = 6.6
- centroid: jump at onset 0.009" +- 0.025 (0.4 sigma, PA 61); largest consecutive-visit jump 0.055"; rms 0.039"; toward neighbour: 8.4" PA40 G19.5 (angle 21 deg); expected shift if a neighbour were the source: 8.4" G19.5: 0.66"
- AllWISE 2010: W1-W2 0.486, W2-W3 1.873 (W3 S/N 63.5), W3-W4 2.150 (W4 S/N 36.8), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.19, ipd_frac_multi_peak 0, NSS none, Teff 6124 K, logg 3.86, H-alpha pEW -3.822 nm, varclass YSO(0.32); M_G 6.06, -2.73 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 8.4" PA40 G19.54 dG+5.61
- SIMBAD (10"): V* V442 Ori [Or*; *,Em*,EmO,IR,NIR,Or*,V*,Y*?,Y*O,ev] 0.04" refs=30
- ASAS-SN: 851 points, cameras bD(g,195, d=-0.046); bH(g,114); bd(V,170); bl(g,179, d=-0.023); bp(g,91); bt(g,102, d=-0.001); change at onset (after-before, per-camera median) -0.023 mag; largest seasonal dimming 0.06 mag at MJD 60402
- dust: excess flux W1 4.86 mJy, W2 3.54 mJy, T = 2320 K (16-84%: 1708-3929) 

### uid1564349  [D2]  YOUNG
- position 83.72103 -5.05754; Gaia DR3 3209533166569829504; G 14.24, BP-RP 1.79, plx 2.58 mas; plot `plots/uid1564349.png`
- **young:** SIMBAD young-star types Or*,TT*,TT?,Y*O (V* YZ Ori) | Gaia DR3 variability class YSO(0.40)
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | 1.59 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.19 mag (MJD 59627)
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 19 visits, 176 points; baseline W1 10.08, W1-W2 0.577; onset between MJD 57646 and 57811
- detector 2: excess 0.605 mag, z 17.9, jitter ratio 4.9
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
- detector 2: excess 0.609 mag, z 27.9, jitter ratio 5.9
- field control: target step +0.163 (W1 +0.135); neighbours N=126, median -0.010, robust sigma 0.029, max +0.170; z = 6.1
- centroid: jump at onset 0.026" +- 0.016 (1.7 sigma, PA 130); largest consecutive-visit jump 0.084"; rms 0.028"; toward neighbour: 6.3" PA170 G20.3 (angle 40 deg); expected shift if a neighbour were the source: 6.3" G20.3: 0.88"; 9.5" G20.8: 1.32"
- AllWISE 2010: W1-W2 0.599, W2-W3 2.466 (W3 S/N 30.2), W3-W4 2.101 (W4 S/N 21.4), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.09, ipd_frac_multi_peak 0, NSS none, Teff 5322 K, logg 4.16, H-alpha pEW -1.141 nm, varclass RS(0.70); M_G 5.26, -1.87 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 6.3" PA170 G20.35 dG+7.12; 9.5" PA319 G20.84 dG+7.61
- SIMBAD (10"): V* V501 Ori [TT*; *,Em*,MIR,NIR,Or*,TT*,TT?,V*,Y*O] 0.03" refs=45
- ASAS-SN: 1307 points, cameras bA(g,151); bE(g,217); ba(V,160, d=+0.018); be(V,195, d=-0.056); bi(g,235); bm(g,195); bq(g,154); change at onset (after-before, per-camera median) -0.019 mag; largest seasonal dimming 0.09 mag at MJD 59685
- dust: excess flux W1 10.77 mJy, W2 10.92 mJy, T = 1283 K (16-84%: 1186-1397) 

### uid1252374  [D2]  YOUNG
- position 121.98109 -47.12941; Gaia DR3 5519263533510676224; G 13.10, BP-RP 1.37, plx 2.74 mas; plot `plots/uid1252374.png`
- **young:** SIMBAD young-star types Or*,Y*?,Y*O (2MASS J08075546-4707460) | Gaia DR3 variability class YSO(0.20)
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | 1.47 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 0.37 (stored 0.37, reproduced True); dW2 0.077, dW1 0.078, 14 visits, 167 points; baseline W1 9.90, W1-W2 0.335; onset between MJD 57152 and 57346
- detector 2: excess 0.398 mag, z 20.6, jitter ratio 16.9
- field control: target step +0.058 (W1 +0.085); neighbours N=200, median -0.005, robust sigma 0.011, max +0.227; z = 5.8
- centroid: jump at onset 0.037" +- 0.022 (1.7 sigma, PA 120); largest consecutive-visit jump 0.073"; rms 0.037"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.319, W2-W3 1.508 (W3 S/N 63.8), W3-W4 2.797 (W4 S/N 42.3), ext_flg 1, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.08, ipd_frac_multi_peak 0, NSS none, Teff 4721 K, logg 4.15, H-alpha pEW -0.274 nm, varclass YSO(0.20); M_G 5.29, -1.47 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): 2MASS J08075546-4707460 [Or*; *,NIR,Or*,Y*?,Y*O] 0.17" refs=28
- ASAS-SN: 2553 points, cameras bE(g,421); bF(g,373); be(V,231); bf(V,186); bi(g,526); bj(g,427); bm(g,207); bn(g,182); change at onset (after-before, per-camera median) n/a mag; largest seasonal dimming 0.04 mag at MJD 60256
- dust: excess flux W1 2.89 mJy, W2 1.80 mJy, T = 4152 K (16-84%: 2094-8000) 
- checks missing: ASAS-SN change at onset (no camera spans the onset)

### uid1600353  [D2]  YOUNG
- position 82.49688 +12.32972; Gaia DR3 3340944352481408512; G 12.68, BP-RP 1.58, plx 2.56 mas; plot `plots/uid1600353.png`
- **young:** SIMBAD young-star types TT?,Y*O (UCAC2  36062792) | Gaia DR3 variability class YSO(0.28)
- flags: 2.59 mag above the main sequence at its colour | largest seasonal optical dimming 0.20 mag (MJD 58498)
- NEOWISE: score refetch 0.87 (stored 0.87, reproduced True); dW2 0.128, dW1 0.091, 19 visits, 175 points; baseline W1 9.01, W1-W2 0.207; onset between MJD 58168 and 58377
- detector 2: excess 0.261 mag, z 10.9, jitter ratio 13.2
- field control: target step +0.052 (W1 +0.049); neighbours N=95, median -0.004, robust sigma 0.010, max +0.028; z = 5.7
- centroid: jump at onset 0.023" +- 0.025 (0.9 sigma, PA 91); largest consecutive-visit jump 0.032"; rms 0.027"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.226, W2-W3 2.016 (W3 S/N 33.7), W3-W4 3.130 (W4 S/N 29.1), ext_flg 0, ph_qual AAAA: W3 excess only (W2-W3 > 1.0; debris-disk-like or blend)
- Gaia: RUWE 1.02, ipd_frac_multi_peak 0, NSS none, Teff 5036 K, logg 3.73, H-alpha pEW -0.120 nm, varclass YSO(0.28); M_G 4.72, -2.59 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): UCAC2  36062792 [Y*O; *,NIR,TT?,Y*O] 0.00" refs=13
- ASAS-SN: 854 points, cameras bD(g,197); bH(g,114); bd(V,169, d=+0.010); bl(g,179); bp(g,93); bt(g,102); change at onset (after-before, per-camera median) +0.010 mag; largest seasonal dimming 0.20 mag at MJD 58498
- dust: excess flux W1 6.60 mJy, W2 6.12 mJy, T = 1450 K (16-84%: 1265-1697) 

### uid1551109  [D2]  YOUNG
- position 84.10098 -5.74686; Gaia DR3 3017199170935143680; G 13.73, BP-RP 1.74, plx 2.58 mas; plot `plots/uid1551109.png`
- **young:** SIMBAD young-star types Or*,TT*,Y*O (V* V1607 Ori) | Gaia DR3 variability class YSO(0.54)
- flags: 1.95 mag above the main sequence at its colour
- NEOWISE: score refetch 0.60 (stored 0.60, reproduced True); dW2 0.041, dW1 0.047, 20 visits, 194 points; baseline W1 10.50, W1-W2 0.293; onset between MJD 58377 and 58535
- detector 2: excess 0.329 mag, z 10.4, jitter ratio 5.5
- field control: target step +0.146 (W1 +0.118); neighbours N=144, median -0.001, robust sigma 0.026, max +0.288; z = 5.7
- centroid: jump at onset 0.032" +- 0.019 (1.7 sigma, PA 137); largest consecutive-visit jump 0.104"; rms 0.032"; toward neighbour: none; expected shift if a neighbour were the source: 8.2" G20.4: 1.03"
- AllWISE 2010: W1-W2 0.243, W2-W3 2.176 (W3 S/N 10.4), W3-W4 1.656 (W4 S/N 3.9), ext_flg 0, ph_qual AAAB: W3 excess only (W2-W3 > 1.0; debris-disk-like or blend)
- Gaia: RUWE 1.12, ipd_frac_multi_peak 0, NSS none, Teff 4913 K, logg 4.14, H-alpha pEW -0.416 nm, varclass YSO(0.54); M_G 5.79, -1.95 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 8.2" PA279 G20.45 dG+6.72
- SIMBAD (10"): V* V1607 Ori [TT*; *,MIR,NIR,Or*,TT*,V*,Y*O] 0.01" refs=35
- ASAS-SN: 0 points, cameras n/a; change at onset (after-before, per-camera median) n/a mag; largest seasonal dimming n/a mag at MJD n/a
- dust: excess flux W1 1.60 mJy, W2 1.47 mJy, T = 1476 K (16-84%: 1281-1749) 
- checks missing: ASAS-SN (no source)

### uid1393011  [D2]  YOUNG
- position 82.63189 +2.05143; Gaia DR3 3223556647106159232; G 14.40, BP-RP 1.77, plx 2.66 mas; plot `plots/uid1393011.png`
- **young:** SIMBAD young-star types TT*,TT?,Y*?,Y*O (Kiso A-0903 195) | Gaia DR3 variability class YSO(0.52)
- flags: 1.30 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | possible optical brightening at onset (-0.061 mag, one camera only) | largest seasonal optical dimming 0.25 mag (MJD 60603)
- NEOWISE: score refetch 0.87 (stored 0.87, reproduced True); dW2 0.142, dW1 0.190, 21 visits, 239 points; baseline W1 9.96, W1-W2 0.431; onset between MJD 57087 and 57281
- detector 2: excess 0.463 mag, z 14.2, jitter ratio 13.5
- field control: target step +0.052 (W1 +0.109); neighbours N=82, median -0.003, robust sigma 0.010, max +0.028; z = 5.5
- centroid: jump at onset 0.009" +- 0.015 (0.6 sigma, PA 18); largest consecutive-visit jump 0.044"; rms 0.025"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.371, W2-W3 1.929 (W3 S/N 58.5), W3-W4 2.228 (W4 S/N 28.8), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.18, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW -2.268 nm, varclass YSO(0.52); M_G 6.53, -1.30 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): Kiso A-0903 195 [TT*; *,Em*,MIR,NIR,TT*,TT?,V*,Y*?,Y*O] 0.03" refs=21
- ASAS-SN: 1232 points, cameras bA(g,168); bE(g,175); ba(V,210, d=-0.061); be(V,56); bi(g,279); bm(g,213); bq(g,131); change at onset (after-before, per-camera median) -0.061 mag; largest seasonal dimming 0.25 mag at MJD 60603
- dust: excess flux W1 6.09 mJy, W2 2.72 mJy, T = 8000 K (16-84%: 8000-8000) ratio bluer than an 8000 K blackbody (not dust-like)

### uid1616399  [D2]  YOUNG
- position 84.00076 -6.70943; Gaia DR3 3016926045373231616; G 13.74, BP-RP 1.78, plx 2.55 mas; plot `plots/uid1616399.png`
- **young:** SIMBAD young-star types Or*,TT*,Y*O (V* AV Ori) | Gaia DR3 variability class YSO(0.45)
- flags: binary type in SIMBAD (**, V* AV Ori) | 2.06 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.69 mag (MJD 56618)
- NEOWISE: score refetch 0.23 (stored 0.23, reproduced True); dW2 0.029, dW1 0.069, 20 visits, 192 points; baseline W1 8.61, W1-W2 0.558; onset between MJD 58899 and 59109
- detector 2: excess 0.589 mag, z 18.1, jitter ratio 11.0
- field control: target step +0.060 (W1 +0.106); neighbours N=103, median +0.000, robust sigma 0.011, max +0.233; z = 5.4
- centroid: jump at onset 0.017" +- 0.037 (0.5 sigma, PA 49); largest consecutive-visit jump 0.084"; rms 0.053"; toward neighbour: none; expected shift if a neighbour were the source: 6.1" G17.0: 0.33"
- AllWISE 2010: W1-W2 0.507, W2-W3 1.412 (W3 S/N 48.4), W3-W4 1.695 (W4 S/N 17.9), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.29, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW -2.171 nm, varclass YSO(0.45); M_G 5.77, -2.06 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 6.1" PA304 G17.03 dG+3.29
- SIMBAD (10"): V* AV Ori [Or*; *,**,Em*,IR,MIR,NIR,Opt,Or*,TT*,V*,Y*O] 0.02" refs=72; V* V819 Ori [Or*; *,**,Em*,G,MIR,NIR,Opt,Or*,V*,Y*O] 6.08" refs=22
- ASAS-SN: 1253 points, cameras bA(g,151, d=+0.033); bE(g,215, d=+0.145); ba(V,167); be(V,193); bi(g,207, d=+0.516); bm(g,176); bq(g,144, d=-0.426); change at onset (after-before, per-camera median) +0.089 mag; largest seasonal dimming 0.69 mag at MJD 56618
- dust: excess flux W1 9.69 mJy, W2 2.92 mJy, T = 8000 K (16-84%: 8000-8000) ratio bluer than an 8000 K blackbody (not dust-like)

### uid1642569  [D2]  YOUNG
- position 83.88698 -5.50596; Gaia DR3 3017347398857791104; G 14.32, BP-RP 1.86, plx 2.54 mas; plot `plots/uid1642569.png`
- **young:** SIMBAD young-star types Or*,TT?,Y*?,Y*O (V* NX Ori)
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | 1.72 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 0.28 (stored 0.28, reproduced True); dW2 0.034, dW1 0.111, 19 visits, 145 points; baseline W1 8.98, W1-W2 0.446; onset between MJD 58741 and 58899
- detector 2: excess 0.464 mag, z 12.7, jitter ratio 10.8
- field control: target step +0.205 (W1 +0.230); neighbours N=93, median -0.006, robust sigma 0.040, max +0.448; z = 5.3
- centroid: jump at onset 0.050" +- 0.025 (2.0 sigma, PA 84); largest consecutive-visit jump 0.048"; rms 0.038"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.497, W2-W3 2.391 (W3 S/N 29.0), W3-W4 2.419 (W4 S/N 6.2), ext_flg 1, ph_qual AAAB: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.16, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW -0.825 nm, varclass none; M_G 6.34, -1.72 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): V* NX Ori [Or*; *,Em*,MIR,NIR,Or*,Rad,TT?,V*,X,Y*?,Y*O] 0.04" refs=49; HH 876 [HH; HH] 0.58" refs=2; [SKN2015] AzTEC-Ori 347 [mm; cor,mm] 3.48" refs=1
- ASAS-SN: 1148 points, cameras bA(g,149, d=+0.020); bE(g,215, d=-0.016); ba(V,140); be(V,194); bi(g,187); bm(g,156, d=+0.010); bq(g,107, d=-0.018); change at onset (after-before, per-camera median) -0.003 mag; largest seasonal dimming 0.08 mag at MJD 57614
- dust: excess flux W1 10.13 mJy, W2 4.77 mJy, T = 8000 K (16-84%: 8000-8000) ratio bluer than an 8000 K blackbody (not dust-like)

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

### uid1616156  [D2]  YOUNG
- position 83.96928 -5.08489; Gaia DR3 3209530280351892096; G 11.35, BP-RP 1.10, plx 2.55 mas; plot `plots/uid1616156.png`
- **young:** SIMBAD young-star types Or*,Y*O (V* V815 Ori) | Gaia DR3 variability class YSO(0.79)
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | 2.51 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 0.21 (stored 0.21, reproduced True); dW2 0.027, dW1 -0.016, 19 visits, 160 points; baseline W1 8.00, W1-W2 0.328; onset between MJD 58899 and 59109
- detector 2: excess 0.384 mag, z 23.6, jitter ratio 9.5
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
- detector 2: excess 0.510 mag, z 18.1, jitter ratio 7.6
- field control: target step +0.151 (W1 +0.128); neighbours N=62, median -0.011, robust sigma 0.039, max +0.438; z = 4.1
- centroid: jump at onset 0.037" +- 0.025 (1.5 sigma, PA 59); largest consecutive-visit jump 0.076"; rms 0.034"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.503, W2-W3 3.147 (W3 S/N 16.0), W3-W4 3.616 (W4 S/N 9.5), ext_flg 0, ph_qual AAAB: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.05, ipd_frac_multi_peak 0, NSS none, Teff 5778 K, logg 4.28, H-alpha pEW -2.929 nm, varclass YSO(0.28); M_G 6.15, -1.41 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): V* AL Ori [TT*; *,Em*,IR,MIR,NIR,Or*,TT*,V*,X,Y*O] 0.04" refs=69
- ASAS-SN: 1138 points, cameras bA(g,148); bE(g,214); ba(V,139); be(V,194, d=+0.067); bi(g,179); bm(g,152); bq(g,112); change at onset (after-before, per-camera median) +0.067 mag; largest seasonal dimming 0.12 mag at MJD 56618
- dust: excess flux W1 4.04 mJy, W2 3.16 mJy, T = 1951 K (16-84%: 1535-2684) 

### uid1281030  [D2]  YOUNG
- position 70.57174 +37.66241; Gaia DR3 175539303414648448; G 13.52, BP-RP 1.77, plx 2.73 mas; plot `plots/uid1281030.png`
- **young:** SIMBAD young-star types Y*? (UCAC4 639-018918) | Gaia DR3 variability class YSO(0.43)
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | 2.13 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | optical dimming +0.063 mag after the infrared onset (debris transit signature) | largest seasonal optical dimming 0.19 mag (MJD 60556)
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 18 visits, 161 points; baseline W1 9.42, W1-W2 0.363; onset between MJD 57439 and 57638
- detector 2: excess 0.394 mag, z 12.1, jitter ratio 29.2
- field control: target step +0.047 (W1 +0.043); neighbours N=132, median +0.000, robust sigma 0.011, max +0.047; z = 4.0
- centroid: jump at onset 0.029" +- 0.016 (1.8 sigma, PA 292); largest consecutive-visit jump 0.072"; rms 0.035"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.405, W2-W3 1.177 (W3 S/N 52.8), W3-W4 3.435 (W4 S/N 37.8), ext_flg 1, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.27, ipd_frac_multi_peak 0, NSS none, Teff 4923 K, logg 4.13, H-alpha pEW -0.196 nm, varclass YSO(0.43); M_G 5.70, -2.13 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): UCAC4 639-018918 [Y*?; *,MIR,NIR,Y*?] 0.11" refs=2; [MJR2015] 1179 [Y*O; IR,Y*O] 6.66" refs=1
- ASAS-SN: 587 points, cameras bC(g,236); bc(V,175, d=+0.063); bs(g,176); change at onset (after-before, per-camera median) +0.063 mag; largest seasonal dimming 0.19 mag at MJD 60556
- dust: excess flux W1 -3.83 mJy, W2 -2.80 mJy, T = n/a K (16-84%: n/a-n/a) no W2 excess flux after onset

### uid1357327  [D2]  YOUNG
- position 83.65061 -6.09298; Gaia DR3 3017163539886560768; G 14.72, BP-RP 1.68, plx 2.68 mas; plot `plots/uid1357327.png`
- **young:** SIMBAD young-star types Or*,TT*,Y*O (V* XX Ori) | Gaia DR3 variability class YSO(0.35)
- flags: AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | optical dimming +0.102 mag after the infrared onset (debris transit signature) | largest seasonal optical dimming 0.25 mag (MJD 57974)
- NEOWISE: score refetch 0.59 (stored 0.59, reproduced True); dW2 0.075, dW1 0.138, 20 visits, 183 points; baseline W1 10.17, W1-W2 0.484; onset between MJD 57087 and 57282
- detector 2: excess 0.528 mag, z 18.4, jitter ratio 9.8
- field control: target step +0.063 (W1 +0.088); neighbours N=127, median -0.003, robust sigma 0.019, max +0.177; z = 3.4
- centroid: jump at onset 0.010" +- 0.019 (0.5 sigma, PA 259); largest consecutive-visit jump 0.115"; rms 0.033"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.491, W2-W3 1.812 (W3 S/N 42.9), W3-W4 1.881 (W4 S/N 23.1), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.15, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW -2.942 nm, varclass YSO(0.35); M_G 6.86, -0.73 mag vs sequence (on the sequence); neighbours within 10": none
- SIMBAD (10"): V* XX Ori [TT*; *,Em*,Er*,MIR,NIR,Opt,Or*,TT*,V*,X,Y*O,ev] 0.03" refs=59
- ASAS-SN: 1452 points, cameras bA(g,146); bE(g,212); ba(V,179, d=+0.107); be(V,195, d=+0.098); bi(g,337); bm(g,220); bq(g,163); change at onset (after-before, per-camera median) +0.102 mag; largest seasonal dimming 0.25 mag at MJD 57974
- dust: excess flux W1 2.80 mJy, W2 1.81 mJy, T = 3441 K (16-84%: 2193-8000) 

### uid1463204  [D2]  YOUNG
- position 59.01345 +35.24735; Gaia DR3 218960529425493504; G 14.91, BP-RP 1.98, plx 2.63 mas; plot `plots/uid1463204.png`
- **young:** Gaia DR3 variability class YSO(0.57)
- flags: SIMBAD candidate type(s) CV? (UCAC4 627-013834): uncertain, not a kill | 1.40 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | optical dimming +0.055 mag after the infrared onset (debris transit signature) | largest seasonal optical dimming 0.37 mag (MJD 60309)
- NEOWISE: score refetch 0.38 (stored 0.38, reproduced True); dW2 0.071, dW1 -0.005, 20 visits, 174 points; baseline W1 9.85, W1-W2 0.444; onset between MJD 57262 and 57427
- detector 2: excess 0.442 mag, z 10.6, jitter ratio 17.2
- field control: target step +0.045 (W1 -0.013); neighbours N=84, median +0.002, robust sigma 0.014, max +0.172; z = 3.1
- centroid: jump at onset 0.015" +- 0.021 (0.7 sigma, PA 77); largest consecutive-visit jump 0.059"; rms 0.035"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.475, W2-W3 1.769 (W3 S/N 55.4), W3-W4 2.236 (W4 S/N 23.7), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.08, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW -2.512 nm, varclass YSO(0.57); M_G 7.01, -1.40 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): UCAC4 627-013834 [CV?; *,CV?,Em*,MIR,NIR,Opt] 0.09" refs=10
- ASAS-SN: 589 points, cameras bA(g,247); ba(V,160, d=+0.055); bq(g,182); change at onset (after-before, per-camera median) +0.055 mag; largest seasonal dimming 0.37 mag at MJD 60309
- dust: excess flux W1 -0.49 mJy, W2 1.18 mJy, T = 150 K (16-84%: 150-150) W1 excess <= 0: colder than ~150 K (upper limit)

### uid900210  [D2]  YOUNG
- position 83.94168 -0.96451; Gaia DR3 3217657011309526016; G 13.45, BP-RP 1.73, plx 2.97 mas; plot `plots/uid900210.png`
- **young:** SIMBAD young-star types Or*,TT*,Y*?,Y*O (Haro 5-73) | Gaia DR3 variability class YSO(0.55)
- flags: 1.91 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.21 mag (MJD 60524)
- NEOWISE: score refetch 3.91 (stored 3.91, reproduced True); dW2 0.198, dW1 0.170, 20 visits, 214 points; baseline W1 9.40, W1-W2 0.328; onset between MJD 58742 and 58900
- detector 2: excess 0.365 mag, z 11.6, jitter ratio 4.3
- field control: target step +0.044 (W1 +0.054); neighbours N=76, median +0.003, robust sigma 0.014, max +0.071; z = 2.9
- centroid: jump at onset 0.016" +- 0.013 (1.2 sigma, PA 7); largest consecutive-visit jump 0.028"; rms 0.022"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.302, W2-W3 1.963 (W3 S/N 52.7), W3-W4 2.475 (W4 S/N 28.0), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.05, ipd_frac_multi_peak 0, NSS none, Teff 5580 K, logg 4.16, H-alpha pEW -1.346 nm, varclass YSO(0.55); M_G 5.81, -1.91 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): Haro 5-73 [TT*; *,Em*,NIR,Or*,TT*,V*,Y*?,Y*O,ev] 0.03" refs=42
- ASAS-SN: 1435 points, cameras bC(g,150, d=+0.038); bG(g,222, d=+0.131); ba(V,51); bc(V,150); be(V,38); bg(V,153); bk(g,305, d=-0.123); bo(g,211, d=+0.010); bs(g,155, d=-0.173); change at onset (after-before, per-camera median) +0.010 mag; largest seasonal dimming 0.21 mag at MJD 60524
- dust: excess flux W1 3.95 mJy, W2 2.42 mJy, T = 4625 K (16-84%: 2422-8000) 

### uid1450875  [D2]  YOUNG
- position 83.54366 -4.84309; Gaia DR3 3209598548853143680; G 12.65, BP-RP 1.31, plx 2.63 mas; plot `plots/uid1450875.png`
- **young:** SIMBAD young-star types Or*,TT*,Y*O (V* V1931 Ori) | Gaia DR3 variability class YSO(0.41)
- flags: binary type in SIMBAD (**, V* V1931 Ori) | 1.84 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | not plain dust: optical brightening -0.026 mag (per-camera -0.023,-0.029) together with the infrared rise
- NEOWISE: score refetch 0.28 (stored 0.28, reproduced True); dW2 0.048, dW1 0.046, 19 visits, 165 points; baseline W1 9.23, W1-W2 0.349; onset between MJD 57282 and 57446
- detector 2: excess 0.412 mag, z 21.7, jitter ratio 15.4
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
- detector 2: excess 0.527 mag, z 16.7, jitter ratio 7.2
- field control: target step +0.066 (W1 +0.098); neighbours N=133, median -0.001, robust sigma 0.024, max +0.471; z = 2.8
- centroid: jump at onset 0.055" +- 0.031 (1.8 sigma, PA 66); largest consecutive-visit jump 0.040"; rms 0.042"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.464, W2-W3 2.148 (W3 S/N 59.3), W3-W4 3.204 (W4 S/N 21.3), ext_flg 1, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.11, ipd_frac_multi_peak 0, NSS none, Teff 4939 K, logg 4.17, H-alpha pEW -1.278 nm, varclass none; M_G 6.12, -1.61 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): V* IV Ori [Or*; *,Em*,MIR,NIR,Or*,TT?,V*,Y*O] 0.02" refs=58
- ASAS-SN: 1503 points, cameras bA(g,153, d=-0.004); bE(g,219, d=+0.059); ba(V,179); be(V,195); bi(g,344, d=+0.003); bm(g,248, d=-0.069); bq(g,165, d=-0.021); change at onset (after-before, per-camera median) -0.004 mag; largest seasonal dimming 0.11 mag at MJD 56892
- dust: excess flux W1 3.83 mJy, W2 3.05 mJy, T = 1881 K (16-84%: 1465-2696) 

### uid1511589  [D2]  YOUNG
- position 80.08108 -5.76540; Gaia DR3 3209947132696346752; G 12.10, BP-RP 1.37, plx 2.60 mas; plot `plots/uid1511589.png`
- **young:** SIMBAD young-star types Or*,TT*,Y*O (EM* StHA   37) | Gaia DR3 variability class YSO(0.28)
- flags: 2.58 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 20 visits, 213 points; baseline W1 8.09, W1-W2 0.421; onset between MJD 58006 and 58164
- detector 2: excess 0.484 mag, z 25.1, jitter ratio 8.4
- field control: target step +0.034 (W1 -0.021); neighbours N=51, median -0.004, robust sigma 0.016, max +0.081; z = 2.4
- centroid: jump at onset 0.021" +- 0.015 (1.4 sigma, PA 212); largest consecutive-visit jump 0.054"; rms 0.024"; toward neighbour: none; expected shift if a neighbour were the source: 7.0" G20.5: 0.21"
- AllWISE 2010: W1-W2 0.435, W2-W3 2.431 (W3 S/N 72.0), W3-W4 2.179 (W4 S/N 48.8), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.09, ipd_frac_multi_peak 0, NSS none, Teff 5604 K, logg 4.02, H-alpha pEW -1.403 nm, varclass YSO(0.28); M_G 4.18, -2.58 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 7.0" PA282 G20.54 dG+8.44
- SIMBAD (10"): EM* StHA   37 [TT*; *,Em*,IR,MIR,NIR,Or*,TT*,Y*O] 0.03" refs=21
- ASAS-SN: 0 points, cameras n/a; change at onset (after-before, per-camera median) n/a mag; largest seasonal dimming n/a mag at MJD n/a
- dust: excess flux W1 -8.97 mJy, W2 -6.00 mJy, T = n/a K (16-84%: n/a-n/a) no W2 excess flux after onset
- checks missing: ASAS-SN (no source)

### uid1435420  [D2]  YOUNG
- position 82.52106 -2.25645; Gaia DR3 3217043964857566464; G 14.04, BP-RP 1.60, plx 2.64 mas; plot `plots/uid1435420.png`
- **young:** SIMBAD young-star types TT*,Y*? (2MASS J05300505-0215231)
- flags: 1.20 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | optical dimming +0.069 mag after the infrared onset (debris transit signature) | largest seasonal optical dimming 0.10 mag (MJD 58190)
- NEOWISE: score refetch 0.58 (stored 0.58, reproduced True); dW2 0.098, dW1 0.130, 20 visits, 217 points; baseline W1 10.94, W1-W2 0.285; onset between MJD 57645 and 57810
- detector 2: excess 0.338 mag, z 13.5, jitter ratio 6.2
- field control: target step +0.026 (W1 +0.083); neighbours N=73, median +0.000, robust sigma 0.011, max +0.069; z = 2.3
- centroid: jump at onset 0.025" +- 0.021 (1.2 sigma, PA 242); largest consecutive-visit jump 0.018"; rms 0.034"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.251, W2-W3 2.540 (W3 S/N 37.9), W3-W4 2.319 (W4 S/N 24.2), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.16, ipd_frac_multi_peak 0, NSS none, Teff 5202 K, logg 4.28, H-alpha pEW -3.725 nm, varclass none; M_G 6.15, -1.20 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): 2MASS J05300505-0215231 [TT*; *,Em*,NIR,TT*,Y*?] 0.03" refs=10
- ASAS-SN: 2426 points, cameras bD(g,166); bG(g,222); bH(g,203); ba(V,50); bd(V,156, d=+0.069); be(V,37); bf(V,34); bg(V,153, d=+0.057); bh(V,152, d=+0.089); bk(g,310); bl(g,316); bo(g,232); bp(g,221); bt(g,174); change at onset (after-before, per-camera median) +0.069 mag; largest seasonal dimming 0.10 mag at MJD 58190
- dust: excess flux W1 1.10 mJy, W2 0.55 mJy, T = 8000 K (16-84%: 7873-8000) ratio bluer than an 8000 K blackbody (not dust-like)

### uid1505343  [D2]  YOUNG
- position 83.15619 -5.21142; Gaia DR3 3209492072320894080; G 14.83, BP-RP 2.12, plx 2.61 mas; plot `plots/uid1505343.png`
- **young:** SIMBAD young-star types Or*,TT*,Y*O (V* V383 Ori)
- flags: 1.93 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | not plain dust: optical brightening -0.069 mag (per-camera -0.066,-0.072) together with the infrared rise
- NEOWISE: score refetch 0.84 (stored 0.84, reproduced True); dW2 0.190, dW1 0.173, 20 visits, 181 points; baseline W1 10.57, W1-W2 0.740; onset between MJD 57446 and 57645
- detector 2: excess 0.714 mag, z 16.6, jitter ratio 20.2
- field control: target step +0.038 (W1 -0.054); neighbours N=75, median +0.002, robust sigma 0.016, max +0.524; z = 2.3
- centroid: jump at onset 0.006" +- 0.022 (0.3 sigma, PA 276); largest consecutive-visit jump 0.106"; rms 0.036"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.691, W2-W3 2.171 (W3 S/N 56.9), W3-W4 1.803 (W4 S/N 24.2), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.07, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW -0.091 nm, varclass none; M_G 6.91, -1.93 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): V* V383 Ori [TT*; *,BY*,Er*,MIR,NIR,Or*,TT*,V*,Y*O] 0.01" refs=24
- ASAS-SN: 1460 points, cameras bA(g,153); bE(g,217); ba(V,174, d=-0.066); be(V,194, d=-0.072); bi(g,331); bm(g,226); bq(g,165); change at onset (after-before, per-camera median) -0.069 mag; largest seasonal dimming 0.06 mag at MJD 59252
- dust: excess flux W1 5.15 mJy, W2 4.67 mJy, T = 1496 K (16-84%: 1405-1601) 

### uid1623754  [D2]  YOUNG
- position 83.51727 +12.40638; Gaia DR3 3340816401113645440; G 14.95, BP-RP 1.94, plx 2.55 mas; plot `plots/uid1623754.png`
- **young:** SIMBAD young-star types Y*O (Haro 6-71)
- flags: 1.30 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.28 mag (MJD 60044)
- NEOWISE: score refetch 0.62 (stored 0.62, reproduced True); dW2 0.056, dW1 0.066, 20 visits, 176 points; baseline W1 10.12, W1-W2 0.495; onset between MJD 58900 and 59109
- detector 2: excess 0.500 mag, z 12.7, jitter ratio 8.6
- field control: target step +0.020 (W1 +0.069); neighbours N=81, median -0.006, robust sigma 0.014, max +0.028; z = 1.8
- centroid: jump at onset 0.032" +- 0.016 (1.9 sigma, PA 206); largest consecutive-visit jump 0.039"; rms 0.029"; toward neighbour: none; expected shift if a neighbour were the source: 7.3" G20.8: 0.13"; 7.4" G21.1: 0.14"
- AllWISE 2010: W1-W2 0.458, W2-W3 1.750 (W3 S/N 51.4), W3-W4 2.082 (W4 S/N 25.2), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.12, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW -3.736 nm, varclass none; M_G 6.98, -1.30 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 7.3" PA117 G20.76 dG+5.82; 7.4" PA144 G21.11 dG+6.17
- SIMBAD (10"): Haro 6-71 [Y*O; *,Em*,NIR,V*,Y*O,ev] 0.03" refs=17
- ASAS-SN: 765 points, cameras bD(g,177, d=-0.204); bH(g,108, d=+0.078); bd(V,161); bl(g,155, d=+0.127); bp(g,76, d=-0.100); bt(g,88, d=-0.054); change at onset (after-before, per-camera median) -0.054 mag; largest seasonal dimming 0.28 mag at MJD 60044
- dust: excess flux W1 2.26 mJy, W2 1.67 mJy, T = 2210 K (16-84%: 1690-3372) 

### uid1493976  [D2]  YOUNG
- position 83.56914 -3.95624; Gaia DR3 3215869922660573568; G 12.91, BP-RP 1.39, plx 2.61 mas; plot `plots/uid1493976.png`
- **young:** SIMBAD young-star types Or*,Y*?,Y*O (V* V1937 Ori)
- flags: 1.82 mag above the main sequence at its colour | not plain dust: optical brightening -0.053 mag (per-camera -0.035,-0.045,-0.061,-0.072) together with the infrared rise
- NEOWISE: score refetch 0.86 (stored 0.86, reproduced True); dW2 0.088, dW1 0.088, 21 visits, 208 points; baseline W1 9.68, W1-W2 0.227; onset between MJD 57447 and 57646
- detector 2: excess 0.290 mag, z 14.7, jitter ratio 8.9
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
- detector 2: excess 0.736 mag, z 35.5, jitter ratio 16.2
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
- detector 2: excess 0.447 mag, z 16.3, jitter ratio 11.6
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
- detector 2: excess 0.992 mag, z 33.0, jitter ratio 3.8
- field control: target step +0.017 (W1 +0.009); neighbours N=183, median +0.009, robust sigma 0.020, max +0.099; z = 0.4
- centroid: jump at onset 0.297" +- 0.119 (2.5 sigma, PA 24); largest consecutive-visit jump 0.285"; rms 0.171"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.929, W2-W3 2.793 (W3 S/N 27.9), W3-W4 1.267 (W4 S/N 7.5), ext_flg 3, ph_qual AAAB: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.18, ipd_frac_multi_peak 0, NSS none, Teff 4182 K, logg 4.66, H-alpha pEW -0.077 nm, varclass none; M_G 7.69, +0.04 mag vs sequence (on the sequence); neighbours within 10": none
- SIMBAD (10"): WISEA J061633.49+223110.4 [Y*?; MIR,Y*?] 1.26" refs=1; WISEA J061633.23+223103.7 [Y*?; MIR,Y*?] 6.76" refs=1
- ASAS-SN: 828 points, cameras bD(g,194, d=+0.019); bH(g,93); bd(V,187); bl(g,165, d=+0.006); bp(g,55); bt(g,134, d=+0.053); change at onset (after-before, per-camera median) +0.019 mag; largest seasonal dimming 0.08 mag at MJD 57048
- dust: excess flux W1 0.03 mJy, W2 0.22 mJy, T = 412 K (16-84%: 150-631) 

### uid1547585  [D2]  YOUNG
- position 83.62313 -4.75075; Gaia DR3 3209600855254363520; G 15.81, BP-RP 2.00, plx 2.59 mas; plot `plots/uid1547585.png`
- **young:** SIMBAD young-star types Or*,Y*O (V* BV Ori)
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.38 mag (MJD 58159)
- NEOWISE: score refetch 0.54 (stored 0.54, reproduced True); dW2 0.141, dW1 0.137, 20 visits, 177 points; baseline W1 10.52, W1-W2 0.549; onset between MJD 58168 and 58377
- detector 2: excess 0.543 mag, z 13.1, jitter ratio 18.8
- field control: target step -0.000 (W1 +0.033); neighbours N=148, median -0.005, robust sigma 0.027, max +0.198; z = 0.2
- centroid: jump at onset 0.043" +- 0.018 (2.3 sigma, PA 67); largest consecutive-visit jump 0.050"; rms 0.032"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.548, W2-W3 2.257 (W3 S/N 22.8), W3-W4 2.190 (W4 S/N 12.3), ext_flg 1, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.18, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW -1.120 nm, varclass none; M_G 7.88, -0.59 mag vs sequence (on the sequence); neighbours within 10": none
- SIMBAD (10"): V* BV Ori [Or*; *,Em*,MIR,NIR,Or*,V*,V*?,Y*O] 0.01" refs=34
- ASAS-SN: 748 points, cameras bA(g,62); bE(g,111); ba(V,124, d=-0.014); be(V,118); bi(g,194, d=+0.191); bm(g,43, d=-0.340); bq(g,96, d=-0.624); change at onset (after-before, per-camera median) -0.177 mag; largest seasonal dimming 0.38 mag at MJD 58159
- dust: excess flux W1 1.62 mJy, W2 1.90 mJy, T = 1092 K (16-84%: 984-1226) 

### uid1486857  [D2]  YOUNG
- position 0.26380 +47.02299; Gaia DR3 387155327088745728; G 13.25, BP-RP 1.55, plx 2.62 mas; plot `plots/uid1486857.png`
- **young:** SIMBAD young-star types Y*? (UCAC4 686-000123) | Gaia DR3 variability class YSO(0.48)
- flags: 1.90 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 22 visits, 246 points; baseline W1 9.00, W1-W2 0.431; onset between MJD 58680 and 58840
- detector 2: excess 0.487 mag, z 21.1, jitter ratio 13.2
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
- detector 2: excess 0.392 mag, z 20.3, jitter ratio 16.1
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
- detector 2: excess 0.668 mag, z 15.5, jitter ratio 8.5
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
- detector 2: excess 0.469 mag, z 13.7, jitter ratio 14.5
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
- detector 2: excess 0.479 mag, z 15.1, jitter ratio 4.9
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
- detector 2: excess 0.566 mag, z 25.8, jitter ratio 15.7
- field control: target step -0.091 (W1 -0.017); neighbours N=92, median -0.005, robust sigma 0.013, max +0.118; z = -6.4
- centroid: jump at onset 0.015" +- 0.013 (1.1 sigma, PA 327); largest consecutive-visit jump 0.041"; rms 0.023"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.466, W2-W3 1.336 (W3 S/N 63.3), W3-W4 2.503 (W4 S/N 41.5), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.36, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW -0.211 nm, varclass none; M_G 5.36, -1.77 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): V* V993 Ori [Or*; *,MIR,NIR,Or*,V*,Y*O] 0.04" refs=13
- ASAS-SN: 1456 points, cameras bC(g,155); bG(g,219); ba(V,51); bc(V,151, d=-0.308); be(V,38, d=+0.027); bg(V,153); bk(g,308); bo(g,220); bs(g,161); change at onset (after-before, per-camera median) -0.140 mag; largest seasonal dimming 0.60 mag at MJD 58885
- dust: excess flux W1 12.55 mJy, W2 5.32 mJy, T = 8000 K (16-84%: 8000-8000) ratio bluer than an 8000 K blackbody (not dust-like)

## Killed (35)

### uid889197  [D2]  KILLED
- position 275.30795 +11.66447; Gaia DR3 4483860026397559680; G 13.50, BP-RP 1.19, plx 2.98 mas; plot `plots/uid889197.png`
- **KILL:** blend: Gaia neighbour within 6" only 0.51 mag fainter in G (2.1" PA271 G14.02 dG+0.51; 9.9" PA197 G20.84 dG+7.33)
- flags: centroid jump 0.143" (3.1 sigma, PA 91) away from the neighbour(s) 2.1" PA271 G14.0, as expected when the target itself brightens in a blended WISE PSF | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 4.78 (stored 4.78, reproduced True); dW2 0.418, dW1 0.204, 19 visits, 236 points; baseline W1 10.66, W1-W2 0.164; onset between MJD 57473 and 57647
- detector 2: excess 0.224 mag, z 13.4, jitter ratio 8.1
- field control: target step +0.498 (W1 +0.241); neighbours N=179, median -0.002, robust sigma 0.010, max +0.052; z = 51.8
- centroid: jump at onset 0.143" +- 0.045 (3.1 sigma, PA 91); largest consecutive-visit jump 0.194"; rms 0.078"; toward neighbour: none; expected shift if a neighbour were the source: 2.1" G14.0: 0.79"; 9.9" G20.8: 3.65"
- AllWISE 2010: W1-W2 0.448, W2-W3 1.818 (W3 S/N 51.2), W3-W4 0.656 (W4 S/N 9.0), ext_flg 0, ph_qual AAAB: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 0.94, ipd_frac_multi_peak 0, NSS none, Teff 4915 K, logg 4.45, H-alpha pEW 0.068 nm, varclass none; M_G 5.87, -0.32 mag vs sequence (on the sequence); neighbours within 10": 2.1" PA271 G14.02 dG+0.51; 9.9" PA197 G20.84 dG+7.33
- SIMBAD (10"): 2MASS J18211387+1139522 [*; *,MIR,NIR] 0.55" refs=2
- ASAS-SN: 1058 points, cameras bA(g,215); bE(g,118); ba(V,224, d=-0.003); bi(g,202); bm(g,100); bq(g,199); change at onset (after-before, per-camera median) -0.003 mag; largest seasonal dimming 0.01 mag at MJD 60397
- dust: excess flux W1 4.36 mJy, W2 5.86 mJy, T = 958 K (16-84%: 931-987) 

### uid892905  [D2]  KILLED
- position 275.30734 +11.66448; Gaia DR3 4483860030702236800; G 14.02, BP-RP 1.31, plx 2.98 mas; plot `plots/uid892905.png`
- **KILL:** centroid jump 0.143" (3.1 sigma) at the onset toward a neighbour: 2.1" PA91 G13.5 (angle 0 deg) | blend: Gaia neighbour within 6" only -0.51 mag fainter in G (2.1" PA91 G13.50 dG-0.51; 9.6" PA184 G20.84 dG+6.82; 9.9" PA305 G18.63 dG+4.61)
- flags: AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 4.78 (stored 4.78, reproduced True); dW2 0.418, dW1 0.204, 19 visits, 236 points; baseline W1 10.66, W1-W2 0.164; onset between MJD 57473 and 57647
- detector 2: excess 0.227 mag, z 12.0, jitter ratio 8.1
- field control: target step +0.498 (W1 +0.241); neighbours N=179, median -0.002, robust sigma 0.010, max +0.052; z = 51.8
- centroid: jump at onset 0.143" +- 0.045 (3.1 sigma, PA 91); largest consecutive-visit jump 0.194"; rms 0.078"; toward neighbour: 2.1" PA91 G13.5 (angle 0 deg); expected shift if a neighbour were the source: 2.1" G13.5: 0.79"; 9.6" G20.8: 3.52"; 9.9" G18.6: 3.62"
- AllWISE 2010: W1-W2 0.448, W2-W3 1.818 (W3 S/N 51.2), W3-W4 0.656 (W4 S/N 9.0), ext_flg 0, ph_qual AAAB: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 0.92, ipd_frac_multi_peak 1, NSS none, Teff nan K, logg nan, H-alpha pEW nan nm, varclass none; M_G 6.39, -0.20 mag vs sequence (on the sequence); neighbours within 10": 2.1" PA91 G13.50 dG-0.51; 9.6" PA184 G20.84 dG+6.82; 9.9" PA305 G18.63 dG+4.61
- SIMBAD (10"): 2MASS J18211387+1139522 [*; *,MIR,NIR] 1.61" refs=2
- ASAS-SN: 1058 points, cameras bA(g,215); bE(g,118); ba(V,224, d=-0.003); bi(g,202); bm(g,100); bq(g,199); change at onset (after-before, per-camera median) -0.003 mag; largest seasonal dimming 0.01 mag at MJD 60397
- dust: excess flux W1 4.36 mJy, W2 5.86 mJy, T = 958 K (16-84%: 931-987) 

### uid1624344  [D2]  KILLED
- position 79.40482 +5.99674; Gaia DR3 3240563068331009920; G 14.24, BP-RP 1.79, plx 2.55 mas; plot `plots/uid1624344.png`
- **KILL:** eclipsing binary in SIMBAD (EB*, V* V1013 Ori)
- **young:** SIMBAD young-star types TT*,Y*?,Y*O (V* V1013 Ori) | Gaia DR3 variability class YSO(0.32)
- flags: 1.62 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | optical dimming +0.095 mag after the infrared onset (debris transit signature) | largest seasonal optical dimming 0.37 mag (MJD 57012)
- NEOWISE: score refetch 1.21 (stored 1.21, reproduced True); dW2 0.207, dW1 0.088, 21 visits, 217 points; baseline W1 10.83, W1-W2 0.324; onset between MJD 58738 and 58896
- detector 2: excess 0.352 mag, z 10.4, jitter ratio 12.2
- field control: target step +0.429 (W1 +0.242); neighbours N=59, median +0.000, robust sigma 0.009, max +0.030; z = 48.1
- centroid: jump at onset 0.029" +- 0.017 (1.7 sigma, PA 156); largest consecutive-visit jump 0.062"; rms 0.029"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.359, W2-W3 1.964 (W3 S/N 37.2), W3-W4 1.157 (W4 S/N 6.8), ext_flg 0, ph_qual AAAB: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.10, ipd_frac_multi_peak 0, NSS none, Teff 4147 K, logg 4.08, H-alpha pEW -0.181 nm, varclass YSO(0.32); M_G 6.27, -1.62 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): V* V1013 Ori [TT*; *,EB*,NIR,TT*,V*,Y*?,Y*O] 0.07" refs=11
- ASAS-SN: 1242 points, cameras bD(g,195, d=+0.190); bH(g,142, d=+0.130); bd(V,249); bh(V,52); bl(g,266, d=+0.083); bp(g,217, d=+0.095); bt(g,121, d=+0.029); change at onset (after-before, per-camera median) +0.095 mag; largest seasonal dimming 0.37 mag at MJD 57012
- dust: excess flux W1 2.08 mJy, W2 3.08 mJy, T = 881 K (16-84%: 843-921) 

### uid850157  [D2]  KILLED
- position 81.81119 -5.27505; Gaia DR3 3209303196839477120; G 15.70, BP-RP 2.04, plx 3.01 mas; plot `plots/uid850157.png`
- **KILL:** galaxy/QSO within 6" in SIMBAD: V* V1157 Ori [G] 0.0"
- **young:** SIMBAD young-star types Or*,Y*O (V* V1157 Ori)
- flags: AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.23 mag (MJD 60611)
- NEOWISE: score refetch 0.91 (stored 0.91, reproduced True); dW2 0.237, dW1 0.197, 15 visits, 183 points; baseline W1 10.54, W1-W2 0.500; onset between MJD 58533 and 58897
- detector 2: excess 0.487 mag, z 11.6, jitter ratio 24.1
- field control: target step +0.407 (W1 +0.416); neighbours N=45, median +0.000, robust sigma 0.009, max +0.032; z = 45.7
- centroid: jump at onset 0.023" +- 0.018 (1.3 sigma, PA 98); largest consecutive-visit jump 0.036"; rms 0.025"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.537, W2-W3 1.399 (W3 S/N 39.6), W3-W4 1.751 (W4 S/N 11.0), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.11, ipd_frac_multi_peak 0, NSS none, Teff 3480 K, logg 4.13, H-alpha pEW -1.676 nm, varclass none; M_G 8.09, -0.49 mag vs sequence (on the sequence); neighbours within 10": none
- SIMBAD (10"): V* V1157 Ori [Or*; *,Em*,G,NIR,Opt,Or*,Pu*,V*,Y*O] 0.01" refs=7
- ASAS-SN: 1229 points, cameras bA(g,140, d=-0.044); bE(g,190, d=-0.093); ba(V,125); be(V,169); bi(g,286, d=-0.164); bm(g,179, d=+0.008); bq(g,140, d=+0.062); change at onset (after-before, per-camera median) -0.044 mag; largest seasonal dimming 0.23 mag at MJD 60611
- dust: excess flux W1 6.48 mJy, W2 6.06 mJy, T = 1430 K (16-84%: 1310-1579) 

### uid1678941  [D2]  KILLED
- position 115.75425 -47.30429; Gaia DR3 5530505936819408640; G 14.98, BP-RP 1.97, plx 2.52 mas; plot `plots/uid1678941.png`
- **KILL:** blend: Gaia neighbour within 6" only 2.56 mag fainter in G (4.9" PA153 G17.54 dG+2.56; 5.7" PA226 G19.19 dG+4.22; 5.8" PA77 G18.88 dG+3.91)
- **young:** SIMBAD young-star types Y*?,Y*O (Gaia DR3 5530505936819408640) | Gaia DR3 variability class YSO(0.43)
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | 1.37 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 3.29 (stored 3.29, reproduced True); dW2 0.431, dW1 0.337, 21 visits, 401 points; baseline W1 10.49, W1-W2 0.493; onset between MJD 60050 and 60260
- detector 2: excess 0.493 mag, z 12.0, jitter ratio 10.9
- field control: target step +0.366 (W1 +0.309); neighbours N=123, median -0.004, robust sigma 0.010, max +0.026; z = 38.5
- centroid: jump at onset 0.062" +- 0.027 (2.3 sigma, PA 320); largest consecutive-visit jump 0.072"; rms 0.041"; toward neighbour: none; expected shift if a neighbour were the source: 4.9" G17.5: 1.40"; 5.7" G19.2: 1.65"; 5.8" G18.9: 1.65"
- AllWISE 2010: W1-W2 0.515, W2-W3 1.322 (W3 S/N 45.3), W3-W4 1.545 (W4 S/N 13.3), ext_flg 1, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.07, ipd_frac_multi_peak 0, NSS none, Teff 6298 K, logg 4.35, H-alpha pEW -1.209 nm, varclass YSO(0.43); M_G 6.99, -1.37 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 4.9" PA153 G17.54 dG+2.56; 5.7" PA226 G19.19 dG+4.22; 5.8" PA77 G18.88 dG+3.91
- SIMBAD (10"): Gaia DR3 5530505936819408640 [Y*?; *,Y*?,Y*O] 0.16" refs=6; Gaia DR3 5530505932523743616 [Y*?; *,Y*?,Y*O] 5.04" refs=6
- ASAS-SN: 1209 points, cameras bF(g,369, d=-0.139); bf(V,224); bj(g,442, d=-0.065); bn(g,174, d=+0.010); change at onset (after-before, per-camera median) -0.065 mag; largest seasonal dimming 0.10 mag at MJD 59643
- dust: excess flux W1 7.74 mJy, W2 8.58 mJy, T = 1155 K (16-84%: 1119-1193) 

### uid1207210  [D2]  KILLED
- position 71.64783 +23.40364; Gaia DR3 146931385248519296; G 15.21, BP-RP 1.91, plx 2.77 mas; plot `plots/uid1207210.png`
- **KILL:** blend: Gaia neighbour within 6" only -2.64 mag fainter in G (5.2" PA311 G12.57 dG-2.64)
- flags: 0.78 mag above the main sequence at its colour
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 15 visits, 118 points; baseline W1 12.82, W1-W2 0.449; onset between MJD 57273 and 57438
- detector 2: excess 0.459 mag, z 12.1, jitter ratio 22.2
- field control: target step +0.273 (W1 +0.417); neighbours N=80, median +0.000, robust sigma 0.011, max +0.038; z = 25.4
- centroid: jump at onset 0.596" +- 0.646 (0.9 sigma, PA 357); largest consecutive-visit jump 1.144"; rms 0.653"; toward neighbour: none; expected shift if a neighbour were the source: 5.2" G12.6: 1.15"
- AllWISE 2010: W1-W2 0.000, W2-W3 0.368 (W3 S/N 1.8), W3-W4 3.456 (W4 S/N 1.0), ext_flg 0, ph_qual AAUU: W3 S/N < 5: no W2-W3 class
- Gaia: RUWE 1.13, ipd_frac_multi_peak 0, NSS none, Teff 5036 K, logg 4.57, H-alpha pEW 0.012 nm, varclass none; M_G 7.42, -0.78 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 5.2" PA311 G12.57 dG-2.64
- SIMBAD (10"): no object
- ASAS-SN: 1054 points, cameras bC(g,241); bG(g,102); bc(V,251, d=+0.005); bg(V,42); bk(g,139); bo(g,149); bs(g,130); change at onset (after-before, per-camera median) +0.005 mag; largest seasonal dimming 0.01 mag at MJD 60165
- dust: excess flux W1 0.51 mJy, W2 0.25 mJy, T = 8000 K (16-84%: 2089-8000) ratio bluer than an 8000 K blackbody (not dust-like)

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

### uid1238881  [D2]  KILLED
- position 82.94434 -7.27503; Gaia DR3 3016425527064862976; G 14.55, BP-RP 1.90, plx 2.75 mas; plot `plots/uid1238881.png`
- **KILL:** galaxy/QSO within 6" in SIMBAD: ESO-HA  720 [G] 0.0"
- **young:** SIMBAD young-star types Y*?,Y*O (ESO-HA  720)
- flags: 1.43 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | not plain dust: optical brightening -0.212 mag (per-camera -0.046,-0.301,-0.162,-0.262) together with the infrared rise | largest seasonal optical dimming 0.32 mag (MJD 58068)
- NEOWISE: score refetch 1.14 (stored 1.14, reproduced True); dW2 0.174, dW1 0.176, 21 visits, 203 points; baseline W1 10.54, W1-W2 0.402; onset between MJD 58376 and 58534
- detector 2: excess 0.413 mag, z 10.9, jitter ratio 14.6
- field control: target step +0.326 (W1 +0.306); neighbours N=59, median -0.002, robust sigma 0.016, max +0.028; z = 21.1
- centroid: jump at onset 0.032" +- 0.015 (2.2 sigma, PA 291); largest consecutive-visit jump 0.068"; rms 0.024"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.373, W2-W3 1.434 (W3 S/N 42.3), W3-W4 2.598 (W4 S/N 17.2), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.04, ipd_frac_multi_peak 0, NSS none, Teff 5718 K, logg 4.36, H-alpha pEW -0.733 nm, varclass none; M_G 6.75, -1.43 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): ESO-HA  720 [Y*O; *,Em*,G,NIR,Y*?,Y*O] 0.01" refs=12
- ASAS-SN: 1494 points, cameras bA(g,155); bE(g,216, d=-0.046); ba(V,179); be(V,195); bi(g,335, d=-0.301); bm(g,246, d=-0.162); bq(g,168, d=-0.262); change at onset (after-before, per-camera median) -0.212 mag; largest seasonal dimming 0.32 mag at MJD 58068
- dust: excess flux W1 5.33 mJy, W2 4.75 mJy, T = 1539 K (16-84%: 1457-1630) 

### uid1148744  [D2]  KILLED
- position 126.62254 -34.58555; Gaia DR3 5543488248577017344; G 15.38, BP-RP 1.48, plx 2.80 mas; plot `plots/uid1148744.png`
- **KILL:** blend: Gaia neighbour within 6" only 1.46 mag fainter in G (3.8" PA197 G20.28 dG+4.90; 5.9" PA46 G16.84 dG+1.46; 7.6" PA254 G16.25 dG+0.87; 7.9" PA343 G19.80 dG+4.42; 9.1" PA42 G21.16 dG+5.78; 9.6" PA241 G19.02 dG+3.63)
- flags: AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.47 mag (MJD 60639)
- NEOWISE: score refetch 0.54 (stored 0.54, reproduced True); dW2 0.088, dW1 0.046, 17 visits, 143 points; baseline W1 10.45, W1-W2 0.632; onset between MJD 57867 and 58073
- detector 2: excess 0.693 mag, z 33.0, jitter ratio 11.0
- field control: target step +0.225 (W1 +0.252); neighbours N=170, median -0.005, robust sigma 0.013, max +0.048; z = 17.3
- centroid: jump at onset 0.032" +- 0.039 (0.8 sigma, PA 50); largest consecutive-visit jump 0.105"; rms 0.052"; toward neighbour: 5.9" PA46 G16.8 (angle 4 deg); 9.1" PA42 G21.2 (angle 8 deg); expected shift if a neighbour were the source: 3.8" G20.3: 0.71"; 5.9" G16.8: 1.10"; 7.6" G16.3: 1.43"; 7.9" G19.8: 1.49"; 9.1" G21.2: 1.72"; 9.6" G19.0: 1.80"
- AllWISE 2010: W1-W2 0.642, W2-W3 2.107 (W3 S/N 63.6), W3-W4 1.970 (W4 S/N 27.0), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.21, ipd_frac_multi_peak 0, NSS none, Teff 5870 K, logg 4.73, H-alpha pEW -3.254 nm, varclass none; M_G 7.62, +0.56 mag vs sequence (on the sequence); neighbours within 10": 3.8" PA197 G20.28 dG+4.90; 5.9" PA46 G16.84 dG+1.46; 7.6" PA254 G16.25 dG+0.87; 7.9" PA343 G19.80 dG+4.42; 9.1" PA42 G21.16 dG+5.78; 9.6" PA241 G19.02 dG+3.63
- SIMBAD (10"): 2MASS J08262942-3435081 [Em*; *,Em*,NIR] 0.20" refs=4
- ASAS-SN: 1314 points, cameras bG(g,442); bg(V,239, d=-0.014); bk(g,448); bo(g,185); change at onset (after-before, per-camera median) -0.014 mag; largest seasonal dimming 0.47 mag at MJD 60639
- dust: excess flux W1 2.94 mJy, W2 3.55 mJy, T = 1058 K (16-84%: 954-1179) 

### uid980347  [D2]  KILLED
- position 81.73918 +3.24962; Gaia DR3 3235952747355612672; G 15.10, BP-RP 2.14, plx 2.91 mas; plot `plots/uid980347.png`
- **KILL:** blend: Gaia neighbour within 6" only 0.09 mag fainter in G (4.7" PA136 G15.19 dG+0.09; 6.7" PA36 G19.91 dG+4.81; 7.7" PA34 G19.35 dG+4.25)
- **young:** SIMBAD young-star types Y*?,Y*O (UCAC4 467-010440; ZTF J052657.62+031455.3)
- flags: 1.47 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.30 mag (MJD 59433)
- NEOWISE: score refetch 1.54 (stored 1.54, reproduced True); dW2 0.302, dW1 0.238, 20 visits, 218 points; baseline W1 9.72, W1-W2 0.543; onset between MJD 58376 and 58533
- detector 2: excess 0.515 mag, z 12.0, jitter ratio 11.8
- field control: target step +0.195 (W1 +0.160); neighbours N=64, median +0.001, robust sigma 0.012, max +0.030; z = 16.4
- centroid: jump at onset 0.012" +- 0.048 (0.3 sigma, PA 167); largest consecutive-visit jump 0.081"; rms 0.075"; toward neighbour: 4.7" PA136 G15.2 (angle 32 deg); expected shift if a neighbour were the source: 4.7" G15.2: 0.77"; 6.7" G19.9: 1.11"; 7.7" G19.4: 1.27"
- AllWISE 2010: W1-W2 0.701, W2-W3 1.499 (W3 S/N 45.1), W3-W4 2.338 (W4 S/N 20.4), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.06, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW -0.343 nm, varclass none; M_G 7.42, -1.47 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 4.7" PA136 G15.19 dG+0.09; 6.7" PA36 G19.91 dG+4.81; 7.7" PA34 G19.35 dG+4.25
- SIMBAD (10"): UCAC4 467-010440 [Y*O; *,MIR,NIR,Y*?,Y*O] 0.02" refs=10; ZTF J052657.62+031455.3 [BY*; *,BY*,MIR,NIR,Y*?] 4.65" refs=11
- ASAS-SN: 1217 points, cameras bA(g,167); bE(g,174); ba(V,211); be(V,56); bi(g,277, d=-0.008); bm(g,205, d=+0.050); bq(g,127, d=+0.018); change at onset (after-before, per-camera median) +0.018 mag; largest seasonal dimming 0.30 mag at MJD 59433
- dust: excess flux W1 9.81 mJy, W2 8.68 mJy, T = 1555 K (16-84%: 1442-1689) 

### uid1613134  [D2]  KILLED
- position 82.65082 +12.61456; Gaia DR3 3341051967182318208; G 14.30, BP-RP 1.70, plx 2.55 mas; plot `plots/uid1613134.png`
- **KILL:** blend: Gaia neighbour within 6" only 1.69 mag fainter in G (5.0" PA34 G15.98 dG+1.69)
- **young:** SIMBAD young-star types Or*,Y*O (V* V447 Ori)
- flags: binary type in SIMBAD (**, V* V447 Ori) | 1.31 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.39 mag (MJD 60044)
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 21 visits, 184 points; baseline W1 9.38, W1-W2 0.447; onset between MJD 58899 and 59108
- detector 2: excess 0.488 mag, z 16.4, jitter ratio 7.2
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
- detector 2: excess 0.518 mag, z 14.3, jitter ratio 8.5
- field control: target step +0.175 (W1 +0.138); neighbours N=76, median -0.001, robust sigma 0.012, max +0.025; z = 14.4
- centroid: jump at onset 0.018" +- 0.020 (0.9 sigma, PA 308); largest consecutive-visit jump 0.050"; rms 0.027"; toward neighbour: none; expected shift if a neighbour were the source: 2.4" G14.6: 0.36"; 8.0" G20.3: 1.19"; 8.6" G17.7: 1.27"
- AllWISE 2010: W1-W2 0.495, W2-W3 1.644 (W3 S/N 58.1), W3-W4 1.989 (W4 S/N 27.8), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.23, ipd_frac_multi_peak 0, NSS none, Teff 6477 K, logg 4.26, H-alpha pEW -3.212 nm, varclass none; M_G 6.64, -1.40 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 2.4" PA110 G14.59 dG+0.13; 8.0" PA10 G20.34 dG+5.89; 8.6" PA140 G17.65 dG+3.20
- SIMBAD (10"): NAME Haro 5-64A [*; *,**] 0.03" refs=1; Haro 5-64 [TT*; *,**,Em*,MIR,NIR,SB*,TT*,V*,Y*O] 0.03" refs=40; NAME Haro 5-64B [*; *,**] 2.27" refs=0; Gaia DR3 3217634162083288320 [Or*; *,Or*] 2.27" refs=2
- ASAS-SN: 1388 points, cameras bC(g,141, d=-0.047); bG(g,218, d=-0.056); ba(V,51); bc(V,137); be(V,38); bg(V,153); bk(g,296, d=+0.042); bo(g,205, d=-0.075); bs(g,149, d=+0.078); change at onset (after-before, per-camera median) -0.047 mag; largest seasonal dimming 0.08 mag at MJD 56897
- dust: excess flux W1 4.44 mJy, W2 3.79 mJy, T = 1653 K (16-84%: 1339-2171) 

### uid1004862  [D2]  KILLED
- position 315.63764 +68.12475; Gaia DR3 2270056968043900928; G 14.29, BP-RP 2.07, plx 2.90 mas; plot `plots/uid1004862.png`
- **KILL:** eclipsing binary in SIMBAD (EB*, V* FW Cep)
- **young:** SIMBAD young-star types Or*,Y*?,Y*O (V* FW Cep) | Gaia DR3 variability class YSO(0.73)
- flags: 2.08 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.17 mag (MJD 60546)
- NEOWISE: score refetch 1.19 (stored 1.19, reproduced True); dW2 0.137, dW1 0.135, 21 visits, 355 points; baseline W1 9.94, W1-W2 0.489; onset between MJD 58843 and 59049
- detector 2: excess 0.472 mag, z 11.0, jitter ratio 7.1
- field control: target step +0.155 (W1 +0.154); neighbours N=102, median -0.002, robust sigma 0.011, max +0.105; z = 13.7
- centroid: jump at onset 0.021" +- 0.017 (1.2 sigma, PA 305); largest consecutive-visit jump 0.050"; rms 0.027"; toward neighbour: none; expected shift if a neighbour were the source: 8.7" G20.1: 1.15"
- AllWISE 2010: W1-W2 0.453, W2-W3 1.431 (W3 S/N 38.3), W3-W4 1.106 (W4 S/N 12.6), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.09, ipd_frac_multi_peak 0, NSS none, Teff 4866 K, logg 4.15, H-alpha pEW -0.496 nm, varclass YSO(0.73); M_G 6.60, -2.08 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 8.7" PA174 G20.11 dG+5.82
- SIMBAD (10"): V* FW Cep [Or*; *,EB*,NIR,Or*,V*,Y*?,Y*O] 0.11" refs=19; 1RXS J210233.9+680724 [X; X] 7.03" refs=0
- ASAS-SN: 1450 points, cameras bA(g,351, d=+0.004); bD(g,378, d=-0.002); bd(V,192); bq(g,270, d=-0.023); bt(g,259, d=+0.014); change at onset (after-before, per-camera median) +0.001 mag; largest seasonal dimming 0.17 mag at MJD 60546
- dust: excess flux W1 3.70 mJy, W2 4.44 mJy, T = 1066 K (16-84%: 966-1184) 

### uid1608482  [D2]  KILLED
- position 83.66609 -5.50186; Gaia DR3 3017268921203932032; G 15.00, BP-RP 1.88, plx 2.56 mas; plot `plots/uid1608482.png`
- **KILL:** blend: Gaia neighbour within 6" only 0.53 mag fainter in G (3.0" PA39 G15.53 dG+0.53) | galaxy/QSO within 6" in SIMBAD: V* IW Ori A [G] 0.0"; V* IW Ori B [G] 3.0"
- **young:** SIMBAD young-star types Or*,TT*,TT?,Y*O (V* IW Ori A; V* IW Ori; V* IW Ori B)
- flags: binary type in SIMBAD (**, V* IW Ori A) | AllWISE ext_flg = 1 (extended or 2MASS XSC association) | 1.08 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 20 visits, 182 points; baseline W1 9.21, W1-W2 0.473; onset between MJD 59995 and 60204
- detector 2: excess 0.487 mag, z 13.1, jitter ratio 11.1
- field control: target step +0.292 (W1 +0.281); neighbours N=119, median -0.001, robust sigma 0.027, max +0.317; z = 11.0
- centroid: jump at onset 0.106" +- 0.091 (1.2 sigma, PA 9); largest consecutive-visit jump 0.285"; rms 0.155"; toward neighbour: 3.0" PA39 G15.5 (angle 30 deg); expected shift if a neighbour were the source: 3.0" G15.5: 0.70"
- AllWISE 2010: W1-W2 0.485, W2-W3 2.049 (W3 S/N 30.2), W3-W4 3.358 (W4 S/N 0.9), ext_flg 1, ph_qual AAAU: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.06, ipd_frac_multi_peak 0, NSS none, Teff 3601 K, logg 4.00, H-alpha pEW -1.388 nm, varclass none; M_G 7.04, -1.08 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 3.0" PA39 G15.53 dG+0.53
- SIMBAD (10"): V* IW Ori A [Or*; *,Em*,G,NIR,Or*,TT?,V*,Y*O] 0.03" refs=27; V* IW Ori [TT*; *,**,MIR,Or*,TT*,V*,V*?,X,Y*O] 1.29" refs=27; V* IW Ori B [Or*; *,**,Em*,G,Ir*,NIR,Or*,TT?,V*,Y*O] 2.97" refs=17
- ASAS-SN: 1500 points, cameras bA(g,153, d=+0.020); bE(g,219, d=+0.030); ba(V,179); be(V,195); bi(g,344, d=+0.031); bm(g,245, d=+0.005); bq(g,165, d=+0.051); change at onset (after-before, per-camera median) +0.030 mag; largest seasonal dimming 0.03 mag at MJD 59252
- dust: excess flux W1 4.55 mJy, W2 3.91 mJy, T = 1634 K (16-84%: 1339-2107) 

### uid1639002  [D2]  KILLED
- position 128.80091 -50.51295; Gaia DR3 5322740776530753280; G 15.06, BP-RP 1.73, plx 2.54 mas; plot `plots/uid1639002.png`
- **KILL:** blend: Gaia neighbour within 6" only 2.11 mag fainter in G (2.7" PA288 G17.17 dG+2.11; 3.6" PA233 G20.97 dG+5.90; 9.0" PA282 G20.06 dG+5.00)
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 0.69 (stored 0.69, reproduced True); dW2 0.115, dW1 0.055, 18 visits, 234 points; baseline W1 11.35, W1-W2 0.407; onset between MJD 57164 and 57358
- detector 2: excess 0.444 mag, z 14.1, jitter ratio 12.2
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
- detector 2: excess 0.661 mag, z 20.8, jitter ratio 11.5
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
- detector 2: excess 0.673 mag, z 15.7, jitter ratio 7.0
- field control: target step +0.216 (W1 +0.261); neighbours N=87, median +0.003, robust sigma 0.020, max +0.181; z = 10.6
- centroid: jump at onset 0.045" +- 0.024 (1.9 sigma, PA 258); largest consecutive-visit jump 0.099"; rms 0.045"; toward neighbour: none; expected shift if a neighbour were the source: 4.4" G17.7: 0.80"
- AllWISE 2010: W1-W2 0.743, W2-W3 2.312 (W3 S/N 73.2), W3-W4 1.398 (W4 S/N 47.4), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.05, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW 0.025 nm, varclass none; M_G 7.70, -1.19 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 4.4" PA40 G17.73 dG+2.67
- SIMBAD (10"): ATO J052.3580+31.4444 [Or*; *,IR,MIR,NIR,Opt,Or*,V*,X,Y*?,Y*O] 0.19" refs=49; [HL2013] 052.35902+31.44538 [Y*?; *,IR,Y*?] 4.46" refs=8
- ASAS-SN: 2220 points, cameras bC(g,253, d=+0.042); bD(g,288, d=+0.070); bG(g,70, d=+0.295); bH(g,86, d=+0.150); ba(V,40); bc(V,272); bd(V,251); bg(V,22); bh(V,33); bk(g,130, d=+0.065); bl(g,163, d=+0.126); bo(g,126, d=+0.150); bp(g,126, d=-0.010); bs(g,172, d=+0.103); bt(g,188, d=+0.065); change at onset (after-before, per-camera median) +0.086 mag; largest seasonal dimming 0.15 mag at MJD 59967
- dust: excess flux W1 22.87 mJy, W2 21.36 mJy, T = 1433 K (16-84%: 1326-1562) 

### uid1197479  [D2]  KILLED
- position 81.41972 -5.88013; Gaia DR3 3209147822102195072; G 13.79, BP-RP 1.61, plx 2.77 mas; plot `plots/uid1197479.png`
- **KILL:** blend: Gaia neighbour within 6" only 2.44 mag fainter in G (3.1" PA192 G16.22 dG+2.44; 8.3" PA0 G19.06 dG+5.28) | galaxy/QSO within 6" in SIMBAD: ESO-HA  593 [G] 3.1"
- **young:** SIMBAD young-star types TT*,Y*?,Y*O (Kiso A-0975  87)
- flags: binary type in SIMBAD (**, Kiso A-0975  87) | AllWISE ext_flg = 1 (extended or 2MASS XSC association) | 1.38 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 0.63 (stored 0.63, reproduced True); dW2 0.076, dW1 0.057, 16 visits, 163 points; baseline W1 9.80, W1-W2 0.458; onset between MJD 57808 and 58009
- detector 2: excess 0.510 mag, z 19.8, jitter ratio 11.2
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
- detector 2: excess 0.598 mag, z 24.3, jitter ratio 6.8
- field control: target step +0.132 (W1 +0.104); neighbours N=119, median +0.003, robust sigma 0.015, max +0.291; z = 8.7
- centroid: jump at onset 0.051" +- 0.056 (0.9 sigma, PA 60); largest consecutive-visit jump 0.153"; rms 0.111"; toward neighbour: none; expected shift if a neighbour were the source: 3.4" G14.4: 0.39"
- AllWISE 2010: W1-W2 0.516, W2-W3 1.832 (W3 S/N 44.1), W3-W4 1.992 (W4 S/N 29.0), ext_flg 1, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.28, ipd_frac_multi_peak 0, NSS none, Teff 5777 K, logg 4.30, H-alpha pEW -3.126 nm, varclass none; M_G 6.15, -1.18 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 3.4" PA235 G14.37 dG+0.25
- SIMBAD (10"): V* BW Ori [TT*; *,Em*,Er*,MIR,NIR,Opt,Or*,TT*,V*,Y*O,ev] 0.01" refs=48; SOXS 105 [X; X] 2.87" refs=1; 2MASS J05345386-0623526 [TT*; *,Em*,G,NIR,Opt,Or*,TT*,Y*O] 3.40" refs=12
- ASAS-SN: 1322 points, cameras bA(g,150, d=-0.087); bE(g,217, d=-0.119); ba(V,172); be(V,194); bi(g,272, d=+0.003); bm(g,192, d=-0.020); bq(g,125, d=-0.140); change at onset (after-before, per-camera median) -0.087 mag; largest seasonal dimming 0.23 mag at MJD 59841
- dust: excess flux W1 4.97 mJy, W2 6.72 mJy, T = 952 K (16-84%: 845-1080) 

### uid1643031  [D2]  KILLED
- position 85.77822 +9.73039; Gaia DR3 3336465805401439744; G 15.67, BP-RP 2.05, plx 2.54 mas; plot `plots/uid1643031.png`
- **KILL:** blend: Gaia neighbour within 6" only 1.16 mag fainter in G (1.1" PA175 G16.83 dG+1.16; 1.6" PA97 G19.37 dG+3.70)
- **young:** SIMBAD young-star types Y*O (ATO J085.7782+09.7303)
- flags: binary type in SIMBAD (**, ATO J085.7782+09.7303) | 0.91 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | possible optical brightening at onset (-0.174 mag, one camera only) | largest seasonal optical dimming 0.19 mag (MJD 57069)
- NEOWISE: score refetch 1.04 (stored 1.04, reproduced True); dW2 0.114, dW1 0.081, 20 visits, 221 points; baseline W1 10.53, W1-W2 0.482; onset between MJD 57090 and 57284
- detector 2: excess 0.468 mag, z 11.1, jitter ratio 10.3
- field control: target step +0.084 (W1 +0.062); neighbours N=90, median -0.005, robust sigma 0.010, max +0.030; z = 8.6
- centroid: jump at onset 0.029" +- 0.018 (1.7 sigma, PA 248); largest consecutive-visit jump 0.062"; rms 0.037"; toward neighbour: none; expected shift if a neighbour were the source: 1.1" G16.8: 0.08"; 1.6" G19.4: 0.12"
- AllWISE 2010: W1-W2 0.453, W2-W3 1.356 (W3 S/N 36.1), W3-W4 1.916 (W4 S/N 11.9), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.11, ipd_frac_multi_peak 0, NSS none, Teff 6016 K, logg 4.55, H-alpha pEW -2.692 nm, varclass none; M_G 7.70, -0.91 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 1.1" PA175 G16.83 dG+1.16; 1.6" PA97 G19.37 dG+3.70
- SIMBAD (10"): ATO J085.7782+09.7303 [Y*O; *,**,MIR,NIR,Opt,Pu*,Y*O] 0.01" refs=11; Gaia DR2 3336465805401439744 [*; *] 0.05" refs=7; Gaia DR2 3336465805399245824 [*; *] 1.03" refs=6
- ASAS-SN: 790 points, cameras bA(g,162); bE(g,103); ba(V,135, d=-0.174); bi(g,197); bm(g,92); bq(g,101); change at onset (after-before, per-camera median) -0.174 mag; largest seasonal dimming 0.19 mag at MJD 57069
- dust: excess flux W1 1.69 mJy, W2 1.85 mJy, T = 1174 K (16-84%: 992-1427) 

### uid1271126  [D2]  KILLED
- position 84.93817 -2.08175; Gaia DR3 3216541419323380480; G 13.30, BP-RP 1.74, plx 2.73 mas; plot `plots/uid1271126.png`
- **KILL:** blend: Gaia neighbour within 6" only 0.47 mag fainter in G (1.5" PA340 G13.77 dG+0.47)
- **young:** SIMBAD young-star types Or*,TT* (V* V2749 Ori)
- flags: Gaia ipd_frac_multi_peak 13% (resolved double?) | 2.26 mag above the main sequence at its colour
- NEOWISE: score refetch 0.96 (stored 0.96, reproduced True); dW2 0.085, dW1 0.038, 20 visits, 192 points; baseline W1 9.01, W1-W2 0.326; onset between MJD 59110 and 59265
- detector 2: excess 0.362 mag, z 11.5, jitter ratio 7.5
- field control: target step +0.107 (W1 +0.038); neighbours N=89, median -0.002, robust sigma 0.013, max +0.050; z = 8.2
- centroid: jump at onset 0.019" +- 0.020 (1.0 sigma, PA 111); largest consecutive-visit jump 0.047"; rms 0.034"; toward neighbour: none; expected shift if a neighbour were the source: 1.5" G13.8: 0.14"
- AllWISE 2010: W1-W2 0.293, W2-W3 0.883 (W3 S/N 19.4), W3-W4 3.267 (W4 S/N 37.2), ext_flg 0, ph_qual AAAA: weak W3 excess (0.5 < W2-W3 < 1.0)
- Gaia: RUWE 1.11, ipd_frac_multi_peak 13, NSS none, Teff 6007 K, logg 4.10, H-alpha pEW -0.308 nm, varclass none; M_G 5.48, -2.26 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 1.5" PA340 G13.77 dG+0.47
- SIMBAD (10"): V* V2749 Ori A [*; *,V*] 0.04" refs=3; V* V2749 Ori [Or*; *,MIR,NIR,Or*,TT*,V*,X] 0.51" refs=6; V* V2749 Ori B [*; *,V*] 1.52" refs=0
- ASAS-SN: 1338 points, cameras bC(g,149, d=+0.030); bG(g,220, d=-0.010); bc(V,150); be(V,38); bg(V,149); bk(g,241, d=+0.008); bo(g,231, d=+0.039); bs(g,160, d=+0.038); change at onset (after-before, per-camera median) +0.030 mag; largest seasonal dimming 0.06 mag at MJD 57761
- dust: excess flux W1 5.83 mJy, W2 7.41 mJy, T = 1007 K (16-84%: 915-1112) 

### uid958315  [D2]  KILLED
- position 334.77944 +73.83737; Gaia DR3 2279011077205275136; G 12.61, BP-RP 1.48, plx 2.93 mas; plot `plots/uid958315.png`
- **KILL:** blend: Gaia neighbour within 6" only 2.66 mag fainter in G (1.6" PA173 G15.27 dG+2.66)
- **young:** SIMBAD young-star types Y*?,Y*O (UCAC4 820-027202) | Gaia DR3 variability class YSO(0.73)
- flags: 2.11 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.10 mag (MJD 60533)
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 21 visits, 409 points; baseline W1 8.66, W1-W2 0.381; onset between MJD 57776 and 57974
- detector 2: excess 0.441 mag, z 21.0, jitter ratio 7.8
- field control: target step +0.052 (W1 +0.052); neighbours N=98, median -0.002, robust sigma 0.007, max +0.409; z = 7.7
- centroid: jump at onset 0.055" +- 0.023 (2.3 sigma, PA 336); largest consecutive-visit jump 0.101"; rms 0.038"; toward neighbour: none; expected shift if a neighbour were the source: 1.6" G15.3: 0.08"
- AllWISE 2010: W1-W2 0.378, W2-W3 2.373 (W3 S/N 88.0), W3-W4 1.881 (W4 S/N 54.5), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.19, ipd_frac_multi_peak 9, NSS none, Teff 5218 K, logg 3.96, H-alpha pEW -0.897 nm, varclass YSO(0.73); M_G 4.95, -2.11 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 1.6" PA173 G15.27 dG+2.66
- SIMBAD (10"): UCAC4 820-027202 [Y*O; *,MIR,NIR,Y*?,Y*O] 0.09" refs=6; Gaia DR3 2279011081503333376 [*; *] 1.62" refs=0; IRAS F22181+7335 [Y*O; IR,Y*O] 7.95" refs=3
- ASAS-SN: 1385 points, cameras bA(g,337); bB(g,119); ba(V,249, d=+0.024); bb(V,163, d=-0.029); bq(g,266); br(g,251); change at onset (after-before, per-camera median) -0.003 mag; largest seasonal dimming 0.10 mag at MJD 60533
- dust: excess flux W1 -1.36 mJy, W2 -1.30 mJy, T = n/a K (16-84%: n/a-n/a) no W2 excess flux after onset

### uid1565407  [D2]  KILLED
- position 83.96024 -5.86160; Gaia DR3 3017196486578194688; G 14.41, BP-RP 1.66, plx 2.58 mas; plot `plots/uid1565407.png`
- **KILL:** blend: Gaia neighbour within 6" only -0.40 mag fainter in G (0.9" PA150 G14.02 dG-0.40)
- **young:** SIMBAD young-star types Or*,Y*O (V* OU Ori; V* OU Ori A)
- flags: 1.05 mag above the main sequence at its colour
- NEOWISE: score refetch 0.13 (stored 0.13, reproduced True); dW2 0.013, dW1 0.027, 20 visits, 185 points; baseline W1 9.77, W1-W2 0.321; onset between MJD 57646 and 57811
- detector 2: excess 0.368 mag, z 13.3, jitter ratio 6.2
- field control: target step +0.146 (W1 +0.028); neighbours N=132, median -0.002, robust sigma 0.027, max +0.352; z = 5.6
- centroid: jump at onset 0.013" +- 0.016 (0.8 sigma, PA 156); largest consecutive-visit jump 0.050"; rms 0.032"; toward neighbour: 0.9" PA150 G14.0 (angle 6 deg); expected shift if a neighbour were the source: 0.9" G14.0: 0.11"
- AllWISE 2010: W1-W2 0.293, W2-W3 0.071 (W3 S/N 2.4), W3-W4 3.447 (W4 S/N 7.1), ext_flg 0, ph_qual AACB: W3 S/N < 5: no W2-W3 class; W1-W2 > 0.25
- Gaia: RUWE 1.19, ipd_frac_multi_peak 3, NSS none, Teff nan K, logg nan, H-alpha pEW nan nm, varclass none; M_G 6.47, -1.05 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 0.9" PA150 G14.02 dG-0.40
- SIMBAD (10"): V* OU Ori B [*; *,V*] 0.02" refs=1; V* OU Ori [Or*; *,Em*,MIR,NIR,Opt,Or*,V*,X,Y*O,ev] 0.61" refs=31; V* OU Ori A [Or*; *,Or*,V*] 0.85" refs=2
- ASAS-SN: 0 points, cameras n/a; change at onset (after-before, per-camera median) n/a mag; largest seasonal dimming n/a mag at MJD n/a
- dust: excess flux W1 1.71 mJy, W2 2.39 mJy, T = 929 K (16-84%: 807-1076) 
- checks missing: ASAS-SN (no source)

### uid1657002  [D2]  KILLED
- position 83.71486 -5.42027; Gaia DR3 3017269883276585088; G 13.96, BP-RP 1.79, plx 2.53 mas; plot `plots/uid1657002.png`
- **KILL:** galaxy/QSO within 6" in SIMBAD: V* V401 Ori [G] 0.0"
- **young:** SIMBAD young-star types Or*,TT*,TT?,Y*?,Y*O (V* V401 Ori)
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | 1.91 mag above the main sequence at its colour | AllWISE 2010 Class I-like colour cuts (W1-W2 > 1.0, W2-W3 > 2.0)
- NEOWISE: score refetch 1.65 (stored 1.65, reproduced True); dW2 0.244, dW1 0.154, 15 visits, 110 points; baseline W1 8.74, W1-W2 0.540; onset between MJD 59109 and 59473
- detector 2: excess 0.568 mag, z 16.9, jitter ratio 10.9
- field control: target step +0.234 (W1 +0.220); neighbours N=103, median +0.002, robust sigma 0.044, max +0.180; z = 5.3
- centroid: jump at onset 0.040" +- 0.018 (2.2 sigma, PA 353); largest consecutive-visit jump 0.100"; rms 0.036"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 1.073, W2-W3 3.000 (W3 S/N 16.8), W3-W4 3.034 (W4 S/N nan), ext_flg 1, ph_qual AAAZ: Class I-like colour cuts (W1-W2 > 1.0, W2-W3 > 2.0)
- Gaia: RUWE 1.06, ipd_frac_multi_peak 0, NSS none, Teff 5908 K, logg 4.14, H-alpha pEW -1.149 nm, varclass none; M_G 5.98, -1.91 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): V* V401 Ori [TT*; *,Em*,G,NIR,Or*,TT*,TT?,V*,X,Y*?,Y*O] 0.03" refs=65
- ASAS-SN: 0 points, cameras n/a; change at onset (after-before, per-camera median) n/a mag; largest seasonal dimming n/a mag at MJD n/a
- dust: excess flux W1 22.92 mJy, W2 26.09 mJy, T = 1123 K (16-84%: 1072-1178) 
- checks missing: ASAS-SN (no source)

### uid1404605  [D2]  KILLED
- position 83.55500 -5.56486; Gaia DR3 3017266962698857216; G 15.00, BP-RP 1.74, plx 2.66 mas; plot `plots/uid1404605.png`
- **KILL:** blend: Gaia neighbour within 6" only 2.74 mag fainter in G (5.5" PA337 G17.74 dG+2.74) | galaxy/QSO within 6" in SIMBAD: V* V1934 Ori [G] 5.5"
- **young:** SIMBAD young-star types Or*,TT*,TT?,Y*O (V* IM Ori)
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 0.81 (stored 0.81, reproduced True); dW2 0.072, dW1 -0.032, 18 visits, 169 points; baseline W1 10.51, W1-W2 0.384; onset between MJD 58377 and 58535
- detector 2: excess 0.420 mag, z 13.3, jitter ratio 6.3
- field control: target step +0.134 (W1 +0.139); neighbours N=126, median -0.005, robust sigma 0.027, max +0.550; z = 5.2
- centroid: jump at onset 0.041" +- 0.041 (1.0 sigma, PA 115); largest consecutive-visit jump 0.122"; rms 0.077"; toward neighbour: none; expected shift if a neighbour were the source: 5.5" G17.7: 0.64"
- AllWISE 2010: W1-W2 0.456, W2-W3 2.582 (W3 S/N 39.4), W3-W4 2.820 (W4 S/N 24.5), ext_flg 1, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.04, ipd_frac_multi_peak 0, NSS none, Teff 3712 K, logg 4.08, H-alpha pEW -5.469 nm, varclass none; M_G 7.13, -0.62 mag vs sequence (on the sequence); neighbours within 10": 5.5" PA337 G17.74 dG+2.74
- SIMBAD (10"): V* IM Ori [TT*; *,Em*,MIR,NIR,Or*,TT*,TT?,V*,V*?,X,Y*O] 0.02" refs=52; V* V1934 Ori [Or*; *,Em*,G,NIR,Or*,TT?,V*,Y*O] 5.49" refs=24
- ASAS-SN: 1529 points, cameras bA(g,159); bE(g,221, d=+0.008); ba(V,180); be(V,195); bi(g,346, d=-0.008); bm(g,252, d=-0.001); bq(g,176, d=-0.001); change at onset (after-before, per-camera median) -0.001 mag; largest seasonal dimming 0.09 mag at MJD 57974
- dust: excess flux W1 0.53 mJy, W2 0.99 mJy, T = 750 K (16-84%: 625-906) 

### uid1363385  [D2]  KILLED
- position 85.04659 -7.16449; Gaia DR3 3016086740044032512; G 14.97, BP-RP 1.97, plx 2.68 mas; plot `plots/uid1363385.png`
- **KILL:** blend: Gaia neighbour within 6" only 1.55 mag fainter in G (2.7" PA128 G16.52 dG+1.55)
- **young:** SIMBAD young-star types Or*,Y*O (V* DK Ori)
- flags: centroid jump 0.222" (3.7 sigma, PA 298) away from the neighbour(s) 2.7" PA128 G16.5, as expected when the target itself brightens in a blended WISE PSF | binary type in SIMBAD (**, V* DK Ori A) | AllWISE ext_flg = 1 (extended or 2MASS XSC association) | 1.27 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | optical dimming +0.124 mag after the infrared onset (debris transit signature) | largest seasonal optical dimming 0.35 mag (MJD 60055)
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 21 visits, 216 points; baseline W1 9.53, W1-W2 0.594; onset between MJD 57089 and 57283
- detector 2: excess 0.593 mag, z 14.3, jitter ratio 10.2
- field control: target step +0.050 (W1 +0.042); neighbours N=72, median -0.002, robust sigma 0.010, max +0.064; z = 5.0
- centroid: jump at onset 0.222" +- 0.060 (3.7 sigma, PA 298); largest consecutive-visit jump 0.124"; rms 0.103"; toward neighbour: none; expected shift if a neighbour were the source: 2.7" G16.5: 0.12"
- AllWISE 2010: W1-W2 0.569, W2-W3 1.444 (W3 S/N 42.8), W3-W4 1.696 (W4 S/N 19.9), ext_flg 1, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.04, ipd_frac_multi_peak 0, NSS none, Teff 3661 K, logg 4.03, H-alpha pEW -0.068 nm, varclass none; M_G 7.11, -1.27 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 2.7" PA128 G16.52 dG+1.55
- SIMBAD (10"): V* DK Ori A [*; *,**,V*] 0.02" refs=3; V* DK Ori [Or*; *,**,Em*,MIR,NIR,Opt,Or*,V*,Y*O] 0.33" refs=17; V* DK Ori B [*; *,**,V*] 2.66" refs=2
- ASAS-SN: 1098 points, cameras bB(g,93); bF(g,187); ba(V,30); bb(V,129, d=+0.124); bf(V,143); bj(g,250); bn(g,107); br(g,159); change at onset (after-before, per-camera median) +0.124 mag; largest seasonal dimming 0.35 mag at MJD 60055
- dust: excess flux W1 -2.46 mJy, W2 -1.80 mJy, T = n/a K (16-84%: n/a-n/a) no W2 excess flux after onset

### uid1592714  [D2]  KILLED
- position 84.87231 -2.45584; Gaia DR3 3216495068036524416; G 15.93, BP-RP 1.91, plx 2.56 mas; plot `plots/uid1592714.png`
- **KILL:** blend: Gaia neighbour within 6" only -1.40 mag fainter in G (5.7" PA107 G14.53 dG-1.40)
- **young:** SIMBAD young-star types TT*,Y*O (UCAC4 438-011271)
- flags: binary type in SIMBAD (**, UCAC4 438-011271) | in the Gaia DR3 QSO candidate table (low purity) | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 21 visits, 215 points; baseline W1 10.35, W1-W2 0.478; onset between MJD 59632 and 59841
- detector 2: excess 0.487 mag, z 12.8, jitter ratio 6.8
- field control: target step +0.074 (W1 +0.067); neighbours N=131, median +0.001, robust sigma 0.015, max +0.264; z = 4.9
- centroid: jump at onset 0.122" +- 0.091 (1.3 sigma, PA 254); largest consecutive-visit jump 0.268"; rms 0.150"; toward neighbour: none; expected shift if a neighbour were the source: 5.7" G14.5: 0.38"
- AllWISE 2010: W1-W2 0.797, W2-W3 2.293 (W3 S/N 50.7), W3-W4 2.209 (W4 S/N 22.5), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.18, ipd_frac_multi_peak 0, NSS none, Teff 3808 K, logg 4.67, H-alpha pEW -3.867 nm, varclass none; M_G 7.98, -0.23 mag vs sequence (on the sequence); neighbours within 10": 5.7" PA107 G14.53 dG-1.40
- SIMBAD (10"): UCAC4 438-011271 [TT*; *,**,Em*,MIR,NIR,TT*,Y*O] 0.03" refs=35; Kiso A-0976 351 [Em*; *,Em*,NIR] 5.63" refs=12
- ASAS-SN: 1385 points, cameras bC(g,151, d=+0.013); bG(g,223, d=+0.043); bc(V,151); be(V,38); bg(V,152); bk(g,304, d=-0.001); bo(g,208, d=+0.003); bs(g,158, d=+0.033); change at onset (after-before, per-camera median) +0.013 mag; largest seasonal dimming 0.06 mag at MJD 60396
- dust: excess flux W1 -0.57 mJy, W2 -0.29 mJy, T = n/a K (16-84%: n/a-n/a) no W2 excess flux after onset

### uid1615293  [D2]  KILLED
- position 83.91676 -4.76539; Gaia DR3 3209574741853143552; G 14.06, BP-RP 1.91, plx 2.55 mas; plot `plots/uid1615293.png`
- **KILL:** galaxy/QSO within 6" in SIMBAD: V* OO Ori [G] 0.0"
- **young:** SIMBAD young-star types Or*,TT*,Y*O (V* OO Ori)
- flags: 2.11 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | optical dimming +0.765 mag after the infrared onset (debris transit signature) | largest seasonal optical dimming 0.67 mag (MJD 60298)
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 18 visits, 170 points; baseline W1 10.01, W1-W2 0.401; onset between MJD 59837 and 59995
- detector 2: excess 0.410 mag, z 10.7, jitter ratio 14.0
- field control: target step +0.133 (W1 +0.042); neighbours N=107, median +0.003, robust sigma 0.028, max +0.480; z = 4.6
- centroid: jump at onset 0.014" +- 0.013 (1.1 sigma, PA 225); largest consecutive-visit jump 0.045"; rms 0.024"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.384, W2-W3 1.923 (W3 S/N 27.3), W3-W4 1.560 (W4 S/N 9.3), ext_flg 0, ph_qual AAAB: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.07, ipd_frac_multi_peak 0, NSS none, Teff 5399 K, logg 4.17, H-alpha pEW -0.601 nm, varclass none; M_G 6.10, -2.11 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): V* OO Ori [TT*; *,Em*,G,MIR,NIR,Or*,TT*,V*,X,Y*O] 0.03" refs=44
- ASAS-SN: 319 points, cameras ba(V,119); be(V,178); bq(g,22, d=+0.765); change at onset (after-before, per-camera median) +0.765 mag; largest seasonal dimming 0.67 mag at MJD 60298
- dust: excess flux W1 0.79 mJy, W2 1.20 mJy, T = 863 K (16-84%: 705-1076) 

### uid875307  [D2]  KILLED
- position 85.17870 -1.78713; Gaia DR3 3216648548696357376; G 11.37, BP-RP 1.13, plx 2.99 mas; plot `plots/uid875307.png`
- **KILL:** centroid jump 0.232" (3.2 sigma) at the onset toward a neighbour: 3.7" PA196 G12.9 (angle 9 deg) | blend: Gaia neighbour within 6" only 1.51 mag fainter in G (3.7" PA196 G12.88 dG+1.51)
- **young:** SIMBAD young-star types Y*?,Y*O (2MASS J05404289-0147136; 2MASS J05404281-0147171) | Gaia DR3 variability class YSO(0.27)
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | 2.27 mag above the main sequence at its colour
- NEOWISE: score refetch 1.54 (stored 1.54, reproduced True); dW2 0.135, dW1 0.101, 20 visits, 186 points; baseline W1 8.74, W1-W2 0.158; onset between MJD 57448 and 57648
- detector 2: excess 0.216 mag, z 13.3, jitter ratio 7.0
- field control: target step +0.083 (W1 +0.041); neighbours N=44, median -0.003, robust sigma 0.022, max +0.348; z = 3.9
- centroid: jump at onset 0.232" +- 0.073 (3.2 sigma, PA 188); largest consecutive-visit jump 0.222"; rms 0.124"; toward neighbour: 3.7" PA196 G12.9 (angle 9 deg); expected shift if a neighbour were the source: 3.7" G12.9: 0.27"
- AllWISE 2010: W1-W2 0.229, W2-W3 1.098 (W3 S/N 3.5), W3-W4 2.179 (W4 S/N -0.1), ext_flg 1, ph_qual AABU: W3 S/N < 5: no W2-W3 class
- Gaia: RUWE 1.09, ipd_frac_multi_peak 0, NSS none, Teff 5238 K, logg 3.78, H-alpha pEW 0.051 nm, varclass YSO(0.27); M_G 3.75, -2.27 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 3.7" PA196 G12.88 dG+1.51
- SIMBAD (10"): 2MASS J05404289-0147136 [Y*O; *,NIR,Y*O] 0.04" refs=8; GSC 04767-01392 [*; *] 2.29" refs=1; 2MASS J05404281-0147171 [Y*O; *,NIR,Y*?,Y*O] 3.65" refs=12
- ASAS-SN: 0 points, cameras ; change at onset (after-before, per-camera median) n/a mag; largest seasonal dimming n/a mag at MJD n/a
- dust: excess flux W1 2.15 mJy, W2 3.85 mJy, T = 768 K (16-84%: 608-975) 
- checks missing: ASAS-SN change at onset (no camera spans the onset)

### uid1607640  [D2]  KILLED
- position 83.71019 -5.33899; Gaia DR3 3209518598040871296; G 14.90, BP-RP 1.85, plx 2.56 mas; plot `plots/uid1607640.png`
- **KILL:** galaxy/QSO within 6" in SIMBAD: V* V2057 Ori [G] 0.0"
- **young:** SIMBAD young-star types Or*,TT*,TT?,Y*?,Y*O (V* V2057 Ori)
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | 1.10 mag above the main sequence at its colour
- NEOWISE: score refetch 0.64 (stored 0.64, reproduced True); dW2 0.100, dW1 0.102, 10 visits, 100 points; baseline W1 9.83, W1-W2 0.380; onset between MJD 58168 and 58377
- detector 2: excess 0.400 mag, z 11.0, jitter ratio 14.5
- field control: target step +0.109 (W1 +0.105); neighbours N=82, median -0.000, robust sigma 0.040, max +0.341; z = 2.7
- centroid: jump at onset 0.025" +- 0.035 (0.7 sigma, PA 229); largest consecutive-visit jump 0.066"; rms 0.042"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.378, W2-W3 1.526 (W3 S/N 2.5), W3-W4 6.462 (W4 S/N nan), ext_flg 1, ph_qual AACZ: W3 S/N < 5: no W2-W3 class; W1-W2 > 0.25
- Gaia: RUWE 1.09, ipd_frac_multi_peak 0, NSS none, Teff 5854 K, logg 4.33, H-alpha pEW -1.381 nm, varclass none; M_G 6.94, -1.10 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): V* V2057 Ori [TT*; *,Em*,G,Ir*,MIR,NIR,Or*,TT*,TT?,V*,X,Y*?,Y*O] 0.03" refs=57
- ASAS-SN: 1343 points, cameras bA(g,151); bE(g,216); ba(V,175, d=+0.012); be(V,194); bi(g,273, d=+0.006); bm(g,197, d=+0.015); bq(g,137, d=+0.009); change at onset (after-before, per-camera median) +0.011 mag; largest seasonal dimming 0.02 mag at MJD 60045
- dust: excess flux W1 4.02 mJy, W2 3.19 mJy, T = 1887 K (16-84%: 1483-2597) 

### uid999033  [D2]  KILLED
- position 267.53313 -28.86257; Gaia DR3 4057393138528809088; G 14.94, BP-RP 1.58, plx 2.90 mas; plot `plots/uid999033.png`
- **KILL:** blend: Gaia neighbour within 6" only 2.16 mag fainter in G (2.1" PA37 G19.53 dG+4.58; 2.8" PA22 G20.43 dG+5.48; 3.1" PA238 G18.28 dG+3.34; 3.9" PA176 G20.69 dG+5.75; 4.6" PA231 G17.10 dG+2.16; 5.8" PA89 G20.58 dG+5.64; 7.8" PA179 G19.69 dG+4.74; 8.5" PA27 G18.40 dG+3.46; 9.4" PA175 G19.94 dG+5.00)
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 16 visits, 114 points; baseline W1 9.69, W1-W2 0.571; onset between MJD 60187 and 60387
- detector 2: excess 0.625 mag, z 26.0, jitter ratio 4.1
- field control: target step +0.048 (W1 +0.014); neighbours N=73, median +0.018, robust sigma 0.047, max +0.179; z = 0.6
- centroid: jump at onset 0.262" +- 0.111 (2.4 sigma, PA 41); largest consecutive-visit jump 0.344"; rms 0.171"; toward neighbour: 2.1" PA37 G19.5 (angle 3 deg); 2.8" PA22 G20.4 (angle 19 deg); 8.5" PA27 G18.4 (angle 13 deg); expected shift if a neighbour were the source: 2.1" G19.5: 0.09"; 2.8" G20.4: 0.12"; 3.1" G18.3: 0.13"; 3.9" G20.7: 0.17"; 4.6" G17.1: 0.20"; 5.8" G20.6: 0.25"; 7.8" G19.7: 0.33"; 8.5" G18.4: 0.36"; 9.4" G19.9: 0.40"
- AllWISE 2010: W1-W2 0.502, W2-W3 1.316 (W3 S/N 12.1), W3-W4 3.261 (W4 S/N 20.3), ext_flg 1, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.02, ipd_frac_multi_peak 0, NSS none, Teff 4497 K, logg 4.64, H-alpha pEW -0.029 nm, varclass none; M_G 7.26, -0.05 mag vs sequence (on the sequence); neighbours within 10": 2.1" PA37 G19.53 dG+4.58; 2.8" PA22 G20.43 dG+5.48; 3.1" PA238 G18.28 dG+3.34; 3.9" PA176 G20.69 dG+5.75; 4.6" PA231 G17.10 dG+2.16; 5.8" PA89 G20.58 dG+5.64; 7.8" PA179 G19.69 dG+4.74; 8.5" PA27 G18.40 dG+3.46; 9.4" PA175 G19.94 dG+5.00
- SIMBAD (10"): no object
- ASAS-SN: 0 points, cameras n/a; change at onset (after-before, per-camera median) n/a mag; largest seasonal dimming n/a mag at MJD n/a
- dust: excess flux W1 0.43 mJy, W2 1.76 mJy, T = 493 K (16-84%: 150-771) 
- checks missing: ASAS-SN (no source)

### uid1512338  [D2]  KILLED
- position 84.07700 -6.34410; Gaia DR3 3016953120847162240; G 14.51, BP-RP 1.85, plx 2.60 mas; plot `plots/uid1512338.png`
- **KILL:** eclipsing binary in SIMBAD (EB*, V* V832 Ori)
- **young:** SIMBAD young-star types Or*,TT*,Y*O (V* V832 Ori) | Gaia DR3 variability class YSO(0.33)
- flags: 1.46 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | not plain dust: optical brightening -0.043 mag (per-camera -0.013,-0.073) together with the infrared rise | largest seasonal optical dimming 0.14 mag (MJD 59497)
- NEOWISE: score refetch 0.31 (stored 0.30, reproduced True); dW2 0.047, dW1 0.002, 19 visits, 162 points; baseline W1 10.41, W1-W2 0.420; onset between MJD 57811 and 58013
- detector 2: excess 0.439 mag, z 12.1, jitter ratio 13.6
- field control: target step -0.003 (W1 -0.010); neighbours N=132, median -0.007, robust sigma 0.019, max +0.303; z = 0.2
- centroid: jump at onset 0.034" +- 0.025 (1.4 sigma, PA 61); largest consecutive-visit jump 0.043"; rms 0.033"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.475, W2-W3 2.139 (W3 S/N 34.2), W3-W4 1.736 (W4 S/N 9.8), ext_flg 0, ph_qual AAAB: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.22, ipd_frac_multi_peak 1, NSS none, Teff 6186 K, logg 4.33, H-alpha pEW -1.947 nm, varclass YSO(0.33); M_G 6.58, -1.46 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): V* V832 Ori [TT*; *,EB*,Em*,IR,MIR,NIR,Opt,Or*,TT*,V*,X,Y*O] 0.01" refs=49
- ASAS-SN: 1419 points, cameras bA(g,149); bE(g,216); ba(V,172, d=-0.013); be(V,195, d=-0.073); bi(g,305); bm(g,218); bq(g,164); change at onset (after-before, per-camera median) -0.043 mag; largest seasonal dimming 0.14 mag at MJD 59497
- dust: excess flux W1 0.46 mJy, W2 0.97 mJy, T = 695 K (16-84%: 565-857) 

### uid1533329  [D2]  KILLED
- position 83.90702 -5.10889; Gaia DR3 3209529799315558784; G 15.75, BP-RP 2.18, plx 2.59 mas; plot `plots/uid1533329.png`
- **KILL:** galaxy/QSO within 6" in SIMBAD: V* V362 Ori [G] 0.0"
- **young:** SIMBAD young-star types Or*,TT?,Y*O (V* V362 Ori)
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | 1.18 mag above the main sequence at its colour
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 14 visits, 108 points; baseline W1 11.41, W1-W2 0.511; onset between MJD 57646 and 57811
- detector 2: excess 0.479 mag, z 11.1, jitter ratio 6.4
- field control: target step -0.047 (W1 -0.057); neighbours N=87, median +0.002, robust sigma 0.027, max +0.431; z = -1.8
- centroid: jump at onset 0.039" +- 0.023 (1.7 sigma, PA 92); largest consecutive-visit jump 0.094"; rms 0.045"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.442, W2-W3 0.917 (W3 S/N -2.4), W3-W4 5.709 (W4 S/N 13.8), ext_flg 1, ph_qual AAUA: W3 S/N < 5: no W2-W3 class; W1-W2 > 0.25
- Gaia: RUWE 1.02, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW -1.227 nm, varclass none; M_G 7.82, -1.18 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): V* V362 Ori [Or*; *,Em*,G,IR,MIR,NIR,Or*,TT?,V*,X,Y*O] 0.02" refs=32; [KFP2017] Orion A 462 [cor; cor] 6.25" refs=1
- ASAS-SN: 1126 points, cameras bA(g,146); bE(g,210); ba(V,135, d=+0.039); be(V,192, d=+0.010); bi(g,174); bm(g,151); bq(g,118); change at onset (after-before, per-camera median) +0.024 mag; largest seasonal dimming 0.10 mag at MJD 59414
- dust: excess flux W1 -0.23 mJy, W2 -0.25 mJy, T = n/a K (16-84%: n/a-n/a) no W2 excess flux after onset

### uid1649098  [D2]  KILLED
- position 83.68833 -5.17989; Gaia DR3 3209525263830030336; G 15.23, BP-RP 1.89, plx 2.54 mas; plot `plots/uid1649098.png`
- **KILL:** blend: Gaia neighbour within 6" only 2.84 mag fainter in G (1.5" PA235 G18.07 dG+2.84)
- **young:** SIMBAD young-star types Or*,TT*,TT?,Y*O (V* XZ Ori)
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | 0.90 mag above the main sequence at its colour
- NEOWISE: score refetch 0.09 (stored 0.09, reproduced True); dW2 0.015, dW1 -0.018, 19 visits, 186 points; baseline W1 10.17, W1-W2 0.448; onset between MJD 57282 and 57447
- detector 2: excess 0.461 mag, z 12.3, jitter ratio 14.1
- field control: target step -0.068 (W1 +0.011); neighbours N=100, median -0.002, robust sigma 0.029, max +0.195; z = -2.3
- centroid: jump at onset 0.032" +- 0.020 (1.7 sigma, PA 40); largest consecutive-visit jump 0.062"; rms 0.035"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.550, W2-W3 -0.396 (W3 S/N -2.2), W3-W4 4.338 (W4 S/N -0.1), ext_flg 1, ph_qual AAUU: W3 S/N < 5: no W2-W3 class; W1-W2 > 0.25
- Gaia: RUWE 1.28, ipd_frac_multi_peak 1, NSS none, Teff 6169 K, logg 4.61, H-alpha pEW -3.631 nm, varclass none; M_G 7.25, -0.90 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 1.5" PA235 G18.07 dG+2.84
- SIMBAD (10"): V* XZ Ori [TT*; *,Em*,IR,MIR,NIR,Or*,TT*,TT?,V*,V*?,X,Y*O] 0.04" refs=61; [DRS2009] 1277 [*; *] 1.56" refs=1
- ASAS-SN: 1453 points, cameras bA(g,152); bE(g,217); ba(V,179, d=-0.025); be(V,194, d=+0.045); bi(g,337); bm(g,219); bq(g,155); change at onset (after-before, per-camera median) +0.010 mag; largest seasonal dimming 0.10 mag at MJD 60654
- dust: excess flux W1 -0.29 mJy, W2 -0.76 mJy, T = n/a K (16-84%: n/a-n/a) no W2 excess flux after onset

### uid896516  [D2]  KILLED
- position 81.17100 +1.91070; Gaia DR3 3222286505017306240; G 14.86, BP-RP 2.01, plx 2.97 mas; plot `plots/uid896516.png`
- **KILL:** eclipsing binary in SIMBAD (EB*, Kiso A-0903 109)
- **young:** SIMBAD young-star types TT*,Y*O (Kiso A-0903 109)
- flags: 1.26 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | optical dimming +0.435 mag after the infrared onset (debris transit signature) | largest seasonal optical dimming 0.60 mag (MJD 58442)
- NEOWISE: score refetch 0.95 (stored 0.95, reproduced True); dW2 0.189, dW1 0.268, 21 visits, 221 points; baseline W1 9.77, W1-W2 0.548; onset between MJD 57085 and 57279
- detector 2: excess 0.541 mag, z 13.0, jitter ratio 9.2
- field control: target step -0.042 (W1 -0.067); neighbours N=94, median -0.004, robust sigma 0.010, max +0.026; z = -3.7
- centroid: jump at onset 0.016" +- 0.017 (0.9 sigma, PA 242); largest consecutive-visit jump 0.083"; rms 0.031"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.572, W2-W3 1.869 (W3 S/N 61.7), W3-W4 2.017 (W4 S/N 29.9), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.28, ipd_frac_multi_peak 1, NSS none, Teff nan K, logg nan, H-alpha pEW -2.377 nm, varclass none; M_G 7.23, -1.26 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 8.4" PA178 G18.34 dG+3.48
- SIMBAD (10"): Kiso A-0903 109 [TT*; *,EB*,Em*,NIR,TT*,Y*O] 0.02" refs=34; Gaia DR3 3222286500721462784 [*; *] 8.40" refs=2
- ASAS-SN: 1236 points, cameras bA(g,168); bE(g,178); ba(V,210, d=+0.435); be(V,56); bi(g,282); bm(g,212); bq(g,130); change at onset (after-before, per-camera median) +0.435 mag; largest seasonal dimming 0.60 mag at MJD 58442
- dust: excess flux W1 6.18 mJy, W2 5.77 mJy, T = 1431 K (16-84%: 1223-1728) 

