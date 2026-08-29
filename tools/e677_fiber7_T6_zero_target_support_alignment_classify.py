"""Classify the exact s=0 support-alignment core of tuple 6.

For z(t)=O7_t^-1(0), q(t)=O7_t(0), and

    rho(t) = D(q(t)-t) - A(q(t)),

the zero-target kernel requires ker(z)=ker(rho).  The cyclic Q
transversals also require t -> t+z(t) to be a permutation, while Badness
requires z(t),q(t) != 0.  This script eliminates q and rho block by block.
It is a finite classifier of that necessary core, not a model finder for
the complete E677 table.
"""

from __future__ import annotations

import itertools
import time
from collections import Counter, defaultdict


N = 7
CANONICAL_D = tuple(
    tuple(map(int, text))
    for text in ("0125634", "0145236", "1023546", "1024356")
)


def profile(partition):
    return tuple(sorted((mask.bit_count() for mask in partition), reverse=True))


def displacement_partitions():
    """Return realizable unlabeled z-kernel partitions and their counts."""
    counts = Counter()
    for phi in itertools.permutations(range(N)):
        if any(phi[t] == t for t in range(N)):
            continue
        z = tuple((phi[t] - t) % N for t in range(N))
        blocks = defaultdict(int)
        for t, value in enumerate(z):
            blocks[value] |= 1 << t
        if len(blocks) not in (3, 4, 5):
            continue
        partition = tuple(sorted(blocks.values()))
        counts[partition] += 1
    return counts


def normalized_A():
    """Canonical-D gauge retains A(0)=0, but not A(1)=1."""
    for tail in itertools.permutations(range(1, N)):
        yield (0, *tail)


def block_options(D, A, mask, support):
    """Map rho value to attainable support-hit masks for one z-block."""
    points = tuple(t for t in range(N) if mask & (1 << t))
    result = {}
    for rho in range(N):
        allowed = {}
        for t in points:
            choices = []
            for q in range(1, N):
                x = (q - t) % N
                if (D[x] - A[q]) % N == rho:
                    choices.append((q, x in support))
            if not choices:
                break
            allowed[t] = choices
        else:
            hit_masks = set()

            def visit(index, used_q, hit_mask):
                if index == len(points):
                    hit_masks.add(hit_mask)
                    return
                t = points[index]
                for q, hit in allowed[t]:
                    if used_q & (1 << q):
                        continue
                    visit(
                        index + 1,
                        used_q | (1 << q),
                        hit_mask | ((1 << t) if hit else 0),
                    )

            visit(0, 0, 0)
            if hit_masks:
                result[rho] = hit_masks
    return result


def partition_support_counts(partition, options):
    """Choose distinct rho labels for blocks and return attainable |E|."""
    states = {(0, 0)}  # (used rho values, global support-hit mask)
    for mask in partition:
        updated = set()
        for used_rho, global_hits in states:
            for rho, hit_masks in options[mask].items():
                if used_rho & (1 << rho):
                    continue
                for hit_mask in hit_masks:
                    updated.add((used_rho | (1 << rho), global_hits | hit_mask))
        states = updated
        if not states:
            break
    return {hit_mask.bit_count() for _, hit_mask in states}


def main():
    started = time.time()
    partition_counts = displacement_partitions()
    partitions = tuple(partition_counts)
    masks = tuple(sorted({mask for part in partitions for mask in part}))
    by_profile = Counter(profile(part) for part in partitions)
    print(
        f"derangements=1854; partitions={len(partitions)}; masks={len(masks)}; "
        f"profiles={dict(sorted(by_profile.items()))}",
        flush=True,
    )

    feasible_partitions = [set() for _ in CANONICAL_D]
    support_counts = [set() for _ in CANONICAL_D]
    feasible_A = [0 for _ in CANONICAL_D]
    profile_hits = [defaultdict(set) for _ in CANONICAL_D]

    for D_index, D in enumerate(CANONICAL_D):
        support = {x for x in range(N) if D[x] != x}
        for A in normalized_A():
            options = {
                mask: block_options(D, A, mask, support) for mask in masks
            }
            A_works = False
            for partition in partitions:
                counts = partition_support_counts(partition, options)
                if not counts:
                    continue
                A_works = True
                feasible_partitions[D_index].add(partition)
                support_counts[D_index].update(counts)
                profile_hits[D_index][profile(partition)].update(counts)
            feasible_A[D_index] += A_works
        print(
            f"D={''.join(map(str, D))}; feasible-A={feasible_A[D_index]}/720; "
            f"feasible-partitions={len(feasible_partitions[D_index])}/{len(partitions)}; "
            f"support-counts={sorted(support_counts[D_index])}",
            flush=True,
        )
        for key in sorted(profile_hits[D_index]):
            print(
                f"  profile={key}; support-counts="
                f"{sorted(profile_hits[D_index][key])}",
                flush=True,
            )

    print(
        "ZERO-TARGET SUPPORT ALIGNMENT COMPLETE; "
        f"elapsed={time.time()-started:.3f}s"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
