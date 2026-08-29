"""Targeted completion tests for K5 periodic and ZERO-reuse shells.

Besides block-tree completion, the two equivariant modes test the exact
four-layer SHORT skeleton and its pure three-layer ZIPPER quotient.  Every
SAT table is independently checked against all E677 pairs and its Bad set.
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


def blocks(count: int, shape: str) -> list[tuple[int, ...]]:
    if shape == "star":
        return [tuple([0, *range(4 * index + 1, 4 * index + 5)]) for index in range(count)]
    result = [tuple(range(5))]
    for index in range(1, count):
        shared = result[-1][-1]
        result.append(tuple([shared, *range(4 * index + 1, 4 * index + 5)]))
    return result


def k5_order_five_automorphism() -> tuple[int, ...]:
    """Return a canonical fixed-point-free order-five automorphism of K5."""
    for permutation in itertools.permutations(range(5)):
        if any(permutation[point] == point for point in range(5)):
            continue
        if all(
            K5_ROWS[permutation[row]][permutation[inp]]
            == permutation[K5_ROWS[row][inp]]
            for row in range(5)
            for inp in range(5)
        ):
            return permutation
    raise RuntimeError("the K5 core has no fixed-point-free automorphism")


def verify(table: list[list[int]], require_all_bad: bool) -> list[int]:
    n = len(table)
    for row in table:
        if sorted(row) != list(range(n)):
            raise RuntimeError("decoded row is not a permutation")
    for x in range(n):
        for y in range(n):
            value = table[y][table[x][table[table[y][x]][y]]]
            if value != x:
                raise RuntimeError(f"E677 failure at ({x},{y}): {value}")
    bad = [x for x in range(n) if table[table[table[x][x]][x]][x] != x]
    if require_all_bad and len(bad) != n:
        raise RuntimeError(f"not all points are Bad: {bad}")
    return bad


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--blocks", type=int, default=2)
    parser.add_argument("--shape", choices=("star", "chain"), default="chain")
    parser.add_argument("--extra", type=int, default=0)
    parser.add_argument("--seconds", type=int, default=180)
    parser.add_argument("--allow-good", action="store_true")
    parser.add_argument("--pair-core", action="store_true")
    parser.add_argument("--minimize-pair-core", action="store_true")
    parser.add_argument("--core-witnesses", action="store_true")
    parser.add_argument("--row8-profile", action="store_true")
    parser.add_argument("--terminal-k5", action="store_true")
    parser.add_argument("--equivariant-four-layer", action="store_true")
    parser.add_argument("--equivariant-three-layer-zipper", action="store_true")
    parser.add_argument("--skip-e677", action="store_true")
    parser.add_argument("--solver", default="glucose42")
    args = parser.parse_args()
    if args.blocks < 1:
        raise SystemExit("--blocks must be positive")
    if args.extra < 0:
        raise SystemExit("--extra must be nonnegative")
    if args.minimize_pair_core:
        args.pair_core = True
    if args.core_witnesses:
        args.minimize_pair_core = True
        args.pair_core = True
    if args.row8_profile:
        args.pair_core = True
    if args.skip_e677:
        args.pair_core = True

    block_list = blocks(args.blocks, args.shape)
    n = 1 + 4 * args.blocks + args.extra
    if args.terminal_k5 and (args.blocks != 1 or args.extra < 5):
        raise SystemExit("--terminal-k5 requires --blocks 1 and --extra at least 5")
    if args.equivariant_four_layer and (
        not args.terminal_k5 or args.blocks != 1 or args.extra != 15
    ):
        raise SystemExit(
            "--equivariant-four-layer requires --terminal-k5 --blocks 1 --extra 15"
        )
    if args.equivariant_three_layer_zipper and (
        not args.terminal_k5 or args.blocks != 1 or args.extra != 10
    ):
        raise SystemExit(
            "--equivariant-three-layer-zipper requires "
            "--terminal-k5 --blocks 1 --extra 10"
        )
    if args.equivariant_four_layer and args.equivariant_three_layer_zipper:
        raise SystemExit("choose only one equivariant shell")

    def cell(row: int, inp: int, value: int) -> int:
        return 1 + ((row * n + inp) * n + value)

    clauses: list[list[int]] = []
    for row in range(n):
        for inp in range(n):
            exactly_one(clauses, [cell(row, inp, value) for value in range(n)])
        for value in range(n):
            exactly_one(clauses, [cell(row, inp, value) for inp in range(n)])

    fixed_literals: list[int] = []
    fixed_cells: list[tuple[int, int, int]] = []

    def fix(row: int, inp: int, value: int) -> None:
        literal = cell(row, inp, value)
        fixed_literals.append(literal)
        fixed_cells.append((row, inp, value))
        clauses.append([literal])

    for block in block_list:
        for local_row, row in enumerate(block):
            for local_input, inp in enumerate(block):
                if local_input == local_row:
                    continue
                value = block[K5_ROWS[local_row][local_input]]
                fix(row, inp, value)

    equivariant_shift: tuple[int, ...] | None = None
    equivariant_orbit: tuple[int, ...] | None = None
    if args.equivariant_four_layer:
        bad_shift = k5_order_five_automorphism()
        orbit = [0]
        for _ in range(4):
            orbit.append(bad_shift[orbit[-1]])
        if len(set(orbit)) != 5 or bad_shift[orbit[-1]] != orbit[0]:
            raise RuntimeError(f"bad K5 order-five orbit: {orbit}")
        equivariant_orbit = tuple(orbit)

        shift = list(bad_shift)
        for base in (5, 10, 15):
            shift.extend(base + ((index + 1) % 5) for index in range(5))
        equivariant_shift = tuple(shift)

        # The exact 20-point shadow/SHORT skeleton.  The five Bad points are
        # indexed along an automorphism orbit; the three Good layers are the
        # square, sigma, and kappa bands.  A completion would be a genuine
        # E677 counterexample with a Bad D-cycle.
        for index, x in enumerate(equivariant_orbit):
            successor = equivariant_orbit[(index + 1) % 5]
            square = 5 + index
            sigma = 10 + index
            kappa = 15 + index
            fix(x, x, square)
            fix(square, x, sigma)
            fix(x, sigma, kappa)
            fix(x, kappa, x)
            fix(sigma, x, successor)
            fix(kappa, square, sigma)
        for good in range(5, 20):
            fix(good, good, good)

    elif args.equivariant_three_layer_zipper:
        bad_shift = k5_order_five_automorphism()
        orbit = [0]
        for _ in range(4):
            orbit.append(bad_shift[orbit[-1]])
        if len(set(orbit)) != 5 or bad_shift[orbit[-1]] != orbit[0]:
            raise RuntimeError(f"bad K5 order-five orbit: {orbit}")
        equivariant_orbit = tuple(orbit)

        shift = list(bad_shift)
        for base in (5, 10):
            shift.extend(base + ((index + 1) % 5) for index in range(5))
        equivariant_shift = tuple(shift)

        h_index: list[int] = []
        for index, x in enumerate(equivariant_orbit):
            d_value = equivariant_orbit[(index + 1) % 5]
            candidates = [
                candidate_index
                for candidate_index, candidate in enumerate(equivariant_orbit)
                if K5_ROWS[d_value][candidate] == x
            ]
            if len(candidates) != 1:
                raise RuntimeError(f"bad K5 H-value at orbit index {index}: {candidates}")
            h_index.append(candidates[0])
        if sorted(h_index) != list(range(5)):
            raise RuntimeError(f"K5 H is not a permutation: {h_index}")
        h_inverse = [h_index.index(index) for index in range(5)]

        # Pure zipper closure of the canonical mixed collision:
        # sigma(q)=kappa(H(q)) and sigma(q)*D(q)=H(q).
        for index, x in enumerate(equivariant_orbit):
            successor = equivariant_orbit[(index + 1) % 5]
            h_value = equivariant_orbit[h_index[index]]
            square = 5 + index
            sigma = 10 + index
            kappa = 10 + h_inverse[index]
            if sigma == kappa:
                raise RuntimeError("zipper unexpectedly identifies sigma(x) with kappa(x)")
            fix(x, x, square)
            fix(square, x, sigma)
            fix(x, sigma, kappa)
            fix(x, kappa, x)
            fix(sigma, x, successor)
            fix(kappa, square, sigma)
            fix(sigma, successor, h_value)
    if equivariant_shift is not None:
        # Simultaneous shift is required to be an automorphism of the whole
        # multiplication table.  One implication around the order-five orbit
        # already gives equivalence, but both directions keep the encoding
        # auditable in isolation.
        for row in range(n):
            for inp in range(n):
                for value in range(n):
                    source = cell(row, inp, value)
                    image = cell(
                        equivariant_shift[row],
                        equivariant_shift[inp],
                        equivariant_shift[value],
                    )
                    clauses.append([-source, image])
                    clauses.append([-image, source])

    if args.terminal_k5:
        bad_labels = set(block_list[0])
        good_labels = set(range(n)) - bad_labels
        for point in bad_labels:
            for row in range(n):
                clauses.append([-cell(row, point, point)])
        for point in good_labels:
            clauses.append([cell(row, point, point) for row in range(n)])

        # Exact no-HIT residue: D(x)=((x*x)*x)*x remains in the K5 layer.
        for point in bad_labels:
            for square in range(n):
                for sigma in range(n):
                    for good in good_labels:
                        clauses.append(
                            [
                                -cell(point, point, square),
                                -cell(square, point, sigma),
                                -cell(sigma, point, good),
                            ]
                        )
    elif not args.allow_good:
        for point in range(n):
            for row in range(n):
                clauses.append([-cell(row, point, point)])

    next_variable = n ** 3 + 1
    pair_selectors: list[int] = []
    selector_labels: dict[int, tuple[int, int]] = {}
    for x in range(n):
        for y in range(n):
            selector = next_variable if args.pair_core else None
            if selector is not None:
                next_variable += 1
                pair_selectors.append(selector)
                selector_labels[selector] = (x, y)
            gate = [-selector] if selector is not None else []
            middle = list(range(next_variable, next_variable + n))
            next_variable += n
            outer = list(range(next_variable, next_variable + n))
            next_variable += n
            exactly_one(clauses, middle)
            exactly_one(clauses, outer)
            for first in range(n):
                for second in range(n):
                    clauses.append(
                        [*gate, -cell(y, x, first), -cell(first, y, second), middle[second]]
                    )
            for second in range(n):
                for third in range(n):
                    clauses.append([*gate, -middle[second], -cell(x, second, third), outer[third]])
            for third in range(n):
                clauses.append([*gate, -outer[third], cell(y, third, x)])

    print(
        f"encoding: blocks={args.blocks}; shape={args.shape}; order={n}; "
        f"fixed={len(fixed_literals)}; "
        f"all-bad={not args.allow_good and not args.terminal_k5}; "
        f"terminal-k5={args.terminal_k5}; variables={next_variable - 1}; "
        f"equivariant-four-layer={args.equivariant_four_layer}; "
        f"equivariant-three-layer-zipper={args.equivariant_three_layer_zipper}; "
        f"clauses={len(clauses)}",
        flush=True,
    )
    started = time.time()
    with Solver(name=args.solver, bootstrap_with=clauses, use_timer=True) as solver:
        timer = threading.Timer(max(1, args.seconds), solver.interrupt)
        timer.daemon = True
        timer.start()
        try:
            result = solver.solve_limited(
                assumptions=[] if args.skip_e677 else pair_selectors,
                expect_interrupt=True,
            )
        finally:
            timer.cancel()
        elapsed = time.time() - started
        if result is None:
            print(f"status: UNKNOWN; elapsed={elapsed:.3f}s")
            return 3
        if result is False:
            if args.pair_core:
                core = list(solver.get_core() or pair_selectors)
                unknown_trials = 0
                if args.minimize_pair_core:
                    for literal in list(core):
                        trial = [item for item in core if item != literal]
                        solver.clear_interrupt()
                        trial_timer = threading.Timer(2, solver.interrupt)
                        trial_timer.daemon = True
                        trial_timer.start()
                        try:
                            trial_result = solver.solve_limited(
                                assumptions=trial,
                                expect_interrupt=True,
                            )
                        finally:
                            trial_timer.cancel()
                        if trial_result is False:
                            core = trial
                        elif trial_result is None:
                            unknown_trials += 1
                labels = sorted(selector_labels[literal] for literal in core)
                print(
                    f"pair-core={len(labels)}; unknown-trials={unknown_trials}: "
                    + " ".join(f"({x},{y})" for x, y in labels)
                )
                if args.core_witnesses:
                    for omitted in core:
                        assumptions = [item for item in core if item != omitted]
                        if solver.solve(assumptions=assumptions) is not True:
                            raise RuntimeError("minimal pair-core deletion has no witness")
                        model = {literal for literal in solver.get_model() if literal > 0}
                        table = []
                        for row in range(n):
                            decoded = []
                            for inp in range(n):
                                values = [
                                    value
                                    for value in range(n)
                                    if cell(row, inp, value) in model
                                ]
                                if len(values) != 1:
                                    raise RuntimeError(
                                        f"bad witness cell ({row},{inp}): {values}"
                                    )
                                decoded.append(values[0])
                            table.append(decoded)
                        omitted_pair = selector_labels[omitted]
                        traces = []
                        for literal in core:
                            x, y = selector_labels[literal]
                            first = table[y][x]
                            second = table[first][y]
                            third = table[x][second]
                            result_value = table[y][third]
                            traces.append(
                                f"({x},{y}):{first},{second},{third}->{result_value}"
                            )
                        print(
                            f"omit={omitted_pair}; row1={''.join(map(str, table[1]))}; "
                            f"row8={''.join(map(str, table[8]))}; "
                            + " ".join(traces)
                        )
                if args.row8_profile:
                    if n != 13 or args.blocks != 3 or args.shape != "chain":
                        raise RuntimeError("--row8-profile requires the order-13 chain")
                    by_pair = {label: literal for literal, label in selector_labels.items()}
                    stages = (
                        ("four-y8", [(0, 8), (1, 8), (2, 8), (3, 8)]),
                        ("plus-self1", [(0, 8), (1, 8), (2, 8), (3, 8), (1, 1)]),
                        (
                            "plus-cross81",
                            [(0, 8), (1, 8), (2, 8), (3, 8), (1, 1), (8, 1)],
                        ),
                    )
                    carrier = (0, 1, 2, 3, 8)
                    for stage_name, pairs in stages:
                        survivors = []
                        stage_assumptions = [by_pair[pair] for pair in pairs]
                        for image in itertools.permutations(carrier):
                            row_assumptions = [
                                cell(8, inp, value)
                                for inp, value in zip(carrier, image)
                            ]
                            if solver.solve(assumptions=[*stage_assumptions, *row_assumptions]):
                                survivors.append(image)
                        print(
                            f"row8-stage={stage_name}; survivors={len(survivors)}; "
                            + " ".join("".join(map(str, image)) for image in survivors)
                        )
            print(f"status: UNSAT; elapsed={elapsed:.3f}s")
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

        # Audit the encoded shell independently of the SAT clauses.  This is
        # especially important for --skip-e677: that mode is a consistency
        # control for the same fixed shell, not a magma verification.
        for row in table:
            if sorted(row) != list(range(n)):
                raise RuntimeError("decoded row is not a permutation")
        for row, inp, value in fixed_cells:
            if table[row][inp] != value:
                raise RuntimeError(
                    f"fixed-cell failure at ({row},{inp}): "
                    f"expected {value}, got {table[row][inp]}"
                )
        if args.terminal_k5:
            shell_bad = set(block_list[0])
            shell_good = set(range(n)) - shell_bad
            for point in shell_bad:
                fixers = [row for row in range(n) if table[row][point] == point]
                if fixers:
                    raise RuntimeError(
                        f"terminal shell has a forbidden fixer at {point}: {fixers}"
                    )
                d_value = table[table[table[point][point]][point]][point]
                if d_value not in shell_bad:
                    raise RuntimeError(f"terminal shell HIT at {point}: D={d_value}")
            for point in shell_good:
                fixers = [row for row in range(n) if table[row][point] == point]
                if not fixers:
                    raise RuntimeError(f"terminal shell has no designated fixer at {point}")
        if args.equivariant_four_layer or args.equivariant_three_layer_zipper:
            assert equivariant_shift is not None
            assert equivariant_orbit is not None
            for row in range(n):
                for inp in range(n):
                    shifted_value = table[equivariant_shift[row]][equivariant_shift[inp]]
                    if shifted_value != equivariant_shift[table[row][inp]]:
                        raise RuntimeError(f"equivariance failure at ({row},{inp})")
            d_cycle = [
                table[table[table[point][point]][point]][point]
                for point in equivariant_orbit
            ]
            if d_cycle != [
                equivariant_orbit[(index + 1) % 5] for index in range(5)
            ]:
                raise RuntimeError(f"wrong equivariant Bad D-cycle: {d_cycle}")

        if args.skip_e677:
            print(f"status: BASE SHELL SAT VERIFIED; elapsed={elapsed:.3f}s")
            return 0
        bad = verify(table, not args.allow_good and not args.terminal_k5)
        if args.terminal_k5:
            expected_bad = set(block_list[0])
            if set(bad) != expected_bad:
                raise RuntimeError(
                    f"terminal K5 colour mismatch: expected {sorted(expected_bad)}, got {bad}"
                )
            for point in expected_bad:
                d_value = table[table[table[point][point]][point]][point]
                if d_value not in expected_bad:
                    raise RuntimeError(f"terminal K5 HIT at {point}: D={d_value}")
        print(f"status: SAT VERIFIED; bad={bad}; elapsed={elapsed:.3f}s")
        for row in table:
            print(" ".join(map(str, row)))
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
