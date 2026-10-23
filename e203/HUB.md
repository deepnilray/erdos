# Erdős #203 — project hub (single source of truth)

Headed from the Andrica session; Andrica work lives separately on branch `claude/andrica-state` (`andrica/`).
Problem: is there an m (coprime to 6) such that 2^k·3^l·m + 1 is composite for all k, l ≥ 1? Status: **OPEN**.
Current verdict: NO more likely [CONJECTURED] — see `VERDICT.md` and `verdict/1–5`.

## Proved / verified so far (see the linked files)
- All pure coverings with e_p ≤ 4·10⁵ excluded; B(4·10⁵) = 0.730584 exact rational [PROVED, `DISTORTION.md`].
- Mixed certificates (primes + algebraic factorisations) excluded for e_p ≤ 4·10⁵ [PROVED, `MIXED.md`, Theorem E].
- B(8·10⁵) = 0.742445 in floating point; the 4–8·10⁵ pool is complete only by construction [VERIFIED, float].
- Every m ≤ 3·10⁹ coprime to 6 has a prime with 2^k3^l ≤ 2^29.6 [VERIFIED, `verdict/search.c`].
- Erdős–Odlyzko 1979 Thm 2: positive lower density of m with a prime [literature].

## Run log
- 2026-10-10: five-direction assessment (verdict/1–5).
- 2026-10-17/22: scheduled all-agents run (trigger trig_016THwwcVavtrWxeAPL3Eiv1) fired; no commits came back
  (the parallel Andrica run failed on the usage limit, likely the same cause).
- 2026-10-23: two Sonnet agents launched from the head session (run3): agent A = YES-side certification,
  agent B = NO-side and literature. Reports go to `verdict3/`.

## Run3 assignments
- **A (certify):** second-route completeness certificate for `poolE_400k_800k.jsonl`; exact-rational B(8·10⁵);
  Theorem E at 8·10⁵; conditional all-E theorem with explicit hypothesis H; push E to 1.6·10⁶ if feasible.
- **B (no side + literature):** literature ledger `verdict3/APPROACHES.md`; best provable unconditional statement
  toward "every m has a prime"; extend the exhaustive search beyond 3·10⁹; Bateman–Horn refinement; red team of A.

## Aristotle (Lean) prompts
Prompts for formal verification are collected here when a result is ready for it.
