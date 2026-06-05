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
      out.push({ p, inv });
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
  for (const c of cycles) {
    for (let i = 0; i < c.length; i++) {
      p[c[i]] = c[(i + 1) % c.length];
    }
  }
  const inv = Array(n);
  for (let i = 0; i < n; i++) inv[p[i]] = i;
  return { p, inv };
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

function cloneReq(req) {
  return req.map((row) => row.slice());
}

function impose(req, assign, row, col, value, stats) {
  const old = req[row][col];
  if (old !== -1) return old === value;
  if (col === 0 && value === 0) return false;

  for (let c = 0; c < req.length; c++) {
    if (c !== col && req[row][c] === value) return false;
  }

  const assigned = assign[row];
  if (assigned && assigned.p[col] !== value) return false;

  req[row][col] = value;
  stats.imposed++;
  return true;
}

function propagate(req, assign, n, stats) {
  let changed = true;
  while (changed) {
    const before = stats.imposed;

    for (let row = 0; row < n; row++) {
      const assigned = assign[row];
      if (!assigned) continue;
      for (let col = 0; col < n; col++) {
        const value = req[row][col];
        if (value !== -1 && assigned.p[col] !== value) return false;
      }
    }

    for (let x = 0; x < n; x++) {
      const rowX = assign[x];
      if (!rowX) continue;
      for (let y = 0; y < n; y++) {
        const rowY = assign[y];
        if (!rowY) continue;

        const targetRow = rowY.p[x];
        const targetValue = rowX.inv[rowY.inv[x]];
        if (!impose(req, assign, targetRow, y, targetValue, stats)) {
          return false;
        }
      }
    }

    changed = stats.imposed !== before;
  }
  return true;
}

function fitsRequirements(value, reqRow) {
  for (let col = 0; col < reqRow.length; col++) {
    const required = reqRow[col];
    if (required !== -1 && value.p[col] !== required) return false;
  }
  return true;
}

function satisfiesE677(assign, n) {
  for (let x = 0; x < n; x++) {
    for (let y = 0; y < n; y++) {
      const targetRow = assign[y].p[x];
      const lhs = assign[targetRow].p[y];
      const rhs = assign[x].inv[assign[y].inv[x]];
      if (lhs !== rhs) return false;
    }
  }
  return true;
}

function formatTable(assign) {
  return assign.map((row) => row.p.join(" ")).join("\n");
}

function search(n, maxMs) {
  const start = Date.now();
  const bad = 0;
  const allValues = permutations(n).filter((v) => v.p[bad] !== bad);
  const row0Values = row0Representatives(n);
  const assign = Array(n).fill(null);
  const req = Array.from({ length: n }, () => Array(n).fill(-1));
  const stats = {
    nodes: 0,
    imposed: 0,
    deadEnds: 0,
    candidateChecks: 0,
  };

  function timedOut() {
    return Date.now() - start > maxMs;
  }

  function domainFor(reqState, variable) {
    const base = variable === bad ? row0Values : allValues;
    const out = [];
    const reqRow = reqState[variable];
    for (const value of base) {
      stats.candidateChecks++;
      if (fitsRequirements(value, reqRow)) out.push(value);
    }
    return out;
  }

  function rec(reqState, depth) {
    if (timedOut()) return { status: "timeout" };
    stats.nodes++;

    let bestVar = -1;
    let bestDomain = null;

    for (let row = 0; row < n; row++) {
      if (assign[row]) continue;
      const domain = domainFor(reqState, row);
      if (domain.length === 0) {
        stats.deadEnds++;
        return { status: "none" };
      }
      if (!bestDomain || domain.length < bestDomain.length) {
        bestVar = row;
        bestDomain = domain;
      }
    }

    if (bestVar === -1) {
      if (satisfiesE677(assign, n)) {
        return { status: "found", table: formatTable(assign) };
      }
      stats.deadEnds++;
      return { status: "none" };
    }

    if (depth <= 1) {
      console.log(`depth ${depth}: row ${bestVar}, ${bestDomain.length} candidates`);
    }

    for (const value of bestDomain) {
      assign[bestVar] = value;
      const nextReq = cloneReq(reqState);
      if (propagate(nextReq, assign, n, stats)) {
        const result = rec(nextReq, depth + 1);
        if (result.status !== "none") return result;
      } else {
        stats.deadEnds++;
      }
      assign[bestVar] = null;
    }

    return { status: "none" };
  }

  const initialReq = cloneReq(req);
  const result = rec(initialReq, 0);
  result.ms = Date.now() - start;
  result.stats = stats;
  return result;
}

const n = Number(process.argv[2] || 8);
const maxSeconds = Number(process.argv[3] || 60);
console.log(`Propagating search for E677 counterexample to E255, size ${n}.`);
console.log("Bad element is normalized to 0; row 0 is symmetry-reduced.");
const result = search(n, maxSeconds * 1000);
console.log(`status: ${result.status}`);
console.log(`time: ${(result.ms / 1000).toFixed(2)}s`);
console.log(`nodes: ${result.stats.nodes}`);
console.log(`dead ends: ${result.stats.deadEnds}`);
console.log(`forced cells: ${result.stats.imposed}`);
console.log(`candidate checks: ${result.stats.candidateChecks}`);
if (result.table) {
  console.log("counterexample table:");
  console.log(result.table);
}
