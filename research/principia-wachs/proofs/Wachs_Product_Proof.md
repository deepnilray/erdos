# Wachs permutation polytope: a product decomposition

**Target:** Brenti–Sentinelli, Conjecture 6.3 (2022), corresponding to MathDB 381794 (as identified in earlier project work). **Status:** complete human-readable mathematical argument, **not** independently refereed or Lean-kernel-verified. No claim of novelty is made.

## Theorem
For every integer m >= 1, let W_m be the set of Wachs permutations in S_(2m), represented by their one-line vectors in R^(2m). Let P_m = conv{(pi(1),...,pi(m)): pi in S_m}, the standard permutohedron, and C_m=[-1,1]^m. Then conv(W_m) is affinely isomorphic to P_m x C_m. In particular it is a simple polytope of dimension 2m-1.

## Proof
The original paper (Brenti–Sentinelli, arXiv:2212.04932, Proposition 3.2 and the formula preceding it) supplies a bijection from W_m to pairs (pi,epsilon), where pi in S_m and epsilon in {-1,1}^m. Explicitly, for i=1,...,m,

x_(2i-1) = 2 pi(i) - 1/2 - epsilon_i/2,
x_(2i)   = 2 pi(i) - 1/2 + epsilon_i/2.

(Thus epsilon_i=1 gives (2pi(i)-1,2pi(i)); epsilon_i=-1 reverses this pair.)

Define an invertible linear map T:R^(2m)->R^m x R^m by

T(x)=(a,b), a_i=(x_(2i-1)+x_(2i)+1)/4, b_i=x_(2i)-x_(2i-1).

Strictly, T is an **affine** bijection because of the +1 term. Its inverse is

x_(2i-1)=2a_i-1/2-b_i/2, x_(2i)=2a_i-1/2+b_i/2.

For a Wachs vertex x(pi,epsilon), T(x)=(pi(1),...,pi(m),epsilon). Consequently

T(conv(W_m)) = conv{(pi,epsilon):pi in S_m,epsilon in {-1,1}^m}.

For any nonempty finite A and B, conv(A x B)=conv(A) x conv(B): the forward inclusion follows from convexity; conversely, if a=sum_i lambda_i a_i and b=sum_j mu_j b_j, then (a,b)=sum_(i,j)lambda_i mu_j (a_i,b_j), with nonnegative coefficients summing to 1. Applying this identity gives T(conv(W_m))=P_m x C_m.

The standard permutohedron P_m has affine dimension m-1, because its coordinates always sum to m(m+1)/2 and the differences of permutations obtained by swapping neighboring values span the zero-sum subspace. Its vertices are all permutations of (1,...,m). Every such vertex is incident to exactly m-1 edges (swaps of consecutive *values*, in the positions where those values occur); equivalently its normal cone is defined by the strict ordering of m coordinate weights, and has m-1 facets in the quotient by the all-ones direction. Thus P_m is simple. C_m is an m-dimensional cube and each vertex has exactly m incident edges, so C_m is simple. Edges of a Cartesian product through (v,w) are precisely E x {w} and {v} x F for edges E,F incident to v,w. Hence each vertex of P_m x C_m has (m-1)+m=2m-1 incident edges, equal to the dimension of the product. The polytope is simple. QED.

## Further consequences
- Dimension: 2m-1.
- Vertices: 2^m m!.
- Edges: (2m-1) 2^(m-1) m!.
- Face lattice: product of the ordered-set-partition face lattice of P_m and the cube face lattice.
- All face numbers can be computed by convolution: if f_r(P_m) counts r-dimensional faces and f_s(C_m)=2^(m-s) binom(m,s), then f_k(conv(W_m))=sum_(r+s=k) f_r(P_m) f_s(C_m). Here f_r(P_m)=(m-r)! S(m,m-r), where S is a Stirling number of the second kind.
- Linear optimization over the polytope separates into sorting m pair-sum coefficients and choosing m independent signs, yielding O(m log m) comparisons.

## Formalization milestones (not yet checked)
1. Define the finite vertex set as image of Equiv.Perm (Fin m) x (Fin m -> Bool) under the block map.
2. Prove its equivalence to the original Wachs inverse-position condition, using Proposition 3.2 as the mathematical guide.
3. Define the affine equivalence T with explicit inverse and prove T maps vertices onto permutations x sign-vectors.
4. Formalize conv(A x B)=conv(A) x conv(B) for finite sets.
5. Use Mathlib's convex-polytope product / face / simple-polytope infrastructure, or explicitly count adjacent vertices via exposed edges.

## Provenance and cautions
- Primary source: Francesco Brenti and Paolo Sentinelli, *Wachs permutations, Bruhat order and weak order*, arXiv:2212.04932 (2022), §2 definition, §3 Proposition 3.2, §6 Conjecture 6.3.
- The source itself explicitly conjectures simplicity and checks m <= 5. The product decomposition here is a direct deduction from its block parametrization. This argument does not establish that the result has never appeared elsewhere.
- This file is a **mathematical proof draft**, not a compiled Lean proof or completed competition submission.
