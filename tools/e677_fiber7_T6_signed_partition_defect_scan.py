"""Scan the signed T6 partition defect on coherent nonlinear Latin seeds.

For each target s, C(z_s) and C(rho_s) count equal row pairs.  The signed
vector Delta_s=C(z_s)-C(rho_s) must vanish in every exact T6 core.  This
script determines whether the scalar sum or the full seven-vector supplies
a useful obstruction, while retaining the exact pair-kernel score epsilon.
"""

from __future__ import annotations

import argparse
import itertools
import random
import time
from collections import Counter

import numpy as np

import e677_fiber7_T6_kernel_pair_clique_search as clique
import e677_fiber7_T6_latin_seed_search as latin


N = 7


def analyse(O7, A_maps):
    Q = np.asarray(O7, dtype=np.int16).T
    Z = np.asarray(latin.inverse_rows(O7), dtype=np.int16).T
    z_collisions = np.zeros(N, dtype=np.int16)
    for s in range(N):
        for left in range(N):
            for right in range(left + 1, N):
                z_collisions[s] += Z[s, left] == Z[s, right]

    t_values = np.arange(N, dtype=np.int16)[None, :]
    results = []
    for D_index, D in enumerate(clique.CANONICAL_D):
        D_array = np.asarray(D, dtype=np.int16)
        first = D_array[(Q - t_values) % N]
        rho = (first[None, :, :] - A_maps[:, Q]) % N
        rho_collisions = np.zeros((len(A_maps), N), dtype=np.int16)
        epsilon = np.zeros(len(A_maps), dtype=np.int16)
        for s in range(N):
            for left in range(N):
                for right in range(left + 1, N):
                    actual = rho[:, s, left] == rho[:, s, right]
                    desired = Z[s, left] == Z[s, right]
                    rho_collisions[:, s] += actual
                    epsilon += actual != desired
        delta = z_collisions[None, :] - rho_collisions
        results.append((D_index, delta, epsilon))
    return results


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--seconds", type=float, default=120.0)
    parser.add_argument("--bases", type=int, default=50)
    parser.add_argument("--labelings", type=int, default=100)
    parser.add_argument("--seed", type=int, default=677256)
    args = parser.parse_args()

    started = time.time()
    deadline = started + args.seconds
    rng = random.Random(args.seed)
    A_tuples = [(0, *tail) for tail in itertools.permutations(range(1, N))]
    A_maps = np.asarray(A_tuples, dtype=np.int16)
    seen_bases = set()
    generated = tested = pair_cases = 0
    scalar_zero = vector_zero = 0
    scalar_distribution = Counter()
    best_l1 = None
    best_vector_epsilon = None
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
                for D_index, delta, epsilon in analyse(O7, A_maps):
                    pair_cases += len(A_tuples)
                    totals = delta.sum(axis=1)
                    values, counts = np.unique(totals, return_counts=True)
                    scalar_distribution.update(
                        {int(value): int(count) for value, count in zip(values, counts)}
                    )
                    scalar_zero += int(np.count_nonzero(totals == 0))
                    l1 = np.abs(delta).sum(axis=1)
                    local_index = int(np.argmin(l1))
                    local_l1 = int(l1[local_index])
                    if best_l1 is None or local_l1 < best_l1:
                        best_l1 = local_l1
                        best_data = (
                            O7,
                            D_index,
                            local_index,
                            tuple(map(int, delta[local_index])),
                            int(epsilon[local_index]),
                        )
                        print(
                            f"best |Delta|_1={best_l1}; Delta={best_data[3]}; "
                            f"epsilon={best_data[4]}; bases={generated}; tested={tested}; "
                            f"D={D_index}; A={''.join(map(str,A_tuples[local_index]))}",
                            flush=True,
                        )
                    zero_indices = np.flatnonzero(np.all(delta == 0, axis=1))
                    vector_zero += len(zero_indices)
                    if len(zero_indices):
                        scores = epsilon[zero_indices]
                        position = int(np.argmin(scores))
                        A_index = int(zero_indices[position])
                        candidate_score = int(scores[position])
                        if best_vector_epsilon is None or candidate_score < best_vector_epsilon:
                            best_vector_epsilon = candidate_score
                            best_data = (O7, D_index, A_index, (0,) * N, candidate_score)
                            print(
                                f"zero-vector best epsilon={candidate_score}/147; "
                                f"bases={generated}; tested={tested}; D={D_index}; "
                                f"A={''.join(map(str,A_tuples[A_index]))}",
                                flush=True,
                            )
                        if candidate_score == 0:
                            D = clique.CANONICAL_D[D_index]
                            A = A_tuples[A_index]
                            K = clique.reconstruct_K(O7, A, D)
                            clique.audit(O7, A, D, K)
                            print(
                                f"SIGNED-DEFECT T6 CORE; D={''.join(map(str,D))}; "
                                f"A={''.join(map(str,A))}; "
                                f"profile={clique.kernel_profile(O7)}; "
                                f"elapsed={time.time()-started:.3f}s"
                            )
                            print(f"O7={clique.render(O7)}")
                            print(f"K={clique.render(K)}")
                            return 0
    except latin.DeadlineReached:
        pass

    print(
        f"SIGNED DEFECT SCAN COMPLETE; bases={generated}; tested={tested}; "
        f"(O,A,D)-cases={pair_cases}; scalar-zero={scalar_zero}; "
        f"vector-zero={vector_zero}; best-L1={best_l1}; "
        f"zero-vector-best-epsilon={best_vector_epsilon}; "
        f"elapsed={time.time()-started:.3f}s"
    )
    print(f"scalar-Delta-distribution={dict(sorted(scalar_distribution.items()))}")
    if best_data is not None:
        O7, D_index, A_index, delta, epsilon = best_data
        print(
            f"best D={''.join(map(str,clique.CANONICAL_D[D_index]))}; "
            f"A={''.join(map(str,A_tuples[A_index]))}; Delta={delta}; "
            f"epsilon={epsilon}; O7={clique.render(O7)}"
        )
    return 3


if __name__ == "__main__":
    raise SystemExit(main())
