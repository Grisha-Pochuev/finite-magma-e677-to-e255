"use strict";

// Scan external eq677 db period-3 zipper representatives for short named
// product identities. This is a candidate-lemma finder, not a proof.

const fs = require("fs");
const path = require("path");

const cacheDir = process.argv[2] || path.join("cache", "eq677-db");
const sizes = fs.existsSync(cacheDir)
  ? fs.readdirSync(cacheDir).filter((x) => /^\d+$/.test(x))
  : [];

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

function distinct(values) {
  return new Set(values).size === values.length;
}

function localModelFiles() {
  const out = [];
  for (const size of sizes) {
    const dir = path.join(cacheDir, size);
    if (!fs.existsSync(dir)) continue;
    for (const name of fs.readdirSync(dir)) {
      const file = path.join(dir, name);
      if (fs.statSync(file).isFile()) out.push({ size, name, file });
    }
  }
  out.sort((a, b) => Number(a.size) - Number(b.size) || Number(a.name) - Number(b.name));
  return out;
}

function addCount(map, key) {
  map.set(key, (map.get(key) || 0) + 1);
}

function firstSourceOrbitEvent(table, inv, named) {
  const { b, z, U, W, h, alpha, T, S } = named;
  const n = table.length;
  const orbits = [
    { name: "U", rows: [U], firstInput: named.p, firstOutput: T },
    { name: "W", rows: [W], firstInput: named.q, firstOutput: S },
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
      const onlySelfRepeat = parts.every((x) => x.startsWith("self-source-repeat:"));
      return {
        kind: onlySelfRepeat ? "clean-self-repeat" : "routed",
        depth,
        signature: onlySelfRepeat ? selfRepeatSignature(current, edges) : "",
      };
    }
    edges.push(...current);
  }
  return { kind: "no-event", depth: n + 1, signature: "" };
}

function firstEventParts(current, previous) {
  const parts = [];
  const allPrevious = previous.slice();
  for (let i = 0; i < current.length; i++) {
    const edge = current[i];
    for (const old of allPrevious) compareSourceOrbitEdges(parts, edge, old);
    for (let j = 0; j < i; j++) compareSourceOrbitEdges(parts, edge, current[j]);
  }
  return Array.from(new Set(parts)).sort();
}

function compareSourceOrbitEdges(parts, a, b) {
  if (a.source === b.source) {
    if (a.orbit === b.orbit) parts.push(`self-source-repeat:${a.orbit}`);
    else parts.push(`cross-source:${a.orbit}=${b.orbit}`);
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

const productHits = new Map();
const productSelfHits = new Map();
const e255Hits = new Map();
const idempotentHits = new Map();
const modelCounts = new Map();
let total = 0;

for (const item of localModelFiles()) {
  const table = parseTable(item.file);
  const n = table.length;
  const inv = inverseRows(table);
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

  let modelCount = 0;
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
        const T = table[U][h];
        const S = table[W][h];
        if (T === S) continue;
        const alpha = inv[z][h];
        if (!distinct([b, z, p, q, U, W, h, T, S, alpha])) continue;

        const firstEvent = firstSourceOrbitEvent(table, inv, { b, z, p, q, U, W, h, alpha, T, S });
        if (firstEvent.kind !== "clean-self-repeat" || !firstEvent.signature.includes("z:3->0")) continue;

        const c = table[b][h];
        if (table[c][h] !== z) continue;
        const ZB = table[z][b];
        const BC = table[b][c];
        const CZ = table[c][z];
        if (!distinct([z, b, c])) continue;
        if (!distinct([ZB, BC, CZ])) continue;
        if ([ZB, BC, CZ].some((v) => v === h || v === z || v === b || v === c)) continue;

        const Ib = inv[b][h];
        const Ic = inv[c][h];
        const names = { b, z, h, c, alpha, Ib, Ic, ZB, BC, CZ, p, q, U, W, T, S };
        const entries = Object.entries(names);
        total++;
        modelCount++;

        for (const [xName, x] of entries) {
          const xx = table[x][x];
          if (xx === x) addCount(idempotentHits, `${xName}*${xName}=${xName}`);
          const d4 = table[table[table[x][x]][x]][x];
          if (d4 === x) addCount(e255Hits, `E255(${xName})`);
          for (const [yName, y] of entries) {
            const xy = table[x][y];
            if (xy === x) addCount(productSelfHits, `${xName}*${yName}=${xName}`);
            if (xy === y) addCount(productSelfHits, `${xName}*${yName}=${yName}`);
            for (const [zName, value] of entries) {
              if (xy === value) addCount(productHits, `${xName}*${yName}=${zName}`);
            }
          }
        }
      }
    }
  }
  if (modelCount > 0) modelCounts.set(`${item.size}/${item.name}`, modelCount);
}

function universal(map) {
  return Array.from(map.entries())
    .filter(([, count]) => count === total)
    .map(([profile, count]) => ({ profile, count }))
    .sort((a, b) => a.profile.localeCompare(b.profile));
}

function top(map, limit = 30) {
  return Array.from(map.entries())
    .sort((a, b) => b[1] - a[1] || a[0].localeCompare(b[0]))
    .slice(0, limit)
    .map(([profile, count]) => ({ profile, count }));
}

console.log(JSON.stringify({
  cache: cacheDir,
  totalPeriod3Clean: total,
  modelCounts: Object.fromEntries(modelCounts),
  universalNamedProductHits: universal(productHits),
  universalSelfProductHits: universal(productSelfHits),
  universalIdempotentHits: universal(idempotentHits),
  universalE255Hits: universal(e255Hits),
  topNamedProductHits: top(productHits),
}, null, 2));
