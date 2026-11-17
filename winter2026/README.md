# Winter 2026 research plan for Deepnil Ray: start here

Branch `claude/winter-2026-plan` of `deepnilray/erdos`. Written 2026-11-16. This file is the entry point for any model or person
picking up the work. Read it fully, then the file for the part you are working on. Every file uses the labels PROVED, VERIFIED
(with bound and a control that fired), CONJECTURED, OCCUPIED, DEAD, and puts the verdict first.

## The three goals (Deepnil's own words, paraphrased)
1. Find a reading project and a strong winter research project to do with Prof. T. R. Seshadri, nothing that argues against his
   work, ideally near what Deepnil already does (Gaia, TESS, survey pipelines).
2. Find open mathematical conjectures of real difficulty (about 19 to 39 where the Riemann hypothesis is 100) and prove them
   completely, using scheduled runs so the work continues without being asked again.
3. Find the most ambitious physics or astronomy idea that could become a field-changing paper, and push it as far as possible.

## Where everything is and its state

| Part | File | State on 2026-11-17 |
|---|---|---|
| 1 | `01_seshadri/SESHADRI_DOSSIER.md` | Publication list verified (INSPIRE id T.Seshadri.1). Option 4.1 (k^4) mostly answered in his own 2017 paper; option 4.3 (RM x Mg II) OCCUPIED by his co-author Malik et al. 2026 (arXiv:2605.16924); option 4.2 (streams x primordial fields) apparently open. His 2024 eBOSS quasar homogeneity paper connects to our isotropy tests. |
| 2 | `02_math/` (TARGETS.md, LOG.md, ssnc_2d3.tex/pdf) | Target: Seymour's second neighbourhood conjecture, case n = 2delta+3. PROVED: a counterexample needs at least two complete min-outdegree vertices. Case still open; next step in LOG.md. Needs a human check. |
| 3 | `03_frontier/FRONTIER_IDEAS.md`, `03_frontier/giant_impacts/` | Flagship: blind NEOWISE hunt for planetary-collision afterglows over 699,339 nearby main-sequence stars. Prototype ASASSN-21qj recovered blindly (score 38 vs field maximum 4.4). Run in progress on branches impacts-live-0..3 (31% on 2026-11-17 04:10 UTC). Only field star above threshold is the known 2019 dimmer ASASSN-V J060000.76-310027.83, with a coincident NEOWISE brightening not yet found in print (see giant_impacts/LOG.md, CANDIDATES.md). ASKAP polarisation test: NULL. |

## Code and data
- `03_frontier/polarisation_alignment/align_pilot.py`, `align_diagnostics.py`: run with
  `python3 align_pilot.py consolidated_catalog_ver1.2.0.fits` (catalogue from github.com/CIRADA-Tools/RMTable, unzip first).
- `03_frontier/pmf_streams/pmf_streams_first_pass.py`: self-contained, `python3 pmf_streams_first_pass.py`.
- Outputs of the runs used in the write-ups are the `*_output.txt` and `*.json` files beside each script.
- The cloud sandbox reaches GitHub, PyPI and public papers, but not CASDA or CDS (SIMBAD, VizieR). On 2026-11-17 IRSA TAP and the
  Gaia TAP endpoint DID answer from the sandbox; CDS fails from both the sandbox and GitHub Actions. Large downloads go through
  Deepnil's PC or a GitHub Actions workflow that pushes results to a branch.

## Standing rules (from Deepnil)
Prior-art search on the object before computing; forecast before computing; planted-failure controls that must fire; verify every
citation against the primary source; never overclaim; no numeric success odds; check past work (CHECKPOINTS.md on branch
`claude/all-checkpoints`) before starting anything.
