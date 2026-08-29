"""Exact order-9 no-HIT scan split by the cardinality of Bad.

The formula searches for a full E677 magma in which the element named 0 is
Bad, defines every Good/Bad colour by the unique-fixer criterion, computes D
exactly, and requires D(Bad) to be contained in Bad.  The eight cardinality
cubes are exhaustive.  Every SAT table is decoded and checked independently.
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


def exactly_one(clauses: list[list[int]], literals: list[int]) -> None:
    clauses.append(literals)
    for left, right in itertools.combinations(literals, 2):
        clauses.append([-left, -right])


def verify(table: list[list[int]], expected_bad_count: int) -> list[int]:
    order = len(table)
    for row in table:
        if sorted(row) != list(range(order)):
            raise RuntimeError("decoded left row is not a permutation")
    for x in range(order):
        for y in range(order):
            value = table[y][table[x][table[table[y][x]][y]]]
            if value != x:
                raise RuntimeError(f"E677 failure at x={x}, y={y}: {value}")
    d_map = [table[table[table[x][x]][x]][x] for x in range(order)]
    bad = [x for x in range(order) if not any(table[row][x] == x for row in range(order))]
    if 0 not in bad:
        raise RuntimeError(f"zero is not Bad: bad={bad}")
    if len(bad) != expected_bad_count:
        raise RuntimeError(f"wrong Bad count: expected {expected_bad_count}, got {bad}")
    bad_set = set(bad)
    hits = [(x, d_map[x]) for x in bad if d_map[x] not in bad_set]
    if hits:
        raise RuntimeError(f"decoded table has HIT: {hits}")
    return bad


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--solver", default="cadical195")
    parser.add_argument("--per-count-seconds", type=int, default=20)
    parser.add_argument("--min-bad", type=int, default=2)
    parser.add_argument("--max-bad", type=int, default=9)
    parser.add_argument("--scan-bad2-structural", action="store_true")
    parser.add_argument("--bad2-case", type=int, choices=(1, 2, 3, 4))
    parser.add_argument("--scan-bad3-structural", action="store_true")
    parser.add_argument("--bad3-case", type=int, choices=range(1, 25))
    parser.add_argument("--bad3-frontier-only", action="store_true")
    parser.add_argument("--bad3-root-pair-split", action="store_true")
    parser.add_argument("--bad3-canonical-root-outcomes", action="store_true")
    parser.add_argument("--bad3-good-product-reps-only", action="store_true")
    parser.add_argument("--bad3-companion-pilot", action="store_true")
    parser.add_argument("--bad3-case2-reduction", action="store_true")
    parser.add_argument("--crossing-profiles", action="store_true")
    parser.add_argument("--case3-term-cores", action="store_true")
    parser.add_argument("--case4-product-cores", action="store_true")
    parser.add_argument("--conflict-budget", type=int, default=300000)
    args = parser.parse_args()

    order = 9
    if not 2 <= args.min_bad <= args.max_bad <= order:
        raise SystemExit("require 2 <= min-bad <= max-bad <= 9")

    def cell(row: int, inp: int, value: int) -> int:
        return 1 + ((row * order + inp) * order + value)

    clauses: list[list[int]] = []
    for row in range(order):
        for inp in range(order):
            exactly_one(clauses, [cell(row, inp, value) for value in range(order)])
        for value in range(order):
            exactly_one(clauses, [cell(row, inp, value) for inp in range(order)])

    # Zero is a distinguished Bad point.  Relabelling the other eight points
    # gives the same exhaustive four-way normalization as the direct scan:
    # 1*0=1, or 1*0=2 with 2*0 in {1,2,3}.
    for row in range(order):
        clauses.append([-cell(row, 0, 0)])
    clauses.append([cell(0, 0, 1)])
    if not args.scan_bad2_structural and not args.scan_bad3_structural:
        clauses.append([cell(1, 0, 1), cell(1, 0, 2)])
        clauses.append([
            -cell(1, 0, 2),
            cell(2, 0, 1),
            cell(2, 0, 2),
            cell(2, 0, 3),
        ])

    next_variable = order**3 + 1

    # All E677 instances: u=y*x, v=u*y, w=x*v, y*w=x.
    for x in range(order):
        for y in range(order):
            v_aux = list(range(next_variable, next_variable + order))
            next_variable += order
            w_aux = list(range(next_variable, next_variable + order))
            next_variable += order
            exactly_one(clauses, v_aux)
            exactly_one(clauses, w_aux)
            for u in range(order):
                for v in range(order):
                    clauses.append([-cell(y, x, u), -cell(u, y, v), v_aux[v]])
            for v in range(order):
                for w in range(order):
                    clauses.append([-v_aux[v], -cell(x, v, w), w_aux[w]])
            for w in range(order):
                clauses.append([-w_aux[w], cell(y, w, x)])

    # Audited redundant y=0 and x=0 consequences used by the direct solver.
    for p in range(order):
        for x in range(order):
            for z in range(order):
                for a in range(order):
                    clauses.append([
                        -cell(0, p, x),
                        -cell(0, x, z),
                        -cell(z, 0, a),
                        cell(x, a, p),
                    ])
    for p in range(order):
        for z in range(order):
            clauses.append([-cell(0, p, z), -cell(z, 0, p)])

    for y in range(order):
        for a in range(order):
            for b in range(order):
                for p in range(order):
                    clauses.append([
                        -cell(y, 0, a),
                        -cell(y, b, 0),
                        -cell(0, p, b),
                        cell(a, y, p),
                    ])
    for y in range(1, order):
        for a in range(order):
            for b in range(order):
                for p in range(order):
                    clauses.append([
                        -cell(y, 0, a),
                        -cell(a, 0, p),
                        -cell(y, b, 0),
                        -cell(0, p, b),
                    ])

    # bad[x] is equivalent to the absence of a left fixer of input x.
    bad_literals = list(range(next_variable, next_variable + order))
    next_variable += order
    for x, bad_x in enumerate(bad_literals):
        fixers = [cell(row, x, x) for row in range(order)]
        for fixer in fixers:
            clauses.append([-bad_x, -fixer])
        clauses.append([bad_x, *fixers])
    clauses.append([bad_literals[0]])

    # Compute sigma(x)=(x*x)*x and D(x)=sigma(x)*x exactly.
    d_literals: list[list[int]] = []
    for x in range(order):
        sigma = list(range(next_variable, next_variable + order))
        next_variable += order
        d_value = list(range(next_variable, next_variable + order))
        next_variable += order
        exactly_one(clauses, sigma)
        exactly_one(clauses, d_value)
        for square in range(order):
            for value in range(order):
                clauses.append([
                    -cell(x, x, square),
                    -cell(square, x, value),
                    sigma[value],
                ])
        for sigma_value in range(order):
            for value in range(order):
                clauses.append([
                    -sigma[sigma_value],
                    -cell(sigma_value, x, value),
                    d_value[value],
                ])
        d_literals.append(d_value)

    # Exact no-HIT condition D(Bad) subset Bad.
    for x in range(order):
        for value in range(order):
            clauses.append([-bad_literals[x], -d_literals[x][value], bad_literals[value]])

    # Gated exact-cardinality constraints for one shared solver.
    activations: dict[int, int] = {}
    for bad_count in range(args.min_bad, args.max_bad + 1):
        activation = next_variable
        next_variable += 1
        activations[bad_count] = activation
        for chosen in itertools.combinations(bad_literals, bad_count + 1):
            clauses.append([-activation, *(-literal for literal in chosen)])
        for chosen in itertools.combinations(bad_literals, order - bad_count + 1):
            clauses.append([-activation, *chosen])

    bad3_root_witnesses: list[int] = []
    bad3_root_witnesses_by_pair: dict[tuple[int, int], list[int]] = {}
    bad3_root_pair_activations: dict[tuple[int, int], int] = {}
    bad3_root_good_activations: dict[tuple[int, int], int] = {}
    if args.scan_bad3_structural:
        # The terminal equality/no-HIT branch is already closed at order 9.
        # Since the three diagonal states are always Omega-roots, every
        # surviving |Bad|=3 model must have a non-diagonal root (v,h).
        # Its product u=v*h is either Good, or it is Bad with N_B(u,v)=0.
        activation = activations[3]
        for row in range(order):
            for inp in range(order):
                if row == inp:
                    continue
                pair_witnesses: list[int] = []
                for product in range(order):
                    witness = next_variable
                    next_variable += 1
                    bad3_root_witnesses.append(witness)
                    pair_witnesses.append(witness)
                    clauses.extend([
                        [-witness, bad_literals[row]],
                        [-witness, bad_literals[inp]],
                        [-witness, cell(row, inp, product)],
                    ])
                    for carrier in range(order):
                        clauses.append([
                            -witness,
                            -bad_literals[product],
                            -bad_literals[carrier],
                            -cell(carrier, product, row),
                        ])
                bad3_root_witnesses_by_pair[(row, inp)] = pair_witnesses
                pair_activation = next_variable
                next_variable += 1
                bad3_root_pair_activations[(row, inp)] = pair_activation
                clauses.append([-pair_activation, *pair_witnesses])
                good_activation = next_variable
                next_variable += 1
                bad3_root_good_activations[(row, inp)] = good_activation
                clauses.append([-good_activation, *pair_witnesses])
                for product, witness in enumerate(pair_witnesses):
                    clauses.append([
                        -good_activation,
                        -witness,
                        -bad_literals[product],
                    ])
        clauses.append([-activation, *bad3_root_witnesses])

    if args.scan_bad2_structural:
        # If exactly two points are Bad, every state in Bad x Bad is an
        # Omega-root.  Squares are roots by the general square-root lemma.
        # For r!=u, a Bad value r*u cannot be u (a forbidden fixer), hence it
        # is r; then the target indegree is N_B(r,r)=0.  Therefore no tau edge
        # from Bad x Bad can have both target coordinates Bad.
        activation = activations[2]
        for row in range(order):
            for inp in range(order):
                for value in range(order):
                    for hinge in range(order):
                        clauses.append([
                            -activation,
                            -bad_literals[row],
                            -bad_literals[inp],
                            -bad_literals[value],
                            -bad_literals[hinge],
                            -cell(row, inp, value),
                            -cell(value, hinge, inp),
                        ])

    print(
        f"encoding: order=9; variables={next_variable-1}; clauses={len(clauses)}; "
        f"solver={args.solver}; no-HIT=True; bad-counts={args.min_bad}..{args.max_bad}; "
        f"bad2-structural={args.scan_bad2_structural}; "
        f"bad3-structural={args.scan_bad3_structural}",
        flush=True,
    )

    cadical_solver = args.solver.lower() in {
        "cadical195", "cd195", "cdl195", "cd19", "cdl19",
    }

    def limited_solve(solver: Solver, assumptions: list[int]):
        if cadical_solver:
            solver.conf_budget(args.conflict_budget)
            return solver.solve_limited(assumptions=assumptions)
        timer = threading.Timer(max(1, args.per_count_seconds), solver.interrupt)
        timer.daemon = True
        timer.start()
        try:
            return solver.solve_limited(assumptions=assumptions, expect_interrupt=True)
        finally:
            timer.cancel()

    started = time.time()
    unsat_counts: list[int] = []
    unknown_counts: list[int] = []
    with Solver(name=args.solver, bootstrap_with=clauses, use_timer=True) as solver:
        # A simple cyclic table is only a phase preference, never a clause.
        phases = []
        for row in range(order):
            shift = 1 if row != 1 else 2
            for inp in range(order):
                chosen = (inp + shift) % order
                for value in range(order):
                    literal = cell(row, inp, value)
                    phases.append(literal if value == chosen else -literal)
        solver.set_phases(phases)

        if args.scan_bad2_structural:
            if 2 not in activations:
                raise RuntimeError("bad2 structural scan requires a cardinality-2 activation")
            bad01 = [bad_literals[0], bad_literals[1], *(-bad_literals[x] for x in range(2, order))]
            bad02 = [
                bad_literals[0],
                -bad_literals[1],
                bad_literals[2],
                *(-bad_literals[x] for x in range(3, order)),
            ]
            cases = [
                (
                    "B={0,1}; f(1)=1",
                    [*bad01, cell(1, 0, 1), d_literals[0][1], d_literals[1][0]],
                ),
                (
                    "B={0,1}; f(1)=2,f(2)=1",
                    [
                        *bad01,
                        cell(1, 0, 2),
                        cell(2, 0, 1),
                        d_literals[0][1],
                        d_literals[1][0],
                    ],
                ),
                (
                    "B={0,2}; f(1)=2,f(2)=2",
                    [
                        *bad02,
                        cell(1, 0, 2),
                        cell(2, 0, 2),
                        d_literals[0][2],
                        d_literals[2][0],
                    ],
                ),
                (
                    "B={0,2}; f(1)=3,f(3)=2",
                    [
                        *bad02,
                        cell(1, 0, 3),
                        cell(3, 0, 2),
                        d_literals[0][2],
                        d_literals[2][0],
                    ],
                ),
            ]
            if args.bad2_case is not None:
                cases = [cases[args.bad2_case - 1]]
            if args.case3_term_cores:
                if args.bad2_case != 3:
                    raise RuntimeError("case3 term cores require --bad2-case 3")
                name, structural = cases[0]
                # The surviving profile has a=0*2 and g=2*2 Good.  Label 3
                # is free, so normalize a=3.  Then g is 1 or a new label 4;
                # g cannot equal a because 0*a=0 while 0*g=h is Good.  After
                # fixing g, the displayed h-orbits exhaust residual labels.
                term_orbits = [
                    (1, 3),
                    (1, 4),
                    (4, 1),
                    (4, 3),
                    (4, 5),
                ]
                cases = []
                for g_value, h_value in term_orbits:
                    cases.append((
                        f"{name}; a=3,g={g_value},h={h_value}",
                        [
                            *structural,
                            cell(0, 2, 3),
                            cell(0, 3, 0),
                            cell(2, 2, g_value),
                            cell(g_value, 2, h_value),
                            cell(2, h_value, 0),
                            cell(h_value, 2, 0),
                            cell(0, g_value, h_value),
                        ],
                    ))
            if args.case4_product_cores:
                if args.bad2_case != 4:
                    raise RuntimeError("case4 product cores require --bad2-case 4")
                name, structural = cases[0]
                product_cases: list[tuple[str, list[int]]] = []
                for a_value in (3, 4):
                    fixed_after_a = {1, 3, a_value}
                    new_b = next(value for value in range(4, order) if value not in fixed_after_a)
                    b_values = [*sorted(fixed_after_a), new_b]
                    for b_value in b_values:
                        fixed_after_b = {*fixed_after_a, b_value}
                        new_c = next(
                            value for value in range(4, order) if value not in fixed_after_b
                        )
                        c_values = [
                            *sorted(fixed_after_b - {b_value}),
                            new_c,
                        ]
                        for c_value in c_values:
                            product_cases.append((
                                f"{name}; a={a_value},b={b_value},c={c_value}",
                                [
                                    *structural,
                                    cell(0, 2, a_value),
                                    cell(2, 0, b_value),
                                    cell(2, 2, c_value),
                                ],
                            ))
                if len(product_cases) != 20:
                    raise RuntimeError(f"expected 20 case4 product orbits, got {len(product_cases)}")
                cases = product_cases
            if args.crossing_profiles:
                if args.bad2_case not in (3, 4):
                    raise RuntimeError("crossing profiles require --bad2-case 3 or 4")
                profiled_cases: list[tuple[str, list[int]]] = []
                profile_cells = [(0, 2), (2, 2)]
                if args.bad2_case == 4:
                    profile_cells.insert(1, (2, 0))
                for name, structural in cases:
                    for colours in itertools.product((False, True), repeat=len(profile_cells)):
                        profile_literals: list[int] = []
                        labels = []
                        for (row, inp), is_good in zip(profile_cells, colours):
                            labels.append(f"{row}*{inp}={'G' if is_good else 'B'}")
                            if is_good:
                                profile_literals.extend([
                                    -cell(row, inp, 0),
                                    -cell(row, inp, 2),
                                ])
                            else:
                                bad_value = 0 if inp == 2 else 2
                                profile_literals.append(cell(row, inp, bad_value))
                        profiled_cases.append(
                            (f"{name}; {','.join(labels)}", [*structural, *profile_literals])
                        )
                cases = profiled_cases
            case_unknown: list[str] = []
            case_unsat: list[str] = []
            for name, structural in cases:
                before = solver.accum_stats().copy()
                case_started = time.time()
                result = limited_solve(solver, [activations[2], *structural])
                elapsed = time.time() - case_started
                after = solver.accum_stats().copy()
                conflicts = after.get("conflicts", 0) - before.get("conflicts", 0)
                status = "SAT" if result is True else "UNSAT" if result is False else "UNKNOWN"
                print(
                    f"bad2 case {name}: {status}; elapsed={elapsed:.3f}s; "
                    f"conflicts={conflicts}",
                    flush=True,
                )
                if result is True:
                    model = {literal for literal in solver.get_model() if literal > 0}
                    table = [
                        [
                            next(
                                value
                                for value in range(order)
                                if cell(row, inp, value) in model
                            )
                            for inp in range(order)
                        ]
                        for row in range(order)
                    ]
                    bad = verify(table, 2)
                    print(f"status: VERIFIED NO-HIT COUNTEREXAMPLE; bad={bad}", flush=True)
                    for row in table:
                        print(" ".join(map(str, row)), flush=True)
                    return 0
                if result is False:
                    case_unsat.append(name)
                else:
                    case_unknown.append(name)
                    if not cadical_solver:
                        solver.clear_interrupt()
            print(
                f"bad2 summary: unsat={len(case_unsat)}/{len(cases)}; "
                f"unknown={case_unknown}; elapsed={time.time()-started:.3f}s",
                flush=True,
            )
            return 2 if not case_unknown else 3

        if args.scan_bad3_structural:
            if 3 not in activations:
                raise RuntimeError("bad3 structural scan requires a cardinality-3 activation")

            bad012 = [
                bad_literals[0],
                bad_literals[1],
                bad_literals[2],
                *(-bad_literals[x] for x in range(3, order)),
            ]
            bad023 = [
                bad_literals[0],
                -bad_literals[1],
                bad_literals[2],
                bad_literals[3],
                *(-bad_literals[x] for x in range(4, order)),
            ]

            # Choose 0 on a D-cycle and normalize 0*0=1.  If 1 is Bad,
            # D(0) is 1 or the other Bad label 2.  If 1 is Good, normalize
            # D(0)=2 and the third Bad label to 3.  On three nonfixed points
            # D is either a 3-cycle or a 2-cycle with one tail, whose target
            # is one of the two cycle points.
            families = [
                (
                    "A:square-Bad,D0=1",
                    bad012,
                    1,
                    [
                        ("f1=1", [cell(1, 0, 1)]),
                        ("f1=2,f2=1", [cell(1, 0, 2), cell(2, 0, 1)]),
                        ("f1=3,f3=1", [cell(1, 0, 3), cell(3, 0, 1)]),
                    ],
                ),
                (
                    "B:square-Bad,D0=2",
                    bad012,
                    2,
                    [
                        ("f1=2,f2=2", [cell(1, 0, 2), cell(2, 0, 2)]),
                        ("f1=3,f3=2", [cell(1, 0, 3), cell(3, 0, 2)]),
                    ],
                ),
                (
                    "C:square-Good,D0=2",
                    bad023,
                    2,
                    [
                        ("f1=2,f2=2", [cell(1, 0, 2), cell(2, 0, 2)]),
                        ("f1=3,f3=2", [cell(1, 0, 3), cell(3, 0, 2)]),
                        ("f1=4,f4=2", [cell(1, 0, 4), cell(4, 0, 2)]),
                    ],
                ),
            ]

            cases: list[
                tuple[
                    str,
                    list[int],
                    tuple[int, int, int],
                    tuple[tuple[int, int], ...],
                ]
            ] = []
            for family_name, bad_cube, d0, f_forms in families:
                remaining_bad = 2 if d0 == 1 else (1 if family_name.startswith("B:") else 3)
                d_forms = [
                    (
                        "D-3cycle",
                        [
                            d_literals[0][d0],
                            d_literals[d0][remaining_bad],
                            d_literals[remaining_bad][0],
                        ],
                    ),
                    (
                        "D-2cycle,tail->0",
                        [
                            d_literals[0][d0],
                            d_literals[d0][0],
                            d_literals[remaining_bad][0],
                        ],
                    ),
                    (
                        "D-2cycle,tail->D0",
                        [
                            d_literals[0][d0],
                            d_literals[d0][0],
                            d_literals[remaining_bad][d0],
                        ],
                    ),
                ]
                for d_name, d_cube in d_forms:
                    if d_name == "D-3cycle":
                        canonical_root_pairs = (
                            (0, d0),
                            (0, remaining_bad),
                        )
                    else:
                        canonical_root_pairs = (
                            (0, d0),
                            (0, remaining_bad),
                            (remaining_bad, 0),
                        )
                    for f_name, f_cube in f_forms:
                        cases.append((
                            f"{family_name}; {d_name}; {f_name}",
                            [*bad_cube, *d_cube, *f_cube],
                            (0, d0, remaining_bad),
                            canonical_root_pairs,
                        ))

            if len(cases) != 24:
                raise RuntimeError(f"expected 24 bad3 structural cases, got {len(cases)}")
            indexed_cases = list(enumerate(cases, start=1))
            if args.bad3_frontier_only:
                frontier_indices = {2, 3, 11, 15, 16, 18, 21, 23, 24}
                indexed_cases = [
                    item for item in indexed_cases if item[0] in frontier_indices
                ]
            if args.bad3_case is not None:
                indexed_cases = [
                    item for item in indexed_cases if item[0] == args.bad3_case
                ]
                if not indexed_cases:
                    raise RuntimeError("selected bad3 case was filtered out")

            split_cases: list[tuple[int, str, list[int]]] = []

            def good_product_representatives(
                name: str,
                row: int,
            ) -> tuple[int, ...]:
                # Residual relabelling fixes every displayed label and is
                # transitive on the unnamed Good labels.  Row zero already
                # uses output 1 at input zero, so an off-diagonal row-zero
                # root cannot have product 1.
                if name.startswith("A:"):
                    if "f1=3,f3=1" in name:
                        return (3, 4)
                    if row == 2 and "f1=2,f2=1" in name:
                        return ()
                    return (3,)
                if name.startswith("B:"):
                    if "f1=3,f3=2" in name:
                        return (3,) if row == 1 else (3, 4)
                    return () if row == 1 else (3,)
                if "f1=4,f4=2" in name:
                    return (1, 4, 5) if row == 3 else (4, 5)
                if "f1=3,f3=2" in name:
                    return () if row == 3 else (4,)
                return (1, 4) if row == 3 else (4,)

            for index, (
                name,
                structural,
                bad_labels,
                canonical_root_pairs,
            ) in indexed_cases:
                if args.bad3_case2_reduction:
                    if index != 2:
                        continue
                    split_cases.extend([
                        (
                            index,
                            f"{name}; root=(0,1),product=row=0",
                            [
                                *structural,
                                bad3_root_witnesses_by_pair[(0, 1)][0],
                            ],
                        ),
                        (
                            index,
                            f"{name}; root=(0,1),product=third=2",
                            [
                                *structural,
                                bad3_root_witnesses_by_pair[(0, 1)][2],
                            ],
                        ),
                        (
                            index,
                            f"{name}; root=(0,2),product=row=0",
                            [
                                *structural,
                                bad3_root_witnesses_by_pair[(0, 2)][0],
                            ],
                        ),
                        (
                            index,
                            f"{name}; root=(0,2),product=third=1",
                            [
                                *structural,
                                bad3_root_witnesses_by_pair[(0, 2)][1],
                            ],
                        ),
                    ])
                    for hinge in (2, 3, 4, 5):
                        split_cases.append((
                            index,
                            f"{name}; root=(0,1),u=3,a=4,k={hinge}",
                            [
                                *structural,
                                bad3_root_witnesses_by_pair[(0, 1)][3],
                                cell(0, 3, 4),
                                cell(4, 0, hinge),
                                cell(3, hinge, 1),
                            ],
                        ))
                elif args.bad3_companion_pilot:
                    if index != 2:
                        continue
                    # In case 2 with root (0,1) and Good product 3, the
                    # y=0 companion word is
                    #   0*1=3, 0*3=a, a*0=k, 3*k=1.
                    # Row-zero injectivity excludes a=1,3.  The choices
                    # a=0,2 both give k=1 and hence the forbidden fixer
                    # 3*1=1 of the Bad point 1.  Residual Good symmetry
                    # therefore normalizes a=4.  Then k is 2,3,4 or a new
                    # Good label 5; k=0 is a fixer of Bad 0 and k=1 would
                    # again fix Bad 1.
                    for hinge in (2, 3, 4, 5):
                        split_cases.append((
                            index,
                            f"{name}; root=(0,1),u=3,a=4,k={hinge}",
                            [
                                *structural,
                                bad3_root_witnesses_by_pair[(0, 1)][3],
                                cell(0, 3, 4),
                                cell(4, 0, hinge),
                                cell(3, hinge, 1),
                            ],
                        ))
                elif args.bad3_good_product_reps_only:
                    for row, inp in canonical_root_pairs:
                        for product in good_product_representatives(name, row):
                            split_cases.append((
                                index,
                                f"{name}; root=({row},{inp}),product=Good:{product}",
                                [
                                    *structural,
                                    bad3_root_witnesses_by_pair[(row, inp)][product],
                                ],
                            ))
                elif args.bad3_canonical_root_outcomes:
                    for row, inp in canonical_root_pairs:
                        third = next(
                            value for value in bad_labels if value not in (row, inp)
                        )
                        split_cases.extend([
                            (
                                index,
                                f"{name}; root=({row},{inp}),product=Good",
                                [
                                    *structural,
                                    bad3_root_good_activations[(row, inp)],
                                ],
                            ),
                            (
                                index,
                                f"{name}; root=({row},{inp}),product=row={row}",
                                [
                                    *structural,
                                    bad3_root_witnesses_by_pair[(row, inp)][row],
                                ],
                            ),
                            (
                                index,
                                f"{name}; root=({row},{inp}),product=third={third}",
                                [
                                    *structural,
                                    bad3_root_witnesses_by_pair[(row, inp)][third],
                                ],
                            ),
                        ])
                elif args.bad3_root_pair_split:
                    for row, inp in itertools.permutations(bad_labels, 2):
                        split_cases.append((
                            index,
                            f"{name}; extra-root=({row},{inp})",
                            [*structural, bad3_root_pair_activations[(row, inp)]],
                        ))
                else:
                    split_cases.append((index, name, structural))

            case_unknown: list[str] = []
            case_unsat: list[str] = []
            for ordinal, (index, name, structural) in enumerate(split_cases, start=1):
                before = solver.accum_stats().copy()
                case_started = time.time()
                result = limited_solve(solver, [activations[3], *structural])
                elapsed = time.time() - case_started
                after = solver.accum_stats().copy()
                conflicts = after.get("conflicts", 0) - before.get("conflicts", 0)
                status = "SAT" if result is True else "UNSAT" if result is False else "UNKNOWN"
                print(
                    f"bad3 case {index:02d}/24 split {ordinal}/{len(split_cases)} "
                    f"{name}: {status}; "
                    f"elapsed={elapsed:.3f}s; conflicts={conflicts}",
                    flush=True,
                )
                if result is True:
                    model = {literal for literal in solver.get_model() if literal > 0}
                    table = [
                        [
                            next(
                                value
                                for value in range(order)
                                if cell(row, inp, value) in model
                            )
                            for inp in range(order)
                        ]
                        for row in range(order)
                    ]
                    bad = verify(table, 3)
                    d_map = [table[table[table[x][x]][x]][x] for x in range(order)]
                    print(
                        f"status: VERIFIED NO-HIT COUNTEREXAMPLE; bad={bad}; "
                        f"D(Bad)={[d_map[x] for x in bad]}",
                        flush=True,
                    )
                    for row in table:
                        print(" ".join(map(str, row)), flush=True)
                    return 0
                if result is False:
                    case_unsat.append(name)
                else:
                    case_unknown.append(name)
                    if not cadical_solver:
                        solver.clear_interrupt()
            print(
                f"bad3 summary: unsat={len(case_unsat)}/{len(split_cases)}; "
                f"unknown={case_unknown}; elapsed={time.time()-started:.3f}s",
                flush=True,
            )
            return 2 if not case_unknown else 3

        for bad_count in range(args.min_bad, args.max_bad + 1):
            before = solver.accum_stats().copy()
            case_started = time.time()
            result = limited_solve(solver, [activations[bad_count]])
            elapsed = time.time() - case_started
            after = solver.accum_stats().copy()
            conflicts = after.get("conflicts", 0) - before.get("conflicts", 0)
            status = "SAT" if result is True else "UNSAT" if result is False else "UNKNOWN"
            print(
                f"|Bad|={bad_count}: {status}; elapsed={elapsed:.3f}s; "
                f"conflicts={conflicts}",
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
                bad = verify(table, bad_count)
                print(f"status: VERIFIED NO-HIT COUNTEREXAMPLE; bad={bad}", flush=True)
                for row in table:
                    print(" ".join(map(str, row)), flush=True)
                return 0
            if result is False:
                unsat_counts.append(bad_count)
            else:
                unknown_counts.append(bad_count)
                if not cadical_solver:
                    solver.clear_interrupt()

    print(
        f"summary: unsat={unsat_counts}; unknown={unknown_counts}; "
        f"elapsed={time.time()-started:.3f}s",
        flush=True,
    )
    return 2 if not unknown_counts else 3


if __name__ == "__main__":
    raise SystemExit(main())
