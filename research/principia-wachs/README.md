# Wachs permutation polytopes — PRINCIPIA research archive

**Status: unverified research draft. Not a formally certified proof or a completed competition entry.**

This archive consolidates research notes created during 7–12 November 2026 toward Brenti–Sentinelli Conjecture 6.3 (MathDB 381794). The proposed principal statement is the affine equivalence

\[
\operatorname{conv}(\mathcal W(S_{2m}))\cong_{\mathrm{aff}}\operatorname{Perm}_m\times[-1,1]^m.
\]

The argument uses the block parametrization in Brenti–Sentinelli, *Wachs permutations, Bruhat order and weak order*, Proposition 3.2 (arXiv:2212.04932). The proposed corollaries concern simplicity, face counts, graph distances, the h-polynomial, and a zonotope representation. Priority has **not** been established, and no publication claim is made.

## Directory layout

- `paper/` — LaTeX source and compiled PDF snapshot.
- `proofs/` — proposed product proof, exposition, applications, original PRINCIPIA submission README.
- `lean/` — **uncompiled, non-certified** Lean drafts; no claim that they type-check.
- `verification/` — computational checks; testing finite cases cannot establish the theorem universally.
- `notes/` — dated reports and derived results.
- `archives/` — intact historical ZIP packages from November 7–12, retained for provenance.
- `SHA256SUMS` — hashes of staged files.

## Important cautions

- The full theorem has **not** been compiled and kernel-verified in Lean.
- Mathematical correctness has **not** been established by an independent referee.
- Literature searches have **not** established novelty or publication priority.
- This GitHub archival commit is **not** a PRINCIPIA registration, an academic publication, or a journal submission.
- Some computational checks assume the product decomposition and are not independent proof of it.
- User account registration and official competition submission must be performed separately if approved.

## Primary reference

F. Brenti and P. Sentinelli, *Wachs permutations, Bruhat order and weak order*, European Journal of Combinatorics (2024), DOI: https://doi.org/10.1016/j.ejc.2023.103804.
