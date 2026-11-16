# Forecast written BEFORE the SPICE-RACS run (2026-11-16, Claude)

Data: SPICE-RACS DR1 "cut" polarised catalogue (Thomson et al. 2023, PASA 40, e040; 5818 RMs over about 1300 deg^2).
Test: transported nearest-neighbour coherence statistic S_D (same code as the pilot), one source per 10' and per 60',
null by global shuffle and by within-field shuffle, plus leakage cuts (|RM| > 20 rad m^-2, fractional polarisation > 3%).

Forecast: NULL after the leakage cuts. If any excess appears it will most likely live inside single ASKAP fields
(instrumental leakage, which ASKAP's sky-fixed beams would turn into a fake sky-frame alignment) and vanish with |RM| > 20.
A signal that survives the |RM| cut, the within-field null and the one-per-60' de-duplication would be surprising and would
trigger an independent-catalogue check (POSSUM pilot, LoTSS DR2 RM grid) before anything else.
