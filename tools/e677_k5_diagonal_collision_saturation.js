"use strict";

// Bounded ground-congruence diagnostic for two precise hand targets on the
// off-diagonal K5 periodic-port core: a0*a0=a1*a1 (default), or one row
// first-return whose length divides five (--row-five-cycle).
//
// Every equality produced below follows from the displayed K5 cells,
// E677, congruence, and injectivity of finite left translations.  Absence
// of a contradiction is only a bounded negative result.

const maxDepth = Number(process.argv[2] || 8);
const maxRounds = Number(process.argv[3] || 10);
const maxTerms = Number(process.argv[4] || 220000);
const rowFiveCycle = process.argv.includes("--row-five-cycle");

const K5 = [
  [0, 2, 1, 4, 3],
  [3, 1, 4, 0, 2],
  [4, 3, 2, 1, 0],
  [2, 4, 0, 3, 1],
  [1, 0, 3, 2, 4],
];

const terms = [];
const byKey = new Map();
const parent = [];
const rank = [];

function make(key, expr, depth, left = -1, right = -1) {
  if (byKey.has(key)) return byKey.get(key);
  if (terms.length >= maxTerms) throw new Error(`term cap ${maxTerms}`);
  const id = terms.length;
  byKey.set(key, id);
  terms.push({ id, key, expr, depth, left, right });
  parent.push(id);
  rank.push(0);
  return id;
}

function constant(name) {
  return make(name, name, 0);
}

function op(left, right) {
  if (left < 0 || right < 0) return -1;
  const depth = 1 + Math.max(terms[left].depth, terms[right].depth);
  if (depth > maxDepth) return -1;
  return make(
    `*(${left},${right})`,
    `(${terms[left].expr}*${terms[right].expr})`,
    depth,
    left,
    right,
  );
}

function find(id) {
  while (parent[id] !== id) {
    parent[id] = parent[parent[id]];
    id = parent[id];
  }
  return id;
}

function union(left, right) {
  if (left < 0 || right < 0) return false;
  let x = find(left), y = find(right);
  if (x === y) return false;
  if (rank[x] < rank[y]) [x, y] = [y, x];
  parent[y] = x;
  if (rank[x] === rank[y]) rank[x]++;
  return true;
}

function same(left, right) {
  return left >= 0 && right >= 0 && find(left) === find(right);
}

const a = [0, 1, 2, 3, 4].map((i) => constant(`a${i}`));
const assumptions = [];
for (let row = 0; row < 5; row++) {
  for (let input = 0; input < 5; input++) {
    if (row !== input) assumptions.push([op(a[row], a[input]), a[K5[row][input]]]);
  }
}
const diagonal = a.map((x) => op(x, x));
const rowPowers = [a[0]];
for (let i = 0; i < 5; i++) rowPowers.push(op(a[0], rowPowers.at(-1)));
if (rowFiveCycle) assumptions.push([rowPowers[5], a[0]]);
else assumptions.push([diagonal[0], diagonal[1]]);

// Include the diagonal shell and its first translates by core vertices for
// observation.  E677 itself is instantiated only on the ten core/diagonal
// roots: closing it on the whole observation shell creates irrelevant
// fourth-level terms before one useful congruence round can finish.
const watch = [];
const watchSet = new Set();
function addWatch(id) {
  if (id < 0 || watchSet.has(id)) return;
  watchSet.add(id);
  watch.push(id);
}
for (const x of a) addWatch(x);
for (const x of a) for (const y of a) addWatch(op(x, y));
for (const x of rowPowers) addWatch(x);
for (const x of watch.slice()) {
  for (const y of a) {
    addWatch(op(x, y));
    addWatch(op(y, x));
  }
}
const e677Basis = [...a, ...diagonal, ...(rowFiveCycle ? rowPowers : [])];

function products() {
  return terms.filter((term) => term.left >= 0);
}

function closeRound() {
  let changed = false;
  for (const [left, right] of assumptions) changed = union(left, right) || changed;

  for (const y of e677Basis) {
    for (const x of e677Basis) {
      const yx = op(y, x);
      changed = union(op(y, op(x, op(yx, y))), x) || changed;
    }
  }

  // Congruence closure.
  const pair = new Map();
  for (const term of products()) {
    const key = `${find(term.left)},${find(term.right)}`;
    if (pair.has(key)) changed = union(term.id, pair.get(key)) || changed;
    else pair.set(key, term.id);
  }

  // Finite E677 magmas have injective left translations.
  const leftValue = new Map();
  for (const term of products()) {
    const key = `${find(term.left)}:${find(term.id)}`;
    if (leftValue.has(key)) {
      changed = union(term.right, terms[leftValue.get(key)].right) || changed;
    } else {
      leftValue.set(key, term.id);
    }
  }
  return changed;
}

let rounds = 0;
let capped = false;
try {
  for (; rounds < maxRounds; rounds++) {
    if (!closeRound()) break;
  }
} catch (error) {
  if (!String(error).includes("term cap")) throw error;
  capped = true;
}

const equalVertices = [];
for (let i = 0; i < 5; i++) {
  for (let j = i + 1; j < 5; j++) {
    if (same(a[i], a[j])) equalVertices.push([i, j]);
  }
}

const fixerRows = a.map((point) => {
  const rows = [];
  for (const term of products()) {
    if (same(term.right, point) && same(term.id, point)) {
      rows.push(terms[term.left].expr);
    }
  }
  return [...new Set(rows)].slice(0, 20);
});

const diagonalClasses = diagonal.map((entry, index) => ({
  index,
  equalVertices: a.flatMap((vertex, j) => same(entry, vertex) ? [j] : []),
  equalDiagonals: diagonal.flatMap((other, j) => same(entry, other) ? [j] : []),
}));

console.log(JSON.stringify({
  diagnostic: rowFiveCycle
    ? "E677 K5 off-diagonal core with L_a0 cycle length dividing five at a0"
    : "E677 K5 off-diagonal core with a0*a0=a1*a1",
  rowFiveCycle,
  maxDepth,
  maxRounds,
  rounds,
  capped,
  watch: watch.length,
  e677Basis: e677Basis.length,
  terms: terms.length,
  equalVertices,
  forcedFixerAt: fixerRows.flatMap((rows, i) => rows.length ? [i] : []),
  fixerRows,
  diagonalClasses,
}, null, 2));
