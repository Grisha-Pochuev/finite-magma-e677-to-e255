"use strict";

function permutations(n) {
  const out = [];
  const used = Array(n).fill(false);
  const cur = [];
  function rec() {
    if (cur.length === n) {
      const p = cur.slice();
      const inv = Array(n);
      for (let i = 0; i < n; i++) inv[p[i]] = i;
      out.push({ p, inv, label: p.join(" ") });
      return;
    }
    for (let i = 0; i < n; i++) {
      if (!used[i]) {
        used[i] = true;
        cur.push(i);
        rec();
        cur.pop();
        used[i] = false;
      }
    }
  }
  rec();
  return out;
}

function cyclePerm(n, cycles) {
  const p = Array.from({ length: n }, (_, i) => i);
  for (const cycle of cycles) {
    for (let i = 0; i < cycle.length; i++) p[cycle[i]] = cycle[(i + 1) % cycle.length];
  }
  const inv = Array(n);
  for (let i = 0; i < n; i++) inv[p[i]] = i;
  return { p, inv, label: p.join(" ") };
}

function partitions(n, maxPart = n) {
  if (n === 0) return [[]];
  const out = [];
  for (let first = Math.min(n, maxPart); first >= 1; first--) {
    for (const rest of partitions(n - first, first)) out.push([first, ...rest]);
  }
  return out;
}

function row0Representatives(n) {
  const reps = [];
  for (let zeroCycleLength = 2; zeroCycleLength <= n; zeroCycleLength++) {
    for (const tailPartition of partitions(n - zeroCycleLength)) {
      const cycles = [Array.from({ length: zeroCycleLength }, (_, i) => i)];
      let next = zeroCycleLength;
      for (const length of tailPartition) {
        const cycle = Array.from({ length }, (_, i) => next + i);
        next += length;
        if (cycle.length > 1) cycles.push(cycle);
      }
      reps.push(cyclePerm(n, cycles));
    }
  }
  return reps;
}

function cycleType(p) {
  const seen = Array(p.length).fill(false);
  const parts = [];
  for (let i = 0; i < p.length; i++) {
    if (seen[i]) continue;
    let cur = i;
    let len = 0;
    while (!seen[cur]) {
      seen[cur] = true;
      len++;
      cur = p[cur];
    }
    parts.push(len);
  }
  return parts.sort((a, b) => b - a).join("+");
}

function cloneState(state) {
  return {
    domains: state.domains.map((domain) => domain.slice()),
    assigned: state.assigned.slice(),
  };
}

function formatTable(state) {
  return state.assigned.map((row) => row.label).join("\n");
}

function satisfiesE677(state, n) {
  for (let x = 0; x < n; x++) {
    for (let y = 0; y < n; y++) {
      const px = state.assigned[x];
      const py = state.assigned[y];
      const targetRow = py.p[x];
      const lhs = state.assigned[targetRow].p[y];
      const rhs = px.inv[py.inv[x]];
      if (lhs !== rhs) return false;
    }
  }
  return true;
}

function satisfiesE255(state, n) {
  for (let x = 0; x < n; x++) {
    const rhs = state.assigned[state.assigned[state.assigned[x].p[x]].p[x]].p[x];
    if (rhs !== x) return false;
  }
  return true;
}

function makeSearch(n, row0Index, maxSeconds) {
  const allPerms = permutations(n);
  const row0Reps = row0Representatives(n);
  const row0 = row0Reps[row0Index];
  const start = Date.now();
  const maxMs = maxSeconds * 1000;
  const stats = {
    nodes: 0,
    domainCuts: 0,
    imposed: 0,
    contradictions: 0,
    forcedRows: 0,
  };

  function timedOut() {
    return Date.now() - start > maxMs;
  }

  function initialDomain(row) {
    if (row === 0) return [row0];
    const forbidden = row0.inv[row];
    return allPerms.filter((candidate) => {
      if (candidate.p[0] === 0) return false; // no y*0=0
      if (candidate.p[0] === forbidden) return false; // no R_0 L_0 fixed point
      if (candidate.p[row] === forbidden) return false; // no L_0 S fixed point
      return true;
    });
  }

  function cutDomain(state, row, predicate) {
    const old = state.domains[row];
    const next = [];
    for (const candidate of old) {
      if (predicate(candidate)) next.push(candidate);
    }
    if (next.length === old.length) return true;
    stats.domainCuts += old.length - next.length;
    if (next.length === 0) {
      stats.contradictions++;
      return false;
    }
    state.domains[row] = next;
    if (state.assigned[row] && !predicate(state.assigned[row])) {
      stats.contradictions++;
      return false;
    }
    return true;
  }

  function impose(state, row, col, value) {
    stats.imposed++;
    if (col === 0 && value === 0) return false;
    return cutDomain(state, row, (candidate) => candidate.p[col] === value);
  }

  function assignSingletons(state) {
    let changed = false;
    for (let row = 0; row < n; row++) {
      if (!state.assigned[row] && state.domains[row].length === 1) {
        state.assigned[row] = state.domains[row][0];
        stats.forcedRows++;
        changed = true;
      }
    }
    return changed;
  }

  function propagate(state) {
    let changed = true;
    while (changed) {
      changed = assignSingletons(state);
      const beforeCuts = stats.domainCuts;

      const usedRows = new Set();
      for (let row = 0; row < n; row++) {
        const assigned = state.assigned[row];
        if (!assigned) continue;
        if (usedRows.has(assigned.label)) return false;
        usedRows.add(assigned.label);
      }
      for (let row = 0; row < n; row++) {
        if (state.assigned[row]) continue;
        if (
          !cutDomain(
            state,
            row,
            (candidate) => !usedRows.has(candidate.label)
          )
        ) {
          return false;
        }
      }

      for (let x = 0; x < n; x++) {
        const px = state.assigned[x];
        if (!px) continue;
        for (let y = 0; y < n; y++) {
          const py = state.assigned[y];
          if (!py) continue;

          const targetRow = py.p[x];
          const targetValue = px.inv[py.inv[x]];
          if (!impose(state, targetRow, y, targetValue)) return false;
        }
      }

      for (let x = 0; x < n; x++) {
        for (let y = 0; y < n; y++) {
          const py = state.assigned[y];
          if (!py) continue;
          const a = py.p[x];
          const pa = state.assigned[a];
          if (!pa) continue;
          const b = py.p[a];
          const targetValue = pa.inv[x];
          if (!impose(state, b, y, targetValue)) return false;
        }
      }

      changed = changed || stats.domainCuts !== beforeCuts;
    }
    return true;
  }

  function chooseRow(state) {
    let best = -1;
    let bestSize = Infinity;
    for (let row = 0; row < n; row++) {
      if (state.assigned[row]) continue;
      const size = state.domains[row].length;
      if (size < bestSize) {
        best = row;
        bestSize = size;
      }
    }
    return best;
  }

  function rec(state, depth) {
    if (timedOut()) return { status: "timeout" };
    stats.nodes++;
    if (!propagate(state)) return { status: "none" };

    const row = chooseRow(state);
    if (row === -1) {
      if (satisfiesE677(state, n) && !satisfiesE255(state, n)) {
        return { status: "found", table: formatTable(state) };
      }
      return { status: "none" };
    }

    const domain = state.domains[row];
    if (depth <= 1) console.log(`depth ${depth}: row ${row}, ${domain.length} candidates`);

    for (const candidate of domain) {
      const next = cloneState(state);
      next.domains[row] = [candidate];
      next.assigned[row] = candidate;
      const result = rec(next, depth + 1);
      if (result.status !== "none") return result;
    }
    return { status: "none" };
  }

  function run() {
    const state = {
      domains: Array.from({ length: n }, (_, row) => initialDomain(row)),
      assigned: Array(n).fill(null),
    };
    const result = rec(state, 0);
    result.ms = Date.now() - start;
    result.stats = stats;
    result.row0 = row0;
    result.row0Count = row0Reps.length;
    return result;
  }

  return { run, row0, row0Count: row0Reps.length };
}

const n = Number(process.argv[2] || 8);
const maxSeconds = Number(process.argv[3] || 60);
const row0Index = Number(process.argv[4] || 18);
const search = makeSearch(n, row0Index, maxSeconds);

console.log(`Domain search for E677 counterexample to E255, size ${n}.`);
console.log(`row-0 case ${row0Index + 1}/${search.row0Count}: ${search.row0.label}`);
console.log(`row-0 cycle type: ${cycleType(search.row0.p)}`);
const result = search.run();
console.log(`status: ${result.status}`);
console.log(`time: ${(result.ms / 1000).toFixed(2)}s`);
console.log(`nodes: ${result.stats.nodes}`);
console.log(`domain cuts: ${result.stats.domainCuts}`);
console.log(`imposed cells: ${result.stats.imposed}`);
console.log(`forced rows: ${result.stats.forcedRows}`);
console.log(`contradictions: ${result.stats.contradictions}`);
if (result.table) {
  console.log("counterexample table:");
  console.log(result.table);
}
