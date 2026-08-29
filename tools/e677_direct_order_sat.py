"""Compact direct SAT search for an E677 magma violating E255 at zero."""

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


def exactly_one(clauses: list[list[int]], literals: list[int]) -> None:
    clauses.append(literals)
    for a, b in itertools.combinations(literals, 2):
        clauses.append([-a, -b])


def integer_partitions(total: int, maximum: int | None = None):
    if total == 0:
        yield []
        return
    if maximum is None or maximum > total:
        maximum = total
    for first in range(maximum, 0, -1):
        for tail in integer_partitions(total - first, first):
            yield [first, *tail]


def permutation_from_cycles(order: int, cycles: list[list[int]]) -> list[int]:
    permutation = list(range(order))
    seen: set[int] = set()
    for cycle in cycles:
        if not cycle:
            continue
        for index, value in enumerate(cycle):
            if value in seen:
                raise RuntimeError(f"duplicate cycle value {value}")
            seen.add(value)
            permutation[value] = cycle[(index + 1) % len(cycle)]
    if seen != set(range(order)):
        raise RuntimeError(f"cycles do not cover the permutation: missing={set(range(order)) - seen}")
    return permutation


def ordinary_cycles(labels: list[int], partition: list[int]) -> list[list[int]]:
    cycles = []
    offset = 0
    for length in partition:
        cycles.append(labels[offset:offset + length])
        offset += length
    if offset != len(labels):
        raise RuntimeError("partition does not cover labels")
    return cycles


def normalized_row0_orbits(order: int) -> list[tuple[int, list[int]]]:
    if order != 11:
        raise RuntimeError("row-zero orbit generator is specialized to order 11")
    orbits: list[tuple[int, list[int]]] = []

    # f(2)=1 or 2: only 0,1,2 are distinguished.  The 0-cycle has length
    # m and the complement is determined by an ordinary integer partition.
    for f2 in (1, 2):
        for length in range(4, order + 1):
            distinguished = [0, 1, *range(3, length - 1), 2, length - 1]
            remaining = list(range(length, order))
            for partition in integer_partitions(len(remaining)):
                cycles = [distinguished, *ordinary_cycles(remaining, partition)]
                orbits.append((f2, permutation_from_cycles(order, cycles)))

    # f(2)=3 and label 3 lies in the distinguished 0-cycle.  Its exact
    # position is invariant under the residual relabelling.
    for length in range(4, order + 1):
        positions = [*range(2, length - 2), length - 1]
        for position3 in positions:
            distinguished: list[int | None] = [None] * length
            distinguished[0], distinguished[1] = 0, 1
            distinguished[length - 2], distinguished[position3] = 2, 3
            free_labels = iter(range(4, length))
            for index in range(length):
                if distinguished[index] is None:
                    distinguished[index] = next(free_labels)
            remaining = list(range(length, order))
            for partition in integer_partitions(len(remaining)):
                cycles = [
                    [int(value) for value in distinguished],
                    *ordinary_cycles(remaining, partition),
                ]
                orbits.append((3, permutation_from_cycles(order, cycles)))

    # f(2)=3 and label 3 is outside the distinguished cycle.  Its own cycle
    # is determined by its length; all other complement cycles form a
    # partition.
    for length in range(4, order):
        distinguished = [0, 1, *range(4, length), 2, length]
        complement_free = list(range(length + 1, order))
        complement_size = order - length
        for cycle3_length in range(1, complement_size + 1):
            cycle3 = [3, *complement_free[:cycle3_length - 1]]
            rest = complement_free[cycle3_length - 1:]
            for partition in integer_partitions(len(rest)):
                cycles = [distinguished, cycle3, *ordinary_cycles(rest, partition)]
                orbits.append((3, permutation_from_cycles(order, cycles)))

    return orbits


def load_cached(order: int) -> list[list[int]] | None:
    path = ROOT / "cache" / "eq677-db" / str(order) / "0"
    if not path.exists():
        return None
    rows = [[int(x) for x in line.split()] for line in path.read_text().splitlines() if line.strip()]
    if len(rows) != order or any(len(row) != order for row in rows):
        raise RuntimeError(f"bad cached table at {path}")
    return rows


def verify(table: list[list[int]], require_bad: bool) -> list[int]:
    n = len(table)
    for row in table:
        if sorted(row) != list(range(n)):
            raise RuntimeError("decoded left row is not a permutation")
    for x in range(n):
        for y in range(n):
            value = table[y][table[x][table[table[y][x]][y]]]
            if value != x:
                raise RuntimeError(f"E677 failure at x={x}, y={y}: {value}")
    bad = [x for x in range(n) if table[table[table[x][x]][x]][x] != x]
    if require_bad and 0 not in bad:
        raise RuntimeError(f"zero is not Bad; bad={bad}")
    return bad


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--order", type=int, default=11)
    parser.add_argument("--seconds", type=int, default=180)
    parser.add_argument("--solver", default="glucose42")
    parser.add_argument("--allow-good", action="store_true")
    parser.add_argument("--no-phases", action="store_true")
    parser.add_argument("--second-column-value", type=int, choices=(1, 2))
    parser.add_argument("--third-column-value", type=int, choices=(1, 2, 3))
    parser.add_argument("--scan-normalized-cubes", action="store_true")
    parser.add_argument("--scan-f3-cubes", action="store_true")
    parser.add_argument("--scan-row0-input2-cubes", action="store_true")
    parser.add_argument("--scan-row0-input3-cubes", action="store_true")
    parser.add_argument("--scan-f4-cubes", action="store_true")
    parser.add_argument("--scan-row0-cycle-cubes", action="store_true")
    parser.add_argument("--scan-row0-cycle-g2-cubes", action="store_true")
    parser.add_argument("--scan-row0-permutation-orbits", action="store_true")
    parser.add_argument("--redundant-y0", action="store_true")
    parser.add_argument("--redundant-x0", action="store_true")
    parser.add_argument("--quiet-unknown", action="store_true")
    parser.add_argument("--per-cube-seconds", type=int, default=10)
    args = parser.parse_args()
    n = args.order
    if n < 2:
        raise SystemExit("order must be at least 2")
    scan_count = sum(
        (
            args.scan_normalized_cubes,
            args.scan_f3_cubes,
            args.scan_row0_input2_cubes,
            args.scan_row0_input3_cubes,
            args.scan_f4_cubes,
            args.scan_row0_cycle_cubes,
            args.scan_row0_cycle_g2_cubes,
            args.scan_row0_permutation_orbits,
        )
    )
    if scan_count > 1:
        raise SystemExit("choose only one cube scan")
    if scan_count:
        if args.allow_good or n != 11:
            raise SystemExit("cube scans require Bad order 11")
        if args.second_column_value not in (None, 2) or args.third_column_value is not None:
            raise SystemExit("cube scan sets the second and third column normalization itself")
        args.second_column_value = 2
    if args.third_column_value is not None and args.second_column_value != 2:
        raise SystemExit("--third-column-value requires --second-column-value 2")

    def cell(row: int, inp: int, value: int) -> int:
        return 1 + ((row * n + inp) * n + value)

    clauses: list[list[int]] = []
    for row in range(n):
        for inp in range(n):
            exactly_one(clauses, [cell(row, inp, value) for value in range(n)])
        for value in range(n):
            exactly_one(clauses, [cell(row, inp, value) for inp in range(n)])

    if not args.allow_good:
        # In an E677 magma, zero is Bad iff no left row fixes input zero.
        for row in range(n):
            clauses.append([-cell(row, 0, 0)])
        # Valid isomorphism breaking under relabellings fixing zero.
        clauses.append([cell(0, 0, 1)])
        if args.second_column_value is None:
            clauses.append([cell(1, 0, 1), cell(1, 0, 2)])
        else:
            clauses.append([cell(1, 0, args.second_column_value)])
        if args.second_column_value == 2:
            if args.third_column_value is None:
                clauses.append([cell(2, 0, 1), cell(2, 0, 2), cell(2, 0, 3)])
            else:
                clauses.append([cell(2, 0, args.third_column_value)])

    next_variable = n ** 3 + 1
    auxiliary_ranges: list[tuple[list[int], list[int], int, int]] = []
    for x in range(n):
        for y in range(n):
            v_aux = list(range(next_variable, next_variable + n))
            next_variable += n
            w_aux = list(range(next_variable, next_variable + n))
            next_variable += n
            auxiliary_ranges.append((v_aux, w_aux, x, y))
            exactly_one(clauses, v_aux)
            exactly_one(clauses, w_aux)
            # u=y*x, v=u*y, w=x*v, and y*w=x.
            for u in range(n):
                for v in range(n):
                    clauses.append([-cell(y, x, u), -cell(u, y, v), v_aux[v]])
            for v in range(n):
                for w in range(n):
                    clauses.append([-v_aux[v], -cell(x, v, w), w_aux[w]])
            for w in range(n):
                clauses.append([-w_aux[w], cell(y, w, x)])

    if args.redundant_y0:
        # Let s(x)=0*x and f(z)=z*0.  E677 at y=0 says
        # s(x*f(s(x)))=x.  Since s is a permutation, if s(p)=x,
        # s(x)=z and f(z)=a, then the direct cell x*a=p is forced.
        # These clauses are redundant but expose the full row/column
        # coupling immediately once a normalized row-zero orbit is fixed.
        for p in range(n):
            for x in range(n):
                for z in range(n):
                    for a in range(n):
                        clauses.append([
                            -cell(0, p, x),
                            -cell(0, x, z),
                            -cell(z, 0, a),
                            cell(x, a, p),
                        ])
        if not args.allow_good:
            # If s(p)=z, then p=s^-1(z).  The forced y=0 cell in row z is
            # z*f(s(z))=p.  Badness gives f(s(z))!=0, while z*0=f(z), so row
            # injectivity forbids f(z)=p.  Expose this collision directly.
            for p in range(n):
                for z in range(n):
                    clauses.append([-cell(0, p, z), -cell(z, 0, p)])

    if args.redundant_x0:
        # Put s(t)=0*t, f(y)=y*0, and let g(y) be the unique input with
        # y*g(y)=0.  E677 at x=0 gives
        #
        #   f(y)*y = s^-1(g(y)).
        #
        # Thus if f(y)=a, g(y)=b, and s(p)=b, then a*y=p.
        for y in range(n):
            for a in range(n):
                for b in range(n):
                    for p in range(n):
                        clauses.append([
                            -cell(y, 0, a),
                            -cell(y, b, 0),
                            -cell(0, p, b),
                            cell(a, y, p),
                        ])
        if not args.allow_good:
            # For y!=0, row a=f(y) has distinct inputs 0 and y.  Its values
            # f(a) and s^-1(g(y)) must therefore differ.
            for y in range(1, n):
                for a in range(n):
                    for b in range(n):
                        for p in range(n):
                            clauses.append([
                                -cell(y, 0, a),
                                -cell(a, 0, p),
                                -cell(y, b, 0),
                                -cell(0, p, b),
                            ])

    variable_count = next_variable - 1
    started = time.time()
    print(
        f"encoding: order={n}; variables={variable_count}; clauses={len(clauses)}; "
        f"solver={args.solver}; bad-zero={not args.allow_good}; "
        f"second-column={args.second_column_value if args.second_column_value else '1-or-2'}; "
        f"third-column={args.third_column_value if args.third_column_value else '1-or-2-or-3' if args.second_column_value == 2 else 'off'}",
        f"redundant-y0={args.redundant_y0}; redundant-x0={args.redundant_x0}",
        flush=True,
    )

    with Solver(name=args.solver, bootstrap_with=clauses, use_timer=True) as solver:
        if not args.no_phases:
            if args.allow_good:
                phase_table = load_cached(n)
            else:
                shifts = [1] * n
                if args.second_column_value == 2:
                    shifts[1] = 2
                if args.third_column_value is not None:
                    shifts[2] = args.third_column_value
                phase_table = [[(inp + shifts[row]) % n for inp in range(n)] for row in range(n)]
            if phase_table is not None:
                phases = []
                for row in range(n):
                    for inp in range(n):
                        chosen = phase_table[row][inp]
                        for value in range(n):
                            literal = cell(row, inp, value)
                            phases.append(literal if value == chosen else -literal)
                for v_aux, w_aux, x, y in auxiliary_ranges:
                    u = phase_table[y][x]
                    v = phase_table[u][y]
                    w = phase_table[x][v]
                    for value in range(n):
                        phases.append(v_aux[value] if value == v else -v_aux[value])
                        phases.append(w_aux[value] if value == w else -w_aux[value])
                solver.set_phases(phases)

        if args.scan_normalized_cubes:
            # If f(2)=1 or 2, the residual S_8 action on labels 3,...,10
            # normalizes T(0,1) to 0, 2, or 3.  If f(2)=3, label 3 is also
            # fixed and the residual S_7 action gives 0, 2, 3, or 4.
            cubes = [
                (1, 2), (1, 0), (1, 3),
                (2, 2), (2, 0), (2, 3),
                (3, 2), (3, 0), (3, 3), (3, 4),
            ]
            unknown = []
            unsat = 0
            for index, (f2, row0_input1) in enumerate(cubes):
                assumptions = [cell(2, 0, f2), cell(0, 1, row0_input1)]
                before = solver.accum_stats().copy()
                case_started = time.time()
                timer = threading.Timer(max(1, args.per_cube_seconds), solver.interrupt)
                timer.daemon = True
                timer.start()
                try:
                    result = solver.solve_limited(assumptions=assumptions, expect_interrupt=True)
                finally:
                    timer.cancel()
                after = solver.accum_stats().copy()
                delta_conflicts = after.get("conflicts", 0) - before.get("conflicts", 0)
                print(
                    f"cube {index+1}/{len(cubes)} f2={f2},T(0,1)={row0_input1}: "
                    f"{'SAT' if result is True else 'UNSAT' if result is False else 'UNKNOWN'}; "
                    f"elapsed={time.time()-case_started:.3f}s; conflicts={delta_conflicts}",
                    flush=True,
                )
                if result is True:
                    model = {literal for literal in solver.get_model() if literal > 0}
                    table = []
                    for row in range(n):
                        decoded = []
                        for inp in range(n):
                            values = [value for value in range(n) if cell(row, inp, value) in model]
                            if len(values) != 1:
                                raise RuntimeError(f"bad decoded cell ({row},{inp}): {values}")
                            decoded.append(values[0])
                        table.append(decoded)
                    bad = verify(table, True)
                    print(f"status: VERIFIED COUNTEREXAMPLE; bad={bad}")
                    for row in table:
                        print(" ".join(map(str, row)))
                    return 0
                if result is False:
                    unsat += 1
                else:
                    unknown.append((f2, row0_input1))
                    solver.clear_interrupt()
            print(
                f"status: {'UNSAT' if not unknown else 'NORMALIZED CUBE SCAN INCOMPLETE'}; "
                f"unsat={unsat}; unknown={len(unknown)}; total={len(cubes)}; "
                f"elapsed={time.time()-started:.3f}s"
            )
            if unknown:
                print("unknown-cubes=" + ",".join(f"{a}:{b}" for a, b in unknown))
                return 3
            return 2

        if args.scan_f3_cubes:
            # These are exactly the five unresolved parent cubes from the
            # exhaustive f(2),T(0,1) scan.  In the first four, labels 0..3
            # are fixed by the parent data, so f(3) is one of 1,2,3 or a new
            # label represented by 4.  In the last parent label 4 is fixed as
            # well, hence f(3) is one of 1,2,3,4 or a new label represented by
            # 5.  The value zero is excluded by Bad(0).
            parents = [(1, 3), (2, 3), (3, 2), (3, 3), (3, 4)]
            cubes = [
                (f2, row0_input1, f3)
                for f2, row0_input1 in parents
                for f3 in range(1, 6 if (f2, row0_input1) == (3, 4) else 5)
            ]
            unknown = []
            unsat = 0
            for index, (f2, row0_input1, f3) in enumerate(cubes):
                assumptions = [
                    cell(2, 0, f2),
                    cell(0, 1, row0_input1),
                    cell(3, 0, f3),
                ]
                before = solver.accum_stats().copy()
                case_started = time.time()
                timer = threading.Timer(max(1, args.per_cube_seconds), solver.interrupt)
                timer.daemon = True
                timer.start()
                try:
                    result = solver.solve_limited(assumptions=assumptions, expect_interrupt=True)
                finally:
                    timer.cancel()
                after = solver.accum_stats().copy()
                delta_conflicts = after.get("conflicts", 0) - before.get("conflicts", 0)
                print(
                    f"cube {index+1}/{len(cubes)} f2={f2},T(0,1)={row0_input1},f3={f3}: "
                    f"{'SAT' if result is True else 'UNSAT' if result is False else 'UNKNOWN'}; "
                    f"elapsed={time.time()-case_started:.3f}s; conflicts={delta_conflicts}",
                    flush=True,
                )
                if result is True:
                    model = {literal for literal in solver.get_model() if literal > 0}
                    table = []
                    for row in range(n):
                        decoded = []
                        for inp in range(n):
                            values = [value for value in range(n) if cell(row, inp, value) in model]
                            if len(values) != 1:
                                raise RuntimeError(f"bad decoded cell ({row},{inp}): {values}")
                            decoded.append(values[0])
                        table.append(decoded)
                    bad = verify(table, True)
                    print(f"status: VERIFIED COUNTEREXAMPLE; bad={bad}")
                    for row in table:
                        print(" ".join(map(str, row)))
                    return 0
                if result is False:
                    unsat += 1
                else:
                    unknown.append((f2, row0_input1, f3))
                    solver.clear_interrupt()
            print(
                f"status: {'UNSAT' if not unknown else 'F3 CUBE SCAN INCOMPLETE'}; "
                f"unsat={unsat}; unknown={len(unknown)}; total={len(cubes)}; "
                f"elapsed={time.time()-started:.3f}s"
            )
            if unknown:
                print("unknown-cubes=" + ",".join(f"{a}:{b}:{c}" for a, b, c in unknown))
                return 3
            return 2

        if args.scan_row0_input2_cubes:
            # Refine exactly the thirteen unresolved f(3) cubes.  The listed
            # values are the orbits of T(0,2) under each residual relabelling
            # group.  Values already used by T(0,0)=1 and T(0,1) are omitted
            # because row zero is a permutation; the last value in each list
            # represents every still-unfixed label.
            parents = [
                (1, 3, 4, [0, 2, 4, 5]),
                (2, 3, 3, [0, 2, 4]),
                (2, 3, 4, [0, 2, 4, 5]),
                (3, 2, 2, [0, 3, 4]),
                (3, 2, 3, [0, 3, 4]),
                (3, 2, 4, [0, 3, 4, 5]),
                (3, 3, 3, [0, 2, 4]),
                (3, 3, 4, [0, 2, 4, 5]),
                (3, 4, 1, [0, 2, 3, 5]),
                (3, 4, 2, [0, 2, 3, 5]),
                (3, 4, 3, [0, 2, 3, 5]),
                (3, 4, 4, [0, 2, 3, 5]),
                (3, 4, 5, [0, 2, 3, 5, 6]),
            ]
            cubes = [
                (f2, row0_input1, f3, row0_input2)
                for f2, row0_input1, f3, values in parents
                for row0_input2 in values
            ]
            unknown = []
            unsat = 0
            for index, (f2, row0_input1, f3, row0_input2) in enumerate(cubes):
                assumptions = [
                    cell(2, 0, f2),
                    cell(0, 1, row0_input1),
                    cell(3, 0, f3),
                    cell(0, 2, row0_input2),
                ]
                before = solver.accum_stats().copy()
                case_started = time.time()
                timer = threading.Timer(max(1, args.per_cube_seconds), solver.interrupt)
                timer.daemon = True
                timer.start()
                try:
                    result = solver.solve_limited(assumptions=assumptions, expect_interrupt=True)
                finally:
                    timer.cancel()
                after = solver.accum_stats().copy()
                delta_conflicts = after.get("conflicts", 0) - before.get("conflicts", 0)
                print(
                    f"cube {index+1}/{len(cubes)} f2={f2},T(0,1)={row0_input1},"
                    f"f3={f3},T(0,2)={row0_input2}: "
                    f"{'SAT' if result is True else 'UNSAT' if result is False else 'UNKNOWN'}; "
                    f"elapsed={time.time()-case_started:.3f}s; conflicts={delta_conflicts}",
                    flush=True,
                )
                if result is True:
                    model = {literal for literal in solver.get_model() if literal > 0}
                    table = []
                    for row in range(n):
                        decoded = []
                        for inp in range(n):
                            values = [value for value in range(n) if cell(row, inp, value) in model]
                            if len(values) != 1:
                                raise RuntimeError(f"bad decoded cell ({row},{inp}): {values}")
                            decoded.append(values[0])
                        table.append(decoded)
                    bad = verify(table, True)
                    print(f"status: VERIFIED COUNTEREXAMPLE; bad={bad}")
                    for row in table:
                        print(" ".join(map(str, row)))
                    return 0
                if result is False:
                    unsat += 1
                else:
                    unknown.append((f2, row0_input1, f3, row0_input2))
                    solver.clear_interrupt()
            print(
                f"status: {'UNSAT' if not unknown else 'ROW0 INPUT2 CUBE SCAN INCOMPLETE'}; "
                f"unsat={unsat}; unknown={len(unknown)}; total={len(cubes)}; "
                f"elapsed={time.time()-started:.3f}s"
            )
            if unknown:
                print("unknown-cubes=" + ",".join(f"{a}:{b}:{c}:{d}" for a, b, c, d in unknown))
                return 3
            return 2

        if args.scan_row0_input3_cubes:
            # Refine exactly the twenty-one unresolved T(0,2) cubes.  Every
            # parent fixes labels 0,1,2,3.  Its other displayed values are
            # fixed too.  Thus T(0,3) is either an as-yet unused fixed label
            # or one representative of all still-free labels.
            parents = [
                (1, 3, 4, 4), (1, 3, 4, 5),
                (2, 3, 3, 4), (2, 3, 4, 5),
                (3, 2, 2, 4), (3, 2, 3, 4),
                (3, 2, 4, 3), (3, 2, 4, 4), (3, 2, 4, 5),
                (3, 3, 3, 4), (3, 3, 4, 4), (3, 3, 4, 5),
                (3, 4, 1, 5), (3, 4, 2, 5),
                (3, 4, 3, 3), (3, 4, 3, 5),
                (3, 4, 4, 3), (3, 4, 4, 5),
                (3, 4, 5, 3), (3, 4, 5, 5), (3, 4, 5, 6),
            ]
            cubes = []
            for f2, row0_input1, f3, row0_input2 in parents:
                fixed = {0, 1, 2, 3, f2, row0_input1, f3, row0_input2}
                used_in_row0 = {1, row0_input1, row0_input2}
                values = sorted(fixed - used_in_row0)
                new_value = next(value for value in range(n) if value not in fixed)
                values.append(new_value)
                cubes.extend(
                    (f2, row0_input1, f3, row0_input2, row0_input3)
                    for row0_input3 in values
                )
            unknown = []
            unsat = 0
            for index, (f2, row0_input1, f3, row0_input2, row0_input3) in enumerate(cubes):
                assumptions = [
                    cell(2, 0, f2),
                    cell(0, 1, row0_input1),
                    cell(3, 0, f3),
                    cell(0, 2, row0_input2),
                    cell(0, 3, row0_input3),
                ]
                before = solver.accum_stats().copy()
                case_started = time.time()
                timer = threading.Timer(max(1, args.per_cube_seconds), solver.interrupt)
                timer.daemon = True
                timer.start()
                try:
                    result = solver.solve_limited(assumptions=assumptions, expect_interrupt=True)
                finally:
                    timer.cancel()
                after = solver.accum_stats().copy()
                delta_conflicts = after.get("conflicts", 0) - before.get("conflicts", 0)
                print(
                    f"cube {index+1}/{len(cubes)} f2={f2},T(0,1)={row0_input1},"
                    f"f3={f3},T(0,2)={row0_input2},T(0,3)={row0_input3}: "
                    f"{'SAT' if result is True else 'UNSAT' if result is False else 'UNKNOWN'}; "
                    f"elapsed={time.time()-case_started:.3f}s; conflicts={delta_conflicts}",
                    flush=True,
                )
                if result is True:
                    model = {literal for literal in solver.get_model() if literal > 0}
                    table = []
                    for row in range(n):
                        decoded = []
                        for inp in range(n):
                            values = [value for value in range(n) if cell(row, inp, value) in model]
                            if len(values) != 1:
                                raise RuntimeError(f"bad decoded cell ({row},{inp}): {values}")
                            decoded.append(values[0])
                        table.append(decoded)
                    bad = verify(table, True)
                    print(f"status: VERIFIED COUNTEREXAMPLE; bad={bad}")
                    for row in table:
                        print(" ".join(map(str, row)))
                    return 0
                if result is False:
                    unsat += 1
                else:
                    unknown.append((f2, row0_input1, f3, row0_input2, row0_input3))
                    solver.clear_interrupt()
            print(
                f"status: {'UNSAT' if not unknown else 'ROW0 INPUT3 CUBE SCAN INCOMPLETE'}; "
                f"unsat={unsat}; unknown={len(unknown)}; total={len(cubes)}; "
                f"elapsed={time.time()-started:.3f}s"
            )
            if unknown:
                print("unknown-cubes=" + ",".join(
                    f"{a}:{b}:{c}:{d}:{e}" for a, b, c, d, e in unknown
                ))
                return 3
            return 2

        if args.scan_f4_cubes:
            # Change axis after the row-zero refinements.  These are exactly
            # the thirty-one unresolved T(0,3) cubes.  They all fix label 4,
            # so f(4)=T(4,0) is one nonzero fixed label or one representative
            # of all remaining labels.
            parents = [
                (1, 3, 4, 4, 2), (1, 3, 4, 4, 5),
                (1, 3, 4, 5, 2), (1, 3, 4, 5, 6),
                (2, 3, 3, 4, 5),
                (2, 3, 4, 5, 2), (2, 3, 4, 5, 4), (2, 3, 4, 5, 6),
                (3, 2, 2, 4, 5), (3, 2, 3, 4, 5),
                (3, 2, 4, 3, 0), (3, 2, 4, 4, 5),
                (3, 2, 4, 5, 4), (3, 2, 4, 5, 6),
                (3, 3, 3, 4, 5), (3, 3, 4, 4, 5), (3, 3, 4, 5, 6),
                (3, 4, 1, 5, 3), (3, 4, 1, 5, 6),
                (3, 4, 2, 5, 6),
                (3, 4, 3, 3, 0), (3, 4, 3, 5, 6),
                (3, 4, 4, 3, 0), (3, 4, 4, 5, 3), (3, 4, 4, 5, 6),
                (3, 4, 5, 3, 0), (3, 4, 5, 5, 3), (3, 4, 5, 5, 6),
                (3, 4, 5, 6, 3), (3, 4, 5, 6, 5), (3, 4, 5, 6, 7),
            ]
            cubes = []
            for f2, row0_input1, f3, row0_input2, row0_input3 in parents:
                fixed = {
                    0, 1, 2, 3, 4, f2, row0_input1, f3,
                    row0_input2, row0_input3,
                }
                values = sorted(fixed - {0})
                new_value = next(value for value in range(n) if value not in fixed)
                values.append(new_value)
                cubes.extend(
                    (f2, row0_input1, f3, row0_input2, row0_input3, f4)
                    for f4 in values
                )
            print(f"f4-cubes={len(cubes)}", flush=True)
            unknown = []
            unsat = 0
            for index, (f2, row0_input1, f3, row0_input2, row0_input3, f4) in enumerate(cubes):
                assumptions = [
                    cell(2, 0, f2),
                    cell(0, 1, row0_input1),
                    cell(3, 0, f3),
                    cell(0, 2, row0_input2),
                    cell(0, 3, row0_input3),
                    cell(4, 0, f4),
                ]
                before = solver.accum_stats().copy()
                case_started = time.time()
                timer = threading.Timer(max(1, args.per_cube_seconds), solver.interrupt)
                timer.daemon = True
                timer.start()
                try:
                    result = solver.solve_limited(assumptions=assumptions, expect_interrupt=True)
                finally:
                    timer.cancel()
                after = solver.accum_stats().copy()
                delta_conflicts = after.get("conflicts", 0) - before.get("conflicts", 0)
                print(
                    f"cube {index+1}/{len(cubes)} f2={f2},T(0,1)={row0_input1},"
                    f"f3={f3},T(0,2)={row0_input2},T(0,3)={row0_input3},f4={f4}: "
                    f"{'SAT' if result is True else 'UNSAT' if result is False else 'UNKNOWN'}; "
                    f"elapsed={time.time()-case_started:.3f}s; conflicts={delta_conflicts}",
                    flush=True,
                )
                if result is True:
                    model = {literal for literal in solver.get_model() if literal > 0}
                    table = []
                    for row in range(n):
                        decoded = []
                        for inp in range(n):
                            values = [value for value in range(n) if cell(row, inp, value) in model]
                            if len(values) != 1:
                                raise RuntimeError(f"bad decoded cell ({row},{inp}): {values}")
                            decoded.append(values[0])
                        table.append(decoded)
                    bad = verify(table, True)
                    print(f"status: VERIFIED COUNTEREXAMPLE; bad={bad}")
                    for row in table:
                        print(" ".join(map(str, row)))
                    return 0
                if result is False:
                    unsat += 1
                else:
                    unknown.append((f2, row0_input1, f3, row0_input2, row0_input3, f4))
                    solver.clear_interrupt()
            print(
                f"status: {'UNSAT' if not unknown else 'F4 CUBE SCAN INCOMPLETE'}; "
                f"unsat={unsat}; unknown={len(unknown)}; total={len(cubes)}; "
                f"elapsed={time.time()-started:.3f}s"
            )
            if unknown:
                print("unknown-cubes=" + ",".join(
                    f"{a}:{b}:{c}:{d}:{e}:{f}" for a, b, c, d, e, f in unknown
                ))
                return 3
            return 2

        if args.scan_row0_cycle_cubes or args.scan_row0_cycle_g2_cubes:
            # Put s(t)=T(0,t).  E677 at x=y=0 gives s^2(2)=0 under
            # T(0,0)=1,T(1,0)=2.  Thus if g=s(1), h=s(2), then h is
            # distinct from 0,1,2, g is distinct from 0,1,h, and s(h)=0.
            # The g=2 parents for f(2)=1,2 were already proved UNSAT.  For
            # f(2)=3 they leave the two extra orbits scanned separately here.
            cubes = (
                [(3, 2, 3), (3, 2, 4)]
                if args.scan_row0_cycle_g2_cubes
                else [
                    (1, 3, 4),
                    (2, 3, 4),
                    (3, 3, 4),
                    (3, 4, 3),
                    (3, 4, 5),
                ]
            )
            unknown = []
            unsat = 0
            for index, (f2, g, h) in enumerate(cubes):
                assumptions = [
                    cell(2, 0, f2),
                    cell(0, 1, g),
                    cell(0, 2, h),
                    cell(0, h, 0),
                ]
                before = solver.accum_stats().copy()
                case_started = time.time()
                timer = threading.Timer(max(1, args.per_cube_seconds), solver.interrupt)
                timer.daemon = True
                timer.start()
                try:
                    result = solver.solve_limited(assumptions=assumptions, expect_interrupt=True)
                finally:
                    timer.cancel()
                after = solver.accum_stats().copy()
                delta_conflicts = after.get("conflicts", 0) - before.get("conflicts", 0)
                print(
                    f"cube {index+1}/{len(cubes)} f2={f2},s(1)={g},s(2)={h},s({h})=0: "
                    f"{'SAT' if result is True else 'UNSAT' if result is False else 'UNKNOWN'}; "
                    f"elapsed={time.time()-case_started:.3f}s; conflicts={delta_conflicts}",
                    flush=True,
                )
                if result is True:
                    model = {literal for literal in solver.get_model() if literal > 0}
                    table = []
                    for row in range(n):
                        decoded = []
                        for inp in range(n):
                            values = [value for value in range(n) if cell(row, inp, value) in model]
                            if len(values) != 1:
                                raise RuntimeError(f"bad decoded cell ({row},{inp}): {values}")
                            decoded.append(values[0])
                        table.append(decoded)
                    bad = verify(table, True)
                    print(f"status: VERIFIED COUNTEREXAMPLE; bad={bad}")
                    for row in table:
                        print(" ".join(map(str, row)))
                    return 0
                if result is False:
                    unsat += 1
                else:
                    unknown.append((f2, g, h))
                    solver.clear_interrupt()
            print(
                f"status: {'UNSAT' if not unknown else 'ROW0 CYCLE CUBE SCAN INCOMPLETE'}; "
                f"unsat={unsat}; unknown={len(unknown)}; total={len(cubes)}; "
                f"elapsed={time.time()-started:.3f}s"
            )
            if unknown:
                print("unknown-cubes=" + ",".join(f"{a}:{b}:{c}" for a, b, c in unknown))
                return 3
            return 2

        if args.scan_row0_permutation_orbits:
            cubes = normalized_row0_orbits(n)
            if len(cubes) != 285:
                raise RuntimeError(f"expected 285 row-zero orbits, got {len(cubes)}")
            unknown = []
            unsat = 0
            for index, (f2, row0) in enumerate(cubes):
                assumptions = [cell(2, 0, f2)]
                assumptions.extend(cell(0, inp, value) for inp, value in enumerate(row0))
                before = solver.accum_stats().copy()
                case_started = time.time()
                timer = threading.Timer(max(1, args.per_cube_seconds), solver.interrupt)
                timer.daemon = True
                timer.start()
                try:
                    result = solver.solve_limited(assumptions=assumptions, expect_interrupt=True)
                finally:
                    timer.cancel()
                after = solver.accum_stats().copy()
                delta_conflicts = after.get("conflicts", 0) - before.get("conflicts", 0)
                label = f"f2={f2},row0={'-'.join(map(str, row0))}"
                if result is True:
                    print(
                        f"orbit {index+1}/{len(cubes)} {label}: SAT; "
                        f"elapsed={time.time()-case_started:.3f}s; conflicts={delta_conflicts}",
                        flush=True,
                    )
                    model = {literal for literal in solver.get_model() if literal > 0}
                    table = []
                    for row in range(n):
                        decoded = []
                        for inp in range(n):
                            values = [value for value in range(n) if cell(row, inp, value) in model]
                            if len(values) != 1:
                                raise RuntimeError(f"bad decoded cell ({row},{inp}): {values}")
                            decoded.append(values[0])
                        table.append(decoded)
                    bad = verify(table, True)
                    print(f"status: VERIFIED COUNTEREXAMPLE; bad={bad}")
                    for row in table:
                        print(" ".join(map(str, row)))
                    return 0
                if result is False:
                    unsat += 1
                    if (index + 1) % 25 == 0:
                        print(
                            f"progress {index+1}/{len(cubes)}; unsat={unsat}; "
                            f"unknown={len(unknown)}",
                            flush=True,
                        )
                else:
                    unknown.append((f2, row0))
                    solver.clear_interrupt()
                    if not args.quiet_unknown:
                        print(
                            f"orbit {index+1}/{len(cubes)} {label}: UNKNOWN; "
                            f"elapsed={time.time()-case_started:.3f}s; "
                            f"conflicts={delta_conflicts}",
                            flush=True,
                        )
                    elif (index + 1) % 25 == 0:
                        print(
                            f"progress {index+1}/{len(cubes)}; unsat={unsat}; "
                            f"unknown={len(unknown)}",
                            flush=True,
                        )
            print(
                f"status: {'UNSAT' if not unknown else 'ROW0 ORBIT SCAN INCOMPLETE'}; "
                f"unsat={unsat}; unknown={len(unknown)}; total={len(cubes)}; "
                f"elapsed={time.time()-started:.3f}s"
            )
            if unknown:
                if not args.quiet_unknown:
                    print("unknown-orbits=" + ",".join(
                        f"{f2}:{'-'.join(map(str, row0))}" for f2, row0 in unknown
                    ))
                return 3
            return 2

        timer = threading.Timer(max(1, args.seconds), solver.interrupt)
        timer.daemon = True
        timer.start()
        try:
            result = solver.solve_limited(expect_interrupt=True)
        finally:
            timer.cancel()
        elapsed = time.time() - started
        stats = solver.accum_stats()
        if result is None:
            print(f"status: UNKNOWN (time bound); elapsed={elapsed:.3f}s; stats={stats}")
            return 3
        if result is False:
            print(f"status: UNSAT; elapsed={elapsed:.3f}s; stats={stats}")
            return 2
        model = {literal for literal in solver.get_model() if literal > 0}

    table = []
    for row in range(n):
        decoded = []
        for inp in range(n):
            values = [value for value in range(n) if cell(row, inp, value) in model]
            if len(values) != 1:
                raise RuntimeError(f"bad decoded cell ({row},{inp}): {values}")
            decoded.append(values[0])
        table.append(decoded)
    bad = verify(table, not args.allow_good)
    print(f"status: {'VERIFIED COUNTEREXAMPLE' if not args.allow_good else 'VERIFIED E677 MODEL'}; bad={bad}")
    for row in table:
        print(" ".join(map(str, row)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
