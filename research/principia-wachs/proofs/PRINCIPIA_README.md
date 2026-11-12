# PRINCIPIA submission package — MathDB 381794

Proposed project title: The Wachs Permutation Polytope: A Permutohedron–Cube Product

Problem: Brenti–Sentinelli Conjecture 6.3, simplicity of the convex hull of even Wachs permutations.

One-sentence pitch: An explicit affine coordinate change identifies the Wachs-permutation polytope with the product of a standard permutohedron and a cube, proving simplicity and determining its faces, facets, and linear optimization.

## Pipeline mapping

1. Solution — `Wachs_Polytope_Paper.tex`, Sections 1–2 (draft proof, not independently refereed).
2. Lean formalization — `BlockCoordinates.lean` (ONLY the two-coordinate affine inverse identities; not compiled; *does not* prove the full conjecture).
3. Paper — `Wachs_Polytope_Paper.pdf` and editable `.tex` (draft, not published).
4. Exposition — `Exposition.md` (text suitable to revise for PRINCIPIA).
5. Applications — `Applications.md` (face enumeration, inequalities, optimization, adjacency, and formalization implications).

## Required checks before marking full completion

- Compile Lean under a pinned Lean 4 + mathlib version and formalize the complete theorem of affine product equivalence, and simplicity; the current Lean fragment alone is NOT a faithful formalization of the research result.
- Seek independent mathematical checking of the block characterization, affine isomorphism, face counts and facets.
- Complete the originality literature search, including recent preprints and author correspondence.
- Verify the MathDB ID and PRINCIPIA problem linkage on the platform.
- Confirm authorship and any usage/disclosure requirements for AI-assisted work.

## Registration limitation

A connected browser page was readable but the available browser integration could not click, type, upload or submit forms in this ChatGPT session. The account currently has a separate Fall Competition project (MathDB 377007), and the site states one competition entry per person. No project modification, registration, posting, or submission has been performed. Do not switch entries without first safeguarding the existing project.

Original source: Brenti and Sentinelli, 'Wachs permutations, Bruhat order and weak order,' European Journal of Combinatorics 119 (2024), 103804, https://doi.org/10.1016/j.ejc.2023.103804.
