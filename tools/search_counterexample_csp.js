"use strict";

function permutations(n) {
  const out = [];
  const used = Array(n).fill(false);
  const cur = [];
  function rec() {
    if (cur.length === n) {
      out.push(cur.slice());
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
  return p;
}

function partitions(n, maxPart = n) {
  if (n === 0) return [[]];
  const out = [];
  for (let first = Math.min(n, maxPart); first >= 1; first--) {
    for (const rest of partitions(n - first, first)) {
      out.push([first, ...rest]);
    }
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

function satisfiesE677(table) {
  const n = table.length;
  for (let x = 0; x < n; x++) {
    for (let y = 0; y < n; y++) {
      const yx = table[y][x];
      const yx_y = table[yx][y];
      const inner = table[x][yx_y];
      const rhs = table[y][inner];
      if (rhs !== x) return false;
    }
  }
  return true;
}

function satisfiesE255(table) {
  const n = table.length;
  for (let x = 0; x < n; x++) {
    const sx = table[x][x];
    const t = table[sx][x];
    const rhs = table[t][x];
    if (rhs !== x) return false;
  }
  return true;
}

function formatTable(table) {
  return table.map((row) => row.join(" ")).join("\n");
}

function constraintOk(assign, x, y) {
  const rowY = assign[y];
  const rowX = assign[x];
  if (!rowY || !rowX) return true;
  const z = rowY[x];
  const rowZ = assign[z];
  if (!rowZ) return true;
  const yx_y = rowZ[y];
  const inner = rowX[yx_y];
  return rowY[inner] === x;
}

function isConsistent(assign, n) {
  for (let x = 0; x < n; x++) {
    for (let y = 0; y < n; y++) {
      if (!constraintOk(assign, x, y)) return false;
    }
  }
  return true;
}

function search(n, options) {
  const bad = options.bad ?? 0;
  const maxMs = options.maxMs ?? 60_000;
  const start = Date.now();
  const allPerms = permutations(n).filter((p) => p[bad] !== bad);
  const allRow0Reps = row0Representatives(n);
  const row0Reps =
    options.row0Index === undefined
      ? allRow0Reps
      : [allRow0Reps[options.row0Index]];
  let nodes = 0;
  let prunedValues = 0;

  function timedOut() {
    return Date.now() - start > maxMs;
  }

  function candidateValues(assign, variable) {
    const base = variable === bad ? row0Reps : allPerms;
    const values = [];
    for (const p of base) {
      assign[variable] = p;
      if (isConsistent(assign, n)) values.push(p);
      else prunedValues++;
      assign[variable] = null;
    }
    return values;
  }

  function rec(assign, depth) {
    if (timedOut()) return { status: "timeout" };
    nodes++;

    let bestVar = -1;
    let bestValues = null;
    for (let v = 0; v < n; v++) {
      if (assign[v]) continue;
      const values = candidateValues(assign, v);
      if (values.length === 0) return { status: "none" };
      if (!bestValues || values.length < bestValues.length) {
        bestVar = v;
        bestValues = values;
      }
    }

    if (bestVar === -1) {
      const table = assign.map((row) => row.slice());
      if (satisfiesE677(table) && !satisfiesE255(table)) {
        return { status: "found", table };
      }
      return { status: "none" };
    }

    if (depth <= 1) {
      console.log(
        `depth ${depth}: row ${bestVar}, ${bestValues.length} candidate rows`
      );
    }

    for (const p of bestValues) {
      assign[bestVar] = p;
      const result = rec(assign, depth + 1);
      assign[bestVar] = null;
      if (result.status !== "none") return result;
    }
    return { status: "none" };
  }

  const result = rec(Array(n).fill(null), 0);
  result.nodes = nodes;
  result.prunedValues = prunedValues;
  result.ms = Date.now() - start;
  result.row0Reps = allRow0Reps.length;
  return result;
}

const n = Number(process.argv[2] || 5);
const maxSeconds = Number(process.argv[3] || 60);
const row0Index =
  process.argv[4] === undefined ? undefined : Number(process.argv[4]);
console.log(`Searching for an E677 counterexample to E255 of size ${n}.`);
console.log("The bad element is normalized to 0.");
if (row0Index !== undefined) {
  const reps = row0Representatives(n);
  console.log(
    `row-0 case ${row0Index + 1}/${reps.length}: ${reps[row0Index].join(" ")}`
  );
  console.log(`row-0 cycle type: ${cycleType(reps[row0Index])}`);
}
const result = search(n, { maxMs: maxSeconds * 1000, bad: 0, row0Index });
console.log(`status: ${result.status}`);
console.log(`time: ${(result.ms / 1000).toFixed(2)}s`);
console.log(`search nodes: ${result.nodes}`);
console.log(`pruned row candidates: ${result.prunedValues}`);
console.log(`row-0 representative count: ${result.row0Reps}`);
if (result.table) {
  console.log("counterexample table:");
  console.log(formatTable(result.table));
}
