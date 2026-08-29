"""Exact tuple-6 kernel abstraction for the four canonical D maps.

Eliminate C, B, and H.  Put K_s=B o H_s.  For

    q=O7_t(s), z=O7_t^-1(s)

tuple 6 is exactly

    K_s(z)=D(q-t)-A(q).

The script keeps only permutation A, permutation rows K, Bad/distinct O7
rows, and the cyclic O7 transversals.
"""

from __future__ import annotations

import argparse
import itertools
import threading
import time

from pysat.solvers import Solver  # type: ignore


N = 7
CANONICAL_D = tuple(
    tuple(map(int, text))
    for text in ("0125634", "0145236", "1023546", "1024356")
)


def add_exactly_one(clauses, literals):
    clauses.append(list(literals))
    for left, right in itertools.combinations(literals, 2):
        clauses.append([-left, -right])


def add_permutation(clauses, next_variable):
    variables = []
    for inp in range(N):
        row = list(range(next_variable, next_variable + N))
        next_variable += N
        variables.append(row)
        add_exactly_one(clauses, row)
    for value in range(N):
        add_exactly_one(
            clauses, [variables[inp][value] for inp in range(N)]
        )
    return variables, next_variable


def decode_permutation(model, variables):
    positive = {literal for literal in model if literal > 0}
    return tuple(
        next(value for value in range(N) if variables[inp][value] in positive)
        for inp in range(N)
    )


def build():
    clauses = []
    next_variable = 1
    O7 = []
    for row in range(N):
        variables, next_variable = add_permutation(clauses, next_variable)
        O7.append(variables)

    # Q fibres: for each t, s -> O7_s(t-s) is a permutation.
    for t in range(N):
        for value in range(N):
            add_exactly_one(
                clauses,
                [O7[s][(t - s) % N][value] for s in range(N)],
            )

    # Badness and pairwise distinct O7 rows.
    for row in range(N):
        clauses.append([-O7[row][0][0]])
    for left in range(N):
        for right in range(left + 1, N):
            differences = []
            for inp in range(N):
                difference = next_variable
                next_variable += 1
                differences.append(difference)
                for value in range(N):
                    clauses.append([
                        -difference,
                        -O7[left][inp][value],
                        -O7[right][inp][value],
                    ])
            clauses.append(differences)

    A, next_variable = add_permutation(clauses, next_variable)
    clauses.append([A[0][0]])
    K = []
    for row in range(N):
        variables, next_variable = add_permutation(clauses, next_variable)
        K.append(variables)

    selectors = list(range(next_variable, next_variable + len(CANONICAL_D)))
    next_variable += len(CANONICAL_D)
    add_exactly_one(clauses, selectors)

    # If O7_t(s)=q and O7_t(z)=s, then z=O7_t^-1(s) and tuple 6 forces K.
    for selector, D in zip(selectors, CANONICAL_D):
        for s in range(N):
            for t in range(N):
                for q in range(N):
                    rho = (D[(q - t) % N] - q) % N
                    for z in range(N):
                        for a in range(N):
                            clauses.append([
                                -selector,
                                -O7[t][s][q],
                                -O7[t][z][s],
                                -A[q][a],
                                K[s][z][(rho + q - a) % N],
                            ])
    return clauses, O7, A, K, selectors, next_variable - 1


def kernel_profile(O7):
    inverse_rows = []
    for row in O7:
        inverse = [0] * N
        for inp, value in enumerate(row):
            inverse[value] = inp
        inverse_rows.append(inverse)
    profiles = []
    for s in range(N):
        counts = {}
        for t in range(N):
            z = inverse_rows[t][s]
            counts[z] = counts.get(z, 0) + 1
        profiles.append(tuple(sorted(counts.values(), reverse=True)))
    return tuple(profiles)


def render(table):
    return "/".join("".join(map(str, row)) for row in table)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seconds", type=int, default=180)
    parser.add_argument("--solver", default="glucose42")
    parser.add_argument("--d-index", type=int, choices=range(len(CANONICAL_D)))
    parser.add_argument("--a", help="fix A, for example 0132465")
    args = parser.parse_args()
    clauses, O7_vars, A_vars, K_vars, selectors, variable_count = build()
    if args.d_index is not None:
        clauses.append([selectors[args.d_index]])
    if args.a is not None:
        fixed_A = tuple(map(int, args.a))
        if (
            len(fixed_A) != N
            or tuple(sorted(fixed_A)) != tuple(range(N))
            or fixed_A[0] != 0
        ):
            raise SystemExit("--a must be a permutation of 0..6 fixing 0")
        for inp, value in enumerate(fixed_A):
            clauses.append([A_vars[inp][value]])
    print(
        f"encoding: variables={variable_count}; clauses={len(clauses)}; "
        f"canonical-D={len(selectors)}; solver={args.solver}",
        flush=True,
    )
    started = time.time()
    with Solver(name=args.solver, bootstrap_with=clauses) as solver:
        timer = threading.Timer(max(1, args.seconds), solver.interrupt)
        timer.daemon = True
        timer.start()
        try:
            status = solver.solve_limited(expect_interrupt=True)
        finally:
            timer.cancel()
        stats = solver.accum_stats()
        if status is None:
            print(
                f"status=UNKNOWN; elapsed={time.time()-started:.3f}s; "
                f"stats={stats}"
            )
            return 3
        if status is False:
            print(
                f"status=UNSAT; elapsed={time.time()-started:.3f}s; "
                f"stats={stats}"
            )
            return 2
        model = solver.get_model()

    positive = {literal for literal in model if literal > 0}
    D_index = next(index for index, literal in enumerate(selectors) if literal in positive)
    D = CANONICAL_D[D_index]
    O7 = tuple(decode_permutation(model, row) for row in O7_vars)
    A = decode_permutation(model, A_vars)
    K = tuple(decode_permutation(model, row) for row in K_vars)

    # Direct cell audit of the forced-kernel equation.
    inverse_O7 = []
    for row in O7:
        inverse = [0] * N
        for inp, value in enumerate(row):
            inverse[value] = inp
        inverse_O7.append(inverse)
    for s in range(N):
        for t in range(N):
            q = O7[t][s]
            z = inverse_O7[t][s]
            required = (D[(q - t) % N] - A[q]) % N
            if K[s][z] != required:
                raise AssertionError((s, t, q, z, required, K[s][z]))

    print(
        f"SAT T6-KERNEL CORE; D={''.join(map(str,D))}; "
        f"A={''.join(map(str,A))}; profile={kernel_profile(O7)}; "
        f"elapsed={time.time()-started:.3f}s; stats={stats}"
    )
    print(f"O7={render(O7)}")
    print(f"K={render(K)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
