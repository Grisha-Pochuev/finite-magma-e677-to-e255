"use strict";

// Finite non-right-cancellative E677 example from the ETP blueprint.
// Carrier: F_31 x F_16.
// This script checks E677, E255, and right-cancellativity diagnostics.

const P = 31;

function mod31(x) {
  x %= P;
  return x < 0 ? x + P : x;
}

// GF(16) with primitive polynomial a^4 + a + 1.
function gfAdd(a, b) {
  return a ^ b;
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

function gfSub(a, b) {
  return gfAdd(a, b);
}

const primitive = 2;
const zeta = gfPow(primitive, 3); // order 5
const omega = gfPow(primitive, 5); // order 3

function gfOrder(a) {
  if (a === 0) return 0;
  let cur = 1;
  for (let i = 1; i <= 15; i++) {
    cur = gfMul(cur, a);
    if (cur === 1) return i;
  }
  return -1;
}

const residues = new Set();
for (let x = 1; x < P; x++) residues.add(mod31(x * x));

function baseOp(x, y) {
  return mod31(x - 2 * (y - x));
}

function fiberKind(x, y) {
  const d = mod31(y - x);
  if (d === 0) return "0";
  return residues.has(d) ? "+" : "-";
}

function fiberOp(kind, s, t) {
  if (kind === "+") return t;
  if (kind === "0") return gfSub(s, gfMul(zeta, gfSub(t, s)));
  return gfSub(s, gfMul(omega, gfSub(t, s)));
}

const N = P * 16;

function enc(x, s) {
  return x * 16 + s;
}

function dec(a) {
  return [Math.floor(a / 16), a & 15];
}

function op(a, b) {
  const [x, s] = dec(a);
  const [y, t] = dec(b);
  const z = baseOp(x, y);
  const u = fiberOp(fiberKind(x, y), s, t);
  return enc(z, u);
}

function checkE677() {
  for (let x = 0; x < N; x++) {
    for (let y = 0; y < N; y++) {
      const rhs = op(y, op(x, op(op(y, x), y)));
      if (rhs !== x) return { ok: false, x, y, rhs };
    }
  }
  return { ok: true };
}

function checkE255() {
  const failures = [];
  for (let x = 0; x < N; x++) {
    const rhs = op(op(op(x, x), x), x);
    if (rhs !== x) failures.push({ x, rhs });
  }
  return failures;
}

function rightCollisionStats() {
  let columnsWithCollision = 0;
  let maxMultiplicity = 1;
  let example = null;
  for (let x = 0; x < N; x++) {
    const seen = new Map();
    for (let y = 0; y < N; y++) {
      const value = op(y, x);
      const old = seen.get(value) || [];
      old.push(y);
      seen.set(value, old);
    }
    for (const [value, ys] of seen.entries()) {
      if (ys.length > 1) {
        columnsWithCollision++;
        if (ys.length > maxMultiplicity) {
          maxMultiplicity = ys.length;
          example = { column: x, value, rows: ys.slice(0, 10) };
        }
        break;
      }
    }
  }
  return { columnsWithCollision, maxMultiplicity, example };
}

function fixedPointStats() {
  let minSolutions = Infinity;
  let maxSolutions = 0;
  const histogram = new Map();
  for (let x = 0; x < N; x++) {
    let count = 0;
    for (let y = 0; y < N; y++) {
      if (op(y, x) === x) count++;
    }
    minSolutions = Math.min(minSolutions, count);
    maxSolutions = Math.max(maxSolutions, count);
    histogram.set(count, (histogram.get(count) || 0) + 1);
  }
  return {
    minSolutions,
    maxSolutions,
    histogram: Array.from(histogram.entries()).sort((a, b) => a[0] - b[0]),
  };
}

function sigma(x) {
  return op(op(x, x), x);
}

function sigmaStats() {
  const image = new Map();
  let fixed = 0;
  let e255WitnessFailures = 0;
  for (let x = 0; x < N; x++) {
    const y = sigma(x);
    if (y === x) fixed++;
    image.set(y, (image.get(y) || 0) + 1);
    if (op(y, x) !== x) e255WitnessFailures++;
  }
  const multiplicities = Array.from(image.values()).sort((a, b) => a - b);
  return {
    imageSize: image.size,
    fixed,
    minMultiplicity: multiplicities[0],
    maxMultiplicity: multiplicities[multiplicities.length - 1],
    e255WitnessFailures,
  };
}

function fixedPointHistogramForMap(mapBuilder) {
  let min = Infinity;
  let max = 0;
  const histogram = new Map();
  const examples = [];
  for (let x = 0; x < N; x++) {
    let count = 0;
    const ys = [];
    for (let y = 0; y < N; y++) {
      if (mapBuilder(x, y) === y) {
        count++;
        if (ys.length < 5) ys.push(y);
      }
    }
    min = Math.min(min, count);
    max = Math.max(max, count);
    histogram.set(count, (histogram.get(count) || 0) + 1);
    if (examples.length < 5) examples.push({ x, count, ys });
  }
  return {
    min,
    max,
    histogram: Array.from(histogram.entries()).sort((a, b) => a[0] - b[0]),
    examples,
  };
}

function collisionSeparationDiagnostics() {
  let checkedCollisions = 0;
  let separated = 0;
  let twistedEqualities = 0;
  let maxFiber = 0;
  let example = null;

  for (let x = 0; x < N; x++) {
    const fibers = new Map();
    for (let y = 0; y < N; y++) {
      const c = op(y, x);
      if (!fibers.has(c)) fibers.set(c, []);
      fibers.get(c).push(y);
    }
    for (const [c, ys] of fibers.entries()) {
      maxFiber = Math.max(maxFiber, ys.length);
      if (ys.length < 2) continue;
      if (!example) example = { x, c, ys: ys.slice(0, 20) };
      for (let i = 0; i < ys.length; i++) {
        for (let j = i + 1; j < ys.length; j++) {
          const y = ys[i];
          const z = ys[j];
          checkedCollisions++;
          if (op(y, c) !== op(z, c)) separated++;
          if (op(op(y, c), y) === op(op(z, c), z)) twistedEqualities++;
        }
      }
    }
  }

  return {
    checkedCollisions,
    separated,
    twistedEqualities,
    maxFiber,
    example,
  };
}

console.log(`GF(16) primitive=${primitive}, zeta=${zeta}, order(zeta)=${gfOrder(zeta)}, omega=${omega}, order(omega)=${gfOrder(omega)}`);
console.log(`carrier size: ${N}`);
const e677 = checkE677();
console.log(`E677: ${e677.ok ? "ok" : JSON.stringify(e677)}`);
const e255Failures = checkE255();
console.log(`E255 failures: ${e255Failures.length}`);
if (e255Failures.length) console.log(JSON.stringify(e255Failures.slice(0, 5)));
console.log(`right collision stats: ${JSON.stringify(rightCollisionStats())}`);
console.log(`fixed-point stats y*x=x: ${JSON.stringify(fixedPointStats())}`);
console.log(`sigma stats (sigma(x)=(x*x)*x): ${JSON.stringify(sigmaStats())}`);
console.log(`fixed x*(y*y)=y: ${JSON.stringify(fixedPointHistogramForMap((x, y) => op(x, op(y, y))))}`);
console.log(`fixed (x*y)*x=y: ${JSON.stringify(fixedPointHistogramForMap((x, y) => op(op(x, y), x)))}`);
console.log(`collision separation: ${JSON.stringify(collisionSeparationDiagnostics())}`);
