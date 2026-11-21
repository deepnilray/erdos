# vet2 report: far target list (final)

Generated 2026-11-21 06:59 UTC; 26 targets; machine-generated, the plots in plots/ still need a look by eye.

Kill rules: field-control z < 5 (detector-1 and list targets); centroid jump > 3 sigma toward a Gaia neighbour; Gaia neighbour within 6" with dG < 3; baseline W1 < 8; SIMBAD CV / confirmed eclipsing binary (counterpart within 3"); SIMBAD galaxy/QSO within 6"; young star (SIMBAD Y*O, Y*?, TT*, TT?, Or*, Ae*, Ae?, pr* within 5" or Gaia variability class YSO) kills detector-1/list targets and labels detector-2 targets 'known/likely young star'. Flags (not kills): 'not plain dust' (optical brightening at the infrared onset in >= 2 ASAS-SN cameras, none dimming, median < -0.015 mag), SIMBAD '?' candidate types, RUWE, NSS, ext_flg, colour classes.

## Controls

| Control | Result | Detail |
|---|---|---|
| ASASSN-21qj | PASS | category SURVIVOR, SIMBAD 2MASS J08152329-3859234 (10 refs), field z 57.3, missing: none |
| J060000 | PASS | category SURVIVOR, largest ASAS-SN seasonal dimming 0.35 mag at MJD 58864 |
| V836 Tau | PASS | young: SIMBAD young-star types Or*,TT*,TT?,Y*?,Y*O (V* V836 Tau) | Gaia DR3 variability class YSO(0.83) |

Counts: {'SURVIVOR': 15, 'KILLED': 6, 'YOUNG': 5}

## Survivors (15)

### uid269584  [D2]  SURVIVOR
- position 81.02729 +34.27504; Gaia DR3 182736942750800256; G 11.57, BP-RP 0.83, plx 3.58 mas; plot `plots/uid269584.png`
- NEOWISE: score refetch 0.90 (stored 0.90, reproduced True); dW2 0.085, dW1 0.020, 18 visits, 160 points; baseline W1 9.99, W1-W2 0.135; onset between MJD 58377 and 58535
- detector 2: excess 0.174 mag, z 16.8, jitter ratio 9.1
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
- detector 2: excess 0.418 mag, z 28.2, jitter ratio 7.7
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
- detector 2: excess 0.189 mag, z 18.2, jitter ratio 3.6
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

### uid239897  [D2]  SURVIVOR
- position 222.73717 +36.20318; Gaia DR3 1293509154439630464; G 14.04, BP-RP 1.46, plx 3.62 mas; plot `plots/uid239897.png`
- flags: AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 1.25 (stored 1.25, reproduced True); dW2 0.095, dW1 0.073, 21 visits, 272 points; baseline W1 11.28, W1-W2 0.307; onset between MJD 57931 and 58134
- detector 2: excess 0.368 mag, z 19.6, jitter ratio 4.0
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
- detector 2: excess 0.398 mag, z 17.6, jitter ratio 5.9
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
- detector 2: excess 0.161 mag, z 15.5, jitter ratio 10.3
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

### uid325718  [D2]  SURVIVOR
- position 35.42480 +62.01116; Gaia DR3 513833673802372736; G 13.99, BP-RP 1.39, plx 3.51 mas; plot `plots/uid325718.png`
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 9 visits, 95 points; baseline W1 11.35, W1-W2 0.948; onset between MJD 57986 and 58144
- detector 2: excess 1.011 mag, z 56.8, jitter ratio 7.8
- field control: target step +0.161 (W1 +0.004); neighbours N=199, median -0.006, robust sigma 0.014, max +0.162; z = 11.9
- centroid: jump at onset 0.444" +- 0.185 (2.4 sigma, PA 181); largest consecutive-visit jump 0.331"; rms 0.389"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 1.083, W2-W3 1.507 (W3 S/N 22.3), W3-W4 2.809 (W4 S/N 21.4), ext_flg 1, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.22, ipd_frac_multi_peak 0, NSS none, Teff 4702 K, logg 4.45, H-alpha pEW -0.037 nm, varclass none; M_G 6.71, -0.11 mag vs sequence (on the sequence); neighbours within 10": none
- SIMBAD (10"): no object
- ASAS-SN: 975 points, cameras bD(g,271); bd(V,177, d=+0.004); bs(g,284); bt(g,243); change at onset (after-before, per-camera median) +0.004 mag; largest seasonal dimming 0.02 mag at MJD 60563
- dust: excess flux W1 -0.05 mJy, W2 1.12 mJy, T = 150 K (16-84%: 150-398) W1 excess <= 0: colder than ~150 K (upper limit)

### uid137313  [D2]  SURVIVOR
- position 330.31742 -28.50241; Gaia DR3 6617669842852419712; G 13.04, BP-RP 1.06, plx 3.77 mas; plot `plots/uid137313.png`
- flags: AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 1.49 (stored 1.49, reproduced True); dW2 0.135, dW1 0.090, 17 visits, 127 points; baseline W1 11.02, W1-W2 0.217; onset between MJD 57885 and 58052
- detector 2: excess 0.272 mag, z 18.8, jitter ratio 7.0
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
- detector 2: excess 0.486 mag, z 32.8, jitter ratio 4.7
- field control: target step +0.058 (W1 +0.029); neighbours N=35, median -0.003, robust sigma 0.013, max +0.032; z = 4.6
- centroid: jump at onset 0.007" +- 0.013 (0.5 sigma, PA 239); largest consecutive-visit jump 0.046"; rms 0.026"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.429, W2-W3 1.517 (W3 S/N 50.4), W3-W4 0.921 (W4 S/N 8.5), ext_flg 0, ph_qual AAAB: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.37, ipd_frac_multi_peak 0, NSS none, Teff 5461 K, logg 4.47, H-alpha pEW 0.105 nm, varclass none; M_G 5.22, -0.59 mag vs sequence (on the sequence); neighbours within 10": none
- SIMBAD (10"): UCAC4 379-068655 [*; *,MIR,NIR] 0.20" refs=1
- ASAS-SN: 1152 points, cameras bB(g,76); bF(g,124, d=-0.001); bb(V,111); bf(V,138); bj(g,281, d=+0.010); bn(g,230, d=-0.001); br(g,145, d=+0.006); cB(g,47); change at onset (after-before, per-camera median) +0.002 mag; largest seasonal dimming 0.00 mag at MJD 59039
- dust: excess flux W1 -0.14 mJy, W2 -0.01 mJy, T = n/a K (16-84%: n/a-n/a) no W2 excess flux after onset

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

### uid126443  [D2]  SURVIVOR
- position 344.04495 +63.72553; Gaia DR3 2208143124690762368; G 13.42, BP-RP 1.21, plx 3.78 mas; plot `plots/uid126443.png`
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association)
- NEOWISE: score refetch 0.75 (stored 0.75, reproduced True); dW2 0.100, dW1 0.363, 13 visits, 181 points; baseline W1 11.23, W1-W2 0.117; onset between MJD 57038 and 57226
- detector 2: excess 0.179 mag, z 11.3, jitter ratio 4.4
- field control: target step -0.002 (W1 +0.016); neighbours N=194, median -0.008, robust sigma 0.010, max +0.097; z = 0.7
- centroid: jump at onset 0.234" +- 0.330 (0.7 sigma, PA 74); largest consecutive-visit jump 1.335"; rms 0.557"; toward neighbour: 5.7" PA44 G20.4 (angle 30 deg); expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 -0.326, W2-W3 0.222 (W3 S/N 15.2), W3-W4 0.806 (W4 S/N 2.2), ext_flg 1, ph_qual AAAC: photosphere-like (W2-W3 < 0.5)
- Gaia: RUWE 1.27, ipd_frac_multi_peak 0, NSS none, Teff 4885 K, logg 4.57, H-alpha pEW -0.037 nm, varclass SOLAR_LIKE(0.57); M_G 6.31, +0.04 mag vs sequence (on the sequence); neighbours within 10": 5.7" PA44 G20.42 dG+6.99; 7.6" PA258 G17.32 dG+3.90
- SIMBAD (10"): Gaia DR3 2208143124690762368 [*; *] 0.17" refs=1
- ASAS-SN: 1002 points, cameras bC(g,310); bc(V,172, d=+0.003); br(g,289); bs(g,231); change at onset (after-before, per-camera median) +0.003 mag; largest seasonal dimming 0.02 mag at MJD 59568
- dust: excess flux W1 3.50 mJy, W2 0.50 mJy, T = 8000 K (16-84%: 8000-8000) ratio bluer than an 8000 K blackbody (not dust-like)

### uid690873  [D2]  SURVIVOR
- position 269.27186 -26.55673; Gaia DR3 4064217566685938560; G 12.82, BP-RP 1.26, plx 3.14 mas; plot `plots/uid690873.png`
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | 1.12 mag above the main sequence at its colour
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 9 visits, 81 points; baseline W1 10.54, W1-W2 0.056; onset between MJD 59821 and 60024
- detector 2: excess 0.119 mag, z 7.3, jitter ratio 5.5
- field control: target step +0.019 (W1 -0.026); neighbours N=102, median +0.010, robust sigma 0.027, max +0.128; z = 0.3
- centroid: jump at onset 0.206" +- 0.196 (1.1 sigma, PA 115); largest consecutive-visit jump 0.519"; rms 0.218"; toward neighbour: 9.9" PA151 G18.9 (angle 36 deg); expected shift if a neighbour were the source: 9.6" G20.2: 0.17"; 9.9" G18.9: 0.17"
- AllWISE 2010: W1-W2 -0.118, W2-W3 0.282 (W3 S/N -4.5), W3-W4 2.458 (W4 S/N -3.9), ext_flg 1, ph_qual AAUU: W3 S/N < 5: no W2-W3 class
- Gaia: RUWE 0.76, ipd_frac_multi_peak 1, NSS none, Teff 5003 K, logg 4.26, H-alpha pEW 0.067 nm, varclass none; M_G 5.31, -1.12 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 9.6" PA182 G20.18 dG+7.36; 9.9" PA151 G18.92 dG+6.10
- SIMBAD (10"): no object
- ASAS-SN: 822 points, cameras bH(g,257, d=-0.010); bl(g,249, d=+0.009); bp(g,166, d=+0.012); bt(g,150, d=-0.004); change at onset (after-before, per-camera median) +0.003 mag; largest seasonal dimming 0.01 mag at MJD 60470
- dust: excess flux W1 -0.30 mJy, W2 -0.27 mJy, T = n/a K (16-84%: n/a-n/a) no W2 excess flux after onset

## Known/likely young stars (detector 2) (5)

### uid532798  [D2]  YOUNG
- position 79.82666 -5.72572; Gaia DR3 3208462482760921088; G 13.77, BP-RP 1.57, plx 3.28 mas; plot `plots/uid532798.png`
- **young:** SIMBAD young-star types TT*,Y*?,Y*O (Kiso A-0975  47)
- flags: 0.94 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.36 mag (MJD 60639)
- NEOWISE: score refetch 3.33 (stored 3.33, reproduced True); dW2 0.382, dW1 0.349, 20 visits, 222 points; baseline W1 9.42, W1-W2 0.426; onset between MJD 57807 and 58006
- detector 2: excess 0.481 mag, z 21.6, jitter ratio 11.2
- field control: target step +0.512 (W1 +0.427); neighbours N=43, median -0.001, robust sigma 0.008, max +0.333; z = 62.9
- centroid: jump at onset 0.024" +- 0.016 (1.5 sigma, PA 300); largest consecutive-visit jump 0.052"; rms 0.027"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.500, W2-W3 1.644 (W3 S/N 61.6), W3-W4 2.119 (W4 S/N 38.5), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.14, ipd_frac_multi_peak 0, NSS none, Teff 5850 K, logg 4.39, H-alpha pEW -2.380 nm, varclass none; M_G 6.36, -0.94 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): Kiso A-0975  47 [TT*; *,Em*,NIR,Opt,TT*,Y*?,Y*O] 0.05" refs=8
- ASAS-SN: 1303 points, cameras bB(g,85); bF(g,205); bb(V,155, d=+0.003); bf(V,171, d=-0.307); bj(g,280); bn(g,237); br(g,170); change at onset (after-before, per-camera median) -0.152 mag; largest seasonal dimming 0.36 mag at MJD 60639
- dust: excess flux W1 18.56 mJy, W2 19.39 mJy, T = 1237 K (16-84%: 1193-1284) 

### uid416674  [D2]  YOUNG
- position 63.57807 +11.97018; Gaia DR3 3304172564776041728; G 12.10, BP-RP 1.51, plx 3.41 mas; plot `plots/uid416674.png`
- **young:** SIMBAD young-star types TT? (IRAS 04114+1150)
- flags: 2.37 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.33 mag (MJD 58902)
- NEOWISE: score refetch 1.37 (stored 1.37, reproduced True); dW2 0.115, dW1 0.133, 21 visits, 196 points; baseline W1 8.97, W1-W2 0.390; onset between MJD 58515 and 58724
- detector 2: excess 0.449 mag, z 22.0, jitter ratio 7.8
- field control: target step +0.369 (W1 +0.327); neighbours N=44, median +0.003, robust sigma 0.009, max +0.022; z = 39.4
- centroid: jump at onset 0.016" +- 0.020 (0.8 sigma, PA 100); largest consecutive-visit jump 0.071"; rms 0.034"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.369, W2-W3 2.912 (W3 S/N 74.5), W3-W4 2.063 (W4 S/N 42.7), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.36, ipd_frac_multi_peak 0, NSS none, Teff 5587 K, logg 3.88, H-alpha pEW 0.022 nm, varclass none; M_G 4.76, -2.37 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): IRAS 04114+1150 [TT?; *,IR,NIR,TT?] 0.13" refs=8
- ASAS-SN: 1989 points, cameras bB(g,96, d=+0.022); bF(g,126, d=-0.031); bG(g,147, d=+0.051); bb(V,249); bc(V,219); bf(V,33); bg(V,45); bj(g,166, d=+0.066); bk(g,247, d=+0.045); bn(g,204, d=+0.051); bo(g,205, d=+0.044); br(g,134, d=+0.036); bs(g,118, d=-0.035); change at onset (after-before, per-camera median) +0.044 mag; largest seasonal dimming 0.33 mag at MJD 58902
- dust: excess flux W1 13.69 mJy, W2 11.57 mJy, T = 1679 K (16-84%: 1475-1963) 

### uid351866  [D2]  YOUNG
- position 79.09382 -7.94732; Gaia DR3 3207022466127209472; G 15.18, BP-RP 2.13, plx 3.48 mas; plot `plots/uid351866.png`
- **young:** SIMBAD young-star types Or*,TT*,Y*O (2MASS J05162251-0756503)
- flags: 0.97 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | optical dimming +0.202 mag after the infrared onset (debris transit signature) | largest seasonal optical dimming 0.34 mag (MJD 56920)
- NEOWISE: score refetch 3.01 (stored 3.01, reproduced True); dW2 0.238, dW1 0.260, 18 visits, 192 points; baseline W1 9.26, W1-W2 0.561; onset between MJD 58005 and 58163
- detector 2: excess 0.533 mag, z 13.3, jitter ratio 7.2
- field control: target step +0.316 (W1 +0.245); neighbours N=44, median +0.002, robust sigma 0.010, max +0.031; z = 30.3
- centroid: jump at onset 0.017" +- 0.021 (0.8 sigma, PA 165); largest consecutive-visit jump 0.034"; rms 0.031"; toward neighbour: none; expected shift if a neighbour were the source: 8.5" G21.9: 2.15"
- AllWISE 2010: W1-W2 0.538, W2-W3 1.633 (W3 S/N 61.3), W3-W4 2.380 (W4 S/N 41.2), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.20, ipd_frac_multi_peak 0, NSS none, Teff 5699 K, logg 4.50, H-alpha pEW -2.313 nm, varclass none; M_G 7.89, -0.97 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 8.5" PA250 G21.91 dG+6.73
- SIMBAD (10"): 2MASS J05162251-0756503 [TT*; *,NIR,Or*,TT*,Y*O] 0.01" refs=5
- ASAS-SN: 2460 points, cameras bB(g,74); bC(g,92); bF(g,190); bG(g,270); bb(V,133, d=+0.075); bc(V,134, d=+0.470); be(V,32); bf(V,164); bg(V,155, d=+0.279); bj(g,252); bk(g,353); bn(g,145); bo(g,220); br(g,144, d=+0.125); bs(g,102); change at onset (after-before, per-camera median) +0.202 mag; largest seasonal dimming 0.34 mag at MJD 56920
- dust: excess flux W1 16.44 mJy, W2 15.23 mJy, T = 1450 K (16-84%: 1370-1540) 

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

### uid310080  [D2]  YOUNG
- position 78.56621 -1.64957; Gaia DR3 3215095114856015232; G 11.95, BP-RP 1.44, plx 3.53 mas; plot `plots/uid310080.png`
- **young:** SIMBAD young-star types Y*?,Y*O (IRAS 05117-0142)
- flags: 2.25 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 0.42 (stored 0.41, reproduced True); dW2 0.089, dW1 0.094, 20 visits, 236 points; baseline W1 8.71, W1-W2 0.263; onset between MJD 57806 and 58005
- detector 2: excess 0.325 mag, z 17.9, jitter ratio 14.8
- field control: target step +0.189 (W1 +0.189); neighbours N=51, median -0.001, robust sigma 0.010, max +0.091; z = 18.4
- centroid: jump at onset 0.017" +- 0.018 (0.9 sigma, PA 267); largest consecutive-visit jump 0.040"; rms 0.028"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.293, W2-W3 2.464 (W3 S/N 76.3), W3-W4 2.564 (W4 S/N 49.5), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.05, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW -0.519 nm, varclass RS(0.53); M_G 4.69, -2.25 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): IRAS 05117-0142 [Y*O; *,IR,NIR,Y*?,Y*O] 0.05" refs=7
- ASAS-SN: 2647 points, cameras bC(g,183); bD(g,166); bG(g,211); bH(g,206); bc(V,119, d=+0.055); be(V,40); bg(V,185, d=+0.030); bh(V,152, d=+0.032); bk(g,298); bl(g,323); bo(g,233); bp(g,213); bs(g,143); bt(g,175); change at onset (after-before, per-camera median) +0.032 mag; largest seasonal dimming 0.03 mag at MJD 59282
- dust: excess flux W1 15.81 mJy, W2 10.53 mJy, T = 3066 K (16-84%: 2490-4061) 

## Killed (6)

### uid311901  [D2]  KILLED
- position 102.41321 -11.53941; Gaia DR3 2953169076934962560; G 12.62, BP-RP 0.96, plx 3.53 mas; plot `plots/uid311901.png`
- **KILL:** blend: Gaia neighbour within 6" only 0.66 mag fainter in G (5.5" PA123 G13.27 dG+0.66)
- NEOWISE: score refetch 0.04 (stored 0.04, reproduced True); dW2 0.015, dW1 -0.049, 12 visits, 99 points; baseline W1 11.95, W1-W2 0.068; onset between MJD 58190 and 58400
- detector 2: excess 0.117 mag, z 9.1, jitter ratio 22.3
- field control: target step +0.087 (W1 -0.153); neighbours N=169, median -0.010, robust sigma 0.013, max +0.027; z = 7.3
- centroid: jump at onset 0.689" +- 0.329 (2.1 sigma, PA 165); largest consecutive-visit jump 0.599"; rms 0.626"; toward neighbour: 5.5" PA123 G13.3 (angle 42 deg); expected shift if a neighbour were the source: 5.5" G13.3: 0.42"
- AllWISE 2010: W1-W2 -0.032, W2-W3 0.034 (W3 S/N 8.7), W3-W4 2.617 (W4 S/N 1.4), ext_flg 0, ph_qual AABU: photosphere-like (W2-W3 < 0.5)
- Gaia: RUWE 0.95, ipd_frac_multi_peak 1, NSS none, Teff 5639 K, logg 4.47, H-alpha pEW 0.083 nm, varclass none; M_G 5.35, +0.04 mag vs sequence (on the sequence); neighbours within 10": 5.5" PA123 G13.27 dG+0.66
- SIMBAD (10"): TYC 5387-2161-1 [PM*; *,PM*] 0.85" refs=0
- ASAS-SN: 1170 points, cameras bC(g,107); bG(g,265); bc(V,126, d=+0.016); bg(V,190, d=+0.010); bk(g,225); bo(g,131); bs(g,126); change at onset (after-before, per-camera median) +0.013 mag; largest seasonal dimming 0.01 mag at MJD 58368
- dust: excess flux W1 -0.52 mJy, W2 0.46 mJy, T = 150 K (16-84%: 150-690) W1 excess <= 0: colder than ~150 K (upper limit)

### uid438254  [D2]  KILLED
- position 52.35804 +31.44442; Gaia DR3 121412854238659712; G 15.05, BP-RP 2.14, plx 3.38 mas; plot `plots/uid438254.png`
- **KILL:** blend: Gaia neighbour within 6" only 2.67 mag fainter in G (4.4" PA40 G17.73 dG+2.67)
- **young:** SIMBAD young-star types Or*,Y*?,Y*O (ATO J052.3580+31.4444; [HL2013] 052.35902+31.44538)
- flags: 1.19 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | optical dimming +0.086 mag after the infrared onset (debris transit signature) | largest seasonal optical dimming 0.15 mag (MJD 59967)
- NEOWISE: score refetch 1.72 (stored 1.72, reproduced True); dW2 0.140, dW1 0.052, 21 visits, 223 points; baseline W1 8.49, W1-W2 0.701; onset between MJD 58510 and 58715
- detector 2: excess 0.673 mag, z 16.6, jitter ratio 7.0
- field control: target step +0.216 (W1 +0.261); neighbours N=87, median +0.003, robust sigma 0.020, max +0.181; z = 10.6
- centroid: jump at onset 0.045" +- 0.024 (1.9 sigma, PA 258); largest consecutive-visit jump 0.099"; rms 0.045"; toward neighbour: none; expected shift if a neighbour were the source: 4.4" G17.7: 0.80"
- AllWISE 2010: W1-W2 0.743, W2-W3 2.312 (W3 S/N 73.2), W3-W4 1.398 (W4 S/N 47.4), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.05, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW 0.025 nm, varclass none; M_G 7.70, -1.19 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 4.4" PA40 G17.73 dG+2.67
- SIMBAD (10"): ATO J052.3580+31.4444 [Or*; *,IR,MIR,NIR,Opt,Or*,V*,X,Y*?,Y*O] 0.19" refs=49; [HL2013] 052.35902+31.44538 [Y*?; *,IR,Y*?] 4.46" refs=8
- ASAS-SN: 2220 points, cameras bC(g,253, d=+0.042); bD(g,288, d=+0.070); bG(g,70, d=+0.295); bH(g,86, d=+0.150); ba(V,40); bc(V,272); bd(V,251); bg(V,22); bh(V,33); bk(g,130, d=+0.065); bl(g,163, d=+0.126); bo(g,126, d=+0.150); bp(g,126, d=-0.010); bs(g,172, d=+0.103); bt(g,188, d=+0.065); change at onset (after-before, per-camera median) +0.086 mag; largest seasonal dimming 0.15 mag at MJD 59967
- dust: excess flux W1 22.87 mJy, W2 21.36 mJy, T = 1433 K (16-84%: 1326-1562) 

### uid354608  [D2]  KILLED
- position 288.96327 -14.25010; Gaia DR3 4185224078359013120; G 11.34, BP-RP 0.93, plx 3.48 mas; plot `plots/uid354608.png`
- **KILL:** eclipsing binary in SIMBAD (EB*, ASAS J191551-1415.0)
- flags: SIMBAD candidate type(s) EB? (ASAS J191551-1415.0): uncertain, not a kill | AllWISE ext_flg = 1 (extended or 2MASS XSC association) | Gaia DR3 NSS solution: nss_two_body_orbit | 1.11 mag above the main sequence at its colour | largest seasonal optical dimming 0.30 mag (MJD 57242)
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 13 visits, 114 points; baseline W1 9.60, W1-W2 0.056; onset between MJD 58947 and 59314
- detector 2: excess 0.102 mag, z 8.6, jitter ratio 13.5
- field control: target step +0.107 (W1 +0.100); neighbours N=185, median -0.003, robust sigma 0.016, max +0.050; z = 6.7
- centroid: jump at onset 0.044" +- 0.026 (1.7 sigma, PA 242); largest consecutive-visit jump 0.053"; rms 0.029"; toward neighbour: none; expected shift if a neighbour were the source: 6.7" G19.3: 0.63"; 6.9" G20.3: 0.65"; 7.1" G19.1: 0.66"; 8.7" G20.2: 0.82"
- AllWISE 2010: W1-W2 -0.033, W2-W3 0.100 (W3 S/N 23.3), W3-W4 0.859 (W4 S/N 2.3), ext_flg 1, ph_qual AAAC: photosphere-like (W2-W3 < 0.5)
- Gaia: RUWE 0.97, ipd_frac_multi_peak 0, NSS nss_two_body_orbit, Teff 5674 K, logg 4.09, H-alpha pEW 0.261 nm, varclass ECL(0.79); M_G 4.05, -1.11 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 6.7" PA337 G19.30 dG+7.95; 6.9" PA191 G20.33 dG+8.98; 7.1" PA320 G19.13 dG+7.79; 8.7" PA53 G20.19 dG+8.84
- SIMBAD (10"): ASAS J191551-1415.0 [EB*; *,EB*,EB?,NIR,Opt,V*] 0.53" refs=5
- ASAS-SN: 888 points, cameras bB(g,66, d=+0.021); bF(g,142, d=-0.195); bb(V,129); bf(V,60); bj(g,159, d=-0.069); bn(g,145, d=-0.037); br(g,166, d=-0.071); cB(g,21); change at onset (after-before, per-camera median) -0.069 mag; largest seasonal dimming 0.30 mag at MJD 57242
- dust: excess flux W1 3.17 mJy, W2 1.44 mJy, T = 8000 K (16-84%: 2395-8000) ratio bluer than an 8000 K blackbody (not dust-like)

### uid407360  [D2]  KILLED
- position 6.18656 +62.41666; Gaia DR3 430541063794014208; G 11.62, BP-RP 0.93, plx 3.42 mas; plot `plots/uid407360.png`
- **KILL:** blend: Gaia neighbour within 6" only -0.74 mag fainter in G (2.4" PA257 G10.88 dG-0.74; 6.7" PA64 G19.07 dG+7.46; 8.9" PA141 G20.11 dG+8.49; 9.1" PA245 G18.83 dG+7.21)
- flags: binary type in SIMBAD (**, TYC 4019-3575-2) | AllWISE ext_flg = 1 (extended or 2MASS XSC association) | 0.87 mag above the main sequence at its colour
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 7 visits, 99 points; baseline W1 9.14, W1-W2 0.057; onset between MJD 57237 and 57409
- detector 2: excess 0.103 mag, z 8.6, jitter ratio 13.4
- field control: target step +0.059 (W1 +0.030); neighbours N=147, median -0.004, robust sigma 0.015, max +0.160; z = 4.3
- centroid: jump at onset 0.183" +- 0.101 (1.8 sigma, PA 240); largest consecutive-visit jump 0.079"; rms 0.069"; toward neighbour: 2.4" PA257 G10.9 (angle 16 deg); 9.1" PA245 G18.8 (angle 5 deg); expected shift if a neighbour were the source: 2.4" G10.9: 0.13"; 6.7" G19.1: 0.36"; 8.9" G20.1: 0.48"; 9.1" G18.8: 0.48"
- AllWISE 2010: W1-W2 -0.029, W2-W3 0.063 (W3 S/N 28.5), W3-W4 0.473 (W4 S/N 4.4), ext_flg 1, ph_qual AAAB: photosphere-like (W2-W3 < 0.5)
- Gaia: RUWE 0.94, ipd_frac_multi_peak 0, NSS none, Teff 5366 K, logg 4.18, H-alpha pEW 0.122 nm, varclass none; M_G 4.29, -0.87 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 2.4" PA257 G10.88 dG-0.74; 6.7" PA64 G19.07 dG+7.46; 8.9" PA141 G20.11 dG+8.49; 9.1" PA245 G18.83 dG+7.21
- SIMBAD (10"): TYC 4019-3575-2 [*; *,**] 1.07" refs=0; GSC 04019-03575 [**; *,**,MIR,NIR] 2.02" refs=12; TYC 4019-3575-1 [*; *,**] 2.27" refs=0
- ASAS-SN: 740 points, cameras bD(g,292); bd(V,204, d=+0.016); bt(g,244); change at onset (after-before, per-camera median) +0.016 mag; largest seasonal dimming 0.03 mag at MJD 57553
- dust: excess flux W1 -3.71 mJy, W2 -3.44 mJy, T = n/a K (16-84%: n/a-n/a) no W2 excess flux after onset

### uid438629  [D2]  KILLED
- position 134.10324 -58.84427; Gaia DR3 5303330788529959808; G 14.35, BP-RP 1.53, plx 3.38 mas; plot `plots/uid438629.png`
- **KILL:** centroid jump 0.288" (4.2 sigma) at the onset toward a neighbour: 6.2" PA100 G18.2 (angle 9 deg)
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 0.04 (stored 0.04, reproduced True); dW2 0.003, dW1 -0.023, 7 visits, 113 points; baseline W1 11.44, W1-W2 0.160; onset between MJD 57744 and 57906
- detector 2: excess 0.218 mag, z 10.4, jitter ratio 5.1
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
- detector 2: excess 0.153 mag, z 9.0, jitter ratio 3.1
- field control: target step +0.012 (W1 +0.034); neighbours N=14, median -0.006, robust sigma 0.009, max +0.007; z = 2.1
- centroid: jump at onset 0.021" +- 0.014 (1.6 sigma, PA 332); largest consecutive-visit jump 0.058"; rms 0.031"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.030, W2-W3 0.052 (W3 S/N 3.7), W3-W4 2.920 (W4 S/N -0.7), ext_flg 0, ph_qual AABU: W3 S/N < 5: no W2-W3 class
- Gaia: RUWE 1.01, ipd_frac_multi_peak 0, NSS none, Teff 5433 K, logg 4.79, H-alpha pEW -1.275 nm, varclass none; M_G 7.36, +0.66 mag vs sequence (on the sequence); neighbours within 10": none
- SIMBAD (10"): V* LY UMa [CV*; *,CV*,NIR,V*,X] 0.36" refs=35
- ASAS-SN: 719 points, cameras bC(g,221); bc(V,229, d=-0.142); bs(g,269); change at onset (after-before, per-camera median) -0.142 mag; largest seasonal dimming 0.14 mag at MJD 59340
- dust: excess flux W1 0.02 mJy, W2 -0.08 mJy, T = n/a K (16-84%: n/a-n/a) no W2 excess flux after onset

