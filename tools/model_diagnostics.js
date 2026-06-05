"use strict";

function mod(a, p) {
  a %= p;
  return a < 0 ? a + p : a;
}

function linearTable(p, A, B) {
  return Array.from({ length: p }, (_, y) =>
    Array.from({ length: p }, (_, x) => mod(A * y + B * x, p))
  );
}

function checkE677(table) {
  const n = table.length;
  for (let x = 0; x < n; x++) {
    for (let y = 0; y < n; y++) {
      const rhs = table[y][table[x][table[table[y][x]][y]]];
      if (rhs !== x) return false;
    }
  }
  return true;
}

function checkE255(table) {
  const n = table.length;
  for (let x = 0; x < n; x++) {
    if (table[table[table[x][x]][x]][x] !== x) return false;
  }
  return true;
}

function fixedCountHistogram(table, mapBuilder) {
  const n = table.length;
  const histogram = new Map();
  let min = Infinity;
  let max = 0;
  for (let x = 0; x < n; x++) {
    let count = 0;
    for (let y = 0; y < n; y++) {
      if (mapBuilder(x, y) === y) count++;
    }
    min = Math.min(min, count);
    max = Math.max(max, count);
    histogram.set(count, (histogram.get(count) || 0) + 1);
  }
  return {
    min,
    max,
    histogram: Array.from(histogram.entries()).sort((a, b) => a[0] - b[0]),
  };
}

function diagnostics(name, table) {
  console.log(name);
  console.log(`  size=${table.length}, E677=${checkE677(table)}, E255=${checkE255(table)}`);
  console.log(
    `  self-orbit length under L_x: ${JSON.stringify(selfOrbitHistogram(table))}`
  );
  console.log(
    `  fixed y*x=x: ${JSON.stringify(
      fixedCountHistogram(table, (x, y) => table[y][x])
    )}`
  );
  console.log(
    `  fixed x*(y*y)=y: ${JSON.stringify(
      fixedCountHistogram(table, (x, y) => table[x][table[y][y]])
    )}`
  );
  console.log(
    `  fixed (x*y)*x=y: ${JSON.stringify(
      fixedCountHistogram(table, (x, y) => table[table[x][y]][x])
    )}`
  );
  console.log(
    `  fixed x*(y*x)=y: ${JSON.stringify(
      fixedCountHistogram(table, (x, y) => table[x][table[y][x]])
    )}`
  );
}

function selfOrbitHistogram(table) {
  const n = table.length;
  const histogram = new Map();
  const bad = [];
  for (let x = 0; x < n; x++) {
    let cur = x;
    let length = 0;
    do {
      cur = table[x][cur];
      length++;
      if (length > n) throw new Error("row is not a permutation");
    } while (cur !== x);
    histogram.set(length, (histogram.get(length) || 0) + 1);
    if (length === 4) bad.push(x);
  }
  return {
    histogram: Array.from(histogram.entries()).sort((a, b) => a[0] - b[0]),
    length4Examples: bad.slice(0, 10),
  };
}

diagnostics("linear F_5: x*y=2x+4y", linearTable(5, 2, 4));
diagnostics("linear F_7: x*y=4x+y", linearTable(7, 4, 1));
diagnostics("linear F_7: x*y=4x+3y", linearTable(7, 4, 3));
diagnostics("linear F_13: x*y=9x+11y", linearTable(13, 9, 11));
