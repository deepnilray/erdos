# Erdős #203 literature hunt (agent L), started 2026-10-26

Scope: new sources only; the existing ledger is APPROACHES.md (rows A1-A8, B1-B8, C1-C10) and is not repeated.
Tools: WebSearch/WebFetch only (arxiv.org via shell is blocked). Only sources I actually opened are listed.
Verification flag: P = statement read on the page fetched; S = second-hand. [LEAD] = could feed a proof.

## Entries

### L1. veljjanoski/erdos203 (GitHub), "search for a 2D covering system ... (negative outcome, data and code)"
https://github.com/veljjanoski/erdos203 (README read 2026-10-26).
Statement (README): "No such m was found, and we do not prove that none exists." Best coverage 71.7% at N=5040, 76.0% at N=55440; no strip covering on Z_N x Z_d for N=720720 and d<720; among 442 small-order primes all lattices are distinct, no Fermat-type nested chain.
Judgement: computational only, already summarised in HUB.md. No proof content. Not a lead. P.

### L2. Related arXiv items opened and rejected
- arXiv:2605.21524 (generalization of the Erdős-Sierpiński conjecture) is about sigma(n+1)=k sigma(n); unrelated. P.
- arXiv:2608.22550 (directions in lattice-line coverings of the integer plane): Thm 7 only produces coverings by lattice *lines* with dense directions; no density/obstruction theorem; no relation to #203. Mentions Cremona-Koymans [arXiv:2601.03212] as the finite-index-sublattice theory. P.
- Filaseta CANT 2005 slides (people.math.sc.edu/filaseta/seminars/CANT2005slides.pdf): Haight-type bound delta >= prod(1-1/m_j) - sum_{i<j, gcd>1} 1/(m_i m_j) for uncovered density of a 1-D covering; Erdős-Guy F13 conjecture (Sierpiński-type sequence without primes <=> bounded least prime factor); nothing two-base. P. Possible tool: the Haight inequality is a first-moment/Bonferroni bound; its 2-D analogue is a (weak) lower bound on uncovered density that needs only pairwise lattice intersections [Λ_p ∩ Λ_q has index e(pq)]. Marginal, repo's distortion bound is stronger.

