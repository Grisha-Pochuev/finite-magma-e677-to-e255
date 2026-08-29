"""Verify the exact T2 matching absorber with distinct Bad O7 rows."""

from __future__ import annotations


N = 7
P = (1, 0, 4, 6, 2, 5, 3)
CANONICAL_D = tuple(
    tuple(map(int, text))
    for text in ("0125634", "0145236", "1023546", "1024356")
)


def inverse(permutation):
    result = [0] * N
    for inp, value in enumerate(permutation):
        result[value] = inp
    return tuple(result)


def inverse_rows(table):
    return tuple(inverse(row) for row in table)


def perfect_matching(remaining):
    order = sorted(
        range(N), key=lambda t: len({remaining[t][h] for h in remaining[t]})
    )
    chosen = {}

    def search(index, used_values):
        if index == N:
            return True
        t = order[index]
        for h, value in remaining[t].items():
            if value in used_values:
                continue
            chosen[t] = h
            if search(index + 1, used_values | {value}):
                return True
            del chosen[t]
        return False

    if not search(0, set()):
        raise AssertionError("regular bipartite graph has no perfect matching")
    return chosen


def render(table):
    return "/".join("".join(map(str, row)) for row in table)


def verify(D):
    D_inverse = inverse(D)
    C = [
        [D_inverse[(t + h) % N] for h in range(N)]
        for t in range(N)
    ]
    W = [[(P[h] + p) % N for p in range(N)] for h in range(N)]
    O7 = [
        [W[(z + s) % N][s] for z in range(N)]
        for s in range(N)
    ]
    f = [
        [W[h][(t - C[t][h]) % N] for h in range(N)]
        for t in range(N)
    ]

    assert all(sorted(row) == list(range(N)) for row in C)
    assert all(sorted(C[t][h] for t in range(N)) == list(range(N)) for h in range(N))
    assert all(D[C[t][h]] == (t + h) % N for t in range(N) for h in range(N))
    assert all(sorted(row) == list(range(N)) for row in W)
    assert all(sorted(W[h][p] for h in range(N)) == list(range(N)) for p in range(N))
    assert len({tuple(row) for row in O7}) == N
    assert all(sorted(row) == list(range(N)) for row in O7)
    assert all(O7[s][0] != 0 for s in range(N))
    assert all(
        sorted(O7[s][(t - s) % N] for s in range(N)) == list(range(N))
        for t in range(N)
    )
    histogram = [sum(f[t][h] == value for t in range(N) for h in range(N)) for value in range(N)]
    assert histogram == [N] * N

    remaining = [dict(enumerate(f[t])) for t in range(N)]
    H = [[None] * N for _ in range(N)]
    for r in range(N):
        matching = perfect_matching(remaining)
        for t, h in matching.items():
            H[t][r] = h
            del remaining[t][h]
    assert all(not row for row in remaining)
    assert all(sorted(row) == list(range(N)) for row in H)
    V = [
        [W[H[t][r]][(t - C[t][H[t][r]]) % N] for t in range(N)]
        for r in range(N)
    ]
    assert all(sorted(row) == list(range(N)) for row in V)
    inverse_O7 = inverse_rows(O7)
    tuple6_failures = []
    for s in range(N):
        for t in range(N):
            q = O7[t][s]
            z = inverse_O7[t][s]
            u = H[s][z]
            if C[q][u] != (q - t) % N:
                tuple6_failures.append((s, t))
    return C, O7, H, V, histogram, tuple6_failures


def main() -> int:
    difference = tuple((P[h] - h) % N for h in range(N))
    assert sorted(P) == list(range(N))
    assert sorted(difference) == list(range(N))
    assert all((P[h] + h) % N != 0 for h in range(N))
    print(
        f"P={''.join(map(str, P))}; P-id={''.join(map(str, difference))}; "
        "complete-mapping=True; anti-fixed-free=True"
    )
    for D in CANONICAL_D:
        C, O7, H, V, histogram, tuple6_failures = verify(D)
        print(
            f"D={''.join(map(str, D))}; histogram={histogram}; "
            f"O7-distinct={len({tuple(row) for row in O7})}; "
            f"tuple6-failures={len(tuple6_failures)}; "
            f"failure-cells={tuple6_failures}; H={render(H)}; V={render(V)}"
        )
    print("T2 MATCHING ABSORBER VERIFIED FOR ALL FOUR CANONICAL D")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
