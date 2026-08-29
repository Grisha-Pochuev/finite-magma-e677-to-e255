"""Classify the zero-target inverse-position displacement profiles."""

from __future__ import annotations

import collections
import itertools


N = 7


def scalar_conjugate(counts, scalar):
    result = [0] * (N - 1)
    for value in range(1, N):
        result[(scalar * value) % N - 1] = counts[value - 1]
    return tuple(result)


def main() -> int:
    rank_histogram = collections.Counter()
    profile_histogram = collections.Counter()
    vectors_by_profile = collections.defaultdict(set)
    derangements = 0
    for permutation in itertools.permutations(range(N)):
        displacement = tuple(
            (permutation[t] - t) % N for t in range(N)
        )
        if 0 in displacement:
            continue
        derangements += 1
        counts = tuple(displacement.count(value) for value in range(1, N))
        rank = sum(count > 0 for count in counts)
        profile = tuple(sorted((count for count in counts if count), reverse=True))
        rank_histogram[rank] += 1
        profile_histogram[profile] += 1
        vectors_by_profile[profile].add(counts)

    if set(rank_histogram) != {1, 3, 4, 5}:
        raise AssertionError(rank_histogram)
    nonconstant_vectors = 0
    scalar_orbits = 0
    print(
        f"derangements={derangements}; ranks={dict(sorted(rank_histogram.items()))}"
    )
    for profile in sorted(vectors_by_profile):
        if profile == (7,):
            continue
        vectors = vectors_by_profile[profile]
        representatives = {
            min(
                scalar_conjugate(counts, scalar)
                for scalar in range(1, N)
            )
            for counts in vectors
        }
        nonconstant_vectors += len(vectors)
        scalar_orbits += len(representatives)
        print(
            f"profile={profile}; derangements={profile_histogram[profile]}; "
            f"vectors={len(vectors)}; scalar-orbits={len(representatives)}"
        )
    if nonconstant_vectors != 108 or scalar_orbits != 18:
        raise AssertionError((nonconstant_vectors, scalar_orbits))
    print(
        f"nonconstant-vectors={nonconstant_vectors}; "
        f"scalar-orbits={scalar_orbits}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
