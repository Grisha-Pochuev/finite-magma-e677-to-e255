"use strict";

// Bounded ground-congruence diagnostic for the crossed double-fan candidate.
// It checks whether a shallow closure forces p=q, r=s, c=d, or u=v.

const maxDepth = Number(process.argv[2] || 3);
const flags = new Set(process.argv.slice(3));

const termByKey = new Map();
const terms = [];
const parent = [];
const rank = [];

function makeTerm(key, expr, depth, left = -1, right = -1) {
  if (termByKey.has(key)) return termByKey.get(key);
  const id = terms.length;
  termByKey.set(key, id);
  terms.push({ id, key, expr, depth, left, right });
  parent.push(id);
  rank.push(0);
  return id;
}

function constant(name) {
  return makeTerm(name, name, 0);
}

function op(x, y) {
  return makeTerm(
    `*(${x},${y})`,
    `(${terms[x].expr}*${terms[y].expr})`,
    1 + Math.max(terms[x].depth, terms[y].depth),
    x,
    y
  );
}

function find(x) {
  while (parent[x] !== x) {
    parent[x] = parent[parent[x]];
    x = parent[x];
  }
  return x;
}

function union(a, b) {
  let ra = find(a);
  let rb = find(b);
  if (ra === rb) return false;
  if (rank[ra] < rank[rb]) [ra, rb] = [rb, ra];
  parent[rb] = ra;
  if (rank[ra] === rank[rb]) rank[ra]++;
  return true;
}

function same(a, b) {
  return find(a) === find(b);
}

const a = constant("a");
const b = constant("b");
const p = constant("p");
const q = constant("q");
const r = constant("r");
const s = constant("s");
const c = constant("c");
const d = constant("d");
const u = constant("u");
const v = constant("v");
const h = constant("h");
const k = constant("k");
const ab = constant("ab");
const ba = constant("ba");
const ta = constant("ta");
const at = constant("at");
const tb = constant("tb");

const assumptions = [];
function eq(x, y, label) {
  assumptions.push({ x, y, label });
}

// Opposite common-edge fans.
eq(op(p, a), b, "p*a=b");
eq(op(q, a), b, "q*a=b");
eq(op(p, b), c, "p*b=c");
eq(op(q, b), d, "q*b=d");
eq(op(c, p), h, "c*p=h");
eq(op(d, q), h, "d*q=h");
eq(op(b, h), a, "b*h=a");
eq(op(c, op(op(p, c), p)), b, "c*((p*c)*p)=b");
eq(op(d, op(op(q, d), q)), b, "d*((q*d)*q)=b");
eq(op(p, op(a, op(b, p))), a, "p*(a*(b*p))=a");
eq(op(q, op(a, op(b, q))), a, "q*(a*(b*q))=a");

eq(op(r, b), a, "r*b=a");
eq(op(s, b), a, "s*b=a");
eq(op(r, a), u, "r*a=u");
eq(op(s, a), v, "s*a=v");
eq(op(u, r), k, "u*r=k");
eq(op(v, s), k, "v*s=k");
eq(op(a, k), b, "a*k=b");
eq(op(u, op(op(r, u), r)), a, "u*((r*u)*r)=a");
eq(op(v, op(op(s, v), s)), a, "v*((s*v)*s)=a");
eq(op(r, op(b, op(a, r))), b, "r*(b*(a*r))=b");
eq(op(s, op(b, op(a, s))), b, "s*(b*(a*s))=b");
eq(op(a, b), ab, "a*b=ab");
eq(op(b, a), ba, "b*a=ba");
eq(op(ab, a), ta, "(a*b)*a=ta");
eq(op(a, ab), at, "a*(a*b)=at");
eq(op(ab, b), tb, "(a*b)*b=tb");

if (flags.has("c=u")) eq(c, u, "extra c=u");
if (flags.has("c=v")) eq(c, v, "extra c=v");
if (flags.has("d=u")) eq(d, u, "extra d=u");
if (flags.has("d=v")) eq(d, v, "extra d=v");
if (flags.has("h=k")) eq(h, k, "extra h=k");
if (flags.has("k=a")) eq(k, a, "extra k=a");
if (flags.has("k=c")) eq(k, c, "extra k=c");
if (flags.has("k=d")) eq(k, d, "extra k=d");
if (flags.has("k=u")) eq(k, u, "extra k=u");
if (flags.has("k=v")) eq(k, v, "extra k=v");
if (flags.has("h=a")) eq(h, a, "extra h=a");
if (flags.has("h=c")) eq(h, c, "extra h=c");
if (flags.has("h=d")) eq(h, d, "extra h=d");
if (flags.has("h=u")) eq(h, u, "extra h=u");
if (flags.has("h=v")) eq(h, v, "extra h=v");
if (flags.has("ab=a")) eq(ab, a, "extra ab=a");
if (flags.has("ab=c")) eq(ab, c, "extra ab=c");
if (flags.has("ab=d")) eq(ab, d, "extra ab=d");
if (flags.has("ab=u")) eq(ab, u, "extra ab=u");
if (flags.has("ab=v")) eq(ab, v, "extra ab=v");
if (flags.has("ab=h")) eq(ab, h, "extra ab=h");
if (flags.has("ab=k")) eq(ab, k, "extra ab=k");
if (flags.has("ta=a")) eq(ta, a, "extra ta=a");
if (flags.has("ta=b")) eq(ta, b, "extra ta=b");
if (flags.has("ta=c")) eq(ta, c, "extra ta=c");
if (flags.has("ta=d")) eq(ta, d, "extra ta=d");
if (flags.has("ta=u")) eq(ta, u, "extra ta=u");
if (flags.has("ta=v")) eq(ta, v, "extra ta=v");
if (flags.has("ta=h")) eq(ta, h, "extra ta=h");
if (flags.has("ta=k")) eq(ta, k, "extra ta=k");
if (flags.has("ta=ab")) eq(ta, ab, "extra ta=ab");
if (flags.has("at=a")) eq(at, a, "extra at=a");
if (flags.has("at=b")) eq(at, b, "extra at=b");
if (flags.has("at=c")) eq(at, c, "extra at=c");
if (flags.has("at=d")) eq(at, d, "extra at=d");
if (flags.has("at=u")) eq(at, u, "extra at=u");
if (flags.has("at=v")) eq(at, v, "extra at=v");
if (flags.has("at=h")) eq(at, h, "extra at=h");
if (flags.has("at=k")) eq(at, k, "extra at=k");
if (flags.has("at=ab")) eq(at, ab, "extra at=ab");
if (flags.has("tb=a")) eq(tb, a, "extra tb=a");
if (flags.has("tb=b")) eq(tb, b, "extra tb=b");
if (flags.has("tb=c")) eq(tb, c, "extra tb=c");
if (flags.has("tb=d")) eq(tb, d, "extra tb=d");
if (flags.has("tb=u")) eq(tb, u, "extra tb=u");
if (flags.has("tb=v")) eq(tb, v, "extra tb=v");
if (flags.has("tb=h")) eq(tb, h, "extra tb=h");
if (flags.has("tb=k")) eq(tb, k, "extra tb=k");
if (flags.has("tb=ab")) eq(tb, ab, "extra tb=ab");
if (flags.has("tb=ta")) eq(tb, ta, "extra tb=ta");
if (flags.has("c=a")) eq(c, a, "extra c=a");
if (flags.has("d=a")) eq(d, a, "extra d=a");
if (flags.has("u=b")) eq(u, b, "extra u=b");
if (flags.has("v=b")) eq(v, b, "extra v=b");

const basis = new Set([a, b, p, q, r, s, c, d, u, v, h, k, ab, ba, ta, at, tb]);

function addBasisProducts(rounds) {
  for (let round = 0; round < rounds; round++) {
    const snapshot = [...basis];
    for (const x of snapshot) {
      for (const y of snapshot) {
        const xy = op(x, y);
        if (terms[xy].depth <= maxDepth) basis.add(xy);
      }
    }
  }
}

addBasisProducts(1);

function close() {
  let changed = false;
  for (const item of assumptions) changed = union(item.x, item.y) || changed;

  const current = [...basis];
  for (const y of current) {
    for (const x of current) {
      const yx = op(y, x);
      const inner = op(x, op(yx, y));
      const e = op(y, inner);
      changed = union(e, x) || changed;
    }
  }

  const byLeftAndValue = new Map();
  for (let id = 0; id < terms.length; id++) {
    const t = terms[id];
    if (t.left < 0) continue;
    const key = `${find(t.left)}:${find(id)}`;
    if (byLeftAndValue.has(key)) {
      changed = union(t.right, terms[byLeftAndValue.get(key)].right) || changed;
    } else {
      byLeftAndValue.set(key, id);
    }
  }

  const byPair = new Map();
  for (let id = 0; id < terms.length; id++) {
    const t = terms[id];
    if (t.left < 0) continue;
    const key = `${find(t.left)},${find(t.right)}`;
    if (byPair.has(key)) {
      changed = union(id, byPair.get(key)) || changed;
    } else {
      byPair.set(key, id);
    }
  }

  return changed;
}

for (let round = 0; round < 20; round++) {
  if (!close()) break;
}

console.log("Crossed double-fan saturation");
console.log(`maxDepth: ${maxDepth}`);
if (flags.size) console.log(`flags: ${[...flags].join(" ")}`);
console.log(`terms: ${terms.length}`);
console.log(`p == q: ${same(p, q)}`);
console.log(`p == r: ${same(p, r)}`);
console.log(`p == s: ${same(p, s)}`);
console.log(`q == r: ${same(q, r)}`);
console.log(`q == s: ${same(q, s)}`);
console.log(`c == d: ${same(c, d)}`);
console.log(`r == s: ${same(r, s)}`);
console.log(`u == v: ${same(u, v)}`);
console.log(`h == k: ${same(h, k)}`);
console.log(`k == a: ${same(k, a)}`);
console.log(`k == c: ${same(k, c)}`);
console.log(`k == d: ${same(k, d)}`);
console.log(`ab == a: ${same(ab, a)}`);
console.log(`ab == c: ${same(ab, c)}`);
console.log(`ab == d: ${same(ab, d)}`);
console.log(`ab == h: ${same(ab, h)}`);
console.log(`ab == k: ${same(ab, k)}`);
console.log(`ta == h: ${same(ta, h)}`);
console.log(`ta == k: ${same(ta, k)}`);
console.log(`at == h: ${same(at, h)}`);
console.log(`at == k: ${same(at, k)}`);
console.log(`tb == a: ${same(tb, a)}`);
console.log(`tb == b: ${same(tb, b)}`);
console.log(`tb == h: ${same(tb, h)}`);
console.log(`tb == k: ${same(tb, k)}`);
console.log(`tb == ab: ${same(tb, ab)}`);

function addRightProducts(target, depthLimit) {
  const snapshot = terms.slice();
  for (const term of snapshot) {
    if (term.depth <= depthLimit) op(term.id, target);
  }
}

function closeToFixpoint(limit = 20) {
  for (let round = 0; round < limit; round++) {
    if (!close()) break;
  }
}

addRightProducts(a, maxDepth);
addRightProducts(b, maxDepth);
closeToFixpoint();

function shortRightFixers(target, depthLimit = maxDepth) {
  const out = [];
  for (const term of terms) {
    const id = term.id;
    if (term.depth > depthLimit) continue;
    if (same(op(id, target), target)) out.push(terms[id].expr);
    if (out.length >= 20) break;
  }
  return out;
}

console.log(`short right-fixers of a: ${JSON.stringify(shortRightFixers(a))}`);
console.log(`short right-fixers of b: ${JSON.stringify(shortRightFixers(b))}`);
