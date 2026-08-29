"""Search the exact tuple-6 kernel core as a 7-partite row clique.

For two row indices t,t' and two permutations U=O7_t,V=O7_t',
tuple 6 is equivalent, for every s, to

  U^-1(s)=V^-1(s)
    iff
  D(U(s)-t)-A(U(s)) = D(V(s)-t')-A(V(s)).

The cyclic Q-fibre condition is also pairwise: the shifted rows must differ
in every column.  Thus a seven-row T6 core is exactly a clique in these
pair-compatibility relations.  The search is constructive and bounded; a
timeout is not an exclusion.
"""

from __future__ import annotations

import argparse
import itertools
import random
import time

import numpy as np


N = 7
CANONICAL_D = tuple(
    tuple(map(int, text))
    for text in ("0125634", "0145236", "1023546", "1024356")
)


def render(table):
    return "/".join("".join(map(str, row)) for row in table)


def inverse(permutation):
    result = [0] * N
    for inp, value in enumerate(permutation):
        result[value] = inp
    return tuple(result)


def kernel_profile(O7):
    inverses = tuple(inverse(row) for row in O7)
    result = []
    for s in range(N):
        counts = {}
        for t in range(N):
            value = inverses[t][s]
            counts[value] = counts.get(value, 0) + 1
        result.append(tuple(sorted(counts.values(), reverse=True)))
    return tuple(result)


def reconstruct_K(O7, A, D):
    inverses = tuple(inverse(row) for row in O7)
    K = []
    for s in range(N):
        partial = {}
        for t in range(N):
            z = inverses[t][s]
            rho = (D[(O7[t][s] - t) % N] - A[O7[t][s]]) % N
            previous = partial.setdefault(z, rho)
            if previous != rho:
                raise AssertionError((s, t, z, previous, rho))
        if len(set(partial.values())) != len(partial):
            raise AssertionError((s, partial))
        unused_inputs = [x for x in range(N) if x not in partial]
        unused_outputs = [x for x in range(N) if x not in partial.values()]
        row = dict(partial)
        row.update(zip(unused_inputs, unused_outputs))
        K.append(tuple(row[x] for x in range(N)))
    return tuple(K)


def audit(O7, A, D, K):
    if any(sorted(row) != list(range(N)) for row in O7):
        raise AssertionError("O7 row is not a permutation")
    if any(row[0] == 0 for row in O7):
        raise AssertionError("Badness failed")
    if len(set(O7)) != N:
        raise AssertionError("O7 rows are not distinct")
    for column in range(N):
        values = [O7[t][(column - t) % N] for t in range(N)]
        if sorted(values) != list(range(N)):
            raise AssertionError(("Q-fibre", column, values))
    inverses = tuple(inverse(row) for row in O7)
    for s in range(N):
        for t in range(N):
            z = inverses[t][s]
            rho = (D[(O7[t][s] - t) % N] - A[O7[t][s]]) % N
            if K[s][z] != rho:
                raise AssertionError(("T6", s, t, z, rho, K[s][z]))


class CliqueSearch:
    def __init__(self, D, A, deadline, rng):
        raw = [p for p in itertools.permutations(range(N)) if p[0] != 0]
        self.perms = np.asarray(raw, dtype=np.int8)
        self.count = len(raw)
        self.inverses = np.empty_like(self.perms)
        inputs = np.arange(N, dtype=np.int8)
        for index in range(self.count):
            self.inverses[index, self.perms[index]] = inputs
        self.columns = []
        for t in range(N):
            self.columns.append(self.perms[:, (inputs - t) % N])
        D_array = np.asarray(D, dtype=np.int8)
        A_array = np.asarray(A, dtype=np.int8)
        self.rho = []
        for t in range(N):
            x = (self.perms - t) % N
            self.rho.append((D_array[x] - A_array[self.perms]) % N)
        self.deadline = deadline
        self.rng = rng
        self.nodes = 0
        self.compatibility_calls = 0
        self.max_depth = 0
        self.roots_attempted = 0

    def compatible(self, left_t, left_index, right_t, candidates):
        self.compatibility_calls += 1
        rows = self.perms[candidates]
        distinct = np.any(rows != self.perms[left_index], axis=1)
        latin = np.all(
            self.columns[right_t][candidates]
            != self.columns[left_t][left_index],
            axis=1,
        )
        inverse_equal = (
            self.inverses[candidates] == self.inverses[left_index]
        )
        rho_equal = (
            self.rho[right_t][candidates] == self.rho[left_t][left_index]
        )
        kernel = np.all(inverse_equal == rho_equal, axis=1)
        return candidates[distinct & latin & kernel]

    def visit(self, chosen, available):
        if time.time() >= self.deadline:
            return None
        self.nodes += 1
        self.max_depth = max(self.max_depth, len(chosen))
        if not available:
            return dict(chosen)
        next_t = min(available, key=lambda t: len(available[t]))
        candidates = available[next_t].copy()
        self.rng.shuffle(candidates)
        rest = {t: values for t, values in available.items() if t != next_t}
        for index in candidates:
            if time.time() >= self.deadline:
                return None
            updated = {}
            failed = False
            for target_t, values in rest.items():
                filtered = self.compatible(next_t, int(index), target_t, values)
                if len(filtered) == 0:
                    failed = True
                    break
                updated[target_t] = filtered
            if failed:
                continue
            chosen[next_t] = int(index)
            result = self.visit(chosen, updated)
            if result is not None:
                return result
            del chosen[next_t]
        return None

    def run(self):
        root_order = np.arange(self.count, dtype=np.int32)
        self.rng.shuffle(root_order)
        all_candidates = np.arange(self.count, dtype=np.int32)
        for root in root_order:
            if time.time() >= self.deadline:
                break
            self.roots_attempted += 1
            available = {}
            failed = False
            for t in range(1, N):
                candidates = self.compatible(0, int(root), t, all_candidates)
                if len(candidates) == 0:
                    failed = True
                    break
                available[t] = candidates
            if failed:
                continue
            result = self.visit({0: int(root)}, available)
            if result is not None:
                return tuple(tuple(map(int, self.perms[result[t]])) for t in range(N))
        return None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--seconds", type=float, default=180.0)
    parser.add_argument("--per-case-seconds", type=float, default=8.0)
    parser.add_argument("--seed", type=int, default=677255)
    parser.add_argument("--a", help="one normalized A, for example 0132465")
    parser.add_argument("--d", type=int, choices=range(len(CANONICAL_D)))
    args = parser.parse_args()

    started = time.time()
    global_deadline = started + args.seconds
    rng = random.Random(args.seed)
    A_maps = [(0, *tail) for tail in itertools.permutations(range(1, N))]
    if args.a is not None:
        selected = tuple(map(int, args.a))
        if len(selected) != N or tuple(sorted(selected)) != tuple(range(N)) or selected[0] != 0:
            raise SystemExit("--a must be a permutation of 0..6 fixing 0")
        A_maps = [selected]
    cases = [(D_index, A) for A in A_maps for D_index in range(len(CANONICAL_D))]
    if args.d is not None:
        cases = [(D_index, A) for D_index, A in cases if D_index == args.d]
    print(
        f"pair-clique candidates=4320/layer; cases={len(cases)}; "
        f"seconds={args.seconds}; per-case={args.per_case_seconds}",
        flush=True,
    )
    attempted = 0
    total_nodes = 0
    for D_index, A in cases:
        if time.time() >= global_deadline:
            break
        case_deadline = min(global_deadline, time.time() + args.per_case_seconds)
        search = CliqueSearch(CANONICAL_D[D_index], A, case_deadline, rng)
        O7 = search.run()
        attempted += 1
        total_nodes += search.nodes
        if O7 is None:
            print(
                f"case={attempted}; D={D_index}; A={''.join(map(str,A))}; "
                f"status=NO-WITNESS-IN-BOUND; nodes={search.nodes}; "
                f"max-depth={search.max_depth}/7; roots={search.roots_attempted}/4320; "
                f"compat={search.compatibility_calls}",
                flush=True,
            )
            continue
        D = CANONICAL_D[D_index]
        K = reconstruct_K(O7, A, D)
        audit(O7, A, D, K)
        print(
            f"T6 PAIR-CLIQUE WITNESS; D={''.join(map(str,D))}; "
            f"A={''.join(map(str,A))}; profile={kernel_profile(O7)}; "
            f"attempted={attempted}; nodes={total_nodes}; "
            f"elapsed={time.time()-started:.3f}s"
        )
        print(f"O7={render(O7)}")
        print(f"K={render(K)}")
        return 0
    print(
        f"NO WITNESS IN BOUND; attempted={attempted}/{len(cases)}; "
        f"nodes={total_nodes}; elapsed={time.time()-started:.3f}s"
    )
    return 3


if __name__ == "__main__":
    raise SystemExit(main())
