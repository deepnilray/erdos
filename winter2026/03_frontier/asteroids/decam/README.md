# DECam archival asteroid search: choosing the programme (2026-11-22)

## Sweep (VERIFIED)
- `sweep.py` queried the NOIRLab Astro Data Archive API for DECam instcal images within ~14 deg of the ecliptic (30-2000 s): 319,555 exposures.
- `rank.py` keeps exposures that are public and have |beta| < 10 deg: 231,546.
- It then groups them by programme and pointing. A night qualifies with >= 3 exposures spanning >= 20 min. Pointings are ranked by how many qualifying nights fall within 7 days of each other, which is needed for linking into orbits.
- Result: 143 programmes have >= 2 linked nights (`programs.csv`).

## Prior work found (checked 2026-11-22)
| Programme | PI / purpose | Already searched for asteroids? |
|---|---|---|
| 2014A-0283 | Trilling/Allen, DECam NEO Survey | Yes (DAD DR1, MPC reports) |
| 2015A-0610 | Fuentes, Jupiter Trojans | Yes (Fuentes appears in DAD DR2: 1,267 tracklets) |
| 2019A-0337 | DEEP TNO survey | Yes (Solar System survey) |
| 2014A-0608 | Forster, HiTS transients | Yes (Pena et al. 2018, AJ 155, 135, "Asteroids in HiTS") |
| 2014B-0064 | (Goyal, Zenodo 2026-11-10) | Yes (71 faint movers) |
| 2017B-0279, 2018A-0913 | Rest, K2 transients | Probably (Rest appears in DAD DR2) |
| 2021A-0113, 2023A-716082 | Graham DDF (COSMOS) | Partly: Stetzler, Juric et al. (2022 talk: ~8,000 known asteroids observed, "10s of new"); Graham et al. 2023 MNRAS 519, 3881 |
| 2018A-0177 | Parker, OSSOS (TNOs) | Solar System programme; main-belt objects unclear |
| **2020A-0353** | **Peng, NGC 4636 galaxy-cluster imaging** | **No published asteroid search found; PI not in the DAD DR1/DR2 tables** |

## Choice: 2020A-0353 (CONJECTURED best, pending validation)
- 10 pointings at beta +3 to +7 deg (asteroid-rich).
- 2020-02-19 to 2020-02-27: up to 6 consecutive nights per pointing, each night 3-4 exposures of 400-525 s spread over ~4 h, in N501/g/r.
- About 1.5 mag deeper per exposure than the 86 s DDF data.
- It is a galaxy programme, so nobody looked for asteroids, and its consecutive nights allow linking.

Next: download one pointing (a subset of CCDs) and recover the known asteroids (SkyBoT, W84) before anything else.
