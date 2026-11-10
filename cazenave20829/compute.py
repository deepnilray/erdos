"""Reproduce the bounded search and audit the exact counterexample certificates."""

import argparse
from fractions import Fraction
from itertools import combinations


def joined_cliques(k, length, missing):
    """Two k-cliques, a missing star at each port, and a path between ports."""
    n = 2 * k + length - 1
    edges = set()
    for start in (0, k):
        edges.update(combinations(range(start, start + k), 2))
        for leaf in range(start + 1, start + 1 + missing):
            edges.remove((start, leaf))
    path = [0, *range(2 * k, n), k]
    edges.update(tuple(sorted(edge)) for edge in zip(path, path[1:]))
    return n, edges


def require(condition, message):
    if not condition:
        raise ValueError(message)


def control(name, check):
    try:
        check()
    except ValueError as error:
        print(f"CONTROL FIRED ({name}): {error}")
    else:
        raise RuntimeError(f"silent control: {name}")


def check_graph(n, edges):
    neighbors = [set() for _ in range(n)]
    for u, v in edges:
        require(0 <= u < v < n, f"invalid edge {(u, v)}")
        neighbors[u].add(v)
        neighbors[v].add(u)
    seen, pending = {0}, [0]
    while pending:
        for v in neighbors[pending.pop()] - seen:
            seen.add(v)
            pending.append(v)
    require(len(seen) == n, "disconnected witness")
    return [len(row) for row in neighbors]


def check_adjacency(edges, x, y, cutoff):
    require(len(x) == len(y), "dimension mismatch")
    require(all(a * b == 0 for a, b in zip(x, y)), "intersecting supports")
    mixed = sum(x[u] * y[v] + x[v] * y[u] for u, v in edges)
    require(mixed == 0, f"mixed adjacency form is {mixed}")
    values = []
    for vector in (x, y):
        squared_norm = sum(a * a for a in vector)
        require(squared_norm > 0, "zero witness vector")
        value = Fraction(2 * sum(vector[u] * vector[v] for u, v in edges), squared_norm)
        require(value > cutoff, f"adjacency Rayleigh quotient {value} <= {cutoff}")
        values.append(value)
    return min(values)


def check_laplacian(n, edges, cutoff):
    degrees = check_graph(n, edges)
    residual = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    for u in range(n):
        residual[u][u] = cutoff - degrees[u]
    for u, v in edges:
        residual[u][v] = residual[v][u] = Fraction(1)
    pivots = []
    for i in range(n):
        pivot = residual[i][i]
        require(pivot > 0, f"nonpositive LDL pivot {i} = {pivot}")
        pivots.append(pivot)
        for u in range(i + 1, n):
            if not residual[u][i]:
                continue
            for v in range(u, n):
                update = residual[u][i] * residual[v][i] / pivot
                residual[u][v] -= update
                residual[v][u] = residual[u][v]
    return min(pivots)


def witnesses(k, length):
    if (k, length) == (4, 4):
        left = [3, 3, 4, 4, 0, 0, 0, 0, 1, 0, 0]
        right = [0, 0, 0, 0, 3, 3, 4, 4, 0, 0, 1]
        return left, right, Fraction(37, 8)
    weights = [5, 5] + [6] * (k - 2)
    return weights + [0] * (k + 1), [0] * k + weights + [0], Fraction(k) + Fraction(7, 10)


def run_exact():
    n, edges = joined_cliques(4, 4, 1)
    left, right, cutoff = witnesses(4, 4)
    _, restored = joined_cliques(4, 4, 0)
    control("Laplacian, restored internal edges", lambda: check_laplacian(n, restored, cutoff))
    control("adjacency, planted mixed edge", lambda: check_adjacency(edges | {(8, 10)}, left, right, cutoff - 2))
    for k, length in [(4, 4), *((k, 2) for k in range(6, 26))]:
        n, edges = joined_cliques(k, length, 1)
        left, right, cutoff = witnesses(k, length)
        rayleigh = check_adjacency(edges, left, right, cutoff - 2)
        pivot = check_laplacian(n, edges, cutoff)
        print(f"VERIFIED exact n={n}, k={k}, length={length}, edges={len(edges)}, adjacency={rayleigh}, min LDL pivot={pivot}")


def spectrum(n, edges):
    import numpy as np

    adjacency = np.zeros((n, n))
    for u, v in edges:
        adjacency[u, v] = adjacency[v, u] = 1
    laplacian = np.diag(adjacency.sum(axis=1)) - adjacency
    return float(np.linalg.eigvalsh(adjacency)[-2]), float(np.linalg.eigvalsh(laplacian)[-1])


def run_sweep():
    def check_k2(edges):
        lam, mu = spectrum(2, edges)
        require(abs(lam + 1) < 1e-12 and abs(mu - 2) < 1e-12, f"K2 oracle failed: {(lam, mu)}")

    check_k2({(0, 1)})
    control("sweep, deleted K2 edge", lambda: check_k2(set()))
    for length in range(1, 7):
        for missing in (0, 1):
            hits = []
            for k in range(3, 51):
                n, edges = joined_cliques(k, length, missing)
                lam, mu = spectrum(n, edges)
                if mu - lam < 2 - 1e-10:
                    hits.append((k, n, round(mu - lam, 12)))
            first = hits[0] if hits else None
            print(f"VERIFIED numerical length={length} missing={missing} k=3..50 hits={len(hits)} first={first}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("exact", "sweep"))
    args = parser.parse_args()
    if args.mode == "exact":
        run_exact()
    else:
        run_sweep()
