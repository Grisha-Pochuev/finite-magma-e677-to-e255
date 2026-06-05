"use strict";

function mod(a, p) {
  a %= p;
  return a < 0 ? a + p : a;
}

function isPrime(n) {
  if (n < 2) return false;
  for (let d = 2; d * d <= n; d++) {
    if (n % d === 0) return false;
  }
  return true;
}

function checkPrime(p) {
  const out = [];
  for (let A = 0; A < p; A++) {
    for (let B = 1; B < p; B++) {
      const e677a = mod(A * B * (1 + B * B) - 1, p) === 0;
      const e677b = mod(A + A * A * B * B + B * B * B, p) === 0;
      if (!e677a || !e677b) continue;

      const idempotent = mod(A + B, p) === 1;
      const e255 = mod(A * A * A + A * A * B + A * B + B - 1, p) === 0;
      const sigmaCoeff = mod(A * A + A * B + B, p);
      out.push({ A, B, idempotent, e255, sigmaCoeff });
    }
  }
  return out;
}

const limit = Number(process.argv[2] || 101);
for (let p = 2; p <= limit; p++) {
  if (!isPrime(p)) continue;
  const models = checkPrime(p);
  if (models.length === 0) continue;
  console.log(`F_${p}:`);
  for (const model of models) {
    console.log(
      `  x*y=${model.A}x+${model.B}y, idempotent=${model.idempotent}, E255=${model.e255}, sigma=${model.sigmaCoeff}x`
    );
  }
}

