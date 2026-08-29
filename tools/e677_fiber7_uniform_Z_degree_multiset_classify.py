"""Exact degree-multiset classifier for the uniform Latin Z side.

Z_s(t)=O_t^-1(s) is encoded without A,D,rho.  Every column is a
permutation, every shifted row t->t+Z_s(t) is a permutation, Z_0 is nonzero,
the seven O rows are distinct, and every Z_s fibre partition has profile
(2,2,1,1,1).  Models are blocked by the entire multiset of the seven vertex
degrees in the resulting fourteen-edge colored matching system.
"""

from __future__ import annotations

import argparse
import itertools
import threading
import time

from pysat.solvers import Solver  # type: ignore


N = 7


def add_exactly_one(clauses, literals):
    clauses.append(list(literals))
    for left, right in itertools.combinations(literals, 2):
        clauses.append([-left, -right])


def conditional_exact(clauses, literals, selector, bound):
    for subset in itertools.combinations(literals, bound + 1):
        clauses.append([-selector, *(-literal for literal in subset)])
    for subset in itertools.combinations(literals, len(literals) - bound + 1):
        clauses.append([-selector, *subset])


def build():
    clauses = []
    next_variable = 1
    Z = []
    for _s in range(N):
        target = []
        for _t in range(N):
            values = list(range(next_variable, next_variable + N))
            next_variable += N
            add_exactly_one(clauses, values)
            target.append(values)
        Z.append(target)

    # For fixed row index t, s -> Z_s(t)=O_t^-1(s) is a permutation.
    for t in range(N):
        for value in range(N):
            add_exactly_one(clauses, [Z[s][t][value] for s in range(N)])

    # For fixed target s, t -> t+Z_s(t) is a permutation (Latin columns).
    for s in range(N):
        for shifted_value in range(N):
            add_exactly_one(
                clauses,
                [Z[s][t][(shifted_value - t) % N] for t in range(N)],
            )

    # Badness at the distinguished target.
    for t in range(N):
        clauses.append([-Z[0][t][0]])

    # The inverse permutation columns, hence the O rows, must be distinct.
    for left in range(N):
        for right in range(left + 1, N):
            differences = []
            for s in range(N):
                difference = next_variable
                next_variable += 1
                differences.append(difference)
                for value in range(N):
                    clauses.append(
                        [-difference, -Z[s][left][value], -Z[s][right][value]]
                    )
            clauses.append(differences)

    equality = [[[] for _t in range(N)] for _s in range(N)]
    target_edges = []
    for s in range(N):
        edges = []
        for left in range(N):
            for right in range(left + 1, N):
                edge = next_variable
                next_variable += 1
                edges.append(edge)
                equality[s][left].append(edge)
                equality[s][right].append(edge)
                for left_value in range(N):
                    for right_value in range(N):
                        clauses.append(
                            [
                                -Z[s][left][left_value],
                                -Z[s][right][right_value],
                                edge if left_value == right_value else -edge,
                            ]
                        )
        # Exactly two equality edges means profile (2,2,1,1,1), since
        # equality is transitive and a block of size three already has 3 edges.
        conditional_exact(clauses, edges, next_variable, 2)
        profile_selector = next_variable
        next_variable += 1
        clauses.append([profile_selector])
        target_edges.append(edges)

    incidence = [[0] * N for _ in range(N)]
    for t in range(N):
        for s in range(N):
            literal = next_variable
            next_variable += 1
            incidence[t][s] = literal
            for edge in equality[s][t]:
                clauses.append([-edge, literal])
            clauses.append([-literal, *equality[s][t]])

    degree_selectors = []
    for t in range(N):
        selectors = list(range(next_variable, next_variable + N + 1))
        next_variable += N + 1
        add_exactly_one(clauses, selectors)
        for degree, selector in enumerate(selectors):
            conditional_exact(clauses, incidence[t], selector, degree)
        degree_selectors.append(selectors)

    return clauses, Z, target_edges, degree_selectors, next_variable - 1


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--seconds", type=float, default=120.0)
    parser.add_argument("--solver", default="glucose42")
    args = parser.parse_args()

    clauses, Z, target_edges, degree_selectors, variable_count = build()
    print(
        f"uniform-Z graph encoding: variables={variable_count}; clauses={len(clauses)}; "
        f"candidate-degree-multisets=155; seconds={args.seconds}",
        flush=True,
    )
    started = time.time()
    deadline = started + args.seconds
    degree_multisets = []
    with Solver(name=args.solver, bootstrap_with=clauses) as solver:
        while time.time() < deadline:
            timer = threading.Timer(max(0.05, deadline - time.time()), solver.interrupt)
            timer.daemon = True
            timer.start()
            try:
                status = solver.solve_limited(expect_interrupt=True)
            finally:
                timer.cancel()
            if status is None:
                print(
                    f"status=UNKNOWN; found={len(degree_multisets)}; "
                    f"elapsed={time.time()-started:.3f}s"
                )
                return 3
            if status is False:
                print(
                    f"UNIFORM-Z DEGREE CLASSIFICATION COMPLETE; "
                    f"multisets={len(degree_multisets)}; "
                    f"elapsed={time.time()-started:.3f}s"
                )
                print(f"degree-multisets={sorted(degree_multisets)}")
                return 0
            model = solver.get_model()
            positive = {literal for literal in model if literal > 0}
            degrees = tuple(
                next(
                    degree
                    for degree, selector in enumerate(degree_selectors[t])
                    if selector in positive
                )
                for t in range(N)
            )
            multiset = tuple(sorted(degrees))
            if multiset in degree_multisets:
                raise AssertionError(multiset)
            degree_multisets.append(multiset)
            for permutation in set(itertools.permutations(multiset)):
                solver.add_clause(
                    [
                        -degree_selectors[t][permutation[t]]
                        for t in range(N)
                    ]
                )
            if len(degree_multisets) <= 10 or len(degree_multisets) % 10 == 0:
                print(
                    f"found={len(degree_multisets)}; latest={multiset}; "
                    f"elapsed={time.time()-started:.3f}s",
                    flush=True,
                )
    return 3


if __name__ == "__main__":
    raise SystemExit(main())
