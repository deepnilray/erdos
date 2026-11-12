# PRINCIPIA research advance — 11 November 2026

## Main new consequence: explicit h-polynomial

Let Q_m be the convex hull of even Wachs permutations in the one-line embedding. The proof draft establishes an affine isomorphism Q_m ≅ Perm_m × [-1,1]^m. Conditional on this theorem, its h-polynomial is

    h(Q_m;t) = A_m(t) (1+t)^m,

where A_m(t) = sum_{π in S_m} t^{des(π)} is the Eulerian polynomial, with A_1(t)=1.

**Proof.** For a d-dimensional simple polytope P, define

    h(P;t) = sum_{k=0}^d f_k(P) (t-1)^k,

where f_k counts k-dimensional nonempty faces. (This is a reversed-variable convention: it is the usual h-polynomial in increasing powers.) Since faces of P×R are precisely products F×G, and dimensions add,

    h(P×R;t) = h(P;t) h(R;t).

The segment has h-polynomial 2+(t-1)=1+t; thus h([-1,1]^m;t)=(1+t)^m. The classical Eulerian h-vector theorem for the standard (m-1)-permutohedron gives h(Perm_m;t)=A_m(t). Multiplication yields the claimed identity.

Equivalently, the coefficient of t^k is

    h_k(Q_m) = sum_{j=0}^{m-1} <m,j> binom(m,k-j),

where <m,j> counts permutations of m elements with j descents, and out-of-range binomial coefficients vanish.

Consequences: the h-vector is palindromic and unimodal; its sum equals 2^m m!, the number of vertices. The product formula supplies a fast way to compute the full h-vector from Eulerian numbers.

## Independent arithmetic check

The accompanying script computes f-vectors by ordered set partitions and cube faces, converts them into h-vectors, and compares with the Eulerian convolution for m=1,...,7. No geometry packages or floating-point arithmetic are used.

## Formalization work

WachsAffineCore_2026_11_11.lean defines the affine block map and its inverse on ℝ×ℝ, extends them to vectors indexed by Fin m, and supplies ring-normalization proofs of the inverse identities and block formula. No `sorry` is present. **Lean and lake are not installed in this environment, so the file has not been compiled or kernel checked.**

Still missing: an actual mathlib representation of Wachs permutations, the proof that the block parameterization is a bijection, a formal affine equivalence, convex hull of Cartesian products, and a formal simplicity theorem. These are necessary before claiming a formal proof of Conjecture 6.3.

## Priority and limitations

The original paper (Brenti–Sentinelli, arXiv:2212.04932) gives the block parametrization in Proposition 3.2 and explicitly studies weak-order products. The new h-polynomial is a standard consequence of the proposed affine-product theorem, not a separately verified original result. A web search on 11 November 2026 did not reveal a direct indexed proof of the exact even-Wachs polytope product, but this is not a definitive priority check.

No account was accessed; nothing was registered or submitted.
