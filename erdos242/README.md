# Erdős–Straus (Erdős #242): family p = mut − m − u

Status 2026-11-08: conjecture open. Theorem A and Proposition B proved (see erdos_straus_family.pdf).
Verified: all hard primes < 2·10^7 (es_family.py, es_identity_check.py), < 2·10^6 via t-form (es_t_form.py),
random 12/15/18-digit samples (es_large.py). Symbolic check: es_symbolic.py. Log: es_research_log.md.
Run from this directory: `python3 es_family.py 20000000 5000` (needs sympy).

Session 2 additions (2026-11-08): Prop C (Jacobi-symbol constraint, odd squares never represented), min-modulus and representation-count data, Chamberland comparison, sieve analysis, dead-idea ledger: see the 'Session 2' section of es_research_log.md. New scripts: es_minm.py es_compare.py es_allints.py es_jacobi.py es_count.c es_lnr.py.
