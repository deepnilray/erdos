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

| Part | File | State on 2026-11-16 |
|---|---|---|
| 1 | `01_seshadri/SESHADRI_DOSSIER.md` | Draft done: reading ladder, three project options, how to approach him. Publication list and two prior-art checks still to do (its section 6). |
| 2 | `02_math/STATUS.md` | Not started; rules and exclusion list written. A scheduled run is set up to start it. |
| 3 | `03_frontier/FRONTIER_IDEAS.md` | Eight ideas triaged; two carried to first computations (both null, documented). Next steps listed. |

## Code and data
- `03_frontier/polarisation_alignment/align_pilot.py`, `align_diagnostics.py`: run with
  `python3 align_pilot.py consolidated_catalog_ver1.2.0.fits` (catalogue from github.com/CIRADA-Tools/RMTable, unzip first).
- `03_frontier/pmf_streams/pmf_streams_first_pass.py`: self-contained, `python3 pmf_streams_first_pass.py`.
- Outputs of the runs used in the write-ups are the `*_output.txt` and `*.json` files beside each script.
- The cloud sandbox reaches GitHub, PyPI and public papers, but not CASDA, Gaia or IRSA archives. Large downloads go through
  Deepnil's PC or a GitHub Actions workflow that pushes results to a branch.

## Standing rules (from Deepnil)
Prior-art search on the object before computing; forecast before computing; planted-failure controls that must fire; verify every
citation against the primary source; never overclaim; no numeric success odds; check past work (CHECKPOINTS.md on branch
`claude/all-checkpoints`) before starting anything.
