# PRINCIPIA Wachs research audit — 12 November 2026

## New structural consequence: an explicit zonotope and normal fan

Assume the proved-in-draft affine equivalence T(Q_m)=Perm_m × [-1,1]^m, with T(x)=(a,b), a_i=(x_{2i-1}+x_{2i}+1)/4 and b_i=x_{2i}-x_{2i-1}.

Write e_1,...,e_m for the standard basis of R^m and [u,v] for the closed segment from u to v. Then

Perm_m = (1,...,1) + Σ_{1≤i<j≤m} [e_i,e_j].       (1)

Proof: the right side is a Minkowski sum of segments. A generic linear functional c maximizes each segment at e_i or e_j according as c_i>c_j or c_j>c_i. If c has distinct coordinates, the resulting maximizing vector has coordinate 1 plus the number of other coordinates with smaller c-value, so its coordinates are 1,...,m in the rank order of c. Conversely every permutation vector occurs for a suitable strict ranking of c. Thus both polytopes have exactly the same vertices and are equal. (Non-generic functionals follow by continuity.)

Therefore, writing (a,b) in R^m × R^m,

T(Q_m) = ((1,...,1),(-1,...,-1))
       + Σ_{i<j} [(e_i,0),(e_j,0)]
       + Σ_i [(0,0),(0,2e_i)].                         (2)

This is a zonotope, i.e. a Minkowski sum of line segments, with m(m-1)/2 + m = m(m+1)/2 generating segments. Since T is an invertible affine map, Q_m itself is a zonotope.

The normal fan (partition of objective vectors by their maximizing faces) in (a,b) coordinates is the product of the braid fan, with walls c_i=c_j, and the coordinate-orthant fan, with walls d_i=0. For generic (c,d), the unique maximizing vertex is obtained by ranking c_i and setting b_i=sign(d_i). This is a direct geometric explanation of the earlier optimization algorithm and partial-cube encoding.

This is a CONSEQUENCE of the central product theorem, not independent evidence for that theorem, and is not claimed to be novel beyond standard zonotope theory.

## Independent check against original definition

The accompanying `verify_direct_hull_2026_11_12.py` enumerates all (2m)! original permutations, filters by |pos(2j-1)-pos(2j)|=1, projects away one redundant coordinate, and invokes SciPy/Qhull on the ORIGINAL Wachs vectors, without generating points from the proposed product parametrization. For m=2 it finds 8 vertices, affine dimension 3, and 6 supporting hyperplanes; for m=3 it finds 48 vertices, affine dimension 5, and 12 supporting hyperplanes. These match the predicted 2^m m! vertices, dimension 2m-1, and 2m+2^m-2 facets. Qhull uses floating-point arithmetic, so these checks are diagnostics rather than a formal proof.

## Remaining critical formalization chain

1. Prove the tiling lemma: any partition of Fin(2m) into disjoint consecutive 2-element subsets must be the canonical adjacent-position tiling.
2. Prove the original inverse-position definition of even Wachs permutations is equivalent to block parametrization by (π,ε).
3. Define the coordinate affine equivalence in mathlib and prove the finite vertex-set image identity.
4. Prove convex hull of Cartesian products equals Cartesian product of convex hulls.
5. Transfer known simplicity of the permutohedron and cube, or prove simplicity from explicit facet incidences.

The existing `WachsAffineCore_2026_11_11.lean` proves only coordinate algebra on paper. It is NOT compiled, and the full Lean formalization remains unfinished.

## Priority caveat

The original Brenti–Sentinelli paper is *Wachs permutations, Bruhat order and weak order*, European Journal of Combinatorics 119 (2024), 103804, DOI 10.1016/j.ejc.2023.103804. Public institutional record: https://re.public.polimi.it/handle/11311/1267078. A 12 November 2026 web search did not establish a published prior affine-product theorem; absence of search hits is not proof of originality.

No account access, publication, registration, or submission was performed.
