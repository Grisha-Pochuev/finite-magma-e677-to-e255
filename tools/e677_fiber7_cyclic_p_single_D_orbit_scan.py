"""Exhaust scalar-conjugacy orbits in the single-nonlinear-D isotope class."""

from __future__ import annotations

import argparse
import collections
import itertools
import threading
import time

import e677_fiber7_cyclic_p_isotope_t0267_sat as isotope
import e677_fiber7_cyclic_p_reduced_t0267_sat as routing
import e677_fiber7_cyclic_p_reduced_t6_sat as reduced
import e677_size7_orbit_full_sat as full
from pysat.solvers import Solver  # type: ignore


N = 7


def delta_rank(permutation: tuple[int, ...]) -> int:
    return len({(permutation[x] - x) % N for x in range(N)})


def scalar_conjugates(permutation: tuple[int, ...]):
    result = []
    for scalar in range(1, N):
        inverse = pow(scalar, -1, N)
        result.append(tuple(
            scalar * permutation[(inverse * x) % N] % N for x in range(N)
        ))
    return result


def representatives(ranks: set[int]):
    affine = {
        tuple((alpha * x + gamma) % N for x in range(N))
        for alpha in range(1, N)
        for gamma in range(N)
    }
    reps = set()
    for permutation in itertools.permutations(range(N)):
        if permutation in affine or delta_rank(permutation) not in ranks:
            continue
        reps.add(min(scalar_conjugates(permutation)))
    return sorted(reps, key=lambda item: (delta_rank(item), item))


def audit_model(model, V, D_vars):
    positive = {literal for literal in model if literal > 0}
    D = tuple(
        next(value for value in range(N) if D_vars[inp][value] in positive)
        for inp in range(N)
    )
    C_table = reduced.decode(model, reduced.C)
    for q in range(N):
        for u in range(N):
            if D[C_table[q][u]] != (q + u) % N:
                raise AssertionError("single-D isotope audit failed")
    O7 = reduced.decode(model, reduced.O7Q)
    H_table = reduced.decode(model, reduced.H)
    O0 = routing.decode_v(model, V)
    O2, O4, O6 = reduced.reconstruct(C_table, H_table)
    W = [[O7[s][(t - s) % N] for s in range(N)] for t in range(N)]
    O1 = routing.inverse_rows(W)
    operations = [[row[:] for row in full.BASE] for _ in range(8)]
    for q, table in (
        (0, O0), (1, O1), (2, O2), (4, O4), (6, O6), (7, O7)
    ):
        operations[q] = table
    failures = {
        d: sum(
            not full.holds(operations, d, s, t)
            for s in range(N) for t in range(N)
        )
        for d in (0, 2, 6, 7)
    }
    if any(failures.values()):
        raise AssertionError(f"original identity audit failed: {failures}")
    return D, C_table, H_table, O7, failures


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--ranks", default="7")
    parser.add_argument("--per-orbit-seconds", type=float, default=1.0)
    parser.add_argument("--solver", default="glucose42")
    args = parser.parse_args()
    ranks = {int(value) for value in args.ranks.split(",") if value}
    if not ranks or not ranks <= set(range(1, N + 1)):
        raise SystemExit("--ranks must be a comma-separated subset of 1,...,7")

    clauses, V, A_vars, B_vars, D_vars, variable_count = isotope.build(True)
    for variables in (A_vars, B_vars):
        for value in range(N):
            clauses.append([variables[value][value]])
    reps = representatives(ranks)
    print(
        f"encoding: variables={variable_count}; clauses={len(clauses)}; "
        f"ranks={sorted(ranks)}; scalar-orbits={len(reps)}; solver={args.solver}",
        flush=True,
    )
    counts = collections.Counter()
    unknown = []
    started = time.time()
    with Solver(name=args.solver, bootstrap_with=clauses) as solver:
        for index, permutation in enumerate(reps, 1):
            assumptions = [
                D_vars[inp][value] for inp, value in enumerate(permutation)
            ]
            timer = threading.Timer(
                max(0.05, args.per_orbit_seconds), solver.interrupt
            )
            timer.daemon = True
            timer.start()
            try:
                status = solver.solve_limited(
                    assumptions=assumptions, expect_interrupt=True
                )
            finally:
                timer.cancel()
            if status is True:
                counts["SAT"] += 1
                model = solver.get_model()
                D, C_table, H_table, O7, failures = audit_model(
                    model, V, D_vars
                )
                print(
                    f"SAT T0267 CORE; orbit={index}/{len(reps)}; "
                    f"rank={delta_rank(D)}; D={''.join(map(str, D))}; "
                    f"failures={failures}; elapsed={time.time()-started:.3f}s"
                )
                for name, table in (("C", C_table), ("H", H_table), ("O7", O7)):
                    print(f"{name}={routing.render(table)}")
                return 0
            if status is False:
                counts["UNSAT"] += 1
            else:
                counts["UNKNOWN"] += 1
                unknown.append(permutation)
                solver.clear_interrupt()
            if index % 50 == 0 or index == len(reps):
                print(
                    f"progress={index}/{len(reps)}; counts={dict(counts)}; "
                    f"elapsed={time.time()-started:.3f}s",
                    flush=True,
                )
    print(
        f"ORBIT SCAN COMPLETE; counts={dict(counts)}; "
        f"elapsed={time.time()-started:.3f}s"
    )
    for permutation in unknown[:20]:
        print(
            f"UNKNOWN rank={delta_rank(permutation)}; "
            f"D={''.join(map(str, permutation))}"
        )
    if len(unknown) > 20:
        print(f"omitted-UNKNOWN={len(unknown)-20}")
    return 2 if not unknown else 3


if __name__ == "__main__":
    raise SystemExit(main())
