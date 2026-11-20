# vet2 report: near target list (final)

Generated 2026-11-20 15:22 UTC; 41 targets; machine-generated, the plots in plots/ still need a look by eye.

Kill rules: field-control z < 5 (detector-1 and list targets); centroid jump > 3 sigma toward a Gaia neighbour; Gaia neighbour within 6" with dG < 3; baseline W1 < 8; SIMBAD CV / confirmed eclipsing binary (counterpart within 3"); SIMBAD galaxy/QSO within 6"; young star (SIMBAD Y*O, Y*?, TT*, TT?, Or*, Ae*, Ae?, pr* within 5" or Gaia variability class YSO) kills detector-1/list targets and labels detector-2 targets 'known/likely young star'. Flags (not kills): 'not plain dust' (optical brightening at the infrared onset in >= 2 ASAS-SN cameras, none dimming, median < -0.015 mag), SIMBAD '?' candidate types, RUWE, NSS, ext_flg, colour classes.

## Controls

| Control | Result | Detail |
|---|---|---|
| ASASSN-21qj | PASS | category SURVIVOR, SIMBAD 2MASS J08152329-3859234 (10 refs), field z 57.3, missing: none |
| J060000 | PASS | category SURVIVOR, largest ASAS-SN seasonal dimming 0.35 mag at MJD 58864 |
| V836 Tau | PASS | young: SIMBAD young-star types Or*,TT*,TT?,Y*?,Y*O (V* V836 Tau) | Gaia DR3 variability class YSO(0.83) |

Counts: {'SURVIVOR': 21, 'YOUNG': 14, 'KILLED': 6}

## Survivors (21)

### uid683344  [D1]  SURVIVOR
- position 220.96632 -76.19612; Gaia DR3 5792808347020475136; G 13.52, BP-RP 1.29, plx 4.04 mas; plot `plots/uid683344.png`
- NEOWISE: score refetch 21.59 (stored 21.59, reproduced True); dW2 0.364, dW1 0.168, 19 visits, 238 points; baseline W1 11.18, W1-W2 -0.067; onset between MJD 58178 and 58342
- field control: target step +0.349 (W1 +0.172); neighbours N=140, median -0.007, robust sigma 0.010, max +0.027; z = 34.3
- centroid: jump at onset 0.028" +- 0.018 (1.6 sigma, PA 306); largest consecutive-visit jump 0.043"; rms 0.024"; toward neighbour: none; expected shift if a neighbour were the source: 6.9" G18.5: 1.90"; 7.9" G16.4: 2.17"
- AllWISE 2010: W1-W2 -0.046, W2-W3 0.215 (W3 S/N 10.7), W3-W4 1.869 (W4 S/N 0.5), ext_flg 0, ph_qual AAAU: photosphere-like (W2-W3 < 0.5)
- Gaia: RUWE 1.02, ipd_frac_multi_peak 0, NSS none, Teff 4774 K, logg 4.58, H-alpha pEW -0.008 nm, varclass SOLAR_LIKE(0.66); M_G 6.55, +0.02 mag vs sequence (on the sequence); neighbours within 10": 6.9" PA122 G18.49 dG+4.97; 7.9" PA223 G16.37 dG+2.85
- SIMBAD (10"): no object
- ASAS-SN: 1114 points, cameras bF(g,324); bf(V,235, d=-0.052); bj(g,358, d=+0.014); bn(g,197, d=-0.064); change at onset (after-before, per-camera median) -0.052 mag; largest seasonal dimming 0.04 mag at MJD 60189
- dust: excess flux W1 1.87 mJy, W2 2.30 mJy, T = 1040 K (16-84%: 996-1086) 

### uid387633  [D2]  SURVIVOR
- position 162.78307 -11.61469; Gaia DR3 3757763060178100736; G 13.45, BP-RP 1.44, plx 5.09 mas; plot `plots/uid387633.png`
- NEOWISE: score refetch 0.13 (stored 0.12, reproduced True); dW2 0.008, dW1 0.003, 19 visits, 158 points; baseline W1 10.88, W1-W2 0.054; onset between MJD 57175 and 57368
- detector 2: excess 0.117 mag, z 7.7, jitter ratio 4.1
- field control: target step +0.048 (W1 +0.016); neighbours N=19, median -0.004, robust sigma 0.007, max +0.016; z = 6.9
- centroid: jump at onset 0.042" +- 0.031 (1.3 sigma, PA 66); largest consecutive-visit jump 0.064"; rms 0.034"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.054, W2-W3 1.511 (W3 S/N 25.4), W3-W4 0.873 (W4 S/N 3.5), ext_flg 0, ph_qual AAAB: W3 excess only (W2-W3 > 1.0; debris-disk-like or blend)
- Gaia: RUWE 1.07, ipd_frac_multi_peak 0, NSS none, Teff 4475 K, logg 4.63, H-alpha pEW -0.020 nm, varclass none; M_G 6.99, +0.05 mag vs sequence (on the sequence); neighbours within 10": none
- SIMBAD (10"): no object
- ASAS-SN: 1287 points, cameras bD(g,116); bH(g,183); bd(V,114, d=+0.009); bf(V,61); bh(V,123); bl(g,283); bp(g,265); bt(g,142); change at onset (after-before, per-camera median) +0.009 mag; largest seasonal dimming 0.02 mag at MJD 59023
- dust: excess flux W1 0.25 mJy, W2 0.39 mJy, T = 862 K (16-84%: 645-1192) 

### uid55148  [D2]  SURVIVOR
- position 13.18917 -27.47577; Gaia DR3 2342601748810281088; G 11.89, BP-RP 1.46, plx 9.98 mas; plot `plots/uid55148.png`
- NEOWISE: score refetch 1.79 (stored 1.79, reproduced True); dW2 0.114, dW1 0.083, 20 visits, 174 points; baseline W1 9.18, W1-W2 0.085; onset between MJD 57560 and 57729
- detector 2: excess 0.146 mag, z 9.1, jitter ratio 6.1
- field control: target step +0.072 (W1 +0.043); neighbours N=18, median -0.007, robust sigma 0.019, max +0.035; z = 4.3
- centroid: jump at onset 0.029" +- 0.016 (1.8 sigma, PA 140); largest consecutive-visit jump 0.062"; rms 0.027"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.144, W2-W3 0.404 (W3 S/N 42.0), W3-W4 0.620 (W4 S/N 5.3), ext_flg 0, ph_qual AAAB: photosphere-like (W2-W3 < 0.5)
- Gaia: RUWE 1.30, ipd_frac_multi_peak 0, NSS none, Teff 5292 K, logg 4.62, H-alpha pEW -0.337 nm, varclass none; M_G 6.88, -0.13 mag vs sequence (on the sequence); neighbours within 10": none
- SIMBAD (10"): BPM 46714 [PM*; *,NIR,PM*,Ro*,V*,X] 1.55" refs=12
- ASAS-SN: 0 points, cameras n/a; change at onset (after-before, per-camera median) n/a mag; largest seasonal dimming n/a mag at MJD n/a
- dust: excess flux W1 4.41 mJy, W2 3.97 mJy, T = 1515 K (16-84%: 1237-1947) 
- checks missing: ASAS-SN (no source)

### uid651925  [D2]  SURVIVOR
- position 269.69076 -25.97545; Gaia DR3 4064266666749464448; G 12.60, BP-RP 1.21, plx 4.12 mas; plot `plots/uid651925.png`
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 11 visits, 88 points; baseline W1 8.12, W1-W2 0.110; onset between MJD 59457 and 59658
- detector 2: excess 0.173 mag, z 14.6, jitter ratio 6.6
- field control: target step +0.020 (W1 +0.063); neighbours N=140, median -0.006, robust sigma 0.025, max +0.189; z = 1.1
- centroid: jump at onset 0.054" +- 0.041 (1.3 sigma, PA 125); largest consecutive-visit jump 0.066"; rms 0.059"; toward neighbour: 5.1" PA130 G20.1 (angle 5 deg); expected shift if a neighbour were the source: 2.5" G17.8: 0.05"; 5.1" G20.1: 0.09"; 9.4" G19.9: 0.17"
- AllWISE 2010: W1-W2 0.110, W2-W3 0.149 (W3 S/N 23.5), W3-W4 -0.284 (W4 S/N 0.4), ext_flg 0, ph_qual AAAU: photosphere-like (W2-W3 < 0.5)
- Gaia: RUWE 1.13, ipd_frac_multi_peak 0, NSS none, Teff 5049 K, logg 4.38, H-alpha pEW 0.053 nm, varclass SOLAR_LIKE(0.67); M_G 5.67, -0.58 mag vs sequence (on the sequence); neighbours within 10": 2.5" PA287 G17.82 dG+5.21; 5.1" PA130 G20.14 dG+7.54; 9.4" PA333 G19.86 dG+7.26
- SIMBAD (10"): no object
- ASAS-SN: 823 points, cameras bH(g,256, d=-0.008); bl(g,250, d=+0.001); bp(g,166, d=-0.002); bt(g,151, d=+0.011); change at onset (after-before, per-camera median) -0.000 mag; largest seasonal dimming 0.02 mag at MJD 60470
- dust: excess flux W1 5.38 mJy, W2 -0.94 mJy, T = n/a K (16-84%: n/a-n/a) no W2 excess flux after onset

### ASASSN-21qj (uid699339)  [CONTROL+D1]  SURVIVOR
- position 123.84704 -38.98983; Gaia DR3 5539970601632026752; G 13.37, BP-RP 0.81, plx 1.76 mas; plot `plots/ASASSN-21qj_uid699339_.png`
- flags: centroid jump 0.349" (5.5 sigma, PA 56) away from the neighbour(s) 3.7" PA253 G16.9, as expected when the target itself brightens in a blended WISE PSF | largest seasonal optical dimming 1.11 mag (MJD 59529)
- NEOWISE: score refetch 38.04 (stored 38.04, reproduced True); dW2 0.738, dW1 0.332, 12 visits, 133 points; baseline W1 11.65, W1-W2 -0.057; onset between MJD 58072 and 58227
- field control: target step +0.803 (W1 +0.402); neighbours N=169, median -0.003, robust sigma 0.014, max +0.055; z = 57.3
- centroid: jump at onset 0.349" +- 0.063 (5.5 sigma, PA 56); largest consecutive-visit jump 0.212"; rms 0.109"; toward neighbour: none; expected shift if a neighbour were the source: 3.7" G16.9: 1.94"; 7.3" G18.7: 3.81"
- AllWISE 2010: W1-W2 -0.068, W2-W3 -0.498 (W3 S/N 2.3), W3-W4 3.219 (W4 S/N -2.6), ext_flg 0, ph_qual AACU: W3 S/N < 5: no W2-W3 class
- Gaia: RUWE 1.10, ipd_frac_multi_peak 0, NSS none, Teff 5761 K, logg 4.34, H-alpha pEW 0.112 nm, varclass none; M_G 4.60, +0.07 mag vs sequence (on the sequence); neighbours within 10": 3.7" PA253 G16.91 dG+3.54; 7.3" PA182 G18.67 dG+5.30
- SIMBAD (10"): 2MASS J08152329-3859234 [*; *,NIR] 0.15" refs=10; 2MASS J08152298-3859244 [*; *,NIR] 3.74" refs=1
- ASAS-SN: 1351 points, cameras bE(g,411); be(V,238, d=-0.018); bi(g,497); bm(g,205); change at onset (after-before, per-camera median) -0.018 mag; largest seasonal dimming 1.11 mag at MJD 59529
- dust: excess flux W1 2.72 mJy, W2 3.68 mJy, T = 953 K (16-84%: 934-972) 

### uid529482  [D2]  SURVIVOR
- position 311.02040 +29.66480; Gaia DR3 1858978638770086016; G 12.06, BP-RP 1.89, plx 4.49 mas; plot `plots/uid529482.png`
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | 2.83 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | optical dimming +0.141 mag after the infrared onset (debris transit signature) | largest seasonal optical dimming 0.40 mag (MJD 58370)
- NEOWISE: score refetch 2.02 (stored 2.02, reproduced True); dW2 0.671, dW1 0.534, 10 visits, 118 points; baseline W1 8.16, W1-W2 0.445; onset between MJD 57159 and 57335
- detector 2: excess 0.449 mag, z 13.0, jitter ratio 30.8
- field control: target step +0.529 (W1 +0.323); neighbours N=180, median -0.005, robust sigma 0.013, max +0.032; z = 42.3
- centroid: jump at onset 0.030" +- 0.022 (1.4 sigma, PA 176); largest consecutive-visit jump 0.072"; rms 0.031"; toward neighbour: none; expected shift if a neighbour were the source: 6.5" G20.6: 2.49"; 7.1" G18.4: 2.72"
- AllWISE 2010: W1-W2 0.505, W2-W3 1.517 (W3 S/N 74.4), W3-W4 1.895 (W4 S/N 46.1), ext_flg 1, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.21, ipd_frac_multi_peak 0, NSS none, Teff 5406 K, logg 3.81, H-alpha pEW -0.979 nm, varclass none; M_G 5.32, -2.83 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 6.5" PA242 G20.62 dG+8.56; 7.1" PA259 G18.41 dG+6.34
- SIMBAD (10"): no object
- ASAS-SN: 961 points, cameras bD(g,282); bH(g,72); bd(V,182, d=+0.141); bl(g,112); bp(g,66); bt(g,247); change at onset (after-before, per-camera median) +0.141 mag; largest seasonal dimming 0.40 mag at MJD 58370
- dust: excess flux W1 72.21 mJy, W2 86.26 mJy, T = 1069 K (16-84%: 1040-1099) 

### uid52960  [D2]  SURVIVOR
- position 141.34135 -67.54018; Gaia DR3 5247128354025136128; G 11.55, BP-RP 1.44, plx 10.11 mas; plot `plots/uid52960.png`
- flags: Gaia ipd_frac_multi_peak 21% (resolved double?)
- NEOWISE: score refetch 1.50 (stored 1.50, reproduced True); dW2 0.089, dW1 0.068, 19 visits, 410 points; baseline W1 8.82, W1-W2 0.097; onset between MJD 57042 and 57214
- detector 2: excess 0.159 mag, z 10.3, jitter ratio 5.0
- field control: target step +0.224 (W1 +0.111); neighbours N=138, median -0.001, robust sigma 0.007, max +0.113; z = 30.4
- centroid: jump at onset 0.014" +- 0.009 (1.5 sigma, PA 8); largest consecutive-visit jump 0.028"; rms 0.021"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.135, W2-W3 0.970 (W3 S/N 66.0), W3-W4 2.630 (W4 S/N 39.7), ext_flg 0, ph_qual AAAA: weak W3 excess (0.5 < W2-W3 < 1.0)
- Gaia: RUWE 1.24, ipd_frac_multi_peak 21, NSS none, Teff 4457 K, logg 4.44, H-alpha pEW 0.001 nm, varclass none; M_G 6.57, -0.38 mag vs sequence (on the sequence); neighbours within 10": none
- SIMBAD (10"): TYC 9196-2916-1 [*; *,MIR,NIR] 0.50" refs=5
- ASAS-SN: 2236 points, cameras bF(g,302); bG(g,395); be(V,148, d=+0.005); bf(V,202); bg(V,223); bk(g,432); bn(g,224); bo(g,310); change at onset (after-before, per-camera median) +0.005 mag; largest seasonal dimming 0.01 mag at MJD 59608
- dust: excess flux W1 6.06 mJy, W2 7.39 mJy, T = 1046 K (16-84%: 937-1178) 

### uid584244  [D2]  SURVIVOR
- position 43.54827 +5.88271; Gaia DR3 5628404318169472; G 13.43, BP-RP 1.35, plx 4.31 mas; plot `plots/uid584244.png`
- flags: AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.10 mag (MJD 60695)
- NEOWISE: score refetch 4.35 (stored 4.35, reproduced True); dW2 0.288, dW1 0.139, 20 visits, 169 points; baseline W1 10.59, W1-W2 0.369; onset between MJD 57606 and 57772
- detector 2: excess 0.434 mag, z 30.6, jitter ratio 5.0
- field control: target step +0.286 (W1 +0.168); neighbours N=26, median -0.003, robust sigma 0.016, max +0.022; z = 18.1
- centroid: jump at onset 0.033" +- 0.023 (1.5 sigma, PA 120); largest consecutive-visit jump 0.056"; rms 0.037"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.389, W2-W3 1.575 (W3 S/N 41.2), W3-W4 1.411 (W4 S/N 10.7), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.08, ipd_frac_multi_peak 0, NSS none, Teff 4510 K, logg 4.55, H-alpha pEW -0.001 nm, varclass SOLAR_LIKE(0.19); M_G 6.60, -0.11 mag vs sequence (on the sequence); neighbours within 10": none
- SIMBAD (10"): no object
- ASAS-SN: 2434 points, cameras bC(g,254); bD(g,272); bG(g,168); bH(g,164); ba(V,28); bc(V,247, d=+0.024); bd(V,240, d=+0.041); bg(V,59, d=+0.093); bh(V,56, d=+0.033); bk(g,192); bl(g,256); bo(g,234); bs(g,135); bt(g,129); change at onset (after-before, per-camera median) +0.037 mag; largest seasonal dimming 0.10 mag at MJD 60695
- dust: excess flux W1 2.56 mJy, W2 3.59 mJy, T = 923 K (16-84%: 880-968) 

### J060000 (uid211004)  [CONTROL+D1]  SURVIVOR
- position 90.00308 -31.00781; Gaia DR3 2891196718939580672; G 13.13, BP-RP 1.52, plx 6.39 mas; plot `plots/J060000_uid211004_.png`
- flags: SIMBAD candidate type(s) EB? (ASASSN-V J060000.76-310027.8): uncertain, not a kill | AllWISE ext_flg = 1 (extended or 2MASS XSC association) | optical dimming +0.142 mag after the infrared onset (debris transit signature) | largest seasonal optical dimming 0.35 mag (MJD 58864)
- NEOWISE: score refetch 8.86 (stored 8.86, reproduced True); dW2 0.130, dW1 0.042, 21 visits, 253 points; baseline W1 10.52, W1-W2 -0.063; onset between MJD 58751 and 58905
- field control: target step +0.146 (W1 +0.049); neighbours N=54, median +0.003, robust sigma 0.010, max +0.054; z = 14.9
- centroid: jump at onset 0.031" +- 0.021 (1.5 sigma, PA 264); largest consecutive-visit jump 0.050"; rms 0.029"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 -0.092, W2-W3 0.039 (W3 S/N 15.2), W3-W4 1.732 (W4 S/N 1.3), ext_flg 1, ph_qual AAAU: photosphere-like (W2-W3 < 0.5)
- Gaia: RUWE 1.02, ipd_frac_multi_peak 0, NSS none, Teff 4498 K, logg 4.67, H-alpha pEW -0.051 nm, varclass SOLAR_LIKE(0.41); M_G 7.16, -0.00 mag vs sequence (on the sequence); neighbours within 10": none
- SIMBAD (10"): ASASSN-V J060000.76-310027.8 [EB?; *,EB?,MIR,NIR,V*] 0.35" refs=12
- ASAS-SN: 1581 points, cameras bE(g,355, d=+0.102); be(V,379); bi(g,415, d=+0.109); bm(g,268, d=+0.276); bq(g,164, d=+0.176); change at onset (after-before, per-camera median) +0.142 mag; largest seasonal dimming 0.35 mag at MJD 58864
- dust: excess flux W1 0.87 mJy, W2 1.44 mJy, T = 813 K (16-84%: 728-912) 

### uid74609  [D2]  SURVIVOR
- position 327.55699 +14.11477; Gaia DR3 1768914166695591296; G 13.07, BP-RP 1.78, plx 9.06 mas; plot `plots/uid74609.png`
- flags: AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 0.52 (stored 0.52, reproduced True); dW2 0.042, dW1 0.084, 21 visits, 253 points; baseline W1 9.66, W1-W2 0.405; onset between MJD 58794 and 58996
- detector 2: excess 0.429 mag, z 14.4, jitter ratio 6.6
- field control: target step +0.164 (W1 +0.138); neighbours N=45, median -0.003, robust sigma 0.013, max +0.061; z = 12.6
- centroid: jump at onset 0.037" +- 0.015 (2.5 sigma, PA 111); largest consecutive-visit jump 0.041"; rms 0.024"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.438, W2-W3 1.073 (W3 S/N 53.0), W3-W4 0.619 (W4 S/N 7.5), ext_flg 0, ph_qual AAAB: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 0.97, ipd_frac_multi_peak 0, NSS none, Teff 4208 K, logg 4.65, H-alpha pEW -0.024 nm, varclass SOLAR_LIKE(0.23); M_G 7.85, -0.00 mag vs sequence (on the sequence); neighbours within 10": none
- SIMBAD (10"): no object
- ASAS-SN: 1196 points, cameras bC(g,265, d=+0.005); bG(g,108, d=+0.009); bc(V,265); bg(V,35); bk(g,138, d=+0.015); bo(g,168, d=+0.022); bs(g,217, d=-0.002); change at onset (after-before, per-camera median) +0.009 mag; largest seasonal dimming 0.01 mag at MJD 57515
- dust: excess flux W1 5.21 mJy, W2 5.06 mJy, T = 1357 K (16-84%: 1241-1497) 

### uid329675  [D2]  SURVIVOR
- position 339.60016 -56.06835; Gaia DR3 6505057483979425024; G 14.34, BP-RP 1.86, plx 5.42 mas; plot `plots/uid329675.png`
- flags: AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 0.80 (stored 0.81, reproduced True); dW2 0.049, dW1 0.027, 21 visits, 249 points; baseline W1 10.61, W1-W2 0.334; onset between MJD 59139 and 59342
- detector 2: excess 0.343 mag, z 10.3, jitter ratio 5.5
- field control: target step +0.145 (W1 +0.074); neighbours N=27, median +0.001, robust sigma 0.013, max +0.044; z = 11.4
- centroid: jump at onset 0.039" +- 0.033 (1.2 sigma, PA 308); largest consecutive-visit jump 0.140"; rms 0.060"; toward neighbour: 7.7" PA294 G15.4 (angle 14 deg); expected shift if a neighbour were the source: 7.5" G19.9: 0.94"; 7.7" G15.4: 0.96"
- AllWISE 2010: W1-W2 0.429, W2-W3 1.922 (W3 S/N 49.7), W3-W4 1.092 (W4 S/N 9.2), ext_flg 0, ph_qual AAAB: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.04, ipd_frac_multi_peak 0, NSS none, Teff 3655 K, logg 4.36, H-alpha pEW 0.170 nm, varclass none; M_G 8.01, -0.07 mag vs sequence (on the sequence); neighbours within 10": 7.5" PA167 G19.88 dG+5.54; 7.7" PA294 G15.35 dG+1.01
- SIMBAD (10"): no object
- ASAS-SN: 2487 points, cameras bF(g,311, d=+0.001); bH(g,378, d=-0.020); bf(V,303); bh(V,190); bj(g,398, d=+0.001); bl(g,408, d=-0.039); bn(g,279, d=-0.016); bp(g,220, d=-0.000); change at onset (after-before, per-camera median) -0.008 mag; largest seasonal dimming 0.03 mag at MJD 56848
- dust: excess flux W1 0.51 mJy, W2 0.93 mJy, T = 751 K (16-84%: 623-909) 

### uid637541  [D1]  SURVIVOR
- position 252.21435 -69.41863; Gaia DR3 5808318474663998464; G 11.92, BP-RP 0.89, plx 4.16 mas; plot `plots/uid637541.png`
- flags: not plain dust: optical brightening -0.037 mag (per-camera -0.037,-0.036,-0.046) together with the infrared rise
- NEOWISE: score refetch 10.18 (stored 10.18, reproduced True); dW2 0.144, dW1 0.085, 21 visits, 209 points; baseline W1 10.34, W1-W2 -0.037; onset between MJD 59082 and 59286
- field control: target step +0.160 (W1 +0.083); neighbours N=109, median +0.002, robust sigma 0.014, max +0.055; z = 11.2
- centroid: jump at onset 0.025" +- 0.012 (2.0 sigma, PA 290); largest consecutive-visit jump 0.032"; rms 0.023"; toward neighbour: 5.1" PA308 G18.1 (angle 19 deg); expected shift if a neighbour were the source: 5.1" G18.1: 0.69"; 7.3" G19.2: 1.00"; 9.7" G19.6: 1.33"
- AllWISE 2010: W1-W2 -0.046, W2-W3 -0.019 (W3 S/N 15.0), W3-W4 1.476 (W4 S/N 0.4), ext_flg 0, ph_qual AAAU: photosphere-like (W2-W3 < 0.5)
- Gaia: RUWE 1.03, ipd_frac_multi_peak 0, NSS none, Teff 5513 K, logg 4.42, H-alpha pEW 0.099 nm, varclass SOLAR_LIKE(0.72); M_G 5.02, +0.05 mag vs sequence (on the sequence); neighbours within 10": 5.1" PA308 G18.09 dG+6.16; 7.3" PA160 G19.19 dG+7.27; 9.7" PA1 G19.60 dG+7.67
- SIMBAD (10"): TYC 9279-457-1 [*; *,NIR] 0.27" refs=7
- ASAS-SN: 1213 points, cameras bF(g,322, d=-0.037); bf(V,297); bj(g,398, d=-0.036); bn(g,196, d=-0.046); change at onset (after-before, per-camera median) -0.037 mag; largest seasonal dimming 0.04 mag at MJD 58744
- dust: excess flux W1 1.82 mJy, W2 1.82 mJy, T = 1310 K (16-84%: 1158-1497) 

### uid584601  [D2]  SURVIVOR
- position 258.62760 +14.23864; Gaia DR3 4541869985001129728; G 11.99, BP-RP 0.91, plx 4.31 mas; plot `plots/uid584601.png`
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association)
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 7 visits, 77 points; baseline W1 10.29, W1-W2 0.123; onset between MJD 57454 and 57625
- detector 2: excess 0.170 mag, z 16.4, jitter ratio 18.4
- field control: target step +0.257 (W1 -0.007); neighbours N=25, median +0.003, robust sigma 0.033, max +0.154; z = 7.6
- centroid: jump at onset 0.017" +- 0.042 (0.4 sigma, PA 323); largest consecutive-visit jump 0.095"; rms 0.043"; toward neighbour: none; expected shift if a neighbour were the source: 8.4" G19.1: 1.78"
- AllWISE 2010: W1-W2 -0.054, W2-W3 5.217 (W3 S/N 71.4), W3-W4 -0.141 (W4 S/N 24.5), ext_flg 1, ph_qual AAAA: W3 excess only (W2-W3 > 1.0; debris-disk-like or blend)
- Gaia: RUWE 1.12, ipd_frac_multi_peak 0, NSS none, Teff 5681 K, logg 4.51, H-alpha pEW 0.092 nm, varclass none; M_G 5.16, +0.10 mag vs sequence (on the sequence); neighbours within 10": 8.4" PA255 G19.14 dG+7.16
- SIMBAD (10"): no object
- ASAS-SN: 1321 points, cameras bD(g,272); bH(g,131); ba(V,40); bd(V,307, d=+0.000); bh(V,30); bl(g,169); bp(g,166); bt(g,206); change at onset (after-before, per-camera median) +0.000 mag; largest seasonal dimming 0.01 mag at MJD 60222
- dust: excess flux W1 -0.05 mJy, W2 3.14 mJy, T = 150 K (16-84%: 150-380) W1 excess <= 0: colder than ~150 K (upper limit)

### uid235546  [D2]  SURVIVOR
- position 279.93986 +40.57960; Gaia DR3 2110512779973465984; G 10.39, BP-RP 0.78, plx 6.14 mas; plot `plots/uid235546.png`
- flags: centroid jump 0.446" (3.9 sigma, PA 292) not toward a Gaia neighbour | binary type in SIMBAD (**,SB*, BD+40  3447B) | Gaia DR3 NSS solution: nss_two_body_orbit
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 7 visits, 78 points; baseline W1 8.19, W1-W2 0.072; onset between MJD 59109 and 60041
- detector 2: excess 0.108 mag, z 10.8, jitter ratio 3.7
- field control: target step +0.072 (W1 +0.076); neighbours N=55, median +0.006, robust sigma 0.013, max +0.035; z = 5.3
- centroid: jump at onset 0.446" +- 0.115 (3.9 sigma, PA 292); largest consecutive-visit jump 0.370"; rms 0.304"; toward neighbour: none; expected shift if a neighbour were the source: 6.5" G10.1: 0.42"; 7.0" G20.7: 0.46"
- AllWISE 2010: W1-W2 -0.007, W2-W3 0.071 (W3 S/N 34.4), W3-W4 0.160 (W4 S/N 3.0), ext_flg 0, ph_qual AAAC: photosphere-like (W2-W3 < 0.5)
- Gaia: RUWE 0.98, ipd_frac_multi_peak 0, NSS nss_two_body_orbit, Teff 5930 K, logg 4.23, H-alpha pEW 0.097 nm, varclass none; M_G 4.33, -0.01 mag vs sequence (on the sequence); neighbours within 10": 6.5" PA175 G10.10 dG-0.29; 7.0" PA239 G20.69 dG+10.30
- SIMBAD (10"): BD+40  3447B [SB*; *,**,MIR,NIR,SB*] 0.27" refs=3; BD+40  3447A [*; *,**,MIR,NIR] 6.55" refs=2
- ASAS-SN: 799 points, cameras bB(g,154, d=+0.062); bb(V,304); br(g,319, d=-0.072); cB(g,22); change at onset (after-before, per-camera median) -0.005 mag; largest seasonal dimming 0.06 mag at MJD 59516
- dust: excess flux W1 14.38 mJy, W2 2.83 mJy, T = 8000 K (16-84%: 8000-8000) ratio bluer than an 8000 K blackbody (not dust-like)

### uid594661  [D2]  SURVIVOR
- position 112.65633 -32.20108; Gaia DR3 5592961049141313920; G 13.30, BP-RP 1.31, plx 4.28 mas; plot `plots/uid594661.png`
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association)
- NEOWISE: score refetch 0.61 (stored 0.61, reproduced True); dW2 0.029, dW1 -0.002, 19 visits, 143 points; baseline W1 10.79, W1-W2 0.189; onset between MJD 58417 and 58574
- detector 2: excess 0.254 mag, z 19.0, jitter ratio 3.4
- field control: target step +0.054 (W1 -0.004); neighbours N=173, median -0.003, robust sigma 0.013, max +0.056; z = 4.3
- centroid: jump at onset 0.026" +- 0.017 (1.5 sigma, PA 186); largest consecutive-visit jump 0.089"; rms 0.039"; toward neighbour: none; expected shift if a neighbour were the source: 2.7" G18.5: 0.13"; 7.4" G16.4: 0.36"
- AllWISE 2010: W1-W2 0.242, W2-W3 1.784 (W3 S/N 41.3), W3-W4 0.951 (W4 S/N 6.2), ext_flg 1, ph_qual AAAB: W3 excess only (W2-W3 > 1.0; debris-disk-like or blend)
- Gaia: RUWE 1.06, ipd_frac_multi_peak 0, NSS none, Teff 4606 K, logg 4.57, H-alpha pEW -0.027 nm, varclass RS(0.27); M_G 6.46, -0.13 mag vs sequence (on the sequence); neighbours within 10": 2.7" PA69 G18.48 dG+5.18; 7.4" PA47 G16.38 dG+3.08
- SIMBAD (10"): no object
- ASAS-SN: 1231 points, cameras bH(g,410, d=+0.014); bh(V,187); bl(g,443, d=+0.029); bp(g,191); change at onset (after-before, per-camera median) +0.021 mag; largest seasonal dimming 0.02 mag at MJD 59895
- dust: excess flux W1 0.14 mJy, W2 0.46 mJy, T = 553 K (16-84%: 360-756) 

### uid531152  [D2]  SURVIVOR
- position 28.13300 +76.82886; Gaia DR3 560335353427284224; G 13.59, BP-RP 1.45, plx 4.49 mas; plot `plots/uid531152.png`
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association)
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 11 visits, 95 points; baseline W1 11.00, W1-W2 0.042; onset between MJD 59250 and 59458
- detector 2: excess 0.104 mag, z 6.7, jitter ratio 4.0
- field control: target step +0.027 (W1 -0.001); neighbours N=75, median -0.004, robust sigma 0.010, max +0.018; z = 3.0
- centroid: jump at onset 0.092" +- 0.045 (2.1 sigma, PA 225); largest consecutive-visit jump 0.186"; rms 0.061"; toward neighbour: none; expected shift if a neighbour were the source: 9.5" G19.5: 0.23"
- AllWISE 2010: W1-W2 0.019, W2-W3 1.504 (W3 S/N 30.8), W3-W4 3.900 (W4 S/N 29.7), ext_flg 1, ph_qual AAAA: W3 excess only (W2-W3 > 1.0; debris-disk-like or blend)
- Gaia: RUWE 1.06, ipd_frac_multi_peak 0, NSS none, Teff 4560 K, logg 4.63, H-alpha pEW -0.045 nm, varclass none; M_G 6.85, -0.11 mag vs sequence (on the sequence); neighbours within 10": 9.5" PA179 G19.46 dG+5.87
- SIMBAD (10"): IRAS F01478+7634 [IR; IR] 7.61" refs=2
- ASAS-SN: 1457 points, cameras bC(g,328, d=-0.004); bD(g,287, d=-0.003); bc(V,143); bd(V,257); bs(g,229, d=-0.017); bt(g,213, d=-0.008); change at onset (after-before, per-camera median) -0.006 mag; largest seasonal dimming 0.01 mag at MJD 60498
- dust: excess flux W1 -0.14 mJy, W2 -0.08 mJy, T = n/a K (16-84%: n/a-n/a) no W2 excess flux after onset

### uid416726  [D2]  SURVIVOR
- position 335.19893 +63.27298; Gaia DR3 2205444407757988096; G 14.27, BP-RP 1.78, plx 4.95 mas; plot `plots/uid416726.png`
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association)
- NEOWISE: score refetch 0.14 (stored 0.14, reproduced True); dW2 0.013, dW1 -0.047, 14 visits, 183 points; baseline W1 11.09, W1-W2 0.215; onset between MJD 57221 and 57394
- detector 2: excess 0.239 mag, z 8.0, jitter ratio 6.3
- field control: target step +0.051 (W1 -0.034); neighbours N=141, median -0.004, robust sigma 0.019, max +0.323; z = 2.9
- centroid: jump at onset 0.067" +- 0.092 (0.7 sigma, PA 252); largest consecutive-visit jump 0.630"; rms 0.213"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.135, W2-W3 1.477 (W3 S/N 2.7), W3-W4 3.400 (W4 S/N 1.8), ext_flg 1, ph_qual AACU: W3 S/N < 5: no W2-W3 class
- Gaia: RUWE 1.03, ipd_frac_multi_peak 0, NSS none, Teff 4251 K, logg 4.63, H-alpha pEW -0.097 nm, varclass none; M_G 7.74, -0.11 mag vs sequence (on the sequence); neighbours within 10": none
- SIMBAD (10"): no object
- ASAS-SN: 1525 points, cameras bC(g,307); bD(g,308); bc(V,178, d=+0.018); bd(V,169, d=+0.001); bs(g,274); bt(g,289); change at onset (after-before, per-camera median) +0.010 mag; largest seasonal dimming 0.02 mag at MJD 59200
- dust: excess flux W1 -0.35 mJy, W2 0.49 mJy, T = 150 K (16-84%: 150-150) W1 excess <= 0: colder than ~150 K (upper limit)

### uid57667  [D2]  SURVIVOR
- position 110.17110 +14.30193; Gaia DR3 3166948080502189696; G 11.81, BP-RP 1.58, plx 9.84 mas; plot `plots/uid57667.png`
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association)
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 12 visits, 92 points; baseline W1 8.47, W1-W2 0.081; onset between MJD 58404 and 58562
- detector 2: excess 0.134 mag, z 6.8, jitter ratio 4.0
- field control: target step +0.025 (W1 +0.003); neighbours N=69, median +0.000, robust sigma 0.011, max +0.055; z = 2.3
- centroid: jump at onset 0.613" +- 0.316 (1.9 sigma, PA 354); largest consecutive-visit jump 0.912"; rms 0.301"; toward neighbour: none; expected shift if a neighbour were the source: 8.5" G11.6: 0.20"
- AllWISE 2010: W1-W2 0.090, W2-W3 -0.555 (W3 S/N 29.9), W3-W4 -0.283 (W4 S/N 2.2), ext_flg 1, ph_qual AAAC: photosphere-like (W2-W3 < 0.5)
- Gaia: RUWE 1.06, ipd_frac_multi_peak 0, NSS none, Teff 4333 K, logg 4.44, H-alpha pEW -0.073 nm, varclass none; M_G 6.77, -0.55 mag vs sequence (on the sequence); neighbours within 10": 8.5" PA192 G11.56 dG-0.25
- SIMBAD (10"): UCAC4 522-039395 [PM*; *,MIR,NIR,Opt,PM*] 1.05" refs=2; Gaia DR3 3166948080497672832 [*; *] 7.51" refs=1
- ASAS-SN: 941 points, cameras bC(g,197, d=-0.008); bG(g,109); bc(V,187); bk(g,160, d=+0.009); bo(g,111); bs(g,177, d=+0.000); change at onset (after-before, per-camera median) +0.000 mag; largest seasonal dimming 0.01 mag at MJD 60592
- dust: excess flux W1 -3.89 mJy, W2 2.34 mJy, T = 150 K (16-84%: 150-560) W1 excess <= 0: colder than ~150 K (upper limit)

### uid166090  [D2]  SURVIVOR
- position 265.12366 -30.86442; Gaia DR3 4055204702374928000; G 13.25, BP-RP 1.60, plx 6.94 mas; plot `plots/uid166090.png`
- flags: centroid jump 0.298" (3.1 sigma, PA 0) away from the neighbour(s) 4.7" PA174 G19.1, as expected when the target itself brightens in a blended WISE PSF | AllWISE ext_flg = 1 (extended or 2MASS XSC association)
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 12 visits, 109 points; baseline W1 9.92, W1-W2 0.183; onset between MJD 57828 and 58358
- detector 2: excess 0.235 mag, z 11.3, jitter ratio 3.6
- field control: target step +0.009 (W1 +0.027); neighbours N=108, median -0.022, robust sigma 0.028, max +0.073; z = 1.1
- centroid: jump at onset 0.298" +- 0.097 (3.1 sigma, PA 0); largest consecutive-visit jump 0.180"; rms 0.131"; toward neighbour: none; expected shift if a neighbour were the source: 4.7" G19.1: 0.04"; 5.7" G19.0: 0.05"; 6.8" G20.1: 0.06"
- AllWISE 2010: W1-W2 0.112, W2-W3 1.093 (W3 S/N 0.0), W3-W4 2.293 (W4 S/N 0.6), ext_flg 1, ph_qual AAUU: W3 S/N < 5: no W2-W3 class
- Gaia: RUWE 0.95, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW -0.009 nm, varclass none; M_G 7.46, +0.10 mag vs sequence (on the sequence); neighbours within 10": 4.7" PA174 G19.11 dG+5.86; 5.7" PA90 G18.97 dG+5.72; 6.8" PA227 G20.12 dG+6.87
- SIMBAD (10"): no object
- ASAS-SN: 1013 points, cameras bF(g,250); bf(V,196, d=-0.004); bj(g,243); bn(g,163); br(g,161); change at onset (after-before, per-camera median) -0.004 mag; largest seasonal dimming 0.01 mag at MJD 60229
- dust: excess flux W1 -0.38 mJy, W2 -0.45 mJy, T = n/a K (16-84%: n/a-n/a) no W2 excess flux after onset

### uid683552  [D2]  SURVIVOR
- position 266.74016 -27.96508; Gaia DR3 4057693202122149376; G 11.93, BP-RP 1.00, plx 4.04 mas; plot `plots/uid683552.png`
- flags: centroid jump 0.197" (3.4 sigma, PA 351) not toward a Gaia neighbour
- NEOWISE: score refetch 0.11 (stored 0.11, reproduced True); dW2 0.005, dW1 0.018, 16 visits, 104 points; baseline W1 8.49, W1-W2 0.076; onset between MJD 57635 and 57829
- detector 2: excess 0.129 mag, z 12.4, jitter ratio 4.3
- field control: target step +0.021 (W1 -0.000); neighbours N=94, median -0.006, robust sigma 0.028, max +0.199; z = 1.0
- centroid: jump at onset 0.197" +- 0.059 (3.4 sigma, PA 351); largest consecutive-visit jump 0.283"; rms 0.133"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.091, W2-W3 -0.122 (W3 S/N 5.7), W3-W4 1.421 (W4 S/N 0.5), ext_flg 0, ph_qual AABU: photosphere-like (W2-W3 < 0.5)
- Gaia: RUWE 0.96, ipd_frac_multi_peak 0, NSS none, Teff 5372 K, logg 4.32, H-alpha pEW 0.158 nm, varclass none; M_G 4.96, -0.52 mag vs sequence (on the sequence); neighbours within 10": none
- SIMBAD (10"): no object
- ASAS-SN: 2814 points, cameras bF(g,250); bG(g,247); bH(g,257); bf(V,195, d=-0.002); bg(V,175, d=-0.007); bj(g,242); bk(g,252); bl(g,243); bn(g,163); bo(g,178); bp(g,165); br(g,156); bs(g,137); bt(g,154); change at onset (after-before, per-camera median) -0.005 mag; largest seasonal dimming 0.01 mag at MJD 58007
- dust: excess flux W1 -0.88 mJy, W2 0.19 mJy, T = 150 K (16-84%: 150-659) W1 excess <= 0: colder than ~150 K (upper limit)

### uid678749  [D2]  SURVIVOR
- position 261.72695 -34.42002; Gaia DR3 5975848621838887424; G 13.34, BP-RP 1.49, plx 4.05 mas; plot `plots/uid678749.png`
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association)
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 9 visits, 88 points; baseline W1 10.59, W1-W2 0.054; onset between MJD 58356 and 58720
- detector 2: excess 0.114 mag, z 6.9, jitter ratio 4.4
- field control: target step -0.005 (W1 +0.017); neighbours N=118, median -0.010, robust sigma 0.029, max +0.095; z = 0.2
- centroid: jump at onset 0.070" +- 0.381 (0.2 sigma, PA 238); largest consecutive-visit jump 0.453"; rms 0.272"; toward neighbour: 7.4" PA251 G21.0 (angle 13 deg); expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.016, W2-W3 2.756 (W3 S/N 4.8), W3-W4 0.603 (W4 S/N -7.3), ext_flg 1, ph_qual AABU: W3 S/N < 5: no W2-W3 class
- Gaia: RUWE 0.92, ipd_frac_multi_peak 0, NSS none, Teff 5784 K, logg 4.48, H-alpha pEW 0.120 nm, varclass none; M_G 6.38, -0.69 mag vs sequence (on the sequence); neighbours within 10": 7.4" PA251 G21.03 dG+7.70
- SIMBAD (10"): no object
- ASAS-SN: 987 points, cameras bH(g,337, d=+0.014); bh(V,179); bl(g,296, d=+0.009); bp(g,175); change at onset (after-before, per-camera median) +0.012 mag; largest seasonal dimming 0.02 mag at MJD 60420
- dust: excess flux W1 -0.37 mJy, W2 -0.39 mJy, T = n/a K (16-84%: n/a-n/a) no W2 excess flux after onset

## Known/likely young stars (detector 2) (14)

### uid661720  [D2]  YOUNG
- position 85.41485 -1.78413; Gaia DR3 3216646250884327936; G 13.85, BP-RP 1.47, plx 4.09 mas; plot `plots/uid661720.png`
- **young:** SIMBAD young-star types Or*,TT*,Y*O (CVSO 183; CXOU J054139.4-014700)
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 7 visits, 80 points; baseline W1 11.15, W1-W2 0.604; onset between MJD 56922 and 57813
- detector 2: excess 0.665 mag, z 40.9, jitter ratio 14.1
- field control: target step +0.328 (W1 +0.286); neighbours N=26, median -0.003, robust sigma 0.034, max +0.219; z = 9.8
- centroid: jump at onset 0.187" +- 0.129 (1.5 sigma, PA 233); largest consecutive-visit jump 0.206"; rms 0.133"; toward neighbour: none; expected shift if a neighbour were the source: 3.3" G19.9: 0.85"
- AllWISE 2010: W1-W2 0.425, W2-W3 2.205 (W3 S/N -8.9), W3-W4 4.446 (W4 S/N -4.5), ext_flg 0, ph_qual ABUU: W3 S/N < 5: no W2-W3 class; W1-W2 > 0.25
- Gaia: RUWE 1.01, ipd_frac_multi_peak 0, NSS none, Teff 4532 K, logg 4.63, H-alpha pEW -0.032 nm, varclass none; M_G 6.91, -0.12 mag vs sequence (on the sequence); neighbours within 10": 3.3" PA322 G19.89 dG+6.04
- SIMBAD (10"): CVSO 183 [TT*; *,MIR,NIR,Or*,TT*,X,Y*O] 0.61" refs=16; CXOU J054139.4-014700 [Y*O; X,Y*O] 3.35" refs=4
- ASAS-SN: 1377 points, cameras bC(g,154); bG(g,220); bc(V,151, d=+0.028); be(V,38); bg(V,151, d=-0.016); bk(g,284); bo(g,216); bs(g,163); change at onset (after-before, per-camera median) +0.006 mag; largest seasonal dimming 0.02 mag at MJD 60640
- dust: excess flux W1 2.49 mJy, W2 3.06 mJy, T = 1039 K (16-84%: 808-1396) 

### uid280237  [D2]  YOUNG
- position 52.07800 +48.66327; Gaia DR3 249236647249997696; G 12.54, BP-RP 1.24, plx 5.76 mas; plot `plots/uid280237.png`
- **young:** SIMBAD young-star types Y*O (V* V488 Per)
- flags: AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 1.03 (stored 1.03, reproduced True); dW2 0.349, dW1 0.324, 18 visits, 213 points; baseline W1 9.36, W1-W2 0.788; onset between MJD 58514 and 58722
- detector 2: excess 0.851 mag, z 69.6, jitter ratio 17.7
- field control: target step +1.204 (W1 +0.973); neighbours N=104, median -0.001, robust sigma 0.013, max +0.056; z = 90.3
- centroid: jump at onset 0.006" +- 0.036 (0.2 sigma, PA 356); largest consecutive-visit jump 0.078"; rms 0.038"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.781, W2-W3 1.648 (W3 S/N 63.8), W3-W4 2.020 (W4 S/N 30.6), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 0.90, ipd_frac_multi_peak 0, NSS none, Teff 5102 K, logg 4.63, H-alpha pEW -0.065 nm, varclass RS(0.13); M_G 6.34, -0.01 mag vs sequence (on the sequence); neighbours within 10": none
- SIMBAD (10"): V* V488 Per [BY*; *,BY*,MIR,NIR,Opt,V*,Y*O] 0.56" refs=60
- ASAS-SN: 633 points, cameras bA(g,216, d=+0.017); ba(V,188); bq(g,229, d=+0.031); change at onset (after-before, per-camera median) +0.024 mag; largest seasonal dimming 0.04 mag at MJD 59095
- dust: excess flux W1 40.71 mJy, W2 50.16 mJy, T = 1037 K (16-84%: 1023-1050) 

### uid78873  [D2]  YOUNG
- position 212.04213 -41.39804; Gaia DR3 6110141563309613056; G 11.61, BP-RP 1.67, plx 8.90 mas; plot `plots/uid78873.png`
- **young:** SIMBAD young-star types TT*,Y*? (CD-40  8434)
- flags: 1.21 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.19 mag (MJD 59715)
- NEOWISE: score refetch 2.71 (stored 2.71, reproduced True); dW2 1.026, dW1 0.802, 17 visits, 158 points; baseline W1 8.59, W1-W2 0.167; onset between MJD 57057 and 57234
- detector 2: excess 0.209 mag, z 8.8, jitter ratio 13.3
- field control: target step +0.888 (W1 +0.670); neighbours N=84, median -0.003, robust sigma 0.011, max +0.059; z = 77.5
- centroid: jump at onset 0.011" +- 0.017 (0.7 sigma, PA 148); largest consecutive-visit jump 0.036"; rms 0.032"; toward neighbour: none; expected shift if a neighbour were the source: 2.4" G15.5: 1.34"; 8.1" G19.2: 4.50"; 9.3" G18.3: 5.22"
- AllWISE 2010: W1-W2 0.322, W2-W3 1.993 (W3 S/N 68.2), W3-W4 2.359 (W4 S/N 53.9), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.39, ipd_frac_multi_peak 0, NSS none, Teff 4138 K, logg 4.15, H-alpha pEW -0.173 nm, varclass none; M_G 6.35, -1.21 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 2.4" PA12 G15.51 dG+3.90; 8.1" PA205 G19.22 dG+7.61; 9.3" PA14 G18.27 dG+6.66
- SIMBAD (10"): CD-40  8434 [TT*; *,IR,MIR,NIR,Ro*,TT*,V*,X,Y*?] 0.61" refs=546; PDS  70d [Pl?; Pl?] 0.61" refs=8; CD-40  8434c [Pl; *,Pl,Pl?] 0.61" refs=240; CD-40  8434b [Pl; *,Pl,Pl?] 0.61" refs=295; Gaia DR3 6110141563309613184 [*; *] 2.49" refs=4
- ASAS-SN: 1380 points, cameras bG(g,373); be(V,101, d=+0.032); bg(V,223); bk(g,383); bo(g,300); change at onset (after-before, per-camera median) +0.032 mag; largest seasonal dimming 0.19 mag at MJD 59715
- dust: excess flux W1 92.65 mJy, W2 82.57 mJy, T = 1537 K (16-84%: 1498-1577) 

### uid312613  [D2]  YOUNG
- position 164.12614 -77.19427; Gaia DR3 5201388292344009984; G 12.54, BP-RP 1.96, plx 5.53 mas; plot `plots/uid312613.png`
- **young:** SIMBAD young-star types Or*,Y*O (V* SY Cha)
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | 2.08 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | optical dimming +0.093 mag after the infrared onset (debris transit signature) | largest seasonal optical dimming 0.15 mag (MJD 58085)
- NEOWISE: score refetch 2.41 (stored 2.41, reproduced True); dW2 0.351, dW1 0.249, 22 visits, 499 points; baseline W1 8.65, W1-W2 0.458; onset between MJD 57967 and 58166
- detector 2: excess 0.447 mag, z 12.2, jitter ratio 11.2
- field control: target step +0.165 (W1 +0.078); neighbours N=96, median -0.001, robust sigma 0.008, max +0.038; z = 20.4
- centroid: jump at onset 0.014" +- 0.014 (0.9 sigma, PA 42); largest consecutive-visit jump 0.048"; rms 0.024"; toward neighbour: 8.1" PA85 G18.6 (angle 43 deg); expected shift if a neighbour were the source: 8.1" G18.6: 1.15"
- AllWISE 2010: W1-W2 0.533, W2-W3 2.360 (W3 S/N 70.1), W3-W4 2.223 (W4 S/N 55.4), ext_flg 1, ph_qual BAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.37, ipd_frac_multi_peak 0, NSS none, Teff 6003 K, logg 4.21, H-alpha pEW -0.544 nm, varclass none; M_G 6.25, -2.08 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 8.1" PA85 G18.62 dG+6.09
- SIMBAD (10"): V* SY Cha [Or*; *,Em*,IR,MIR,NIR,Or*,V*,X,Y*O] 0.38" refs=194
- ASAS-SN: 2366 points, cameras bE(g,368); bF(g,274); be(V,270, d=+0.110); bf(V,166, d=+0.076); bi(g,476); bj(g,368); bm(g,257); bn(g,187); change at onset (after-before, per-camera median) +0.093 mag; largest seasonal dimming 0.15 mag at MJD 58085
- dust: excess flux W1 13.21 mJy, W2 18.30 mJy, T = 932 K (16-84%: 879-990) 

### V836 Tau (uid252570)  [CONTROL+D2]  YOUNG
- position 75.77751 +25.38870; Gaia DR3 3420008412568724736; G 12.64, BP-RP 2.11, plx 5.99 mas; plot `plots/V836_Tau_uid252570_.png`
- **young:** SIMBAD young-star types Or*,TT*,TT?,Y*?,Y*O (V* V836 Tau) | Gaia DR3 variability class YSO(0.83)
- flags: 2.27 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | possible optical brightening at onset (-0.045 mag, one camera only)
- NEOWISE: score refetch 1.57 (stored 1.57, reproduced True); dW2 0.286, dW1 0.325, 20 visits, 187 points; baseline W1 8.42, W1-W2 0.425; onset between MJD 57641 and 57806
- detector 2: excess 0.377 mag, z 10.1, jitter ratio 15.4
- field control: target step +0.210 (W1 +0.198); neighbours N=99, median -0.003, robust sigma 0.011, max +0.164; z = 19.2
- centroid: jump at onset 0.009" +- 0.015 (0.6 sigma, PA 229); largest consecutive-visit jump 0.075"; rms 0.027"; toward neighbour: none; expected shift if a neighbour were the source: 8.8" G20.2: 1.55"
- AllWISE 2010: W1-W2 0.466, W2-W3 1.801 (W3 S/N 69.5), W3-W4 2.069 (W4 S/N 44.4), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.17, ipd_frac_multi_peak 0, NSS none, Teff 5302 K, logg 4.16, H-alpha pEW -0.770 nm, varclass YSO(0.83); M_G 6.53, -2.27 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 8.8" PA107 G20.21 dG+7.56
- SIMBAD (10"): V* V836 Tau [TT*; *,BY*,Em*,IR,MIR,NIR,Or*,TT*,TT?,V*,X,Y*?,Y*O] 0.28" refs=249; USNO-B1.0 1153-00064776 [*; *] 7.05" refs=1
- ASAS-SN: 803 points, cameras bB(g,101); bF(g,94); bb(V,205, d=-0.045); bj(g,99); bn(g,114); br(g,190); change at onset (after-before, per-camera median) -0.045 mag; largest seasonal dimming 0.09 mag at MJD 58867
- dust: excess flux W1 45.49 mJy, W2 36.20 mJy, T = 1882 K (16-84%: 1761-2023) 

### uid162954  [D2]  YOUNG
- position 239.77012 -24.37982; Gaia DR3 6236191156867993344; G 13.04, BP-RP 1.97, plx 6.99 mas; plot `plots/uid162954.png`
- **young:** SIMBAD young-star types Or*,Y*?,Y*O (WRAY 15-1401) | Gaia DR3 variability class YSO(0.84)
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | 1.11 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | possible optical brightening at onset (-0.053 mag, one camera only) | largest seasonal optical dimming 0.27 mag (MJD 58191)
- NEOWISE: score refetch 1.39 (stored 1.39, reproduced True); dW2 0.141, dW1 0.104, 20 visits, 140 points; baseline W1 8.74, W1-W2 0.421; onset between MJD 57610 and 57807
- detector 2: excess 0.406 mag, z 11.0, jitter ratio 8.7
- field control: target step +0.221 (W1 +0.219); neighbours N=93, median -0.003, robust sigma 0.013, max +0.073; z = 17.8
- centroid: jump at onset 0.013" +- 0.016 (0.8 sigma, PA 75); largest consecutive-visit jump 0.067"; rms 0.033"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.523, W2-W3 2.236 (W3 S/N 71.7), W3-W4 1.925 (W4 S/N 41.8), ext_flg 1, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.37, ipd_frac_multi_peak 0, NSS none, Teff 3718 K, logg 4.04, H-alpha pEW -2.760 nm, varclass YSO(0.84); M_G 7.27, -1.11 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): WRAY 15-1401 [Or*; *,Em*,MIR,NIR,Opt,Or*,V*,Y*?,Y*O] 0.44" refs=18
- ASAS-SN: 1149 points, cameras bG(g,236); be(V,103); bg(V,182, d=-0.053); bk(g,301); bo(g,218); bs(g,109); change at onset (after-before, per-camera median) -0.053 mag; largest seasonal dimming 0.27 mag at MJD 58191
- dust: excess flux W1 13.76 mJy, W2 14.30 mJy, T = 1245 K (16-84%: 1096-1447) 

### uid283125  [D2]  YOUNG
- position 78.14266 +25.98013; Gaia DR3 3420824426291884672; G 12.98, BP-RP 2.07, plx 5.74 mas; plot `plots/uid283125.png`
- **young:** SIMBAD young-star types TT?,Y*? (ATO J078.1426+25.9801) | Gaia DR3 variability class YSO(0.24)
- flags: 1.89 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 0.33 (stored 0.33, reproduced True); dW2 0.053, dW1 0.046, 21 visits, 166 points; baseline W1 9.01, W1-W2 0.372; onset between MJD 57084 and 57278
- detector 2: excess 0.334 mag, z 8.7, jitter ratio 11.2
- field control: target step +0.219 (W1 +0.179); neighbours N=121, median -0.005, robust sigma 0.013, max +0.040; z = 16.8
- centroid: jump at onset 0.016" +- 0.019 (0.8 sigma, PA 98); largest consecutive-visit jump 0.055"; rms 0.033"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.392, W2-W3 1.981 (W3 S/N 72.6), W3-W4 1.744 (W4 S/N 34.0), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.04, ipd_frac_multi_peak 0, NSS none, Teff 5631 K, logg 4.28, H-alpha pEW -0.363 nm, varclass YSO(0.24); M_G 6.78, -1.89 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): ATO J078.1426+25.9801 [TT?; *,NIR,Opt,Pu*,TT?,Y*?] 0.29" refs=6
- ASAS-SN: 818 points, cameras bB(g,113); bF(g,94); bb(V,205, d=-0.002); bj(g,106); bn(g,110); br(g,190); change at onset (after-before, per-camera median) -0.002 mag; largest seasonal dimming 0.07 mag at MJD 57693
- dust: excess flux W1 7.94 mJy, W2 8.92 mJy, T = 1139 K (16-84%: 1035-1259) 

### uid190587  [D2]  YOUNG
- position 245.39456 -26.20757; Gaia DR3 6048501945023784704; G 12.58, BP-RP 1.79, plx 6.62 mas; plot `plots/uid190587.png`
- **young:** SIMBAD young-star types Or*,TT* (Haro 1-1) | Gaia DR3 variability class YSO(0.56)
- flags: 1.20 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | possible optical brightening at onset (-0.095 mag, one camera only)
- NEOWISE: score refetch 1.80 (stored 1.80, reproduced True); dW2 0.206, dW1 0.143, 11 visits, 99 points; baseline W1 8.38, W1-W2 0.322; onset between MJD 57080 and 57256
- detector 2: excess 0.344 mag, z 11.4, jitter ratio 10.9
- field control: target step +0.172 (W1 +0.150); neighbours N=132, median -0.007, robust sigma 0.012, max +0.088; z = 14.6
- centroid: jump at onset 0.059" +- 0.028 (2.1 sigma, PA 228); largest consecutive-visit jump 0.061"; rms 0.046"; toward neighbour: 4.9" PA263 G20.4 (angle 36 deg); expected shift if a neighbour were the source: 4.9" G20.4: 0.71"; 6.5" G20.2: 0.95"
- AllWISE 2010: W1-W2 0.353, W2-W3 2.100 (W3 S/N 67.5), W3-W4 2.715 (W4 S/N 45.4), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.18, ipd_frac_multi_peak 0, NSS none, Teff 5778 K, logg 4.36, H-alpha pEW -4.886 nm, varclass YSO(0.56); M_G 6.68, -1.20 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 4.9" PA263 G20.42 dG+7.84; 6.5" PA284 G20.21 dG+7.63
- SIMBAD (10"): Haro 1-1 [Or*; *,Em*,MIR,NIR,Or*,Ro*,TT*,V*] 0.37" refs=73
- ASAS-SN: 1070 points, cameras bG(g,255); be(V,102, d=-0.095); bg(V,144); bk(g,268); bo(g,192); bs(g,109); change at onset (after-before, per-camera median) -0.095 mag; largest seasonal dimming 0.08 mag at MJD 60390
- dust: excess flux W1 25.40 mJy, W2 22.02 mJy, T = 1608 K (16-84%: 1389-1920) 

### uid144763  [D2]  YOUNG
- position 242.25312 -19.14808; Gaia DR3 6245777283349430912; G 12.89, BP-RP 2.19, plx 7.28 mas; plot `plots/uid144763.png`
- **young:** SIMBAD young-star types Or*,TT*,Y*?,Y*O ([PGZ2001] J160900.7-190852) | Gaia DR3 variability class YSO(0.87)
- flags: 1.84 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 0.82 (stored 0.82, reproduced True); dW2 0.152, dW1 0.141, 20 visits, 160 points; baseline W1 8.81, W1-W2 0.272; onset between MJD 58699 and 58903
- detector 2: excess 0.209 mag, z 5.4, jitter ratio 16.0
- field control: target step +0.218 (W1 +0.175); neighbours N=62, median +0.000, robust sigma 0.016, max +0.032; z = 13.7
- centroid: jump at onset 0.044" +- 0.021 (2.1 sigma, PA 313); largest consecutive-visit jump 0.057"; rms 0.029"; toward neighbour: 6.7" PA276 G17.8 (angle 37 deg); expected shift if a neighbour were the source: 6.7" G17.8: 1.23"
- AllWISE 2010: W1-W2 0.252, W2-W3 2.276 (W3 S/N 73.1), W3-W4 2.546 (W4 S/N 49.8), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.40, ipd_frac_multi_peak 1, NSS none, Teff 3880 K, logg 4.07, H-alpha pEW -0.781 nm, varclass YSO(0.87); M_G 7.20, -1.84 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 6.7" PA276 G17.78 dG+4.88
- SIMBAD (10"): [PGZ2001] J160900.7-190852 [TT*; *,MIR,NIR,Or*,Ro*,TT*,Y*?,Y*O] 0.43" refs=94
- ASAS-SN: 2208 points, cameras bC(g,65, d=-0.017); bD(g,55, d=+0.066); bG(g,187, d=+0.052); bH(g,174, d=+0.043); bc(V,97); bd(V,77); be(V,60); bf(V,50); bg(V,135); bh(V,139); bk(g,259, d=+0.006); bl(g,258, d=+0.017); bo(g,193, d=+0.007); bp(g,203, d=+0.031); bs(g,137, d=-0.027); bt(g,119, d=-0.007); change at onset (after-before, per-camera median) +0.012 mag; largest seasonal dimming 0.06 mag at MJD 60486
- dust: excess flux W1 10.36 mJy, W2 9.94 mJy, T = 1380 K (16-84%: 1250-1541) 

### uid338719  [D2]  YOUNG
- position 17.42536 +27.95048; Gaia DR3 307981178401165184; G 11.34, BP-RP 0.96, plx 5.37 mas; plot `plots/uid338719.png`
- **young:** SIMBAD young-star types Ae* (V* RZ Psc)
- flags: binary type in SIMBAD (**, V* RZ Psc B) | AllWISE ext_flg = 1 (extended or 2MASS XSC association) | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.31 mag (MJD 60487)
- NEOWISE: score refetch 0.01 (stored 0.01, reproduced True); dW2 0.001, dW1 -0.007, 20 visits, 196 points; baseline W1 9.21, W1-W2 0.431; onset between MJD 56673 and 56862
- detector 2: excess 0.481 mag, z 46.3, jitter ratio 5.8
- field control: target step +0.166 (W1 +0.152); neighbours N=26, median -0.002, robust sigma 0.025, max +0.037; z = 6.7
- centroid: jump at onset 0.040" +- 0.047 (0.9 sigma, PA 315); largest consecutive-visit jump 0.051"; rms 0.039"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.453, W2-W3 2.711 (W3 S/N 67.7), W3-W4 1.178 (W4 S/N 39.5), ext_flg 1, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.13, ipd_frac_multi_peak 0, NSS none, Teff 5815 K, logg 4.47, H-alpha pEW 0.075 nm, varclass none; M_G 4.99, -0.32 mag vs sequence (on the sequence); neighbours within 10": none
- SIMBAD (10"): V* RZ Psc B [LM*; LM*,V*] 0.36" refs=2; V* RZ Psc [Ae*; *,**,Ae*,MIR,NIR,V*] 0.48" refs=79
- ASAS-SN: 3419 points, cameras bB(g,146); bC(g,248); bD(g,259); bF(g,82); bG(g,84); bH(g,79); bb(V,454, d=-0.029); bc(V,267); bd(V,411); bg(V,35); bj(g,128); bk(g,134); bl(g,129); bn(g,116); bo(g,107); bp(g,110); br(g,213); bs(g,208); bt(g,209); change at onset (after-before, per-camera median) -0.029 mag; largest seasonal dimming 0.31 mag at MJD 60487
- dust: excess flux W1 7.75 mJy, W2 8.39 mJy, T = 1187 K (16-84%: 1104-1283) 

### uid122962  [D2]  YOUNG
- position 207.05427 -52.16970; Gaia DR3 6066287438960606336; G 12.68, BP-RP 1.94, plx 7.69 mas; plot `plots/uid122962.png`
- **young:** SIMBAD young-star types Y*? (UCAC4 190-084909) | Gaia DR3 variability class YSO(0.56)
- flags: 1.19 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 0.15 (stored 0.15, reproduced True); dW2 0.014, dW1 0.005, 7 visits, 62 points; baseline W1 8.89, W1-W2 0.300; onset between MJD 57058 and 57235
- detector 2: excess 0.292 mag, z 8.1, jitter ratio 6.7
- field control: target step +0.060 (W1 +0.057); neighbours N=184, median -0.003, robust sigma 0.010, max +0.043; z = 6.3
- centroid: jump at onset 0.056" +- 0.027 (2.1 sigma, PA 297); largest consecutive-visit jump 0.085"; rms 0.031"; toward neighbour: none; expected shift if a neighbour were the source: 8.6" G18.1: 0.46"
- AllWISE 2010: W1-W2 0.359, W2-W3 1.256 (W3 S/N 66.0), W3-W4 1.639 (W4 S/N 33.2), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.31, ipd_frac_multi_peak 0, NSS none, Teff 5363 K, logg 4.40, H-alpha pEW -0.753 nm, varclass YSO(0.56); M_G 7.11, -1.19 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 8.6" PA240 G18.08 dG+5.40
- SIMBAD (10"): UCAC4 190-084909 [Y*?; *,MIR,NIR,Y*?] 0.52" refs=5
- ASAS-SN: 0 points, cameras n/a; change at onset (after-before, per-camera median) n/a mag; largest seasonal dimming n/a mag at MJD n/a
- dust: excess flux W1 4.31 mJy, W2 0.58 mJy, T = 8000 K (16-84%: 8000-8000) ratio bluer than an 8000 K blackbody (not dust-like)
- checks missing: ASAS-SN (no source)

### uid220686  [D2]  YOUNG
- position 239.34998 -42.66804; Gaia DR3 5994747367001754240; G 12.97, BP-RP 2.13, plx 6.29 mas; plot `plots/uid220686.png`
- **young:** SIMBAD young-star types Or*,TT*,Y*?,Y*O (WRAY 15-1388) | Gaia DR3 variability class YSO(0.76)
- flags: 1.88 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | not plain dust: optical brightening -0.053 mag (per-camera -0.053,-0.011,-0.124) together with the infrared rise | largest seasonal optical dimming 0.16 mag (MJD 60519)
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 11 visits, 89 points; baseline W1 8.19, W1-W2 0.444; onset between MJD 59637 and 60001
- detector 2: excess 0.393 mag, z 10.6, jitter ratio 12.8
- field control: target step +0.117 (W1 +0.069); neighbours N=170, median -0.000, robust sigma 0.021, max +0.067; z = 5.6
- centroid: jump at onset 0.003" +- 0.019 (0.2 sigma, PA 219); largest consecutive-visit jump 0.051"; rms 0.023"; toward neighbour: 8.4" PA182 G19.5 (angle 37 deg); 9.2" PA180 G19.1 (angle 39 deg); expected shift if a neighbour were the source: 2.3" G18.7: 0.23"; 5.4" G19.4: 0.55"; 8.4" G19.5: 0.86"; 9.2" G19.1: 0.94"
- AllWISE 2010: W1-W2 0.462, W2-W3 2.120 (W3 S/N 77.0), W3-W4 1.977 (W4 S/N 51.1), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.01, ipd_frac_multi_peak 0, NSS none, Teff 6479 K, logg 4.25, H-alpha pEW -3.250 nm, varclass YSO(0.76); M_G 6.96, -1.88 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 2.3" PA316 G18.72 dG+5.75; 5.4" PA359 G19.41 dG+6.44; 8.4" PA182 G19.51 dG+6.54; 9.2" PA180 G19.13 dG+6.15
- SIMBAD (10"): WRAY 15-1388 [TT*; *,Em*,MIR,NIR,Or*,TT*,Y*?,Y*O] 0.41" refs=24
- ASAS-SN: 1064 points, cameras bH(g,307, d=-0.053); bh(V,194); bl(g,391, d=-0.011); bp(g,172, d=-0.124); change at onset (after-before, per-camera median) -0.053 mag; largest seasonal dimming 0.16 mag at MJD 60519
- dust: excess flux W1 18.69 mJy, W2 27.42 mJy, T = 889 K (16-84%: 829-958) 

### uid220781  [D2]  YOUNG
- position 239.43169 -41.72728; Gaia DR3 5995233114932232064; G 12.03, BP-RP 1.75, plx 6.29 mas; plot `plots/uid220781.png`
- **young:** SIMBAD young-star types Y*?,Y*O (1RXS J155744.8-414353) | Gaia DR3 variability class YSO(0.79)
- flags: 1.73 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 0.67 (stored 0.67, reproduced True); dW2 0.078, dW1 0.064, 8 visits, 80 points; baseline W1 8.21, W1-W2 0.407; onset between MJD 57443 and 57810
- detector 2: excess 0.437 mag, z 15.6, jitter ratio 10.4
- field control: target step +0.039 (W1 -0.013); neighbours N=162, median -0.002, robust sigma 0.012, max +0.054; z = 3.4
- centroid: jump at onset 0.036" +- 0.033 (1.1 sigma, PA 306); largest consecutive-visit jump 0.071"; rms 0.034"; toward neighbour: none; expected shift if a neighbour were the source: 4.2" G18.5: 0.15"; 4.5" G17.1: 0.16"; 9.5" G20.7: 0.34"; 9.7" G18.4: 0.35"
- AllWISE 2010: W1-W2 0.431, W2-W3 1.695 (W3 S/N 68.1), W3-W4 1.458 (W4 S/N 39.5), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 0.97, ipd_frac_multi_peak 0, NSS none, Teff nan K, logg nan, H-alpha pEW -0.405 nm, varclass YSO(0.79); M_G 6.03, -1.73 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 4.2" PA89 G18.48 dG+6.45; 4.5" PA103 G17.11 dG+5.07; 9.5" PA213 G20.69 dG+8.65; 9.7" PA64 G18.43 dG+6.39
- SIMBAD (10"): 1RXS J155744.8-414353 [Y*O; *,MIR,NIR,X,Y*?,Y*O] 0.42" refs=9
- ASAS-SN: 1057 points, cameras bH(g,305); bh(V,192, d=+0.005); bl(g,388); bp(g,172); change at onset (after-before, per-camera median) +0.005 mag; largest seasonal dimming 0.05 mag at MJD 58596
- dust: excess flux W1 8.91 mJy, W2 9.62 mJy, T = 1191 K (16-84%: 1013-1439) 

### uid171672  [D2]  YOUNG
- position 242.52086 -21.54230; Gaia DR3 6242970711201462144; G 12.49, BP-RP 1.90, plx 6.86 mas; plot `plots/uid171672.png`
- **young:** SIMBAD young-star types Or*,TT*,Y*?,Y*O (2MASS J16100501-2132318) | Gaia DR3 variability class YSO(0.80)
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | 1.50 mag above the main sequence at its colour
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 19 visits, 144 points; baseline W1 8.47, W1-W2 0.287; onset between MJD 58699 and 58904
- detector 2: excess 0.290 mag, z 8.4, jitter ratio 13.5
- field control: target step -0.042 (W1 -0.049); neighbours N=80, median +0.001, robust sigma 0.014, max +0.048; z = -3.0
- centroid: jump at onset 0.016" +- 0.019 (0.8 sigma, PA 237); largest consecutive-visit jump 0.079"; rms 0.031"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.247, W2-W3 1.974 (W3 S/N 64.5), W3-W4 2.610 (W4 S/N 52.4), ext_flg 1, ph_qual AAAA: W3 excess only (W2-W3 > 1.0; debris-disk-like or blend)
- Gaia: RUWE 1.30, ipd_frac_multi_peak 0, NSS none, Teff 5903 K, logg 4.32, H-alpha pEW -1.769 nm, varclass YSO(0.80); M_G 6.67, -1.50 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": none
- SIMBAD (10"): 2MASS J16100501-2132318 [TT*; *,Em*,MIR,NIR,Or*,Ro*,TT*,Y*?,Y*O] 0.43" refs=33
- ASAS-SN: 1038 points, cameras bA(g,57, d=+0.113); bE(g,185, d=+0.013); ba(V,84); be(V,194); bi(g,229, d=-0.004); bm(g,183, d=+0.000); bq(g,106, d=+0.046); change at onset (after-before, per-camera median) +0.013 mag; largest seasonal dimming 0.03 mag at MJD 58369
- dust: excess flux W1 6.47 mJy, W2 5.71 mJy, T = 1560 K (16-84%: 1230-2154) 

## Killed (6)

### uid358951  [D2]  KILLED
- position 167.22331 -75.36000; Gaia DR3 5225533537629764736; G 13.82, BP-RP 2.11, plx 5.25 mas; plot `plots/uid358951.png`
- **KILL:** blend: Gaia neighbour within 6" only 1.00 mag fainter in G (4.9" PA257 G14.82 dG+1.00; 5.8" PA313 G18.32 dG+4.49; 8.1" PA276 G17.06 dG+3.24)
- **young:** SIMBAD young-star types Or*,TT*,Y*? (V* PU Car) | Gaia DR3 variability class YSO(0.41)
- flags: 1.38 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | not plain dust: optical brightening -0.020 mag (per-camera -0.017,-0.020,-0.064,+0.008,-0.027) together with the infrared rise | largest seasonal optical dimming 0.11 mag (MJD 60418)
- NEOWISE: score refetch 1.54 (stored 1.54, reproduced True); dW2 0.224, dW1 0.180, 19 visits, 279 points; baseline W1 8.81, W1-W2 0.352; onset between MJD 59258 and 59622
- detector 2: excess 0.304 mag, z 8.1, jitter ratio 14.0
- field control: target step +0.300 (W1 +0.257); neighbours N=107, median -0.003, robust sigma 0.011, max +0.038; z = 27.3
- centroid: jump at onset 0.040" +- 0.020 (2.0 sigma, PA 67); largest consecutive-visit jump 0.076"; rms 0.034"; toward neighbour: none; expected shift if a neighbour were the source: 4.9" G14.8: 1.18"; 5.8" G18.3: 1.39"; 8.1" G17.1: 1.96"
- AllWISE 2010: W1-W2 0.411, W2-W3 1.207 (W3 S/N 68.8), W3-W4 2.091 (W4 S/N 38.2), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.40, ipd_frac_multi_peak 0, NSS none, Teff 6504 K, logg 4.48, H-alpha pEW -3.010 nm, varclass YSO(0.41); M_G 7.42, -1.38 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 4.9" PA257 G14.82 dG+1.00; 5.8" PA313 G18.32 dG+4.49; 8.1" PA276 G17.06 dG+3.24
- SIMBAD (10"): V* PU Car [TT*; *,LP?,MIR,NIR,Or*,TT*,V*,V*?,Y*?] 0.36" refs=40
- ASAS-SN: 2111 points, cameras bF(g,273, d=-0.017); bG(g,328, d=-0.020); be(V,100); bf(V,163); bg(V,168); bk(g,440, d=-0.064); bl(g,400, d=+0.008); bo(g,239, d=-0.027); change at onset (after-before, per-camera median) -0.020 mag; largest seasonal dimming 0.11 mag at MJD 60418
- dust: excess flux W1 24.96 mJy, W2 23.23 mJy, T = 1440 K (16-84%: 1366-1522) 

### uid468346  [D2]  KILLED
- position 58.83067 +47.35326; Gaia DR3 246657089893122176; G 13.08, BP-RP 1.29, plx 4.72 mas; plot `plots/uid468346.png`
- **KILL:** blend: Gaia neighbour within 6" only 2.88 mag fainter in G (4.0" PA96 G15.96 dG+2.88)
- flags: AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 0.99 (stored 0.99, reproduced True); dW2 0.121, dW1 0.129, 20 visits, 224 points; baseline W1 9.87, W1-W2 0.618; onset between MJD 57797 and 57995
- detector 2: excess 0.682 mag, z 51.1, jitter ratio 11.9
- field control: target step +0.257 (W1 +0.230); neighbours N=151, median -0.005, robust sigma 0.012, max +0.045; z = 22.1
- centroid: jump at onset 0.037" +- 0.022 (1.7 sigma, PA 323); largest consecutive-visit jump 0.081"; rms 0.034"; toward neighbour: none; expected shift if a neighbour were the source: 4.0" G16.0: 0.83"
- AllWISE 2010: W1-W2 0.697, W2-W3 1.118 (W3 S/N 52.0), W3-W4 0.176 (W4 S/N 6.5), ext_flg 0, ph_qual AAAB: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.01, ipd_frac_multi_peak 0, NSS none, Teff 4804 K, logg 4.57, H-alpha pEW 0.014 nm, varclass SOLAR_LIKE(0.72); M_G 6.45, -0.05 mag vs sequence (on the sequence); neighbours within 10": 4.0" PA96 G15.96 dG+2.88
- SIMBAD (10"): no object
- ASAS-SN: 623 points, cameras bC(g,251); bc(V,191, d=+0.009); bs(g,181); change at onset (after-before, per-camera median) +0.009 mag; largest seasonal dimming 0.01 mag at MJD 58026
- dust: excess flux W1 5.15 mJy, W2 5.20 mJy, T = 1288 K (16-84%: 1190-1405) 

### uid361168  [D2]  KILLED
- position 271.96538 +5.86311; Gaia DR3 4471872295941149056; G 12.33, BP-RP 0.88, plx 5.24 mas; plot `plots/uid361168.png`
- **KILL:** cataclysmic variable / X-ray binary in SIMBAD (CV*, V* V426 Oph)
- flags: binary type in SIMBAD (SB*, V* V426 Oph) | largest seasonal optical dimming 0.54 mag (MJD 59480)
- NEOWISE: score refetch 0.06 (stored 0.06, reproduced True); dW2 0.008, dW1 0.035, 20 visits, 195 points; baseline W1 10.19, W1-W2 0.081; onset between MJD 60191 and 60391
- detector 2: excess 0.126 mag, z 12.1, jitter ratio 8.4
- field control: target step +0.299 (W1 +0.271); neighbours N=143, median +0.001, robust sigma 0.014, max +0.100; z = 21.1
- centroid: jump at onset 0.009" +- 0.015 (0.6 sigma, PA 168); largest consecutive-visit jump 0.016"; rms 0.023"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.071, W2-W3 0.392 (W3 S/N 21.8), W3-W4 0.936 (W4 S/N 2.8), ext_flg 0, ph_qual AAAC: photosphere-like (W2-W3 < 0.5)
- Gaia: RUWE 1.24, ipd_frac_multi_peak 0, NSS none, Teff 5963 K, logg 4.72, H-alpha pEW -1.047 nm, varclass none; M_G 5.92, +1.02 mag vs sequence (below the sequence); neighbours within 10": none
- SIMBAD (10"): V* V426 Oph [CV*; *,CV*,NIR,SB*,V*,X] 0.60" refs=182
- ASAS-SN: 1042 points, cameras bC(g,224, d=+0.154); bG(g,130, d=-0.012); bc(V,222); bk(g,162, d=-0.212); bo(g,109, d=-0.413); bs(g,195, d=+0.095); change at onset (after-before, per-camera median) -0.012 mag; largest seasonal dimming 0.54 mag at MJD 59480
- dust: excess flux W1 4.03 mJy, W2 2.84 mJy, T = 2539 K (16-84%: 1882-4000) 

### uid41546  [D2]  KILLED
- position 310.03848 -0.87079; Gaia DR3 4226332451596335616; G 10.95, BP-RP 1.22, plx 10.91 mas; plot `plots/uid41546.png`
- **KILL:** cataclysmic variable / X-ray binary in SIMBAD (CV*, V* AE Aqr)
- flags: centroid jump 0.059" (4.3 sigma, PA 97) not toward a Gaia neighbour | binary type in SIMBAD (SB*, V* AE Aqr) | AllWISE ext_flg = 1 (extended or 2MASS XSC association) | not plain dust: optical brightening -0.022 mag (per-camera +0.008,-0.017,-0.049,-0.027) together with the infrared rise
- NEOWISE: score refetch 1.38 (stored 1.38, reproduced True); dW2 0.073, dW1 0.020, 19 visits, 203 points; baseline W1 8.62, W1-W2 0.045; onset between MJD 57324 and 57512
- detector 2: excess 0.108 mag, z 9.1, jitter ratio 4.8
- field control: target step +0.081 (W1 +0.047); neighbours N=57, median +0.001, robust sigma 0.012, max +0.042; z = 6.7
- centroid: jump at onset 0.059" +- 0.013 (4.3 sigma, PA 97); largest consecutive-visit jump 0.047"; rms 0.025"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.087, W2-W3 0.741 (W3 S/N 52.3), W3-W4 1.886 (W4 S/N 21.9), ext_flg 1, ph_qual AAAA: weak W3 excess (0.5 < W2-W3 < 1.0)
- Gaia: RUWE 1.14, ipd_frac_multi_peak 0, NSS none, Teff 5881 K, logg 4.53, H-alpha pEW -1.715 nm, varclass none; M_G 6.14, -0.17 mag vs sequence (on the sequence); neighbours within 10": none
- SIMBAD (10"): V* AE Aqr [CV*; *,CV*,Em*,NIR,Opt,PM*,SB*,UV,V*,X] 1.15" refs=705
- ASAS-SN: 2404 points, cameras bC(g,237); bD(g,251); bG(g,118); bH(g,119); ba(V,45); bc(V,195, d=+0.008); bd(V,204, d=-0.017); be(V,36); bf(V,33); bg(V,71, d=-0.049); bh(V,83, d=-0.027); bk(g,168); bl(g,166); bo(g,165); bp(g,162); bs(g,175); bt(g,176); change at onset (after-before, per-camera median) -0.022 mag; largest seasonal dimming 0.09 mag at MJD 56430
- dust: excess flux W1 5.72 mJy, W2 4.87 mJy, T = 1655 K (16-84%: 789-8000) 

### uid137372  [D2]  KILLED
- position 239.47677 -24.84523; Gaia DR3 6236150955972919936; G 11.78, BP-RP 1.61, plx 7.40 mas; plot `plots/uid137372.png`
- **KILL:** eclipsing binary in SIMBAD (EB*, UCAC4 326-078840)
- **young:** SIMBAD young-star types Or*,Y*? (UCAC4 326-078840; Gaia DR3 6236150955970405376) | Gaia DR3 variability class YSO(0.72)
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | 1.26 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | optical dimming +0.051 mag after the infrared onset (debris transit signature) | largest seasonal optical dimming 0.21 mag (MJD 60539)
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 18 visits, 133 points; baseline W1 8.22, W1-W2 0.237; onset between MJD 57075 and 57251
- detector 2: excess 0.287 mag, z 13.4, jitter ratio 9.9
- field control: target step +0.080 (W1 +0.034); neighbours N=86, median -0.007, robust sigma 0.014, max +0.054; z = 6.2
- centroid: jump at onset 0.093" +- 0.125 (0.7 sigma, PA 87); largest consecutive-visit jump 0.601"; rms 0.155"; toward neighbour: none; expected shift if a neighbour were the source: 4.3" G17.8: 0.30"; 8.2" G19.7: 0.58"
- AllWISE 2010: W1-W2 0.271, W2-W3 2.185 (W3 S/N 67.1), W3-W4 2.718 (W4 S/N 54.8), ext_flg 1, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.31, ipd_frac_multi_peak 2, NSS none, Teff 4158 K, logg 4.09, H-alpha pEW -0.471 nm, varclass YSO(0.72); M_G 6.13, -1.26 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 4.3" PA267 G17.80 dG+6.01; 8.2" PA142 G19.68 dG+7.89
- SIMBAD (10"): UCAC4 326-078840 [Or*; *,EB*,MIR,NIR,Or*,Ro*,Y*?] 0.47" refs=19; Gaia DR3 6236150955970405376 [Y*?; *,Y*?] 4.08" refs=2
- ASAS-SN: 1137 points, cameras bG(g,237); be(V,103, d=+0.051); bg(V,181); bk(g,299); bo(g,208); bs(g,109); change at onset (after-before, per-camera median) +0.051 mag; largest seasonal dimming 0.21 mag at MJD 60539
- dust: excess flux W1 -23.25 mJy, W2 -16.11 mJy, T = n/a K (16-84%: n/a-n/a) no W2 excess flux after onset

### uid304631  [D2]  KILLED
- position 262.18994 -32.77760; Gaia DR3 4054730091318373376; G 11.22, BP-RP 0.89, plx 5.59 mas; plot `plots/uid304631.png`
- **KILL:** centroid jump 0.618" (3.5 sigma) at the onset toward a neighbour: 7.6" PA52 G18.9 (angle 34 deg); 9.0" PA32 G18.7 (angle 13 deg)
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association)
- NEOWISE: score refetch 0.00 (stored 0.00, reproduced True); dW2 0.000, dW1 0.000, 6 visits, 68 points; baseline W1 9.54, W1-W2 0.154; onset between MJD 58720 and 59084
- detector 2: excess 0.200 mag, z 19.2, jitter ratio 6.1
- field control: target step +0.102 (W1 +0.034); neighbours N=103, median -0.001, robust sigma 0.034, max +0.111; z = 3.0
- centroid: jump at onset 0.618" +- 0.177 (3.5 sigma, PA 18); largest consecutive-visit jump 0.517"; rms 0.243"; toward neighbour: 7.6" PA52 G18.9 (angle 34 deg); 9.0" PA32 G18.7 (angle 13 deg); expected shift if a neighbour were the source: 3.7" G18.1: 0.34"; 4.3" G21.0: 0.38"; 6.9" G20.5: 0.62"; 7.6" G18.9: 0.68"; 9.0" G18.7: 0.81"
- AllWISE 2010: W1-W2 0.228, W2-W3 -0.662 (W3 S/N -2.0), W3-W4 1.644 (W4 S/N -6.2), ext_flg 1, ph_qual AAUU: W3 S/N < 5: no W2-W3 class
- Gaia: RUWE 1.01, ipd_frac_multi_peak 0, NSS none, Teff 5745 K, logg 4.44, H-alpha pEW 0.075 nm, varclass SOLAR_LIKE(0.32); M_G 4.96, -0.01 mag vs sequence (on the sequence); neighbours within 10": 3.7" PA314 G18.11 dG+6.89; 4.3" PA260 G20.98 dG+9.76; 6.9" PA262 G20.51 dG+9.29; 7.6" PA52 G18.88 dG+7.66; 9.0" PA32 G18.68 dG+7.46
- SIMBAD (10"): TYC 7379-2-1 [*; *,NIR] 0.29" refs=0
- ASAS-SN: 977 points, cameras bH(g,336, d=+0.007); bh(V,174); bl(g,293, d=+0.001); bp(g,174, d=+0.006); change at onset (after-before, per-camera median) +0.006 mag; largest seasonal dimming 0.02 mag at MJD 60521
- dust: excess flux W1 1.09 mJy, W2 2.76 mJy, T = 623 K (16-84%: 356-952) 

