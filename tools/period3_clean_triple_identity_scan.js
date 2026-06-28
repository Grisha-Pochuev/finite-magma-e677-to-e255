"use strict";

// Scan cached eq677 db models for strict right-h period-3 cycles that admit
// a clean anchored-X3 shared-step triple.  This sits between the all-cycle
// scan and the M7-witness scan: it asks what the clean anchored input alone
// forces in the cached models.

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

function profileFor(table, inv, z, b, h) {
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

const totals = {
  cleanTriples: 0,
  cleanTripleCycles: new Set(),
  models: new Map(),
  profiles: new Map(),
  firstEvents: new Map(),
  profileEvents: new Map(),
  namedEqualities: new Map(),
  productHits: new Map(),
  examplesWithoutAIbcz: [],
};

for (const item of localModelFiles()) {
  const table = parseTable(item.file);
  const inv = inverseRows(table);
  const n = table.length;
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

  let modelTriples = 0;
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
        const c = table[b][h];
        if (table[c][h] !== z) continue;
        if (!distinct([z, b, c])) continue;
        const Ib = inv[b][h];
        const Ic = inv[c][h];
        const ZB = table[z][b];
        const BC = table[b][c];
        const CZ = table[c][z];
        const strict =
          distinct([z, b, c, h, Ib, Ic, ZB, BC, CZ]) &&
          distinct([ZB, BC, CZ]) &&
          ![ZB, BC, CZ].some((v) => v === h || v === z || v === b || v === c);
        if (!strict) continue;

        const T = table[U][h];
        const S = table[W][h];
        if (T === S) continue;
        const alpha = inv[z][h];
        if (!anchoredX3TripleClean({ p, q, alpha }, { T, S, b })) continue;

        const A = table[Ib][c];
        const K = table[A][Ib];
        const L = table[c][K];
        const event = firstSourceOrbitEvent(table, inv, { b, z, p, q, U, W, h, alpha, T, S });
        const profile = profileFor(table, inv, z, b, h);
        const eventKey = `${event.kind}@d${event.depth}:${event.signature}`;
        const modelKey = `${item.size}/${item.name}`;
        const names = { b, z, h, c, alpha, Ib, Ic, ZB, BC, CZ, p, q, U, W, T, S, A, K, L };
        const entries = Object.entries(names);

        totals.cleanTriples++;
        modelTriples++;
        totals.cleanTripleCycles.add(`${modelKey}:${z},${b},${h}`);
        add(totals.profiles, profile);
        add(totals.firstEvents, eventKey);
        add(totals.profileEvents, `${profile} || ${eventKey}`);
        if (!profile.includes("A=Ib*c=z") && totals.examplesWithoutAIbcz.length < 20) {
          totals.examplesWithoutAIbcz.push({ model: modelKey, z, b, c, h, Ib, Ic, p, q, U, W, T, S, alpha, A, K, L, profile, event });
        }

        for (let a = 0; a < entries.length; a++) {
          const [aName, aValue] = entries[a];
          for (let bIndex = a + 1; bIndex < entries.length; bIndex++) {
            const [bName, bValue] = entries[bIndex];
            if (aValue === bValue) add(totals.namedEqualities, `${aName}=${bName}`);
          }
        }
        for (const [xName, x] of entries) {
          for (const [yName, y] of entries) {
            const xy = table[x][y];
            for (const [vName, v] of entries) {
              if (xy === v) add(totals.productHits, `${xName}*${yName}=${vName}`);
            }
          }
        }
      }
    }
  }
  if (modelTriples > 0) totals.models.set(`${item.size}/${item.name}`, modelTriples);
}

function sortedObject(map) {
  return Object.fromEntries([...map.entries()].sort((a, b) => b[1] - a[1] || a[0].localeCompare(b[0])));
}

function universal(map) {
  return Object.fromEntries([...map.entries()]
    .filter(([, count]) => count === totals.cleanTriples)
    .sort((a, b) => a[0].localeCompare(b[0])));
}

function top(map, limit = 80) {
  return Object.fromEntries([...map.entries()]
    .sort((a, b) => b[1] - a[1] || a[0].localeCompare(b[0]))
    .slice(0, limit));
}

console.log(JSON.stringify({
  cache: cacheDir,
  cleanTriples: totals.cleanTriples,
  cleanTripleCycles: totals.cleanTripleCycles.size,
  modelCounts: sortedObject(totals.models),
  profiles: sortedObject(totals.profiles),
  firstEvents: sortedObject(totals.firstEvents),
  profileEvents: sortedObject(totals.profileEvents),
  universalNamedEqualities: universal(totals.namedEqualities),
  universalNamedProductHits: universal(totals.productHits),
  topNamedEqualities: top(totals.namedEqualities),
  topNamedProductHits: top(totals.productHits),
  examplesWithoutAIbcz: totals.examplesWithoutAIbcz,
}, null, 2));
