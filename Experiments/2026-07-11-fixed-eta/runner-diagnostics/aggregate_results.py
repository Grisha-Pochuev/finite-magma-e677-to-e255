#!/usr/bin/env python3
"""Combine all per-runner diagnostic JSON files into CSV and Markdown."""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import csv
import json
from pathlib import Path
import statistics
from typing import Any, Iterable


def nested(data: dict[str, Any], *keys: str, default: Any = 0) -> Any:
    current: Any = data
    for key in keys:
        if not isinstance(current, dict) or key not in current:
            return default
        current = current[key]
    return current


def median(values: Iterable[float]) -> float:
    clean = [float(value) for value in values if value is not None]
    return statistics.median(clean) if clean else 0.0


def gib_from_kb(value: Any) -> float:
    try:
        return float(value) / 1024.0 / 1024.0
    except (TypeError, ValueError):
        return 0.0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_dir", type=Path)
    parser.add_argument("output_dir", type=Path)
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)

    results: list[dict[str, Any]] = []
    for path in sorted(args.input_dir.rglob("result.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            print(f"skip {path}: {exc}")
            continue
        data["artifact_result_path"] = str(path.relative_to(args.input_dir))
        results.append(data)

    if not results:
        (args.output_dir / "SUMMARY.md").write_text(
            "# Diagnostic summary\n\nNo valid `result.json` files were found.\n",
            encoding="utf-8",
        )
        return 1

    rows: list[dict[str, Any]] = []
    for item in results:
        monitor = item.get("monitor", {})
        one = item.get("memory_bandwidth_1_thread", {})
        four = item.get("memory_bandwidth_4_thread", {})
        rows.append({
            "slot": item.get("slot"),
            "profile": item.get("profile"),
            "repeat": item.get("repeat"),
            "kind": item.get("kind"),
            "intent": item.get("intent"),
            "cores": item.get("cores"),
            "memory_per_worker_mb": item.get("memory_per_worker_mb"),
            "theoretical_worker_budget_mb": item.get("theoretical_worker_budget_mb"),
            "cpu_vendor": item.get("cpu_vendor"),
            "cpu_model": item.get("cpu_model"),
            "reported_cpu_mhz": item.get("reported_cpu_mhz"),
            "mem_total_gib": round(gib_from_kb(item.get("mem_total_kb")), 4),
            "swap_total_gib": round(gib_from_kb(item.get("swap_total_kb")), 4),
            "bandwidth_1_thread_median_gbps": one.get("median_gbps", 0),
            "bandwidth_4_thread_median_gbps": four.get("median_gbps", 0),
            "bandwidth_scaling_4_to_1": round(
                float(four.get("median_gbps", 0)) / float(one.get("median_gbps", 1) or 1), 4
            ),
            "max_process_count": monitor.get("max_process_count", 0),
            "max_tree_rss_gib": round(gib_from_kb(monitor.get("max_tree_rss_kb")), 4),
            "max_tree_pss_gib": round(gib_from_kb(monitor.get("max_tree_pss_kb")), 4),
            "max_tree_swap_gib": round(gib_from_kb(monitor.get("max_tree_swap_kb")), 4),
            "min_mem_available_gib": round(gib_from_kb(monitor.get("min_mem_available_kb")), 4),
            "max_pressure_some_avg10": monitor.get("max_pressure_some_avg10", 0),
            "max_pressure_full_avg10": monitor.get("max_pressure_full_avg10", 0),
            "oom_events": nested(monitor, "memory_events", "oom", default=0),
            "oom_kill_events": nested(monitor, "memory_events", "oom_kill", default=0),
            "exit_status": item.get("exit_status"),
            "classification": item.get("classification"),
            "elapsed_seconds": item.get("elapsed_seconds"),
            "artifact_result_path": item.get("artifact_result_path"),
        })

    machine_fields = list(rows[0].keys())
    with (args.output_dir / "machines.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=machine_fields)
        writer.writeheader()
        writer.writerows(rows)

    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        grouped[str(row["profile"])].append(row)

    profile_rows: list[dict[str, Any]] = []
    for profile, group in sorted(grouped.items()):
        classifications = Counter(str(row["classification"]) for row in group)
        profile_rows.append({
            "profile": profile,
            "samples": len(group),
            "cores": group[0]["cores"],
            "memory_per_worker_mb": group[0]["memory_per_worker_mb"],
            "median_bandwidth_1_thread_gbps": round(median(row["bandwidth_1_thread_median_gbps"] for row in group), 4),
            "median_bandwidth_4_thread_gbps": round(median(row["bandwidth_4_thread_median_gbps"] for row in group), 4),
            "median_bandwidth_scaling_4_to_1": round(median(row["bandwidth_scaling_4_to_1"] for row in group), 4),
            "median_max_tree_rss_gib": round(median(row["max_tree_rss_gib"] for row in group), 4),
            "median_max_tree_pss_gib": round(median(row["max_tree_pss_gib"] for row in group), 4),
            "largest_tree_rss_gib": round(max(float(row["max_tree_rss_gib"]) for row in group), 4),
            "lowest_mem_available_gib": round(min(float(row["min_mem_available_gib"]) for row in group), 4),
            "largest_tree_swap_gib": round(max(float(row["max_tree_swap_gib"]) for row in group), 4),
            "oom_kill_events": sum(int(row["oom_kill_events"] or 0) for row in group),
            "classifications": "; ".join(f"{key}={value}" for key, value in sorted(classifications.items())),
        })

    profile_fields = list(profile_rows[0].keys())
    with (args.output_dir / "profile-summary.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=profile_fields)
        writer.writeheader()
        writer.writerows(profile_rows)

    cpu_counts = Counter(f"{row['cpu_vendor']} | {row['cpu_model']}" for row in rows)
    classification_counts = Counter(str(row["classification"]) for row in rows)
    total_oom_kills = sum(int(row["oom_kill_events"] or 0) for row in rows)

    lines = [
        "# GitHub runner diagnostic summary",
        "",
        f"Valid samples: **{len(rows)}**.",
        "",
        "## Machines received",
        "",
    ]
    for model, count in cpu_counts.most_common():
        lines.append(f"- `{count}` × `{model}`")

    lines.extend(["", "## Completion classes", ""])
    for name, count in sorted(classification_counts.items()):
        lines.append(f"- `{name}`: `{count}`")
    lines.append(f"- cgroup OOM-kill events across samples: `{total_oom_kills}`")

    lines.extend([
        "",
        "## Profile comparison",
        "",
        "| Profile | n | Cores | MB/worker | Median tree RSS GiB | Largest tree RSS GiB | Lowest available GiB | Max swap GiB | Classes |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---|",
    ])
    for row in profile_rows:
        lines.append(
            f"| `{row['profile']}` | {row['samples']} | {row['cores']} | {row['memory_per_worker_mb']} | "
            f"{row['median_max_tree_rss_gib']:.3f} | {row['largest_tree_rss_gib']:.3f} | "
            f"{row['lowest_mem_available_gib']:.3f} | {row['largest_tree_swap_gib']:.3f} | {row['classifications']} |"
        )

    lines.extend([
        "",
        "## Memory bandwidth by machine",
        "",
        "See `machines.csv` for all per-runner measurements and `profile-summary.csv` for grouped values.",
        "",
        "This automatically generated file is evidence only. The final interpretation and recommended limits belong in the repository `RESULTS.md` after manual review.",
    ])
    (args.output_dir / "SUMMARY.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
