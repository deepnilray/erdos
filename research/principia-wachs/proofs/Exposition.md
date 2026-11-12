# Why the Wachs permutation polytope is simple

A permutation of 1 through 2m is called a Wachs permutation (in the even case considered here) when each pair of consecutive values (1,2), (3,4), ..., (2m−1,2m) occurs in neighboring positions. We plot permutations as points in R^(2m) by recording their one-line notation and ask: what is the geometry of their convex hull?

Brenti and Sentinelli conjectured that this polytope is *simple*: at each vertex, the number of incident edges equals its dimension. This is a global geometric statement, and a direct edge-by-edge calculation appears daunting because there are 2^m m! such permutations.

The key simplification is that the neighboring pairs must occupy the slots (1,2), (3,4), ..., (2m−1,2m). To specify a Wachs permutation, we choose which pair of values goes in each slot (a permutation pi of 1,...,m) and whether each pair is written forwards or backwards (m independent signs).

For a point x in R^(2m), define coordinates

    a_i=(x_(2i−1)+x_(2i)+1)/4,
    b_i=x_(2i)−x_(2i−1).

At a Wachs vertex, a=(pi(1),...,pi(m)) and each b_i is either −1 or +1. Conversely,

    x_(2i−1)=2a_i−1/2−b_i/2,
    x_(2i)=2a_i−1/2+b_i/2.

These inverse formulas show that this is an invertible affine change of coordinates. The vertex set becomes the Cartesian product of the permutation vectors and the vertices of an m-dimensional cube. Taking convex hulls preserves this product:

    conv(W(S_(2m))) ≅ Perm_m × [−1,1]^m.

A standard permutohedron is simple of dimension m−1; a cube is simple of dimension m; and the Cartesian product of simple polytopes is simple. Thus the Wachs polytope is simple of dimension 2m−1.

The same argument gives the complete face structure, not just the yes/no answer. In particular it has 2^m m! vertices and (2m−1)2^(m−1)m! edges. All higher face numbers follow by multiplying the face-generating polynomials of the permutohedron and cube.

**Status and provenance:** This is a proof draft based on the known Wachs block parametrization in Brenti–Sentinelli, *European Journal of Combinatorics* 119 (2024), Article 103804, Proposition 3.2. Its novelty has not been conclusively established. The complete theorem has not been Lean-verified. Do not present this exposition as a peer-reviewed or formally certified result.
