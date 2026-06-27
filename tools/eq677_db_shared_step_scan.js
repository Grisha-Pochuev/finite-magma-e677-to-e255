"use strict";

// Narrow scanner for the external memoryleak47/eq677 db models.
//
// It checks the current shared-step anchored triangle frontier:
//
//   p*b = q*b = z
//   U = p*z, W = q*z
//   h = U*p = W*q
//   z*h = b
//   target test: U*h = W*h
//
// The script does not clone the external repository.  With --refresh it
// downloads only selected db files into a local cache.

const fs = require("fs");
const path = require("path");
const https = require("https");

const REPO = "https://api.github.com/repos/memoryleak47/eq677";
const RAW = "https://raw.githubusercontent.com/memoryleak47/eq677/main";
const DEFAULT_CACHE = path.join("cache", "eq677-db");

function parseArgs(argv) {
  const args = {
    cache: DEFAULT_CACHE,
    sizes: ["5", "7", "9", "11", "13", "16", "19", "21"],
    refresh: false,
    all: false,
    maxPairsPerModel: Infinity,
    summaryOnly: false,
    totalsOnly: false,
  };
  for (const arg of argv) {
    if (arg === "--refresh") args.refresh = true;
    else if (arg === "--all") args.all = true;
    else if (arg.startsWith("--sizes=")) {
      args.sizes = arg.slice("--sizes=".length).split(",").filter(Boolean);
    } else if (arg.startsWith("--cache=")) {
      args.cache = arg.slice("--cache=".length);
    } else if (arg.startsWith("--max-pairs-per-model=")) {
      args.maxPairsPerModel = Number(arg.slice("--max-pairs-per-model=".length));
    } else if (arg === "--summary-only") {
      args.summaryOnly = true;
    } else if (arg === "--totals-only") {
      args.totalsOnly = true;
    } else if (arg === "--help") {
      printHelp();
      process.exit(0);
    } else {
      throw new Error(`Unknown argument: ${arg}`);
    }
  }
  return args;
}

function printHelp() {
  console.log(`Usage:
  node tools/eq677_db_shared_step_scan.js [--refresh] [--sizes=5,7,9] [--all]

Options:
  --refresh                download selected db files into cache/eq677-db
  --sizes=5,7,9            comma-separated model sizes to scan
  --all                    with --refresh, scan all available db sizes
  --max-pairs-per-model=N  cap pair scan for a smoke test
  --summary-only           print aggregate and failing models only
  --totals-only            print aggregate only
`);
}

function get(url) {
  return new Promise((resolve, reject) => {
    const req = https.get(
      url,
      {
        headers: {
          "User-Agent": "codex-e677-db-shared-step-scan",
          Accept: "application/vnd.github+json,text/plain",
        },
      },
      (res) => {
        if (res.statusCode >= 300 && res.statusCode < 400 && res.headers.location) {
          resolve(get(res.headers.location));
          return;
        }
        if (res.statusCode !== 200) {
          reject(new Error(`GET ${url} -> ${res.statusCode}`));
          res.resume();
          return;
        }
        const chunks = [];
        res.on("data", (chunk) => chunks.push(chunk));
        res.on("end", () => resolve(Buffer.concat(chunks).toString("utf8")));
      }
    );
    req.on("error", reject);
  });
}

async function refreshCache(cacheDir, sizes, all) {
  fs.mkdirSync(cacheDir, { recursive: true });
  let wantedSizes = sizes;
  if (all) {
    const root = JSON.parse(await get(`${REPO}/contents/db?ref=main`));
    wantedSizes = root
      .filter((x) => x.type === "dir")
      .map((x) => x.name)
      .sort((a, b) => Number(a) - Number(b));
  }

  for (const size of wantedSizes) {
    const dir = path.join(cacheDir, size);
    fs.mkdirSync(dir, { recursive: true });
    const entries = JSON.parse(await get(`${REPO}/contents/db/${size}?ref=main`));
    for (const entry of entries) {
      if (entry.type !== "file") continue;
      const target = path.join(dir, entry.name);
      if (fs.existsSync(target) && fs.statSync(target).size === entry.size) continue;
      const text = await get(`${RAW}/db/${size}/${entry.name}`);
      fs.writeFileSync(target, text.replace(/\r\n/g, "\n"), "utf8");
    }
  }
  return wantedSizes;
}

function localModelFiles(cacheDir, sizes) {
  const out = [];
  for (const size of sizes) {
    const dir = path.join(cacheDir, String(size));
    if (!fs.existsSync(dir)) continue;
    for (const name of fs.readdirSync(dir)) {
      const file = path.join(dir, name);
      const stat = fs.statSync(file);
      if (stat.isFile() && stat.size > 0) out.push({ size: String(size), index: name, file });
    }
  }
  out.sort((a, b) => Number(a.size) - Number(b.size) || Number(a.index) - Number(b.index));
  return out;
}

function parseTable(text) {
  const rows = text
    .split(/\n/)
    .map((line) => line.trim())
    .filter(Boolean)
    .map((line) => line.split(/\s+/).map(Number));
  const n = rows.length;
  if (n === 0) throw new Error("empty model");
  for (const row of rows) {
    if (row.length !== n) throw new Error(`non-square table: row has ${row.length}, n=${n}`);
    for (const value of row) {
      if (!Number.isInteger(value) || value < 0 || value >= n) {
        throw new Error(`table value out of range: ${value}, n=${n}`);
      }
    }
  }
  return rows;
}

function permutationRows(table) {
  const n = table.length;
  for (let row = 0; row < n; row++) {
    const seen = new Uint8Array(n);
    for (let col = 0; col < n; col++) seen[table[row][col]]++;
    for (let x = 0; x < n; x++) if (seen[x] !== 1) return false;
  }
  return true;
}

function inverseRows(table) {
  const n = table.length;
  const inv = Array.from({ length: n }, () => new Int32Array(n).fill(-1));
  for (let row = 0; row < n; row++) {
    for (let col = 0; col < n; col++) inv[row][table[row][col]] = col;
  }
  return inv;
}

function isIdempotent(table) {
  for (let x = 0; x < table.length; x++) if (table[x][x] !== x) return false;
  return true;
}

function scanModel(table, maxPairsPerModel) {
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

  const result = {
    n,
    idempotent: isIdempotent(table),
    permutationRows: permutationRows(table),
    groupsWithSharedStep: 0,
    maxFiber: 0,
    sharedStepPairs: 0,
    scannedPairs: 0,
    hMismatch: 0,
    zhMismatch: 0,
    uWhMismatch: 0,
    uWhMismatchAllNamedDistinct: 0,
    uWhMismatchWithNamedCollision: 0,
    anchoredX3CleanTriple: 0,
    anchoredX3RoutedTriple: 0,
    secondLayerClean: 0,
    secondLayerRouted: 0,
    secondLayerFormulaFailures: 0,
    firstOrbitCleanSelfRepeat: 0,
    firstOrbitRouted: 0,
    firstOrbitNoEvent: 0,
    firstOrbitKindDepths: new Map(),
    cleanSelfRepeatSignatures: new Map(),
    period3AdvanceProfiles: new Map(),
    mismatchProfiles: new Map(),
    tripleProfiles: new Map(),
    secondLayerProfiles: new Map(),
    firstOrbitProfiles: new Map(),
    sameOutput: 0,
    examples: [],
  };

  for (const [key, rows] of groups) {
    if (rows.length < 2) continue;
    result.groupsWithSharedStep++;
    result.maxFiber = Math.max(result.maxFiber, rows.length);
    const b = Math.floor(key / n);
    const z = key % n;
    for (let i = 0; i < rows.length; i++) {
      for (let j = i + 1; j < rows.length; j++) {
        result.sharedStepPairs++;
        if (result.scannedPairs >= maxPairsPerModel) continue;
        result.scannedPairs++;
        const p = rows[i];
        const q = rows[j];
        const U = table[p][z];
        const W = table[q][z];
        const h1 = table[U][p];
        const h2 = table[W][q];
        if (h1 !== h2) {
          result.hMismatch++;
          addExample(result, { kind: "hMismatch", b, z, p, q, U, W, h1, h2 });
          continue;
        }
        const h = h1;
        if (table[z][h] !== b) {
          result.zhMismatch++;
          addExample(result, { kind: "zhMismatch", b, z, p, q, U, W, h, zh: table[z][h] });
        }
        const T = table[U][h];
        const S = table[W][h];
        if (T !== S) {
          result.uWhMismatch++;
          const alpha = inv[z][h];
          const profile = namedCollisionProfile({ b, z, p, q, U, W, h, T, S });
          const triple = anchoredX3TripleProfile({ p, q, alpha }, { T, S, b });
          if (profile === "all-distinct") result.uWhMismatchAllNamedDistinct++;
          else result.uWhMismatchWithNamedCollision++;
          if (triple === "triple-clean") result.anchoredX3CleanTriple++;
          else result.anchoredX3RoutedTriple++;
          result.mismatchProfiles.set(profile, (result.mismatchProfiles.get(profile) || 0) + 1);
          result.tripleProfiles.set(triple, (result.tripleProfiles.get(triple) || 0) + 1);
          let secondLayer = "not-clean-x3";
          if (triple === "triple-clean") {
            const second = secondLayerProfile(table, { b, z, p, q, U, W, h, alpha, T, S });
            secondLayer = second.profile;
            if (!second.formulasHold) result.secondLayerFormulaFailures++;
            if (second.profile === "second-layer-clean") result.secondLayerClean++;
            else result.secondLayerRouted++;
            result.secondLayerProfiles.set(second.profile, (result.secondLayerProfiles.get(second.profile) || 0) + 1);

            const firstEvent = firstSourceOrbitEvent(table, inv, { b, z, p, q, U, W, h, alpha, T, S });
            if (firstEvent.kind === "clean-self-repeat") result.firstOrbitCleanSelfRepeat++;
            else if (firstEvent.kind === "no-event") result.firstOrbitNoEvent++;
            else result.firstOrbitRouted++;
            const depthKey = `${firstEvent.kind}@${firstEvent.depth}`;
            result.firstOrbitKindDepths.set(depthKey, (result.firstOrbitKindDepths.get(depthKey) || 0) + 1);
            if (firstEvent.selfRepeatSignature) {
              result.cleanSelfRepeatSignatures.set(
                firstEvent.selfRepeatSignature,
                (result.cleanSelfRepeatSignatures.get(firstEvent.selfRepeatSignature) || 0) + 1
              );
              if (firstEvent.selfRepeatSignature.includes("z:3->0")) {
                const period3 = period3AnchoredAdvanceProfile(table, { b, z, h });
                result.period3AdvanceProfiles.set(
                  period3,
                  (result.period3AdvanceProfiles.get(period3) || 0) + 1
                );
              }
            }
            result.firstOrbitProfiles.set(firstEvent.profile, (result.firstOrbitProfiles.get(firstEvent.profile) || 0) + 1);
          }
          addExample(result, { kind: "uWhMismatch", b, z, p, q, U, W, h, alpha, T, S, triple, secondLayer });
        } else {
          result.sameOutput++;
        }
      }
    }
  }
  return result;
}

function namedCollisionProfile(named) {
  const byValue = new Map();
  for (const [name, value] of Object.entries(named)) {
    let names = byValue.get(value);
    if (names === undefined) byValue.set(value, (names = []));
    names.push(name);
  }
  const groups = [];
  for (const names of byValue.values()) {
    if (names.length > 1) groups.push(names.sort().join("="));
  }
  if (groups.length === 0) return "all-distinct";
  return groups.sort().join(";");
}

function anchoredX3TripleProfile(inputs, outputs) {
  const groups = [];
  const inputEntries = Object.entries(inputs);
  const outputEntries = Object.entries(outputs);

  for (let i = 0; i < inputEntries.length; i++) {
    for (let j = i + 1; j < inputEntries.length; j++) {
      if (inputEntries[i][1] === inputEntries[j][1]) {
        groups.push(`input:${inputEntries[i][0]}=${inputEntries[j][0]}`);
      }
    }
  }
  for (let i = 0; i < outputEntries.length; i++) {
    for (let j = i + 1; j < outputEntries.length; j++) {
      if (outputEntries[i][1] === outputEntries[j][1]) {
        groups.push(`output:${outputEntries[i][0]}=${outputEntries[j][0]}`);
      }
    }
  }
  for (const [iname, ivalue] of inputEntries) {
    for (const [oname, ovalue] of outputEntries) {
      if (ivalue === ovalue) groups.push(`cross:${iname}=${oname}`);
    }
  }
  if (groups.length === 0) return "triple-clean";
  return groups.sort().join(";");
}

function secondLayerProfile(table, named) {
  const { b, z, p, q, U, W, h, alpha, T, S } = named;
  const UT = table[U][T];
  const WS = table[W][S];
  const zb = table[z][b];
  const betaT = table[UT][U];
  const betaS = table[WS][W];
  const betaB = table[zb][z];
  const Th = table[T][h];
  const Sh = table[S][h];
  const bh = table[b][h];

  const formulasHold =
    table[T][betaT] === h &&
    table[S][betaS] === h &&
    table[b][betaB] === h;

  const inputs = { p, q, alpha, betaT, betaS, betaB };
  const outputs = { T, S, b, Th, Sh, bh };
  const profile = endpointProfile(inputs, outputs, "second-layer-clean");
  return { profile, formulasHold };
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

    const profile = firstEventProfileAtDepth(current, edges);
    if (profile !== null) {
      const onlySelfRepeat = profile.parts.length > 0 && profile.parts.every((x) => x.startsWith("self-source-repeat:"));
      return {
        kind: onlySelfRepeat ? "clean-self-repeat" : "routed",
        depth,
        profile: `${onlySelfRepeat ? "clean-self-repeat" : "routed"}@${depth}:${profile.parts.join("|")}`,
        selfRepeatSignature: onlySelfRepeat ? selfRepeatSignature(current, edges) : undefined,
      };
    }
    edges.push(...current);
  }

  return { kind: "no-event", depth: n + 1, profile: "no-event" };
}

function firstEventProfileAtDepth(current, previous) {
  const parts = [];
  const allPrevious = previous.slice();
  for (let i = 0; i < current.length; i++) {
    const edge = current[i];
    for (const old of allPrevious) compareSourceOrbitEdges(parts, edge, old);
    for (let j = 0; j < i; j++) compareSourceOrbitEdges(parts, edge, current[j]);
  }
  if (parts.length === 0) return null;
  return { parts: Array.from(new Set(parts)).sort() };
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

function period3AnchoredAdvanceProfile(table, named) {
  const { b, z, h } = named;
  const c = table[b][h];
  if (table[c][h] !== z) return "period3-return-failure";

  const targets = { z, b, c };
  const outputs = {
    Az: table[c][z],
    Ab: table[z][b],
    Ac: table[b][c],
  };

  const groups = [];
  const targetEntries = Object.entries(targets);
  const outputEntries = Object.entries(outputs);
  for (let i = 0; i < targetEntries.length; i++) {
    if (targetEntries[i][1] === h) groups.push(`target-input:${targetEntries[i][0]}=h`);
    for (let j = i + 1; j < targetEntries.length; j++) {
      if (targetEntries[i][1] === targetEntries[j][1]) {
        groups.push(`target:${targetEntries[i][0]}=${targetEntries[j][0]}`);
      }
    }
  }
  for (let i = 0; i < outputEntries.length; i++) {
    if (outputEntries[i][1] === h) groups.push(`output-input:${outputEntries[i][0]}=h`);
    for (let j = i + 1; j < outputEntries.length; j++) {
      if (outputEntries[i][1] === outputEntries[j][1]) {
        groups.push(`output:${outputEntries[i][0]}=${outputEntries[j][0]}`);
      }
    }
  }
  for (const [oname, ovalue] of outputEntries) {
    for (const [tname, tvalue] of targetEntries) {
      if (ovalue === tvalue) groups.push(`output-target:${oname}=${tname}`);
    }
  }
  if (groups.length === 0) return "period3-advance-clean";
  return groups.sort().join(";");
}

function compareSourceOrbitEdges(parts, a, b) {
  if (a.source === b.source) {
    if (a.orbit === b.orbit) parts.push(`self-source-repeat:${a.orbit}`);
    else parts.push(`cross-source:${a.orbit}=${b.orbit}`);
  }
  if (a.output === b.output && a.source !== b.source) {
    parts.push(`output-merge:${a.orbit}=${b.orbit}`);
  }
  if (a.input === b.input && a.source !== b.source) {
    parts.push(`input-repeat:${a.orbit}=${b.orbit}`);
  }
  if (a.input === b.output) {
    parts.push(`input-output:${a.orbit}.input=${b.orbit}.output`);
  }
  if (a.output === b.input) {
    parts.push(`input-output:${a.orbit}.output=${b.orbit}.input`);
  }
}

function endpointProfile(inputs, outputs, cleanName) {
  const groups = [];
  const inputEntries = Object.entries(inputs);
  const outputEntries = Object.entries(outputs);

  for (let i = 0; i < inputEntries.length; i++) {
    for (let j = i + 1; j < inputEntries.length; j++) {
      if (inputEntries[i][1] === inputEntries[j][1]) {
        groups.push(`input:${inputEntries[i][0]}=${inputEntries[j][0]}`);
      }
    }
  }
  for (let i = 0; i < outputEntries.length; i++) {
    for (let j = i + 1; j < outputEntries.length; j++) {
      if (outputEntries[i][1] === outputEntries[j][1]) {
        groups.push(`output:${outputEntries[i][0]}=${outputEntries[j][0]}`);
      }
    }
  }
  for (const [iname, ivalue] of inputEntries) {
    for (const [oname, ovalue] of outputEntries) {
      if (ivalue === ovalue) groups.push(`cross:${iname}=${oname}`);
    }
  }
  if (groups.length === 0) return cleanName;
  return groups.sort().join(";");
}

function addExample(result, example) {
  if (result.examples.length < 8) result.examples.push(example);
}

function aggregate(results) {
  const total = {
    models: results.length,
    idempotentModels: 0,
    nonIdempotentModels: 0,
    groupsWithSharedStep: 0,
    sharedStepPairs: 0,
    scannedPairs: 0,
    hMismatch: 0,
    zhMismatch: 0,
    uWhMismatch: 0,
    uWhMismatchAllNamedDistinct: 0,
    uWhMismatchWithNamedCollision: 0,
    anchoredX3CleanTriple: 0,
    anchoredX3RoutedTriple: 0,
    secondLayerClean: 0,
    secondLayerRouted: 0,
    secondLayerFormulaFailures: 0,
    firstOrbitCleanSelfRepeat: 0,
    firstOrbitRouted: 0,
    firstOrbitNoEvent: 0,
    firstOrbitKindDepths: {},
    cleanSelfRepeatSignatures: {},
    period3AdvanceProfiles: {},
    mismatchProfiles: {},
    tripleProfiles: {},
    secondLayerProfiles: {},
    firstOrbitProfiles: {},
    sameOutput: 0,
    modelsWithFailure: [],
  };
  for (const r of results) {
    if (r.idempotent) total.idempotentModels++;
    else total.nonIdempotentModels++;
    total.groupsWithSharedStep += r.groupsWithSharedStep;
    total.sharedStepPairs += r.sharedStepPairs;
    total.scannedPairs += r.scannedPairs;
    total.hMismatch += r.hMismatch;
    total.zhMismatch += r.zhMismatch;
    total.uWhMismatch += r.uWhMismatch;
    total.uWhMismatchAllNamedDistinct += r.uWhMismatchAllNamedDistinct;
    total.uWhMismatchWithNamedCollision += r.uWhMismatchWithNamedCollision;
    total.anchoredX3CleanTriple += r.anchoredX3CleanTriple;
    total.anchoredX3RoutedTriple += r.anchoredX3RoutedTriple;
    total.secondLayerClean += r.secondLayerClean;
    total.secondLayerRouted += r.secondLayerRouted;
    total.secondLayerFormulaFailures += r.secondLayerFormulaFailures;
    total.firstOrbitCleanSelfRepeat += r.firstOrbitCleanSelfRepeat;
    total.firstOrbitRouted += r.firstOrbitRouted;
    total.firstOrbitNoEvent += r.firstOrbitNoEvent;
    for (const [profile, count] of r.firstOrbitKindDepths.entries()) {
      total.firstOrbitKindDepths[profile] = (total.firstOrbitKindDepths[profile] || 0) + count;
    }
    for (const [profile, count] of r.cleanSelfRepeatSignatures.entries()) {
      total.cleanSelfRepeatSignatures[profile] = (total.cleanSelfRepeatSignatures[profile] || 0) + count;
    }
    for (const [profile, count] of r.period3AdvanceProfiles.entries()) {
      total.period3AdvanceProfiles[profile] = (total.period3AdvanceProfiles[profile] || 0) + count;
    }
    for (const [profile, count] of r.mismatchProfiles.entries()) {
      total.mismatchProfiles[profile] = (total.mismatchProfiles[profile] || 0) + count;
    }
    for (const [profile, count] of r.tripleProfiles.entries()) {
      total.tripleProfiles[profile] = (total.tripleProfiles[profile] || 0) + count;
    }
    for (const [profile, count] of r.secondLayerProfiles.entries()) {
      total.secondLayerProfiles[profile] = (total.secondLayerProfiles[profile] || 0) + count;
    }
    for (const [profile, count] of r.firstOrbitProfiles.entries()) {
      total.firstOrbitProfiles[profile] = (total.firstOrbitProfiles[profile] || 0) + count;
    }
    total.sameOutput += r.sameOutput;
    if (r.hMismatch || r.zhMismatch || r.uWhMismatch) {
      total.modelsWithFailure.push({
        name: r.name,
        n: r.n,
        idempotent: r.idempotent,
        hMismatch: r.hMismatch,
        zhMismatch: r.zhMismatch,
        uWhMismatch: r.uWhMismatch,
        uWhMismatchAllNamedDistinct: r.uWhMismatchAllNamedDistinct,
        uWhMismatchWithNamedCollision: r.uWhMismatchWithNamedCollision,
        anchoredX3CleanTriple: r.anchoredX3CleanTriple,
        anchoredX3RoutedTriple: r.anchoredX3RoutedTriple,
        secondLayerClean: r.secondLayerClean,
        secondLayerRouted: r.secondLayerRouted,
        secondLayerFormulaFailures: r.secondLayerFormulaFailures,
        firstOrbitCleanSelfRepeat: r.firstOrbitCleanSelfRepeat,
        firstOrbitRouted: r.firstOrbitRouted,
        firstOrbitNoEvent: r.firstOrbitNoEvent,
        topFirstOrbitKindDepths: topEntries(r.firstOrbitKindDepths, 8),
        topCleanSelfRepeatSignatures: topEntries(r.cleanSelfRepeatSignatures, 8),
        topPeriod3AdvanceProfiles: topEntries(r.period3AdvanceProfiles, 8),
        topMismatchProfiles: topEntries(r.mismatchProfiles, 8),
        topTripleProfiles: topEntries(r.tripleProfiles, 8),
        topSecondLayerProfiles: topEntries(r.secondLayerProfiles, 8),
        topFirstOrbitProfiles: topEntries(r.firstOrbitProfiles, 8),
        examples: r.examples,
      });
    }
  }
  total.topMismatchProfiles = topEntries(new Map(Object.entries(total.mismatchProfiles)), 12);
  total.topTripleProfiles = topEntries(new Map(Object.entries(total.tripleProfiles)), 12);
  total.topSecondLayerProfiles = topEntries(new Map(Object.entries(total.secondLayerProfiles)), 12);
  total.topFirstOrbitKindDepths = topEntries(new Map(Object.entries(total.firstOrbitKindDepths)), 12);
  total.topCleanSelfRepeatSignatures = topEntries(new Map(Object.entries(total.cleanSelfRepeatSignatures)), 12);
  total.topPeriod3AdvanceProfiles = topEntries(new Map(Object.entries(total.period3AdvanceProfiles)), 12);
  total.topFirstOrbitProfiles = topEntries(new Map(Object.entries(total.firstOrbitProfiles)), 12);
  return total;
}

function topEntries(map, limit) {
  return Array.from(map.entries())
    .sort((a, b) => Number(b[1]) - Number(a[1]) || String(a[0]).localeCompare(String(b[0])))
    .slice(0, limit)
    .map(([profile, count]) => ({ profile, count: Number(count) }));
}

async function main() {
  const args = parseArgs(process.argv.slice(2));
  let sizes = args.sizes;
  if (args.refresh) sizes = await refreshCache(args.cache, args.sizes, args.all);
  if (args.all && !args.refresh) {
    sizes = fs.existsSync(args.cache)
      ? fs.readdirSync(args.cache).filter((x) => /^\d+$/.test(x))
      : [];
  }

  const files = localModelFiles(args.cache, sizes);
  if (files.length === 0) {
    throw new Error(
      `No cached model files found. Run with --refresh, for example: --refresh --sizes=${args.sizes.join(",")}`
    );
  }

  const results = [];
  for (const item of files) {
    const table = parseTable(fs.readFileSync(item.file, "utf8"));
    const r = scanModel(table, args.maxPairsPerModel);
    r.name = `${item.size}/${item.index}`;
    results.push(r);
  }

  const summary = aggregate(results);
  const compactSummary = { ...summary };
  delete compactSummary.modelsWithFailure;
  delete compactSummary.mismatchProfiles;
  delete compactSummary.tripleProfiles;
  delete compactSummary.secondLayerProfiles;
  delete compactSummary.firstOrbitProfiles;
  delete compactSummary.firstOrbitKindDepths;
  delete compactSummary.cleanSelfRepeatSignatures;
  delete compactSummary.period3AdvanceProfiles;
  const payload = args.totalsOnly
    ? { cache: args.cache, sizes, summary: compactSummary }
    : args.summaryOnly
    ? { cache: args.cache, sizes, summary, failingModels: summary.modelsWithFailure }
    : { cache: args.cache, sizes, summary, models: results };
  console.log(JSON.stringify(payload, null, 2));
}

main().catch((err) => {
  console.error(err && err.stack ? err.stack : String(err));
  process.exit(1);
});
