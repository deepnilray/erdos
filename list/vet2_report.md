# vet2 report: list target list (final)

Generated 2026-11-20 15:22 UTC; 8 targets; machine-generated, the plots in plots/ still need a look by eye.

Kill rules: field-control z < 5 (detector-1 and list targets); centroid jump > 3 sigma toward a Gaia neighbour; Gaia neighbour within 6" with dG < 3; baseline W1 < 8; SIMBAD CV / confirmed eclipsing binary (counterpart within 3"); SIMBAD galaxy/QSO within 6"; young star (SIMBAD Y*O, Y*?, TT*, TT?, Or*, Ae*, Ae?, pr* within 5" or Gaia variability class YSO) kills detector-1/list targets and labels detector-2 targets 'known/likely young star'. Flags (not kills): 'not plain dust' (optical brightening at the infrared onset in >= 2 ASAS-SN cameras, none dimming, median < -0.015 mag), SIMBAD '?' candidate types, RUWE, NSS, ext_flg, colour classes.

## Controls

| Control | Result | Detail |
|---|---|---|
| ASASSN-21qj | PASS | category SURVIVOR, SIMBAD 2MASS J08152329-3859234 (10 refs), field z 57.3, missing: none |
| J060000 | PASS | category SURVIVOR, largest ASAS-SN seasonal dimming 0.35 mag at MJD 58864 |
| V836 Tau | PASS | young: SIMBAD young-star types Or*,TT*,TT?,Y*?,Y*O (V* V836 Tau) | Gaia DR3 variability class YSO(0.83) |

Counts: {'SURVIVOR': 6, 'KILLED': 1, 'YOUNG': 1}

## Survivors (6)

### ASASSN-21qj  [CONTROL]  SURVIVOR
- position 123.84704 -38.98983; Gaia DR3 5539970601632026752; G 13.37, BP-RP 0.81, plx 1.76 mas; plot `plots/ASASSN-21qj.png`
- flags: centroid jump 0.349" (5.5 sigma, PA 56) away from the neighbour(s) 3.7" PA253 G16.9, as expected when the target itself brightens in a blended WISE PSF | largest seasonal optical dimming 1.11 mag (MJD 59529)
- NEOWISE: score refetch 38.04 (stored n/a, reproduced n/a); dW2 0.738, dW1 0.332, 12 visits, 133 points; baseline W1 11.65, W1-W2 -0.057; onset between MJD 58072 and 58227
- field control: target step +0.803 (W1 +0.402); neighbours N=169, median -0.003, robust sigma 0.014, max +0.055; z = 57.3
- centroid: jump at onset 0.349" +- 0.063 (5.5 sigma, PA 56); largest consecutive-visit jump 0.212"; rms 0.109"; toward neighbour: none; expected shift if a neighbour were the source: 3.7" G16.9: 1.94"; 7.3" G18.7: 3.81"
- AllWISE 2010: W1-W2 -0.068, W2-W3 -0.498 (W3 S/N 2.3), W3-W4 3.219 (W4 S/N -2.6), ext_flg 0, ph_qual AACU: W3 S/N < 5: no W2-W3 class
- Gaia: RUWE 1.10, ipd_frac_multi_peak 0, NSS none, Teff 5761 K, logg 4.34, H-alpha pEW 0.112 nm, varclass none; M_G 4.60, +0.07 mag vs sequence (on the sequence); neighbours within 10": 3.7" PA253 G16.91 dG+3.54; 7.3" PA182 G18.67 dG+5.30
- SIMBAD (10"): 2MASS J08152329-3859234 [*; *,NIR] 0.15" refs=10; 2MASS J08152298-3859244 [*; *,NIR] 3.74" refs=1
- ASAS-SN: 1351 points, cameras bE(g,411); be(V,238, d=-0.018); bi(g,497); bm(g,205); change at onset (after-before, per-camera median) -0.018 mag; largest seasonal dimming 1.11 mag at MJD 59529
- dust: excess flux W1 2.72 mJy, W2 3.68 mJy, T = 953 K (16-84%: 934-972) 

### G1858978638770086016  [LIST]  SURVIVOR
- position 311.02040 +29.66480; Gaia DR3 1858978638770086016; G 12.06, BP-RP 1.89, plx 4.49 mas; plot `plots/G1858978638770086016.png`
- flags: AllWISE ext_flg = 1 (extended or 2MASS XSC association) | 2.83 mag above the main sequence at its colour | AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | optical dimming +0.141 mag after the infrared onset (debris transit signature) | largest seasonal optical dimming 0.40 mag (MJD 58370)
- NEOWISE: score refetch 2.02 (stored n/a, reproduced n/a); dW2 0.671, dW1 0.534, 10 visits, 118 points; baseline W1 8.16, W1-W2 0.445; onset between MJD 57159 and 57335
- field control: target step +0.529 (W1 +0.323); neighbours N=180, median -0.005, robust sigma 0.013, max +0.032; z = 42.3
- centroid: jump at onset 0.030" +- 0.022 (1.4 sigma, PA 176); largest consecutive-visit jump 0.072"; rms 0.031"; toward neighbour: none; expected shift if a neighbour were the source: 6.5" G20.6: 2.49"; 7.1" G18.4: 2.72"
- AllWISE 2010: W1-W2 0.505, W2-W3 1.517 (W3 S/N 74.4), W3-W4 1.895 (W4 S/N 46.1), ext_flg 1, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.21, ipd_frac_multi_peak 0, NSS none, Teff 5406 K, logg 3.81, H-alpha pEW -0.979 nm, varclass none; M_G 5.32, -2.83 mag vs sequence (above the sequence (brighter than stars of the same colour: pre-main-sequence or unresolved binary)); neighbours within 10": 6.5" PA242 G20.62 dG+8.56; 7.1" PA259 G18.41 dG+6.34
- SIMBAD (10"): no object
- ASAS-SN: 961 points, cameras bD(g,282); bH(g,72); bd(V,182, d=+0.141); bl(g,112); bp(g,66); bt(g,247); change at onset (after-before, per-camera median) +0.141 mag; largest seasonal dimming 0.40 mag at MJD 58370
- dust: excess flux W1 72.21 mJy, W2 86.26 mJy, T = 1069 K (16-84%: 1040-1099) 

### G5628404318169472  [LIST]  SURVIVOR
- position 43.54827 +5.88271; Gaia DR3 5628404318169472; G 13.43, BP-RP 1.35, plx 4.31 mas; plot `plots/G5628404318169472.png`
- flags: AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0) | largest seasonal optical dimming 0.10 mag (MJD 60695)
- NEOWISE: score refetch 4.35 (stored n/a, reproduced n/a); dW2 0.288, dW1 0.139, 20 visits, 169 points; baseline W1 10.59, W1-W2 0.369; onset between MJD 57606 and 57772
- field control: target step +0.286 (W1 +0.168); neighbours N=26, median -0.003, robust sigma 0.016, max +0.022; z = 18.1
- centroid: jump at onset 0.033" +- 0.023 (1.5 sigma, PA 120); largest consecutive-visit jump 0.056"; rms 0.037"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.389, W2-W3 1.575 (W3 S/N 41.2), W3-W4 1.411 (W4 S/N 10.7), ext_flg 0, ph_qual AAAA: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.08, ipd_frac_multi_peak 0, NSS none, Teff 4510 K, logg 4.55, H-alpha pEW -0.001 nm, varclass SOLAR_LIKE(0.19); M_G 6.60, -0.11 mag vs sequence (on the sequence); neighbours within 10": none
- SIMBAD (10"): no object
- ASAS-SN: 2434 points, cameras bC(g,254); bD(g,272); bG(g,168); bH(g,164); ba(V,28); bc(V,247, d=+0.024); bd(V,240, d=+0.041); bg(V,59, d=+0.093); bh(V,56, d=+0.033); bk(g,192); bl(g,256); bo(g,234); bs(g,135); bt(g,129); change at onset (after-before, per-camera median) +0.037 mag; largest seasonal dimming 0.10 mag at MJD 60695
- dust: excess flux W1 2.56 mJy, W2 3.59 mJy, T = 923 K (16-84%: 880-968) 

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

### G1768914166695591296  [LIST]  SURVIVOR
- position 327.55699 +14.11477; Gaia DR3 1768914166695591296; G 13.07, BP-RP 1.78, plx 9.06 mas; plot `plots/G1768914166695591296.png`
- flags: AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 0.52 (stored n/a, reproduced n/a); dW2 0.042, dW1 0.084, 21 visits, 253 points; baseline W1 9.66, W1-W2 0.405; onset between MJD 58794 and 58996
- field control: target step +0.164 (W1 +0.138); neighbours N=45, median -0.003, robust sigma 0.013, max +0.061; z = 12.6
- centroid: jump at onset 0.037" +- 0.015 (2.5 sigma, PA 111); largest consecutive-visit jump 0.041"; rms 0.024"; toward neighbour: none; expected shift if a neighbour were the source: n/a
- AllWISE 2010: W1-W2 0.438, W2-W3 1.073 (W3 S/N 53.0), W3-W4 0.619 (W4 S/N 7.5), ext_flg 0, ph_qual AAAB: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 0.97, ipd_frac_multi_peak 0, NSS none, Teff 4208 K, logg 4.65, H-alpha pEW -0.024 nm, varclass SOLAR_LIKE(0.23); M_G 7.85, -0.00 mag vs sequence (on the sequence); neighbours within 10": none
- SIMBAD (10"): no object
- ASAS-SN: 1196 points, cameras bC(g,265, d=+0.005); bG(g,108, d=+0.009); bc(V,265); bg(V,35); bk(g,138, d=+0.015); bo(g,168, d=+0.022); bs(g,217, d=-0.002); change at onset (after-before, per-camera median) +0.009 mag; largest seasonal dimming 0.01 mag at MJD 57515
- dust: excess flux W1 5.21 mJy, W2 5.06 mJy, T = 1357 K (16-84%: 1241-1497) 

### G6505057483979425024  [LIST]  SURVIVOR
- position 339.60016 -56.06835; Gaia DR3 6505057483979425024; G 14.34, BP-RP 1.86, plx 5.42 mas; plot `plots/G6505057483979425024.png`
- flags: AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 0.80 (stored n/a, reproduced n/a); dW2 0.049, dW1 0.027, 21 visits, 249 points; baseline W1 10.61, W1-W2 0.334; onset between MJD 59139 and 59342
- field control: target step +0.145 (W1 +0.074); neighbours N=27, median +0.001, robust sigma 0.013, max +0.044; z = 11.4
- centroid: jump at onset 0.039" +- 0.033 (1.2 sigma, PA 308); largest consecutive-visit jump 0.140"; rms 0.060"; toward neighbour: 7.7" PA294 G15.4 (angle 14 deg); expected shift if a neighbour were the source: 7.5" G19.9: 0.94"; 7.7" G15.4: 0.96"
- AllWISE 2010: W1-W2 0.429, W2-W3 1.922 (W3 S/N 49.7), W3-W4 1.092 (W4 S/N 9.2), ext_flg 0, ph_qual AAAB: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.04, ipd_frac_multi_peak 0, NSS none, Teff 3655 K, logg 4.36, H-alpha pEW 0.170 nm, varclass none; M_G 8.01, -0.07 mag vs sequence (on the sequence); neighbours within 10": 7.5" PA167 G19.88 dG+5.54; 7.7" PA294 G15.35 dG+1.01
- SIMBAD (10"): no object
- ASAS-SN: 2487 points, cameras bF(g,311, d=+0.001); bH(g,378, d=-0.020); bf(V,303); bh(V,190); bj(g,398, d=+0.001); bl(g,408, d=-0.039); bn(g,279, d=-0.016); bp(g,220, d=-0.000); change at onset (after-before, per-camera median) -0.008 mag; largest seasonal dimming 0.03 mag at MJD 56848
- dust: excess flux W1 0.51 mJy, W2 0.93 mJy, T = 751 K (16-84%: 623-909) 

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

## Killed (1)

### G246657089893122176  [LIST]  KILLED
- position 58.83067 +47.35326; Gaia DR3 246657089893122176; G 13.08, BP-RP 1.29, plx 4.72 mas; plot `plots/G246657089893122176.png`
- **KILL:** blend: Gaia neighbour within 6" only 2.88 mag fainter in G (4.0" PA96 G15.96 dG+2.88)
- flags: AllWISE 2010 Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- NEOWISE: score refetch 0.99 (stored n/a, reproduced n/a); dW2 0.121, dW1 0.129, 20 visits, 224 points; baseline W1 9.87, W1-W2 0.618; onset between MJD 57797 and 57995
- field control: target step +0.257 (W1 +0.230); neighbours N=151, median -0.005, robust sigma 0.012, max +0.045; z = 22.1
- centroid: jump at onset 0.037" +- 0.022 (1.7 sigma, PA 323); largest consecutive-visit jump 0.081"; rms 0.034"; toward neighbour: none; expected shift if a neighbour were the source: 4.0" G16.0: 0.83"
- AllWISE 2010: W1-W2 0.697, W2-W3 1.118 (W3 S/N 52.0), W3-W4 0.176 (W4 S/N 6.5), ext_flg 0, ph_qual AAAB: Class II-like colour cuts (W1-W2 > 0.25, W2-W3 > 1.0)
- Gaia: RUWE 1.01, ipd_frac_multi_peak 0, NSS none, Teff 4804 K, logg 4.57, H-alpha pEW 0.014 nm, varclass SOLAR_LIKE(0.72); M_G 6.45, -0.05 mag vs sequence (on the sequence); neighbours within 10": 4.0" PA96 G15.96 dG+2.88
- SIMBAD (10"): no object
- ASAS-SN: 623 points, cameras bC(g,251); bc(V,191, d=+0.009); bs(g,181); change at onset (after-before, per-camera median) +0.009 mag; largest seasonal dimming 0.01 mag at MJD 58026
- dust: excess flux W1 5.15 mJy, W2 5.20 mJy, T = 1288 K (16-84%: 1190-1405) 

