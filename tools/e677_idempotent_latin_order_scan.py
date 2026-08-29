"""Exact small-order scan for idempotent Latin E677 magmas.

This is the auxiliary structure forced on the Bad set by terminal ZERO-root
equality.  The scan is exhaustive up to the cycle type of row zero: in an
idempotent Latin magma row zero fixes zero, and relabelling the other points
conjugates its remaining cycles to the canonical representative used here.
"""

from __future__ import annotations

import argparse
import itertools
import sys
import threading
import time
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools" / "vendor" / "python_sat311"))
sys.path.insert(0, str(ROOT / "tools" / "vendor" / "python_sat"))
from pysat.solvers import Solver  # type: ignore


K5_ROWS = (
    (0, 2, 1, 4, 3),
    (3, 1, 4, 0, 2),
    (4, 3, 2, 1, 0),
    (2, 4, 0, 3, 1),
    (1, 0, 3, 2, 4),
)


def exactly_one(clauses: list[list[int]], literals: list[int]) -> None:
    clauses.append(literals)
    for left, right in itertools.combinations(literals, 2):
        clauses.append([-left, -right])


def partitions(total: int, maximum: int | None = None):
    if total == 0:
        yield ()
        return
    if maximum is None or maximum > total:
        maximum = total
    for first in range(maximum, 0, -1):
        for tail in partitions(total - first, first):
            yield (first, *tail)


def canonical_row_zero(order: int, partition: tuple[int, ...]) -> list[int]:
    result = list(range(order))
    start = 1
    for length in partition:
        cycle = list(range(start, start + length))
        for index, point in enumerate(cycle):
            result[point] = cycle[(index + 1) % length]
        start += length
    if start != order:
        raise RuntimeError("row-zero partition does not cover the labels")
    return result


def verify(table: list[list[int]]) -> None:
    order = len(table)
    expected = list(range(order))
    for row in table:
        if sorted(row) != expected:
            raise RuntimeError("decoded row is not a permutation")
    for inp in range(order):
        if sorted(table[row][inp] for row in range(order)) != expected:
            raise RuntimeError(f"decoded column {inp} is not a permutation")
    for point in range(order):
        if table[point][point] != point:
            raise RuntimeError(f"decoded diagonal is not idempotent at {point}")
    for x in range(order):
        for y in range(order):
            value = table[y][table[x][table[table[y][x]][y]]]
            if value != x:
                raise RuntimeError(f"E677 failure at x={x}, y={y}: {value}")


def scan_order(
    order: int,
    solver_name: str,
    per_cube_seconds: int,
    exclude_k5_orbit: bool,
) -> tuple[str, int, int]:
    def cell(row: int, inp: int, value: int) -> int:
        return 1 + ((row * order + inp) * order + value)

    clauses: list[list[int]] = []

    # Latin property: each left row and each right column is a permutation.
    for row in range(order):
        for inp in range(order):
            exactly_one(clauses, [cell(row, inp, value) for value in range(order)])
        for value in range(order):
            exactly_one(clauses, [cell(row, inp, value) for inp in range(order)])
    for inp in range(order):
        for value in range(order):
            exactly_one(clauses, [cell(row, inp, value) for row in range(order)])

    for point in range(order):
        clauses.append([cell(point, point, point)])

    if exclude_k5_orbit:
        if order != 5:
            raise RuntimeError("--exclude-k5-orbit requires order 5")
        orbit: set[tuple[int, ...]] = set()
        for permutation in itertools.permutations(range(order)):
            relabelled = [[0] * order for _ in range(order)]
            for row in range(order):
                for inp in range(order):
                    relabelled[permutation[row]][permutation[inp]] = permutation[K5_ROWS[row][inp]]
            orbit.add(tuple(value for row in relabelled for value in row))
        for table in orbit:
            clauses.append([
                -cell(row, inp, table[row * order + inp])
                for row in range(order)
                for inp in range(order)
            ])
        print(f"excluded-K5-labelled-orbit={len(orbit)}", flush=True)

    next_variable = order**3 + 1
    for x in range(order):
        for y in range(order):
            v_aux = list(range(next_variable, next_variable + order))
            next_variable += order
            w_aux = list(range(next_variable, next_variable + order))
            next_variable += order
            exactly_one(clauses, v_aux)
            exactly_one(clauses, w_aux)

            # u=y*x, v=u*y, w=x*v, y*w=x.
            for u in range(order):
                for v in range(order):
                    clauses.append([-cell(y, x, u), -cell(u, y, v), v_aux[v]])
            for v in range(order):
                for w in range(order):
                    clauses.append([-v_aux[v], -cell(x, v, w), w_aux[w]])
            for w in range(order):
                clauses.append([-w_aux[w], cell(y, w, x)])

    cube_partitions = list(partitions(order - 1))
    unsat = 0
    unknown = 0
    with Solver(name=solver_name, bootstrap_with=clauses, use_timer=True) as solver:
        for index, partition in enumerate(cube_partitions, 1):
            row_zero = canonical_row_zero(order, partition)
            assumptions = [cell(0, inp, value) for inp, value in enumerate(row_zero)]
            timer = threading.Timer(max(1, per_cube_seconds), solver.interrupt)
            timer.daemon = True
            timer.start()
            started = time.time()
            try:
                result = solver.solve_limited(assumptions=assumptions, expect_interrupt=True)
            finally:
                timer.cancel()
            elapsed = time.time() - started
            status = "SAT" if result is True else "UNSAT" if result is False else "UNKNOWN"
            print(
                f"order={order} cube={index}/{len(cube_partitions)} "
                f"row0-cycles={partition}: {status} ({elapsed:.3f}s)",
                flush=True,
            )
            if result is True:
                model = {literal for literal in solver.get_model() if literal > 0}
                table = [
                    [
                        next(value for value in range(order) if cell(row, inp, value) in model)
                        for inp in range(order)
                    ]
                    for row in range(order)
                ]
                verify(table)
                print(f"order={order} VERIFIED MODEL", flush=True)
                for row in table:
                    print(" ".join(map(str, row)), flush=True)
                return "SAT", unsat, unknown
            if result is False:
                unsat += 1
            else:
                unknown += 1
                solver.clear_interrupt()

    return ("UNSAT" if unknown == 0 else "UNKNOWN"), unsat, unknown


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--min-order", type=int, default=2)
    parser.add_argument("--max-order", type=int, default=8)
    parser.add_argument("--solver", default="cadical195")
    parser.add_argument("--per-cube-seconds", type=int, default=20)
    parser.add_argument("--exclude-k5-orbit", action="store_true")
    args = parser.parse_args()
    if args.min_order < 2 or args.max_order < args.min_order:
        raise SystemExit("require 2 <= min-order <= max-order")
    if args.exclude_k5_orbit and (args.min_order != 5 or args.max_order != 5):
        raise SystemExit("--exclude-k5-orbit requires --min-order 5 --max-order 5")

    started = time.time()
    results = []
    for order in range(args.min_order, args.max_order + 1):
        status, unsat, unknown = scan_order(
            order,
            args.solver,
            args.per_cube_seconds,
            args.exclude_k5_orbit,
        )
        results.append((order, status, unsat, unknown))
    print("summary:", flush=True)
    for order, status, unsat, unknown in results:
        print(f"  order={order}: {status}; unsat-cubes={unsat}; unknown-cubes={unknown}")
    print(f"elapsed={time.time()-started:.3f}s", flush=True)
    return 3 if any(status == "UNKNOWN" for _, status, _, _ in results) else 0


if __name__ == "__main__":
    raise SystemExit(main())
