"""Exact skew row-label extension search for an E677 counterexample.

Starting with a verified base magma B and a permutation theta of its labels,
define the base block of a lifted product by

    base((a,i)*(b,j)) = B[theta^i(a)][b].

The fibre output P[a,i,b](j) is an arbitrary permutation in j.  Thus every
left row of the complete lifted table is a permutation, while the induced
base-block action genuinely depends on the left fibre coordinate.  This is
not an ordinary cover.
"""

from __future__ import annotations

import argparse
import itertools
import sys
import threading
import time
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools" / "vendor" / "python_sat311"))
from pysat.solvers import Solver  # type: ignore


def exactly_one(clauses: list[list[int]], literals: list[int], gate: int | None = None) -> None:
    prefix = [] if gate is None else [-gate]
    clauses.append([*prefix, *literals])
    for left, right in itertools.combinations(literals, 2):
        clauses.append([*prefix, -left, -right])


def load_table(path: Path) -> list[list[int]]:
    table = [[int(value) for value in line.split()] for line in path.read_text().splitlines() if line.strip()]
    n = len(table)
    if n == 0 or any(len(row) != n for row in table):
        raise RuntimeError(f"malformed table: {path}")
    return table


def verify_e677(table: list[list[int]]) -> None:
    n = len(table)
    if any(sorted(row) != list(range(n)) for row in table):
        raise RuntimeError("a left row is not a permutation")
    for x in range(n):
        for y in range(n):
            value = table[y][table[x][table[table[y][x]][y]]]
            if value != x:
                raise RuntimeError(f"E677 failure at x={x}, y={y}: {value}")


def bad_points(table: list[list[int]]) -> list[int]:
    return [x for x in range(len(table)) if table[table[table[x][x]][x]][x] != x]


def powers(permutation: list[int], count: int) -> list[list[int]]:
    result = [list(range(len(permutation)))]
    for _ in range(1, count):
        result.append([permutation[result[-1][x]] for x in range(len(permutation))])
    return result


def permutation_parity(permutation: list[int]) -> int:
    return sum(
        permutation[left] > permutation[right]
        for left in range(len(permutation))
        for right in range(left + 1, len(permutation))
    ) % 2


def permutation_cycle_type(permutation: tuple[int, ...]) -> tuple[int, ...]:
    seen: set[int] = set()
    lengths = []
    for start in range(len(permutation)):
        if start in seen:
            continue
        value, length = start, 0
        while value not in seen:
            seen.add(value)
            value = permutation[value]
            length += 1
        lengths.append(length)
    return tuple(sorted(lengths, reverse=True))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", type=Path, default=ROOT / "cache" / "eq677-db" / "5" / "0")
    parser.add_argument("--fibre", type=int, default=5)
    parser.add_argument("--theta")
    parser.add_argument("--row-maps")
    parser.add_argument("--target-base", type=int, default=0)
    parser.add_argument("--target-fibre", type=int, default=0)
    parser.add_argument("--allow-good", action="store_true")
    parser.add_argument("--basepair-core", action="store_true")
    parser.add_argument("--sample-basepair")
    parser.add_argument("--sample-models", type=int, default=100)
    parser.add_argument("--shared-a", type=int)
    parser.add_argument("--shared-b", type=int)
    parser.add_argument("--classify-incoming-signs", action="store_true")
    parser.add_argument("--force-incoming-signs")
    parser.add_argument("--classify-shared-block")
    parser.add_argument("--twopair-parity")
    parser.add_argument("--twopair-cycletypes")
    parser.add_argument("--twopair-exact-core")
    parser.add_argument("--solver", default="glucose42")
    parser.add_argument("--seconds", type=float, default=180.0)
    args = parser.parse_args()

    base = load_table(args.base)
    verify_e677(base)
    m, k = len(base), args.fibre
    theta = list(range(1, m)) + [0] if args.theta is None else [int(value) for value in args.theta.split(",")]
    if args.row_maps is None:
        if sorted(theta) != list(range(m)):
            raise SystemExit("theta must be a permutation of the base labels")
        row_maps = powers(theta, k)
        row_map_label = f"theta={theta}"
    else:
        encoded_maps = args.row_maps.split("/")
        row_maps = [[int(value) for value in encoded] for encoded in encoded_maps]
        if len(row_maps) != k or any(sorted(permutation) != list(range(m)) for permutation in row_maps):
            raise SystemExit("row-maps must contain one base permutation per fibre label")
        row_map_label = f"row-maps={args.row_maps}"

    def row_label(left_base: int, left_fibre: int) -> int:
        return row_maps[left_fibre][left_base]

    def out_base(left_base: int, left_fibre: int, right_base: int) -> int:
        return base[row_label(left_base, left_fibre)][right_base]

    def cell(left_base: int, left_fibre: int, right_base: int, right_fibre: int, out_fibre: int) -> int:
        return 1 + (((((left_base * k + left_fibre) * m + right_base) * k + right_fibre) * k) + out_fibre)

    clauses: list[list[int]] = []
    for left_base in range(m):
        for left_fibre in range(k):
            for right_base in range(m):
                for right_fibre in range(k):
                    exactly_one(
                        clauses,
                        [cell(left_base, left_fibre, right_base, right_fibre, value) for value in range(k)],
                    )
                for value in range(k):
                    exactly_one(
                        clauses,
                        [cell(left_base, left_fibre, right_base, right_fibre, value) for right_fibre in range(k)],
                    )

    order = m * k
    next_variable = m * m * k ** 3 + 1
    selectors: dict[tuple[int, int], int] = {}
    if args.basepair_core:
        if not args.allow_good:
            raise SystemExit("--basepair-core requires --allow-good")
        for x_base in range(m):
            for y_base in range(m):
                selectors[x_base, y_base] = next_variable
                next_variable += 1
    auxiliary: list[tuple[list[int], list[int], int, int, int, int]] = []
    for x_base in range(m):
        for x_fibre in range(k):
            for y_base in range(m):
                for y_fibre in range(k):
                    gate = selectors.get((x_base, y_base))
                    v_aux = list(range(next_variable, next_variable + order))
                    next_variable += order
                    w_aux = list(range(next_variable, next_variable + order))
                    next_variable += order
                    auxiliary.append((v_aux, w_aux, x_base, x_fibre, y_base, y_fibre))
                    exactly_one(clauses, v_aux, gate)
                    exactly_one(clauses, w_aux, gate)

                    u_base = out_base(y_base, y_fibre, x_base)
                    for u_fibre in range(k):
                        v_base = out_base(u_base, u_fibre, y_base)
                        for v_fibre in range(k):
                            v_full = k * v_base + v_fibre
                            clauses.append(
                                ([ -gate ] if gate is not None else []) + [
                                    -cell(y_base, y_fibre, x_base, x_fibre, u_fibre),
                                    -cell(u_base, u_fibre, y_base, y_fibre, v_fibre),
                                    v_aux[v_full],
                                ]
                            )

                    for v_full in range(order):
                        v_base, v_fibre = divmod(v_full, k)
                        w_base = out_base(x_base, x_fibre, v_base)
                        for w_fibre in range(k):
                            w_full = k * w_base + w_fibre
                            clauses.append(
                                ([ -gate ] if gate is not None else []) + [
                                    -v_aux[v_full],
                                    -cell(x_base, x_fibre, v_base, v_fibre, w_fibre),
                                    w_aux[w_full],
                                ]
                            )

                    for w_full in range(order):
                        w_base, w_fibre = divmod(w_full, k)
                        final_base = out_base(y_base, y_fibre, w_base)
                        if final_base != x_base:
                            clauses.append(([-gate] if gate is not None else []) + [-w_aux[w_full]])
                        else:
                            clauses.append(
                                ([-gate] if gate is not None else [])
                                + [-w_aux[w_full], cell(y_base, y_fibre, w_base, w_fibre, x_fibre)]
                            )

    # Force the named target to violate E255 unless this is an E677-only
    # control run.
    x_base, x_fibre = args.target_base, args.target_fibre
    if not 0 <= x_base < m or not 0 <= x_fibre < k:
        raise SystemExit("target is out of range")
    if not args.allow_good:
        first_base = out_base(x_base, x_fibre, x_base)
        for first_fibre in range(k):
            second_base = out_base(first_base, first_fibre, x_base)
            for second_fibre in range(k):
                third_base = out_base(second_base, second_fibre, x_base)
                if third_base != x_base:
                    continue
                clauses.append(
                    [
                        -cell(x_base, x_fibre, x_base, x_fibre, first_fibre),
                        -cell(first_base, first_fibre, x_base, x_fibre, second_fibre),
                        -cell(second_base, second_fibre, x_base, x_fibre, x_fibre),
                    ]
                )

    print(
        f"encoding: base={m}; fibre={k}; order={order}; {row_map_label}; "
        f"variables={next_variable-1}; clauses={len(clauses)}; "
        f"target={'none' if args.allow_good else k*x_base+x_fibre}",
        flush=True,
    )
    started = time.time()
    if args.twopair_parity is not None:
        if not args.basepair_core or not args.allow_good or args.shared_a is None or args.shared_b is None:
            raise SystemExit("two-pair parity requires core mode, Good allowance, and shared a,b")
        encoded_pairs = args.twopair_parity.split(";")
        if len(encoded_pairs) != 2:
            raise SystemExit("two-pair parity format is x,y;x,y")
        pair_one, pair_two = (
            tuple(int(value) for value in encoded.split(","))
            for encoded in encoded_pairs
        )
        if pair_one not in selectors or pair_two not in selectors:
            raise SystemExit("two-pair parity contains an invalid base pair")
        original_max = next_variable - 1
        offset = original_max

        def shifted_clause(clause: list[int]) -> list[int]:
            return [literal + offset if literal > 0 else literal - offset for literal in clause]

        combined_clauses = [*clauses, *[shifted_clause(clause) for clause in clauses]]
        parity_next = 2 * original_max + 1
        fibre_permutations = list(itertools.permutations(range(k)))
        shared_blocks = [
            (args.shared_a, left_fibre, right_base)
            for left_fibre in range(k)
            for right_base in range(m)
        ] + [
            (args.shared_b, left_fibre, args.shared_a)
            for left_fibre in range(k)
        ]
        for left_base, left_fibre, right_base in shared_blocks:
            parity_one, parity_two = parity_next, parity_next + 1
            parity_next += 2
            for permutation in fibre_permutations:
                chosen = [
                    cell(left_base, left_fibre, right_base, right_fibre, permutation[right_fibre])
                    for right_fibre in range(k)
                ]
                parity_literal = parity_one if permutation_parity(list(permutation)) else -parity_one
                combined_clauses.append([*[-literal for literal in chosen], parity_literal])
                shifted = [literal + offset for literal in chosen]
                parity_literal = parity_two if permutation_parity(list(permutation)) else -parity_two
                combined_clauses.append([*[-literal for literal in shifted], parity_literal])
            combined_clauses.extend(([-parity_one, parity_two], [parity_one, -parity_two]))
        assumptions = [
            literal if pair == pair_one else -literal
            for pair, literal in selectors.items()
        ] + [
            (literal + offset) if pair == pair_two else -(literal + offset)
            for pair, literal in selectors.items()
        ]
        with Solver(name=args.solver, bootstrap_with=combined_clauses) as solver:
            result = solver.solve(assumptions=assumptions)
            if not result:
                print(
                    f"TWOPAIR-PARITY UNSAT: pairs={pair_one},{pair_two}; shared-blocks={len(shared_blocks)}; "
                    f"variables={parity_next-1}; clauses={len(combined_clauses)}"
                )
                return 2
            model = {literal for literal in solver.get_model() if literal > 0}
        profile = tuple(
            1 if (2 * original_max + 1 + 2 * index) in model else 0
            for index in range(len(shared_blocks))
        )
        print(
            f"TWOPAIR-PARITY SAT: signs alone are compatible; pairs={pair_one},{pair_two}; "
            f"profile={profile}"
        )
        return 0
    if args.twopair_cycletypes is not None:
        if not args.basepair_core or not args.allow_good or args.shared_a is None or args.shared_b is None:
            raise SystemExit("two-pair cycle types require core mode, Good allowance, and shared a,b")
        encoded_pairs = args.twopair_cycletypes.split(";")
        if len(encoded_pairs) != 2:
            raise SystemExit("two-pair cycle type format is x,y;x,y")
        pair_one, pair_two = (
            tuple(int(value) for value in encoded.split(","))
            for encoded in encoded_pairs
        )
        original_max = next_variable - 1
        offset = original_max

        def shifted_clause(clause: list[int]) -> list[int]:
            return [literal + offset if literal > 0 else literal - offset for literal in clause]

        combined_clauses = [*clauses, *[shifted_clause(clause) for clause in clauses]]
        profile_next = 2 * original_max + 1
        fibre_permutations = list(itertools.permutations(range(k)))
        cycle_types = sorted({permutation_cycle_type(permutation) for permutation in fibre_permutations})
        cycle_index = {kind: index for index, kind in enumerate(cycle_types)}
        shared_blocks = [
            (args.shared_a, left_fibre, right_base)
            for left_fibre in range(k)
            for right_base in range(m)
        ] + [
            (args.shared_b, left_fibre, args.shared_a)
            for left_fibre in range(k)
        ]
        decoded_profile_variables = []
        for left_base, left_fibre, right_base in shared_blocks:
            profile_one = list(range(profile_next, profile_next + len(cycle_types)))
            profile_next += len(cycle_types)
            profile_two = list(range(profile_next, profile_next + len(cycle_types)))
            profile_next += len(cycle_types)
            exactly_one(combined_clauses, profile_one)
            exactly_one(combined_clauses, profile_two)
            decoded_profile_variables.append(profile_one)
            for permutation in fibre_permutations:
                chosen = [
                    cell(left_base, left_fibre, right_base, right_fibre, permutation[right_fibre])
                    for right_fibre in range(k)
                ]
                kind_index = cycle_index[permutation_cycle_type(permutation)]
                combined_clauses.append([*[-literal for literal in chosen], profile_one[kind_index]])
                shifted = [literal + offset for literal in chosen]
                combined_clauses.append([*[-literal for literal in shifted], profile_two[kind_index]])
            for kind_index in range(len(cycle_types)):
                combined_clauses.extend(
                    (
                        [-profile_one[kind_index], profile_two[kind_index]],
                        [profile_one[kind_index], -profile_two[kind_index]],
                    )
                )
        assumptions = [
            literal if pair == pair_one else -literal
            for pair, literal in selectors.items()
        ] + [
            (literal + offset) if pair == pair_two else -(literal + offset)
            for pair, literal in selectors.items()
        ]
        with Solver(name=args.solver, bootstrap_with=combined_clauses) as solver:
            result = solver.solve(assumptions=assumptions)
            if not result:
                print(
                    f"TWOPAIR-CYCLETYPES UNSAT: pairs={pair_one},{pair_two}; "
                    f"shared-blocks={len(shared_blocks)}"
                )
                return 2
            model = {literal for literal in solver.get_model() if literal > 0}
        profile = tuple(
            cycle_types[next(index for index, literal in enumerate(variables) if literal in model)]
            for variables in decoded_profile_variables
        )
        print(
            f"TWOPAIR-CYCLETYPES SAT: cycle types are compatible; pairs={pair_one},{pair_two}; "
            f"profile={profile}"
        )
        return 0
    if args.twopair_exact_core is not None:
        if not args.basepair_core or not args.allow_good or args.shared_a is None or args.shared_b is None:
            raise SystemExit("two-pair exact core requires core mode, Good allowance, and shared a,b")
        encoded_pairs = args.twopair_exact_core.split(";")
        if len(encoded_pairs) != 2:
            raise SystemExit("two-pair exact core format is x,y;x,y")
        pair_one, pair_two = (
            tuple(int(value) for value in encoded.split(","))
            for encoded in encoded_pairs
        )
        original_max = next_variable - 1
        offset = original_max

        def shifted_clause(clause: list[int]) -> list[int]:
            return [literal + offset if literal > 0 else literal - offset for literal in clause]

        combined_clauses = [*clauses, *[shifted_clause(clause) for clause in clauses]]
        equality_next = 2 * original_max + 1
        shared_blocks = [
            (args.shared_a, left_fibre, right_base)
            for left_fibre in range(k)
            for right_base in range(m)
        ] + [
            (args.shared_b, left_fibre, args.shared_a)
            for left_fibre in range(k)
        ]
        equality_selectors = []
        for left_base, left_fibre, right_base in shared_blocks:
            equality_selector = equality_next
            equality_next += 1
            equality_selectors.append(equality_selector)
            for right_fibre in range(k):
                for value in range(k):
                    first = cell(left_base, left_fibre, right_base, right_fibre, value)
                    second = first + offset
                    combined_clauses.extend(
                        (
                            [-equality_selector, -first, second],
                            [-equality_selector, first, -second],
                        )
                    )
        fixed_assumptions = [
            literal if pair == pair_one else -literal
            for pair, literal in selectors.items()
        ] + [
            (literal + offset) if pair == pair_two else -(literal + offset)
            for pair, literal in selectors.items()
        ]
        with Solver(name=args.solver, bootstrap_with=combined_clauses) as solver:
            if solver.solve(assumptions=[*fixed_assumptions, *equality_selectors]):
                print("TWOPAIR-EXACT SAT: all shared blocks can agree")
                return 0
            raw_core = set(solver.get_core() or [])
            core = [literal for literal in equality_selectors if literal in raw_core]
            print(f"initial-exact-core={len(core)}", flush=True)
            for candidate in list(core):
                trial = [literal for literal in core if literal != candidate]
                trial_set = set(trial)
                equality_assumptions = [
                    literal if literal in trial_set else -literal
                    for literal in equality_selectors
                ]
                if not solver.solve(assumptions=[*fixed_assumptions, *equality_assumptions]):
                    core = trial
        block_by_selector = dict(zip(equality_selectors, shared_blocks))
        print(f"minimal-exact-core={len(core)}")
        for literal in core:
            print(f"shared-block={block_by_selector[literal]}")
        return 2
    with Solver(name=args.solver, bootstrap_with=clauses) as solver:
        if args.basepair_core:
            all_selectors = list(selectors.values())
            if args.sample_basepair is not None:
                if args.shared_a is None or args.shared_b is None:
                    raise SystemExit("sampling requires --shared-a and --shared-b")
                sample_pair = tuple(int(value) for value in args.sample_basepair.split(","))
                if len(sample_pair) != 2 or sample_pair not in selectors:
                    raise SystemExit("bad sample base pair")
                chosen_selector = selectors[sample_pair]
                assumptions = [
                    literal if literal == chosen_selector else -literal
                    for literal in all_selectors
                ]
                if args.classify_shared_block is not None:
                    block = tuple(int(value) for value in args.classify_shared_block.split(","))
                    if len(block) != 3:
                        raise SystemExit("shared block format is left-base,left-fibre,right-base")
                    left_base, left_fibre, right_base = block
                    feasible_permutations = []
                    for permutation_index, permutation in enumerate(itertools.permutations(range(k))):
                        selector = next_variable + permutation_index
                        for right_fibre in range(k):
                            solver.add_clause(
                                [
                                    -selector,
                                    cell(
                                        left_base,
                                        left_fibre,
                                        right_base,
                                        right_fibre,
                                        permutation[right_fibre],
                                    ),
                                ]
                            )
                        if solver.solve(assumptions=[*assumptions, selector]):
                            feasible_permutations.append(permutation)
                    print(
                        f"sample-pair={sample_pair}; shared-block={block}; "
                        f"feasible={len(feasible_permutations)}"
                    )
                    print("permutations=" + "/".join("".join(map(str, value)) for value in feasible_permutations))
                    return 0
                if args.classify_incoming_signs:
                    fibre_permutations = list(itertools.permutations(range(k)))
                    sign_selectors = list(range(next_variable, next_variable + 2 ** k))
                    for profile, sign_selector in enumerate(sign_selectors):
                        for left_fibre in range(k):
                            required = (profile >> left_fibre) & 1
                            for permutation in fibre_permutations:
                                if permutation_parity(list(permutation)) == required:
                                    continue
                                solver.add_clause(
                                    [
                                        -sign_selector,
                                        *[
                                            -cell(
                                                args.shared_b,
                                                left_fibre,
                                                args.shared_a,
                                                right_fibre,
                                                permutation[right_fibre],
                                            )
                                            for right_fibre in range(k)
                                        ],
                                    ]
                                )
                    feasible = []
                    for profile, sign_selector in enumerate(sign_selectors):
                        sign_assumptions = [
                            literal if literal == sign_selector else -literal
                            for literal in sign_selectors
                        ]
                        if solver.solve(assumptions=[*assumptions, *sign_assumptions]):
                            feasible.append(tuple((profile >> index) & 1 for index in range(k)))
                    print(f"sample-pair={sample_pair}; exact-incoming-sign-profiles={feasible}")
                    return 0
                if args.force_incoming_signs is not None:
                    bits = [int(value) for value in args.force_incoming_signs]
                    if len(bits) != k or any(value not in (0, 1) for value in bits):
                        raise SystemExit("forced incoming signs must be a 0/1 word of fibre length")
                    for left_fibre, required in enumerate(bits):
                        for permutation in itertools.permutations(range(k)):
                            if permutation_parity(list(permutation)) == required:
                                continue
                            solver.add_clause(
                                [
                                    -cell(
                                        args.shared_b,
                                        left_fibre,
                                        args.shared_a,
                                        right_fibre,
                                        permutation[right_fibre],
                                    )
                                    for right_fibre in range(k)
                                ]
                            )
                aggregates: Counter[tuple[int, int, int]] = Counter()
                row_profiles: Counter[tuple[int, ...]] = Counter()
                column_profiles: Counter[tuple[int, ...]] = Counter()
                incoming_profiles: Counter[tuple[int, ...]] = Counter()
                sampled = 0
                while sampled < args.sample_models and solver.solve(assumptions=assumptions):
                    model = {literal for literal in solver.get_model() if literal > 0}
                    shared_literals = []
                    row_parities = []
                    column_parities = [0] * m
                    for left_fibre in range(k):
                        row_parity = 0
                        for right_base in range(m):
                            permutation = []
                            for right_fibre in range(k):
                                values = [
                                    value
                                    for value in range(k)
                                    if cell(args.shared_a, left_fibre, right_base, right_fibre, value) in model
                                ]
                                if len(values) != 1:
                                    raise RuntimeError("bad sampled shared permutation")
                                permutation.append(values[0])
                                shared_literals.append(
                                    cell(args.shared_a, left_fibre, right_base, right_fibre, values[0])
                                )
                            parity = permutation_parity(permutation)
                            row_parity ^= parity
                            column_parities[right_base] ^= parity
                        row_parities.append(row_parity)
                    incoming = []
                    for left_fibre in range(k):
                        permutation = []
                        for right_fibre in range(k):
                            values = [
                                value
                                for value in range(k)
                                if cell(args.shared_b, left_fibre, args.shared_a, right_fibre, value) in model
                            ]
                            if len(values) != 1:
                                raise RuntimeError("bad sampled incoming permutation")
                            permutation.append(values[0])
                            shared_literals.append(
                                cell(args.shared_b, left_fibre, args.shared_a, right_fibre, values[0])
                            )
                        incoming.append(permutation_parity(permutation))
                    row_total = sum(row_parities) % 2
                    incoming_total = sum(incoming) % 2
                    aggregates[row_total, incoming_total, row_total ^ incoming_total] += 1
                    row_profiles[tuple(row_parities)] += 1
                    column_profiles[tuple(column_parities)] += 1
                    incoming_profiles[tuple(incoming)] += 1
                    solver.add_clause([-literal for literal in shared_literals])
                    sampled += 1
                print(f"sample-pair={sample_pair}; projections={sampled}")
                print(f"aggregate-signs={dict(aggregates)}")
                print(f"row-sign-profiles={dict(row_profiles)}")
                print(f"column-sign-profiles={dict(column_profiles)}")
                print(f"incoming-sign-profiles={dict(incoming_profiles)}")
                return 0
            if solver.solve(assumptions=all_selectors):
                print("SAT: all base pairs are compatible")
                return 0
            core = list(dict.fromkeys(literal for literal in solver.get_core() or [] if literal > 0))
            print(f"initial-core={len(core)}", flush=True)
            for candidate in list(core):
                trial = [literal for literal in core if literal != candidate]
                trial_set = set(trial)
                assumptions = [literal if literal in trial_set else -literal for literal in all_selectors]
                if not solver.solve(assumptions=assumptions):
                    core = trial
            inverse_selectors = {literal: pair for pair, literal in selectors.items()}
            print(f"minimal-core={len(core)}")
            for literal in core:
                print(f"pair={inverse_selectors[literal]}")
            return 2
        # A verified fibre E677 table gives a coherent deterministic phase,
        # even though the skew base action need not satisfy E677 initially.
        phase_source = load_table(ROOT / "cache" / "eq677-db" / str(k) / "0")
        if len(phase_source) == k:
            phases = []
            for left_base in range(m):
                for left_fibre in range(k):
                    for right_base in range(m):
                        for right_fibre in range(k):
                            chosen = phase_source[left_fibre][right_fibre]
                            for value in range(k):
                                literal = cell(left_base, left_fibre, right_base, right_fibre, value)
                                phases.append(literal if value == chosen else -literal)
            solver.set_phases(phases)
        timer = threading.Timer(args.seconds, solver.interrupt)
        timer.start()
        try:
            result = solver.solve_limited(expect_interrupt=True)
        finally:
            timer.cancel()
        if result is None:
            print(f"UNKNOWN ({time.time()-started:.3f}s)")
            return 3
        if result is False:
            print(f"UNSAT ({time.time()-started:.3f}s)")
            return 2
        model = {literal for literal in solver.get_model() if literal > 0}

    table = [[0] * order for _ in range(order)]
    for left_base in range(m):
        for left_fibre in range(k):
            left = k * left_base + left_fibre
            for right_base in range(m):
                output_base = out_base(left_base, left_fibre, right_base)
                for right_fibre in range(k):
                    values = [
                        value
                        for value in range(k)
                        if cell(left_base, left_fibre, right_base, right_fibre, value) in model
                    ]
                    if len(values) != 1:
                        raise RuntimeError("bad decoded skew cell")
                    right = k * right_base + right_fibre
                    table[left][right] = k * output_base + values[0]
    verify_e677(table)
    bad = bad_points(table)
    target = k * x_base + x_fibre
    if not args.allow_good and target not in bad:
        raise RuntimeError("decoded target is not Bad")
    status = "VERIFIED E677 MODEL" if args.allow_good else "VERIFIED COUNTEREXAMPLE"
    print(f"{status}: bad={bad}; elapsed={time.time()-started:.3f}s")
    for row in table:
        print(" ".join(map(str, row)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
