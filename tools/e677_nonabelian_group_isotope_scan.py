"""Exact scan of a new nonabelian one-constant isotope layer.

For a finite group G, let A and B range over automorphisms and automorphisms
composed with inversion.  The scan checks all operations with at most one
inserted group constant:

    c A(x) B(y),   A(x) c B(y),   A(x) B(y) c.

Every complete table is checked directly against E677 and E255.  Counts are
presentation counts; the identity-constant presentation is scanned once.
"""

from __future__ import annotations

import argparse
import math
import time
from dataclasses import dataclass


@dataclass(frozen=True)
class Group:
    name: str
    multiplication: tuple[tuple[int, ...], ...]
    inverse: tuple[int, ...]
    automorphisms: tuple[tuple[int, ...], ...]

    @property
    def order(self) -> int:
        return len(self.multiplication)


def verify_group(group: Group) -> None:
    n = group.order
    product = group.multiplication
    if any(len(row) != n for row in product):
        raise RuntimeError(f"{group.name}: malformed multiplication table")
    if any(product[0][x] != x or product[x][0] != x for x in range(n)):
        raise RuntimeError(f"{group.name}: zero is not the identity")
    if any(product[x][group.inverse[x]] != 0 or product[group.inverse[x]][x] != 0 for x in range(n)):
        raise RuntimeError(f"{group.name}: bad inverse map")
    if any(product[product[x][y]][z] != product[x][product[y][z]] for x in range(n) for y in range(n) for z in range(n)):
        raise RuntimeError(f"{group.name}: multiplication is not associative")
    for mapping in group.automorphisms:
        if sorted(mapping) != list(range(n)):
            raise RuntimeError(f"{group.name}: nonpermutation automorphism")
        if any(mapping[product[x][y]] != product[mapping[x]][mapping[y]] for x in range(n) for y in range(n)):
            raise RuntimeError(f"{group.name}: invalid automorphism")


def compose(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(left[right[x]] for x in range(len(left)))


def unique_maps(maps: list[tuple[int, ...]]) -> tuple[tuple[int, ...], ...]:
    return tuple(dict.fromkeys(maps))


def dihedral_group(rotation_order: int) -> Group:
    m = rotation_order

    def index(rotation: int, reflection: int) -> int:
        return 2 * (rotation % m) + reflection

    multiplication = []
    for left in range(2 * m):
        i, j = divmod(left, 2)
        row = []
        for right in range(2 * m):
            k, ell = divmod(right, 2)
            row.append(index(i + (-1 if j else 1) * k, (j + ell) % 2))
        multiplication.append(tuple(row))
    inverse = []
    for value in range(2 * m):
        inverse.append(next(x for x in range(2 * m) if multiplication[value][x] == 0))

    automorphisms = []
    for scale in range(m):
        if math.gcd(scale, m) != 1:
            continue
        for shift in range(m):
            automorphisms.append(
                tuple(
                    index(scale * rotation + shift * reflection, reflection)
                    for rotation in range(m)
                    for reflection in range(2)
                )
            )
    return Group(
        name=f"D_{2*m}",
        multiplication=tuple(multiplication),
        inverse=tuple(inverse),
        automorphisms=unique_maps(automorphisms),
    )


def quaternion_group() -> Group:
    # Values are +1,-1,+i,-i,+j,-j,+k,-k.
    basis_product = (
        ((1, 0), (1, 1), (1, 2), (1, 3)),
        ((1, 1), (-1, 0), (1, 3), (-1, 2)),
        ((1, 2), (-1, 3), (-1, 0), (1, 1)),
        ((1, 3), (1, 2), (-1, 1), (-1, 0)),
    )

    def encode(sign: int, basis: int) -> int:
        return 2 * basis + (0 if sign == 1 else 1)

    multiplication = []
    for left in range(8):
        left_basis, left_negative = divmod(left, 2)
        row = []
        for right in range(8):
            right_basis, right_negative = divmod(right, 2)
            sign, basis = basis_product[left_basis][right_basis]
            if left_negative:
                sign = -sign
            if right_negative:
                sign = -sign
            row.append(encode(sign, basis))
        multiplication.append(tuple(row))
    inverse = tuple(next(x for x in range(8) if multiplication[value][x] == 0) for value in range(8))

    automorphisms = []
    order_four = (2, 3, 4, 5, 6, 7)
    for image_i in order_four:
        for image_j in order_four:
            if image_i in (image_j, inverse[image_j]):
                continue
            image_k = multiplication[image_i][image_j]
            mapping = [0, 1, image_i, inverse[image_i], image_j, inverse[image_j], image_k, inverse[image_k]]
            candidate = tuple(mapping)
            if all(
                candidate[multiplication[x][y]] == multiplication[candidate[x]][candidate[y]]
                for x in range(8)
                for y in range(8)
            ):
                automorphisms.append(candidate)
    return Group("Q_8", tuple(multiplication), inverse, unique_maps(automorphisms))


def signed_maps(group: Group) -> tuple[tuple[int, ...], ...]:
    inversion = group.inverse
    return unique_maps(
        [mapping for automorphism in group.automorphisms for mapping in (automorphism, compose(automorphism, inversion))]
    )


def make_table(
    group: Group,
    left_map: tuple[int, ...],
    right_map: tuple[int, ...],
    constant: int,
    position: int,
) -> list[list[int]]:
    product = group.multiplication
    table: list[list[int]] = []
    for x in range(group.order):
        row = []
        for y in range(group.order):
            a, b = left_map[x], right_map[y]
            if position == 0:
                value = product[product[constant][a]][b]
            elif position == 1:
                value = product[product[a][constant]][b]
            else:
                value = product[product[a][b]][constant]
            row.append(value)
        table.append(row)
    return table


def make_full_translation_table(
    group: Group,
    left_map: tuple[int, ...],
    right_map: tuple[int, ...],
    prefix: int,
    middle: int,
    suffix: int,
) -> list[list[int]]:
    """Return p A(x) q B(y) r, the full signed principal-isotope layer."""
    product = group.multiplication
    left_values = [product[product[prefix][left_map[x]]][middle] for x in range(group.order)]
    right_values = [product[right_map[y]][suffix] for y in range(group.order)]
    return [[product[left_values[x]][right_values[y]] for y in range(group.order)] for x in range(group.order)]


def satisfies_e677(table: list[list[int]]) -> bool:
    n = len(table)
    for x in range(n):
        for y in range(n):
            if table[y][table[x][table[table[y][x]][y]]] != x:
                return False
    return True


def bad_points(table: list[list[int]]) -> list[int]:
    return [x for x in range(len(table)) if table[table[table[x][x]][x]][x] != x]


def verify_table(table: list[list[int]]) -> None:
    n = len(table)
    if any(sorted(row) != list(range(n)) for row in table):
        raise RuntimeError("a left row is not a permutation")
    if not satisfies_e677(table):
        raise RuntimeError("reported table fails E677")


def scan_group(group: Group) -> tuple[int, int, list[list[int]] | None, tuple[int, int, int, int] | None]:
    maps = signed_maps(group)
    checked = 0
    good_models = 0
    for left_index, left_map in enumerate(maps):
        for right_index, right_map in enumerate(maps):
            for constant in range(group.order):
                positions = (1,) if constant == 0 else (0, 1, 2)
                for position in positions:
                    checked += 1
                    table = make_table(group, left_map, right_map, constant, position)
                    if not satisfies_e677(table):
                        continue
                    bad = bad_points(table)
                    if bad:
                        verify_table(table)
                        return checked, good_models, table, (left_index, right_index, constant, position)
                    good_models += 1
    return checked, good_models, None, None


def scan_full_translation_group(
    group: Group,
) -> tuple[int, int, list[list[int]] | None, tuple[int, int, int, int, int] | None]:
    maps = signed_maps(group)
    checked = 0
    good_models = 0
    for left_index, left_map in enumerate(maps):
        for right_index, right_map in enumerate(maps):
            for prefix in range(group.order):
                for middle in range(group.order):
                    for suffix in range(group.order):
                        checked += 1
                        table = make_full_translation_table(
                            group, left_map, right_map, prefix, middle, suffix
                        )
                        if not satisfies_e677(table):
                            continue
                        bad = bad_points(table)
                        if bad:
                            verify_table(table)
                            return (
                                checked,
                                good_models,
                                table,
                                (left_index, right_index, prefix, middle, suffix),
                            )
                        good_models += 1
    return checked, good_models, None, None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-dihedral-rotation", type=int, default=12)
    parser.add_argument("--full-translations", action="store_true")
    parser.add_argument("--min-full-order", type=int, default=0)
    parser.add_argument("--max-full-order", type=int, default=8)
    args = parser.parse_args()
    if args.max_dihedral_rotation < 3:
        raise SystemExit("maximum dihedral rotation order must be at least 3")

    groups = [dihedral_group(m) for m in range(3, args.max_dihedral_rotation + 1)]
    groups.append(quaternion_group())
    groups = [
        group
        for group in groups
        if not args.full_translations
        or args.min_full_order <= group.order <= args.max_full_order
    ]
    for group in groups:
        verify_group(group)
    total_checked = 0
    total_good = 0
    started = time.time()
    for group in groups:
        if args.full_translations:
            checked, good, table, parameters = scan_full_translation_group(group)
        else:
            checked, good, table, parameters = scan_group(group)
        total_checked += checked
        total_good += good
        print(
            f"{group.name}: order={group.order}; automorphisms={len(group.automorphisms)}; "
            f"signed-maps={len(signed_maps(group))}; presentations={checked}; "
            f"E677-good={good}; counterexample={'yes' if table is not None else 'no'}",
            flush=True,
        )
        if table is not None:
            bad = bad_points(table)
            print(f"VERIFIED COUNTEREXAMPLE: group={group.name}; parameters={parameters}; bad={bad}")
            for row in table:
                print(" ".join(map(str, row)))
            return 0
    print(
        f"COMPLETE: presentations={total_checked}; E677-good={total_good}; "
        f"counterexamples=0; elapsed={time.time()-started:.3f}s"
    )
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
