#!/usr/bin/env python3
"""Measure memory use of a process tree once per second."""

from __future__ import annotations

import argparse
import csv
import json
import os
from pathlib import Path
import time
from typing import Any


def read_key_values(path: Path) -> dict[str, str]:
    result: dict[str, str] = {}
    try:
        for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
            if ":" in line:
                key, value = line.split(":", 1)
                result[key] = value.strip()
    except (FileNotFoundError, PermissionError, ProcessLookupError):
        pass
    return result


def int_kb(value: str | None) -> int:
    if not value:
        return 0
    try:
        return int(value.split()[0])
    except (ValueError, IndexError):
        return 0


def process_snapshot() -> dict[int, dict[str, Any]]:
    processes: dict[int, dict[str, Any]] = {}
    for entry in Path("/proc").iterdir():
        if not entry.name.isdigit():
            continue
        pid = int(entry.name)
        status = read_key_values(entry / "status")
        if not status:
            continue
        try:
            ppid = int(status.get("PPid", "0"))
        except ValueError:
            ppid = 0
        smaps = read_key_values(entry / "smaps_rollup")
        processes[pid] = {
            "pid": pid,
            "ppid": ppid,
            "name": status.get("Name", "?"),
            "rss_kb": int_kb(status.get("VmRSS")),
            "swap_kb": int_kb(status.get("VmSwap")),
            "pss_kb": int_kb(smaps.get("Pss")),
        }
    return processes


def meminfo() -> dict[str, int]:
    values = read_key_values(Path("/proc/meminfo"))
    return {
        "mem_available_kb": int_kb(values.get("MemAvailable")),
        "swap_free_kb": int_kb(values.get("SwapFree")),
    }


def pressure_values() -> dict[str, float]:
    values = {"pressure_some_avg10": 0.0, "pressure_full_avg10": 0.0}
    try:
        lines = Path("/proc/pressure/memory").read_text(encoding="utf-8").splitlines()
    except (FileNotFoundError, PermissionError):
        return values
    for line in lines:
        parts = line.split()
        if not parts:
            continue
        prefix = parts[0]
        fields = dict(item.split("=", 1) for item in parts[1:] if "=" in item)
        try:
            values[f"pressure_{prefix}_avg10"] = float(fields.get("avg10", "0"))
        except ValueError:
            pass
    return values


def cgroup_v2_path() -> Path | None:
    try:
        for line in Path("/proc/self/cgroup").read_text(encoding="utf-8").splitlines():
            fields = line.split(":", 2)
            if len(fields) == 3 and fields[0] == "0":
                return Path("/sys/fs/cgroup") / fields[2].lstrip("/")
    except (FileNotFoundError, PermissionError):
        pass
    return None


def read_int_file(path: Path) -> int:
    try:
        text = path.read_text(encoding="utf-8").strip()
        return int(text) if text != "max" else -1
    except (FileNotFoundError, PermissionError, ValueError):
        return 0


def read_cgroup(group: Path | None) -> dict[str, Any]:
    if group is None:
        return {
            "cgroup_memory_current_bytes": 0,
            "cgroup_memory_peak_bytes": 0,
            "cgroup_swap_current_bytes": 0,
            "cgroup_events": {},
        }
    events: dict[str, int] = {}
    try:
        for line in (group / "memory.events").read_text(encoding="utf-8").splitlines():
            key, value = line.split()
            events[key] = int(value)
    except (FileNotFoundError, PermissionError, ValueError):
        pass
    return {
        "cgroup_memory_current_bytes": read_int_file(group / "memory.current"),
        "cgroup_memory_peak_bytes": read_int_file(group / "memory.peak"),
        "cgroup_swap_current_bytes": read_int_file(group / "memory.swap.current"),
        "cgroup_events": events,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root_pid", type=int)
    parser.add_argument("csv_path", type=Path)
    parser.add_argument("summary_path", type=Path)
    parser.add_argument("--interval", type=float, default=1.0)
    args = parser.parse_args()

    args.csv_path.parent.mkdir(parents=True, exist_ok=True)
    tracked: set[int] = {args.root_pid}
    start = time.monotonic()
    empty_rounds = 0
    group = cgroup_v2_path()

    maxima = {
        "max_process_count": 0,
        "max_tree_rss_kb": 0,
        "max_tree_pss_kb": 0,
        "max_tree_swap_kb": 0,
        "min_mem_available_kb": 2**63 - 1,
        "min_swap_free_kb": 2**63 - 1,
        "max_pressure_some_avg10": 0.0,
        "max_pressure_full_avg10": 0.0,
        "max_cgroup_memory_current_bytes": 0,
        "max_cgroup_memory_peak_bytes": 0,
        "max_cgroup_swap_current_bytes": 0,
    }
    final_events: dict[str, int] = {}

    columns = [
        "elapsed_s",
        "process_count",
        "tree_rss_kb",
        "tree_pss_kb",
        "tree_swap_kb",
        "mem_available_kb",
        "swap_free_kb",
        "pressure_some_avg10",
        "pressure_full_avg10",
        "cgroup_memory_current_bytes",
        "cgroup_memory_peak_bytes",
        "cgroup_swap_current_bytes",
        "pids",
    ]

    with args.csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns)
        writer.writeheader()

        while True:
            snapshot = process_snapshot()
            changed = True
            while changed:
                changed = False
                for pid, info in snapshot.items():
                    if pid not in tracked and info["ppid"] in tracked:
                        tracked.add(pid)
                        changed = True

            live = sorted(pid for pid in tracked if pid in snapshot)
            if live:
                empty_rounds = 0
            else:
                empty_rounds += 1

            tree_rss = sum(snapshot[pid]["rss_kb"] for pid in live)
            tree_pss = sum(snapshot[pid]["pss_kb"] for pid in live)
            tree_swap = sum(snapshot[pid]["swap_kb"] for pid in live)
            system = meminfo()
            pressure = pressure_values()
            cgroup = read_cgroup(group)
            final_events = cgroup["cgroup_events"]

            row = {
                "elapsed_s": round(time.monotonic() - start, 3),
                "process_count": len(live),
                "tree_rss_kb": tree_rss,
                "tree_pss_kb": tree_pss,
                "tree_swap_kb": tree_swap,
                **system,
                **pressure,
                "cgroup_memory_current_bytes": cgroup["cgroup_memory_current_bytes"],
                "cgroup_memory_peak_bytes": cgroup["cgroup_memory_peak_bytes"],
                "cgroup_swap_current_bytes": cgroup["cgroup_swap_current_bytes"],
                "pids": ";".join(str(pid) for pid in live),
            }
            writer.writerow(row)
            handle.flush()

            maxima["max_process_count"] = max(maxima["max_process_count"], len(live))
            maxima["max_tree_rss_kb"] = max(maxima["max_tree_rss_kb"], tree_rss)
            maxima["max_tree_pss_kb"] = max(maxima["max_tree_pss_kb"], tree_pss)
            maxima["max_tree_swap_kb"] = max(maxima["max_tree_swap_kb"], tree_swap)
            maxima["min_mem_available_kb"] = min(maxima["min_mem_available_kb"], system["mem_available_kb"])
            maxima["min_swap_free_kb"] = min(maxima["min_swap_free_kb"], system["swap_free_kb"])
            maxima["max_pressure_some_avg10"] = max(maxima["max_pressure_some_avg10"], pressure["pressure_some_avg10"])
            maxima["max_pressure_full_avg10"] = max(maxima["max_pressure_full_avg10"], pressure["pressure_full_avg10"])
            maxima["max_cgroup_memory_current_bytes"] = max(maxima["max_cgroup_memory_current_bytes"], cgroup["cgroup_memory_current_bytes"])
            maxima["max_cgroup_memory_peak_bytes"] = max(maxima["max_cgroup_memory_peak_bytes"], cgroup["cgroup_memory_peak_bytes"])
            maxima["max_cgroup_swap_current_bytes"] = max(maxima["max_cgroup_swap_current_bytes"], cgroup["cgroup_swap_current_bytes"])

            if empty_rounds >= 3:
                break
            time.sleep(max(args.interval, 0.1))

    for key in ("min_mem_available_kb", "min_swap_free_kb"):
        if maxima[key] == 2**63 - 1:
            maxima[key] = 0

    summary = {
        "root_pid": args.root_pid,
        "duration_s": round(time.monotonic() - start, 3),
        "cgroup_path": str(group) if group else None,
        "memory_events": final_events,
        **maxima,
    }
    args.summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
