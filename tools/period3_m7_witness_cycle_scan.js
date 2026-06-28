"use strict";

// Scan cached eq677 db models for right-h period-3 cycles and mark which
// cycles actually arise from the current shared-step/M7 clean self-repeat
// residual.  This is a diagnostic/candidate-lemma finder, not a proof.

const fs = require("fs");
const path = require("path");

const cacheDir = process.argv[2] || path.join("cache", "eq677-db");

function parseTable(file) {
  return fs.readFileSync(file, "utf8").trim().split(/\n/).map((line) =>
    line.trim().split(/\s+/).map(Number)
  );
}

function inverseRows(table) {
  const n = table.length;
  const inv = Array.from({ length: n }, () => new Int32Array(n).fill(-1));
  for (let row = 0; row < n; row++) {
    for (let col = 0; col < n; col++) inv[row][table[row][col]] = col;
  }
  return inv;
}

function localModelFiles() {
  if (!fs.existsSync(cacheDir)) return [];
  const out = [];
  const sizes = fs.readdirSync(cacheDir).filter((x) => /^\d+$/.test(x));
  for (const size of sizes) {
    const dir = path.join(cacheDir, size);
    if (!fs.existsSync(dir)) continue;
    for (const name of fs.readdirSync(dir)) {
      const file = path.join(dir, name);
      if (fs.statSync(file).isFile()) out.push({ size, name, file });
    }
  }
  out.sort((a, b) => Number(a.size) - Number(b.size) || a.name.localeCompare(b.name));
  return out;
}

function distinct(values) {
  return new Set(values).size === values.length;
}

function add(map, key, amount = 1) {
  map.set(key, (map.get(key) || 0) + amount);
}

function cycleKey(z, b, h) {
  return `${z},${b},${h}`;
}

function profileForCycle(table, inv, z, b, h) {
  const c = table[b][h];
  const Ib = inv[b][h];
  const Ic = inv[c][h];
  const BC = table[b][c];
  const A = table[Ib][c];
  const K = table[A][Ib];
  const L = table[c][K];
  const parts = [];
  if (A === z) parts.push("A=Ib*c=z");
  if (A === b) parts.push("A=Ib*c=b");
  if (A === c) parts.push("A=Ib*c=c");
  if (A === h) parts.push("A=Ib*c=h");
  if (A === BC) parts.push("A=Ib*c=BC");
  if (K === Ic) parts.push("K=Ic");
  if (K === c) parts.push("K=c");
  if (K === A) parts.push("K=A");
  if (K === z) parts.push("K=z");
  if (L === h) parts.push("L=h");
  if (L === table[c][c]) parts.push("L=c*c");
  if (table[Ib][h] === c) parts.push("Ib*h=c");
  if (table[z][Ib] === Ic) parts.push("z*Ib=Ic");
  return parts.length ? parts.sort().join(";") : "fresh";
}

function anchoredX3TripleClean(inputs, outputs) {
  const inVals = Object.values(inputs);
  const outVals = Object.values(outputs);
  if (!distinct(inVals) || !distinct(outVals)) return false;
  for (const i of inVals) {
    for (const o of outVals) {
      if (i === o) return false;
    }
  }
  return true;
}

function firstSourceOrbitEvent(table, inv, named) {
  const { b, z, p, q, U, W, h, alpha, T, S } = named;
  const n = table.length;
  const orbits = [
    { name: "U", rows: [U], firstInput: p, firstOutput: T },
    { name: "W", rows: [W], firstInput: q, firstOutput: S },
    { name: "z", rows: [z], firstInput: alpha, firstOutput: b },
  ];
  const edges = [];
  for (const orbit of orbits) {
    edges.push({
      orbit: orbit.name,
      depth: 0,
      source: orbit.rows[0],
      input: orbit.firstInput,
      output: orbit.firstOutput,
    });
  }

  for (let depth = 1; depth <= n + 1; depth++) {
    const current = [];
    for (const orbit of orbits) {
      const prev = orbit.rows[depth - 1];
      const source = table[prev][h];
      orbit.rows.push(source);
      current.push({
        orbit: orbit.name,
        depth,
        source,
        input: inv[source][h],
        output: table[source][h],
      });
    }
    const parts = firstEventParts(current, edges);
    if (parts.length > 0) {
      const onlySelf = parts.every((x) => x.startsWith("self-source-repeat:"));
      return {
        kind: onlySelf ? "clean-self-repeat" : "routed",
        depth,
        signature: onlySelf ? selfRepeatSignature(current, edges) : parts.join("|"),
      };
    }
    edges.push(...current);
  }
  return { kind: "no-event", depth: n + 1, signature: "" };
}

function firstEventParts(current, previous) {
  const parts = [];
  for (let i = 0; i < current.length; i++) {
    const edge = current[i];
    for (const old of previous) compareEdges(parts, edge, old);
    for (let j = 0; j < i; j++) compareEdges(parts, edge, current[j]);
  }
  return Array.from(new Set(parts)).sort();
}

function compareEdges(parts, a, b) {
  if (a.source === b.source) {
    parts.push(a.orbit === b.orbit ? `self-source-repeat:${a.orbit}` : `cross-source:${a.orbit}=${b.orbit}`);
  }
  if (a.output === b.output && a.source !== b.source) parts.push(`output-merge:${a.orbit}=${b.orbit}`);
  if (a.input === b.input && a.source !== b.source) parts.push(`input-repeat:${a.orbit}=${b.orbit}`);
  if (a.input === b.output) parts.push(`input-output:${a.orbit}.input=${b.orbit}.output`);
  if (a.output === b.input) parts.push(`input-output:${a.orbit}.output=${b.orbit}.input`);
}

function selfRepeatSignature(current, previous) {
  const parts = [];
  for (const edge of current) {
    for (const old of previous) {
      if (edge.orbit === old.orbit && edge.source === old.source) {
        parts.push(`${edge.orbit}:${edge.depth}->${old.depth}`);
      }
    }
  }
  return Array.from(new Set(parts)).sort().join("|");
}

function scanModel(table) {
  const n = table.length;
  const inv = inverseRows(table);
  const cycles = new Map();
  for (let h = 0; h < n; h++) {
    for (let z = 0; z < n; z++) {
      const b = table[z][h];
      const c = table[b][h];
      if (table[c][h] !== z) continue;
      if (!distinct([z, b, c])) continue;
      const key = cycleKey(z, b, h);
      const ZB = table[z][b];
      const BC = table[b][c];
      const CZ = table[c][z];
      const strict =
        distinct([z, b, c, h, inv[b][h], inv[c][h], ZB, BC, CZ]) &&
        distinct([ZB, BC, CZ]) &&
        ![ZB, BC, CZ].some((v) => v === h || v === z || v === b || v === c);
      cycles.set(key, {
        z, b, h,
        strict,
        profile: profileForCycle(table, inv, z, b, h),
        m7Witnesses: 0,
        m7CleanTriples: 0,
        routedBeforeM7: 0,
        routedEvents: new Map(),
      });
    }
  }

  const groups = new Map();
  for (let p = 0; p < n; p++) {
    for (let b = 0; b < n; b++) {
      const z = table[p][b];
      const key = b * n + z;
      let rows = groups.get(key);
      if (rows === undefined) groups.set(key, (rows = []));
      rows.push(p);
    }
  }

  for (const [key, rows] of groups) {
    if (rows.length < 2) continue;
    const b = Math.floor(key / n);
    const z = key % n;
    for (let i = 0; i < rows.length; i++) {
      for (let j = i + 1; j < rows.length; j++) {
        const p = rows[i];
        const q = rows[j];
        const U = table[p][z];
        const W = table[q][z];
        const h = table[U][p];
        if (table[W][q] !== h) continue;
        if (table[z][h] !== b) continue;
        const cycle = cycles.get(cycleKey(z, b, h));
        if (cycle === undefined) continue;
        const T = table[U][h];
        const S = table[W][h];
        if (T === S) continue;
        const alpha = inv[z][h];
        if (!anchoredX3TripleClean({ p, q, alpha }, { T, S, b })) continue;
        cycle.m7CleanTriples++;
        const event = firstSourceOrbitEvent(table, inv, { b, z, p, q, U, W, h, alpha, T, S });
        if (event.kind === "clean-self-repeat" && event.signature.includes("z:3->0")) {
          cycle.m7Witnesses++;
        } else {
          cycle.routedBeforeM7++;
          add(cycle.routedEvents, `d${event.depth}:${event.signature}`);
        }
      }
    }
  }

  return cycles;
}

const totals = {
  cycles: 0,
  strictCycles: 0,
  cyclesWithM7Witness: 0,
  strictCyclesWithM7Witness: 0,
  m7WitnessPairs: 0,
  m7ProfileCounts: new Map(),
  strictM7ProfileCounts: new Map(),
  strictNoM7ProfileCounts: new Map(),
  strictNoM7NoCleanTripleProfileCounts: new Map(),
  strictNoM7RoutedCleanTripleProfileCounts: new Map(),
  cleanTripleProfilePairCounts: new Map(),
  routedBeforeM7ProfileCounts: new Map(),
  routedBeforeM7EventCounts: new Map(),
  routedBeforeM7ProfileEventCounts: new Map(),
  examplesM7WithoutAIbcz: [],
  examplesKcNoM7: [],
  examplesNoM7WithCleanTripleWithoutAIbcz: [],
};

for (const item of localModelFiles()) {
  const table = parseTable(item.file);
  const cycles = scanModel(table);
  for (const cycle of cycles.values()) {
    totals.cycles++;
    if (cycle.strict) totals.strictCycles++;
    if (cycle.m7Witnesses > 0) {
      totals.cyclesWithM7Witness++;
      totals.m7WitnessPairs += cycle.m7Witnesses;
      add(totals.m7ProfileCounts, cycle.profile);
      if (cycle.strict) {
        totals.strictCyclesWithM7Witness++;
        add(totals.strictM7ProfileCounts, cycle.profile);
        if (!cycle.profile.includes("A=Ib*c=z") && totals.examplesM7WithoutAIbcz.length < 20) {
          totals.examplesM7WithoutAIbcz.push({ model: `${item.size}/${item.name}`, ...cycle });
        }
      }
    } else if (cycle.strict) {
      add(totals.strictNoM7ProfileCounts, cycle.profile);
      if (cycle.m7CleanTriples === 0) {
        add(totals.strictNoM7NoCleanTripleProfileCounts, cycle.profile);
      } else {
        add(totals.strictNoM7RoutedCleanTripleProfileCounts, cycle.profile);
        if (!cycle.profile.includes("A=Ib*c=z") && totals.examplesNoM7WithCleanTripleWithoutAIbcz.length < 20) {
          totals.examplesNoM7WithCleanTripleWithoutAIbcz.push({ model: `${item.size}/${item.name}`, ...cycle });
        }
      }
      if (cycle.profile.includes("K=c") && totals.examplesKcNoM7.length < 20) {
        totals.examplesKcNoM7.push({ model: `${item.size}/${item.name}`, ...cycle });
      }
    }
    if (cycle.m7CleanTriples > 0) add(totals.cleanTripleProfilePairCounts, cycle.profile, cycle.m7CleanTriples);
    if (cycle.routedBeforeM7 > 0) {
      add(totals.routedBeforeM7ProfileCounts, cycle.profile, cycle.routedBeforeM7);
      for (const [event, count] of cycle.routedEvents) {
        add(totals.routedBeforeM7EventCounts, event, count);
        add(totals.routedBeforeM7ProfileEventCounts, `${cycle.profile} || ${event}`, count);
      }
    }
  }
}

function sortedObject(map) {
  return Object.fromEntries([...map.entries()].sort((a, b) => b[1] - a[1] || a[0].localeCompare(b[0])));
}

console.log(JSON.stringify({
  cache: cacheDir,
  cycles: totals.cycles,
  strictCycles: totals.strictCycles,
  cyclesWithM7Witness: totals.cyclesWithM7Witness,
  strictCyclesWithM7Witness: totals.strictCyclesWithM7Witness,
  m7WitnessPairs: totals.m7WitnessPairs,
  m7ProfileCounts: sortedObject(totals.m7ProfileCounts),
  strictM7ProfileCounts: sortedObject(totals.strictM7ProfileCounts),
  strictNoM7ProfileCounts: sortedObject(totals.strictNoM7ProfileCounts),
  strictNoM7NoCleanTripleProfileCounts: sortedObject(totals.strictNoM7NoCleanTripleProfileCounts),
  strictNoM7RoutedCleanTripleProfileCounts: sortedObject(totals.strictNoM7RoutedCleanTripleProfileCounts),
  cleanTripleProfilePairCounts: sortedObject(totals.cleanTripleProfilePairCounts),
  routedBeforeM7ProfileCounts: sortedObject(totals.routedBeforeM7ProfileCounts),
  routedBeforeM7EventCounts: sortedObject(totals.routedBeforeM7EventCounts),
  routedBeforeM7ProfileEventCounts: sortedObject(totals.routedBeforeM7ProfileEventCounts),
  examplesM7WithoutAIbcz: totals.examplesM7WithoutAIbcz,
  examplesKcNoM7: totals.examplesKcNoM7,
  examplesNoM7WithCleanTripleWithoutAIbcz: totals.examplesNoM7WithCleanTripleWithoutAIbcz,
}, null, 2));
