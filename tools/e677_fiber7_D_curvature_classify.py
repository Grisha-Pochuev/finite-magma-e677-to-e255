"""Classify permutation symbols D on F_7 by translation curvature.

For t != 0, the derivative row is

    partial_t D(x) = D(x+t)-D(x).

An affine permutation has six constant derivative rows.  For a nonlinear D,
measure the distance from that situation by

    kappa(D) = sum_t (7 - max_v |{x: partial_t D(x)=v}|).

The script exhausts all 7! permutations and reports the first nonlinear
layer, including its exact derivative multiplicity signatures and scalar
conjugacy orbits.
"""

from __future__ import annotations

import argparse
import collections
import itertools


N = 7


def derivative_counts(permutation: tuple[int, ...], shift: int):
    counts = collections.Counter(
        (permutation[(x + shift) % N] - permutation[x]) % N
        for x in range(N)
    )
    return tuple(sorted(counts.values(), reverse=True))


def curvature_signature(permutation: tuple[int, ...]):
    rows = tuple(
        derivative_counts(permutation, shift) for shift in range(1, N)
    )
    cost = sum(N - row[0] for row in rows)
    return cost, tuple(sorted(rows))


def is_affine(permutation: tuple[int, ...]):
    return any(
        all(permutation[x] == (slope * x + offset) % N for x in range(N))
        for slope in range(1, N)
        for offset in range(N)
    )


def scalar_conjugates(permutation: tuple[int, ...]):
    result = []
    for scalar in range(1, N):
        inverse = pow(scalar, -1, N)
        result.append(tuple(
            scalar * permutation[(inverse * x) % N] % N for x in range(N)
        ))
    return tuple(result)


def render(permutation: tuple[int, ...]):
    return "".join(map(str, permutation))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--list-representatives", action="store_true")
    args = parser.parse_args()
    affine_permutations = {
        tuple((slope * x + offset) % N for x in range(N))
        for slope in range(1, N)
        for offset in range(N)
    }
    nonlinear = []
    for permutation in itertools.permutations(range(N)):
        if not is_affine(permutation):
            nonlinear.append((curvature_signature(permutation), permutation))

    minimum = min(signature[0] for signature, _ in nonlinear)
    first = [
        (signature, permutation)
        for signature, permutation in nonlinear
        if signature[0] == minimum
    ]
    by_signature = collections.Counter(signature[1] for signature, _ in first)
    first_set = {permutation for _, permutation in first}
    harmonic_double_swaps = set()
    for affine in affine_permutations:
        for anchor in range(N):
            for step in range(1, N):
                defect = list(range(N))
                left = anchor
                right = (anchor + step) % N
                defect[left], defect[right] = defect[right], defect[left]
                left = (anchor + 4 * step) % N
                right = (anchor + 5 * step) % N
                defect[left], defect[right] = defect[right], defect[left]
                harmonic_double_swaps.add(tuple(affine[defect[x]] for x in range(N)))
    if harmonic_double_swaps != first_set:
        raise AssertionError(
            "minimum-curvature layer is not the harmonic double-swap layer"
        )
    nearest_affine_centres = collections.Counter(
        sum(
            sum(left != right for left, right in zip(permutation, affine)) == 4
            for affine in affine_permutations
        )
        for permutation in first_set
    )
    representatives = sorted({
        min(conjugate for conjugate in scalar_conjugates(permutation))
        for permutation in first_set
    })

    print(
        f"permutations={len(nonlinear)+42}; affine=42; "
        f"nonlinear={len(nonlinear)}; minimum-kappa={minimum}; "
        f"first-layer={len(first_set)}; scalar-orbits={len(representatives)}; "
        f"harmonic-double-swaps={len(harmonic_double_swaps)}; "
        f"nearest-affine-centres={dict(sorted(nearest_affine_centres.items()))}"
    )
    for signature, count in sorted(by_signature.items()):
        print(f"signature={signature}; count={count}")
    if args.list_representatives:
        for representative in representatives:
            print(
                f"representative={render(representative)}; "
                f"signature={curvature_signature(representative)[1]}"
            )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
