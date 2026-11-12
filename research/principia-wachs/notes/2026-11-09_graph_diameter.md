# New consequence: exact graph distances and diameter (9 November 2026)

**Status:** Mathematical deduction from the proposed affine-product theorem; not independently Lean-certified. Not a separate novelty claim.

Let a Wachs vertex be encoded by a permutation `p=(p_1,...,p_m)` of `[m]` and a sign vector `e in {-1,+1}^m`. Define `inv(q)` as the number of pairs `i<j` for which `q_i>q_j`.

**Theorem (conditional on the product theorem).** The shortest edge-path distance between vertices `(p,e)` and `(q,d)` of `Q_m` is

`dist((p,e),(q,d)) = inv(q^{-1} ∘ p) + #{i : e_i != d_i}`,

where permutations are viewed as maps from positions to values. Consequently

`diam(Graph(Q_m)) = m(m-1)/2 + m = m(m+1)/2`.

**Proof.** An invertible affine transformation preserves the face lattice, hence the edge graph. The edge graph of a product of polytopes is the Cartesian graph product of their edge graphs: an edge changes exactly one factor. In the cube factor, edges flip exactly one sign, so the shortest path length is Hamming distance. In the permutohedron factor, edges swap two consecutive *values* `k,k+1` in the permutation's one-line notation. Equivalently, if `p` is regarded as the list of values in position order, a step left-composes `p` by an adjacent transposition on values. To transform `p` to `q` requires expressing `q ∘ p^{-1}` as a product of adjacent transpositions; its minimum length is its inversion count. Inversion count is invariant under taking inverses, so this equals `inv(q^{-1} ∘ p)`. The Cartesian graph-product metric is the sum of factor distances, since each edge changes only one factor, and concatenating shortest paths attains the lower bound. The maximal inversion count is `m(m-1)/2`, attained by reversal relative to the starting permutation; the maximal Hamming distance is `m`, attained by opposite signs. Both maxima can be attained simultaneously. QED.

**Caution.** The exact distance formula relies on the *value*-adjacent swap edge convention. A naive formula counting inversions of `p^{-1} ∘ q` is also correct (inverse of the displayed relative permutation); counting inversions of `p ∘ q^{-1}` is likewise equal. The important thing is not to count positional adjacent swaps directly on `p` without tracking the representation.

**Applications.** Exact routing between Wachs vertices; worst-case number of polytope-edge pivots; graph Cartesian factorization; benchmark for optimization and random walks. This is a consequence of known permutohedron/cube geometry, not evidence of independent originality.

**Outstanding:** complete Lean proof of the Wachs membership-to-product equivalence and of the polytope simplicity theorem; independent priority check beyond indexed sources.
