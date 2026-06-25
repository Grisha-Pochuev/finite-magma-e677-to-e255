"use strict";

// Targeted diagnostic for mixed_junction_target_swap_bridge_square.md.
// It samples outgoing-majority mixed 2+1 junctions in the known M496 model
// and checks whether the two target-swap bridges h=pred_b(v) and j=pred_v(b)
// satisfy simple coincidences. It also checks the paired right-fixer candidates
// from double_outgoing_mixed_witness_candidate.md. This is not a proof.

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

function op7(a, b) {
  return mod(4 * a + b, 7);
}

function pack(a7, a496) {
  return a7 * N + a496;
}

function first7(x) {
  return Math.floor(x / N);
}

function second496(x) {
  return x % N;
}

function opProduct(a, b) {
  return pack(op7(first7(a), first7(b)), op(second496(a), second496(b)));
}

function buildGraph(target) {
  const edges = [];
  const out = new Map();
  const incoming = new Map();
  for (let q = 0; q < N; q++) {
    let a = -1;
    for (let x = 0; x < N; x++) {
      if (op(q, x) === target) {
        a = x;
        break;
      }
    }
    const c = op(q, target);
    const edge = { q, a, c };
    edges.push(edge);
    if (!out.has(a)) out.set(a, []);
    if (!incoming.has(c)) incoming.set(c, []);
    out.get(a).push(edge);
    incoming.get(c).push(edge);
  }
  return { edges, out, incoming };
}

function edgeExists(graph, a, c) {
  const list = graph.out.get(a) || [];
  return list.some((edge) => edge.c === c);
}

function liftMixedSampleToProduct(sample, index) {
  const b7 = index % 7;
  const p7 = 1 + (index % 6);
  const r7 = mod(-p7, 7);
  const v7 = mod(b7 - 4 * p7, 7);
  const c7 = op7(p7, b7);
  const a7 = mod(b7 - 4 * r7, 7);
  return {
    b: pack(b7, sample.b),
    v: pack(v7, sample.v),
    p: pack(p7, sample.p),
    q: pack(p7, sample.q),
    r: pack(r7, sample.r),
    a: pack(a7, sample.a),
    c: pack(c7, sample.c),
    d: pack(c7, sample.d),
  };
}

function auditMixedSamples(samples, opFn) {
  const counters = {
    validSetup: 0,
    yCRightFixesB: 0,
    yDRightFixesB: 0,
    yCEqualsB: 0,
    yDEqualsB: 0,
    yCEqualsYD: 0,
    yCEqualsCanonical: 0,
    yDEqualsCanonical: 0,
    canonicalRightFixesB: 0,
    yCFixesV: 0,
    yCFixesA: 0,
    yCFixesC: 0,
    yCFixesD: 0,
    yCFixesS: 0,
    yCFixesJ: 0,
    bcTimesSEqualsR: 0,
    bdTimesSEqualsR: 0,
    bcTimesJEqualsA: 0,
    bdTimesJEqualsA: 0,
    suffixEqualsBInverseOfB: 0,
  };
  const firstFailure = {};
  for (const sample of samples) {
    const { b, v, p, q, r, a, c, d } = sample;
    const validSetup =
      opFn(p, v) === b &&
      opFn(p, b) === c &&
      opFn(q, v) === b &&
      opFn(q, b) === d &&
      opFn(r, a) === b &&
      opFn(r, b) === v;
    if (validSetup) counters.validSetup++;

    const s = opFn(r, v);
    const j = opFn(s, r);
    const suffix = opFn(s, j);
    const bc = opFn(b, c);
    const bd = opFn(b, d);
    const yC = opFn(bc, suffix);
    const yD = opFn(bd, suffix);
    const canonical = opFn(opFn(b, b), b);
    const bInverseUnderBc = opFn(b, opFn(opFn(bc, b), bc));
    const checks = {
      yCRightFixesB: opFn(yC, b) === b,
      yDRightFixesB: opFn(yD, b) === b,
      yCEqualsB: yC === b,
      yDEqualsB: yD === b,
      yCEqualsYD: yC === yD,
      yCEqualsCanonical: yC === canonical,
      yDEqualsCanonical: yD === canonical,
      canonicalRightFixesB: opFn(canonical, b) === b,
      yCFixesV: opFn(yC, v) === v,
      yCFixesA: opFn(yC, a) === a,
      yCFixesC: opFn(yC, c) === c,
      yCFixesD: opFn(yC, d) === d,
      yCFixesS: opFn(yC, s) === s,
      yCFixesJ: opFn(yC, j) === j,
      bcTimesSEqualsR: opFn(bc, s) === r,
      bdTimesSEqualsR: opFn(bd, s) === r,
      bcTimesJEqualsA: opFn(bc, j) === a,
      bdTimesJEqualsA: opFn(bd, j) === a,
      suffixEqualsBInverseOfB: suffix === bInverseUnderBc,
    };
    for (const [name, ok] of Object.entries(checks)) {
      if (ok) {
        counters[name]++;
      } else if (!firstFailure[name]) {
        firstFailure[name] = {
          b,
          v,
          p,
          q,
          r,
          a,
          c,
          d,
          s,
          j,
          suffix,
          bc,
          bd,
          yC,
          yD,
          canonical,
          yCb: opFn(yC, b),
          yDb: opFn(yD, b),
          bInverseUnderBc,
          bcTimesS: opFn(bc, s),
          bcTimesJ: opFn(bc, j),
        };
      }
    }
  }
  return { counters, firstFailure };
}

function main() {
  const targets = [0, 1, 17, 31, 255, 495];
  const perTargetLimit = 50;
  let total = 0;
  const counters = {
    hEqualsJ: 0,
    hRightFixesB: 0,
    jRightFixesB: 0,
    edgeHtoJ: 0,
    edgeJtoH: 0,
    yCRightFixesB: 0,
    yDRightFixesB: 0,
    bothYRightFixB: 0,
    pairedImagesEqual: 0,
    yCEqualsYD: 0,
    yCEqualsCanonical: 0,
    yDEqualsCanonical: 0,
    suffixEqualsH: 0,
    suffixEqualsJ: 0,
    suffixEqualsB: 0,
    bcEqualsBD: 0,
    bcRightFixesB: 0,
    bdRightFixesB: 0,
    bcTimesJEqualsA: 0,
    bdTimesJEqualsA: 0,
    bcTimesSEqualsR: 0,
    bdTimesSEqualsR: 0,
    suffixEqualsBInverseOfB: 0,
  };
  const examples = [];
  const junctionSamples = [];
  const exampleTargets = new Set();

  for (const b of targets) {
    let targetTotal = 0;
    const graph = buildGraph(b);
    for (const [v, outs] of graph.out.entries()) {
      const ins = graph.incoming.get(v) || [];
      if (outs.length < 2 || ins.length < 1) continue;
      for (let i = 0; i < outs.length && targetTotal < perTargetLimit; i++) {
        for (let j0 = i + 1; j0 < outs.length && targetTotal < perTargetLimit; j0++) {
          for (const incoming of ins) {
            if (targetTotal >= perTargetLimit) break;
            const p = outs[i].q;
            const q = outs[j0].q;
            const c = outs[i].c;
            const d = outs[j0].c;
            const r = incoming.q;
            const a = incoming.a;
            junctionSamples.push({ b, v, p, q, r, a, c, d });
            const h = op(c, p);
            const h2 = op(d, q);
            if (h !== h2 || op(b, h) !== v) throw new Error("bad h bridge");
            const s = op(r, v);
            const jj = op(s, r);
            if (op(v, jj) !== b) throw new Error("bad j bridge");
            total++;
            targetTotal++;
            if (h === jj) counters.hEqualsJ++;
            if (op(h, b) === b) counters.hRightFixesB++;
            if (op(jj, b) === b) counters.jRightFixesB++;
            if (edgeExists(graph, h, jj)) counters.edgeHtoJ++;
            if (edgeExists(graph, jj, h)) counters.edgeJtoH++;
            const suffix = op(s, jj);
            const bc = op(b, c);
            const bd = op(b, d);
            const yC = op(op(b, c), suffix);
            const yD = op(op(b, d), suffix);
            const yCb = op(yC, b);
            const yDb = op(yD, b);
            const canonical = op(op(b, b), b);
            if (yCb === b) counters.yCRightFixesB++;
            if (yDb === b) counters.yDRightFixesB++;
            if (yCb === b && yDb === b) counters.bothYRightFixB++;
            if (yCb === yDb) counters.pairedImagesEqual++;
            if (yC === yD) counters.yCEqualsYD++;
            if (yC === canonical) counters.yCEqualsCanonical++;
            if (yD === canonical) counters.yDEqualsCanonical++;
            if (suffix === h) counters.suffixEqualsH++;
            if (suffix === jj) counters.suffixEqualsJ++;
            if (suffix === b) counters.suffixEqualsB++;
            if (bc === bd) counters.bcEqualsBD++;
            if (op(bc, b) === b) counters.bcRightFixesB++;
            if (op(bd, b) === b) counters.bdRightFixesB++;
            if (op(bc, jj) === a) counters.bcTimesJEqualsA++;
            if (op(bd, jj) === a) counters.bdTimesJEqualsA++;
            if (op(bc, s) === r) counters.bcTimesSEqualsR++;
            if (op(bd, s) === r) counters.bdTimesSEqualsR++;
            const bInverseUnderBc = op(b, op(op(bc, b), bc));
            if (suffix === bInverseUnderBc) counters.suffixEqualsBInverseOfB++;
            if (!exampleTargets.has(b)) {
              exampleTargets.add(b);
              examples.push({
                b,
                v,
                p,
                q,
                r,
                a,
                c,
                d,
                h,
                s,
                j: jj,
                suffix,
                bInverseUnderBc,
                bc,
                bd,
                yC,
                yD,
                canonical,
                suffixTimes: {
                  b: op(suffix, b),
                  v: op(suffix, v),
                  p: op(suffix, p),
                  q: op(suffix, q),
                  r: op(suffix, r),
                  c: op(suffix, c),
                  d: op(suffix, d),
                },
                bcTimes: {
                  h: op(bc, h),
                  j: op(bc, jj),
                  s: op(bc, s),
                  b: op(bc, b),
                  v: op(bc, v),
                },
              });
            }
          }
        }
      }
    }
  }

  console.log("Mixed junction bridge-square diagnostic on M496");
  console.log(`sampled junctions: ${total}`);
  for (const [key, value] of Object.entries(counters)) {
    console.log(`${key}: ${value}`);
  }
  console.log(`first examples: ${JSON.stringify(examples)}`);

  const productSamples = junctionSamples.map(liftMixedSampleToProduct);
  const productAudit = auditMixedSamples(productSamples, opProduct);
  console.log("Lifted mixed junction diagnostic on F7 x M496");
  console.log(`sampled junctions: ${productSamples.length}`);
  for (const [key, value] of Object.entries(productAudit.counters)) {
    console.log(`${key}: ${value}`);
  }
  console.log(`first failures: ${JSON.stringify(productAudit.firstFailure)}`);
}

main();
