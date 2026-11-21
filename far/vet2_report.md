# vet2 report: far target list (final)

Generated 2026-11-21 23:44 UTC; 145 targets; machine-generated, the plots in plots/ still need a look by eye.

Kill rules: field-control z < 5 (detector-1 and list targets); centroid jump > 3 sigma toward a Gaia neighbour; Gaia neighbour within 6" with dG < 3; baseline W1 < 8; SIMBAD CV / confirmed eclipsing binary (counterpart within 3"); SIMBAD galaxy/QSO within 6"; young star (SIMBAD Y*O, Y*?, TT*, TT?, Or*, Ae*, Ae?, pr* within 5" or Gaia variability class YSO) kills detector-1/list targets and labels detector-2 targets 'known/likely young star'. Flags (not kills): 'not plain dust' (optical brightening at the infrared onset in >= 2 ASAS-SN cameras, none dimming, median < -0.015 mag), SIMBAD '?' candidate types, RUWE, NSS, ext_flg, colour classes.

## Controls

| Control | Result | Detail |
|---|---|---|
| ASASSN-21qj | PASS | category SURVIVOR, SIMBAD 2MASS J08152329-3859234 (10 refs), field z 57.3, missing: none |
| J060000 | PASS | category SURVIVOR, largest ASAS-SN seasonal dimming 0.35 mag at MJD 58864 |
| V836 Tau | PASS | young: SIMBAD young-star types Or*,TT*,TT?,Y*?,Y*O (V* V836 Tau) | Gaia DR3 variability class YSO(0.83) |

Counts: {'YOUNG': 85, 'KILLED': 33, 'SURVIVOR': 27}

## Survivors (27)

### uid1144163  [D2]  SURVIVOR
- position 266.89948 -29.63303; Gaia DR3 4057203850731922560; G 12.79, BP-RP 1.03, plx 2.81 mas; plot `plots/uid1144163.png`
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 16 visits, 125 points; baseline W1 8.33, W1-W2 0.136; onset between MJD 58560 and 58927
- detector 2: excess 0.188 mag, z 12.7, jitter ratio 4.2
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
- position 123.84704 -38.98983; Gaia DR3 5539970601632026752; G 13.37, BP-RP 0.81, plx 1.76 mas; plot ``
- flags: centroid jump 0.349" (5.5 sigma, PA 56) away from the neighbour(s) 3.7" PA253 G16.9, as expected when the target itself brightens in a blended WISE PSF | largest seasonal optical dimming 1.11 mag (MJD 59529)
- NEOWISE: score refetch 38.04 (stored 38.04, reproduced True); dW2 0.738, dW1 0.332, 12 visits, 133 points; baseline W1 11.65, W1-W2 -0.057; onset between MJD 58072 and 58227
- field control: target step +0.803 (W1 +0.402); neighbours N=169, median -0.003, robust sigma 0.014, max +0.055; z = 57.3
- centroid: jump at onset 0.349" +- 0.063 (5.5 sigma, PA 56); largest consecutive-visit jump 0.212"; rms 0.109"; toward neighbour: none; expected shift if a neighbour were the source: 3.7" G16.9: 1.94"; 7.3" G18.7: 3.81"
- AllWISE 2010: W1-W2 -0.068, W2-W3 -0.498 (W3 S/N 2.3), W3-W4 3.219 (W4 S/N -2.6), ext_flg 0, ph_qual AACU: W3 S/N < 5: no W2-W3 class
- Gaia: RUWE 1.10, ipd_frac_multi_peak 0, NSS none, Teff 5761 K, logg 4.34, H-alpha pEW 0.112 nm, varclass none; M_G 4.60, +0.07 mag vs sequence (on the sequence); neighbours within 10": 3.7" PA253 G16.91 dG+3.54; 7.3" PA182 G18.67 dG+5.30
- SIMBAD (10"): 2MASS J08152329-3859234 [*; *,NIR] 0.15" refs=10; 2MASS J08152298-3859244 [*; *,NIR] 3.74" refs=1
- ASAS-SN: 1351 points, cameras bE(g,411); be(V,238, d=-0.018); bi(g,497); bm(g,205); change at onset (after-before, per-camera median) -0.018 mag; largest seasonal dimming 1.11 mag at MJD 59529
- dust: excess flux W1 2.72 mJy, W2 3.68 mJy, T = 953 K (16-84%: 934-972) 
- errors: plot: AttributeError("partially initialized module 'matplotlib.pyplot' has no attribute 'switch_backend' (most likely due to a circular import)")

### uid959202  [D2]  SURVIVOR
- position 123.56894 -34.93364; Gaia DR3 5546268776043673984; G 13.83, BP-RP 1.89, plx 2.93 mas; plot `plots/uid959202.png`
- flags: 1.99 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.61 mag (MJD 60691)
- NEOWISE: score refetch 1.96 (stored 1.96, reproduced True); dW2 0.366, dW1 0.067, 10 visits, 138 points; baseline W1 10.10, W1-W2 0.410; onset between MJD 57144 and 57338
- detector 2: excess 0.421 mag, z 11.2, jitter ratio 15.8
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
- detector 2: excess 0.223 mag, z 12.5, jitter ratio 7.9
- field control: target step +0.360 (W1 +0.265); neighbours N=72, median -0.002, robust sigma 0.009, max +0.057; z = 42.5
- centroid: jump at onset 0.017" +- 0.012 (1.4 sigma, PA 131); largest consecutive-visit jump 0.040"; rms 0.021"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.217, W2-W3 0.788 (W3 S/N 30.5), W3-W4 0.991 (W4 S/N 3.6), ext_flg 0, ph_qual AAAB: weak W3 excess (0.5 < W2-W3 < 1.0)
- Gaia: RUWE 1.13, ipd_frac_multi_peak 0, NSS none, Teff 6241 K, logg 4.50, H-alpha pEW -1.487 nm, varclass none; M_G 6.28, -0.36 mag vs sequence (on the sequence); neighbours within 10": none
- SIMBAD (10"): no object
- ASAS-SN: 1426 points, cameras bF(g,371); bf(V,279, d=-0.068); bj(g,444); bn(g,332); change at onset (after-before, per-camera median) -0.068 mag; largest seasonal dimming 0.29 mag at MJD 58530
- dust: excess flux W1 1.59 mJy, W2 1.18 mJy, T = 2204 K (16-84%: 1886-2686) 

### uid1137499  [D2]  SURVIVOR
- position 125.90621 -43.97173; Gaia DR3 5526017421124772992; G 14.94, BP-RP 1.80, plx 2.81 mas; plot `plots/uid1137499.png`
- flags: AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.12 mag (MJD 58643)
- NEOWISE: score refetch 1.05 (stored 1.05, reproduced True); dW2 0.274, dW1 0.234, 13 visits, 135 points; baseline W1 10.77, W1-W2 0.267; onset between MJD 57153 and 57347
- detector 2: excess 0.292 mag, z 8.5, jitter ratio 25.3
- field control: target step +0.398 (W1 +0.349); neighbours N=173, median -0.005, robust sigma 0.012, max +0.307; z = 33.9
- centroid: jump at onset 0.018" +- 0.015 (1.2 sigma, PA 106); largest consecutive-visit jump 0.047"; rms 0.028"; toward neighbour: 3.6" PA64 G20.3 (angle 42 deg); expected shift if a neighbour were the source: 3.6" G20.3: 1.12"; 6.4" G19.4: 1.97"; 9.2" G16.2: 2.83"
- AllWISE 2010: W1-W2 0.313, W2-W3 2.135 (W3 S/N 51.7), W3-W4 2.686 (W4 S/N 30.7), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.16, ipd_frac_multi_peak 0, NSS none, Teff 6212 K, logg 4.47, H-alpha pEW -5.394 nm, varclass none; M_G 7.19, -0.73 mag vs sequence (on the sequence); neighbours within 10": 3.6" PA64 G20.29 dG+5.34; 6.4" PA161 G19.41 dG+4.47; 9.2" PA247 G16.24 dG+1.29
- SIMBAD (10"): UCAC4 231-027438 [*; *,NIR] 0.18" refs=4
- ASAS-SN: 2288 points, cameras bF(g,368); bH(g,359); bf(V,186); bh(V,162); bj(g,382); bl(g,459); bn(g,174); bp(g,198); change at onset (after-before, per-camera median) n/a mag; largest seasonal dimming 0.12 mag at MJD 58643
- dust: excess flux W1 4.92 mJy, W2 4.00 mJy, T = 1807 K (16-84%: 1696-1935) 
- checks missing: ASAS-SN change at onset (no camera spans the onset)

### uid239897  [D2]  SURVIVOR
- position 222.73717 +36.20318; Gaia DR3 1293509154439630464; G 14.04, BP-RP 1.46, plx 3.62 mas; plot `plots/uid239897.png`
- flags: AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 1.25 (stored 1.25, reproduced True); dW2 0.095, dW1 0.073, 21 visits, 272 points; baseline W1 11.28, W1-W2 0.307; onset between MJD 57931 and 58134
- detector 2: excess 0.368 mag, z 18.2, jitter ratio 4.0
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
- detector 2: excess 0.398 mag, z 16.6, jitter ratio 5.9
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

### uid1277809  [D2]  SURVIVOR
- position 280.04305 +23.47269; Gaia DR3 4532694083738109824; G 14.77, BP-RP 1.56, plx 2.73 mas; plot `plots/uid1277809.png`
- flags: AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 20 visits, 244 points; baseline W1 11.55, W1-W2 0.483; onset between MJD 59837 and 60037
- detector 2: excess 0.539 mag, z 23.1, jitter ratio 5.9
- field control: target step +0.163 (W1 +0.071); neighbours N=127, median +0.000, robust sigma 0.012, max +0.036; z = 13.7
- centroid: jump at onset 0.008" +- 0.020 (0.4 sigma, PA 297); largest consecutive-visit jump 0.037"; rms 0.034"; toward neighbour: none; expected shift if a neighbour were the source: 8.7" G17.3: 1.21"
- AllWISE 2010: W1-W2 0.485, W2-W3 2.091 (W3 S/N 36.2), W3-W4 0.834 (W4 S/N 5.0), ext_flg 0, ph_qual AAAB: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.06, ipd_frac_multi_peak 1, NSS none, Teff 4485 K, logg 4.44, H-alpha pEW -0.198 nm, varclass RS(0.34); M_G 6.95, -0.31 mag vs sequence (on the sequence); neighbours within 10": 8.7" PA213 G17.27 dG+2.51
- SIMBAD (10"): ZTF J184010.33+232821.7 [BY*; *,BY*] 0.10" refs=4
- ASAS-SN: 0 points, cameras n/a; change at onset (after-before, per-camera median) n/a mag; largest seasonal dimming n/a mag at MJD n/a
- dust: excess flux W1 -0.12 mJy, W2 0.10 mJy, T = 150 K (16-84%: 150-150) W1 excess <= 0: colder than ~150 K (upper limit)
- checks missing: ASAS-SN (no source)

### uid325718  [D2]  SURVIVOR
- position 35.42480 +62.01116; Gaia DR3 513833673802372736; G 13.99, BP-RP 1.39, plx 3.51 mas; plot ``
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 9 visits, 95 points; baseline W1 11.35, W1-W2 0.948; onset between MJD 57986 and 58144
- detector 2: excess 1.011 mag, z 52.4, jitter ratio 7.8
- field control: target step +0.161 (W1 +0.004); neighbours N=199, median -0.006, robust sigma 0.014, max +0.162; z = 11.9
- centroid: jump at onset 0.444" +- 0.185 (2.4 sigma, PA 181); largest consecutive-visit jump 0.331"; rms 0.389"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 1.083, W2-W3 1.507 (W3 S/N 22.3), W3-W4 2.809 (W4 S/N 21.4), ext_flg 1, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.22, ipd_frac_multi_peak 0, NSS none, Teff 4702 K, logg 4.45, H-alpha pEW -0.037 nm, varclass none; M_G 6.71, -0.11 mag vs sequence (on the sequence); neighbours within 10": none
- SIMBAD (10"): no object
- ASAS-SN: 975 points, cameras bD(g,271); bd(V,177, d=+0.004); bs(g,284); bt(g,243); change at onset (after-before, per-camera median) +0.004 mag; largest seasonal dimming 0.02 mag at MJD 60563
- dust: excess flux W1 -0.05 mJy, W2 1.12 mJy, T = 150 K (16-84%: 150-398) W1 excess <= 0: colder than ~150 K (upper limit)
- errors: plot: AttributeError("partially initialized module 'matplotlib.pyplot' has no attribute 'switch_backend' (most likely due to a circular import)")

### uid783499  [D2]  SURVIVOR
- position 38.73477 -10.10700; Gaia DR3 5175340655722935296; G 15.68, BP-RP 1.95, plx 3.06 mas; plot `plots/uid783499.png`
- flags: AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 1.32 (stored 1.32, reproduced True); dW2 0.096, dW1 0.050, 22 visits, 206 points; baseline W1 12.05, W1-W2 0.382; onset between MJD 59216 and 59420
- detector 2: excess 0.384 mag, z 9.6, jitter ratio 4.5
- field control: target step +0.085 (W1 +0.093); neighbours N=17, median -0.007, robust sigma 0.008, max +0.021; z = 11.3
- centroid: jump at onset 0.014" +- 0.020 (0.7 sigma, PA 205); largest consecutive-visit jump 0.062"; rms 0.037"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.408, W2-W3 1.559 (W3 S/N 20.8), W3-W4 1.904 (W4 S/N 5.4), ext_flg 0, ph_qual AAAB: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 0.94, ipd_frac_multi_peak 0, NSS none, Teff 4005 K, logg 4.66, H-alpha pEW -0.043 nm, varclass none; M_G 8.11, -0.19 mag vs sequence (on the sequence); neighbours within 10": none
- SIMBAD (10"): no object
- ASAS-SN: 1132 points, cameras bC(g,156, d=+0.054); bG(g,177, d=+0.001); bc(V,64); be(V,29); bg(V,144); bk(g,223, d=+0.008); bo(g,180, d=+0.035); bs(g,159, d=-0.028); change at onset (after-before, per-camera median) +0.008 mag; largest seasonal dimming 0.07 mag at MJD 57013
- dust: excess flux W1 0.27 mJy, W2 0.28 mJy, T = 1235 K (16-84%: 1044-1516) 

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
- detector 2: excess 0.271 mag, z 18.3, jitter ratio 7.0
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
- detector 2: excess 0.485 mag, z 32.6, jitter ratio 4.7
- field control: target step +0.058 (W1 +0.029); neighbours N=35, median -0.003, robust sigma 0.013, max +0.032; z = 4.6
- centroid: jump at onset 0.007" +- 0.013 (0.5 sigma, PA 239); largest consecutive-visit jump 0.046"; rms 0.026"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.429, W2-W3 1.517 (W3 S/N 50.4), W3-W4 0.921 (W4 S/N 8.5), ext_flg 0, ph_qual AAAB: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.37, ipd_frac_multi_peak 0, NSS none, Teff 5461 K, logg 4.47, H-alpha pEW 0.105 nm, varclass none; M_G 5.22, -0.59 mag vs sequence (on the sequence); neighbours within 10": none
- SIMBAD (10"): UCAC4 379-068655 [*; *,MIR,NIR] 0.20" refs=1
- ASAS-SN: 1152 points, cameras bB(g,76); bF(g,124, d=-0.001); bb(V,111); bf(V,138); bj(g,281, d=+0.010); bn(g,230, d=-0.001); br(g,145, d=+0.006); cB(g,47); change at onset (after-before, per-camera median) +0.002 mag; largest seasonal dimming 0.00 mag at MJD 59039
- dust: excess flux W1 -0.14 mJy, W2 -0.01 mJy, T = n/a K (16-84%: n/a-n/a) no W2 excess flux after onset

### uid902493  [D2]  SURVIVOR
- position 96.96592 +5.52192; Gaia DR3 3131660633490179456; G 11.58, BP-RP 0.76, plx 2.97 mas; plot `plots/uid902493.png`
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association)
- NEOWISE: score refetch 0.35 (stored 0.35, reproduced True); dW2 0.023, dW1 -0.033, 16 visits, 121 points; baseline W1 10.00, W1-W2 0.083; onset between MJD 57662 and 57825
- detector 2: excess 0.117 mag, z 11.7, jitter ratio 5.9
- field control: target step +0.050 (W1 +0.069); neighbours N=187, median -0.006, robust sigma 0.021, max +0.117; z = 2.7
- centroid: jump at onset 0.224" +- 0.107 (2.1 sigma, PA 75); largest consecutive-visit jump 0.268"; rms 0.180"; toward neighbour: 6.7" PA70 G18.3 (angle 4 deg); 8.5" PA41 G19.7 (angle 34 deg); expected shift if a neighbour were the source: 6.7" G18.3: 0.30"; 8.5" G19.7: 0.38"
- AllWISE 2010: W1-W2 0.219, W2-W3 1.532 (W3 S/N 39.6), W3-W4 3.092 (W4 S/N 27.1), ext_flg 1, ph_qual AAAA: W3 excess only (W2-W3 > 1.0; debris-disk-like or blend)
- Gaia: RUWE 0.86, ipd_frac_multi_peak 0, NSS none, Teff 5910 K, logg 4.16, H-alpha pEW 0.172 nm, varclass none; M_G 3.94, -0.26 mag vs sequence (on the sequence); neighbours within 10": 6.7" PA70 G18.30 dG+6.72; 8.5" PA41 G19.69 dG+8.11
- SIMBAD (10"): TYC  141-925-1 [*; *,NIR] 0.37" refs=0
- ASAS-SN: 1063 points, cameras bD(g,180); bH(g,171); bd(V,177, d=+0.001); bl(g,240); bp(g,141); bt(g,154); change at onset (after-before, per-camera median) +0.001 mag; largest seasonal dimming 0.01 mag at MJD 59847
- dust: excess flux W1 0.06 mJy, W2 0.83 mJy, T = 320 K (16-84%: 150-692) 

### uid1084142  [D2]  SURVIVOR
- position 260.90633 -35.81510; Gaia DR3 5975325082505365376; G 12.74, BP-RP 1.32, plx 2.84 mas; plot `plots/uid1084142.png`
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | 1.62 mag above the main sequence at its colour
- NEOWISE: score refetch 0.77 (stored 0.77, reproduced True); dW2 0.047, dW1 0.012, 8 visits, 74 points; baseline W1 9.84, W1-W2 0.102; onset between MJD 58556 and 58920
- detector 2: excess 0.165 mag, z 9.3, jitter ratio 4.4
- field control: target step +0.085 (W1 +0.023); neighbours N=106, median +0.013, robust sigma 0.028, max +0.103; z = 2.6
- centroid: jump at onset 0.069" +- 0.185 (0.4 sigma, PA 185); largest consecutive-visit jump 0.999"; rms 0.271"; toward neighbour: 3.0" PA214 G20.3 (angle 29 deg); expected shift if a neighbour were the source: 3.0" G20.3: 0.23"; 6.5" G20.1: 0.49"
- AllWISE 2010: W1-W2 0.103, W2-W3 2.842 (W3 S/N 19.9), W3-W4 3.100 (W4 S/N 21.6), ext_flg 1, ph_qual AAAA: W3 excess only (W2-W3 > 1.0; debris-disk-like or blend)
- Gaia: RUWE 0.99, ipd_frac_multi_peak 0, NSS none, Teff 5854 K, logg 4.06, H-alpha pEW 0.174 nm, varclass none; M_G 5.01, -1.62 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 3.0" PA214 G20.35 dG+7.61; 6.5" PA292 G20.10 dG+7.36
- SIMBAD (10"): no object
- ASAS-SN: 994 points, cameras bH(g,341, d=-0.004); bh(V,178); bl(g,304, d=-0.012); bp(g,171, d=-0.000); change at onset (after-before, per-camera median) -0.004 mag; largest seasonal dimming 0.01 mag at MJD 58526
- dust: excess flux W1 0.57 mJy, W2 1.12 mJy, T = 724 K (16-84%: 150-2417) 

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

### uid775856  [D2]  SURVIVOR
- position 207.27850 -16.29816; Gaia DR3 6295379340956493952; G 11.22, BP-RP 1.35, plx 3.07 mas; plot `plots/uid775856.png`
- flags: 3.04 mag above the main sequence at its colour
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 21 visits, 161 points; baseline W1 8.47, W1-W2 0.039; onset between MJD 60128 and 60331
- detector 2: excess 0.102 mag, z 5.5, jitter ratio 5.1
- field control: target step +0.008 (W1 +0.066); neighbours N=26, median -0.024, robust sigma 0.014, max +0.005; z = 2.3
- centroid: jump at onset 0.031" +- 0.021 (1.5 sigma, PA 150); largest consecutive-visit jump 0.068"; rms 0.033"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.032, W2-W3 0.114 (W3 S/N 44.7), W3-W4 0.090 (W4 S/N 3.6), ext_flg 0, ph_qual AAAB: photosphere-like (W2-W3 < 0.5)
- Gaia: RUWE 0.91, ipd_frac_multi_peak 0, NSS none, Teff 5487 K, logg 3.63, H-alpha pEW -0.131 nm, varclass RS(0.49); M_G 3.65, -3.04 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): TYC 6123-460-1 [*; *,NIR] 0.37" refs=6; 1RXS J134907.0-161749 [X; X] 4.98" refs=0
- ASAS-SN: 1195 points, cameras bD(g,76, d=+0.152); bH(g,211, d=-0.012); bd(V,89); bf(V,55); bh(V,132); bl(g,259, d=-0.088); bp(g,238, d=-0.015); bt(g,135, d=+0.116); change at onset (after-before, per-camera median) -0.012 mag; largest seasonal dimming 0.07 mag at MJD 59309
- dust: excess flux W1 4.43 mJy, W2 0.07 mJy, T = 8000 K (16-84%: 8000-8000) ratio bluer than an 8000 K blackbody (not dust-like)

### uid220308  [D2]  SURVIVOR
- position 274.26638 +64.56526; Gaia DR3 2161325369818713984; G 11.45, BP-RP 0.71, plx 3.65 mas; plot ``
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
- errors: plot: AttributeError("partially initialized module 'matplotlib.pyplot' has no attribute 'switch_backend' (most likely due to a circular import)")

### uid126443  [D2]  SURVIVOR
- position 344.04495 +63.72553; Gaia DR3 2208143124690762368; G 13.42, BP-RP 1.21, plx 3.78 mas; plot `plots/uid126443.png`
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association)
- NEOWISE: score refetch 0.75 (stored 0.75, reproduced True); dW2 0.100, dW1 0.363, 13 visits, 181 points; baseline W1 11.23, W1-W2 0.117; onset between MJD 57038 and 57226
- detector 2: excess 0.178 mag, z 10.2, jitter ratio 4.4
- field control: target step -0.002 (W1 +0.016); neighbours N=194, median -0.008, robust sigma 0.010, max +0.097; z = 0.7
- centroid: jump at onset 0.234" +- 0.330 (0.7 sigma, PA 74); largest consecutive-visit jump 1.335"; rms 0.557"; toward neighbour: 5.7" PA44 G20.4 (angle 30 deg); expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 -0.326, W2-W3 0.222 (W3 S/N 15.2), W3-W4 0.806 (W4 S/N 2.2), ext_flg 1, ph_qual AAAC: photosphere-like (W2-W3 < 0.5)
- Gaia: RUWE 1.27, ipd_frac_multi_peak 0, NSS none, Teff 4885 K, logg 4.57, H-alpha pEW -0.037 nm, varclass SOLAR_LIKE(0.57); M_G 6.31, +0.04 mag vs sequence (on the sequence); neighbours within 10": 5.7" PA44 G20.42 dG+6.99; 7.6" PA258 G17.32 dG+3.90
- SIMBAD (10"): Gaia DR3 2208143124690762368 [*; *] 0.17" refs=1
- ASAS-SN: 1002 points, cameras bC(g,310); bc(V,172, d=+0.003); br(g,289); bs(g,231); change at onset (after-before, per-camera median) +0.003 mag; largest seasonal dimming 0.02 mag at MJD 59568
- dust: excess flux W1 3.50 mJy, W2 0.50 mJy, T = 8000 K (16-84%: 8000-8000) ratio bluer than an 8000 K blackbody (not dust-like)

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

### uid690873  [D2]  SURVIVOR
- position 269.27186 -26.55673; Gaia DR3 4064217566685938560; G 12.82, BP-RP 1.26, plx 3.14 mas; plot `plots/uid690873.png`
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | 1.12 mag above the main sequence at its colour
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 9 visits, 81 points; baseline W1 10.54, W1-W2 0.056; onset between MJD 59821 and 60024
- detector 2: excess 0.118 mag, z 6.6, jitter ratio 5.5
- field control: target step +0.019 (W1 -0.026); neighbours N=102, median +0.010, robust sigma 0.027, max +0.128; z = 0.3
- centroid: jump at onset 0.206" +- 0.196 (1.1 sigma, PA 115); largest consecutive-visit jump 0.519"; rms 0.218"; toward neighbour: 9.9" PA151 G18.9 (angle 36 deg); expected shift if a neighbour were the source: 9.6" G20.2: 0.17"; 9.9" G18.9: 0.17"
- AllWISE 2010: W1-W2 -0.118, W2-W3 0.282 (W3 S/N -4.5), W3-W4 2.458 (W4 S/N -3.9), ext_flg 1, ph_qual AAUU: W3 S/N < 5: no W2-W3 class
- Gaia: RUWE 0.76, ipd_frac_multi_peak 1, NSS none, Teff 5003 K, logg 4.26, H-alpha pEW 0.067 nm, varclass none; M_G 5.31, -1.12 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 9.6" PA182 G20.18 dG+7.36; 9.9" PA151 G18.92 dG+6.10
- SIMBAD (10"): no object
- ASAS-SN: 822 points, cameras bH(g,257, d=-0.010); bl(g,249, d=+0.009); bp(g,166, d=+0.012); bt(g,150, d=-0.004); change at onset (after-before, per-camera median) +0.003 mag; largest seasonal dimming 0.01 mag at MJD 60470
- dust: excess flux W1 -0.30 mJy, W2 -0.27 mJy, T = n/a K (16-84%: n/a-n/a) no W2 excess flux after onset

### uid704416  [D2]  SURVIVOR
- position 306.84149 -28.29312; Gaia DR3 6798054792794344064; G 13.71, BP-RP 1.18, plx 3.13 mas; plot `plots/uid704416.png`
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association)
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 9 visits, 75 points; baseline W1 11.44, W1-W2 0.043; onset between MJD 58759 and 58962
- detector 2: excess 0.103 mag, z 6.3, jitter ratio 9.8
- field control: target step -0.083 (W1 +0.011); neighbours N=19, median -0.017, robust sigma 0.021, max +0.045; z = -3.1
- centroid: jump at onset 0.029" +- 0.043 (0.7 sigma, PA 207); largest consecutive-visit jump 0.123"; rms 0.052"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 -0.061, W2-W3 0.058 (W3 S/N 5.2), W3-W4 2.802 (W4 S/N 0.6), ext_flg 1, ph_qual AABU: photosphere-like (W2-W3 < 0.5)
- Gaia: RUWE 1.08, ipd_frac_multi_peak 7, NSS none, Teff 4813 K, logg 4.52, H-alpha pEW 0.029 nm, varclass none; M_G 6.18, +0.01 mag vs sequence (on the sequence); neighbours within 10": 1.3" PA11 G17.58 dG+3.87
- SIMBAD (10"): no object
- ASAS-SN: 1345 points, cameras bE(g,240, d=-0.013); be(V,220); bi(g,282, d=+0.009); bm(g,235, d=-0.006); bn(g,211, d=-0.004); bq(g,157, d=+0.004); change at onset (after-before, per-camera median) -0.004 mag; largest seasonal dimming 0.01 mag at MJD 60628
- dust: excess flux W1 0.05 mJy, W2 -0.47 mJy, T = n/a K (16-84%: n/a-n/a) no W2 excess flux after onset

## Known/likely young stars (detector 2) (85)

### uid1355017  [D2]  YOUNG
- position 313.27661 +74.84301; Gaia DR3 2277845423082083200; G 11.98, BP-RP 1.36, plx 2.68 mas; plot `plots/uid1355017.png`
- **young:** SIMBAD young-star types Or*,Y*O (GSC 04472-00143) | Gaia DR3 variability class YSO(0.38)
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | 2.62 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 3.26 (stored 3.26, reproduced True); dW2 1.508, dW1 1.573, 21 visits, 554 points; baseline W1 9.19, W1-W2 0.519; onset between MJD 58137 and 58343
- detector 2: excess 0.582 mag, z 30.8, jitter ratio 11.2
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
- detector 2: excess 0.600 mag, z 16.0, jitter ratio 11.9
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

### uid1048217  [D2]  YOUNG
- position 81.44487 +0.54828; Gaia DR3 3221844226465235712; G 14.20, BP-RP 1.79, plx 2.87 mas; plot `plots/uid1048217.png`
- **young:** SIMBAD young-star types Y*?,Y*O (UCAC4 453-010343)
- flags: 1.40 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | possible optical brightening at onset (-0.049 mag, one camera only) | largest seasonal optical dimming 0.27 mag (MJD 58182)
- NEOWISE: score refetch 1.59 (stored 1.59, reproduced True); dW2 0.919, dW1 0.692, 20 visits, 184 points; baseline W1 10.29, W1-W2 0.793; onset between MJD 57086 and 57280
- detector 2: excess 0.820 mag, z 24.3, jitter ratio 13.0
- field control: target step +0.612 (W1 +0.452); neighbours N=61, median -0.005, robust sigma 0.011, max +0.018; z = 55.5
- centroid: jump at onset 0.023" +- 0.019 (1.2 sigma, PA 274); largest consecutive-visit jump 0.095"; rms 0.038"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.778, W2-W3 2.477 (W3 S/N 73.7), W3-W4 2.487 (W4 S/N 43.5), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.08, ipd_frac_multi_peak 0, NSS none, Teff 4458 K, logg 4.29, H-alpha pEW -0.092 nm, varclass none; M_G 6.49, -1.40 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): UCAC4 453-010343 [Y*O; *,MIR,NIR,Y*?,Y*O] 0.02" refs=19
- ASAS-SN: 927 points, cameras bA(g,166); bE(g,69); ba(V,208, d=-0.049); be(V,56); bi(g,172); bm(g,158); bq(g,98); change at onset (after-before, per-camera median) -0.049 mag; largest seasonal dimming 0.27 mag at MJD 58182
- dust: excess flux W1 13.34 mJy, W2 22.40 mJy, T = 803 K (16-84%: 792-814) 

### uid857434  [D2]  YOUNG
- position 83.27600 -0.70550; Gaia DR3 3220679568773158016; G 14.22, BP-RP 1.96, plx 3.00 mas; plot `plots/uid857434.png`
- **young:** SIMBAD young-star types Or*,TT*,Y*O (CVSO 115) | Gaia DR3 variability class YSO(0.56)
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | 1.74 mag above the main sequence at its colour | optical dimming +0.064 mag after the infrared onset (debris transit signature) | largest seasonal optical dimming 0.33 mag (MJD 57094)
- NEOWISE: score refetch 0.38 (stored 0.38, reproduced True); dW2 0.132, dW1 0.116, 19 visits, 207 points; baseline W1 10.40, W1-W2 0.323; onset between MJD 57087 and 57282
- detector 2: excess 0.323 mag, z 7.9, jitter ratio 17.1
- field control: target step +0.562 (W1 +0.340); neighbours N=94, median -0.003, robust sigma 0.011, max +0.177; z = 50.8
- centroid: jump at onset 0.024" +- 0.015 (1.6 sigma, PA 14); largest consecutive-visit jump 0.090"; rms 0.034"; toward neighbour: none; expected shift if a neighbour were the source: 3.6" G19.1: 1.47"; 8.0" G19.3: 3.22"
- AllWISE 2010: W1-W2 0.126, W2-W3 0.482 (W3 S/N 13.5), W3-W4 4.048 (W4 S/N 18.7), ext_flg 1, ph_qual AAAA: photosphere-like (W2-W3 < 0.5)
- Gaia: RUWE 1.34, ipd_frac_multi_peak 0, NSS none, Teff 4125 K, logg 4.08, H-alpha pEW -0.192 nm, varclass YSO(0.56); M_G 6.61, -1.74 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 3.6" PA95 G19.12 dG+4.90; 8.0" PA323 G19.32 dG+5.10
- SIMBAD (10"): CVSO 115 [TT*; *,NIR,Or*,TT*,Y*O] 0.03" refs=17
- ASAS-SN: 1420 points, cameras bC(g,151); bG(g,222); ba(V,51); bc(V,151, d=+0.074); be(V,38, d=+0.054); bg(V,153); bk(g,297); bo(g,201); bs(g,156); change at onset (after-before, per-camera median) +0.064 mag; largest seasonal dimming 0.33 mag at MJD 57094
- dust: excess flux W1 2.66 mJy, W2 2.44 mJy, T = 1477 K (16-84%: 1334-1657) 

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

### uid835189  [D2]  YOUNG
- position 78.18641 -1.09027; Gaia DR3 3215349651798096768; G 12.98, BP-RP 1.38, plx 3.02 mas; plot `plots/uid835189.png`
- **young:** SIMBAD young-star types Y*? (UCAC4 445-008861)
- flags: 1.41 mag above the main sequence at its colour
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 18 visits, 210 points; baseline W1 10.15, W1-W2 0.187; onset between MJD 56720 and 56912
- detector 2: excess 0.250 mag, z 13.0, jitter ratio 14.4
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
- detector 2: excess 0.267 mag, z 11.2, jitter ratio 15.4
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

### uid1069828  [D2]  YOUNG
- position 80.72662 +4.94878; Gaia DR3 3237214505668335488; G 14.77, BP-RP 2.19, plx 2.85 mas; plot `plots/uid1069828.png`
- **young:** SIMBAD young-star types TT*,Y*?,Y*O (CVSO 567)
- flags: 2.00 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.10 mag (MJD 58191)
- NEOWISE: score refetch 0.78 (stored 0.78, reproduced True); dW2 0.140, dW1 0.097, 21 visits, 249 points; baseline W1 10.54, W1-W2 0.324; onset between MJD 57809 and 58008
- detector 2: excess 0.292 mag, z 6.8, jitter ratio 13.8
- field control: target step +0.416 (W1 +0.342); neighbours N=63, median -0.007, robust sigma 0.014, max +0.018; z = 30.0
- centroid: jump at onset 0.018" +- 0.016 (1.1 sigma, PA 246); largest consecutive-visit jump 0.062"; rms 0.026"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.282, W2-W3 1.363 (W3 S/N 35.8), W3-W4 3.359 (W4 S/N 25.6), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.07, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW -0.630 nm, varclass none; M_G 7.05, -2.00 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): CVSO 567 [TT*; *,MIR,NIR,TT*,Y*?,Y*O] 0.02" refs=4
- ASAS-SN: 1264 points, cameras bD(g,197); bH(g,148); bd(V,250, d=+0.137); bh(V,51, d=-0.025); bl(g,265); bp(g,222); bt(g,131); change at onset (after-before, per-camera median) +0.056 mag; largest seasonal dimming 0.10 mag at MJD 58191
- dust: excess flux W1 4.37 mJy, W2 4.29 mJy, T = 1339 K (16-84%: 1279-1405) 

### uid1197713  [D2]  YOUNG
- position 81.73074 +1.67289; Gaia DR3 3222237885987655424; G 15.31, BP-RP 1.93, plx 2.77 mas; plot `plots/uid1197713.png`
- **young:** SIMBAD young-star types TT?,Y*?,Y*O (Kiso A-0903 134) | Gaia DR3 variability class YSO(0.43)
- flags: AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | not plain dust: optical brightening -0.089 mag (per-camera -0.106,-0.180,-0.059,-0.089,-0.016) together with the infrared rise
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 21 visits, 223 points; baseline W1 10.61, W1-W2 0.417; onset between MJD 58740 and 58898
- detector 2: excess 0.423 mag, z 11.0, jitter ratio 11.6
- field control: target step +0.347 (W1 +0.244); neighbours N=87, median -0.001, robust sigma 0.012, max +0.040; z = 29.3
- centroid: jump at onset 0.063" +- 0.021 (3.0 sigma, PA 247); largest consecutive-visit jump 0.118"; rms 0.034"; toward neighbour: none; expected shift if a neighbour were the source: 6.9" G16.1: 1.88"
- AllWISE 2010: W1-W2 0.438, W2-W3 1.512 (W3 S/N 44.8), W3-W4 2.529 (W4 S/N 23.1), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.11, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW -2.490 nm, varclass YSO(0.43); M_G 7.53, -0.72 mag vs sequence (on the sequence); neighbours within 10": 6.9" PA96 G16.12 dG+0.81
- SIMBAD (10"): Kiso A-0903 134 [Y*O; *,Em*,IR,MIR,NIR,TT?,V*,Y*?,Y*O] 0.03" refs=31
- ASAS-SN: 1215 points, cameras bA(g,168, d=-0.106); bE(g,177, d=-0.180); ba(V,210); be(V,56); bi(g,284, d=-0.059); bm(g,193, d=-0.089); bq(g,127, d=-0.016); change at onset (after-before, per-camera median) -0.089 mag; largest seasonal dimming 0.09 mag at MJD 58880
- dust: excess flux W1 -0.07 mJy, W2 0.19 mJy, T = 150 K (16-84%: 150-588) W1 excess <= 0: colder than ~150 K (upper limit)

### uid1435805  [D2]  YOUNG
- position 80.47611 -2.29051; Gaia DR3 3214120329078892544; G 14.37, BP-RP 1.78, plx 2.64 mas; plot `plots/uid1435805.png`
- **young:** SIMBAD young-star types TT*,Y*?,Y*O (CVSO 504)
- flags: centroid jump 0.061" (3.0 sigma, PA 337) away from the neighbour(s) 6.5" PA153 G15.4, as expected when the target itself brightens in a blended WISE PSF | AllWISE ext_flg = 1 (extended or 2MASS XSC association) | 1.39 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | not plain dust: optical brightening -0.249 mag (per-camera -0.398,-0.099) together with the infrared rise | largest seasonal optical dimming 0.46 mag (MJD 59787)
- NEOWISE: score refetch 2.18 (stored 2.19, reproduced True); dW2 0.214, dW1 0.194, 21 visits, 229 points; baseline W1 9.33, W1-W2 0.368; onset between MJD 57808 and 58007
- detector 2: excess 0.396 mag, z 11.9, jitter ratio 9.6
- field control: target step +0.273 (W1 +0.271); neighbours N=53, median -0.005, robust sigma 0.010, max +0.037; z = 28.9
- centroid: jump at onset 0.061" +- 0.020 (3.0 sigma, PA 337); largest consecutive-visit jump 0.090"; rms 0.041"; toward neighbour: none; expected shift if a neighbour were the source: 6.5" G15.4: 1.45"
- AllWISE 2010: W1-W2 0.413, W2-W3 1.292 (W3 S/N 58.7), W3-W4 2.225 (W4 S/N 30.3), ext_flg 1, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.23, ipd_frac_multi_peak 1, NSS none, Teff nan K, logg nan, H-alpha pEW -1.026 nm, varclass none; M_G 6.48, -1.39 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 6.5" PA153 G15.45 dG+1.08
- SIMBAD (10"): CVSO 504 [TT*; *,NIR,TT*,Y*?,Y*O] 0.02" refs=10; Gaia DR3 3214120329078892800 [Y*?; *,Y*?] 6.48" refs=3
- ASAS-SN: 1482 points, cameras bD(g,160); bH(g,205); bb(V,55); bd(V,156, d=-0.398); bf(V,40); bh(V,152, d=-0.099); bl(g,326); bp(g,216); bt(g,172); change at onset (after-before, per-camera median) -0.249 mag; largest seasonal dimming 0.46 mag at MJD 59787
- dust: excess flux W1 13.82 mJy, W2 12.07 mJy, T = 1587 K (16-84%: 1478-1712) 

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
- detector 2: excess 0.483 mag, z 27.2, jitter ratio 18.4
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
- detector 2: excess 0.380 mag, z 14.4, jitter ratio 13.9
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

### uid955772  [D2]  YOUNG
- position 77.79844 -8.10347; Gaia DR3 3206972403988810752; G 15.06, BP-RP 2.12, plx 2.93 mas; plot `plots/uid955772.png`
- **young:** SIMBAD young-star types Y*?,Y*O (UCAC4 410-008105) | Gaia DR3 variability class YSO(0.11)
- flags: 1.44 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | optical dimming +0.084 mag after the infrared onset (debris transit signature) | largest seasonal optical dimming 0.16 mag (MJD 56980)
- NEOWISE: score refetch 0.61 (stored 0.61, reproduced True); dW2 0.142, dW1 0.044, 20 visits, 205 points; baseline W1 11.42, W1-W2 0.328; onset between MJD 59099 and 59257
- detector 2: excess 0.303 mag, z 7.0, jitter ratio 11.9
- field control: target step +0.225 (W1 +0.092); neighbours N=48, median -0.002, robust sigma 0.009, max +0.042; z = 24.4
- centroid: jump at onset 0.025" +- 0.020 (1.3 sigma, PA 224); largest consecutive-visit jump 0.096"; rms 0.032"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.397, W2-W3 2.178 (W3 S/N 39.6), W3-W4 2.351 (W4 S/N 17.2), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.15, ipd_frac_multi_peak 0, NSS none, Teff 3938 K, logg 4.26, H-alpha pEW -0.158 nm, varclass YSO(0.11); M_G 7.39, -1.44 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): UCAC4 410-008105 [Y*O; *,MIR,NIR,Y*?,Y*O] 0.02" refs=3
- ASAS-SN: 2125 points, cameras bC(g,99, d=+0.050); bF(g,176, d=+0.123); bG(g,233, d=+0.020); ba(V,32); bc(V,140); be(V,34); bf(V,167); bg(V,170); bj(g,223, d=+0.116); bk(g,358, d=+0.069); bn(g,188, d=+0.232); bo(g,202, d=+0.045); bs(g,103, d=+0.100); change at onset (after-before, per-camera median) +0.084 mag; largest seasonal dimming 0.16 mag at MJD 56980
- dust: excess flux W1 1.41 mJy, W2 1.85 mJy, T = 974 K (16-84%: 935-1014) 

### uid1018261  [D2]  YOUNG
- position 328.15812 +72.57478; Gaia DR3 2272880410824048512; G 14.86, BP-RP 2.00, plx 2.89 mas; plot `plots/uid1018261.png`
- **young:** SIMBAD young-star types Y*? (UCAC4 813-029498) | Gaia DR3 variability class YSO(0.55)
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | 1.29 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | not plain dust: optical brightening -0.286 mag (per-camera -0.309,-0.263) together with the infrared rise | largest seasonal optical dimming 0.36 mag (MJD 58266)
- NEOWISE: score refetch 4.97 (stored 4.97, reproduced True); dW2 0.659, dW1 0.453, 21 visits, 394 points; baseline W1 10.58, W1-W2 0.619; onset between MJD 58336 and 58494
- detector 2: excess 0.613 mag, z 14.8, jitter ratio 13.1
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

### uid1003353  [D2]  YOUNG
- position 79.68332 +0.89593; Gaia DR3 3233737575023512704; G 14.70, BP-RP 1.96, plx 2.90 mas; plot `plots/uid1003353.png`
- **young:** SIMBAD young-star types TT*,Y*?,Y*O (CVSO 415)
- flags: 1.32 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 2.47 (stored 2.47, reproduced True); dW2 0.217, dW1 0.102, 19 visits, 206 points; baseline W1 11.23, W1-W2 0.331; onset between MJD 57084 and 57278
- detector 2: excess 0.332 mag, z 8.2, jitter ratio 7.7
- field control: target step +0.280 (W1 +0.231); neighbours N=59, median -0.004, robust sigma 0.012, max +0.019; z = 23.9
- centroid: jump at onset 0.011" +- 0.021 (0.5 sigma, PA 345); largest consecutive-visit jump 0.050"; rms 0.027"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.381, W2-W3 2.300 (W3 S/N 43.2), W3-W4 1.403 (W4 S/N 10.9), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.01, ipd_frac_multi_peak 0, NSS none, Teff 3858 K, logg 4.13, H-alpha pEW -0.004 nm, varclass none; M_G 7.01, -1.32 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): CVSO 415 [TT*; *,MIR,NIR,TT*,Y*?,Y*O] 0.02" refs=9
- ASAS-SN: 1125 points, cameras bB(g,99); bF(g,168); bb(V,252, d=-0.006); bf(V,55); bj(g,212); bn(g,211); br(g,128); change at onset (after-before, per-camera median) -0.006 mag; largest seasonal dimming 0.06 mag at MJD 58181
- dust: excess flux W1 1.96 mJy, W2 1.77 mJy, T = 1500 K (16-84%: 1387-1633) 

### uid1315434  [D2]  YOUNG
- position 82.70000 -7.52567; Gaia DR3 3016413501156518400; G 14.29, BP-RP 1.79, plx 2.71 mas; plot `plots/uid1315434.png`
- **young:** SIMBAD young-star types Y*?,Y*O (2MASS J05304799-0731323)
- flags: 1.44 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | not plain dust: optical brightening -0.065 mag (per-camera -0.103,-0.028) together with the infrared rise
- NEOWISE: score refetch 1.02 (stored 1.01, reproduced True); dW2 0.194, dW1 0.206, 20 visits, 214 points; baseline W1 10.60, W1-W2 0.332; onset between MJD 57445 and 57645
- detector 2: excess 0.359 mag, z 10.6, jitter ratio 15.3
- field control: target step +0.240 (W1 +0.087); neighbours N=66, median -0.003, robust sigma 0.011, max +0.023; z = 22.6
- centroid: jump at onset 0.017" +- 0.015 (1.2 sigma, PA 249); largest consecutive-visit jump 0.045"; rms 0.035"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.315, W2-W3 2.277 (W3 S/N 53.9), W3-W4 1.561 (W4 S/N 15.2), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.18, ipd_frac_multi_peak 0, NSS none, Teff 4448 K, logg 4.15, H-alpha pEW -0.107 nm, varclass none; M_G 6.45, -1.44 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): 2MASS J05304799-0731323 [Y*O; *,NIR,Y*?,Y*O] 0.01" refs=7
- ASAS-SN: 1515 points, cameras bA(g,158); bE(g,220); ba(V,179, d=-0.103); be(V,195, d=-0.028); bi(g,345); bm(g,247); bq(g,171); change at onset (after-before, per-camera median) -0.065 mag; largest seasonal dimming 0.09 mag at MJD 59496
- dust: excess flux W1 0.78 mJy, W2 2.51 mJy, T = 551 K (16-84%: 510-594) 

### uid1408208  [D2]  YOUNG
- position 333.92469 +69.64908; Gaia DR3 2223295734949415168; G 11.42, BP-RP 1.11, plx 2.66 mas; plot `plots/uid1408208.png`
- **young:** SIMBAD young-star types Or*,Y*O (TYC 4467-324-1) | Gaia DR3 variability class YSO(0.20)
- flags: 2.40 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | not plain dust: optical brightening -0.033 mag (per-camera -0.043,-0.024) together with the infrared rise
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 22 visits, 413 points; baseline W1 8.35, W1-W2 0.550; onset between MJD 59584 and 59791
- detector 2: excess 0.607 mag, z 38.1, jitter ratio 7.3
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
- detector 2: excess 0.480 mag, z 15.0, jitter ratio 5.9
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
- detector 2: excess 0.355 mag, z 10.4, jitter ratio 5.9
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
- detector 2: excess 0.438 mag, z 12.3, jitter ratio 11.5
- field control: target step +0.204 (W1 +0.194); neighbours N=103, median -0.002, robust sigma 0.010, max +0.102; z = 19.8
- centroid: jump at onset 0.031" +- 0.017 (1.8 sigma, PA 114); largest consecutive-visit jump 0.080"; rms 0.026"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.458, W2-W3 1.770 (W3 S/N 63.6), W3-W4 1.992 (W4 S/N 29.1), ext_flg 1, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.16, ipd_frac_multi_peak 0, NSS none, Teff 4972 K, logg 4.20, H-alpha pEW -2.262 nm, varclass YSO(0.79); M_G 6.33, -1.64 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): [K98c] Em* 109 [Or*; *,Em*,LP*,NIR,Or*,Y*?,Y*O] 0.09" refs=11
- ASAS-SN: 1366 points, cameras bA(g,331, d=+0.014); bB(g,110, d=+0.027); ba(V,250); bb(V,163); bq(g,261, d=-0.042); br(g,251, d=-0.010); change at onset (after-before, per-camera median) +0.002 mag; largest seasonal dimming 0.17 mag at MJD 59886
- dust: excess flux W1 -0.24 mJy, W2 0.22 mJy, T = 150 K (16-84%: 150-531) W1 excess <= 0: colder than ~150 K (upper limit)

### uid781730  [D2]  YOUNG
- position 83.18253 -0.45423; Gaia DR3 3220703856813064448; G 11.28, BP-RP 1.11, plx 3.06 mas; plot `plots/uid781730.png`
- **young:** Gaia DR3 variability class YSO(0.18)
- flags: 2.20 mag above the main sequence at its colour
- NEOWISE: score refetch 1.55 (stored 1.55, reproduced True); dW2 0.177, dW1 0.125, 18 visits, 177 points; baseline W1 9.05, W1-W2 0.101; onset between MJD 57087 and 57281
- detector 2: excess 0.158 mag, z 10.0, jitter ratio 8.3
- field control: target step +0.227 (W1 +0.156); neighbours N=103, median -0.003, robust sigma 0.012, max +0.191; z = 19.4
- centroid: jump at onset 0.024" +- 0.016 (1.5 sigma, PA 60); largest consecutive-visit jump 0.046"; rms 0.024"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.157, W2-W3 1.382 (W3 S/N 42.3), W3-W4 4.152 (W4 S/N 47.1), ext_flg 0, ph_qual AAAA: W3 excess only (W2-W3 > 1.0; debris-disk-like or blend)
- Gaia: RUWE 0.99, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW -1.403 nm, varclass YSO(0.18); M_G 3.71, -2.20 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): TYC 4766-937-1 [Em*; *,Em*,NIR,Opt] 0.03" refs=12
- ASAS-SN: 0 points, cameras n/a; change at onset (after-before, per-camera median) n/a mag; largest seasonal dimming n/a mag at MJD n/a
- dust: excess flux W1 10.36 mJy, W2 9.28 mJy, T = 1525 K (16-84%: 1389-1691) 
- checks missing: ASAS-SN (no source)

### uid1284783  [D2]  YOUNG
- position 84.61071 -2.20486; Gaia DR3 3216517706809394560; G 15.39, BP-RP 1.86, plx 2.72 mas; plot `plots/uid1284783.png`
- **young:** SIMBAD young-star types Or*,TT*,Y*O (V* V2730 Ori) | Gaia DR3 variability class YSO(0.53)
- flags: AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | possible optical brightening at onset (-1.124 mag, one camera only) | largest seasonal optical dimming 0.55 mag (MJD 57022)
- NEOWISE: score refetch 2.22 (stored 2.22, reproduced True); dW2 0.328, dW1 0.133, 21 visits, 218 points; baseline W1 10.33, W1-W2 0.513; onset between MJD 57089 and 57283
- detector 2: excess 0.528 mag, z 14.4, jitter ratio 13.9
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
- detector 2: excess 0.549 mag, z 28.5, jitter ratio 13.7
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
- detector 2: excess 0.586 mag, z 16.4, jitter ratio 9.6
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

### uid310080  [D2]  YOUNG
- position 78.56621 -1.64957; Gaia DR3 3215095114856015232; G 11.95, BP-RP 1.44, plx 3.53 mas; plot `plots/uid310080.png`
- **young:** SIMBAD young-star types Y*?,Y*O (IRAS 05117-0142)
- flags: 2.25 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 0.42 (stored 0.41, reproduced True); dW2 0.089, dW1 0.094, 20 visits, 236 points; baseline W1 8.71, W1-W2 0.263; onset between MJD 57806 and 58005
- detector 2: excess 0.325 mag, z 16.5, jitter ratio 14.8
- field control: target step +0.189 (W1 +0.189); neighbours N=51, median -0.001, robust sigma 0.010, max +0.091; z = 18.4
- centroid: jump at onset 0.017" +- 0.018 (0.9 sigma, PA 267); largest consecutive-visit jump 0.040"; rms 0.028"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.293, W2-W3 2.464 (W3 S/N 76.3), W3-W4 2.564 (W4 S/N 49.5), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.05, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW -0.519 nm, varclass RS(0.53); M_G 4.69, -2.25 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): IRAS 05117-0142 [Y*O; *,IR,NIR,Y*?,Y*O] 0.05" refs=7
- ASAS-SN: 2647 points, cameras bC(g,183); bD(g,166); bG(g,211); bH(g,206); bc(V,119, d=+0.055); be(V,40); bg(V,185, d=+0.030); bh(V,152, d=+0.032); bk(g,298); bl(g,323); bo(g,233); bp(g,213); bs(g,143); bt(g,175); change at onset (after-before, per-camera median) +0.032 mag; largest seasonal dimming 0.03 mag at MJD 59282
- dust: excess flux W1 15.81 mJy, W2 10.53 mJy, T = 3066 K (16-84%: 2490-4061) 

### uid1376645  [D2]  YOUNG
- position 82.95572 -6.00537; Gaia DR3 3016848735963141760; G 13.27, BP-RP 1.43, plx 2.67 mas; plot `plots/uid1376645.png`
- **young:** SIMBAD young-star types Or*,TT*,Y*?,Y*O (V* V1207 Ori)
- flags: 1.51 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 2.16 (stored 2.16, reproduced True); dW2 0.183, dW1 0.185, 19 visits, 218 points; baseline W1 10.21, W1-W2 0.274; onset between MJD 57446 and 57645
- detector 2: excess 0.336 mag, z 17.4, jitter ratio 8.3
- field control: target step +0.219 (W1 +0.193); neighbours N=57, median +0.000, robust sigma 0.013, max +0.053; z = 17.4
- centroid: jump at onset 0.007" +- 0.013 (0.5 sigma, PA 237); largest consecutive-visit jump 0.035"; rms 0.023"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.287, W2-W3 1.963 (W3 S/N 50.3), W3-W4 3.193 (W4 S/N 33.3), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.32, ipd_frac_multi_peak 0, NSS none, Teff 4752 K, logg 4.17, H-alpha pEW -0.233 nm, varclass none; M_G 5.40, -1.51 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): V* V1207 Ori [TT*; *,Er*,MIR,NIR,Or*,TT*,V*,Y*?,Y*O] 0.01" refs=16
- ASAS-SN: 1499 points, cameras bA(g,155); bE(g,216); ba(V,177, d=+0.023); be(V,195, d=+0.001); bi(g,341); bm(g,246); bq(g,169); change at onset (after-before, per-camera median) +0.012 mag; largest seasonal dimming 0.08 mag at MJD 60315
- dust: excess flux W1 5.56 mJy, W2 3.86 mJy, T = 2658 K (16-84%: 2312-3137) 

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

### uid1052915  [D2]  YOUNG
- position 123.39806 -35.02856; Gaia DR3 5546261560498935936; G 14.55, BP-RP 2.14, plx 2.86 mas; plot `plots/uid1052915.png`
- **young:** SIMBAD young-star types Y*? (UCAC4 275-030249)
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | 2.05 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | possible optical brightening at onset (-0.030 mag, one camera only)
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 12 visits, 126 points; baseline W1 10.91, W1-W2 0.345; onset between MJD 57503 and 57703
- detector 2: excess 0.318 mag, z 7.4, jitter ratio 4.3
- field control: target step +0.202 (W1 +0.170); neighbours N=145, median -0.002, robust sigma 0.013, max +0.040; z = 16.2
- centroid: jump at onset 0.034" +- 0.015 (2.3 sigma, PA 346); largest consecutive-visit jump 0.074"; rms 0.034"; toward neighbour: none; expected shift if a neighbour were the source: 5.2" G18.8: 0.89"
- AllWISE 2010: W1-W2 0.303, W2-W3 2.310 (W3 S/N 47.6), W3-W4 2.330 (W4 S/N 29.7), ext_flg 1, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.28, ipd_frac_multi_peak 0, NSS none, Teff 6280 K, logg 4.32, H-alpha pEW -0.830 nm, varclass none; M_G 6.84, -2.05 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 5.2" PA66 G18.82 dG+4.27
- SIMBAD (10"): UCAC4 275-030249 [Y*?; *,MIR,NIR,Y*?] 0.22" refs=2
- ASAS-SN: 1256 points, cameras bH(g,336); bh(V,216, d=-0.030); bl(g,492); bp(g,212); change at onset (after-before, per-camera median) -0.030 mag; largest seasonal dimming 0.07 mag at MJD 58421
- dust: excess flux W1 1.34 mJy, W2 0.79 mJy, T = 5908 K (16-84%: 3163-8000) 

### uid1223949  [D2]  YOUNG
- position 84.53030 -5.02174; Gaia DR3 3017393200389094912; G 14.54, BP-RP 2.03, plx 2.76 mas; plot `plots/uid1223949.png`
- **young:** SIMBAD young-star types Or*,Y*O (V* V1301 Ori)
- flags: 1.79 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.11 mag (MJD 60319)
- NEOWISE: score refetch 1.93 (stored 1.93, reproduced True); dW2 0.150, dW1 0.107, 21 visits, 227 points; baseline W1 10.48, W1-W2 0.270; onset between MJD 58536 and 58742
- detector 2: excess 0.260 mag, z 6.3, jitter ratio 7.6
- field control: target step +0.203 (W1 +0.144); neighbours N=67, median +0.001, robust sigma 0.013, max +0.033; z = 16.0
- centroid: jump at onset 0.014" +- 0.014 (1.0 sigma, PA 207); largest consecutive-visit jump 0.041"; rms 0.022"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.313, W2-W3 2.328 (W3 S/N 46.9), W3-W4 2.245 (W4 S/N 26.1), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.15, ipd_frac_multi_peak 0, NSS none, Teff 6341 K, logg 4.21, H-alpha pEW -3.668 nm, varclass none; M_G 6.74, -1.79 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): V* V1301 Ori [Or*; *,Em*,Er*,MIR,NIR,Or*,V*,Y*O] 0.03" refs=17
- ASAS-SN: 2527 points, cameras bA(g,148); bB(g,96, d=+0.171); bE(g,212, d=-0.085); bF(g,188, d=+0.016); ba(V,179); bb(V,129); be(V,194); bf(V,144); bi(g,334, d=+0.000); bj(g,252, d=-0.128); bm(g,222, d=+0.001); bn(g,110); bq(g,163, d=-0.125); br(g,156, d=+0.044); change at onset (after-before, per-camera median) +0.000 mag; largest seasonal dimming 0.11 mag at MJD 60319
- dust: excess flux W1 3.67 mJy, W2 3.48 mJy, T = 1405 K (16-84%: 1296-1534) 

### uid878866  [D2]  YOUNG
- position 88.42049 +1.63723; Gaia DR3 3315801583867579392; G 13.11, BP-RP 1.77, plx 2.99 mas; plot `plots/uid878866.png`
- **young:** SIMBAD young-star types Or*,TT*,Y*O (EM* LkHA  334) | Gaia DR3 variability class YSO(0.69)
- flags: 2.33 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.25 mag (MJD 59133)
- NEOWISE: score refetch 3.76 (stored 3.76, reproduced True); dW2 0.224, dW1 0.240, 21 visits, 211 points; baseline W1 8.27, W1-W2 0.562; onset between MJD 57287 and 57452
- detector 2: excess 0.593 mag, z 18.3, jitter ratio 5.2
- field control: target step +0.187 (W1 +0.144); neighbours N=96, median -0.002, robust sigma 0.012, max +0.123; z = 15.9
- centroid: jump at onset 0.008" +- 0.018 (0.4 sigma, PA 294); largest consecutive-visit jump 0.045"; rms 0.039"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.619, W2-W3 1.849 (W3 S/N 77.1), W3-W4 1.734 (W4 S/N 44.2), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.35, ipd_frac_multi_peak 0, NSS none, Teff 5744 K, logg 3.91, H-alpha pEW -0.695 nm, varclass YSO(0.69); M_G 5.49, -2.33 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): EM* LkHA  334 [TT*; *,Em*,IR,NIR,Or*,TT*,V*,Y*O,ev] 0.08" refs=24
- ASAS-SN: 890 points, cameras bA(g,91); bB(g,91); bE(g,69); bF(g,54); bi(g,125); bj(g,118); bm(g,80); bn(g,74); bq(g,104); br(g,84); change at onset (after-before, per-camera median) n/a mag; largest seasonal dimming 0.25 mag at MJD 59133
- dust: excess flux W1 23.86 mJy, W2 20.40 mJy, T = 1646 K (16-84%: 1476-1866) 
- checks missing: ASAS-SN change at onset (no camera spans the onset)

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
- detector 2: excess 0.604 mag, z 18.6, jitter ratio 7.5
- field control: target step +0.214 (W1 +0.192); neighbours N=182, median +0.003, robust sigma 0.014, max +0.071; z = 15.0
- centroid: jump at onset 0.007" +- 0.022 (0.3 sigma, PA 326); largest consecutive-visit jump 0.078"; rms 0.031"; toward neighbour: none; expected shift if a neighbour were the source: 2.8" G18.1: 0.50"
- AllWISE 2010: W1-W2 0.546, W2-W3 1.183 (W3 S/N 64.3), W3-W4 2.061 (W4 S/N 34.3), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.03, ipd_frac_multi_peak 0, NSS none, Teff 5052 K, logg 4.27, H-alpha pEW -0.759 nm, varclass YSO(0.50); M_G 6.55, -1.27 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 2.8" PA183 G18.07 dG+3.65
- SIMBAD (10"): 2MASS J08082235-4710594 [Or*; *,NIR,Or*,Y*?,Y*O] 0.17" refs=17
- ASAS-SN: 2405 points, cameras bE(g,391, d=-0.080); bF(g,371, d=+0.064); be(V,221); bf(V,187); bi(g,500, d=+0.074); bj(g,395, d=+0.115); bm(g,162, d=-0.188); bn(g,178, d=-0.162); change at onset (after-before, per-camera median) -0.008 mag; largest seasonal dimming 0.17 mag at MJD 58084
- dust: excess flux W1 9.50 mJy, W2 8.26 mJy, T = 1600 K (16-84%: 1445-1787) 

### uid1385941  [D2]  YOUNG
- position 315.52057 +76.95517; Gaia DR3 2278495754146297472; G 13.54, BP-RP 1.94, plx 2.67 mas; plot `plots/uid1385941.png`
- **young:** SIMBAD young-star types Or*,Y*?,Y*O (GSC 04590-00831) | Gaia DR3 variability class YSO(0.54)
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | 2.61 mag above the main sequence at its colour | not plain dust: optical brightening -0.058 mag (per-camera -0.101,-0.056,-0.047,-0.060) together with the infrared rise | largest seasonal optical dimming 0.13 mag (MJD 60035)
- NEOWISE: score refetch 0.16 (stored 0.16, reproduced True); dW2 0.026, dW1 0.047, 21 visits, 549 points; baseline W1 9.52, W1-W2 0.247; onset between MJD 60176 and 60335
- detector 2: excess 0.251 mag, z 6.4, jitter ratio 10.0
- field control: target step +0.143 (W1 +0.153); neighbours N=91, median +0.000, robust sigma 0.010, max +0.943; z = 14.8
- centroid: jump at onset 0.035" +- 0.017 (2.1 sigma, PA 70); largest consecutive-visit jump 0.041"; rms 0.019"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 -0.015, W2-W3 2.608 (W3 S/N 70.8), W3-W4 2.731 (W4 S/N 58.2), ext_flg 1, ph_qual ZAAA: W3 excess only (W2-W3 > 1.0; debris-disk-like or blend)
- Gaia: RUWE 1.01, ipd_frac_multi_peak 0, NSS none, Teff 5089 K, logg 4.09, H-alpha pEW -0.538 nm, varclass YSO(0.54); M_G 5.67, -2.61 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): GSC 04590-00831 [Or*; *,Em*,IR,NIR,Or*,Y*?,Y*O] 0.11" refs=18
- ASAS-SN: 1934 points, cameras bC(g,449, d=-0.101); bD(g,362, d=-0.056); ba(V,41); bc(V,288); bd(V,255); bs(g,283, d=-0.047); bt(g,256, d=-0.060); change at onset (after-before, per-camera median) -0.058 mag; largest seasonal dimming 0.13 mag at MJD 60035
- dust: excess flux W1 14.63 mJy, W2 10.26 mJy, T = 2579 K (16-84%: 2338-2883) 

### uid984249  [D2]  YOUNG
- position 81.04666 +3.58933; Gaia DR3 3236174230229658240; G 13.83, BP-RP 1.67, plx 2.91 mas; plot `plots/uid984249.png`
- **young:** SIMBAD young-star types TT*,Y*O (CVSO 662)
- flags: centroid jump 0.042" (3.1 sigma, PA 280) not toward a Gaia neighbour | 1.40 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.32 mag (MJD 58709)
- NEOWISE: score refetch 1.83 (stored 1.83, reproduced True); dW2 0.223, dW1 0.287, 20 visits, 220 points; baseline W1 10.14, W1-W2 0.312; onset between MJD 57085 and 57280
- detector 2: excess 0.358 mag, z 12.9, jitter ratio 11.5
- field control: target step +0.165 (W1 +0.187); neighbours N=57, median -0.005, robust sigma 0.012, max +0.019; z = 14.3
- centroid: jump at onset 0.042" +- 0.013 (3.1 sigma, PA 280); largest consecutive-visit jump 0.028"; rms 0.023"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.276, W2-W3 1.841 (W3 S/N 52.7), W3-W4 2.161 (W4 S/N 27.9), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.18, ipd_frac_multi_peak 1, NSS none, Teff 4449 K, logg 4.13, H-alpha pEW -0.092 nm, varclass none; M_G 6.15, -1.40 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): CVSO 662 [TT*; *,MIR,NIR,TT*,Y*O] 0.02" refs=19
- ASAS-SN: 1238 points, cameras bA(g,167); bE(g,179); ba(V,210, d=+0.007); be(V,56); bi(g,286); bm(g,209); bq(g,131); change at onset (after-before, per-camera median) +0.007 mag; largest seasonal dimming 0.32 mag at MJD 58709
- dust: excess flux W1 5.55 mJy, W2 4.55 mJy, T = 1772 K (16-84%: 1550-2079) 

### uid1432270  [D2]  YOUNG
- position 83.03243 -6.92692; Gaia DR3 3016721536212199168; G 14.81, BP-RP 1.89, plx 2.64 mas; plot `plots/uid1432270.png`
- **young:** SIMBAD young-star types Or*,Y*?,Y*O (V* V540 Ori)
- flags: 1.22 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.18 mag (MJD 56618)
- NEOWISE: score refetch 1.43 (stored 1.44, reproduced True); dW2 0.252, dW1 0.252, 21 visits, 214 points; baseline W1 10.41, W1-W2 0.350; onset between MJD 58376 and 58534
- detector 2: excess 0.361 mag, z 9.7, jitter ratio 13.0
- field control: target step +0.191 (W1 +0.190); neighbours N=63, median +0.002, robust sigma 0.013, max +0.030; z = 14.2
- centroid: jump at onset 0.012" +- 0.017 (0.7 sigma, PA 139); largest consecutive-visit jump 0.049"; rms 0.025"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.407, W2-W3 1.173 (W3 S/N 41.5), W3-W4 2.036 (W4 S/N 13.2), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.07, ipd_frac_multi_peak 0, NSS none, Teff 6111 K, logg 4.43, H-alpha pEW -2.117 nm, varclass none; M_G 6.92, -1.22 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): V* V540 Ori [Or*; *,Em*,NIR,Opt,Or*,V*,Y*?,Y*O] 0.01" refs=22
- ASAS-SN: 1484 points, cameras bA(g,154); bE(g,215, d=+0.016); ba(V,179); be(V,194); bi(g,340, d=+0.026); bm(g,239, d=+0.091); bq(g,163, d=-0.162); change at onset (after-before, per-camera median) +0.021 mag; largest seasonal dimming 0.18 mag at MJD 56618
- dust: excess flux W1 6.09 mJy, W2 4.81 mJy, T = 1913 K (16-84%: 1756-2100) 

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
- detector 2: excess 0.469 mag, z 10.9, jitter ratio 11.1
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
- detector 2: excess 0.456 mag, z 14.5, jitter ratio 15.8
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
- detector 2: excess 0.483 mag, z 15.5, jitter ratio 13.0
- field control: target step +0.199 (W1 +0.234); neighbours N=84, median +0.007, robust sigma 0.014, max +0.053; z = 13.3
- centroid: jump at onset 0.147" +- 0.224 (0.7 sigma, PA 176); largest consecutive-visit jump 0.137"; rms 0.101"; toward neighbour: none; expected shift if a neighbour were the source: 1.8" G17.8: 0.31"; 2.5" G18.6: 0.41"
- AllWISE 2010: W1-W2 0.412, W2-W3 1.853 (W3 S/N 68.4), W3-W4 2.190 (W4 S/N 42.0), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.12, ipd_frac_multi_peak 0, NSS none, Teff 5506 K, logg 4.16, H-alpha pEW -1.443 nm, varclass YSO(0.81); M_G 5.73, -1.97 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 1.8" PA263 G17.78 dG+4.35; 2.5" PA76 G18.60 dG+5.18
- SIMBAD (10"): 2MASS J22131219+7332585 [Or*; *,Em*,NIR,Or*,Y*?,Y*O] 0.09" refs=9
- ASAS-SN: 1361 points, cameras bA(g,325, d=-0.035); bB(g,110); ba(V,250); bb(V,163); bq(g,262, d=+0.072); br(g,251, d=+0.030); change at onset (after-before, per-camera median) +0.030 mag; largest seasonal dimming 0.16 mag at MJD 60438
- dust: excess flux W1 1.79 mJy, W2 3.35 mJy, T = 746 K (16-84%: 540-1035) 

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
- detector 2: excess 0.462 mag, z 19.1, jitter ratio 7.9
- field control: target step +0.108 (W1 +0.044); neighbours N=39, median -0.007, robust sigma 0.009, max +0.019; z = 12.8
- centroid: jump at onset 0.014" +- 0.024 (0.6 sigma, PA 277); largest consecutive-visit jump 0.038"; rms 0.021"; toward neighbour: none; expected shift if a neighbour were the source: 9.8" G17.3: 0.92"
- AllWISE 2010: W1-W2 0.466, W2-W3 1.548 (W3 S/N 53.6), W3-W4 1.448 (W4 S/N 17.6), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.33, ipd_frac_multi_peak 0, NSS none, Teff 4818 K, logg 4.20, H-alpha pEW -0.671 nm, varclass YSO(0.14); M_G 5.91, -1.43 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 9.8" PA206 G17.35 dG+3.62
- SIMBAD (10"): UCAC4 414-008437 [Y*O; *,MIR,NIR,Y*O] 0.02" refs=3
- ASAS-SN: 1293 points, cameras bB(g,84); bF(g,207); bb(V,154, d=+0.165); bf(V,171, d=-0.149); bj(g,277); bn(g,237); br(g,163); change at onset (after-before, per-camera median) +0.008 mag; largest seasonal dimming 0.20 mag at MJD 59828
- dust: excess flux W1 2.11 mJy, W2 1.32 mJy, T = 4011 K (16-84%: 1588-8000) 

### uid893973  [D2]  YOUNG
- position 108.92033 -48.52421; Gaia DR3 5505636461266794112; G 14.39, BP-RP 2.15, plx 2.97 mas; plot `plots/uid893973.png`
- **young:** SIMBAD young-star types Or*,Y*? (2MASS J07154087-4831274)
- flags: 2.16 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.16 mag (MJD 58774)
- NEOWISE: score refetch 1.92 (stored 1.92, reproduced True); dW2 0.258, dW1 0.202, 20 visits, 311 points; baseline W1 10.58, W1-W2 0.315; onset between MJD 58789 and 58945
- detector 2: excess 0.286 mag, z 6.7, jitter ratio 9.7
- field control: target step +0.094 (W1 +0.103); neighbours N=60, median -0.000, robust sigma 0.007, max +0.019; z = 12.7
- centroid: jump at onset 0.021" +- 0.016 (1.3 sigma, PA 230); largest consecutive-visit jump 0.050"; rms 0.032"; toward neighbour: 7.8" PA215 G19.2 (angle 15 deg); expected shift if a neighbour were the source: 7.8" G19.2: 0.65"
- AllWISE 2010: W1-W2 0.349, W2-W3 1.920 (W3 S/N 57.2), W3-W4 2.537 (W4 S/N 33.6), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.10, ipd_frac_multi_peak 0, NSS none, Teff 3964 K, logg 4.04, H-alpha pEW -1.656 nm, varclass none; M_G 6.76, -2.16 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 7.8" PA215 G19.19 dG+4.80
- SIMBAD (10"): 2MASS J07154087-4831274 [Or*; *,Em*,NIR,Or*,Y*?] 0.21" refs=5
- ASAS-SN: 1557 points, cameras bH(g,378, d=-0.022); bf(V,108); bh(V,216); bl(g,552, d=-0.023); bp(g,303, d=+0.031); change at onset (after-before, per-camera median) -0.022 mag; largest seasonal dimming 0.16 mag at MJD 58774
- dust: excess flux W1 2.08 mJy, W2 1.53 mJy, T = 2279 K (16-84%: 1855-3004) 

### uid1108316  [D2]  YOUNG
- position 84.21799 -1.35686; Gaia DR3 3217396701931361792; G 13.60, BP-RP 1.61, plx 2.83 mas; plot `plots/uid1108316.png`
- **young:** SIMBAD young-star types Y*?,Y*O (CRTS J053652.2-012124)
- flags: 1.54 mag above the main sequence at its colour
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 14 visits, 119 points; baseline W1 10.56, W1-W2 0.237; onset between MJD 56921 and 57088
- detector 2: excess 0.288 mag, z 11.6, jitter ratio 11.6
- field control: target step +0.135 (W1 +0.045); neighbours N=88, median -0.003, robust sigma 0.011, max +0.035; z = 11.9
- centroid: jump at onset 0.036" +- 0.029 (1.2 sigma, PA 196); largest consecutive-visit jump 0.080"; rms 0.042"; toward neighbour: 7.4" PA169 G18.3 (angle 26 deg); expected shift if a neighbour were the source: 7.4" G18.3: 0.86"
- AllWISE 2010: W1-W2 0.205, W2-W3 1.372 (W3 S/N 31.8), W3-W4 2.085 (W4 S/N 10.3), ext_flg 0, ph_qual AAAA: W3 excess only (W2-W3 > 1.0; debris-disk-like or blend)
- Gaia: RUWE 0.98, ipd_frac_multi_peak 0, NSS none, Teff 4581 K, logg 4.14, H-alpha pEW -0.164 nm, varclass RS(0.55); M_G 5.86, -1.54 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 7.4" PA169 G18.27 dG+4.67
- SIMBAD (10"): CRTS J053652.2-012124 [RS*; *,NIR,RS*,Y*?,Y*O] 0.03" refs=14; 2E 0534.3-0123 [X; X] 3.91" refs=0
- ASAS-SN: 1371 points, cameras bC(g,158); bG(g,221); ba(V,51); bc(V,151, d=+0.016); be(V,38, d=-0.010); bg(V,153); bk(g,287); bo(g,165); bs(g,147); change at onset (after-before, per-camera median) +0.003 mag; largest seasonal dimming 0.05 mag at MJD 57629
- dust: excess flux W1 0.52 mJy, W2 1.47 mJy, T = 589 K (16-84%: 522-663) 

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
- detector 2: excess 0.425 mag, z 12.6, jitter ratio 14.0
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
- detector 2: excess 0.597 mag, z 14.4, jitter ratio 8.0
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
- detector 2: excess 0.418 mag, z 17.4, jitter ratio 5.8
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

### uid1192683  [D2]  YOUNG
- position 94.43232 -1.85737; Gaia DR3 3118092797442942976; G 15.50, BP-RP 1.98, plx 2.78 mas; plot `plots/uid1192683.png`
- **young:** SIMBAD young-star types Y*? (2MASS J06174375-0151264)
- flags: AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.76 mag (MJD 60288)
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 20 visits, 189 points; baseline W1 10.79, W1-W2 0.580; onset between MJD 56931 and 57098
- detector 2: excess 0.578 mag, z 13.9, jitter ratio 11.0
- field control: target step +0.116 (W1 +0.094); neighbours N=143, median -0.003, robust sigma 0.012, max +0.036; z = 10.0
- centroid: jump at onset 0.019" +- 0.027 (0.7 sigma, PA 200); largest consecutive-visit jump 0.054"; rms 0.034"; toward neighbour: none; expected shift if a neighbour were the source: 7.2" G19.1: 0.73"; 7.5" G18.5: 0.76"
- AllWISE 2010: W1-W2 0.577, W2-W3 1.969 (W3 S/N 49.1), W3-W4 2.231 (W4 S/N 21.8), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.25, ipd_frac_multi_peak 0, NSS none, Teff 3518 K, logg 4.08, H-alpha pEW -5.812 nm, varclass none; M_G 7.72, -0.67 mag vs sequence (on the sequence); neighbours within 10": 7.2" PA123 G19.11 dG+3.60; 7.5" PA259 G18.54 dG+3.04
- SIMBAD (10"): 2MASS J06174375-0151264 [Y*?; *,NIR,Y*?] 0.08" refs=1
- ASAS-SN: 1567 points, cameras bC(g,111); bD(g,102); bG(g,120); bH(g,98); bc(V,120); bd(V,121); bg(V,122); bh(V,136); bk(g,165); bl(g,128); bo(g,77); bp(g,67); bs(g,100); bt(g,100); change at onset (after-before, per-camera median) n/a mag; largest seasonal dimming 0.76 mag at MJD 60288
- dust: excess flux W1 0.38 mJy, W2 0.51 mJy, T = 966 K (16-84%: 751-1334) 
- checks missing: ASAS-SN change at onset (no camera spans the onset)

### uid961709  [D2]  YOUNG
- position 82.54790 -6.56916; Gaia DR3 3016799154860928128; G 11.64, BP-RP 1.58, plx 2.93 mas; plot `plots/uid961709.png`
- **young:** SIMBAD young-star types Or*,Y*O (V* HH Ori)
- flags: 3.33 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | optical dimming +0.151 mag after the infrared onset (debris transit signature) | largest seasonal optical dimming 1.04 mag (MJD 57804)
- NEOWISE: score refetch 1.22 (stored 1.22, reproduced True); dW2 0.170, dW1 0.185, 18 visits, 187 points; baseline W1 8.49, W1-W2 0.763; onset between MJD 57280 and 57445
- detector 2: excess 0.818 mag, z 34.3, jitter ratio 5.8
- field control: target step +0.122 (W1 +0.154); neighbours N=72, median -0.004, robust sigma 0.014, max +0.067; z = 9.2
- centroid: jump at onset 0.027" +- 0.019 (1.4 sigma, PA 232); largest consecutive-visit jump 0.053"; rms 0.034"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.789, W2-W3 2.984 (W3 S/N 74.3), W3-W4 1.623 (W4 S/N 59.6), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.34, ipd_frac_multi_peak 1, NSS none, Teff 4792 K, logg 3.64, H-alpha pEW 0.220 nm, varclass none; M_G 3.97, -3.33 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): V* HH Ori [Or*; *,IR,NIR,Or*,V*,Y*O] 0.01" refs=13
- ASAS-SN: 1521 points, cameras bA(g,159); bE(g,220); ba(V,180, d=+0.233); be(V,195, d=+0.068); bi(g,343); bm(g,251); bq(g,173); change at onset (after-before, per-camera median) +0.151 mag; largest seasonal dimming 1.04 mag at MJD 57804
- dust: excess flux W1 15.24 mJy, W2 13.60 mJy, T = 1534 K (16-84%: 1342-1809) 

### uid1387731  [D2]  YOUNG
- position 84.06150 -6.22136; Gaia DR3 3017166082507174272; G 15.04, BP-RP 2.09, plx 2.67 mas; plot `plots/uid1387731.png`
- **young:** SIMBAD young-star types Or*,TT*,Y*O (V* V2653 Ori)
- flags: binary type in SIMBAD (SB*, V* V2653 Ori) | 1.56 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | not plain dust: optical brightening -0.096 mag (per-camera -0.077,-0.116) together with the infrared rise | largest seasonal optical dimming 0.16 mag (MJD 59687)
- NEOWISE: score refetch 1.83 (stored 1.83, reproduced True); dW2 0.240, dW1 0.200, 19 visits, 177 points; baseline W1 11.17, W1-W2 0.421; onset between MJD 57088 and 57282
- detector 2: excess 0.401 mag, z 9.3, jitter ratio 12.3
- field control: target step +0.204 (W1 +0.158); neighbours N=113, median -0.002, robust sigma 0.023, max +0.320; z = 8.9
- centroid: jump at onset 0.023" +- 0.012 (1.9 sigma, PA 93); largest consecutive-visit jump 0.045"; rms 0.021"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.425, W2-W3 1.801 (W3 S/N 29.3), W3-W4 1.861 (W4 S/N 12.0), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.10, ipd_frac_multi_peak 0, NSS none, Teff 3608 K, logg 4.00, H-alpha pEW -1.298 nm, varclass none; M_G 7.17, -1.56 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): V* V2653 Ori [TT*; *,Em*,MIR,NIR,Opt,Or*,SB*,TT*,V*,X,Y*O] 0.03" refs=42
- ASAS-SN: 1303 points, cameras bA(g,140); bE(g,204); ba(V,165, d=-0.077); be(V,192, d=-0.116); bi(g,279); bm(g,175); bq(g,148); change at onset (after-before, per-camera median) -0.096 mag; largest seasonal dimming 0.16 mag at MJD 59687
- dust: excess flux W1 1.01 mJy, W2 1.65 mJy, T = 817 K (16-84%: 769-869) 

### uid1394555  [D2]  YOUNG
- position 81.41583 -4.18394; Gaia DR3 3210586361269300992; G 14.79, BP-RP 1.61, plx 2.66 mas; plot `plots/uid1394555.png`
- **young:** SIMBAD young-star types Or*,TT*,Y*?,Y*O (Kiso A-0975  86) | Gaia DR3 variability class YSO(0.26)
- flags: AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.50 mag (MJD 57116)
- NEOWISE: score refetch 0.74 (stored 0.74, reproduced True); dW2 0.143, dW1 0.193, 15 visits, 204 points; baseline W1 10.88, W1-W2 0.558; onset between MJD 57809 and 58011
- detector 2: excess 0.609 mag, z 24.5, jitter ratio 15.6
- field control: target step +0.124 (W1 +0.145); neighbours N=58, median -0.003, robust sigma 0.014, max +0.042; z = 8.8
- centroid: jump at onset 0.009" +- 0.022 (0.4 sigma, PA 144); largest consecutive-visit jump 0.102"; rms 0.032"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.472, W2-W3 2.516 (W3 S/N 51.3), W3-W4 1.808 (W4 S/N 21.1), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.35, ipd_frac_multi_peak 0, NSS none, Teff 5889 K, logg 4.52, H-alpha pEW -3.032 nm, varclass YSO(0.26); M_G 6.92, -0.48 mag vs sequence (on the sequence); neighbours within 10": none
- SIMBAD (10"): Kiso A-0975  86 [TT*; *,Em*,MIR,NIR,Opt,Or*,TT*,Y*?,Y*O] 0.03" refs=9
- ASAS-SN: 1803 points, cameras bA(g,155); bE(g,218); bH(g,195); ba(V,147, d=+0.169); be(V,191, d=-0.099); bf(V,37); bh(V,147, d=+0.155); bi(g,320); bm(g,231); bq(g,162); change at onset (after-before, per-camera median) +0.155 mag; largest seasonal dimming 0.50 mag at MJD 57116
- dust: excess flux W1 3.68 mJy, W2 3.04 mJy, T = 1748 K (16-84%: 1546-2020) 

### uid847196  [D2]  YOUNG
- position 84.14645 -1.03803; Gaia DR3 3217605093744826880; G 15.05, BP-RP 2.19, plx 3.01 mas; plot `plots/uid847196.png`
- **young:** SIMBAD young-star types Or*,Y*?,Y*O (Haro 5-74)
- flags: 1.60 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | not plain dust: optical brightening -0.168 mag (per-camera -0.255,-0.081) together with the infrared rise | largest seasonal optical dimming 0.24 mag (MJD 56645)
- NEOWISE: score refetch 1.04 (stored 1.04, reproduced True); dW2 0.110, dW1 0.000, 20 visits, 171 points; baseline W1 10.27, W1-W2 0.379; onset between MJD 57088 and 57283
- detector 2: excess 0.347 mag, z 8.1, jitter ratio 10.6
- field control: target step +0.093 (W1 +0.091); neighbours N=76, median -0.005, robust sigma 0.012, max +0.137; z = 8.2
- centroid: jump at onset 0.025" +- 0.016 (1.6 sigma, PA 115); largest consecutive-visit jump 0.043"; rms 0.031"; toward neighbour: 7.8" PA160 G20.4 (angle 45 deg); expected shift if a neighbour were the source: 7.8" G20.4: 0.64"; 8.7" G19.2: 0.72"
- AllWISE 2010: W1-W2 0.479, W2-W3 1.704 (W3 S/N 46.5), W3-W4 1.655 (W4 S/N 17.2), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.04, ipd_frac_multi_peak 0, NSS none, Teff 3504 K, logg 4.03, H-alpha pEW -1.097 nm, varclass none; M_G 7.44, -1.60 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 7.8" PA160 G20.45 dG+5.39; 8.7" PA284 G19.21 dG+4.16
- SIMBAD (10"): Haro 5-74 [Or*; *,Em*,NIR,Or*,V*,Y*?,Y*O] 0.04" refs=17
- ASAS-SN: 1201 points, cameras bC(g,149); bG(g,216); ba(V,51); bc(V,149, d=-0.255); be(V,38, d=-0.081); bg(V,153); bk(g,169); bo(g,161); bs(g,115); change at onset (after-before, per-camera median) -0.168 mag; largest seasonal dimming 0.24 mag at MJD 56645
- dust: excess flux W1 2.34 mJy, W2 1.69 mJy, T = 2354 K (16-84%: 1828-3426) 

### uid1424151  [D2]  YOUNG
- position 85.02105 -6.49019; Gaia DR3 3016991122718336128; G 14.81, BP-RP 1.93, plx 2.65 mas; plot `plots/uid1424151.png`
- **young:** SIMBAD young-star types Or*,Y*?,Y*O (V* V1188 Ori)
- flags: 1.33 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.56 mag (MJD 60680)
- NEOWISE: score refetch 1.00 (stored 1.00, reproduced True); dW2 0.205, dW1 0.202, 21 visits, 241 points; baseline W1 10.11, W1-W2 0.586; onset between MJD 58536 and 58743
- detector 2: excess 0.591 mag, z 15.2, jitter ratio 12.0
- field control: target step +0.119 (W1 +0.059); neighbours N=65, median +0.000, robust sigma 0.016, max +0.117; z = 7.6
- centroid: jump at onset 0.007" +- 0.020 (0.4 sigma, PA 360); largest consecutive-visit jump 0.067"; rms 0.026"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.613, W2-W3 2.168 (W3 S/N 56.2), W3-W4 1.952 (W4 S/N 25.6), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.11, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW -1.105 nm, varclass none; M_G 6.93, -1.33 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): V* V1188 Ori [Or*; *,Em*,MIR,NIR,Or*,V*,Y*?,Y*O] 0.05" refs=23
- ASAS-SN: 1073 points, cameras bB(g,91, d=+0.454); bF(g,179, d=-0.175); ba(V,30); bb(V,129); bf(V,141); bj(g,245, d=+0.197); bn(g,108); br(g,150, d=+0.032); change at onset (after-before, per-camera median) +0.114 mag; largest seasonal dimming 0.56 mag at MJD 60680
- dust: excess flux W1 6.46 mJy, W2 5.10 mJy, T = 1913 K (16-84%: 1720-2162) 

### uid1262405  [D2]  YOUNG
- position 84.55883 -2.26661; Gaia DR3 3216511182753680512; G 10.31, BP-RP 0.73, plx 2.74 mas; plot `plots/uid1262405.png`
- **young:** SIMBAD young-star types Y*O (HD 294268)
- flags: centroid jump 0.050" (5.1 sigma, PA 69) not toward a Gaia neighbour | 1.57 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | optical dimming +0.064 mag after the infrared onset (debris transit signature) | largest seasonal optical dimming 0.44 mag (MJD 56542)
- NEOWISE: score refetch 0.51 (stored 0.51, reproduced True); dW2 0.083, dW1 0.058, 21 visits, 209 points; baseline W1 8.56, W1-W2 0.315; onset between MJD 57089 and 57283
- detector 2: excess 0.348 mag, z 34.8, jitter ratio 12.5
- field control: target step +0.111 (W1 +0.118); neighbours N=98, median -0.003, robust sigma 0.015, max +0.295; z = 7.5
- centroid: jump at onset 0.050" +- 0.010 (5.1 sigma, PA 69); largest consecutive-visit jump 0.097"; rms 0.024"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.291, W2-W3 4.195 (W3 S/N 73.2), W3-W4 2.794 (W4 S/N 68.0), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 0.83, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW -0.007 nm, varclass none; M_G 2.50, -1.57 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): HD 294268 [Y*O; *,IR,NIR,X,Y*O] 0.04" refs=48
- ASAS-SN: 1466 points, cameras bC(g,150); bG(g,223); ba(V,51); bc(V,148, d=+0.076); be(V,38, d=+0.052); bg(V,153); bk(g,311); bo(g,230); bs(g,162); change at onset (after-before, per-camera median) +0.064 mag; largest seasonal dimming 0.44 mag at MJD 56542
- dust: excess flux W1 16.51 mJy, W2 14.92 mJy, T = 1505 K (16-84%: 1370-1669) 

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

### uid1252374  [D2]  YOUNG
- position 121.98109 -47.12941; Gaia DR3 5519263533510676224; G 13.10, BP-RP 1.37, plx 2.74 mas; plot `plots/uid1252374.png`
- **young:** SIMBAD young-star types Or*,Y*?,Y*O (2MASS J08075546-4707460) | Gaia DR3 variability class YSO(0.20)
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | 1.47 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 0.37 (stored 0.37, reproduced True); dW2 0.077, dW1 0.078, 14 visits, 167 points; baseline W1 9.90, W1-W2 0.335; onset between MJD 57152 and 57346
- detector 2: excess 0.398 mag, z 20.8, jitter ratio 16.9
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
- detector 2: excess 0.462 mag, z 14.2, jitter ratio 13.5
- field control: target step +0.052 (W1 +0.109); neighbours N=82, median -0.003, robust sigma 0.010, max +0.028; z = 5.5
- centroid: jump at onset 0.009" +- 0.015 (0.6 sigma, PA 18); largest consecutive-visit jump 0.044"; rms 0.025"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.371, W2-W3 1.929 (W3 S/N 58.5), W3-W4 2.228 (W4 S/N 28.8), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.18, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW -2.268 nm, varclass YSO(0.52); M_G 6.53, -1.30 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): Kiso A-0903 195 [TT*; *,Em*,MIR,NIR,TT*,TT?,V*,Y*?,Y*O] 0.03" refs=21
- ASAS-SN: 1232 points, cameras bA(g,168); bE(g,175); ba(V,210, d=-0.061); be(V,56); bi(g,279); bm(g,213); bq(g,131); change at onset (after-before, per-camera median) -0.061 mag; largest seasonal dimming 0.25 mag at MJD 60603
- dust: excess flux W1 6.09 mJy, W2 2.72 mJy, T = 8000 K (16-84%: 8000-8000) ratio bluer than an 8000 K blackbody (not dust-like)

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

### uid1281030  [D2]  YOUNG
- position 70.57174 +37.66241; Gaia DR3 175539303414648448; G 13.52, BP-RP 1.77, plx 2.73 mas; plot `plots/uid1281030.png`
- **young:** SIMBAD young-star types Y*? (UCAC4 639-018918) | Gaia DR3 variability class YSO(0.43)
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | 2.13 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | optical dimming +0.063 mag after the infrared onset (debris transit signature) | largest seasonal optical dimming 0.19 mag (MJD 60556)
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 18 visits, 161 points; baseline W1 9.42, W1-W2 0.363; onset between MJD 57439 and 57638
- detector 2: excess 0.393 mag, z 12.1, jitter ratio 29.2
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
- detector 2: excess 0.527 mag, z 18.4, jitter ratio 9.8
- field control: target step +0.063 (W1 +0.088); neighbours N=127, median -0.003, robust sigma 0.019, max +0.177; z = 3.4
- centroid: jump at onset 0.010" +- 0.019 (0.5 sigma, PA 259); largest consecutive-visit jump 0.115"; rms 0.033"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.491, W2-W3 1.812 (W3 S/N 42.9), W3-W4 1.881 (W4 S/N 23.1), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.15, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW -2.942 nm, varclass YSO(0.35); M_G 6.86, -0.73 mag vs sequence (on the sequence); neighbours within 10": none
- SIMBAD (10"): V* XX Ori [TT*; *,Em*,Er*,MIR,NIR,Opt,Or*,TT*,V*,X,Y*O,ev] 0.03" refs=59
- ASAS-SN: 1452 points, cameras bA(g,146); bE(g,212); ba(V,179, d=+0.107); be(V,195, d=+0.098); bi(g,337); bm(g,220); bq(g,163); change at onset (after-before, per-camera median) +0.102 mag; largest seasonal dimming 0.25 mag at MJD 57974
- dust: excess flux W1 2.80 mJy, W2 1.81 mJy, T = 3441 K (16-84%: 2193-8000) 

### uid900210  [D2]  YOUNG
- position 83.94168 -0.96451; Gaia DR3 3217657011309526016; G 13.45, BP-RP 1.73, plx 2.97 mas; plot `plots/uid900210.png`
- **young:** SIMBAD young-star types Or*,TT*,Y*?,Y*O (Haro 5-73) | Gaia DR3 variability class YSO(0.55)
- flags: 1.91 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.21 mag (MJD 60524)
- NEOWISE: score refetch 3.91 (stored 3.91, reproduced True); dW2 0.198, dW1 0.170, 20 visits, 214 points; baseline W1 9.40, W1-W2 0.328; onset between MJD 58742 and 58900
- detector 2: excess 0.364 mag, z 11.6, jitter ratio 4.3
- field control: target step +0.044 (W1 +0.054); neighbours N=76, median +0.003, robust sigma 0.014, max +0.071; z = 2.9
- centroid: jump at onset 0.016" +- 0.013 (1.2 sigma, PA 7); largest consecutive-visit jump 0.028"; rms 0.022"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.302, W2-W3 1.963 (W3 S/N 52.7), W3-W4 2.475 (W4 S/N 28.0), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.05, ipd_frac_multi_peak 0, NSS none, Teff 5580 K, logg 4.16, H-alpha pEW -1.346 nm, varclass YSO(0.55); M_G 5.81, -1.91 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): Haro 5-73 [TT*; *,Em*,NIR,Or*,TT*,V*,Y*?,Y*O,ev] 0.03" refs=42
- ASAS-SN: 1435 points, cameras bC(g,150, d=+0.038); bG(g,222, d=+0.131); ba(V,51); bc(V,150); be(V,38); bg(V,153); bk(g,305, d=-0.123); bo(g,211, d=+0.010); bs(g,155, d=-0.173); change at onset (after-before, per-camera median) +0.010 mag; largest seasonal dimming 0.21 mag at MJD 60524
- dust: excess flux W1 3.95 mJy, W2 2.42 mJy, T = 4625 K (16-84%: 2422-8000) 

### uid1356608  [D2]  YOUNG
- position 56.42745 +34.77553; Gaia DR3 218336625295850624; G 13.84, BP-RP 1.65, plx 2.68 mas; plot `plots/uid1356608.png`
- **young:** Gaia DR3 variability class YSO(0.20)
- flags: 1.52 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 1.09 (stored 1.09, reproduced True); dW2 0.144, dW1 0.102, 21 visits, 218 points; baseline W1 9.18, W1-W2 0.400; onset between MJD 57425 and 57626
- detector 2: excess 0.447 mag, z 16.7, jitter ratio 11.6
- field control: target step +0.006 (W1 +0.016); neighbours N=89, median -0.003, robust sigma 0.011, max +0.029; z = 0.9
- centroid: jump at onset 0.014" +- 0.012 (1.2 sigma, PA 274); largest consecutive-visit jump 0.061"; rms 0.027"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.469, W2-W3 1.139 (W3 S/N 58.1), W3-W4 1.729 (W4 S/N 18.3), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.34, ipd_frac_multi_peak 1, NSS none, Teff nan K, logg nan, H-alpha pEW -3.526 nm, varclass YSO(0.20); M_G 5.98, -1.52 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): 2MASS J03454257+3446320 [Em*; *,Em*,MIR,NIR,Opt,V*,ev] 0.09" refs=13
- ASAS-SN: 0 points, cameras n/a; change at onset (after-before, per-camera median) n/a mag; largest seasonal dimming n/a mag at MJD n/a
- dust: excess flux W1 6.32 mJy, W2 6.55 mJy, T = 1248 K (16-84%: 1112-1423) 
- checks missing: ASAS-SN (no source)

### uid1295756  [D2]  YOUNG
- position 83.06180 -6.34851; Gaia DR3 3016826814450125184; G 14.98, BP-RP 2.08, plx 2.72 mas; plot `plots/uid1295756.png`
- **young:** SIMBAD young-star types Or*,Y*?,Y*O (V* V1164 Ori)
- flags: binary type in SIMBAD (SB*, V* V1164 Ori) | 1.56 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.15 mag (MJD 58872)
- NEOWISE: score refetch 0.05 (stored 0.05, reproduced True); dW2 0.004, dW1 -0.060, 21 visits, 208 points; baseline W1 11.02, W1-W2 0.335; onset between MJD 59108 and 59263
- detector 2: excess 0.316 mag, z 7.3, jitter ratio 7.7
- field control: target step -0.017 (W1 +0.000); neighbours N=74, median -0.000, robust sigma 0.013, max +0.035; z = -1.3
- centroid: jump at onset 0.011" +- 0.016 (0.7 sigma, PA 237); largest consecutive-visit jump 0.052"; rms 0.030"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.353, W2-W3 2.402 (W3 S/N 49.5), W3-W4 2.028 (W4 S/N 14.8), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.19, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW -1.735 nm, varclass none; M_G 7.15, -1.56 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): V* V1164 Ori [Or*; *,Em*,MIR,NIR,Or*,SB*,V*,Y*?,Y*O] 0.02" refs=24
- ASAS-SN: 1384 points, cameras bA(g,148, d=+0.060); bE(g,207, d=-0.034); ba(V,177); be(V,192); bi(g,308, d=-0.020); bm(g,203, d=-0.070); bq(g,149, d=-0.218); change at onset (after-before, per-camera median) -0.034 mag; largest seasonal dimming 0.15 mag at MJD 58872
- dust: excess flux W1 -0.06 mJy, W2 -0.19 mJy, T = n/a K (16-84%: n/a-n/a) no W2 excess flux after onset

### uid800756  [D2]  YOUNG
- position 133.13021 -43.18291; Gaia DR3 5523872681948712960; G 12.51, BP-RP 1.37, plx 3.05 mas; plot `plots/uid800756.png`
- **young:** SIMBAD young-star types Y*? (2MASS J08523126-4310586) | Gaia DR3 variability class YSO(0.10)
- flags: 1.83 mag above the main sequence at its colour
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 16 visits, 167 points; baseline W1 9.01, W1-W2 0.329; onset between MJD 57161 and 57355
- detector 2: excess 0.392 mag, z 20.5, jitter ratio 16.1
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

### uid712994  [D2]  YOUNG
- position 84.12785 -0.31222; Gaia DR3 3217809564250552704; G 12.33, BP-RP 1.75, plx 3.12 mas; plot `plots/uid712994.png`
- **young:** SIMBAD young-star types Or*,Y*?,Y*O (UCAC4 449-011147) | Gaia DR3 variability class YSO(0.73)
- flags: 2.96 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 0.30 (stored 0.30, reproduced True); dW2 0.019, dW1 0.027, 20 visits, 199 points; baseline W1 8.14, W1-W2 0.444; onset between MJD 57447 and 57647
- detector 2: excess 0.478 mag, z 15.0, jitter ratio 4.9
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

### uid926008  [D2]  YOUNG
- position 60.74988 +31.95108; Gaia DR3 170052259357409024; G 14.09, BP-RP 1.79, plx 2.95 mas; plot `plots/uid926008.png`
- **young:** SIMBAD young-star types Y*? (WISEA J040259.96+315703.9)
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | 1.45 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.14 mag (MJD 58507)
- NEOWISE: score refetch 1.27 (stored 1.27, reproduced True); dW2 0.260, dW1 0.249, 20 visits, 190 points; baseline W1 10.11, W1-W2 0.247; onset between MJD 57262 and 57428
- detector 2: excess 0.274 mag, z 8.1, jitter ratio 10.3
- field control: target step -0.176 (W1 -0.154); neighbours N=70, median -0.001, robust sigma 0.013, max +0.049; z = -13.5
- centroid: jump at onset 0.014" +- 0.016 (0.9 sigma, PA 258); largest consecutive-visit jump 0.052"; rms 0.026"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.256, W2-W3 1.029 (W3 S/N 40.3), W3-W4 3.236 (W4 S/N 34.6), ext_flg 1, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.12, ipd_frac_multi_peak 0, NSS none, Teff 4907 K, logg 4.20, H-alpha pEW -2.556 nm, varclass none; M_G 6.44, -1.45 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 5.5" PA115 G19.75 dG+5.66
- SIMBAD (10"): WISEA J040259.96+315703.9 [Y*?; *,MIR,Y*?] 0.11" refs=8
- ASAS-SN: 2583 points, cameras bA(g,253); bC(g,271); bD(g,286); bE(g,21); bG(g,89); bH(g,72); ba(V,168, d=+0.011); bc(V,232, d=-0.030); bd(V,268, d=-0.021); bg(V,29); bl(g,161); bo(g,112); bp(g,106); bq(g,203); bs(g,67); bt(g,245); change at onset (after-before, per-camera median) -0.021 mag; largest seasonal dimming 0.14 mag at MJD 58507
- dust: excess flux W1 3.58 mJy, W2 2.67 mJy, T = 2169 K (16-84%: 1838-2666) 

## Killed (33)

### uid311901  [D2]  KILLED
- position 102.41321 -11.53941; Gaia DR3 2953169076934962560; G 12.62, BP-RP 0.96, plx 3.53 mas; plot `plots/uid311901.png`
- **KILL:** blend: Gaia neighbour within 6" only 0.66 mag fainter in G (5.5" PA123 G13.27 dG+0.66)
- NEOWISE: score refetch 0.04 (stored 0.04, reproduced True); dW2 0.015, dW1 -0.049, 12 visits, 99 points; baseline W1 11.95, W1-W2 0.068; onset between MJD 58190 and 58400
- detector 2: excess 0.116 mag, z 8.7, jitter ratio 22.3
- field control: target step +0.087 (W1 -0.153); neighbours N=169, median -0.010, robust sigma 0.013, max +0.027; z = 7.3
- centroid: jump at onset 0.689" +- 0.329 (2.1 sigma, PA 165); largest consecutive-visit jump 0.599"; rms 0.626"; toward neighbour: 5.5" PA123 G13.3 (angle 42 deg); expected shift if a neighbour were the source: 5.5" G13.3: 0.42"
- AllWISE 2010: W1-W2 -0.032, W2-W3 0.034 (W3 S/N 8.7), W3-W4 2.617 (W4 S/N 1.4), ext_flg 0, ph_qual AABU: photosphere-like (W2-W3 < 0.5)
- Gaia: RUWE 0.95, ipd_frac_multi_peak 1, NSS none, Teff 5639 K, logg 4.47, H-alpha pEW 0.083 nm, varclass none; M_G 5.35, +0.04 mag vs sequence (on the sequence); neighbours within 10": 5.5" PA123 G13.27 dG+0.66
- SIMBAD (10"): TYC 5387-2161-1 [PM*; *,PM*] 0.85" refs=0
- ASAS-SN: 1170 points, cameras bC(g,107); bG(g,265); bc(V,126, d=+0.016); bg(V,190, d=+0.010); bk(g,225); bo(g,131); bs(g,126); change at onset (after-before, per-camera median) +0.013 mag; largest seasonal dimming 0.01 mag at MJD 58368
- dust: excess flux W1 -0.52 mJy, W2 0.46 mJy, T = 150 K (16-84%: 150-690) W1 excess <= 0: colder than ~150 K (upper limit)

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
- detector 2: excess 0.227 mag, z 12.7, jitter ratio 8.1
- field control: target step +0.498 (W1 +0.241); neighbours N=179, median -0.002, robust sigma 0.010, max +0.052; z = 51.8
- centroid: jump at onset 0.143" +- 0.045 (3.1 sigma, PA 91); largest consecutive-visit jump 0.194"; rms 0.078"; toward neighbour: 2.1" PA91 G13.5 (angle 0 deg); expected shift if a neighbour were the source: 2.1" G13.5: 0.79"; 9.6" G20.8: 3.52"; 9.9" G18.6: 3.62"
- AllWISE 2010: W1-W2 0.448, W2-W3 1.818 (W3 S/N 51.2), W3-W4 0.656 (W4 S/N 9.0), ext_flg 0, ph_qual AAAB: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 0.92, ipd_frac_multi_peak 1, NSS none, Teff nan K, logg nan, H-alpha pEW nan nm, varclass none; M_G 6.39, -0.20 mag vs sequence (on the sequence); neighbours within 10": 2.1" PA91 G13.50 dG-0.51; 9.6" PA184 G20.84 dG+6.82; 9.9" PA305 G18.63 dG+4.61
- SIMBAD (10"): 2MASS J18211387+1139522 [*; *,MIR,NIR] 1.61" refs=2
- ASAS-SN: 1058 points, cameras bA(g,215); bE(g,118); ba(V,224, d=-0.003); bi(g,202); bm(g,100); bq(g,199); change at onset (after-before, per-camera median) -0.003 mag; largest seasonal dimming 0.01 mag at MJD 60397
- dust: excess flux W1 4.36 mJy, W2 5.86 mJy, T = 958 K (16-84%: 931-987) 

### uid1402296  [D2]  KILLED
- position 80.39713 -4.89146; Gaia DR3 3210158170209393920; G 14.48, BP-RP 1.66, plx 2.66 mas; plot `plots/uid1402296.png`
- **KILL:** blend: Gaia neighbour within 6" only -4.84 mag fainter in G (5.2" PA237 G9.64 dG-4.84)
- **young:** SIMBAD young-star types Y*O (2MASS J05213530-0453292)
- flags: centroid jump 1.180" (6.5 sigma, PA 61) away from the neighbour(s) 5.2" PA237 G9.6, as expected when the target itself brightens in a blended WISE PSF | 0.93 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.28 mag (MJD 59456)
- NEOWISE: score refetch 2.98 (stored 2.98, reproduced True); dW2 0.511, dW1 0.272, 7 visits, 84 points; baseline W1 8.86, W1-W2 0.204; onset between MJD 59260 and 59833
- detector 2: excess 0.250 mag, z 9.1, jitter ratio 15.5
- field control: target step +0.567 (W1 +0.310); neighbours N=49, median -0.014, robust sigma 0.012, max +0.021; z = 48.9
- centroid: jump at onset 1.180" +- 0.183 (6.5 sigma, PA 61); largest consecutive-visit jump 1.194"; rms 0.444"; toward neighbour: none; expected shift if a neighbour were the source: 5.2" G9.6: 2.12"
- AllWISE 2010: W1-W2 0.517, W2-W3 1.788 (W3 S/N 50.0), W3-W4 2.026 (W4 S/N 19.2), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.11, ipd_frac_multi_peak 0, NSS none, Teff 5685 K, logg 4.30, H-alpha pEW -1.133 nm, varclass none; M_G 6.60, -0.93 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 5.2" PA237 G9.64 dG-4.84
- SIMBAD (10"): 2MASS J05213530-0453292 [Y*O; *,MIR,NIR,Y*O] 0.03" refs=1; HD  35020 [*; *,NIR] 5.21" refs=8
- ASAS-SN: 1207 points, cameras bB(g,78); bF(g,194, d=-0.144); bb(V,155); bf(V,169); bj(g,252, d=-0.422); bn(g,237, d=+0.136); br(g,122, d=+1.073); change at onset (after-before, per-camera median) -0.004 mag; largest seasonal dimming 0.28 mag at MJD 59456
- dust: excess flux W1 28.36 mJy, W2 34.15 mJy, T = 1060 K (16-84%: 990-1142) 

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

### uid1207210  [D2]  KILLED
- position 71.64783 +23.40364; Gaia DR3 146931385248519296; G 15.21, BP-RP 1.91, plx 2.77 mas; plot `plots/uid1207210.png`
- **KILL:** blend: Gaia neighbour within 6" only -2.64 mag fainter in G (5.2" PA311 G12.57 dG-2.64)
- flags: 0.78 mag above the main sequence at its colour
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 15 visits, 118 points; baseline W1 12.82, W1-W2 0.449; onset between MJD 57273 and 57438
- detector 2: excess 0.457 mag, z 12.0, jitter ratio 22.3
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
- detector 2: excess 0.412 mag, z 10.9, jitter ratio 14.6
- field control: target step +0.326 (W1 +0.306); neighbours N=59, median -0.002, robust sigma 0.016, max +0.028; z = 21.1
- centroid: jump at onset 0.032" +- 0.015 (2.2 sigma, PA 291); largest consecutive-visit jump 0.068"; rms 0.024"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.373, W2-W3 1.434 (W3 S/N 42.3), W3-W4 2.598 (W4 S/N 17.2), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.04, ipd_frac_multi_peak 0, NSS none, Teff 5718 K, logg 4.36, H-alpha pEW -0.733 nm, varclass none; M_G 6.75, -1.43 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): ESO-HA  720 [Y*O; *,Em*,G,NIR,Y*?,Y*O] 0.01" refs=12
- ASAS-SN: 1494 points, cameras bA(g,155); bE(g,216, d=-0.046); ba(V,179); be(V,195); bi(g,335, d=-0.301); bm(g,246, d=-0.162); bq(g,168, d=-0.262); change at onset (after-before, per-camera median) -0.212 mag; largest seasonal dimming 0.32 mag at MJD 58068
- dust: excess flux W1 5.33 mJy, W2 4.75 mJy, T = 1539 K (16-84%: 1457-1630) 

### uid1205623  [D2]  KILLED
- position 202.83110 -54.97604; Gaia DR3 6064008494961785472; G 12.77, BP-RP 1.09, plx 2.77 mas; plot `plots/uid1205623.png`
- **KILL:** cataclysmic variable / X-ray binary in SIMBAD (CV*, V* BV Cen)
- flags: binary type in SIMBAD (SB*, V* BV Cen) | 0.88 mag above the main sequence at its colour | largest seasonal optical dimming 0.15 mag (MJD 60390)
- NEOWISE: score refetch 0.12 (stored 0.12, reproduced True); dW2 0.011, dW1 0.021, 15 visits, 162 points; baseline W1 10.53, W1-W2 0.055; onset between MJD 57057 and 57234
- detector 2: excess 0.111 mag, z 7.3, jitter ratio 8.0
- field control: target step +0.226 (W1 +0.229); neighbours N=185, median -0.002, robust sigma 0.013, max +0.057; z = 18.1
- centroid: jump at onset 0.033" +- 0.015 (2.2 sigma, PA 241); largest consecutive-visit jump 0.040"; rms 0.029"; toward neighbour: none; expected shift if a neighbour were the source: 2.3" G16.2: 0.43"; 4.8" G17.1: 0.91"
- AllWISE 2010: W1-W2 0.020, W2-W3 0.338 (W3 S/N 22.4), W3-W4 1.011 (W4 S/N 2.8), ext_flg 0, ph_qual AAAC: photosphere-like (W2-W3 < 0.5)
- Gaia: RUWE 1.03, ipd_frac_multi_peak 0, NSS none, Teff 5497 K, logg 4.24, H-alpha pEW -0.641 nm, varclass none; M_G 4.98, -0.88 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 2.3" PA26 G16.20 dG+3.43; 4.8" PA13 G17.07 dG+4.30
- SIMBAD (10"): V* BV Cen [CV*; *,CV*,Em*,MIR,NIR,SB*,UV,V*,X] 0.41" refs=196
- ASAS-SN: 1138 points, cameras bE(g,350); be(V,204); bi(g,391); bm(g,193); change at onset (after-before, per-camera median) n/a mag; largest seasonal dimming 0.15 mag at MJD 60390
- dust: excess flux W1 4.23 mJy, W2 2.82 mJy, T = 3078 K (16-84%: 2435-4207) 
- checks missing: ASAS-SN change at onset (no camera spans the onset)

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

### uid1273358  [D2]  KILLED
- position 83.02660 -1.18337; Gaia DR3 3217634157789741952; G 14.45, BP-RP 1.84, plx 2.73 mas; plot `plots/uid1273358.png`
- **KILL:** blend: Gaia neighbour within 6" only 0.13 mag fainter in G (2.4" PA110 G14.59 dG+0.13; 8.0" PA10 G20.34 dG+5.89; 8.6" PA140 G17.65 dG+3.20)
- **young:** SIMBAD young-star types Or*,TT*,Y*O (Haro 5-64; Gaia DR3 3217634162083288320)
- flags: binary type in SIMBAD (**,SB*, NAME Haro 5-64A) | 1.40 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 0.98 (stored 0.97, reproduced True); dW2 0.098, dW1 0.116, 20 visits, 224 points; baseline W1 9.75, W1-W2 0.498; onset between MJD 58899 and 59108
- detector 2: excess 0.516 mag, z 14.3, jitter ratio 8.5
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

### uid1441210  [D2]  KILLED
- position 30.89187 +72.54761; Gaia DR3 546443058371096832; G 15.61, BP-RP 2.10, plx 2.64 mas; plot `plots/uid1441210.png`
- **KILL:** galaxy/QSO within 6" in SIMBAD: 6C 015907+721900 [AGN,BLL,Bla,QSO] 3.7"
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | 1.05 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.14 mag (MJD 59611)
- NEOWISE: score refetch 4.37 (stored 4.37, reproduced True); dW2 0.626, dW1 0.404, 20 visits, 294 points; baseline W1 11.62, W1-W2 0.449; onset between MJD 57261 and 57427
- detector 2: excess 0.427 mag, z 9.9, jitter ratio 10.7
- field control: target step +0.140 (W1 +0.055); neighbours N=107, median +0.000, robust sigma 0.011, max +0.046; z = 12.6
- centroid: jump at onset 0.122" +- 0.129 (0.9 sigma, PA 276); largest consecutive-visit jump 0.360"; rms 0.193"; toward neighbour: 3.7" PA307 G18.7 (angle 31 deg); expected shift if a neighbour were the source: 3.7" G18.7: 0.45"
- AllWISE 2010: W1-W2 0.664, W2-W3 2.468 (W3 S/N 54.1), W3-W4 2.220 (W4 S/N 29.4), ext_flg 1, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.06, ipd_frac_multi_peak 0, NSS none, Teff 4228 K, logg 4.39, H-alpha pEW -0.093 nm, varclass none; M_G 7.71, -1.05 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 3.7" PA307 G18.75 dG+3.14
- SIMBAD (10"): 6C 015907+721900 [BLL; *,AGN,BL?,BLL,Bla,Bz?,MIR,QSO,Rad,gam] 3.74" refs=102
- ASAS-SN: 645 points, cameras bB(g,101); ba(V,209, d=-0.011); bb(V,141, d=+0.020); br(g,153); cB(g,41); change at onset (after-before, per-camera median) +0.004 mag; largest seasonal dimming 0.14 mag at MJD 59611
- dust: excess flux W1 1.30 mJy, W2 2.31 mJy, T = 771 K (16-84%: 744-799) 

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
- detector 2: excess 0.510 mag, z 20.6, jitter ratio 11.2
- field control: target step +0.106 (W1 +0.095); neighbours N=43, median -0.002, robust sigma 0.012, max +0.032; z = 9.1
- centroid: jump at onset 0.082" +- 0.151 (0.5 sigma, PA 206); largest consecutive-visit jump 0.334"; rms 0.152"; toward neighbour: 3.1" PA192 G16.2 (angle 14 deg); expected shift if a neighbour were the source: 3.1" G16.2: 0.29"; 8.3" G19.1: 0.78"
- AllWISE 2010: W1-W2 0.442, W2-W3 2.047 (W3 S/N 57.3), W3-W4 2.054 (W4 S/N 29.0), ext_flg 1, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.36, ipd_frac_multi_peak 2, NSS none, Teff 4880 K, logg 4.22, H-alpha pEW -0.267 nm, varclass none; M_G 6.00, -1.38 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 3.1" PA192 G16.22 dG+2.44; 8.3" PA0 G19.06 dG+5.28
- SIMBAD (10"): Kiso A-0975  87 [TT*; *,**,Em*,NIR,TT*,Y*?,Y*O] 0.04" refs=7; ESO-HA  593 [Em*; *,**,Em*,G] 3.07" refs=2
- ASAS-SN: 1477 points, cameras bA(g,158); bE(g,219); ba(V,149, d=-0.028); be(V,195, d=+0.039); bi(g,338); bm(g,249); bq(g,169); change at onset (after-before, per-camera median) +0.006 mag; largest seasonal dimming 0.04 mag at MJD 58001
- dust: excess flux W1 2.38 mJy, W2 2.37 mJy, T = 1311 K (16-84%: 1095-1629) 

### uid1361145  [D2]  KILLED
- position 84.16952 -6.50256; Gaia DR3 3016935867962755968; G 14.44, BP-RP 2.15, plx 2.68 mas; plot `plots/uid1361145.png`
- **KILL:** blend: Gaia neighbour within 6" only 2.46 mag fainter in G (1.2" PA114 G16.90 dG+2.46)
- **young:** SIMBAD young-star types Or*,Y*?,Y*O (V* V658 Ori A; V* V658 Ori)
- flags: Gaia ipd_frac_multi_peak 33% (resolved double?) | 2.36 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | optical dimming +0.131 mag after the infrared onset (debris transit signature) | largest seasonal optical dimming 1.11 mag (MJD 57807)
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 21 visits, 199 points; baseline W1 10.39, W1-W2 0.408; onset between MJD 56920 and 57088
- detector 2: excess 0.378 mag, z 8.8, jitter ratio 14.9
- field control: target step +0.173 (W1 +0.142); neighbours N=100, median -0.005, robust sigma 0.020, max +0.313; z = 9.0
- centroid: jump at onset 0.015" +- 0.016 (0.9 sigma, PA 2); largest consecutive-visit jump 0.053"; rms 0.032"; toward neighbour: none; expected shift if a neighbour were the source: 1.2" G16.9: 0.17"
- AllWISE 2010: W1-W2 0.311, W2-W3 1.717 (W3 S/N 16.3), W3-W4 2.156 (W4 S/N 10.2), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.28, ipd_frac_multi_peak 33, NSS none, Teff nan K, logg nan, H-alpha pEW -0.395 nm, varclass none; M_G 6.58, -2.36 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 1.2" PA114 G16.90 dG+2.46
- SIMBAD (10"): V* V658 Ori A [Or*; *,Or*,V*,Y*?] 0.02" refs=9; V* V658 Ori [Or*; *,Er*,MIR,NIR,Opt,Or*,V*,X,Y*O] 0.02" refs=28; V* V658 Ori B [*; *,V*] 1.16" refs=2
- ASAS-SN: 1503 points, cameras bA(g,157); bE(g,220); ba(V,178, d=+0.152); be(V,194, d=+0.110); bi(g,343); bm(g,247); bq(g,164); change at onset (after-before, per-camera median) +0.131 mag; largest seasonal dimming 1.11 mag at MJD 57807
- dust: excess flux W1 1.55 mJy, W2 1.89 mJy, T = 1047 K (16-84%: 947-1164) 

### uid1271126  [D2]  KILLED
- position 84.93817 -2.08175; Gaia DR3 3216541419323380480; G 13.30, BP-RP 1.74, plx 2.73 mas; plot `plots/uid1271126.png`
- **KILL:** blend: Gaia neighbour within 6" only 0.47 mag fainter in G (1.5" PA340 G13.77 dG+0.47)
- **young:** SIMBAD young-star types Or*,TT* (V* V2749 Ori)
- flags: Gaia ipd_frac_multi_peak 13% (resolved double?) | 2.26 mag above the main sequence at its colour
- NEOWISE: score refetch 0.96 (stored 0.96, reproduced True); dW2 0.085, dW1 0.038, 20 visits, 192 points; baseline W1 9.01, W1-W2 0.326; onset between MJD 59110 and 59265
- detector 2: excess 0.361 mag, z 11.4, jitter ratio 7.5
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

### uid1330847  [D2]  KILLED
- position 61.64109 +33.27980; Gaia DR3 170646579753471488; G 15.00, BP-RP 2.16, plx 2.70 mas; plot `plots/uid1330847.png`
- **KILL:** blend: Gaia neighbour within 6" only 2.72 mag fainter in G (3.7" PA163 G17.72 dG+2.72; 4.5" PA199 G19.70 dG+4.70)
- **young:** SIMBAD young-star types Y*? (2MASS J04063385+3316474)
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | 1.81 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 0.68 (stored 0.68, reproduced True); dW2 0.138, dW1 0.086, 20 visits, 215 points; baseline W1 10.69, W1-W2 0.367; onset between MJD 59090 and 59248
- detector 2: excess 0.336 mag, z 7.8, jitter ratio 16.1
- field control: target step +0.083 (W1 +0.081); neighbours N=82, median +0.005, robust sigma 0.011, max +0.052; z = 7.0
- centroid: jump at onset 0.021" +- 0.038 (0.5 sigma, PA 21); largest consecutive-visit jump 0.040"; rms 0.051"; toward neighbour: none; expected shift if a neighbour were the source: 3.7" G17.7: 0.27"; 4.5" G19.7: 0.33"
- AllWISE 2010: W1-W2 0.458, W2-W3 2.188 (W3 S/N 49.8), W3-W4 2.391 (W4 S/N 24.9), ext_flg 1, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 0.96, ipd_frac_multi_peak 0, NSS none, Teff 4964 K, logg 4.24, H-alpha pEW -0.515 nm, varclass none; M_G 7.16, -1.81 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 3.7" PA163 G17.72 dG+2.72; 4.5" PA199 G19.70 dG+4.70
- SIMBAD (10"): 2MASS J04063385+3316474 [Y*?; *,NIR,Y*?] 0.10" refs=7; Gaia DR3 170646579753471616 [*; *] 3.62" refs=2
- ASAS-SN: 0 points, cameras n/a; change at onset (after-before, per-camera median) n/a mag; largest seasonal dimming n/a mag at MJD n/a
- dust: excess flux W1 1.71 mJy, W2 1.73 mJy, T = 1296 K (16-84%: 1172-1450) 
- checks missing: ASAS-SN (no source)

### uid354608  [D2]  KILLED
- position 288.96327 -14.25010; Gaia DR3 4185224078359013120; G 11.34, BP-RP 0.93, plx 3.48 mas; plot `plots/uid354608.png`
- **KILL:** eclipsing binary in SIMBAD (EB*, ASAS J191551-1415.0)
- flags: SIMBAD candidate type(s) EB? (ASAS J191551-1415.0): uncertain, not a kill | AllWISE ext_flg = 1 (extended or 2MASS XSC association) | Gaia DR3 NSS solution: nss_two_body_orbit | 1.11 mag above the main sequence at its colour | largest seasonal optical dimming 0.30 mag (MJD 57242)
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 13 visits, 114 points; baseline W1 9.60, W1-W2 0.056; onset between MJD 58947 and 59314
- detector 2: excess 0.102 mag, z 7.7, jitter ratio 13.5
- field control: target step +0.107 (W1 +0.100); neighbours N=185, median -0.003, robust sigma 0.016, max +0.050; z = 6.7
- centroid: jump at onset 0.044" +- 0.026 (1.7 sigma, PA 242); largest consecutive-visit jump 0.053"; rms 0.029"; toward neighbour: none; expected shift if a neighbour were the source: 6.7" G19.3: 0.63"; 6.9" G20.3: 0.65"; 7.1" G19.1: 0.66"; 8.7" G20.2: 0.82"
- AllWISE 2010: W1-W2 -0.033, W2-W3 0.100 (W3 S/N 23.3), W3-W4 0.859 (W4 S/N 2.3), ext_flg 1, ph_qual AAAC: photosphere-like (W2-W3 < 0.5)
- Gaia: RUWE 0.97, ipd_frac_multi_peak 0, NSS nss_two_body_orbit, Teff 5674 K, logg 4.09, H-alpha pEW 0.261 nm, varclass ECL(0.79); M_G 4.05, -1.11 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 6.7" PA337 G19.30 dG+7.95; 6.9" PA191 G20.33 dG+8.98; 7.1" PA320 G19.13 dG+7.79; 8.7" PA53 G20.19 dG+8.84
- SIMBAD (10"): ASAS J191551-1415.0 [EB*; *,EB*,EB?,NIR,Opt,V*] 0.53" refs=5
- ASAS-SN: 888 points, cameras bB(g,66, d=+0.021); bF(g,142, d=-0.195); bb(V,129); bf(V,60); bj(g,159, d=-0.069); bn(g,145, d=-0.037); br(g,166, d=-0.071); cB(g,21); change at onset (after-before, per-camera median) -0.069 mag; largest seasonal dimming 0.30 mag at MJD 57242
- dust: excess flux W1 3.17 mJy, W2 1.44 mJy, T = 8000 K (16-84%: 2395-8000) ratio bluer than an 8000 K blackbody (not dust-like)

### uid1395999  [D2]  KILLED
- position 84.38946 -5.21028; Gaia DR3 3017383201705272192; G 14.33, BP-RP 1.86, plx 2.66 mas; plot `plots/uid1395999.png`
- **KILL:** blend: Gaia neighbour within 6" only 0.54 mag fainter in G (0.9" PA167 G14.87 dG+0.54)
- **young:** SIMBAD young-star types Or*,Y*O (V* V368 Ori)
- flags: binary type in SIMBAD (**, V* V368 Ori A) | Gaia ipd_frac_multi_peak 26% (resolved double?) | 1.62 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.11 mag (MJD 58340)
- NEOWISE: score refetch 0.52 (stored 0.52, reproduced True); dW2 0.051, dW1 -0.003, 21 visits, 208 points; baseline W1 10.10, W1-W2 0.317; onset between MJD 57447 and 57647
- detector 2: excess 0.333 mag, z 9.1, jitter ratio 8.2
- field control: target step +0.073 (W1 +0.049); neighbours N=85, median -0.005, robust sigma 0.013, max +0.185; z = 5.8
- centroid: jump at onset 0.038" +- 0.025 (1.5 sigma, PA 27); largest consecutive-visit jump 0.143"; rms 0.039"; toward neighbour: none; expected shift if a neighbour were the source: 0.9" G14.9: 0.06"
- AllWISE 2010: W1-W2 0.269, W2-W3 2.440 (W3 S/N 40.1), W3-W4 2.622 (W4 S/N 29.1), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.23, ipd_frac_multi_peak 26, NSS none, Teff nan K, logg nan, H-alpha pEW -5.073 nm, varclass none; M_G 6.45, -1.62 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 0.9" PA167 G14.87 dG+0.54
- SIMBAD (10"): V* V368 Ori A [*; *,V*] 0.01" refs=3; V* V368 Ori [Or*; *,**,Em*,MIR,NIR,Or*,Rad,V*,X,Y*O,ev] 0.24" refs=20; V* V368 Ori B [*; *,V*] 0.94" refs=1
- ASAS-SN: 2601 points, cameras bA(g,153); bB(g,92); bE(g,219); bF(g,190); ba(V,179, d=+0.020); bb(V,128, d=+0.021); be(V,195, d=+0.041); bf(V,143, d=+0.014); bi(g,345); bj(g,259); bm(g,248); bn(g,119); bq(g,168); br(g,163); change at onset (after-before, per-camera median) +0.020 mag; largest seasonal dimming 0.11 mag at MJD 58340
- dust: excess flux W1 0.37 mJy, W2 1.17 mJy, T = 553 K (16-84%: 414-703) 

### uid1425993  [D2]  KILLED
- position 151.75300 +67.54649; Gaia DR3 1067083117158668800; G 14.73, BP-RP 1.26, plx 2.65 mas; plot `plots/uid1425993.png`
- **KILL:** cataclysmic variable / X-ray binary in SIMBAD (CV*, V* CH UMa)
- flags: binary type in SIMBAD (SB*, V* CH UMa) | possible optical brightening at onset (-0.185 mag, one camera only) | largest seasonal optical dimming 0.33 mag (MJD 60255)
- NEOWISE: score refetch 0.96 (stored 0.96, reproduced True); dW2 0.088, dW1 0.054, 20 visits, 261 points; baseline W1 12.08, W1-W2 0.120; onset between MJD 57688 and 57846
- detector 2: excess 0.182 mag, z 10.2, jitter ratio 5.1
- field control: target step +0.038 (W1 +0.065); neighbours N=20, median -0.006, robust sigma 0.008, max +0.012; z = 5.6
- centroid: jump at onset 0.006" +- 0.016 (0.4 sigma, PA 359); largest consecutive-visit jump 0.041"; rms 0.032"; toward neighbour: none; expected shift if a neighbour were the source: 8.9" G19.0: 0.30"
- AllWISE 2010: W1-W2 0.151, W2-W3 0.249 (W3 S/N 5.9), W3-W4 2.473 (W4 S/N 0.1), ext_flg 0, ph_qual AABU: photosphere-like (W2-W3 < 0.5)
- Gaia: RUWE 1.04, ipd_frac_multi_peak 0, NSS none, Teff 5848 K, logg 4.74, H-alpha pEW -1.207 nm, varclass CV(0.23); M_G 6.85, +0.41 mag vs sequence (on the sequence); neighbours within 10": 8.9" PA202 G18.97 dG+4.24
- SIMBAD (10"): V* CH UMa [CV*; *,CV*,NIR,SB*,UV,V*,V*?,X] 0.14" refs=114
- ASAS-SN: 670 points, cameras bA(g,189); ba(V,194, d=-0.185); bq(g,287); change at onset (after-before, per-camera median) -0.185 mag; largest seasonal dimming 0.33 mag at MJD 60255
- dust: excess flux W1 0.38 mJy, W2 0.17 mJy, T = 8000 K (16-84%: 8000-8000) ratio bluer than an 8000 K blackbody (not dust-like)

### uid1404605  [D2]  KILLED
- position 83.55500 -5.56486; Gaia DR3 3017266962698857216; G 15.00, BP-RP 1.74, plx 2.66 mas; plot `plots/uid1404605.png`
- **KILL:** blend: Gaia neighbour within 6" only 2.74 mag fainter in G (5.5" PA337 G17.74 dG+2.74) | galaxy/QSO within 6" in SIMBAD: V* V1934 Ori [G] 5.5"
- **young:** SIMBAD young-star types Or*,TT*,TT?,Y*O (V* IM Ori)
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 0.81 (stored 0.81, reproduced True); dW2 0.072, dW1 -0.032, 18 visits, 169 points; baseline W1 10.51, W1-W2 0.384; onset between MJD 58377 and 58535
- detector 2: excess 0.419 mag, z 13.2, jitter ratio 6.3
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
- detector 2: excess 0.592 mag, z 14.3, jitter ratio 10.2
- field control: target step +0.050 (W1 +0.042); neighbours N=72, median -0.002, robust sigma 0.010, max +0.064; z = 5.0
- centroid: jump at onset 0.222" +- 0.060 (3.7 sigma, PA 298); largest consecutive-visit jump 0.124"; rms 0.103"; toward neighbour: none; expected shift if a neighbour were the source: 2.7" G16.5: 0.12"
- AllWISE 2010: W1-W2 0.569, W2-W3 1.444 (W3 S/N 42.8), W3-W4 1.696 (W4 S/N 19.9), ext_flg 1, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.04, ipd_frac_multi_peak 0, NSS none, Teff 3661 K, logg 4.03, H-alpha pEW -0.068 nm, varclass none; M_G 7.11, -1.27 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 2.7" PA128 G16.52 dG+1.55
- SIMBAD (10"): V* DK Ori A [*; *,**,V*] 0.02" refs=3; V* DK Ori [Or*; *,**,Em*,MIR,NIR,Opt,Or*,V*,Y*O] 0.33" refs=17; V* DK Ori B [*; *,**,V*] 2.66" refs=2
- ASAS-SN: 1098 points, cameras bB(g,93); bF(g,187); ba(V,30); bb(V,129, d=+0.124); bf(V,143); bj(g,250); bn(g,107); br(g,159); change at onset (after-before, per-camera median) +0.124 mag; largest seasonal dimming 0.35 mag at MJD 60055
- dust: excess flux W1 -2.46 mJy, W2 -1.80 mJy, T = n/a K (16-84%: n/a-n/a) no W2 excess flux after onset

### uid407360  [D2]  KILLED
- position 6.18656 +62.41666; Gaia DR3 430541063794014208; G 11.62, BP-RP 0.93, plx 3.42 mas; plot `plots/uid407360.png`
- **KILL:** blend: Gaia neighbour within 6" only -0.74 mag fainter in G (2.4" PA257 G10.88 dG-0.74; 6.7" PA64 G19.07 dG+7.46; 8.9" PA141 G20.11 dG+8.49; 9.1" PA245 G18.83 dG+7.21)
- flags: binary type in SIMBAD (**, TYC 4019-3575-2) | AllWISE ext_flg = 1 (extended or 2MASS XSC association) | 0.87 mag above the main sequence at its colour
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 7 visits, 99 points; baseline W1 9.14, W1-W2 0.057; onset between MJD 57237 and 57409
- detector 2: excess 0.103 mag, z 7.7, jitter ratio 13.4
- field control: target step +0.059 (W1 +0.030); neighbours N=147, median -0.004, robust sigma 0.015, max +0.160; z = 4.3
- centroid: jump at onset 0.183" +- 0.101 (1.8 sigma, PA 240); largest consecutive-visit jump 0.079"; rms 0.069"; toward neighbour: 2.4" PA257 G10.9 (angle 16 deg); 9.1" PA245 G18.8 (angle 5 deg); expected shift if a neighbour were the source: 2.4" G10.9: 0.13"; 6.7" G19.1: 0.36"; 8.9" G20.1: 0.48"; 9.1" G18.8: 0.48"
- AllWISE 2010: W1-W2 -0.029, W2-W3 0.063 (W3 S/N 28.5), W3-W4 0.473 (W4 S/N 4.4), ext_flg 1, ph_qual AAAB: photosphere-like (W2-W3 < 0.5)
- Gaia: RUWE 0.94, ipd_frac_multi_peak 0, NSS none, Teff 5366 K, logg 4.18, H-alpha pEW 0.122 nm, varclass none; M_G 4.29, -0.87 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 2.4" PA257 G10.88 dG-0.74; 6.7" PA64 G19.07 dG+7.46; 8.9" PA141 G20.11 dG+8.49; 9.1" PA245 G18.83 dG+7.21
- SIMBAD (10"): TYC 4019-3575-2 [*; *,**] 1.07" refs=0; GSC 04019-03575 [**; *,**,MIR,NIR] 2.02" refs=12; TYC 4019-3575-1 [*; *,**] 2.27" refs=0
- ASAS-SN: 740 points, cameras bD(g,292); bd(V,204, d=+0.016); bt(g,244); change at onset (after-before, per-camera median) +0.016 mag; largest seasonal dimming 0.03 mag at MJD 57553
- dust: excess flux W1 -3.71 mJy, W2 -3.44 mJy, T = n/a K (16-84%: n/a-n/a) no W2 excess flux after onset

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

### uid765206  [D2]  KILLED
- position 85.17842 -1.78810; Gaia DR3 3216648552986769920; G 12.88, BP-RP 1.53, plx 3.07 mas; plot `plots/uid765206.png`
- **KILL:** blend: Gaia neighbour within 6" only -1.51 mag fainter in G (3.7" PA16 G11.37 dG-1.51)
- **young:** SIMBAD young-star types Y*?,Y*O (2MASS J05404281-0147171; 2MASS J05404289-0147136) | Gaia DR3 variability class YSO(0.09)
- flags: centroid jump 0.232" (3.2 sigma, PA 188) away from the neighbour(s) 3.7" PA16 G11.4, as expected when the target itself brightens in a blended WISE PSF | AllWISE ext_flg = 1 (extended or 2MASS XSC association) | 1.85 mag above the main sequence at its colour | not plain dust: optical brightening -0.016 mag (per-camera -0.016,-0.017) together with the infrared rise
- NEOWISE: score refetch 1.54 (stored 1.54, reproduced True); dW2 0.135, dW1 0.101, 20 visits, 186 points; baseline W1 8.74, W1-W2 0.158; onset between MJD 57448 and 57648
- detector 2: excess 0.216 mag, z 9.6, jitter ratio 7.0
- field control: target step +0.083 (W1 +0.041); neighbours N=44, median -0.003, robust sigma 0.022, max +0.348; z = 3.9
- centroid: jump at onset 0.232" +- 0.073 (3.2 sigma, PA 188); largest consecutive-visit jump 0.222"; rms 0.124"; toward neighbour: none; expected shift if a neighbour were the source: 3.7" G11.4: 0.27"
- AllWISE 2010: W1-W2 0.229, W2-W3 1.098 (W3 S/N 3.5), W3-W4 2.179 (W4 S/N -0.1), ext_flg 1, ph_qual AABU: W3 S/N < 5: no W2-W3 class
- Gaia: RUWE 1.11, ipd_frac_multi_peak 0, NSS none, Teff 4985 K, logg 4.13, H-alpha pEW -0.352 nm, varclass YSO(0.09); M_G 5.32, -1.85 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 3.7" PA16 G11.37 dG-1.51
- SIMBAD (10"): 2MASS J05404281-0147171 [Y*O; *,NIR,Y*?,Y*O] 0.04" refs=12; GSC 04767-01392 [*; *] 2.45" refs=1; 2MASS J05404289-0147136 [Y*O; *,NIR,Y*O] 3.67" refs=8
- ASAS-SN: 953 points, cameras bC(g,152); bG(g,219); bc(V,145, d=-0.016); be(V,38); bg(V,153, d=-0.017); bo(g,163); bs(g,83); change at onset (after-before, per-camera median) -0.016 mag; largest seasonal dimming 0.03 mag at MJD 59660
- dust: excess flux W1 2.15 mJy, W2 3.85 mJy, T = 768 K (16-84%: 608-975) 

### uid983466  [D2]  KILLED
- position 81.81985 +0.13132; Gaia DR3 3221019798902558976; G 14.69, BP-RP 2.03, plx 2.91 mas; plot `plots/uid983466.png`
- **KILL:** blend: Gaia neighbour within 6" only 2.92 mag fainter in G (1.8" PA177 G17.62 dG+2.92)
- **young:** SIMBAD young-star types TT*,Y*? (CVSO 932)
- flags: 1.54 mag above the main sequence at its colour
- NEOWISE: score refetch 0.03 (stored 0.03, reproduced True); dW2 0.002, dW1 0.013, 21 visits, 222 points; baseline W1 10.93, W1-W2 0.222; onset between MJD 56725 and 56918
- detector 2: excess 0.211 mag, z 5.0, jitter ratio 4.4
- field control: target step +0.062 (W1 +0.031); neighbours N=66, median +0.006, robust sigma 0.017, max +0.130; z = 3.4
- centroid: jump at onset 0.026" +- 0.042 (0.6 sigma, PA 136); largest consecutive-visit jump 0.042"; rms 0.041"; toward neighbour: 1.8" PA177 G17.6 (angle 41 deg); expected shift if a neighbour were the source: 1.8" G17.6: 0.10"
- AllWISE 2010: W1-W2 0.221, W2-W3 0.585 (W3 S/N 18.4), W3-W4 1.816 (W4 S/N 3.9), ext_flg 0, ph_qual AAAB: weak W3 excess (0.5 < W2-W3 < 1.0)
- Gaia: RUWE 1.04, ipd_frac_multi_peak 0, NSS none, Teff 4907 K, logg 4.24, H-alpha pEW -0.585 nm, varclass none; M_G 7.01, -1.54 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 1.8" PA177 G17.62 dG+2.92
- SIMBAD (10"): CVSO 932 [TT*; *,LM*,NIR,TT*,Y*?] 0.02" refs=12; Gaia DR3 3221019794608110336 [*; *] 1.78" refs=1
- ASAS-SN: 2068 points, cameras bA(g,166); bE(g,172); ba(V,259, d=+0.039); bd(V,151, d=+0.058); be(V,56); bi(g,275); bl(g,311); bm(g,198); bp(g,192); bq(g,125); bt(g,163); change at onset (after-before, per-camera median) +0.049 mag; largest seasonal dimming 0.06 mag at MJD 59783
- dust: excess flux W1 0.35 mJy, W2 0.62 mJy, T = 778 K (16-84%: 642-947) 

### uid438629  [D2]  KILLED
- position 134.10324 -58.84427; Gaia DR3 5303330788529959808; G 14.35, BP-RP 1.53, plx 3.38 mas; plot `plots/uid438629.png`
- **KILL:** centroid jump 0.288" (4.2 sigma) at the onset toward a neighbour: 6.2" PA100 G18.2 (angle 9 deg)
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 0.04 (stored 0.04, reproduced True); dW2 0.003, dW1 -0.023, 7 visits, 113 points; baseline W1 11.44, W1-W2 0.160; onset between MJD 57744 and 57906
- detector 2: excess 0.218 mag, z 9.7, jitter ratio 5.1
- field control: target step +0.020 (W1 -0.002); neighbours N=178, median -0.005, robust sigma 0.010, max +0.029; z = 2.4
- centroid: jump at onset 0.288" +- 0.068 (4.2 sigma, PA 109); largest consecutive-visit jump 0.304"; rms 0.114"; toward neighbour: 6.2" PA100 G18.2 (angle 9 deg); expected shift if a neighbour were the source: 2.0" G18.6: 0.04"; 6.2" G18.2: 0.11"
- AllWISE 2010: W1-W2 0.361, W2-W3 3.202 (W3 S/N 54.4), W3-W4 2.134 (W4 S/N 27.2), ext_flg 1, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.00, ipd_frac_multi_peak 0, NSS none, Teff 4560 K, logg 4.64, H-alpha pEW -0.035 nm, varclass none; M_G 7.00, -0.18 mag vs sequence (on the sequence); neighbours within 10": 2.0" PA193 G18.63 dG+4.28; 6.2" PA100 G18.23 dG+3.88
- SIMBAD (10"): no object
- ASAS-SN: 0 points, cameras n/a; change at onset (after-before, per-camera median) n/a mag; largest seasonal dimming n/a mag at MJD n/a
- dust: excess flux W1 -0.18 mJy, W2 -0.16 mJy, T = n/a K (16-84%: n/a-n/a) no W2 excess flux after onset
- checks missing: ASAS-SN (no source)

### uid624745  [D2]  KILLED
- position 162.07510 +52.30819; Gaia DR3 837035254216960128; G 14.84, BP-RP 1.35, plx 3.20 mas; plot `plots/uid624745.png`
- **KILL:** cataclysmic variable / X-ray binary in SIMBAD (CV*, V* LY UMa)
- flags: possible optical brightening at onset (-0.142 mag, one camera only) | largest seasonal optical dimming 0.14 mag (MJD 59340)
- NEOWISE: score refetch 0.35 (stored 0.34, reproduced True); dW2 0.026, dW1 0.012, 21 visits, 298 points; baseline W1 12.26, W1-W2 0.089; onset between MJD 57146 and 57340
- detector 2: excess 0.152 mag, z 8.2, jitter ratio 3.1
- field control: target step +0.012 (W1 +0.034); neighbours N=14, median -0.006, robust sigma 0.009, max +0.007; z = 2.1
- centroid: jump at onset 0.021" +- 0.014 (1.6 sigma, PA 332); largest consecutive-visit jump 0.058"; rms 0.031"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.030, W2-W3 0.052 (W3 S/N 3.7), W3-W4 2.920 (W4 S/N -0.7), ext_flg 0, ph_qual AABU: W3 S/N < 5: no W2-W3 class
- Gaia: RUWE 1.01, ipd_frac_multi_peak 0, NSS none, Teff 5433 K, logg 4.79, H-alpha pEW -1.275 nm, varclass none; M_G 7.36, +0.66 mag vs sequence (on the sequence); neighbours within 10": none
- SIMBAD (10"): V* LY UMa [CV*; *,CV*,NIR,V*,X] 0.36" refs=35
- ASAS-SN: 719 points, cameras bC(g,221); bc(V,229, d=-0.142); bs(g,269); change at onset (after-before, per-camera median) -0.142 mag; largest seasonal dimming 0.14 mag at MJD 59340
- dust: excess flux W1 0.02 mJy, W2 -0.08 mJy, T = n/a K (16-84%: n/a-n/a) no W2 excess flux after onset

### uid999033  [D2]  KILLED
- position 267.53313 -28.86257; Gaia DR3 4057393138528809088; G 14.94, BP-RP 1.58, plx 2.90 mas; plot `plots/uid999033.png`
- **KILL:** blend: Gaia neighbour within 6" only 2.16 mag fainter in G (2.1" PA37 G19.53 dG+4.58; 2.8" PA22 G20.43 dG+5.48; 3.1" PA238 G18.28 dG+3.34; 3.9" PA176 G20.69 dG+5.75; 4.6" PA231 G17.10 dG+2.16; 5.8" PA89 G20.58 dG+5.64; 7.8" PA179 G19.69 dG+4.74; 8.5" PA27 G18.40 dG+3.46; 9.4" PA175 G19.94 dG+5.00)
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 16 visits, 114 points; baseline W1 9.69, W1-W2 0.571; onset between MJD 60187 and 60387
- detector 2: excess 0.625 mag, z 26.2, jitter ratio 4.1
- field control: target step +0.048 (W1 +0.014); neighbours N=73, median +0.018, robust sigma 0.047, max +0.179; z = 0.6
- centroid: jump at onset 0.262" +- 0.111 (2.4 sigma, PA 41); largest consecutive-visit jump 0.344"; rms 0.171"; toward neighbour: 2.1" PA37 G19.5 (angle 3 deg); 2.8" PA22 G20.4 (angle 19 deg); 8.5" PA27 G18.4 (angle 13 deg); expected shift if a neighbour were the source: 2.1" G19.5: 0.09"; 2.8" G20.4: 0.12"; 3.1" G18.3: 0.13"; 3.9" G20.7: 0.17"; 4.6" G17.1: 0.20"; 5.8" G20.6: 0.25"; 7.8" G19.7: 0.33"; 8.5" G18.4: 0.36"; 9.4" G19.9: 0.40"
- AllWISE 2010: W1-W2 0.502, W2-W3 1.316 (W3 S/N 12.1), W3-W4 3.261 (W4 S/N 20.3), ext_flg 1, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.02, ipd_frac_multi_peak 0, NSS none, Teff 4497 K, logg 4.64, H-alpha pEW -0.029 nm, varclass none; M_G 7.26, -0.05 mag vs sequence (on the sequence); neighbours within 10": 2.1" PA37 G19.53 dG+4.58; 2.8" PA22 G20.43 dG+5.48; 3.1" PA238 G18.28 dG+3.34; 3.9" PA176 G20.69 dG+5.75; 4.6" PA231 G17.10 dG+2.16; 5.8" PA89 G20.58 dG+5.64; 7.8" PA179 G19.69 dG+4.74; 8.5" PA27 G18.40 dG+3.46; 9.4" PA175 G19.94 dG+5.00
- SIMBAD (10"): no object
- ASAS-SN: 0 points, cameras n/a; change at onset (after-before, per-camera median) n/a mag; largest seasonal dimming n/a mag at MJD n/a
- dust: excess flux W1 0.43 mJy, W2 1.76 mJy, T = 493 K (16-84%: 150-771) 
- checks missing: ASAS-SN (no source)

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

