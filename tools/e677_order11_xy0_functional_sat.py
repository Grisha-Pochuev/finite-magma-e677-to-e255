"""Exact necessary functional system for a normalized Bad zero at order 11.

This is deliberately much smaller than the full magma-table formula.  It
contains only the maps

    s(t) = 0*t,  f(y) = y*0,  g(y) = L_y^{-1}(0),  R = f o s

and exact consequences of E677 plus row injectivity.  SAT is only a
functional seed, never a magma counterexample; UNSAT would exclude the
chosen normalized value f(2).
"""

from __future__ import annotations

import argparse
import itertools
import random
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def exactly_one(clauses: list[list[int]], literals: list[int]) -> None:
    clauses.append(literals)
    for left, right in itertools.combinations(literals, 2):
        clauses.append([-left, -right])


class Variables:
    def __init__(self, order: int) -> None:
        self.order = order
        self.next_variable = 1
        self.s = self._matrix()
        self.f = self._matrix()
        self.g = self._matrix()

    def _matrix(self) -> list[list[int]]:
        matrix = []
        for _ in range(self.order):
            row = list(range(self.next_variable, self.next_variable + self.order))
            self.next_variable += self.order
            matrix.append(row)
        return matrix


def build_formula(order: int, f2: int) -> tuple[Variables, list[list[int]]]:
    if order != 11:
        raise RuntimeError("the normalization is specialized to order 11")
    variables = Variables(order)
    s, f, g = variables.s, variables.f, variables.g
    clauses: list[list[int]] = []

    # s is a permutation; f and g are total functions.
    for matrix in (s, f, g):
        for row in matrix:
            exactly_one(clauses, row)
    for value in range(order):
        exactly_one(clauses, [s[source][value] for source in range(order)])

    # Bad-zero normalization and immediate nonzero facts.
    clauses.extend([[s[0][1]], [f[0][1]], [f[1][2]], [f[2][f2]]])
    for y in range(order):
        clauses.extend([[-f[y][0]], [-g[y][0]]])

    # E677 at x=y=0: s(s(f(s(0))))=0, hence s(s(2))=0.
    for middle in range(order):
        clauses.append([-s[2][middle], s[middle][0]])

    # Y0-COUPLING plus row injectivity: s(f(x)) != x.
    for x in range(order):
        for value in range(order):
            clauses.append([-f[x][value], -s[value][x]])

    # X0-COLLISION for y != 0: g(y) != s(f(f(y))).
    for y in range(1, order):
        for first in range(order):
            for second in range(order):
                for target in range(order):
                    clauses.append(
                        [-f[y][first], -f[first][second], -s[second][target], -g[y][target]]
                    )

    # The two X0 cells determine y, so y -> (f(y),g(y)) is injective.
    for y, z in itertools.combinations(range(order), 2):
        for left in range(order):
            for right in range(order):
                clauses.append([-f[y][left], -f[z][left], -g[y][right], -g[z][right]])

    # The genuine single XY0-CROSS equivalence:
    #     g(y)=f(y)  iff  y=R(f(y)),  R=f o s.
    for y in range(order):
        for value in range(order):
            for shifted in range(order):
                clauses.append([-f[y][value], -g[y][value], -s[value][shifted], f[shifted][y]])
                clauses.append([-f[y][value], -s[value][shifted], -f[shifted][y], g[y][value]])

    # Exact distinguished values: g(0)=s^{-1}(0), g(1)=R(1).
    for source in range(order):
        clauses.extend(([-g[0][source], s[source][0]], [-s[source][0], g[0][source]]))
    for shifted in range(order):
        for value in range(order):
            clauses.append([-s[1][shifted], -f[shifted][value], g[1][value]])

    return variables, clauses


def decode(row: list[int], model: set[int]) -> int:
    values = [value for value, literal in enumerate(row) if literal in model]
    if len(values) != 1:
        raise RuntimeError(f"bad one-hot row: {values}")
    return values[0]


def cycle_type(permutation: list[int]) -> tuple[int, ...]:
    seen: set[int] = set()
    lengths: list[int] = []
    for start in range(len(permutation)):
        if start in seen:
            continue
        current = start
        length = 0
        while current not in seen:
            seen.add(current)
            length += 1
            current = permutation[current]
        lengths.append(length)
    return tuple(sorted(lengths, reverse=True))


def fibre_profile(function: list[int]) -> tuple[int, ...]:
    return tuple(sorted(Counter(function).values(), reverse=True))


def audit(s: list[int], f: list[int], g: list[int], f2: int) -> list[int]:
    n = len(s)
    if sorted(s) != list(range(n)):
        raise RuntimeError("s is not a permutation")
    if (s[0], f[0], f[1], f[2]) != (1, 1, 2, f2):
        raise RuntimeError("normalization failed")
    if 0 in f or 0 in g:
        raise RuntimeError("nonzero range failed")
    if s[s[2]] != 0:
        raise RuntimeError("row-cycle law failed")
    if any(s[f[x]] == x for x in range(n)):
        raise RuntimeError("Y0 collision failed")
    if len(set(zip(f, g))) != n:
        raise RuntimeError("(f,g) injectivity failed")
    if any(g[y] == s[f[f[y]]] for y in range(1, n)):
        raise RuntimeError("X0 collision failed")
    r = [f[s[x]] for x in range(n)]
    if any((g[y] == f[y]) != (r[f[y]] == y) for y in range(n)):
        raise RuntimeError("XY0 cross equivalence failed")
    inverse_s = [0] * n
    for source, value in enumerate(s):
        inverse_s[value] = source
    if g[0] != inverse_s[0] or g[1] != r[1]:
        raise RuntimeError("distinguished g values failed")
    return r


def complete_g(s: list[int], f: list[int]) -> list[int] | None:
    """Complete g exactly once s,f are fixed, by tiny bipartite matchings."""
    n = len(s)
    inverse_s = [0] * n
    for source, value in enumerate(s):
        inverse_s[value] = source
    r = [f[s[x]] for x in range(n)]
    allowed: list[list[int]] = []
    for y in range(n):
        values = set(range(1, n))
        if r[f[y]] == y:
            values &= {f[y]}
        else:
            values.discard(f[y])
        if y:
            values.discard(s[f[f[y]]])
        if y == 0:
            values &= {inverse_s[0]}
        if y == 1:
            values &= {r[1]}
        if not values:
            return None
        allowed.append(sorted(values))

    g = [-1] * n
    groups: dict[int, list[int]] = {}
    for y, value in enumerate(f):
        groups.setdefault(value, []).append(y)

    for group in groups.values():
        ordered = sorted(group, key=lambda y: len(allowed[y]))

        def match(index: int, used: set[int]) -> bool:
            if index == len(ordered):
                return True
            y = ordered[index]
            for value in allowed[y]:
                if value in used:
                    continue
                g[y] = value
                used.add(value)
                if match(index + 1, used):
                    return True
                used.remove(value)
                g[y] = -1
            return False

        if not match(0, set()):
            return None
    return g


def construct_case(order: int, f2: int, trials: int, seed: int) -> str:
    rng = random.Random(seed + f2)
    for trial in range(1, trials + 1):
        # s(0)=1 and s(s(2))=0.  Its intermediate value cannot be 0,1,2.
        middle = rng.randrange(3, order)
        s = [-1] * order
        s[0], s[2], s[middle] = 1, middle, 0
        sources = [x for x in range(order) if s[x] < 0]
        targets = [x for x in range(order) if x not in (0, 1, middle)]
        rng.shuffle(targets)
        for source, target in zip(sources, targets):
            s[source] = target

        inverse_s = [0] * order
        for source, value in enumerate(s):
            inverse_s[value] = source
        f = [-1] * order
        f[0], f[1], f[2] = 1, 2, f2
        if any(f[x] == inverse_s[x] for x in range(3)):
            continue
        for x in range(3, order):
            choices = [value for value in range(1, order) if value != inverse_s[x]]
            f[x] = rng.choice(choices)

        g = complete_g(s, f)
        if g is None:
            continue
        r = audit(s, f, g, f2)
        return "\n".join(
            (
                f"f(2)={f2}: SAT functional seed (not a magma), trial={trial}",
                f"  s={','.join(map(str, s))}; cycles={cycle_type(s)}",
                f"  f={','.join(map(str, f))}; fibres={fibre_profile(f)}",
                f"  g={','.join(map(str, g))}; fibres={fibre_profile(g)}",
                f"  R={','.join(map(str, r))}; fibres={fibre_profile(r)}",
            )
        )
    return f"f(2)={f2}: UNKNOWN after {trials} constructive trials"


def format_sat_model(variables: Variables, model: set[int], f2: int) -> str:
    """Retained decoder for independently solving build_formula's CNF."""
    s = [decode(row, model) for row in variables.s]
    f = [decode(row, model) for row in variables.f]
    g = [decode(row, model) for row in variables.g]
    r = audit(s, f, g, f2)
    return "\n".join(
        (
            f"f(2)={f2}: SAT functional seed (not a magma)",
            f"  s={','.join(map(str, s))}; cycles={cycle_type(s)}",
            f"  f={','.join(map(str, f))}; fibres={fibre_profile(f)}",
            f"  g={','.join(map(str, g))}; fibres={fibre_profile(g)}",
            f"  R={','.join(map(str, r))}; fibres={fibre_profile(r)}",
        )
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--order", type=int, default=11)
    parser.add_argument("--f2", type=int, choices=(1, 2, 3))
    parser.add_argument("--trials", type=int, default=100000)
    parser.add_argument("--seed", type=int, default=677255)
    args = parser.parse_args()

    cases = (args.f2,) if args.f2 is not None else (1, 2, 3)
    for case in cases:
        print(construct_case(args.order, case, args.trials, args.seed), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
