"use strict";

function permutations(n) {
  const out = [];
  const used = Array(n).fill(false);
  const cur = [];
  function rec() {
    if (cur.length === n) {
      const p = cur.slice();
      const inv = Array(n);
      for (let i = 0; i < n; i++) inv[p[i]] = i;
      out.push({ p, inv, label: p.join(" ") });
      return;
    }
    for (let i = 0; i < n; i++) {
      if (!used[i]) {
        used[i] = true;
        cur.push(i);
        rec();
        cur.pop();
        used[i] = false;
      }
    }
  }
  rec();
  return out;
}

function cyclePerm(n, cycles) {
  const p = Array.from({ length: n }, (_, i) => i);
  for (const cycle of cycles) {
    for (let i = 0; i < cycle.length; i++) {
      p[cycle[i]] = cycle[(i + 1) % cycle.length];
    }
  }
  const inv = Array(n);
  for (let i = 0; i < n; i++) inv[p[i]] = i;
  return { p, inv, label: p.join(" ") };
}

function partitions(n, maxPart = n) {
  if (n === 0) return [[]];
  const out = [];
  for (let first = Math.min(n, maxPart); first >= 1; first--) {
    for (const rest of partitions(n - first, first)) {
      out.push([first, ...rest]);
    }
  }
  return out;
}

function row0Representatives(n) {
  const reps = [];
  for (let zeroCycleLength = 2; zeroCycleLength <= n; zeroCycleLength++) {
    for (const tailPartition of partitions(n - zeroCycleLength)) {
      const cycles = [Array.from({ length: zeroCycleLength }, (_, i) => i)];
      let next = zeroCycleLength;
      for (const length of tailPartition) {
        const cycle = Array.from({ length }, (_, i) => next + i);
        next += length;
        if (cycle.length > 1) cycles.push(cycle);
      }
      reps.push(cyclePerm(n, cycles));
    }
  }
  return reps;
}

function cycleType(p) {
  const seen = Array(p.length).fill(false);
  const parts = [];
  for (let i = 0; i < p.length; i++) {
    if (seen[i]) continue;
    let cur = i;
    let len = 0;
    while (!seen[cur]) {
      seen[cur] = true;
      len++;
      cur = p[cur];
    }
    parts.push(len);
  }
  return parts.sort((a, b) => b - a).join("+");
}

function factorial(n) {
  let out = 1;
  for (let i = 2; i <= n; i++) out *= i;
  return out;
}

function cloneState(state) {
  return {
    assign: state.assign.slice(),
    req: state.req.map((row) => row.slice()),
  };
}

function formatTable(assign) {
  return assign.map((row) => row.p.join(" ")).join("\n");
}

function formatReqs(req) {
  const out = [];
  for (let row = 0; row < req.length; row++) {
    for (let col = 0; col < req[row].length; col++) {
      const value = req[row][col];
      if (value !== -1) out.push(`${row}*${col}=${value}`);
    }
  }
  return out;
}

function satisfiesE677(assign, n) {
  for (let x = 0; x < n; x++) {
    for (let y = 0; y < n; y++) {
      const py = assign[y];
      const px = assign[x];
      const targetRow = py.p[x];
      const lhs = assign[targetRow].p[y];
      const rhs = px.inv[py.inv[x]];
      if (lhs !== rhs) return false;
    }
  }
  return true;
}

function satisfiesE255(assign, n) {
  for (let x = 0; x < n; x++) {
    const rhs = assign[assign[assign[x].p[x]].p[x]].p[x];
    if (rhs !== x) return false;
  }
  return true;
}

function makeSearcher(n, options) {
  const bad = 0;
  const maxMs = (options.maxSeconds ?? 60) * 1000;
  const start = Date.now();
  const avoidBadColumn = options.mode !== "nonidempotent";
  const allValues = permutations(n).filter(
    (value) => !avoidBadColumn || value.p[bad] !== bad
  );
  const valueByLabel = new Map(allValues.map((value) => [value.label, value]));
  const valuesByCell = Array.from({ length: n }, () =>
    Array.from({ length: n }, () => [])
  );
  for (const value of allValues) {
    for (let col = 0; col < n; col++) {
      valuesByCell[col][value.p[col]].push(value);
    }
  }
  const allRow0 = row0Representatives(n);
  const row0Values =
    options.row0Index === undefined ? allRow0 : [allRow0[options.row0Index]];
  const extraReqs = options.extraReqs || [];
  const extraForbidPairs = options.extraForbidPairs || [];
  const stats = {
    nodes: 0,
    deadEnds: 0,
    imposedCells: 0,
    forcedRows: 0,
    domainChecks: 0,
  };

  function timedOut() {
    return Date.now() - start > maxMs;
  }

  function baseDomain(row) {
    return row === bad ? row0Values : allValues;
  }

  function impose(state, row, col, value) {
    if (avoidBadColumn && col === bad && value === bad) return false;
    const old = state.req[row][col];
    if (old !== -1) return old === value;

    for (let c = 0; c < n; c++) {
      if (c !== col && state.req[row][c] === value) return false;
    }

    const assigned = state.assign[row];
    if (assigned && assigned.p[col] !== value) return false;

    state.req[row][col] = value;
    stats.imposedCells++;
    return true;
  }

  function violatesForbidPair(row, candidate) {
    for (const forbid of extraForbidPairs) {
      if (forbid.row !== row) continue;
      let matched = true;
      for (const [col, value] of forbid.cells) {
        if (candidate.p[col] !== value) {
          matched = false;
          break;
        }
      }
      if (matched) return true;
    }
    return false;
  }

  function completeRows(state) {
    for (let row = 0; row < n; row++) {
      const used = Array(n).fill(false);
      let missingCol = -1;
      let missingCols = 0;
      for (let col = 0; col < n; col++) {
        const value = state.req[row][col];
        if (value === -1) {
          missingCol = col;
          missingCols++;
        } else {
          if (used[value]) return false;
          used[value] = true;
        }
      }
      if (missingCols === 1) {
        let missingValue = -1;
        for (let value = 0; value < n; value++) {
          if (!used[value]) {
            missingValue = value;
            break;
          }
        }
        if (!impose(state, row, missingCol, missingValue)) return false;
      }
    }
    return true;
  }

  function propagate(state) {
    let changed = true;
    while (changed) {
      const before = stats.imposedCells;

      for (let row = 0; row < n; row++) {
        const assigned = state.assign[row];
        if (!assigned) continue;
        if (avoidBadColumn && assigned.p[bad] === bad) return false;
        if (violatesForbidPair(row, assigned)) return false;
        for (let col = 0; col < n; col++) {
        const value = state.req[row][col];
        if (value !== -1 && assigned.p[col] !== value) return false;
      }
      }

      if (!completeRows(state)) return false;

      // Row-0 consequence of E677 with x=0,y=0:
      // (0*0)*0 = L_0^{-2}(0).  In the bad-cycle notation this is
      // r_{-1}=b_2, so the first hidden step of the ladder is forced
      // by row 0 alone.
      if (avoidBadColumn && state.assign[bad]) {
        const p0 = state.assign[bad];
        const first = p0.p[bad];
        const secondPreimage = p0.inv[p0.inv[bad]];
        if (!impose(state, first, bad, secondPreimage)) return false;
      }

      // x=0 instance of Lemma 13.1(i):
      // L_y^{-1}(0) = 0 * ((y*0)*y).  If a=y*0 and b=a*y are known,
      // then y*(0*b)=0.  This catches the repeated self-branch pattern:
      // if y*0=y and y*y=u, then y*(0*u)=0.
      if (avoidBadColumn && state.assign[bad]) {
        const p0 = state.assign[bad];
        for (let y = 0; y < n; y++) {
          const a = knownValue(state, y, bad, -1, null);
          if (!a.known) continue;
          const b = knownValue(state, a.value, y, -1, null);
          if (!b.known) continue;
          if (!impose(state, y, p0.p[b.value], bad)) return false;
        }
      }

      // Bad-column ladder with y = 0:
      // if r = (0*x)*0 is known, then x*r = L_0^{-1}(x).
      // Equivalently, for row x, prev = 0*x and next = L_0^{-1}(x),
      // a known value prev*0 immediately forces x*(prev*0)=next.
      if (avoidBadColumn && state.assign[bad]) {
        const p0 = state.assign[bad];
        for (let x = 0; x < n; x++) {
          const prev = p0.p[x];
          const next = p0.inv[x];
          const prevRow = state.assign[prev];
          const r =
            prevRow !== null ? prevRow.p[bad] : state.req[prev][bad];
          if (r !== -1 && !impose(state, x, r, next)) return false;
        }
      }

      // Reverse bad-column ladder:
      // from x*(prev*0)=next, if row x already has next in a known unique
      // column c, then prev*0=c.  This detects when self-fixation in the bad
      // column propagates backward along the bad cycle.
      if (avoidBadColumn && state.assign[bad]) {
        const p0 = state.assign[bad];
        for (let x = 0; x < n; x++) {
          const prev = p0.p[x];
          const next = p0.inv[x];
          const c = uniqueKnownColumnForValue(state, x, next, -1, null);
          if (c === -1) continue;
          if (!impose(state, prev, bad, c)) return false;
        }
      }

      // Partial permutation form of E677:
      // if a = y*x, c = L_y^{-1}(x), and d = L_x^{-1}(c) are already known
      // from cells or assigned rows, then a*y = d.
      for (let x = 0; x < n; x++) {
        for (let y = 0; y < n; y++) {
          const yx = knownValue(state, y, x, -1, null);
          if (!yx.known) continue;
          const c = uniqueKnownColumnForValue(state, y, x, -1, null);
          if (c === -1) continue;
          const d = uniqueKnownColumnForValue(state, x, c, -1, null);
          if (d === -1) continue;
          if (!impose(state, yx.value, y, d)) return false;
        }
      }

      // Partial form of Lemma 13.1(iii):
      // if a = y*x, b = y*a, and c = L_a^{-1}(x) are known, then b*y = c.
      for (let x = 0; x < n; x++) {
        for (let y = 0; y < n; y++) {
          const yx = knownValue(state, y, x, -1, null);
          if (!yx.known) continue;
          const yyx = knownValue(state, y, yx.value, -1, null);
          if (!yyx.known) continue;
          const c = uniqueKnownColumnForValue(state, yx.value, x, -1, null);
          if (c === -1) continue;
          if (!impose(state, yyx.value, y, c)) return false;
        }
      }

      // Direct partial E677:
      // x = y * (x * ((y*x)*y)).  If a=y*x, b=a*y, and c=x*b are
      // already known, force y*c=x.
      for (let x = 0; x < n; x++) {
        for (let y = 0; y < n; y++) {
          const a = knownValue(state, y, x, -1, null);
          if (!a.known) continue;
          const b = knownValue(state, a.value, y, -1, null);
          if (!b.known) continue;
          const c = knownValue(state, x, b.value, -1, null);
          if (!c.known) continue;
          if (!impose(state, y, c.value, x)) return false;
        }
      }

      for (let x = 0; x < n; x++) {
        const px = state.assign[x];
        if (!px) continue;
        for (let y = 0; y < n; y++) {
          const py = state.assign[y];
          if (!py) continue;
          const targetRow = py.p[x];
          const targetValue = px.inv[py.inv[x]];
          if (!impose(state, targetRow, y, targetValue)) return false;
        }
      }

      // Lemma 13.1(i), in a form that is useful before row x is chosen:
      // L_y^{-1} x = x * R_y L_y x.
      // If a = y*x and b = a*y are known, then row x must send b to L_y^{-1}(x).
      for (let x = 0; x < n; x++) {
        for (let y = 0; y < n; y++) {
          const py = state.assign[y];
          if (!py) continue;
          const a = py.p[x];
          const pa = state.assign[a];
          if (!pa) continue;
          const b = pa.p[y];
          const targetValue = py.inv[x];
          if (!impose(state, x, b, targetValue)) return false;
        }
      }

      // Reverse-use of the same identity:
      // if row x is not assigned yet but already has L_y^{-1}(x) in one known
      // column c, then (y*x)*y must be c.
      for (let x = 0; x < n; x++) {
        for (let y = 0; y < n; y++) {
          const py = state.assign[y];
          if (!py) continue;
          const targetValue = py.inv[x];
          const c = uniqueKnownColumnForValue(state, x, targetValue, -1, null);
          if (c === -1) continue;
          const a = py.p[x];
          if (!impose(state, a, y, c)) return false;
        }
      }

      // Finite E677 consequence from ETP Lemma 13.1(iii):
      // x = L_y x * R_y L_y^2 x.
      // In row form, if a = y*x and b = y*a, then b*y = L_a^{-1}(x).
      for (let x = 0; x < n; x++) {
        for (let y = 0; y < n; y++) {
          const py = state.assign[y];
          if (!py) continue;
          const a = py.p[x];
          const pa = state.assign[a];
          if (!pa) continue;
          const b = py.p[a];
          const targetValue = pa.inv[x];
          if (!impose(state, b, y, targetValue)) return false;
        }
      }

      // Reverse-use of Lemma 13.1(iii):
      // if row a already has x in one known column c, then b*y must be c.
      for (let x = 0; x < n; x++) {
        for (let y = 0; y < n; y++) {
          const py = state.assign[y];
          if (!py) continue;
          const a = py.p[x];
          const b = py.p[a];
          const c = uniqueKnownColumnForValue(state, a, x, -1, null);
          if (c === -1) continue;
          if (!impose(state, b, y, c)) return false;
        }
      }

      // Reverse form of Lemma 13.1(iii):
      // if b = y*a and a = y*x, then a*(b*y) = x.
      for (let y = 0; y < n; y++) {
        const py = state.assign[y];
        if (!py) continue;
        for (let b = 0; b < n; b++) {
          const pb = state.assign[b];
          if (!pb) continue;
          const a = py.inv[b];
          const x = py.inv[a];
          const col = pb.p[y];
          if (!impose(state, a, col, x)) return false;
        }
      }

      // General collision consequence from Lemma 13.1(iii):
      // if y*x = z*x = c and y != z, then (y*c)*y = (z*c)*z.
      for (let y = 0; y < n; y++) {
        const py = state.assign[y];
        if (!py) continue;
        for (let z = y + 1; z < n; z++) {
          const pz = state.assign[z];
          if (!pz) continue;
          for (let x = 0; x < n; x++) {
            const c = py.p[x];
            if (pz.p[x] !== c) continue;
            const d = py.p[c];
            const e = pz.p[c];
            if (d === e) return false;
            const pd = state.assign[d];
            const pe = state.assign[e];
            if (pd && pe) {
              if (pd.p[y] !== pe.p[z]) return false;
            } else if (pd) {
              if (!impose(state, e, z, pd.p[y])) return false;
            } else if (pe) {
              if (!impose(state, d, y, pe.p[z])) return false;
            }
          }
        }
      }

      // Inverse-collision consequence from Lemma 13.1(i):
      // if L_y^{-1}(x) = L_z^{-1}(x), then (y*x)*y = (z*x)*z.
      for (let y = 0; y < n; y++) {
        const py = state.assign[y];
        if (!py) continue;
        for (let z = y + 1; z < n; z++) {
          const pz = state.assign[z];
          if (!pz) continue;
          for (let x = 0; x < n; x++) {
            if (py.inv[x] !== pz.inv[x]) continue;
            const d = py.p[x];
            const e = pz.p[x];
            if (d === e) return false;
            const pd = state.assign[d];
            const pe = state.assign[e];
            if (pd && pe) {
              if (pd.p[y] !== pe.p[z]) return false;
            } else if (pd) {
              if (!impose(state, e, z, pd.p[y])) return false;
            } else if (pe) {
              if (!impose(state, d, y, pe.p[z])) return false;
            }
          }
        }
      }

      changed = stats.imposedCells !== before;
    }
    return true;
  }

  function requirementWouldConflict(state, row, col, value, candidateRow, candidate) {
    if (row === candidateRow) return candidate.p[col] !== value;
    const assigned = state.assign[row];
    if (assigned) return assigned.p[col] !== value;
    const old = state.req[row][col];
    if (old !== -1) return old !== value;
    for (let c = 0; c < n; c++) {
      if (c !== col && state.req[row][c] === value) return true;
    }
    return false;
  }

  function knownValue(state, targetRow, col, candidateRow, candidate) {
    if (targetRow === candidateRow) return { known: true, value: candidate.p[col] };
    const assigned = state.assign[targetRow];
    if (assigned) return { known: true, value: assigned.p[col] };
    const required = state.req[targetRow][col];
    if (required !== -1) return { known: true, value: required };
    return { known: false, value: -1 };
  }

  function uniqueKnownColumnForValue(state, targetRow, value, candidateRow, candidate) {
    if (targetRow === candidateRow) return candidate.inv[value];
    const assigned = state.assign[targetRow];
    if (assigned) return assigned.inv[value];

    let found = -1;
    for (let col = 0; col < n; col++) {
      if (state.req[targetRow][col] !== value) continue;
      if (found !== -1) return -1;
      found = col;
    }
    return found;
  }

  function candidateConsistent(state, row, candidate) {
    stats.domainChecks++;
    if (avoidBadColumn && candidate.p[bad] === bad) return false;

    for (let other = 0; other < n; other++) {
      if (other !== row && state.assign[other]?.label === candidate.label) {
        return false;
      }
      const otherRow = state.assign[other];
      if (
        avoidBadColumn &&
        other !== row &&
        otherRow &&
        otherRow.p[bad] === candidate.p[bad] &&
        otherRow.p[candidate.p[bad]] === candidate.p[candidate.p[bad]]
      ) {
        return false;
      }
    }

    for (let col = 0; col < n; col++) {
      const required = state.req[row][col];
      if (required !== -1 && candidate.p[col] !== required) return false;
    }
    if (violatesForbidPair(row, candidate)) return false;

    // In a true counterexample with bad element 0, Lemma 13.2 says
    // there is no y with 0*(y*y)=y.
    const p0 = row === bad ? candidate : state.assign[bad];
    if (avoidBadColumn && p0) {
      const diagonal = candidate.p[row];
      if (p0.p[diagonal] === row) return false;
      const forbidden = p0.inv[row];
      if (candidate.p[row] === forbidden) return false;
      if (candidate.p[bad] === forbidden) return false;
    }

    // Collision consequence from Lemma 13.1(iii), checked early for candidates:
    // if y*x = z*x = c, then (y*c)*y = (z*c)*z.
    for (let other = 0; other < n; other++) {
      if (other === row) continue;
      const otherRow = state.assign[other];
      if (!otherRow) continue;
      for (let x = 0; x < n; x++) {
        const c = candidate.p[x];
        if (otherRow.p[x] !== c) continue;
        const d = candidate.p[c];
        const e = otherRow.p[c];
        if (d === e) return false;
        const lhs = knownValue(state, d, row, row, candidate);
        const rhs = knownValue(state, e, other, row, candidate);
        if (lhs.known && rhs.known && lhs.value !== rhs.value) return false;
        if (
          lhs.known &&
          requirementWouldConflict(state, e, other, lhs.value, row, candidate)
        ) {
          return false;
        }
        if (
          rhs.known &&
          requirementWouldConflict(state, d, row, rhs.value, row, candidate)
        ) {
          return false;
        }
      }
    }

    for (let y = 0; y < n; y++) {
      const py = state.assign[y];
      if (!py) continue;
      for (let z = y + 1; z < n; z++) {
        const pz = state.assign[z];
        if (!pz) continue;
        for (let x = 0; x < n; x++) {
          const c = py.p[x];
          if (pz.p[x] !== c) continue;
          const d = py.p[c];
          const e = pz.p[c];
          if (d !== row && e !== row) continue;
          if (d === e) return false;
          const lhs = knownValue(state, d, y, row, candidate);
          const rhs = knownValue(state, e, z, row, candidate);
          if (lhs.known && rhs.known && lhs.value !== rhs.value) return false;
          if (
            lhs.known &&
            requirementWouldConflict(state, e, z, lhs.value, row, candidate)
          ) {
            return false;
          }
          if (
            rhs.known &&
            requirementWouldConflict(state, d, y, rhs.value, row, candidate)
          ) {
            return false;
          }
        }
      }
    }

    // Inverse-collision candidate check:
    // if two rows put value x in the same column, then (y*x)*y = (z*x)*z.
    for (let other = 0; other < n; other++) {
      if (other === row) continue;
      const otherRow = state.assign[other];
      if (!otherRow) continue;
      for (let x = 0; x < n; x++) {
        if (candidate.inv[x] !== otherRow.inv[x]) continue;
        const d = candidate.p[x];
        const e = otherRow.p[x];
        if (d === e) return false;
        const lhs = knownValue(state, d, row, row, candidate);
        const rhs = knownValue(state, e, other, row, candidate);
        if (lhs.known && rhs.known && lhs.value !== rhs.value) return false;
        if (
          lhs.known &&
          requirementWouldConflict(state, e, other, lhs.value, row, candidate)
        ) {
          return false;
        }
        if (
          rhs.known &&
          requirementWouldConflict(state, d, row, rhs.value, row, candidate)
        ) {
          return false;
        }
      }
    }

    for (let y = 0; y < n; y++) {
      const py = state.assign[y];
      if (!py) continue;
      for (let z = y + 1; z < n; z++) {
        const pz = state.assign[z];
        if (!pz) continue;
        for (let x = 0; x < n; x++) {
          if (py.inv[x] !== pz.inv[x]) continue;
          const d = py.p[x];
          const e = pz.p[x];
          if (d !== row && e !== row) continue;
          if (d === e) return false;
          const lhs = knownValue(state, d, y, row, candidate);
          const rhs = knownValue(state, e, z, row, candidate);
          if (lhs.known && rhs.known && lhs.value !== rhs.value) return false;
          if (
            lhs.known &&
            requirementWouldConflict(state, e, z, lhs.value, row, candidate)
          ) {
            return false;
          }
          if (
            rhs.known &&
            requirementWouldConflict(state, d, y, rhs.value, row, candidate)
          ) {
            return false;
          }
        }
      }
    }

    for (let x = 0; x < n; x++) {
      for (let y = 0; y < n; y++) {
        const yx = knownValue(state, y, x, row, candidate);
        if (!yx.known) continue;
        const c = uniqueKnownColumnForValue(state, y, x, row, candidate);
        if (c === -1) continue;
        const d = uniqueKnownColumnForValue(state, x, c, row, candidate);
        if (d === -1) continue;
        if (requirementWouldConflict(state, yx.value, y, d, row, candidate)) {
          return false;
        }
      }
    }

    for (let x = 0; x < n; x++) {
      for (let y = 0; y < n; y++) {
        const yx = knownValue(state, y, x, row, candidate);
        if (!yx.known) continue;
        const yyx = knownValue(state, y, yx.value, row, candidate);
        if (!yyx.known) continue;
        const c = uniqueKnownColumnForValue(state, yx.value, x, row, candidate);
        if (c === -1) continue;
        if (requirementWouldConflict(state, yyx.value, y, c, row, candidate)) {
          return false;
        }
      }
    }

    const p0ForCandidate = row === bad ? candidate : state.assign[bad];
    if (avoidBadColumn && p0ForCandidate) {
      for (let y = 0; y < n; y++) {
        const a = knownValue(state, y, bad, row, candidate);
        if (!a.known) continue;
        const b = knownValue(state, a.value, y, row, candidate);
        if (!b.known) continue;
        const col = p0ForCandidate.p[b.value];
        if (requirementWouldConflict(state, y, col, bad, row, candidate)) {
          return false;
        }
      }
    }

    if (avoidBadColumn && p0ForCandidate) {
      for (let x = 0; x < n; x++) {
        const prev = p0ForCandidate.p[x];
        const next = p0ForCandidate.inv[x];
        const c = uniqueKnownColumnForValue(state, x, next, row, candidate);
        if (c === -1) continue;
        if (requirementWouldConflict(state, prev, bad, c, row, candidate)) {
          return false;
        }
      }
    }

    for (let x = 0; x < n; x++) {
      for (let y = 0; y < n; y++) {
        const a = knownValue(state, y, x, row, candidate);
        if (!a.known) continue;
        const b = knownValue(state, a.value, y, row, candidate);
        if (!b.known) continue;
        const c = knownValue(state, x, b.value, row, candidate);
        if (!c.known) continue;
        if (requirementWouldConflict(state, y, c.value, x, row, candidate)) {
          return false;
        }
      }
    }

    for (let x = 0; x < n; x++) {
      const px = x === row ? candidate : state.assign[x];
      if (!px) continue;
      for (let y = 0; y < n; y++) {
        const py = y === row ? candidate : state.assign[y];
        if (!py) continue;
        const targetRow = py.p[x];
        const targetValue = px.inv[py.inv[x]];
        if (requirementWouldConflict(state, targetRow, y, targetValue, row, candidate)) {
          return false;
        }
      }
    }

    for (let x = 0; x < n; x++) {
      for (let y = 0; y < n; y++) {
        const py = y === row ? candidate : state.assign[y];
        if (!py) continue;
        const a = py.p[x];
        const pa = a === row ? candidate : state.assign[a];
        if (!pa) continue;
        const b = pa.p[y];
        const targetValue = py.inv[x];
        if (requirementWouldConflict(state, x, b, targetValue, row, candidate)) {
          return false;
        }
      }
    }

    for (let x = 0; x < n; x++) {
      for (let y = 0; y < n; y++) {
        const py = y === row ? candidate : state.assign[y];
        if (!py) continue;
        const targetValue = py.inv[x];
        const c = uniqueKnownColumnForValue(state, x, targetValue, row, candidate);
        if (c === -1) continue;
        const a = py.p[x];
        if (requirementWouldConflict(state, a, y, c, row, candidate)) {
          return false;
        }
      }
    }

    for (let x = 0; x < n; x++) {
      for (let y = 0; y < n; y++) {
        const py = y === row ? candidate : state.assign[y];
        if (!py) continue;
        const a = py.p[x];
        const pa = a === row ? candidate : state.assign[a];
        if (!pa) continue;
        const b = py.p[a];
        const targetValue = pa.inv[x];
        if (requirementWouldConflict(state, b, y, targetValue, row, candidate)) {
          return false;
        }
      }
    }

    for (let x = 0; x < n; x++) {
      for (let y = 0; y < n; y++) {
        const py = y === row ? candidate : state.assign[y];
        if (!py) continue;
        const a = py.p[x];
        const b = py.p[a];
        const c = uniqueKnownColumnForValue(state, a, x, row, candidate);
        if (c === -1) continue;
        if (requirementWouldConflict(state, b, y, c, row, candidate)) {
          return false;
        }
      }
    }

    for (let y = 0; y < n; y++) {
      const py = y === row ? candidate : state.assign[y];
      if (!py) continue;
      for (let b = 0; b < n; b++) {
        const pb = b === row ? candidate : state.assign[b];
        if (!pb) continue;
        const a = py.inv[b];
        const x = py.inv[a];
        const col = pb.p[y];
        if (requirementWouldConflict(state, a, col, x, row, candidate)) {
          return false;
        }
      }
    }

    return true;
  }

  function domainFor(state, row) {
    const out = [];
    let source = baseDomain(row);
    if (row !== bad) {
      for (let col = 0; col < n; col++) {
        const required = state.req[row][col];
        if (required === -1) continue;
        const indexed = valuesByCell[col][required];
        if (indexed.length < source.length) source = indexed;
      }
      const generated = sourceFromRequirements(state, row, source.length);
      if (generated) source = generated;
    }
    for (const candidate of source) {
      if (candidateConsistent(state, row, candidate)) out.push(candidate);
    }
    return out;
  }

  function sourceFromRequirements(state, row, currentSourceLength) {
    const req = state.req[row];
    const fixed = [];
    const used = Array(n).fill(false);
    for (let col = 0; col < n; col++) {
      const value = req[col];
      if (value === -1) continue;
      if (used[value]) return [];
      used[value] = true;
      fixed.push([col, value]);
    }

    if (fixed.length < 2) return null;
    const estimated = factorial(n - fixed.length);
    if (estimated >= currentSourceLength) return null;

    const p = Array(n).fill(-1);
    for (const [col, value] of fixed) p[col] = value;

    const freeCols = [];
    const freeValues = [];
    for (let col = 0; col < n; col++) {
      if (p[col] === -1) freeCols.push(col);
    }
    for (let value = 0; value < n; value++) {
      if (!used[value]) freeValues.push(value);
    }

    const out = [];
    const usedFree = Array(freeValues.length).fill(false);
    function rec(i) {
      if (i === freeCols.length) {
        const candidate = valueByLabel.get(p.join(" "));
        if (candidate) out.push(candidate);
        return;
      }
      const col = freeCols[i];
      for (let j = 0; j < freeValues.length; j++) {
        if (usedFree[j]) continue;
        const value = freeValues[j];
        if (avoidBadColumn && col === bad && value === bad) continue;
        usedFree[j] = true;
        p[col] = value;
        rec(i + 1);
        p[col] = -1;
        usedFree[j] = false;
      }
    }
    rec(0);
    return out;
  }

  function closeState(state) {
    while (true) {
      if (!propagate(state)) return { ok: false };

      let allAssigned = true;
      const domains = Array(n).fill(null);
      let singletonRow = -1;

      for (let row = 0; row < n; row++) {
        if (state.assign[row]) continue;
        allAssigned = false;
        const domain = domainFor(state, row);
        if (domain.length === 0) return { ok: false };
        domains[row] = domain;
        if (domain.length === 1 && singletonRow === -1) singletonRow = row;
      }

      if (allAssigned) return { ok: true, domains };

      let imposedCommonCell = false;
      for (let row = 0; row < n; row++) {
        if (state.assign[row]) continue;
        const domain = domains[row];
        for (let col = 0; col < n; col++) {
          if (state.req[row][col] !== -1) continue;
          const value = domain[0].p[col];
          let common = true;
          for (let i = 1; i < domain.length; i++) {
            if (domain[i].p[col] !== value) {
              common = false;
              break;
            }
          }
          if (common) {
            if (!impose(state, row, col, value)) return { ok: false };
            imposedCommonCell = true;
          }
        }
      }
      if (imposedCommonCell) continue;

      if (singletonRow === -1) return { ok: true, domains };

      const domain = domains[singletonRow];
      state.assign[singletonRow] = domain[0];
      stats.forcedRows++;
    }
  }

  function rec(state, depth) {
    if (timedOut()) return { status: "timeout" };
    stats.nodes++;

    const closed = closeState(state);
    if (!closed.ok) {
      stats.deadEnds++;
      return { status: "none" };
    }

    let bestRow = -1;
    let bestDomain = null;
    for (let row = 0; row < n; row++) {
      if (state.assign[row]) continue;
      const domain = closed.domains[row];
      if (!bestDomain || domain.length < bestDomain.length) {
        bestRow = row;
        bestDomain = domain;
      }
    }

    if (bestRow === -1) {
      if (satisfiesE677(state.assign, n)) {
        return {
          status: "found",
          table: formatTable(state.assign),
          e255: satisfiesE255(state.assign, n),
        };
      }
      stats.deadEnds++;
      return { status: "none" };
    }

    if (depth === 0) {
      console.log(`depth ${depth}: row ${bestRow}, ${bestDomain.length} candidates`);
    }

    for (const candidate of bestDomain) {
      const next = cloneState(state);
      next.assign[bestRow] = candidate;
      const result = rec(next, depth + 1);
      if (result.status !== "none") return result;
    }

    return { status: "none" };
  }

  function run() {
    const initial = freshState();
    if (!initial) return { status: "none", ms: Date.now() - start, stats, row0Count: allRow0.length };
    const result = rec(initial, 0);
    result.ms = Date.now() - start;
    result.stats = stats;
    result.row0Count = allRow0.length;
    return result;
  }

  function diagnoseInitial() {
    const initial = freshState();
    if (!initial) return { ok: false, stats };
    const closed = closeState(initial);
    if (!closed.ok) {
      return { ok: false, stats };
    }
    const rows = [];
    for (let row = 0; row < n; row++) {
      const assigned = initial.assign[row];
      const forcedCells = initial.req[row].filter((value) => value !== -1).length;
      rows.push({
        row,
        assigned: assigned ? assigned.label : null,
        domainSize: assigned ? 1 : closed.domains[row].length,
        forcedCells,
        req: initial.req[row].slice(),
      });
    }
    return { ok: true, rows, stats };
  }

  function diagnoseFirstBranches(limit = Infinity) {
    const initial = freshState();
    if (!initial) return { ok: false, stats };
    const closed = closeState(initial);
    if (!closed.ok) return { ok: false, stats };

    let bestRow = -1;
    let bestDomain = null;
    for (let row = 0; row < n; row++) {
      if (initial.assign[row]) continue;
      const domain = closed.domains[row];
      if (!bestDomain || domain.length < bestDomain.length) {
        bestRow = row;
        bestDomain = domain;
      }
    }
    if (bestRow === -1) return { ok: true, complete: true, stats };

    const histogram = new Map();
    const samples = [];
    const aliveCellHist = Array.from({ length: n }, () => new Map());
    let dead = 0;
    let checked = 0;
    for (const candidate of bestDomain) {
      if (checked >= limit) break;
      checked++;
      const next = cloneState(initial);
      next.assign[bestRow] = candidate;
      const nextClosed = closeState(next);
      if (!nextClosed.ok) {
        dead++;
        histogram.set("dead", (histogram.get("dead") || 0) + 1);
        continue;
      }
      let nextRow = -1;
      let nextSize = Infinity;
      for (let row = 0; row < n; row++) {
        if (next.assign[row]) continue;
        const size = nextClosed.domains[row].length;
        if (size < nextSize) {
          nextRow = row;
          nextSize = size;
        }
      }
      const key = nextRow === -1 ? "complete" : `row ${nextRow}, domain ${nextSize}`;
      histogram.set(key, (histogram.get(key) || 0) + 1);
      for (let col = 0; col < n; col++) {
        const value = candidate.p[col];
        const cellHist = aliveCellHist[col];
        cellHist.set(value, (cellHist.get(value) || 0) + 1);
      }
      if (samples.length < 20) {
        samples.push({ candidate: candidate.label, next: key });
      }
    }
    return {
      ok: true,
      bestRow,
      bestDomainSize: bestDomain.length,
      checked,
      dead,
      samples,
      aliveCellHist: aliveCellHist.map((cellHist) =>
        Array.from(cellHist.entries()).sort((a, b) => a[0] - b[0])
      ),
      histogram: Array.from(histogram.entries()).sort((a, b) =>
        String(a[0]).localeCompare(String(b[0]))
      ),
      stats,
    };
  }

  function diagnoseBestDomain() {
    const initial = freshState();
    if (!initial) return { ok: false, stats };
    const closed = closeState(initial);
    if (!closed.ok) return { ok: false, stats };

    let bestRow = -1;
    let bestDomain = null;
    for (let row = 0; row < n; row++) {
      if (initial.assign[row]) continue;
      const domain = closed.domains[row];
      if (!bestDomain || domain.length < bestDomain.length) {
        bestRow = row;
        bestDomain = domain;
      }
    }
    if (bestRow === -1) return { ok: true, complete: true, stats };

    const hist = Array.from({ length: n }, () => new Map());
    for (const candidate of bestDomain) {
      for (let col = 0; col < n; col++) {
        const cellHist = hist[col];
        const value = candidate.p[col];
        cellHist.set(value, (cellHist.get(value) || 0) + 1);
      }
    }

    return {
      ok: true,
      bestRow,
      bestDomainSize: bestDomain.length,
      samples: bestDomain.slice(0, 20).map((candidate) => candidate.label),
      hist: hist.map((cellHist) =>
        Array.from(cellHist.entries()).sort((a, b) => a[0] - b[0])
      ),
      stats,
    };
  }

  function diagnoseCellScores(limit = 30) {
    const initial = freshState();
    if (!initial) return { ok: false, stats };
    const closed = closeState(initial);
    if (!closed.ok) return { ok: false, stats };

    const scores = [];
    for (let row = 0; row < n; row++) {
      if (initial.assign[row]) continue;
      const domain = closed.domains[row];
      if (!domain || domain.length === 0) continue;
      const hists = Array.from({ length: n }, () => new Map());
      for (const candidate of domain) {
        for (let col = 0; col < n; col++) {
          const value = candidate.p[col];
          const hist = hists[col];
          hist.set(value, (hist.get(value) || 0) + 1);
        }
      }
      for (let col = 0; col < n; col++) {
        const entries = Array.from(hists[col].entries()).sort((a, b) => a[0] - b[0]);
        if (entries.length <= 1) continue;
        const minCount = Math.min(...entries.map((entry) => entry[1]));
        const maxCount = Math.max(...entries.map((entry) => entry[1]));
        scores.push({
          row,
          col,
          domainSize: domain.length,
          distinct: entries.length,
          minCount,
          maxCount,
          entries,
        });
      }
    }
    scores.sort((a, b) => {
      if (a.minCount !== b.minCount) return a.minCount - b.minCount;
      if (a.distinct !== b.distinct) return a.distinct - b.distinct;
      if (a.domainSize !== b.domainSize) return a.domainSize - b.domainSize;
      if (a.row !== b.row) return a.row - b.row;
      return a.col - b.col;
    });
    return { ok: true, scores: scores.slice(0, limit), stats };
  }

  function diagnoseCellScoresForRows(targetRows, limit = 30) {
    const initial = freshState();
    if (!initial) return { ok: false, stats };
    const closed = closeState(initial);
    if (!closed.ok) return { ok: false, stats };

    const wanted = new Set(targetRows);
    const scores = [];
    for (let row = 0; row < n; row++) {
      if (!wanted.has(row)) continue;
      if (initial.assign[row]) continue;
      const domain = closed.domains[row];
      if (!domain || domain.length === 0) continue;
      const hists = Array.from({ length: n }, () => new Map());
      for (const candidate of domain) {
        for (let col = 0; col < n; col++) {
          const value = candidate.p[col];
          const hist = hists[col];
          hist.set(value, (hist.get(value) || 0) + 1);
        }
      }
      for (let col = 0; col < n; col++) {
        const entries = Array.from(hists[col].entries()).sort((a, b) => a[0] - b[0]);
        if (entries.length <= 1) continue;
        const minCount = Math.min(...entries.map((entry) => entry[1]));
        const maxCount = Math.max(...entries.map((entry) => entry[1]));
        scores.push({
          row,
          col,
          domainSize: domain.length,
          distinct: entries.length,
          minCount,
          maxCount,
          entries,
        });
      }
    }
    scores.sort((a, b) => {
      if (a.minCount !== b.minCount) return a.minCount - b.minCount;
      if (a.distinct !== b.distinct) return a.distinct - b.distinct;
      if (a.domainSize !== b.domainSize) return a.domainSize - b.domainSize;
      if (a.row !== b.row) return a.row - b.row;
      return a.col - b.col;
    });
    return { ok: true, scores: scores.slice(0, limit), stats };
  }

  function diagnoseRowDomain(targetRow) {
    const initial = freshState();
    if (!initial) return { ok: false, stats };
    const closed = closeState(initial);
    if (!closed.ok) return { ok: false, stats };
    if (targetRow < 0 || targetRow >= n) {
      throw new Error(`Bad row for rowhist: ${targetRow}`);
    }

    const assigned = initial.assign[targetRow];
    const domain = assigned ? [assigned] : closed.domains[targetRow];
    const hist = Array.from({ length: n }, () => new Map());
    for (const candidate of domain) {
      for (let col = 0; col < n; col++) {
        const cellHist = hist[col];
        const value = candidate.p[col];
        cellHist.set(value, (cellHist.get(value) || 0) + 1);
      }
    }

    return {
      ok: true,
      row: targetRow,
      assigned: assigned ? assigned.label : null,
      domainSize: domain.length,
      samples: domain.slice(0, 20).map((candidate) => candidate.label),
      hist: hist.map((cellHist) =>
        Array.from(cellHist.entries()).sort((a, b) => a[0] - b[0])
      ),
      stats,
    };
  }

  return {
    run,
    diagnoseInitial,
    diagnoseFirstBranches,
    diagnoseBestDomain,
    diagnoseCellScores,
    diagnoseCellScoresForRows,
    diagnoseRowDomain,
    closeState,
    freshState,
    stats,
    allRow0,
  };

  function freshState() {
    const state = {
      assign: Array(n).fill(null),
      req: Array.from({ length: n }, () => Array(n).fill(-1)),
    };
    for (const req of extraReqs) {
      if (!impose(state, req.row, req.col, req.value)) return null;
    }
    return state;
  }
}

const runtimeProcess =
  typeof process !== "undefined"
    ? process
    : {
        argv: globalThis.__searchCounterexampleArgv || [],
        exit(code = 0) {
          throw Object.assign(new Error("__SEARCH_COUNTEREXAMPLE_EXIT__"), {
            code,
          });
        },
      };

const n = Number(runtimeProcess.argv[2] || 8);
const maxSeconds = Number(runtimeProcess.argv[3] || 60);
const rawRow0Index = runtimeProcess.argv[4];
const row0Index =
  rawRow0Index === undefined || rawRow0Index === "all"
    ? undefined
    : Number(rawRow0Index);
const mode = runtimeProcess.argv[5] || "counterexample";
const extraReqs = [];
const extraForbidPairs = [];
let branchLimit = Infinity;
let extraReqArg = "";
let rowHistTarget = -1;
let rowScoreTargets = [];
if (mode === "branches") {
  const arg6 = runtimeProcess.argv[6];
  const arg7 = runtimeProcess.argv[7];
  if (arg6 && arg6.includes(":")) {
    extraReqArg = arg6;
  } else {
    branchLimit = Number(arg6 || Infinity);
    extraReqArg = arg7 || "";
  }
} else if (mode === "rowhist") {
  rowHistTarget = Number(runtimeProcess.argv[6]);
  if (Number.isNaN(rowHistTarget)) {
    throw new Error("rowhist mode requires a row number as argument 6");
  }
  extraReqArg = runtimeProcess.argv[7] || "";
} else if (mode === "rowscores") {
  rowScoreTargets = (runtimeProcess.argv[6] || "")
    .split(",")
    .filter(Boolean)
    .map(Number);
  if (!rowScoreTargets.length || rowScoreTargets.some((row) => Number.isNaN(row))) {
    throw new Error("rowscores mode requires comma-separated row numbers as argument 6");
  }
  extraReqArg = runtimeProcess.argv[7] || "";
} else {
  extraReqArg = runtimeProcess.argv[6] || "";
}
if (extraReqArg) {
  for (const raw of extraReqArg.split(",")) {
    if (raw.includes("~")) {
      const [left, right] = raw.split("~");
      const [row, col1, value1] = left.split(":").map(Number);
      const [col2, value2] = right.split(":").map(Number);
      if ([row, col1, value1, col2, value2].some((part) => Number.isNaN(part))) {
        throw new Error(`Bad extra forbid pair: ${raw}`);
      }
      extraForbidPairs.push({
        row,
        cells: [
          [col1, value1],
          [col2, value2],
        ],
      });
      continue;
    }
    const [row, col, value] = raw.split(":").map(Number);
    if ([row, col, value].some((part) => Number.isNaN(part))) {
      throw new Error(`Bad extra requirement: ${raw}`);
    }
    extraReqs.push({ row, col, value });
  }
}

const searcher = makeSearcher(n, {
  maxSeconds,
  row0Index,
  mode,
  extraReqs,
  extraForbidPairs,
});
if (mode === "diagnose") {
  console.log(`Strong diagnostic for E677 counterexample search, size ${n}.`);
  if (row0Index !== undefined) {
    const rep = searcher.allRow0[row0Index];
    console.log(`row-0 case ${row0Index + 1}/${searcher.allRow0.length}: ${rep.label}`);
    console.log(`row-0 cycle type: ${cycleType(rep.p)}`);
  }
  const diagnostic = searcher.diagnoseInitial();
  console.log(`status: ${diagnostic.ok ? "ok" : "contradiction"}`);
  for (const row of diagnostic.rows || []) {
    const reqText = row.req
      .map((value, col) => (value === -1 ? null : `${col}->${value}`))
      .filter(Boolean)
      .join(", ");
    console.log(
      `row ${row.row}: domain=${row.domainSize}, forcedCells=${row.forcedCells}` +
        (row.assigned ? `, assigned=${row.assigned}` : "") +
        (reqText ? `, req=[${reqText}]` : "")
    );
  }
  console.log(`forced cells: ${diagnostic.stats.imposedCells}`);
  console.log(`domain checks: ${diagnostic.stats.domainChecks}`);
  runtimeProcess.exit(0);
}
if (mode === "closure") {
  console.log(`Strong closure diagnostic, size ${n}.`);
  if (row0Index !== undefined) {
    const rep = searcher.allRow0[row0Index];
    console.log(`row-0 case ${row0Index + 1}/${searcher.allRow0.length}: ${rep.label}`);
    console.log(`row-0 cycle type: ${cycleType(rep.p)}`);
  }
  const state = searcher.freshState();
  if (!state) {
    console.log("status: contradiction");
    console.log("reason: initial requirements conflict");
    runtimeProcess.exit(0);
  }
  const closed = searcher.closeState(state);
  console.log(`status: ${closed.ok ? "ok" : "contradiction"}`);
  const reqs = formatReqs(state.req);
  for (const req of reqs) console.log(req);
  console.log(`forced cells: ${searcher.stats.imposedCells}`);
  console.log(`domain checks: ${searcher.stats.domainChecks}`);
  runtimeProcess.exit(0);
}
if (mode === "branches") {
  console.log(`Strong first-branch diagnostic, size ${n}.`);
  if (row0Index !== undefined) {
    const rep = searcher.allRow0[row0Index];
    console.log(`row-0 case ${row0Index + 1}/${searcher.allRow0.length}: ${rep.label}`);
    console.log(`row-0 cycle type: ${cycleType(rep.p)}`);
  }
  const diagnostic = searcher.diagnoseFirstBranches(branchLimit);
  console.log(`status: ${diagnostic.ok ? "ok" : "contradiction"}`);
  if (diagnostic.bestRow !== undefined) {
    console.log(`first row: ${diagnostic.bestRow}`);
    console.log(`first domain: ${diagnostic.bestDomainSize}`);
    console.log(`checked: ${diagnostic.checked}`);
    console.log(`dead after first row: ${diagnostic.dead}`);
    for (const sample of diagnostic.samples || []) {
      console.log(`sample ${sample.candidate} -> ${sample.next}`);
    }
    for (let col = 0; col < (diagnostic.aliveCellHist || []).length; col++) {
      const hist = diagnostic.aliveCellHist[col];
      if (!hist.length) continue;
      console.log(
        `alive first-row col ${col}: ` +
          hist.map(([value, count]) => `${value}:${count}`).join(" ")
      );
    }
    for (const [key, count] of diagnostic.histogram || []) {
      console.log(`${key}: ${count}`);
    }
  }
  console.log(`forced cells: ${diagnostic.stats.imposedCells}`);
  console.log(`domain checks: ${diagnostic.stats.domainChecks}`);
  runtimeProcess.exit(0);
}
if (mode === "domainhist") {
  console.log(`Strong best-domain diagnostic, size ${n}.`);
  if (row0Index !== undefined) {
    const rep = searcher.allRow0[row0Index];
    console.log(`row-0 case ${row0Index + 1}/${searcher.allRow0.length}: ${rep.label}`);
    console.log(`row-0 cycle type: ${cycleType(rep.p)}`);
  }
  const diagnostic = searcher.diagnoseBestDomain();
  console.log(`status: ${diagnostic.ok ? "ok" : "contradiction"}`);
  if (diagnostic.bestRow !== undefined) {
    console.log(`best row: ${diagnostic.bestRow}`);
    console.log(`best domain: ${diagnostic.bestDomainSize}`);
    for (const sample of diagnostic.samples || []) {
      console.log(`sample ${sample}`);
    }
    for (let col = 0; col < (diagnostic.hist || []).length; col++) {
      const hist = diagnostic.hist[col];
      if (!hist.length) continue;
      console.log(
        `domain col ${col}: ` +
          hist.map(([value, count]) => `${value}:${count}`).join(" ")
      );
    }
  }
  console.log(`forced cells: ${diagnostic.stats.imposedCells}`);
  console.log(`domain checks: ${diagnostic.stats.domainChecks}`);
  runtimeProcess.exit(0);
}
if (mode === "cellscores") {
  console.log(`Strong cell-score diagnostic, size ${n}.`);
  if (row0Index !== undefined) {
    const rep = searcher.allRow0[row0Index];
    console.log(`row-0 case ${row0Index + 1}/${searcher.allRow0.length}: ${rep.label}`);
    console.log(`row-0 cycle type: ${cycleType(rep.p)}`);
  }
  const diagnostic = searcher.diagnoseCellScores();
  console.log(`status: ${diagnostic.ok ? "ok" : "contradiction"}`);
  if (diagnostic.ok) {
    for (const score of diagnostic.scores || []) {
      console.log(
        `cell ${score.row}*${score.col}: domain ${score.domainSize}, distinct ${score.distinct}, min ${score.minCount}, max ${score.maxCount}; ` +
          score.entries.map(([value, count]) => `${value}:${count}`).join(" ")
      );
    }
  }
  console.log(`forced cells: ${diagnostic.stats.imposedCells}`);
  console.log(`domain checks: ${diagnostic.stats.domainChecks}`);
  runtimeProcess.exit(0);
}
if (mode === "rowscores") {
  console.log(`Strong row-limited cell-score diagnostic, size ${n}.`);
  if (row0Index !== undefined) {
    const rep = searcher.allRow0[row0Index];
    console.log(`row-0 case ${row0Index + 1}/${searcher.allRow0.length}: ${rep.label}`);
    console.log(`row-0 cycle type: ${cycleType(rep.p)}`);
  }
  console.log(`target rows: ${rowScoreTargets.join(",")}`);
  const diagnostic = searcher.diagnoseCellScoresForRows(rowScoreTargets);
  console.log(`status: ${diagnostic.ok ? "ok" : "contradiction"}`);
  if (diagnostic.ok) {
    for (const score of diagnostic.scores || []) {
      console.log(
        `cell ${score.row}*${score.col}: domain ${score.domainSize}, distinct ${score.distinct}, min ${score.minCount}, max ${score.maxCount}; ` +
          score.entries.map(([value, count]) => `${value}:${count}`).join(" ")
      );
    }
  }
  console.log(`forced cells: ${diagnostic.stats.imposedCells}`);
  console.log(`domain checks: ${diagnostic.stats.domainChecks}`);
  runtimeProcess.exit(0);
}
if (mode === "rowhist") {
  console.log(`Strong row-domain diagnostic, size ${n}.`);
  if (row0Index !== undefined) {
    const rep = searcher.allRow0[row0Index];
    console.log(`row-0 case ${row0Index + 1}/${searcher.allRow0.length}: ${rep.label}`);
    console.log(`row-0 cycle type: ${cycleType(rep.p)}`);
  }
  const diagnostic = searcher.diagnoseRowDomain(rowHistTarget);
  console.log(`status: ${diagnostic.ok ? "ok" : "contradiction"}`);
  if (diagnostic.ok) {
    console.log(`row: ${diagnostic.row}`);
    console.log(`domain: ${diagnostic.domainSize}`);
    if (diagnostic.assigned) console.log(`assigned: ${diagnostic.assigned}`);
    for (const sample of diagnostic.samples || []) {
      console.log(`sample ${sample}`);
    }
    for (let col = 0; col < (diagnostic.hist || []).length; col++) {
      const hist = diagnostic.hist[col];
      if (!hist.length) continue;
      console.log(
        `domain col ${col}: ` +
          hist.map(([value, count]) => `${value}:${count}`).join(" ")
      );
    }
  }
  console.log(`forced cells: ${diagnostic.stats.imposedCells}`);
  console.log(`domain checks: ${diagnostic.stats.domainChecks}`);
  runtimeProcess.exit(0);
}
if (mode === "nonidempotent") {
  console.log(`Strong search for non-idempotent E677 model, size ${n}.`);
  console.log("Element 0 is normalized so 0*0 != 0.");
} else {
  console.log(`Strong search for E677 counterexample to E255, size ${n}.`);
  console.log("Bad element is normalized to 0.");
}
if (row0Index !== undefined) {
  const rep = searcher.allRow0[row0Index];
  console.log(`row-0 case ${row0Index + 1}/${searcher.allRow0.length}: ${rep.label}`);
  console.log(`row-0 cycle type: ${cycleType(rep.p)}`);
}
const result = searcher.run();
console.log(`status: ${result.status}`);
console.log(`time: ${(result.ms / 1000).toFixed(2)}s`);
console.log(`nodes: ${result.stats.nodes}`);
console.log(`dead ends: ${result.stats.deadEnds}`);
console.log(`forced rows: ${result.stats.forcedRows}`);
console.log(`forced cells: ${result.stats.imposedCells}`);
console.log(`domain checks: ${result.stats.domainChecks}`);
console.log(`row-0 representative count: ${result.row0Count}`);
if (result.table) {
  if (result.e255 !== undefined) console.log(`E255 on found table: ${result.e255}`);
  console.log("counterexample table:");
  console.log(result.table);
}
