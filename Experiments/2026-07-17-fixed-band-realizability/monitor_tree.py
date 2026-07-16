#!/usr/bin/env python3
import argparse
import csv
import json
import os
import signal
import subprocess
import sys
import time
from pathlib import Path


def proc_snapshot():
    parents = {}
    rss_kib = {}
    for name in os.listdir('/proc'):
        if not name.isdigit():
            continue
        pid = int(name)
        try:
            with open(f'/proc/{pid}/stat', 'r', encoding='utf-8') as fh:
                fields = fh.read().split()
            parents[pid] = int(fields[3])
            with open(f'/proc/{pid}/status', 'r', encoding='utf-8') as fh:
                for line in fh:
                    if line.startswith('VmRSS:'):
                        rss_kib[pid] = int(line.split()[1])
                        break
        except (FileNotFoundError, ProcessLookupError, PermissionError, ValueError, IndexError):
            continue
    return parents, rss_kib


def descendants(root, parents):
    keep = {root}
    changed = True
    while changed:
        changed = False
        for pid, ppid in parents.items():
            if ppid in keep and pid not in keep:
                keep.add(pid)
                changed = True
    return keep


def meminfo():
    values = {}
    with open('/proc/meminfo', 'r', encoding='utf-8') as fh:
        for line in fh:
            key, rest = line.split(':', 1)
            values[key] = int(rest.strip().split()[0])
    return values


def terminate_group(proc, grace=20):
    try:
        os.killpg(proc.pid, signal.SIGTERM)
    except ProcessLookupError:
        return
    deadline = time.monotonic() + grace
    while time.monotonic() < deadline:
        if proc.poll() is not None:
            return
        time.sleep(0.5)
    try:
        os.killpg(proc.pid, signal.SIGKILL)
    except ProcessLookupError:
        pass


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--limit-seconds', type=int, required=True)
    parser.add_argument('--rss-limit-mib', type=int, default=12288)
    parser.add_argument('--memavailable-min-mib', type=int, default=2560)
    parser.add_argument('--samples-before-stop', type=int, default=3)
    parser.add_argument('--interval', type=float, default=2.0)
    parser.add_argument('--out-dir', required=True)
    parser.add_argument('command', nargs=argparse.REMAINDER)
    args = parser.parse_args()
    if not args.command or args.command[0] != '--':
        parser.error('command must follow --')
    command = args.command[1:]
    out = Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)
    (out / 'command.txt').write_text(' '.join(command) + '\n', encoding='utf-8')

    log_path = out / 'solver.log'
    rows = []
    started = time.monotonic()
    reason = 'process_exit'
    guarded = 0
    peak_rss = 0
    min_available = None
    max_swap = 0

    with log_path.open('wb') as log:
        proc = subprocess.Popen(command, stdout=log, stderr=subprocess.STDOUT, start_new_session=True)
        while proc.poll() is None:
            elapsed = time.monotonic() - started
            parents, rss = proc_snapshot()
            tree = descendants(proc.pid, parents)
            tree_rss = sum(rss.get(pid, 0) for pid in tree)
            mi = meminfo()
            available = mi.get('MemAvailable', 0)
            swap_used = mi.get('SwapTotal', 0) - mi.get('SwapFree', 0)
            peak_rss = max(peak_rss, tree_rss)
            min_available = available if min_available is None else min(min_available, available)
            max_swap = max(max_swap, swap_used)
            rows.append([round(elapsed, 3), len(tree), tree_rss, available, swap_used])

            over = tree_rss >= args.rss_limit_mib * 1024 or available <= args.memavailable_min_mib * 1024
            guarded = guarded + 1 if over else 0
            if elapsed >= args.limit_seconds:
                reason = 'time_limit'
                terminate_group(proc)
                break
            if guarded >= args.samples_before_stop:
                reason = 'memory_guard'
                terminate_group(proc)
                break
            time.sleep(args.interval)

        raw_code = proc.wait()

    with (out / 'resources.csv').open('w', newline='', encoding='utf-8') as fh:
        writer = csv.writer(fh)
        writer.writerow(['elapsed_seconds', 'process_count', 'tree_rss_kib', 'mem_available_kib', 'swap_used_kib'])
        writer.writerows(rows)

    if reason == 'time_limit':
        public_code = 124
    elif reason == 'memory_guard':
        public_code = 125
    else:
        public_code = raw_code

    summary = {
        'reason': reason,
        'raw_exit_code': raw_code,
        'exit_code': public_code,
        'elapsed_seconds': round(time.monotonic() - started, 3),
        'peak_tree_rss_mib': round(peak_rss / 1024, 3),
        'min_mem_available_mib': round((min_available or 0) / 1024, 3),
        'max_swap_used_mib': round(max_swap / 1024, 3),
    }
    (out / 'resource-summary.json').write_text(json.dumps(summary, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(summary, indent=2))
    return public_code


if __name__ == '__main__':
    sys.exit(main())
