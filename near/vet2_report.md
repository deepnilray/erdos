# vet2 report: near target list (PARTIAL, run in progress)

Generated 2026-11-20 15:02 UTC; 16 targets; machine-generated, the plots in plots/ still need a look by eye.

Kill rules: field-control z < 5 (detector-1 and list targets); centroid jump > 3 sigma toward a Gaia neighbour; Gaia neighbour within 6" with dG < 3; baseline W1 < 8; SIMBAD CV / confirmed eclipsing binary (counterpart within 3"); SIMBAD galaxy/QSO within 6"; young star (SIMBAD Y*O, Y*?, TT*, TT?, Or*, Ae*, Ae?, pr* within 5" or Gaia variability class YSO) kills detector-1/list targets and labels detector-2 targets 'known/likely young star'. Flags (not kills): 'not plain dust' (optical brightening at the infrared onset in >= 2 ASAS-SN cameras, none dimming, median < -0.015 mag), SIMBAD '?' candidate types, RUWE, NSS, ext_flg, colour classes.

## Controls

| Control | Result | Detail |
|---|---|---|
| ASASSN-21qj | PASS | category SURVIVOR, SIMBAD 2MASS J08152329-3859234 (10 refs), field z 57.3, missing: none |
| J060000 | PASS | category SURVIVOR, largest ASAS-SN seasonal dimming 0.35 mag at MJD 58864 |
| V836 Tau | PASS | young: SIMBAD young-star types Or*,TT*,TT?,Y*?,Y*O (V* V836 Tau) | Gaia DR3 variability class YSO(0.83) |

Counts: {'YOUNG': 8, 'SURVIVOR': 6, 'KILLED': 2}

## Survivors (6)

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

## Known/likely young stars (detector 2) (8)

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

## Killed (2)

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

