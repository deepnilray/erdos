#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <gmpxx.h>
#include <iostream>
#include <string>

constexpr int capacity = 11;

struct Graph {
    int n = 0;
    std::array<unsigned, capacity> neighbors{};
    std::array<int, capacity> degrees{};
};

Graph decode(const std::string& data) {
    Graph g;
    if (data.empty()) std::exit(2);
    g.n = data[0] - 63;
    if (g.n < 2 || g.n > capacity || data.size() != size_t(1 + (g.n * (g.n - 1) / 2 + 5) / 6))
        std::exit(2);
    int index = 0;
    for (int j = 1; j < g.n; ++j) {
        for (int i = 0; i < j; ++i, ++index) {
            const int value = data[1 + index / 6] - 63;
            if (value < 0 || value > 63) std::exit(2);
            if ((value >> (5 - index % 6)) & 1) {
                g.neighbors[i] |= 1U << j;
                g.neighbors[j] |= 1U << i;
                ++g.degrees[i];
                ++g.degrees[j];
            }
        }
    }
    return g;
}

// Bareiss elimination. A zero leading determinant is inconclusive at this
// threshold. A negative pivot in a leading submatrix also certifies one
// negative eigenvalue in the full symmetric matrix.
template<class Int>
int negative_inertia(const Graph& g, int p, int q, bool laplacian, int stop,
                     bool flip_pivot_sign = false) {
    Int b[capacity][capacity]{};
    for (int j = 0; j < g.n; ++j) {
        b[j][j] = p - (laplacian ? q * g.degrees[j] : 0);
        for (int i = 0; i < j; ++i) {
            if (g.neighbors[j] & (1U << i)) b[j][i] = laplacian ? q : -q;
        }
    }
    Int previous = 1;
    int negative = 0;
    for (int j = 0; j < g.n; ++j) {
        const Int pivot = b[j][j];
        if (pivot == 0) return -1;
        const bool negative_pivot = (pivot < 0) != (previous < 0);
        negative += negative_pivot != flip_pivot_sign;
        if (negative >= stop) return negative;
        for (int r = j + 1; r < g.n; ++r) {
            for (int c = j + 1; c <= r; ++c) {
                b[r][c] = (pivot * b[r][c] - b[r][j] * b[c][j]) / previous;
            }
        }
        previous = pivot;
    }
    return negative;
}

int verify(const Graph& g) {
    const int delta = *std::max_element(g.degrees.begin(), g.degrees.begin() + g.n);
    if (delta == 0) return 0;
    unsigned maximum_vertices = 0;
    for (int i = 0; i < g.n; ++i) {
        if (g.degrees[i] == delta) maximum_vertices |= 1U << i;
    }
    for (int i = 0; i < g.n; ++i) {
        if ((maximum_vertices & ~(g.neighbors[i] | (1U << i))) == 0) return 1;
    }
    // For n <= 10, the row norms of (delta - 1)I - A are < 9. Products
    // in this branch use minors of order at most 9, so 2 * 9^18 bounds
    // the integer numerators, safely inside signed 64-bit range.
    int ia = g.n <= 10
        ? negative_inertia<int64_t>(g, delta - 1, 1, false, 2)
        : negative_inertia<mpz_class>(g, delta - 1, 1, false, 2);
    if (0 <= ia && ia <= 1) return 2;
    for (int q : {8, 16, 32, 64}) {
        for (int step = -1; step < q; ++step) {
            const int p = q * (delta - 1) + step;
            ia = negative_inertia<mpz_class>(g, p, q, false, 2);
            if (ia < 0 || ia > 1) continue;
            if (step <= 0 || negative_inertia<mpz_class>(g, p + 2 * q, q, true, 1) == 1)
                return 3;
        }
    }
    return 0;
}

void controls(bool mutate) {
    const Graph edge = decode("A_");
    if (edge.n != 2 || edge.degrees[0] != 1 || edge.degrees[1] != 1) std::exit(3);
    if (negative_inertia<int64_t>(edge, 1, 2, false, 2) != 1 ||
        negative_inertia<int64_t>(edge, 3, 2, false, 2, mutate) != 0) {
        std::cerr << "K2 control detected an incorrect inertia classification\n";
        std::exit(3);
    }
    Graph two_triangles;
    two_triangles.n = 6;
    for (int i = 0; i < 6; ++i) {
        two_triangles.neighbors[i] = (7U << (3 * (i / 3))) & ~(1U << i);
        two_triangles.degrees[i] = 2;
    }
    if (verify(two_triangles) != 0) std::exit(4);
    if (verify(decode("J^??W]??GO_")) != 0) std::exit(5);
}

int main(int argc, char**) {
    controls(argc > 1);
    std::array<uint64_t, 4> counts{};
    std::string graph6;
    while (std::getline(std::cin, graph6)) {
        const Graph g = decode(graph6);
        const int status = verify(g);
        ++counts[status];
        if (status == 0 && counts[0] <= 10) std::cout << "UNRESOLVED " << graph6 << '\n';
    }
    std::cout << "unresolved=" << counts[0] << " interlacing=" << counts[1]
              << " integer_inertia=" << counts[2] << " rational_inertia=" << counts[3] << '\n';
    return counts[0] != 0;
}
