#!/usr/bin/env bash
set -uo pipefail

SLOT="${1:?slot}"
PROFILE="${2:?profile}"
KIND="${3:?kind: vampire or e}"
CORES="${4:?cores}"
MEM_MB="${5:?memory per worker in MB}"
INTENT="${6:?intent: unsat, sat or n/a}"
REPEAT="${7:?repeat}"

DIAG_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(cd "$DIAG_DIR/../../.." && pwd)"
OUT="$ROOT/run-output/runner-diagnostics/slot-$SLOT"
PROBLEM="$ROOT/Experiments/2026-07-11-fixed-eta/problem.p"
BIN_DIR="$ROOT/prover-bin"
mkdir -p "$OUT"

STARTED_EPOCH="$(date +%s)"
STARTED_UTC="$(date -u +%Y-%m-%dT%H:%M:%SZ)"

{
  echo "slot=$SLOT"
  echo "profile=$PROFILE"
  echo "kind=$KIND"
  echo "cores=$CORES"
  echo "memory_per_worker_mb=$MEM_MB"
  echo "intent=$INTENT"
  echo "repeat=$REPEAT"
  echo "started_utc=$STARTED_UTC"
  echo "commit=${GITHUB_SHA:-unknown}"
  echo "runner_name=${RUNNER_NAME:-unknown}"
  echo "runner_os=${RUNNER_OS:-unknown}"
  echo "runner_arch=${RUNNER_ARCH:-unknown}"
  echo "image_os=${ImageOS:-unknown}"
  echo "image_version=${ImageVersion:-unknown}"
} > "$OUT/metadata.txt"

{
  echo "# uname"
  uname -a || true
  echo
  echo "# lscpu"
  lscpu || true
  echo
  echo "# lscpu json"
  lscpu -J || true
  echo
  echo "# cpuinfo"
  cat /proc/cpuinfo || true
  echo
  echo "# memory"
  free -b || true
  cat /proc/meminfo || true
  echo
  echo "# swap"
  swapon --show --bytes || true
  echo
  echo "# cgroup"
  cat /proc/self/cgroup || true
  mount | grep -E 'cgroup|overlay' || true
  for file in memory.max memory.current memory.peak memory.swap.max memory.swap.current memory.events; do
    find /sys/fs/cgroup -path "*/$file" -maxdepth 8 -print -exec cat {} \; 2>/dev/null | head -80 || true
  done
  echo
  echo "# pressure"
  cat /proc/pressure/memory 2>/dev/null || true
  cat /proc/pressure/cpu 2>/dev/null || true
  echo
  echo "# storage"
  df -hT || true
  lsblk -o NAME,TYPE,SIZE,ROTA,MODEL,MOUNTPOINTS || true
  echo
  echo "# limits"
  ulimit -a || true
  echo
  echo "# selected kernel settings"
  sysctl vm.overcommit_memory vm.overcommit_ratio vm.swappiness 2>/dev/null || true
  echo
  echo "# DMI"
  for file in /sys/class/dmi/id/sys_vendor /sys/class/dmi/id/product_name /sys/class/dmi/id/product_version /sys/class/dmi/id/board_vendor /sys/class/dmi/id/board_name; do
    printf '%s=' "$file"
    cat "$file" 2>/dev/null || true
  done
} > "$OUT/hardware.txt" 2>&1

# A compact memory-bandwidth measurement. It is deliberately much smaller
# than the solver workload and runs before the prover starts.
BENCH_BIN="$OUT/stream_bench"
if gcc -O3 -fopenmp -std=c11 "$DIAG_DIR/stream_bench.c" -o "$BENCH_BIN" > "$OUT/stream-build.log" 2>&1; then
  "$BENCH_BIN" 1 > "$OUT/memory-bandwidth-1-thread.json" 2> "$OUT/memory-bandwidth-1-thread.err" || true
  "$BENCH_BIN" 4 > "$OUT/memory-bandwidth-4-thread.json" 2> "$OUT/memory-bandwidth-4-thread.err" || true
else
  echo "memory benchmark build failed" >> "$OUT/metadata.txt"
fi
rm -f "$BENCH_BIN"

LOG="$OUT/solver.log"
MONITOR_CSV="$OUT/process-tree-memory.csv"
MONITOR_JSON="$OUT/process-tree-summary.json"

CMD=()
if [[ "$KIND" == "vampire" ]]; then
  CMD=("$BIN_DIR/vampire" --mode casc --cores "$CORES" -m "$MEM_MB" -t 90 --proof tptp)
  if [[ "$INTENT" == "sat" ]]; then
    CMD+=(--intent sat)
  fi
  CMD+=("$PROBLEM")
elif [[ "$KIND" == "e" ]]; then
  CMD=("$BIN_DIR/eprover" "--auto-schedule=$CORES" --cpu-limit=90 "--memory-limit=$MEM_MB" --proof-object --tstp-format "$PROBLEM")
else
  echo "unknown kind: $KIND" > "$LOG"
fi

printf 'command=' >> "$OUT/metadata.txt"
printf '%q ' "${CMD[@]}" >> "$OUT/metadata.txt"
printf '\n' >> "$OUT/metadata.txt"

SOLVER_STATUS=127
if [[ ${#CMD[@]} -eq 0 ]]; then
  echo "no command constructed" >> "$LOG"
elif [[ ! -x "${CMD[0]}" ]]; then
  echo "missing executable: ${CMD[0]}" >> "$LOG"
elif [[ ! -f "$PROBLEM" ]]; then
  echo "missing problem: $PROBLEM" >> "$LOG"
else
  set +e
  timeout --signal=TERM --kill-after=15s 105s "${CMD[@]}" > "$LOG" 2>&1 &
  ROOT_PID=$!
  python3 "$DIAG_DIR/monitor_tree.py" "$ROOT_PID" "$MONITOR_CSV" "$MONITOR_JSON" --interval 1.0 > "$OUT/monitor.log" 2>&1 &
  MONITOR_PID=$!
  wait "$ROOT_PID"
  SOLVER_STATUS=$?
  wait "$MONITOR_PID" || true
  set -e
fi

FINISHED_EPOCH="$(date +%s)"
FINISHED_UTC="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
ELAPSED_SECONDS=$((FINISHED_EPOCH - STARTED_EPOCH))

CLASSIFICATION="technical-error"
if grep -Eqi 'SZS status (Theorem|Unsatisfiable|Satisfiable|CounterSatisfiable)|Refutation found|Proof found' "$LOG" 2>/dev/null; then
  CLASSIFICATION="mathematical-result"
elif grep -Eqi 'SZS status (Timeout|GaveUp)|time limit|ResourceOut' "$LOG" 2>/dev/null; then
  CLASSIFICATION="expected-short-limit"
elif grep -Eqi 'memory limit|Insufficient system memory|out of memory' "$LOG" 2>/dev/null; then
  CLASSIFICATION="solver-memory-limit"
elif [[ "$SOLVER_STATUS" -eq 124 ]]; then
  CLASSIFICATION="wrapper-timeout"
elif [[ "$SOLVER_STATUS" -eq 137 ]]; then
  CLASSIFICATION="killed-137"
elif [[ "$SOLVER_STATUS" -eq 143 ]]; then
  CLASSIFICATION="killed-143"
elif [[ "$SOLVER_STATUS" -eq 0 ]]; then
  CLASSIFICATION="completed-zero"
elif grep -Eqi 'unknown option|bad option|user error|invalid.*option|missing executable|missing problem|unknown kind' "$LOG" 2>/dev/null; then
  CLASSIFICATION="configuration-error"
fi

{
  echo "exit_status=$SOLVER_STATUS"
  echo "classification=$CLASSIFICATION"
  echo "elapsed_seconds=$ELAPSED_SECONDS"
  echo "finished_utc=$FINISHED_UTC"
} >> "$OUT/metadata.txt"

# Kernel messages are useful if the host recorded an OOM kill. GitHub may
# deny access; that denial is preserved rather than hidden.
{
  sudo dmesg --ctime 2>&1 | tail -250
} > "$OUT/dmesg-tail.txt" || true

python3 - "$OUT" "$SLOT" "$PROFILE" "$KIND" "$CORES" "$MEM_MB" "$INTENT" "$REPEAT" "$SOLVER_STATUS" "$CLASSIFICATION" "$ELAPSED_SECONDS" <<'PY'
from __future__ import annotations

import json
from pathlib import Path
import re
import sys

(
    out_text,
    slot,
    profile,
    kind,
    cores,
    mem_mb,
    intent,
    repeat,
    exit_status,
    classification,
    elapsed_seconds,
) = sys.argv[1:]
out = Path(out_text)


def read_json(name: str) -> dict:
    try:
        return json.loads((out / name).read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError, OSError):
        return {}


def first_cpu_value(label: str) -> str:
    try:
        text = Path("/proc/cpuinfo").read_text(encoding="utf-8", errors="replace")
    except OSError:
        return "unknown"
    match = re.search(rf"^{re.escape(label)}\s*:\s*(.+)$", text, flags=re.MULTILINE)
    return match.group(1).strip() if match else "unknown"


def mem_total_kb() -> int:
    try:
        text = Path("/proc/meminfo").read_text(encoding="utf-8")
    except OSError:
        return 0
    match = re.search(r"^MemTotal:\s+(\d+)\s+kB", text, flags=re.MULTILINE)
    return int(match.group(1)) if match else 0


def swap_total_kb() -> int:
    try:
        text = Path("/proc/meminfo").read_text(encoding="utf-8")
    except OSError:
        return 0
    match = re.search(r"^SwapTotal:\s+(\d+)\s+kB", text, flags=re.MULTILINE)
    return int(match.group(1)) if match else 0


monitor = read_json("process-tree-summary.json")
bandwidth_1 = read_json("memory-bandwidth-1-thread.json")
bandwidth_4 = read_json("memory-bandwidth-4-thread.json")
result = {
    "slot": slot,
    "profile": profile,
    "kind": kind,
    "cores": int(cores),
    "memory_per_worker_mb": int(mem_mb),
    "theoretical_worker_budget_mb": int(cores) * int(mem_mb),
    "intent": intent,
    "repeat": int(repeat),
    "exit_status": int(exit_status),
    "classification": classification,
    "elapsed_seconds": int(elapsed_seconds),
    "cpu_vendor": first_cpu_value("vendor_id"),
    "cpu_model": first_cpu_value("model name"),
    "cpu_family": first_cpu_value("cpu family"),
    "cpu_model_number": first_cpu_value("model"),
    "cpu_stepping": first_cpu_value("stepping"),
    "reported_cpu_mhz": first_cpu_value("cpu MHz"),
    "logical_cpus": int(first_cpu_value("siblings")) if first_cpu_value("siblings").isdigit() else 0,
    "mem_total_kb": mem_total_kb(),
    "swap_total_kb": swap_total_kb(),
    "memory_bandwidth_1_thread": bandwidth_1,
    "memory_bandwidth_4_thread": bandwidth_4,
    "monitor": monitor,
}
(out / "result.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")

summary_lines = [
    f"slot={slot}",
    f"profile={profile}",
    f"cpu_vendor={result['cpu_vendor']}",
    f"cpu_model={result['cpu_model']}",
    f"mem_total_gib={result['mem_total_kb'] / 1024 / 1024:.3f}",
    f"swap_total_gib={result['swap_total_kb'] / 1024 / 1024:.3f}",
    f"bandwidth_1_thread_gbps={bandwidth_1.get('median_gbps', 0)}",
    f"bandwidth_4_thread_gbps={bandwidth_4.get('median_gbps', 0)}",
    f"max_process_count={monitor.get('max_process_count', 0)}",
    f"max_tree_rss_gib={monitor.get('max_tree_rss_kb', 0) / 1024 / 1024:.3f}",
    f"max_tree_pss_gib={monitor.get('max_tree_pss_kb', 0) / 1024 / 1024:.3f}",
    f"max_tree_swap_gib={monitor.get('max_tree_swap_kb', 0) / 1024 / 1024:.3f}",
    f"min_mem_available_gib={monitor.get('min_mem_available_kb', 0) / 1024 / 1024:.3f}",
    f"memory_events={json.dumps(monitor.get('memory_events', {}), sort_keys=True)}",
    f"exit_status={exit_status}",
    f"classification={classification}",
    f"elapsed_seconds={elapsed_seconds}",
]
(out / "summary.txt").write_text("\n".join(summary_lines) + "\n", encoding="utf-8")
print("\n".join(summary_lines))
PY

# A short log excerpt is printed in the Actions page. Full data remains in the artifact.
echo "----- solver tail -----"
tail -80 "$LOG" 2>/dev/null || true

case "$CLASSIFICATION" in
  mathematical-result|expected-short-limit|wrapper-timeout|solver-memory-limit|completed-zero)
    exit 0
    ;;
  *)
    exit 1
    ;;
esac
