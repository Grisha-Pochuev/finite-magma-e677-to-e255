"use strict";

// Diagnostic for orientations inside the 2-core of H_b in the known M496 model.
// Counts vertices with core indegree/outdegree patterns for selected targets.
// This is only a model diagnostic, not a proof.

const P = 31;
const FIBER = 16;
const N = P * FIBER;

function mod(a, p) {
  a %= p;
  return a < 0 ? a + p : a;
}

function gfMul(a, b) {
  let out = 0;
  let aa = a;
  let bb = b;
  while (bb) {
    if (bb & 1) out ^= aa;
    bb >>= 1;
    aa <<= 1;
    if (aa & 0x10) aa ^= 0x13;
  }
  return out & 0x0f;
}

function gfPow(a, e) {
  let out = 1;
  let base = a;
  while (e) {
    if (e & 1) out = gfMul(out, base);
    base = gfMul(base, base);
    e >>= 1;
  }
  return out;
}

const zeta = gfPow(2, 3);
const omega = gfPow(2, 5);
const residues = new Set();
for (let x = 1; x < P; x++) residues.add(mod(x * x, P));

function enc(x, s) {
  return x * FIBER + s;
}

function dec(a) {
  return [Math.floor(a / FIBER), a & 15];
}

function op(a, b) {
  const [x, s] = dec(a);
  const [y, t] = dec(b);
  const z = mod(x - 2 * (y - x), P);
  const d = mod(y - x, P);
  const kind = d === 0 ? "0" : residues.has(d) ? "+" : "-";
  const u = kind === "+" ? t : s ^ gfMul(kind === "0" ? zeta : omega, t ^ s);
  return enc(z, u);
}

function buildEdges(target) {
  const edges = [];
  for (let row = 0; row < N; row++) {
    let from = -1;
    for (let x = 0; x < N; x++) {
      if (op(row, x) === target) {
        from = x;
        break;
      }
    }
    edges.push({ row, from, to: op(row, target) });
  }
  return edges;
}

function coreEdges(edges) {
  const incident = new Map();
  const alive = new Set(edges.map((_, i) => i));

  function addInc(v, i) {
    if (!incident.has(v)) incident.set(v, new Set());
    incident.get(v).add(i);
  }

  for (let i = 0; i < edges.length; i++) {
    addInc(edges[i].from, i);
    addInc(edges[i].to, i);
  }

  const queue = [];
  for (const [v, set] of incident.entries()) {
    if (set.size <= 1) queue.push(v);
  }

  while (queue.length) {
    const v = queue.pop();
    const set = incident.get(v);
    if (!set || set.size > 1) continue;
    for (const i of Array.from(set)) {
      if (!alive.has(i)) continue;
      alive.delete(i);
      for (const u of [edges[i].from, edges[i].to]) {
        const uset = incident.get(u);
        if (!uset) continue;
        uset.delete(i);
        if (uset.size <= 1) queue.push(u);
      }
    }
  }

  return Array.from(alive).map((i) => edges[i]);
}

function summarizeTarget(target) {
  const edges = buildEdges(target);
  const core = coreEdges(edges);
  const allStats = degreeStats(edges);
  const coreStats = degreeStats(core);
  return {
    target,
    allEdges: edges.length,
    coreEdges: core.length,
    allVertices: allStats.vertices,
    coreVertices: coreStats.vertices,
    allCrossedGe2: allStats.crossedGe2,
    pureIncomingGe2: coreStats.pureIncomingGe2,
    pureOutgoingGe2: coreStats.pureOutgoingGe2,
    crossedGe2: coreStats.crossedGe2,
    mixed: coreStats.mixed,
    hist: coreStats.hist,
  };
}

function degreeStats(edges) {
  const vertices = new Set();
  const indeg = new Map();
  const outdeg = new Map();
  for (const e of edges) {
    vertices.add(e.from);
    vertices.add(e.to);
    outdeg.set(e.from, (outdeg.get(e.from) || 0) + 1);
    indeg.set(e.to, (indeg.get(e.to) || 0) + 1);
  }
  const hist = new Map();
  let pureIncomingGe2 = 0;
  let pureOutgoingGe2 = 0;
  let crossedGe2 = 0;
  let mixed = 0;
  for (const v of vertices) {
    const i = indeg.get(v) || 0;
    const o = outdeg.get(v) || 0;
    const key = `${i},${o}`;
    hist.set(key, (hist.get(key) || 0) + 1);
    if (i >= 2 && o === 0) pureIncomingGe2++;
    if (o >= 2 && i === 0) pureOutgoingGe2++;
    if (i >= 2 && o >= 2) crossedGe2++;
    if (i > 0 && o > 0) mixed++;
  }
  return {
    vertices: vertices.size,
    pureIncomingGe2,
    pureOutgoingGe2,
    crossedGe2,
    mixed,
    hist: Array.from(hist.entries()).sort(),
  };
}

function main() {
  const targets =
    process.argv[2] === "all"
      ? Array.from({ length: N }, (_, i) => i)
      : [0, 1, 17, 31, 255, 495];
  let crossedTargets = 0;
  let crossedVertices = 0;
  let allCrossedTargets = 0;
  let allCrossedVertices = 0;
  let maxCoreEdges = 0;
  for (const target of targets) {
    const summary = summarizeTarget(target);
    crossedVertices += summary.crossedGe2;
    if (summary.crossedGe2 > 0) crossedTargets++;
    allCrossedVertices += summary.allCrossedGe2;
    if (summary.allCrossedGe2 > 0) allCrossedTargets++;
    maxCoreEdges = Math.max(maxCoreEdges, summary.coreEdges);
    if (process.argv[2] !== "all" || summary.crossedGe2 > 0 || summary.allCrossedGe2 > 0) {
      console.log(JSON.stringify(summary));
    }
  }
  if (process.argv[2] === "all") {
    console.log(
      JSON.stringify({
        targets: targets.length,
        crossedTargets,
        crossedVertices,
        allCrossedTargets,
        allCrossedVertices,
        maxCoreEdges,
      })
    );
  }
}

main();
