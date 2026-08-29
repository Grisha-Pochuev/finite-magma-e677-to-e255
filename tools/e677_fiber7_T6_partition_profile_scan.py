"""Search coherent Latin seeds with matching z/rho fibre-size profiles.

For a partition of seven points, the pair (C2,C3), where
Ck=sum_B binomial(|B|,k), uniquely determines the block-size profile.
This script requires equality of both invariants for every target s and then
minimizes the remaining exact pair-kernel placement error.
"""

from __future__ import annotations

import argparse
import itertools
import random
import time

import numpy as np

import e677_fiber7_T6_kernel_pair_clique_search as clique
import e677_fiber7_T6_latin_seed_search as latin


N = 7


def collision_invariants(values):
    pair = np.zeros(values.shape[:-1], dtype=np.int16)
    triple = np.zeros(values.shape[:-1], dtype=np.int16)
    for left in range(N):
        for right in range(left + 1, N):
            pair += values[..., left] == values[..., right]
            for third in range(right + 1, N):
                triple += (
                    (values[..., left] == values[..., right])
                    & (values[..., left] == values[..., third])
                )
    return pair, triple


def analyse(O7, A_maps):
    Q = np.asarray(O7, dtype=np.int16).T
    Z = np.asarray(latin.inverse_rows(O7), dtype=np.int16).T
    z_pair, z_triple = collision_invariants(Z)
    z_degree = np.zeros(N, dtype=np.int16)
    for s in range(N):
        for left in range(N):
            for right in range(left + 1, N):
                if Z[s, left] == Z[s, right]:
                    z_degree[left] += 1
                    z_degree[right] += 1
    t_values = np.arange(N, dtype=np.int16)[None, :]
    results = []
    for D_index, D in enumerate(clique.CANONICAL_D):
        D_array = np.asarray(D, dtype=np.int16)
        first = D_array[(Q - t_values) % N]
        rho = (first[None, :, :] - A_maps[:, Q]) % N
        rho_pair, rho_triple = collision_invariants(rho)
        rho_degree = np.zeros((len(A_maps), N), dtype=np.int16)
        for s in range(N):
            for left in range(N):
                for right in range(left + 1, N):
                    equal = rho[:, s, left] == rho[:, s, right]
                    rho_degree[:, left] += equal
                    rho_degree[:, right] += equal
        profile_match = np.all(
            (rho_pair == z_pair[None, :])
            & (rho_triple == z_triple[None, :]),
            axis=1,
        )
        degree_match = np.all(rho_degree == z_degree[None, :], axis=1)
        epsilon = np.zeros(len(A_maps), dtype=np.int16)
        for s in range(N):
            for left in range(N):
                for right in range(left + 1, N):
                    actual = rho[:, s, left] == rho[:, s, right]
                    desired = Z[s, left] == Z[s, right]
                    epsilon += actual != desired
        results.append(
            (D_index, profile_match, degree_match, epsilon, z_pair, z_triple, z_degree)
        )
    return results


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--seconds", type=float, default=120.0)
    parser.add_argument("--bases", type=int, default=50)
    parser.add_argument("--labelings", type=int, default=100)
    parser.add_argument("--seed", type=int, default=677257)
    args = parser.parse_args()

    started = time.time()
    deadline = started + args.seconds
    rng = random.Random(args.seed)
    A_tuples = [(0, *tail) for tail in itertools.permutations(range(1, N))]
    A_maps = np.asarray(A_tuples, dtype=np.int16)
    seen_bases = set()
    generated = tested = pair_cases = profile_matches = degree_matches = 0
    best_epsilon = None
    best_degree_epsilon = None
    best_data = None

    try:
        while generated < args.bases and time.time() < deadline:
            square, _ = latin.reduced_latin(rng, deadline)
            key = tuple(value for row in square for value in row)
            if key in seen_bases:
                continue
            seen_bases.add(key)
            generated += 1
            for _ in range(args.labelings):
                if time.time() >= deadline:
                    raise latin.DeadlineReached
                transformed = latin.relabel_bad_diagonal(square, rng)
                O7 = latin.O_rows(transformed)
                if len(set(O7)) != N:
                    continue
                tested += 1
                for (
                    D_index,
                    matches,
                    degree_match,
                    epsilon,
                    z_pair,
                    z_triple,
                    z_degree,
                ) in analyse(O7, A_maps):
                    pair_cases += len(A_tuples)
                    indices = np.flatnonzero(matches)
                    profile_matches += len(indices)
                    if not len(indices):
                        continue
                    scores = epsilon[indices]
                    position = int(np.argmin(scores))
                    A_index = int(indices[position])
                    local_score = int(scores[position])
                    if best_epsilon is None or local_score < best_epsilon:
                        best_epsilon = local_score
                        best_data = (
                            O7,
                            D_index,
                            A_index,
                            tuple(map(int, z_pair)),
                            tuple(map(int, z_triple)),
                        )
                        print(
                            f"profile-match best epsilon={best_epsilon}/147; "
                            f"matches={profile_matches}; bases={generated}; tested={tested}; "
                            f"D={D_index}; A={''.join(map(str,A_tuples[A_index]))}",
                            flush=True,
                        )
                    if local_score == 0:
                        D = clique.CANONICAL_D[D_index]
                        A = A_tuples[A_index]
                        K = clique.reconstruct_K(O7, A, D)
                        clique.audit(O7, A, D, K)
                        print(
                            f"PROFILE-MATCHED T6 CORE; D={''.join(map(str,D))}; "
                            f"A={''.join(map(str,A))}; "
                            f"profile={clique.kernel_profile(O7)}; "
                            f"elapsed={time.time()-started:.3f}s"
                        )
                        print(f"O7={clique.render(O7)}")
                        print(f"K={clique.render(K)}")
                        return 0
                    degree_indices = np.flatnonzero(matches & degree_match)
                    degree_matches += len(degree_indices)
                    if len(degree_indices):
                        degree_scores = epsilon[degree_indices]
                        degree_position = int(np.argmin(degree_scores))
                        degree_A_index = int(degree_indices[degree_position])
                        degree_score = int(degree_scores[degree_position])
                        if (
                            best_degree_epsilon is None
                            or degree_score < best_degree_epsilon
                        ):
                            best_degree_epsilon = degree_score
                            print(
                                f"degree-match best epsilon={degree_score}/147; "
                                f"degree={tuple(map(int,z_degree))}; "
                                f"matches={degree_matches}; D={D_index}; "
                                f"A={''.join(map(str,A_tuples[degree_A_index]))}",
                                flush=True,
                            )
    except latin.DeadlineReached:
        pass

    print(
        f"PROFILE SCAN COMPLETE; bases={generated}; tested={tested}; "
        f"(O,A,D)-cases={pair_cases}; profile-matches={profile_matches}; "
        f"degree-matches={degree_matches}; best-epsilon={best_epsilon}; "
        f"degree-best-epsilon={best_degree_epsilon}; "
        f"elapsed={time.time()-started:.3f}s"
    )
    if best_data is not None:
        O7, D_index, A_index, z_pair, z_triple = best_data
        print(
            f"best D={''.join(map(str,clique.CANONICAL_D[D_index]))}; "
            f"A={''.join(map(str,A_tuples[A_index]))}; C2={z_pair}; C3={z_triple}; "
            f"O7={clique.render(O7)}"
        )
    return 3


if __name__ == "__main__":
    raise SystemExit(main())
