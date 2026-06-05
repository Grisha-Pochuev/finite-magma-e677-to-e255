"use strict";

function cyclePerm(n, cycles) {
  const p = Array.from({ length: n }, (_, i) => i);
  for (const cycle of cycles) {
    for (let i = 0; i < cycle.length; i++) p[cycle[i]] = cycle[(i + 1) % cycle.length];
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

function addCell(cells, row, col, value, reason) {
  const key = `${row},${col}`;
  if (!cells.has(key)) cells.set(key, { row, col, value, reasons: [] });
  const cell = cells.get(key);
  if (cell.value !== value) {
    cell.conflict = { old: cell.value, value, reason };
  }
  cell.reasons.push(reason);
}

const n = Number(process.argv[2] || 8);
const row0Index = Number(process.argv[3] || 29);
const row0 = row0Representatives(n)[row0Index];
const cells = new Map();

// Known row 0.
for (let col = 0; col < n; col++) addCell(cells, 0, col, row0.p[col], "row0 normalization");

// From E677 with y=0:
// (0*x)*0 = L_x^{-1}(L_0^{-1}(x)).
// When x=0, this is concrete because L_x=L_0.
const a1 = row0.p[0];
addCell(cells, a1, 0, row0.inv[row0.inv[0]], "E677 with x=0,y=0");

// From bad + Lemma 13.2 filters for each row y.
for (let y = 0; y < n; y++) {
  const forbidden = row0.inv[y];
  // These are inequalities; print separately.
}

console.log(`row0 case ${row0Index + 1}: ${row0.p.join(" ")}`);
console.log("forced equalities from row0 alone:");
for (const cell of Array.from(cells.values()).sort((a, b) => a.row - b.row || a.col - b.col)) {
  const conflict = cell.conflict ? ` CONFLICT ${JSON.stringify(cell.conflict)}` : "";
  console.log(`  row ${cell.row}, col ${cell.col} = ${cell.value}; ${cell.reasons.join("; ")}${conflict}`);
}
console.log("universal inequalities for a bad element 0:");
for (let y = 0; y < n; y++) {
  const forbidden = row0.inv[y];
  console.log(`  row ${y}: col 0 != 0, col 0 != ${forbidden}, col ${y} != ${forbidden}`);
}

