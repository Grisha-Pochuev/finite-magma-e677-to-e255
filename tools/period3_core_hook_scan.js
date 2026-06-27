"use strict";

// Scan cached eq677 db models for the period-3 zipper old-target/core hook.
// This is a candidate-lemma finder, not a proof.

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

function distinct(values) {
  return new Set(values).size === values.length;
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
  out.sort((a, b) => Number(a.size) - Number(b.size) || Number(a.name) - Number(b.name));
  return out;
}

function hGraphEdges(table, inv, target) {
  const n = table.length;
  const edges = [];
  const incident = Array.from({ length: n }, () => []);
  const degree = new Int32Array(n);
  for (let row = 0; row < n; row++) {
    const input = inv[row][target];
    const output = table[row][target];
    const id = edges.length;
    edges.push({ row, input, output });
    incident[input].push(id);
    incident[output].push(id);
    if (input === output) degree[input] += 2;
    else {
      degree[input]++;
      degree[output]++;
    }
  }
  return { edges, incident, degree };
}

function twoCoreRows(table, inv, target) {
  const n = table.length;
  const { edges, incident, degree } = hGraphEdges(table, inv, target);
  const aliveEdge = new Uint8Array(edges.length);
  aliveEdge.fill(1);
  const aliveVertex = new Uint8Array(n);
  aliveVertex.fill(1);
  const queue = [];
  for (let v = 0; v < n; v++) if (degree[v] <= 1) queue.push(v);

  for (let head = 0; head < queue.length; head++) {
    const v = queue[head];
    if (!aliveVertex[v] || degree[v] > 1) continue;
    aliveVertex[v] = 0;
    for (const edgeId of incident[v]) {
      if (!aliveEdge[edgeId]) continue;
      aliveEdge[edgeId] = 0;
      const edge = edges[edgeId];
      const a = edge.input;
      const b = edge.output;
      if (a === b) {
        degree[a] -= 2;
        if (aliveVertex[a] && degree[a] <= 1) queue.push(a);
      } else {
        degree[a]--;
        degree[b]--;
        if (aliveVertex[a] && degree[a] <= 1) queue.push(a);
        if (aliveVertex[b] && degree[b] <= 1) queue.push(b);
      }
    }
  }

  const coreRows = new Uint8Array(table.length);
  let coreEdgeCount = 0;
  for (let edgeId = 0; edgeId < edges.length; edgeId++) {
    if (!aliveEdge[edgeId]) continue;
    coreEdgeCount++;
    coreRows[edges[edgeId].row] = 1;
  }

  const rowCoreExcess = new Int32Array(table.length);
  const rowCoreVertices = new Int32Array(table.length);
  const rowCoreEdges = new Int32Array(table.length);
  const rowComponent = new Int32Array(table.length);
  rowComponent.fill(-1);
  const componentHasTargetVertex = [];
  const componentRightFixerCount = [];
  const rightFixerRows = new Uint8Array(table.length);
  for (let row = 0; row < table.length; row++) {
    if (table[row][target] === target) rightFixerRows[row] = 1;
  }
  const seenVertex = new Uint8Array(table.length);
  let componentId = 0;
  for (let start = 0; start < table.length; start++) {
    if (!aliveVertex[start] || seenVertex[start]) continue;
    const queue = [start];
    seenVertex[start] = 1;
    const vertices = [];
    const componentEdges = new Set();
    for (let head = 0; head < queue.length; head++) {
      const v = queue[head];
      vertices.push(v);
      for (const edgeId of incident[v]) {
        if (!aliveEdge[edgeId]) continue;
        componentEdges.add(edgeId);
        const edge = edges[edgeId];
        const other = edge.input === v ? edge.output : edge.input;
        if (!seenVertex[other]) {
          seenVertex[other] = 1;
          queue.push(other);
        }
      }
    }
    const excess = componentEdges.size - vertices.length;
    let rightFixers = 0;
    for (const edgeId of componentEdges) {
      const row = edges[edgeId].row;
      rowCoreExcess[row] = excess;
      rowCoreVertices[row] = vertices.length;
      rowCoreEdges[row] = componentEdges.size;
      rowComponent[row] = componentId;
      if (rightFixerRows[row]) rightFixers++;
    }
    componentHasTargetVertex[componentId] = vertices.includes(target);
    componentRightFixerCount[componentId] = rightFixers;
    componentId++;
  }

  return {
    coreRows,
    rowCoreExcess,
    rowCoreVertices,
    rowCoreEdges,
    rowComponent,
    componentHasTargetVertex,
    componentRightFixerCount,
    coreEdgeCount,
  };
}

function firstEvent(table, inv, named) {
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

    const parts = [];
    for (let i = 0; i < current.length; i++) {
      for (const old of edges) compareEdges(parts, current[i], old);
      for (let j = 0; j < i; j++) compareEdges(parts, current[i], current[j]);
    }
    if (parts.length > 0) {
      const onlySelf = parts.every((x) => x.startsWith("self-source-repeat:"));
      return {
        kind: onlySelf ? "clean-self-repeat" : "routed",
        signature: onlySelf ? selfRepeatSignature(current, edges) : Array.from(new Set(parts)).sort().join("|"),
      };
    }
    edges.push(...current);
  }
  return { kind: "no-event", signature: "" };
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
      if (edge.orbit === old.orbit && edge.source === old.source) parts.push(`${edge.orbit}:${edge.depth}->${old.depth}`);
    }
  }
  return Array.from(new Set(parts)).sort().join("|");
}

function add(map, key) {
  map.set(key, (map.get(key) || 0) + 1);
}

let total = 0;
const modelCounts = new Map();
const hookProfiles = new Map();
const oldTargetProfiles = new Map();
const hookExcessProfiles = new Map();
const hookRightFixerProfiles = new Map();
const hookComponentSizeProfiles = new Map();
const coreSizeProfiles = new Map();
const hookEndpointProfiles = new Map();
const fanRowNameProfiles = new Map();
const fanRowFreshProfiles = new Map();
const misses = [];

for (const item of localModelFiles()) {
  const table = parseTable(item.file);
  const n = table.length;
  const inv = inverseRows(table);
  const coreCache = new Map();
  const core = (target) => {
    if (!coreCache.has(target)) coreCache.set(target, twoCoreRows(table, inv, target));
    return coreCache.get(target);
  };

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

        const event = firstEvent(table, inv, { b, z, p, q, U, W, h, alpha, T, S });
        if (event.kind !== "clean-self-repeat" || !event.signature.includes("z:3->0")) continue;

        const c = table[b][h];
        if (table[c][h] !== z) continue;
        const ZB = table[z][b];
        const BC = table[b][c];
        const CZ = table[c][z];
        if (!distinct([z, b, c])) continue;
        if (!distinct([ZB, BC, CZ])) continue;
        if ([ZB, BC, CZ].some((v) => v === h || v === z || v === b || v === c)) continue;

        total++;
        modelCount++;

        const hb = core(b);
        const hc = core(c);
        const hz = core(z);
        const inHb = hb.coreRows[z] === 1;
        const inHc = hc.coreRows[b] === 1;
        const inHz = hz.coreRows[c] === 1;
        add(hookProfiles, `Hb(row z)=${inHb};Hc(row b)=${inHc};Hz(row c)=${inHz}`);
        add(oldTargetProfiles, `Hb(row z)=${inHb}`);
        add(hookExcessProfiles, `HbExcess(row z)=${hb.rowCoreExcess[z]};HcExcess(row b)=${hc.rowCoreExcess[b]};HzExcess(row c)=${hz.rowCoreExcess[c]}`);
        add(
          hookComponentSizeProfiles,
          [
            `Hb=${hb.rowCoreEdges[z]}/${hb.rowCoreVertices[z]}`,
            `Hc=${hc.rowCoreEdges[b]}/${hc.rowCoreVertices[b]}`,
            `Hz=${hz.rowCoreEdges[c]}/${hz.rowCoreVertices[c]}`,
          ].join(";")
        );
        const hbComp = hb.rowComponent[z];
        const hcComp = hc.rowComponent[b];
        const hzComp = hz.rowComponent[c];
        add(
          hookRightFixerProfiles,
          [
            `HbTargetVertex=${hb.componentHasTargetVertex[hbComp] || false}`,
            `HbRightFixers=${hb.componentRightFixerCount[hbComp] || 0}`,
            `HcTargetVertex=${hc.componentHasTargetVertex[hcComp] || false}`,
            `HcRightFixers=${hc.componentRightFixerCount[hcComp] || 0}`,
            `HzTargetVertex=${hz.componentHasTargetVertex[hzComp] || false}`,
            `HzRightFixers=${hz.componentRightFixerCount[hzComp] || 0}`,
          ].join(";")
        );
        add(coreSizeProfiles, `HbCoreEdges=${hb.coreEdgeCount};HcCoreEdges=${hc.coreEdgeCount};HzCoreEdges=${hz.coreEdgeCount}`);

        let hcOutAtH = 0;
        let hcInAtBC = 0;
        const named = { b, z, c, h, p, q, U, W, T, S, alpha, ZB, BC, CZ };
        named.Ib = inv[b][h];
        named.Ic = inv[c][h];
        const nameByValue = new Map();
        for (const [name, value] of Object.entries(named)) {
          if (!nameByValue.has(value)) nameByValue.set(value, []);
          nameByValue.get(value).push(name);
        }
        const fanNames = [];
        let freshFanRows = 0;
        for (let row = 0; row < n; row++) {
          if (inv[row][c] === h) {
            hcOutAtH++;
            const names = nameByValue.get(row);
            if (names === undefined) freshFanRows++;
            else fanNames.push(...names);
          }
          if (table[row][c] === BC) hcInAtBC++;
        }
        add(hookEndpointProfiles, `HcOutAtH=${hcOutAtH};HcInAtBC=${hcInAtBC}`);
        add(fanRowNameProfiles, fanNames.sort().join(",") || "none-named");
        add(fanRowFreshProfiles, `freshFanRows=${freshFanRows};namedFanRows=${fanNames.length}`);

        if (!(inHb && inHc && inHz) && misses.length < 20) {
          misses.push({
            model: `${item.size}/${item.name}`,
            b, z, c, h,
            rowZInHbCore: inHb,
            rowBInHcCore: inHc,
            rowCInHzCore: inHz,
            rowZHbCoreExcess: hb.rowCoreExcess[z],
            rowBHcCoreExcess: hc.rowCoreExcess[b],
            rowCHzCoreExcess: hz.rowCoreExcess[c],
            rowZHbCoreSize: `${hb.rowCoreEdges[z]}/${hb.rowCoreVertices[z]}`,
            rowBHcCoreSize: `${hc.rowCoreEdges[b]}/${hc.rowCoreVertices[b]}`,
            rowCHzCoreSize: `${hz.rowCoreEdges[c]}/${hz.rowCoreVertices[c]}`,
            rowZHbRightFixers: hb.componentRightFixerCount[hb.rowComponent[z]],
            rowBHcRightFixers: hc.componentRightFixerCount[hc.rowComponent[b]],
            rowCHzRightFixers: hz.componentRightFixerCount[hz.rowComponent[c]],
            hcOutAtH,
            hcInAtBC,
            fanNames: fanNames.sort(),
            freshFanRows,
            hbCoreEdges: hb.coreEdgeCount,
            hcCoreEdges: hc.coreEdgeCount,
            hzCoreEdges: hz.coreEdgeCount,
          });
        }
      }
    }
  }
  if (modelCount > 0) modelCounts.set(`${item.size}/${item.name}`, modelCount);
}

console.log(JSON.stringify({
  cache: cacheDir,
  totalStrictPeriod3: total,
  modelCounts: Object.fromEntries(modelCounts),
  hookProfiles: Object.fromEntries([...hookProfiles.entries()].sort()),
  oldTargetProfiles: Object.fromEntries([...oldTargetProfiles.entries()].sort()),
  hookExcessProfiles: Object.fromEntries([...hookExcessProfiles.entries()].sort()),
  hookComponentSizeProfiles: Object.fromEntries([...hookComponentSizeProfiles.entries()].sort()),
  hookRightFixerProfiles: Object.fromEntries([...hookRightFixerProfiles.entries()].sort()),
  hookEndpointProfiles: Object.fromEntries([...hookEndpointProfiles.entries()].sort()),
  fanRowNameProfiles: Object.fromEntries([...fanRowNameProfiles.entries()].sort()),
  fanRowFreshProfiles: Object.fromEntries([...fanRowFreshProfiles.entries()].sort()),
  coreSizeProfilesTop: [...coreSizeProfiles.entries()].sort((a, b) => b[1] - a[1]).slice(0, 20),
  misses,
}, null, 2));
