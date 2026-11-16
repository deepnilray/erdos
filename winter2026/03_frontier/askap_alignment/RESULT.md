# SPICE-RACS DR1 polarisation-angle coherence: result (2026-11-17)

Verdict: NULL, as forecast in FORECAST.md (written before the run). VERIFIED within the stated sample and statistic.

Data: CASDA table AS110.spice_racs_dr1_corrected_cut_v02 (24,758 rows), restricted to the 5,818 components that pass the
catalogue's snr, leakage, channel and Stokes-I-fit flags (the number Thomson et al. 2023 quote as reliable RMs).
Statistic: transported nearest-neighbour coherence S_D (code in ../polarisation_alignment/align_pilot.py), n_v = 10, 20, 40,
de-duplication at 2', 10', 60', null by global shuffle and by within-tile shuffle (1000 shuffles each).
Full log: branch `askap-results`, file run_log.txt; driver run_askap.py; workflow .github/workflows/askap_alignment.yml.

- Largest excess: z = +3.4 (p = 0.002) for fracpol > 3%, one per 2', n_v = 10, within-tile null. It weakens to z = +2.3 to 2.4
  at one per 10' and to z = +1.4 to 1.9 at one per 60', and disappears (z between -1.0 and +1.4) once |RM| > 20 rad m^-2 is
  required. Around 72 correlated tests were run, so a maximum of z = 3.4 is not significant after the look-elsewhere effect.
  Its pattern (small neighbourhoods only, weakening with de-duplication, absent at large |RM|) matches components of one source
  and residual leakage, the two traps identified in the pilot.
- Caveat on the |RM| cut: it keeps only 812 to 901 sources (most RMs at this high latitude are small), so its null has much less
  power. It does not by itself prove the excess is instrumental.
- Controls: random angles z = +0.71 (p = 0.25, must not fire: OK). Planted alignment in a 10-degree cap: 50% aligned gives
  z = +6.1 (fires); 30% gives z = +2.6; 20% and below are not detected. Sensitivity is therefore limited to strong local alignment.
- What this does NOT bear on: alignment on scales larger than one ASKAP tile in the within-tile test; three-dimensional
  (redshift-resolved) alignment; the northern sky. SPICE-RACS DR1 covers about 1300 deg^2 only.

Next: the decisive version needs POSSUM data releases or SPICE-RACS DR2 (10^5 sources or more) with redshifts. Until those are
public this line is parked; the code is ready to rerun by changing the CASDA table name.
