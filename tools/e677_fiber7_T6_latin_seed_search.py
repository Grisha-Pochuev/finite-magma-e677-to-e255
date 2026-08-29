"""Constructive search for an exact T6 core through nonlinear Latin seeds.

For a Latin square L define O_t(s)=L(t,t+s).  Then the cyclic Q-fibre
condition and every relative-permutation triangle cocycle hold automatically.
The script generates randomized reduced Latin squares, relabels them so that
L(t,t)!=0 (Badness), and checks all 720 normalized A and four canonical D by
the exact condition ker(z_s)=ker(rho_s).

A reported witness is an exact tuple-6 kernel core, not yet a counterexample
to E677 -> E255.  A bounded miss is only a search boundary.
"""

from __future__ import annotations

import argparse
import itertools
import random
import time

import numpy as np

import e677_fiber7_T6_kernel_pair_clique_search as clique


N = 7
FULL = (1 << N) - 1


class DeadlineReached(Exception):
    pass


def reduced_latin(rng, deadline):
    grid = [[-1] * N for _ in range(N)]
    row_used = [0] * N
    column_used = [0] * N

    def place(row, column, value):
        grid[row][column] = value
        row_used[row] |= 1 << value
        column_used[column] |= 1 << value

    for value in range(N):
        place(0, value, value)
    for value in range(1, N):
        place(value, 0, value)

    nodes = 0

    def visit():
        nonlocal nodes
        nodes += 1
        if nodes % 1024 == 0 and time.time() >= deadline:
            raise DeadlineReached
        best = None
        best_values = None
        ties = []
        for row in range(1, N):
            for column in range(1, N):
                if grid[row][column] >= 0:
                    continue
                allowed = FULL & ~(row_used[row] | column_used[column])
                size = allowed.bit_count()
                if size == 0:
                    return False
                if best_values is None or size < best_values.bit_count():
                    best = (row, column)
                    best_values = allowed
                    ties = [(row, column, allowed)]
                elif size == best_values.bit_count():
                    ties.append((row, column, allowed))
        if best_values is None:
            return True
        row, column, allowed = rng.choice(ties)
        values = [value for value in range(N) if allowed & (1 << value)]
        rng.shuffle(values)
        for value in values:
            grid[row][column] = value
            row_used[row] |= 1 << value
            column_used[column] |= 1 << value
            if visit():
                return True
            row_used[row] ^= 1 << value
            column_used[column] ^= 1 << value
            grid[row][column] = -1
        return False

    if not visit():
        raise AssertionError("random reduced Latin search exhausted")
    return tuple(tuple(row) for row in grid), nodes


def relabel_bad_diagonal(square, rng):
    rows = list(range(N))
    symbols = list(range(N))
    rng.shuffle(rows)
    rng.shuffle(symbols)
    for _ in range(100):
        columns = list(range(N))
        rng.shuffle(columns)
        transformed = tuple(
            tuple(symbols[square[rows[row]][columns[column]]] for column in range(N))
            for row in range(N)
        )
        if all(transformed[t][t] != 0 for t in range(N)):
            return transformed
    raise AssertionError("failed to choose a bad diagonal")


def O_rows(square):
    return tuple(
        tuple(square[t][(t + s) % N] for s in range(N))
        for t in range(N)
    )


def inverse_rows(O7):
    rows = []
    for row in O7:
        inverse = [0] * N
        for inp, value in enumerate(row):
            inverse[value] = inp
        rows.append(tuple(inverse))
    return tuple(rows)


def check_seed(O7, A_maps):
    if len(set(O7)) != N:
        return None, None
    Q = np.asarray(O7, dtype=np.int16).T  # target s, row t
    Z = np.asarray(inverse_rows(O7), dtype=np.int16).T
    t_values = np.arange(N, dtype=np.int16)[None, :]
    best = None
    for D_index, D in enumerate(clique.CANONICAL_D):
        D_array = np.asarray(D, dtype=np.int16)
        first = D_array[(Q - t_values) % N]
        rho = (first[None, :, :] - A_maps[:, Q]) % N
        violations = np.zeros(len(A_maps), dtype=np.int16)
        for s in range(N):
            for left in range(N):
                for right in range(left + 1, N):
                    desired = Z[s, left] == Z[s, right]
                    actual = rho[:, s, left] == rho[:, s, right]
                    violations += actual != desired
        local_index = int(np.argmin(violations))
        local_score = int(violations[local_index])
        candidate = (local_score, D_index, local_index)
        if best is None or candidate < best:
            best = candidate
        if local_score == 0:
            return candidate, rho[local_index]
    return best, None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--seconds", type=float, default=120.0)
    parser.add_argument("--bases", type=int, default=50)
    parser.add_argument("--labelings", type=int, default=100)
    parser.add_argument("--seed", type=int, default=677255)
    args = parser.parse_args()

    started = time.time()
    deadline = started + args.seconds
    rng = random.Random(args.seed)
    A_tuples = [(0, *tail) for tail in itertools.permutations(range(1, N))]
    A_maps = np.asarray(A_tuples, dtype=np.int16)
    seen_bases = set()
    generated = tested = duplicate_rows = total_nodes = 0
    best = None
    best_data = None

    try:
        while generated < args.bases and time.time() < deadline:
            square, nodes = reduced_latin(rng, deadline)
            total_nodes += nodes
            key = tuple(value for row in square for value in row)
            if key in seen_bases:
                continue
            seen_bases.add(key)
            generated += 1
            for _ in range(args.labelings):
                if time.time() >= deadline:
                    raise DeadlineReached
                transformed = relabel_bad_diagonal(square, rng)
                O7 = O_rows(transformed)
                if len(set(O7)) != N:
                    duplicate_rows += 1
                    continue
                tested += 1
                result, _ = check_seed(O7, A_maps)
                if result is None:
                    continue
                score, D_index, A_index = result
                if best is None or score < best:
                    best = score
                    best_data = (O7, D_index, A_index)
                    print(
                        f"best violations={best}/147; bases={generated}; "
                        f"tested={tested}; D={D_index}; "
                        f"A={''.join(map(str,A_tuples[A_index]))}; "
                        f"elapsed={time.time()-started:.3f}s",
                        flush=True,
                    )
                if score != 0:
                    continue
                D = clique.CANONICAL_D[D_index]
                A = A_tuples[A_index]
                K = clique.reconstruct_K(O7, A, D)
                clique.audit(O7, A, D, K)
                print(
                    f"LATIN T6 CORE WITNESS; D={''.join(map(str,D))}; "
                    f"A={''.join(map(str,A))}; profile={clique.kernel_profile(O7)}; "
                    f"bases={generated}; tested={tested}; "
                    f"elapsed={time.time()-started:.3f}s"
                )
                print(f"O7={clique.render(O7)}")
                print(f"K={clique.render(K)}")
                return 0
    except DeadlineReached:
        pass

    print(
        f"NO LATIN T6 WITNESS IN BOUND; bases={generated}; tested={tested}; "
        f"duplicate-rows={duplicate_rows}; latin-nodes={total_nodes}; "
        f"best-violations={best}; elapsed={time.time()-started:.3f}s"
    )
    if best_data is not None:
        O7, D_index, A_index = best_data
        print(
            f"best D={''.join(map(str,clique.CANONICAL_D[D_index]))}; "
            f"A={''.join(map(str,A_tuples[A_index]))}; O7={clique.render(O7)}"
        )
    return 3


if __name__ == "__main__":
    raise SystemExit(main())
