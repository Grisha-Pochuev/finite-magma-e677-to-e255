"use strict";

// Persistent diagnostic for the Directed Two-Edge Witness candidate.
//
// It reconstructs:
// - the known nonlinear E677 model of size 496 from the ETP blueprint;
// - the affine E677 model over F_7: y*x = 4y+x;
// - 144 product samples F_7 x M_496 with a directed path a -> v -> c in H_b;
// - the candidate Y=(b*c)*(u*k);
// - the depth <= 2 semantic synthesis audit for z with (b*z)*b=z.
//
// This script has no npm dependencies.

const P = 31;
const FIBER = 16;
const N496 = P * FIBER;
const NPRODUCT = 7 * N496;

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

const zeta = gfPow(2, 3); // order 5
const omega = gfPow(2, 5); // order 3
const residues31 = new Set();
for (let x = 1; x < P; x++) residues31.add(mod(x * x, P));

function enc496(x, s) {
  return x * FIBER + s;
}

function dec496(a) {
  return [Math.floor(a / FIBER), a & 15];
}

function baseOp31(x, y) {
  return mod(x - 2 * (y - x), P);
}

function fiberKind(x, y) {
  const d = mod(y - x, P);
  if (d === 0) return "0";
  return residues31.has(d) ? "+" : "-";
}

function fiberOp(kind, s, t) {
  if (kind === "+") return t;
  const multiplier = kind === "0" ? zeta : omega;
  return s ^ gfMul(multiplier, t ^ s);
}

function op496(a, b) {
  const [x, s] = dec496(a);
  const [y, t] = dec496(b);
  return enc496(baseOp31(x, y), fiberOp(fiberKind(x, y), s, t));
}

function op7(a, b) {
  return mod(4 * a + b, 7);
}

function pack(a7, a496) {
  return a7 * N496 + a496;
}

function first7(x) {
  return Math.floor(x / N496);
}

function second496(x) {
  return x % N496;
}

function opProduct(a, b) {
  return pack(op7(first7(a), first7(b)), op496(second496(a), second496(b)));
}

function checkE677(n, op) {
  for (let x = 0; x < n; x++) {
    for (let y = 0; y < n; y++) {
      if (op(y, op(x, op(op(y, x), y))) !== x) return false;
    }
  }
  return true;
}

function checkE255(n, op) {
  for (let x = 0; x < n; x++) {
    if (op(op(op(x, x), x), x) !== x) return false;
  }
  return true;
}

function buildBasePaths() {
  const targets = [0, 1, 17, 31, 255, 495];
  const out = [];
  for (const b of targets) {
    let count = 0;
    for (let p = 0; p < N496 && count < 24; p++) {
      const v = op496(p, b);
      for (let r = 0; r < N496; r++) {
        if (op496(r, v) !== b) continue;
        const c = op496(r, b);
        const u = op496(p, v);
        const k = op496(u, p);
        if (op496(v, k) !== b) {
          throw new Error("edge certificate failed in M496");
        }
        out.push({ b, v, p, r, c, u, k });
        count++;
        break;
      }
    }
  }
  return out;
}

function buildProductSamples(basePaths) {
  return basePaths.map((s, i) => {
    const b7 = 1 + (i % 6);
    const p7 = mod(2 * i + 3, 7);
    const v7 = op7(p7, b7);
    const r7 = mod(2 * (b7 - v7), 7);
    const c7 = op7(r7, b7);
    const u7 = op7(p7, v7);
    const k7 = op7(u7, p7);
    return {
      b: pack(b7, s.b),
      v: pack(v7, s.v),
      p: pack(p7, s.p),
      r: pack(r7, s.r),
      c: pack(c7, s.c),
      u: pack(u7, s.u),
      k: pack(k7, s.k),
    };
  });
}

function validateDirectedPath(samples, op) {
  return samples.every((s) =>
    op(s.p, s.b) === s.v &&
    op(s.r, s.v) === s.b &&
    op(s.r, s.b) === s.c &&
    op(s.p, s.v) === s.u &&
    op(s.u, s.p) === s.k &&
    op(s.v, s.k) === s.b
  );
}

function candidateY(s, op) {
  return op(op(s.b, s.c), op(s.u, s.k));
}

function leftPreimage(row, target, n, op) {
  for (let x = 0; x < n; x++) {
    if (op(row, x) === target) return x;
  }
  throw new Error(`no left preimage for row=${row}, target=${target}`);
}

function runRowLiftAudit(samples, n, op) {
  const counters = {
    BTimesUEqP: 0,
    BTimesKEqA: 0,
    suffixEqBInverseOfB: 0,
    BTimesSuffixEqB: 0,
    YEqualsB: 0,
    YEqualsCanonical: 0,
    canonicalRightFixesB: 0,
  };
  const firstFailure = {};

  for (const s of samples) {
    const a = leftPreimage(s.p, s.b, n, op);
    const B = op(s.b, s.c);
    const suffix = op(s.u, s.k);
    const y = op(B, suffix);
    const canonical = op(op(s.b, s.b), s.b);
    const bInverseUnderB = op(s.b, op(op(B, s.b), B));
    const checks = {
      BTimesUEqP: op(B, s.u) === s.p,
      BTimesKEqA: op(B, s.k) === a,
      suffixEqBInverseOfB: suffix === bInverseUnderB,
      BTimesSuffixEqB: op(B, suffix) === s.b,
      YEqualsB: y === s.b,
      YEqualsCanonical: y === canonical,
      canonicalRightFixesB: op(canonical, s.b) === s.b,
    };
    for (const [name, ok] of Object.entries(checks)) {
      if (ok) {
        counters[name]++;
      } else if (!firstFailure[name]) {
        firstFailure[name] = {
          b: s.b,
          p: s.p,
          r: s.r,
          a,
          v: s.v,
          c: s.c,
          u: s.u,
          k: s.k,
          B,
          y,
          canonical,
          suffix,
          bInverseUnderB,
          BTimesU: op(B, s.u),
          BTimesK: op(B, s.k),
          BTimesSuffix: op(B, suffix),
        };
      }
    }
  }

  return { counters, firstFailure };
}

function rightFixerToBalancedWitness(b, y, op) {
  const t = op(y, op(op(b, y), b));
  const z = op(t, b);
  return { t, z };
}

function runTermSynthesis(samples) {
  const names = ["b", "v", "p", "r", "c", "u", "k"];
  const termMap = new Map();
  const terms = [];
  for (let i = 0; i < names.length; i++) {
    const name = names[i];
    const vec = samples.map((s) => s[name]);
    const key = vec.join(",");
    if (termMap.has(key)) continue;
    const term = { expr: name, vec, depth: 0, mask: 1 << i };
    termMap.set(key, term);
    terms.push(term);
  }

  const witnesses = [];
  const isWitness = (vec) =>
    samples.every((s, i) => opProduct(opProduct(s.b, vec[i]), s.b) === vec[i]);

  const rounds = [];
  for (let targetDepth = 1; targetDepth <= 2; targetDepth++) {
    const prior = terms.slice();
    const fresh = [];
    for (const left of prior) {
      for (const right of prior) {
        const depth = 1 + Math.max(left.depth, right.depth);
        if (depth !== targetDepth) continue;
        const vec = left.vec.map((x, i) => opProduct(x, right.vec[i]));
        const key = vec.join(",");
        if (termMap.has(key)) continue;
        const term = {
          expr: `(${left.expr}*${right.expr})`,
          vec,
          depth,
          mask: left.mask | right.mask,
        };
        termMap.set(key, term);
        fresh.push(term);
        if ((term.mask & ~1) !== 0 && isWitness(vec)) witnesses.push(term.expr);
      }
    }
    terms.push(...fresh);
    rounds.push({ depth: targetDepth, fresh: fresh.length, total: terms.length });
  }
  return { rounds, witnesses };
}

function main() {
  console.log("Directed Two-Edge Witness diagnostics");
  console.log(`M496 parameters: zeta=${zeta}, omega=${omega}`);
  console.log(`F7 E677: ${checkE677(7, op7)}, E255: ${checkE255(7, op7)}`);
  console.log(`M496 E677: ${checkE677(N496, op496)}, E255: ${checkE255(N496, op496)}`);

  const basePaths = buildBasePaths();
  const productSamples = buildProductSamples(basePaths);
  console.log(`base directed paths: ${basePaths.length}`);
  console.log(`product samples: ${productSamples.length}`);
  console.log(`product path certificates: ${validateDirectedPath(productSamples, opProduct)}`);

  const baseRowLift = runRowLiftAudit(basePaths, N496, op496);
  console.log("base row-lift audit:");
  for (const [name, count] of Object.entries(baseRowLift.counters)) {
    console.log(`  ${name}: ${count}/${basePaths.length}`);
  }
  if (Object.keys(baseRowLift.firstFailure).length) {
    console.log(`  first failures: ${JSON.stringify(baseRowLift.firstFailure)}`);
  }

  const productRowLift = runRowLiftAudit(productSamples, NPRODUCT, opProduct);
  console.log("product row-lift audit:");
  for (const [name, count] of Object.entries(productRowLift.counters)) {
    console.log(`  ${name}: ${count}/${productSamples.length}`);
  }
  if (Object.keys(productRowLift.firstFailure).length) {
    console.log(`  first failures: ${JSON.stringify(productRowLift.firstFailure)}`);
  }

  const yRightFixes = productSamples.every((s) => opProduct(candidateY(s, opProduct), s.b) === s.b);
  console.log(`Y=(b*c)*(u*k) right-fixes b on product samples: ${yRightFixes}`);

  const conversionWorks = productSamples.every((s) => {
    const y = candidateY(s, opProduct);
    const { z } = rightFixerToBalancedWitness(s.b, y, opProduct);
    return opProduct(opProduct(s.b, z), s.b) === z;
  });
  console.log(`right-fixer -> balanced witness conversion works: ${conversionWorks}`);

  const synthesis = runTermSynthesis(productSamples);
  for (const round of synthesis.rounds) {
    console.log(
      `depth ${round.depth} synthesis: fresh=${round.fresh}, total=${round.total}`
    );
  }
  console.log(
    `depth<=2 path-dependent z witnesses: ${
      synthesis.witnesses.length ? synthesis.witnesses.join(", ") : "none"
    }`
  );

  if (!yRightFixes || !conversionWorks || synthesis.witnesses.length !== 0) {
    process.exitCode = 1;
  }
}

main();
