# Applications and further mathematical consequences

The affine decomposition Q_m ≅ Perm_m × [−1,1]^m gives several exact consequences:

1. **Face enumeration.** For 0≤k≤2m−1, the number of k-dimensional faces is

       f_k(Q_m) = Σ_(r+s=k) (m−r)! S(m,m−r) binom(m,s) 2^(m−s),

   where S(m,j) is a Stirling number of the second kind and 0≤r≤m−1, 0≤s≤m. In particular f_0=2^m m!, f_1=(2m−1)2^(m−1)m!.

2. **Facet description.** In transformed coordinates a,b, impose sum a_i=m(m+1)/2, the majorization inequalities sum_(i∈I) a_i ≥ |I|(|I|+1)/2 for every nonempty proper I⊂[m], and −1≤b_i≤1. For m≥2 there are 2^m−2+2m facets.

3. **Efficient linear optimization.** For any linear objective c·x, transform its coefficients into an a component and m independent b components. Optimize the permutohedron term by sorting, and optimize each cube term by choosing a sign. Total comparison complexity is O(m log m).

4. **Combinatorial adjacency.** Each vertex has m−1 neighbors from the permutohedron factor (swapping adjacent ranks) and m neighbors from flipping one orientation sign, for 2m−1 incident edges.

5. **Formalization methodology.** The map gives a route to a reusable Lean library result: affine images commute with convex hulls, convex hulls of finite Cartesian products factor, and simplicity is stable under products and affine equivalence. These results may be useful in subsequent machine-checked polytope proofs; **they are prospective, not implemented or verified here**.

These are applications in combinatorics, discrete geometry and optimization. No physical or industrial application has been claimed.

**Publication caution:** The geometric decomposition is a candidate contribution; publication priority and full Lean verification are open checks.
