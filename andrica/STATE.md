# Andrica attack — state at 2026-10-11

Main result (audited, recomputed from scratch): sum of prime gaps >= x^{1/2} in [x,2x] << x^{0.5575+eps};
Andrica failures up to X << X^{0.0575+eps}; Legendre exceptions << N^{0.115+eps}. Paper: andrica_gaps.tex / .pdf.
Total sieve loss at r=0.0575: 0.99154810 (sieveZ, runN.sh, ZTAB=Z400_0575.txt ZNOZ=1 WSPLIT=1 FULLPART=1 DECOMP=1,
table T400_0575M.txt). r=0.057 fails (partial 1.00221). Control: sieve3 0.07 0 0 0.5 -> 0.99027345.
Barrier: Beurling system with RH-quality behaviour violating Andrica (Section 7; beurling.tex standalone).
Conditional: single-scale fourth moment of psi in intervals sqrt X implies Andrica.
Dead routes and exact obstructions: see the scheduled-run prompt and andrica_master_log.md.
Andrica itself: OPEN.
