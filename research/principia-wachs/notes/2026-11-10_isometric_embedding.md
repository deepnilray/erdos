# PRINCIPIA Wachs-polytope progress — 10 November 2026

## New exact theorem (conditional on the affine-product theorem)

Write a vertex as `(π, ε)` where `π` is a permutation of `[m]` in one-line notation and `ε ∈ {−1,+1}^m`. For `1 ≤ a < b ≤ m`, define `I_ab(π)=1` if the value `a` occurs before `b` in `π`, and `0` otherwise. Define

`Φ(π,ε) = ((I_ab(π))_{a<b}, ((1+ε_i)/2)_{i=1}^m)`.

**Theorem.** The edge graph of `Q_m` embeds isometrically in the hypercube of dimension `binom(m,2)+m` via `Φ`. In particular, for vertices `u=(π,ε)` and `v=(σ,δ)`,

`d_Q(u,v) = #{a<b : I_ab(π) ≠ I_ab(σ)} + #{i : ε_i ≠ δ_i}`.

**Proof.** The product theorem identifies the graph with the Cartesian product of the permutohedron graph and an `m`-cube. An edge in the permutohedron exchanges neighboring entries in its one-line permutation. Such an exchange reverses the relative order of precisely one pair of values, so each edge changes one inversion-signature bit. A cube edge changes exactly one sign bit. Therefore every path from `u` to `v` must have at least the Hamming distance between `Φ(u)` and `Φ(v)` edges. Conversely, sort the entries of `π` into the relative order specified by `σ` using adjacent exchanges. Every exchange can be chosen to correct one discordant pair, and the procedure terminates after exactly the number of discordant pairs. Independently flip each disagreeing sign bit. This constructs a path with precisely the claimed number of edges. Hence equality holds. ∎

The embedding is *isometric*, not an assertion that the graph equals the full hypercube. This establishes that the graph is a **partial cube** (an isometric subgraph of a hypercube). For `m ≥ 3`, it need not be a median graph.

**Consequences.** The diameter is `m(m+1)/2`. Shortest-path distance and a shortest path can be computed using inversion counting and adjacent swaps, with `O(m log m)` inversion counting and `O(m²)` swaps in the worst case. A canonical binary representation supports exact distances without graph construction.

## Independent computation

`verify_isometric_embedding.py` builds the graph from adjacent swaps and sign flips, performs BFS from *every* vertex, and compares each resulting distance with Hamming distance of the proposed embedding. Exact checks passed for `m=1,2,3,4`: respectively `4, 64, 2304, 147456` ordered pairs, 149,828 pairs total. This tests the graph implication, **not** the affine-product theorem independently.

## Formalization progress

`IsometricEmbeddingCore.lean` contains explicit `encode` and `decode` definitions and two inverse-coordinate theorem statements with ring-normalization proof scripts. This file is **uncompiled**; it is not evidence of a successful Lean verification. The essential unformalized work remains: formal definition of Wachs permutations, perfect matching of consecutive positions, finite-set convex-hull product, and a theorem that the permutohedron/cube product is simple. Suggested staging: (1) finite permutation block bijection; (2) coordinate equivalence; (3) convex-hull product; (4) polytope simplicity; (5) optional graph isometry.

## Priority and submission

A fresh 10 November 2026 web search for the affine-product theorem and resolution of Conjecture 6.3 did not find an indexed proof. This is **not** a definitive novelty certification. The 2024 Brenti–Sentinelli paper remains the primary source: https://doi.org/10.1016/j.ejc.2023.103804 . No account was accessed and no submission was made.
