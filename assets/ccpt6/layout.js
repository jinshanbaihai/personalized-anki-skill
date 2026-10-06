/* ccmap — offline layout for deep mind maps and causal chains on Anki cards.
   No dependencies; plain DOM + SVG; runs in Anki desktop (Qt WebEngine), AnkiDroid
   (Android WebView) and AnkiMobile (WKWebView).

   Two map layouts from one authored tree:
     logic   — left-to-right logic chart (XMind "logic chart" style). Non-layered tidy tree:
               each child column starts right after its own parent, subtrees never overlap,
               a parent sits midway between its first and last child (or level with its first
               child when that span is taller than the screen), and sibling subtrees are packed
               by contour (skyline), so a short branch does not reserve a tall empty band.
     outline — indented tree with vertical rails; the indent step shrinks with the width so
               the text column never drops below a readable measure.
   "auto": full logic chart → narrower nodes → logic chart in which only the branches that
   do not fit fold into an indented outline inside their box ("adaptive fold frontier") →
   full outline. Text is never scaled to fit.

   Relation words sit ON the connector, never only in a tooltip. Causal words get arrowheads
   (因为/取决于 point back to the parent), conditions are dashed, evaluations dotted, examples
   thin. The word is always printed; line style is a redundant cue.

   Causal chain: A →(导致) B →(仅当 …) C with forks, joins and condition side notes. Laid out
   in rows (wrapping with a return connector) when it fits, otherwise a vertical flow.

   API (window.CCMap): mapHTML(json) · chainHTML(json) · render(el, json, opts) ·
   renderChain(el, json, opts) · mount(scope) · tidy(tree, opts) · audit(scope) · cleanup()
*/
(function (G) {
'use strict';
const SVGNS = 'http://www.w3.org/2000/svg';
const DEF = {
  layout: 'auto',      // auto | logic | outline
  edge: 'curve',       // curve | elbow
  compact: true,       // contour packing of sibling subtrees (false = bounding-box bands)
  fold: true,          // false: never fold branches into outlines (scroll sideways instead when layout = logic)
  topAlign: 'auto',    // auto | center | top — auto: a parent whose children span > topAlignPx sits level with its first child
  topAlignPx: 600,
  nodeMax: 300,        // widest node box in the logic chart (px)
  nodeMin: 210,        // narrowest we accept before folding (≈ 13 CJK chars at 16px)
  inlineMax: 560,      // folded-outline box cap (≈ 34 CJK chars per line)
  foldText: 190,       // narrowest text column inside a folded box
  foldStep: 22,        // indent per level inside a folded box (indent 10 + elbow 12, see CSS)
  curveW: 30,          // horizontal room for the curved / elbow part of a connector
  stubMin: 22,         // shortest straight run into a child
  labelPad: 6,         // gap between the line and a relation word
  arrow: 9,            // arrowhead length
  vgap: 10,            // gap between sibling leaves
  branchGap: 14,       // extra gap when either sibling has children
  narrow: 600,         // auto: narrower containers use the outline
  stepMax: 34, stepMin: 12, // outline: indent per level (rail indent + elbow)
  tallRatio: 1.15,     // auto: a logic chart this much taller than the outline loses
  chainMax: 230, chainMin: 190, rowGap: 34
};

/* ---------- relation words → connector semantics ---------- */
const REL_RULES = [
  [/^(当且仅当|仅当|只有|如果|假如|若|只要|前提|条件|假设|当|only if|if|when|provided|unless)/i, {arrow: 'none', line: 'dashed', tone: 'cond'}],
  [/^(因为|由于|源于|取决于|来自|基于|because|since|due to|depends on)/i, {arrow: 'back', line: 'solid', tone: 'cause'}],
  [/^(导致|引起|造成|使得|使|所以|因此|从而|进而|于是|推出|得到|带来|意味着|则|因而|结果|以致|引发|诱发|促进|推动|产生|加剧|抑制|提高|降低|增加|减少|形成|刺激|迫使|→|⇒|leads? to|causes?|so|therefore|hence|thus|results? in|raises?|reduces?|increases?|decreases?)/i, {arrow: 'forward', line: 'solid', tone: 'cause'}],
  [/^(但是|但|然而|不过|却|反之|可是|局限|评价|however|but|yet|although)/i, {arrow: 'none', line: 'dotted', tone: 'eval'}],
  [/^(例如|比如|譬如|如|例|e\.g\.|for example|such as)/i, {arrow: 'none', line: 'thin', tone: 'example'}]
];
function relSemantics(text, kind, over) {
  let s = {arrow: kind === 'effect' || kind === 'step' ? 'forward' : 'none', line: 'solid', tone: 'plain'};
  const t = String(text || '').replace(/<[^>]*>/g, '').trim();
  if (t) for (const [re, v] of REL_RULES) if (re.test(t)) { s = Object.assign({}, v); break; }
  if (over && over.arrow) s.arrow = over.arrow;
  if (over && over.line) s.line = over.line;
  return s;
}
const KINDS = ['root', 'topic', 'definition', 'cause', 'effect', 'condition', 'evaluation', 'example', 'step', 'contrast', 'policy', 'limit', 'note'];

/* ---------- markup builders (a generator can emit the same markup server-side) ---------- */
function mapHTML(json, opts) {
  opts = opts || {};
  let n = 0;
  const prefix = opts.idPrefix || 'mm';
  const node = (d, depth, branch) => {
    const kind = KINDS.includes(d.kind) ? d.kind : (depth ? 'topic' : 'root');
    const sem = relSemantics(d.rel, kind, d);
    const id = d.id || prefix + '-n' + (n++);
    const kids = (d.children || []).map((c, i) => node(c, depth + 1, depth === 0 ? i : branch)).join('');
    const b = depth === 0 ? 'root' : branch % 6;
    return '<li class="mm-item' + (d.rel ? ' has-rel' : '') + '" data-kind="' + kind + '" data-depth="' + depth + '" data-branch="' + b +
      '" data-arrow="' + sem.arrow + '" data-line="' + sem.line + '" data-tone="' + sem.tone + '">' +
      (d.rel ? '<span class="mm-rel">' + d.rel + '</span>' : '') +
      '<div class="mm-node" data-kind="' + kind + '" data-node="' + id + '">' + (d.ao ? '<span class="ao-badge">' + d.ao + '</span>' : '') + d.text + '</div>' +
      (kids ? '<ul>' + kids + '</ul>' : '') + '</li>';
  };
  return '<ul class="mm-tree">' + node(json, 0, 0) + '</ul>';
}

function chainHTML(json, opts) {
  opts = opts || {};
  let n = 0;
  const prefix = opts.idPrefix || 'ch';
  const seq = (items, cls) => '<ol class="ch-seq' + (cls ? ' ' + cls : '') + '">' + items.map(item).join('') + '</ol>';
  const item = d => {
    if (d.fork) return '<li class="ch-fork" data-n="' + d.fork.length + '">' + d.fork.map(b => seq(b, 'ch-branch')).join('') + '</li>';
    const kind = KINDS.includes(d.kind) ? d.kind : 'topic';
    const sem = relSemantics(d.rel || '', kind, d);
    if (d.rel && sem.tone === 'plain' && !d.arrow) sem.arrow = 'forward';
    return '<li class="ch-item" data-kind="' + kind + '" data-arrow="' + sem.arrow + '" data-line="' + sem.line + '" data-tone="' + sem.tone + '">' +
      (d.rel ? '<span class="ch-rel">' + d.rel + '</span>' : '') +
      (d.cond ? '<span class="ch-cond">' + d.cond + '</span>' : '') +
      '<div class="ch-node" data-kind="' + kind + '" data-node="' + (d.id || prefix + '-c' + (n++)) + '">' + (d.ao ? '<span class="ao-badge">' + d.ao + '</span>' : '') + d.text +
      (d.note ? '<div class="ch-note">' + d.note + '</div>' : '') + '</div></li>';
  };
  return '<div class="ccchain" data-dir="' + (opts.dir || json.dir || 'auto') + '">' + seq(json.items || json) + '</div>';
}

/* ---------- skyline profiles: sorted disjoint [x0, x1, top, bottom] ---------- */
function shift(p, dx, dy) { return p.map(s => [s[0] + dx, s[1] + dx, s[2] + dy, s[3] + dy]); }
function bbox(p) {
  let a = Infinity, b = -Infinity, t = Infinity, u = -Infinity;
  for (const s of p) { a = Math.min(a, s[0]); b = Math.max(b, s[1]); t = Math.min(t, s[2]); u = Math.max(u, s[3]); }
  return [[a, b, t, u]];
}
function merge(ps) {
  ps = ps.filter(p => p && p.length);
  if (ps.length === 1) return ps[0];
  const xs = [];
  for (const p of ps) for (const s of p) xs.push(s[0], s[1]);
  xs.sort((a, b) => a - b);
  const idx = ps.map(() => 0), out = [];
  for (let i = 0; i + 1 < xs.length; i++) {
    const a = xs[i], b = xs[i + 1];
    if (b - a < 1e-6) continue;
    const m = (a + b) / 2;
    let top = Infinity, bot = -Infinity;
    for (let j = 0; j < ps.length; j++) {
      const p = ps[j];
      let k = idx[j];
      while (k < p.length && p[k][1] <= m) k++;
      idx[j] = k;
      if (k < p.length && p[k][0] <= m) { if (p[k][2] < top) top = p[k][2]; if (p[k][3] > bot) bot = p[k][3]; }
    }
    if (top === Infinity) continue;
    const last = out[out.length - 1];
    if (last && Math.abs(last[1] - a) < 1e-6 && last[2] === top && last[3] === bot) last[1] = b;
    else out.push([a, b, top, bot]);
  }
  return out;
}
// smallest dy so that b (moved down by dy) clears a wherever their x-ranges overlap
function separation(a, b) {
  let i = 0, j = 0, d = -Infinity;
  while (i < a.length && j < b.length) {
    const lo = Math.max(a[i][0], b[j][0]), hi = Math.min(a[i][1], b[j][1]);
    if (hi - lo > 0.5) d = Math.max(d, a[i][3] - b[j][2]);
    if (a[i][1] < b[j][1]) i++; else j++;
  }
  return d === -Infinity ? 0 : d;
}

/* ---------- pure logic-chart layout ----------
   tree nodes: {w, h, lw, lh, arrow, vis:[children drawn as chart nodes]} → sets x, y (box top-left)
   and returns {width, height}. O(n·k) where k is the profile length (≤ number of columns). */
function tidy(root, o) {
  o = Object.assign({}, DEF, o || {});
  const topOver = o.topAlignOver || 0;
  function sub(t) {
    t.ay = t.h / 2;
    const own = [[0, t.w, 0, t.h]];
    if (!t.vis || !t.vis.length) { t.prof = own; return; }
    let stub = o.stubMin;
    for (const k of t.vis) {
      sub(k);
      if (k.lw) stub = Math.max(stub, k.lw + 2 * o.labelPad + 8 + (k.arrow !== 'none' ? o.arrow : 0));
    }
    t.stub = stub;
    let acc = null, prev = null;
    const offs = [];
    for (const k of t.vis) {
      const half = k.lw ? k.lh / 2 + 2 : 2;
      let p = merge([k.prof, [[-stub, 0, k.ay - half, k.ay + half]]]);
      if (!o.compact) p = bbox(p);
      let off = 0;
      if (acc) off = separation(acc, p) + o.vgap + ((prev.vis && prev.vis.length) || (k.vis && k.vis.length) ? o.branchGap : 0);
      offs.push(off);
      acc = acc ? merge([acc, shift(p, 0, off)]) : p;
      prev = k;
    }
    const a0 = offs[0] + t.vis[0].ay, a1 = offs[offs.length - 1] + t.vis[t.vis.length - 1].ay;
    const dy = topOver && a1 - a0 > topOver ? t.ay - a0 : t.ay - (a0 + a1) / 2;
    t.kx = t.w + o.curveW + stub;
    t.koffs = offs.map(v => v + dy);
    t.prof = merge([own, [[t.w, t.w + o.curveW, Math.min(t.ay, a0 + dy) - 1, Math.max(t.ay, a1 + dy) + 1]], shift(acc, t.kx, dy)]);
  }
  sub(root);
  let minY = Infinity, maxY = -Infinity, maxX = 0;
  for (const s of root.prof) { minY = Math.min(minY, s[2]); maxY = Math.max(maxY, s[3]); maxX = Math.max(maxX, s[1]); }
  (function place(t, x, y) {
    t.x = x; t.y = y;
    if (t.vis) t.vis.forEach((k, i) => place(k, x + t.kx, y + t.koffs[i]));
  })(root, 0, -minY);
  return {width: Math.ceil(maxX), height: Math.ceil(maxY - minY)};
}

/* ---------- helpers ---------- */
const el = (tag, cls) => { const e = document.createElement(tag); if (cls) e.className = cls; return e; };
const rectOf = e => { const r = e.getBoundingClientRect(); return {w: Math.ceil(r.width * 2) / 2, h: Math.ceil(r.height * 2) / 2}; };
function roundPoly(pts, r) {
  let d = 'M' + pts[0][0] + ' ' + pts[0][1];
  for (let i = 1; i < pts.length - 1; i++) {
    const [x0, y0] = pts[i - 1], [x1, y1] = pts[i], [x2, y2] = pts[i + 1];
    const l1 = Math.hypot(x1 - x0, y1 - y0), l2 = Math.hypot(x2 - x1, y2 - y1);
    if (l1 < 0.5 || l2 < 0.5) continue;
    const rr = Math.min(r, l1 / 2, l2 / 2);
    d += 'L' + (x1 - (x1 - x0) / l1 * rr) + ' ' + (y1 - (y1 - y0) / l1 * rr) + 'Q' + x1 + ' ' + y1 + ' ' + (x1 + (x2 - x1) / l2 * rr) + ' ' + (y1 + (y2 - y1) / l2 * rr);
  }
  const p = pts[pts.length - 1];
  return d + 'L' + p[0] + ' ' + p[1];
}
const tri = (x, y, dir, len) => 'M' + x + ' ' + y + 'L' + (x - dir * len) + ' ' + (y - len * 0.55) + 'L' + (x - dir * len) + ' ' + (y + len * 0.55) + 'Z';
const live = new Set();
function observe(state, run) {
  let lastW = -1, frame = 0;
  const go = force => {
    cancelAnimationFrame(frame);
    frame = requestAnimationFrame(() => {
      const w = state.root.clientWidth;
      if (!force && Math.abs(w - lastW) < 1) return;
      lastW = w; run();
    });
  };
  const ro = typeof ResizeObserver === 'function' ? new ResizeObserver(() => go(false)) : null;
  const onWin = () => go(false);
  if (ro) ro.observe(state.root); else window.addEventListener('resize', onWin);
  // Measure with the real fonts: re-run when web fonts (incl. math fonts) or images arrive.
  const refont = () => { state.dirty = true; go(true); };
  if (document.fonts) {
    document.fonts.ready.then(refont);
    if (document.fonts.addEventListener) document.fonts.addEventListener('loadingdone', refont);
  }
  state.root.querySelectorAll('img').forEach(img => { if (!img.complete) img.addEventListener('load', refont, {once: true}); });
  state.dispose = () => {
    if (ro) ro.disconnect(); else window.removeEventListener('resize', onWin);
    cancelAnimationFrame(frame);
    if (document.fonts && document.fonts.removeEventListener) document.fonts.removeEventListener('loadingdone', refont);
  };
  live.add(state);
  lastW = state.root.clientWidth;
  run();
}

/* ---------- mind map ---------- */
function parseItem(li, depth, branch) {
  const t = {li, depth, branch, kind: li.dataset.kind || (depth ? 'topic' : 'root'),
    node: li.querySelector(':scope>.mm-node'), rel: li.querySelector(':scope>.mm-rel'), ul: li.querySelector(':scope>ul'), kids: []};
  if (!li.dataset.arrow) {
    const s = relSemantics(t.rel ? t.rel.textContent : '', t.kind);
    li.dataset.arrow = s.arrow; li.dataset.line = s.line; li.dataset.tone = s.tone;
  }
  t.arrow = li.dataset.arrow; t.line = li.dataset.line || 'solid'; t.tone = li.dataset.tone || 'plain';
  if (!li.dataset.branch) li.dataset.branch = depth ? branch % 6 : 'root';
  if (t.rel) li.classList.add('has-rel');
  if (t.node && !t.node.dataset.kind) t.node.dataset.kind = t.kind;
  if (t.ul) t.kids = [...t.ul.children].filter(c => c.matches('li.mm-item')).map((c, i) => parseItem(c, depth + 1, depth === 0 ? i : branch));
  t.below = t.kids.length ? 1 + Math.max(...t.kids.map(k => k.below)) : 0;   // levels under this node
  return t;
}
function walk(t, f) { f(t); t.kids.forEach(k => walk(k, f)); }

function restoreMap(st) {
  if (!st.canvas) return;
  walk(st.tree, t => {
    t.li.insertBefore(t.node, t.ul || null);
    if (t.rel) t.li.insertBefore(t.rel, t.node);
    t.box = t.lab = null;
  });
  st.canvas.remove(); st.canvas = null;
  st.list.style.display = '';
  st.root.classList.remove('is-logic', 'is-scroll');
}

// Outline: indent step = rail indent + elbow. It shrinks with the width; past the deepest level
// that still leaves a readable text column, further levels stop indenting (and say their depth).
function outlineIndent(st, avail) {
  const o = st.opts, d = Math.max(1, st.depth);
  const minText = Math.max(190, Math.min(260, Math.round(avail * 0.6)));
  const step = Math.max(o.stepMin, Math.min(o.stepMax, Math.floor((avail - minText) / d)));
  const elbow = Math.max(8, Math.min(16, Math.round(step * 0.5)));
  st.root.style.setProperty('--mm-indent', (step - elbow) + 'px');
  st.root.style.setProperty('--mm-elbow', elbow + 'px');
  const cap = Math.max(1, Math.floor((avail - minText) / step));
  walk(st.tree, t => { if (t.ul) t.ul.classList.toggle('mm-flat', t.depth + 1 > cap); t.li.classList.toggle('mm-deep', t.depth > cap); });
  return {step, cap};
}

function foldMin(o, t) { return o.foldText + 26 + t.below * o.foldStep; }

// folded branch: the node's descendants as an indented outline inside its chart box
function inlineOutline(t) {
  const ul = el('ul', 'mm-inline');
  for (const k of t.kids) {
    const li = el('li', 'mm-item' + (k.rel ? ' has-rel' : ''));
    for (const a of ['kind', 'depth', 'branch', 'arrow', 'line', 'tone']) li.dataset[a] = k.li.dataset[a];
    if (k.rel) li.appendChild(k.rel);
    li.appendChild(k.node);
    if (k.kids.length) li.appendChild(inlineOutline(k));
    ul.appendChild(li);
  }
  return ul;
}

// Width of t's subtree drawn fully as a chart, estimated from natural widths (no DOM work).
function estimate(st, t, nm) {
  const o = st.opts, w = Math.min(t.nat, nm);
  if (!t.kids.length) return w;
  let stub = o.stubMin, best = 0;
  for (const k of t.kids) {
    best = Math.max(best, estimate(st, k, nm));
    if (k.natLw) stub = Math.max(stub, k.natLw + 2 * o.labelPad + 8 + (k.arrow !== 'none' ? o.arrow : 0));
  }
  return w + o.curveW + stub + best;
}
// Adaptive fold frontier: keep as much chart structure as fits; fold only the branches that do not.
function chooseFolds(st, nm, avail) {
  const o = st.opts;
  avail -= 8;   // estimates come from natural widths; keep a little slack
  const visit = (t, x) => {
    if (x + estimate(st, t, nm) <= avail) return [];
    if (t.kids.length && x + Math.min(t.nat, nm) <= avail) {
      let stub = o.stubMin;
      for (const k of t.kids) if (k.natLw) stub = Math.max(stub, k.natLw + 2 * o.labelPad + 8 + (k.arrow !== 'none' ? o.arrow : 0));
      const xk = x + Math.min(t.nat, nm) + o.curveW + stub;
      let acc = [], ok = true;
      for (const k of t.kids) { const r = visit(k, xk); if (!r) { ok = false; break; } acc = acc.concat(r); }
      if (ok) return acc;
    }
    if (t.depth >= 1 && t.kids.length && x + Math.max(foldMin(o, t), Math.min(t.nat, nm)) <= avail) return [t];
    return null;
  };
  const r = visit(st.tree, 0);
  return r && r.length ? new Set(r) : null;
}

function buildLogic(st, cfg, avail) {
  const o = st.opts, canvas = el('div', 'mm-canvas');
  const svg = document.createElementNS(SVGNS, 'svg');
  svg.setAttribute('class', 'mm-wires'); svg.setAttribute('aria-hidden', 'true');
  canvas.appendChild(svg);
  const shown = [];
  const visit = t => {
    const box = el('div', 'mm-box');
    box.dataset.kind = t.kind; box.dataset.depth = t.depth; box.dataset.branch = t.li.dataset.branch;
    box.appendChild(t.node);
    const fold = !!(cfg.folds && cfg.folds.has(t));
    if (fold) { box.appendChild(inlineOutline(t)); box.classList.add('has-inline'); box.style.maxWidth = Math.max(foldMin(o, t), cfg.nodeMax) + 'px'; }
    else box.style.maxWidth = cfg.nodeMax + 'px';
    canvas.appendChild(box); t.box = box;
    t.lab = null;
    if (t.rel && t.depth) {
      const lab = el('div', 'mm-label');
      lab.dataset.tone = t.tone; lab.dataset.arrow = t.arrow; lab.dataset.branch = t.li.dataset.branch;
      lab.appendChild(t.rel); canvas.appendChild(lab); t.lab = lab;
    }
    t.vis = fold ? [] : t.kids;
    shown.push(t);
    t.vis.forEach(visit);
  };
  visit(st.tree);
  st.list.style.display = 'none';
  st.root.appendChild(canvas);
  st.canvas = canvas;
  const measure = list => {
    for (const t of list) {
      const r = rectOf(t.box); t.w = r.w; t.h = r.h;
      if (t.lab) { const q = rectOf(t.lab); t.lw = q.w; t.lh = q.h; } else { t.lw = 0; t.lh = 0; }
    }
  };
  measure(shown);
  if (!cfg.folds && cfg.nodeMax === o.nodeMax) for (const t of shown) { t.nat = t.w; t.natLw = t.lw; }
  let size = tidy(st.tree, o);
  // each folded box takes the rest of its row (capped): wider is shorter
  const folded = shown.filter(t => t.box.classList.contains('has-inline'));
  if (folded.length) {
    for (const t of folded) t.box.style.maxWidth = Math.floor(Math.max(foldMin(o, t), Math.min(o.inlineMax, avail - t.x - 2))) + 'px';
    measure(folded);
    size = tidy(st.tree, o);
  }
  return {shown, size, cfg};
}

function wirePath(o, x1, y1, xs, y2) {
  if (o.edge === 'elbow') {
    const xt = x1 + o.curveW / 2;
    if (Math.abs(y2 - y1) < 1) return 'M' + x1 + ' ' + y1 + 'H' + xs;
    return roundPoly([[x1, y1], [xt, y1], [xt, y2], [xs, y2]], 8);
  }
  const c = (xs - x1) * 0.55;
  return 'M' + x1 + ' ' + y1 + 'C' + (x1 + c) + ' ' + y1 + ',' + (xs - c) + ' ' + y2 + ',' + xs + ' ' + y2;
}

// the straight run into a node: relation word centred on it, line broken around the word
function labelledRun(o, xs, y, x2, e, cls, headCls) {
  const fwd = e.arrow === 'forward', back = e.arrow === 'back';
  const start = back ? xs + o.arrow : xs, end = fwd ? x2 - o.arrow : x2 - 1;
  let d, out = '';
  if (e.lab) {
    const lx = Math.round((start + end) / 2 - e.lw / 2), ly = Math.round(y - e.lh / 2);
    e.lab.style.left = lx + 'px'; e.lab.style.top = ly + 'px';
    d = 'M' + start + ' ' + y + 'H' + (lx - o.labelPad + 2) + 'M' + (lx + e.lw + o.labelPad - 2) + ' ' + y + 'H' + end;
  } else d = 'M' + start + ' ' + y + 'H' + end;
  if (e.cbox) { e.cbox.style.left = Math.round((start + end) / 2 - e.cw / 2) + 'px'; e.cbox.style.top = Math.round(y + (e.lh ? e.lh / 2 : 2) + 6) + 'px'; }
  out += '<path class="' + cls + '" d="' + d + '"/>';
  if (fwd) out += '<path class="' + headCls + '" d="' + tri(x2 - 1, y, 1, o.arrow) + '"/>';
  if (back) out += '<path class="' + headCls + '" d="' + tri(xs, y, -1, o.arrow) + '"/>';
  return out;
}

function paintLogic(st, res) {
  const o = st.opts, {shown, size} = res, canvas = st.canvas, svg = canvas.querySelector('svg');
  let paths = '';
  for (const t of shown) {
    t.box.style.left = t.x + 'px'; t.box.style.top = t.y + 'px';
    for (const k of t.vis) {
      const b = k.li.dataset.branch, x1 = t.x + t.w, y1 = t.y + t.ay, xs = t.x + t.w + o.curveW, y2 = k.y + k.ay;
      const cls = 'mm-wire b' + b + ' l-' + k.line + ' t-' + k.tone;
      paths += '<path class="' + cls + '" d="' + wirePath(o, x1, y1, xs, y2) + '"/>' + labelledRun(o, xs, y2, k.x, k, cls, 'mm-head b' + b);
    }
  }
  canvas.style.width = size.width + 'px'; canvas.style.height = size.height + 'px';
  svg.setAttribute('width', size.width); svg.setAttribute('height', size.height);
  svg.setAttribute('viewBox', '0 0 ' + size.width + ' ' + size.height);
  svg.innerHTML = paths;
}

function layoutMap(st) {
  const t0 = performance.now(), o = st.opts, root = st.root;
  restoreMap(st);
  const avail = root.clientWidth, want = root.dataset.layout || o.layout;
  // fixed threshold (≈ 3/4 of a laptop viewport): the result must not change when the window only changes height
  o.topAlignOver = o.topAlign === 'center' ? 0 : o.topAlign === 'top' ? 1 : o.topAlignPx;
  let mode = 'outline', chosen = null, domTries = 0, skipped = 0;
  if (want !== 'outline' && st.tree.kids.length && !(want === 'auto' && avail < o.narrow)) {
    const outlineH = (outlineIndent(st, avail), st.list.offsetHeight);
    const mid = Math.round((o.nodeMax + o.nodeMin) / 2);
    const accept = res => res.size.width <= avail + 0.5 && !(want === 'auto' && res.size.height > outlineH * o.tallRatio);
    st.trace = [];
    const tryCfg = cfg => {
      domTries++;
      const r = buildLogic(st, cfg, avail);
      st.trace.push({nodeMax: cfg.nodeMax, folds: cfg.folds ? [...cfg.folds].map(t => t.depth).join(',') : '', w: r.size.width, h: r.size.height, outlineH});
      if (accept(r)) return r;
      restoreMap(st); return null;
    };
    // the full chart at nodeMax also records natural widths; once known, estimates replace DOM tries
    if (!st.natValid || st.dirty || estimate(st, st.tree, o.nodeMax) <= avail + 24) {
      chosen = tryCfg({nodeMax: o.nodeMax, folds: null});
      st.natValid = true; st.dirty = false;
    } else skipped++;
    for (const nm of [mid, o.nodeMin]) {
      if (chosen) break;
      if (estimate(st, st.tree, nm) > avail + 24) { skipped++; continue; }
      chosen = tryCfg({nodeMax: nm, folds: null});
    }
    for (const nm of o.fold === false ? [] : [mid, o.nodeMin]) {
      if (chosen) break;
      const folds = chooseFolds(st, nm, avail);
      if (!folds) { skipped++; continue; }
      chosen = tryCfg({nodeMax: nm, folds});
    }
    if (!chosen && want === 'logic') {      // the author insisted: keep the chart and scroll sideways
      domTries++;
      chosen = buildLogic(st, {nodeMax: avail < o.narrow ? o.nodeMin : o.nodeMax, folds: null}, avail);
    }
    if (chosen) mode = chosen.size.width > avail + 0.5 ? 'logic-scroll' : chosen.cfg.folds ? 'logic+outline' : 'logic';
  }
  if (chosen) {
    paintLogic(st, chosen);
    root.classList.add('is-logic');
    root.classList.toggle('is-scroll', mode === 'logic-scroll');
    root.dataset.folds = chosen.cfg.folds ? [...chosen.cfg.folds].map(t => t.depth).join(',') : '';
    root.dataset.nodeMax = chosen.cfg.nodeMax;
  } else outlineIndent(st, avail);
  root.dataset.applied = mode;
  st.stats = {mode, ms: +(performance.now() - t0).toFixed(2), domTries, skipped, avail, nodes: st.count, depth: st.depth,
    width: chosen ? chosen.size.width : avail, height: root.offsetHeight};
}

function mountMap(root, opts) {
  if (root._ccmap) { layoutMap(root._ccmap); return root._ccmap; }
  const list = root.querySelector(':scope>.mm-tree');
  const first = list && list.querySelector(':scope>li.mm-item');
  if (!first) return null;
  root.classList.add('ccmm');
  const o = Object.assign({}, DEF, opts || {});
  if (root.dataset.edge) o.edge = root.dataset.edge;
  if (root.dataset.compact) o.compact = root.dataset.compact !== 'false';
  if (root.dataset.topAlign) o.topAlign = root.dataset.topAlign;
  if (root.dataset.fold) o.fold = root.dataset.fold !== 'false';
  const st = {root, list, opts: o, canvas: null, tree: parseItem(first, 0, 0)};
  let depth = 0, count = 0;
  walk(st.tree, t => { depth = Math.max(depth, t.depth); count++; });
  st.depth = depth; st.count = count;
  root.dataset.depth = depth;
  root._ccmap = st;
  observe(st, () => layoutMap(st));
  return st;
}

/* ---------- causal chain ---------- */
function parseSeq(ol) {
  return [...ol.children].map(li => {
    if (li.classList.contains('ch-fork')) return {type: 'fork', li, branches: [...li.children].filter(c => c.matches('ol.ch-seq')).map(parseSeq)};
    return {type: 'node', li, node: li.querySelector(':scope>.ch-node'), rel: li.querySelector(':scope>.ch-rel'), cond: li.querySelector(':scope>.ch-cond'),
      arrow: li.dataset.arrow || 'forward', line: li.dataset.line || 'solid', tone: li.dataset.tone || 'cause'};
  });
}
function forEachNode(seq, f) { for (const e of seq) { if (e.type === 'node') f(e); else e.branches.forEach(b => forEachNode(b, f)); } }

/* pure chain layout on measured sizes. Top level may wrap into rows when avail is given. */
function chainLayout(seq, o, avail) {
  const P = o.labelPad, A = o.arrow;
  const edgeRoom = e => Math.max(o.stubMin + A, (e.lw || 0) + 2 * P + 10 + (e.arrow !== 'none' ? A : 0), e.cw ? e.cw + 12 : 0);
  const above = e => (e.lh ? e.lh / 2 : 2);
  const below = e => (e.lh ? e.lh / 2 : 2) + (e.ch ? e.ch + 6 : 0);
  function size(s) {
    s.forEach((e, i) => {
      if (e.type === 'node') {
        e.gapIn = i ? (s[i - 1].type === 'fork' ? o.curveW : 0) + edgeRoom(e) : 0;
        e.bodyW = e.w;
        e.up = Math.max(e.h / 2, e.lw || e.cw ? above(e) : 0); e.down = Math.max(e.h / 2, e.lw || e.cw ? below(e) : 0);
      } else {
        let bw = 0, bh = 0, room = 0;
        e.branches.forEach(b => { size(b); bw = Math.max(bw, b.w); const f = b[0]; if (f.type === 'node') room = Math.max(room, edgeRoom(f)); });
        e.branches.forEach((b, j) => { b.top = bh; bh += b.up + b.down + (j < e.branches.length - 1 ? o.vgap + 8 : 0); });
        e.split = i ? o.curveW + room : 0;
        e.gapIn = e.split; e.bodyW = bw; e.bw = bw; e.bh = bh;
        e.up = e.down = bh / 2;
      }
    });
    s.w = s.reduce((a, e) => a + e.gapIn + e.bodyW, 0);
    s.up = Math.max(...s.map(e => e.up)); s.down = Math.max(...s.map(e => e.down));
  }
  function placeRow(els, x, mid, lead) {
    els.forEach((e, k) => {
      const gap = k ? e.gapIn : lead;
      if (e.type === 'node') { x += gap; e.x = x; e.y = mid - e.h / 2; e.ay = mid; x += e.w; }
      else {
        e.x = x; e.top = mid - e.bh / 2;
        e.branches.forEach(b => placeRow(b, e.x + e.split, e.top + b.top + b.up, 0));
        x += e.split + e.bw;
      }
    });
    return x;
  }
  size(seq);
  const lead = e => edgeRoom(e) + 14;
  const limit = (avail || Infinity) - 16;
  const rows = [[]];
  let w = 0;
  for (const e of seq) {
    const row = rows[rows.length - 1];
    const add = row.length ? e.gapIn + e.bodyW : (rows.length > 1 ? lead(e) : 0) + e.bodyW;
    if (row.length && w + add > limit) {
      if (e.type === 'node') { rows.push([e]); w = lead(e) + e.bodyW; continue; }
      const last = row[row.length - 1];
      if (row.length >= 2 && last.type === 'node') { row.pop(); rows.push([last, e]); w = lead(last) + last.bodyW + e.gapIn + e.bodyW; continue; }
      return null;
    }
    row.push(e); w += add;
  }
  // rows must fit; a wrapped chain made mostly of one-node rows reads worse than the vertical flow
  const rowW = row => row.reduce((a, e, k) => a + (k ? e.gapIn : 0) + e.bodyW, 0);
  if (rows.some((row, r) => (r ? lead(row[0]) : 0) + rowW(row) > limit)) return null;
  if (rows.length > 1 && rows.filter(row => row.length === 1 && row[0].type === 'node').length > 1) return null;
  let y = 0, width = 0;
  rows.forEach((row, r) => {
    const up = Math.max(...row.map(e => e.up)), down = Math.max(...row.map(e => e.down));
    if (r) row[0].wrap = {yGap: y - o.rowGap / 2};
    const end = placeRow(row, 0, y + up, r ? lead(row[0]) : 0);
    width = Math.max(width, end + (rows.length > 1 ? 16 : 0));
    y += up + down + (r < rows.length - 1 ? o.rowGap : 0);
  });
  seq.forEach(e => { if (!rows.some((row, r) => r && row[0] === e)) delete e.wrap; });
  return {width: Math.ceil(width), height: Math.ceil(y), rows: rows.length};
}

function restoreChain(st) {
  if (st.canvas) { st.canvas.remove(); st.canvas = null; }
  forEachNode(st.seq, e => { e.li.appendChild(e.node); if (e.cond) e.li.insertBefore(e.cond, e.node); if (e.rel) e.li.insertBefore(e.rel, e.cond || e.node); e.lab = e.cbox = null; });
  st.list.style.display = '';
  st.root.classList.remove('is-row');
}

function layoutChain(st) {
  const t0 = performance.now(), o = st.opts, root = st.root;
  restoreChain(st);
  const avail = root.clientWidth, want = root.dataset.dir || 'auto';
  let mode = 'column', rows = 0;
  if (want !== 'column') {
    for (const nodeMax of [o.chainMax, o.chainMin]) {
      const canvas = el('div', 'ch-canvas'), svg = document.createElementNS(SVGNS, 'svg');
      svg.setAttribute('class', 'mm-wires'); svg.setAttribute('aria-hidden', 'true'); canvas.appendChild(svg);
      const nodes = [];
      forEachNode(st.seq, e => {
        const box = el('div', 'ch-box'); box.dataset.kind = e.node.dataset.kind || 'topic';
        box.style.maxWidth = nodeMax + 'px'; box.appendChild(e.node); canvas.appendChild(box); e.box = box;
        if (e.rel) { const l = el('div', 'mm-label'); l.dataset.tone = e.tone; l.dataset.arrow = e.arrow; l.appendChild(e.rel); canvas.appendChild(l); e.lab = l; } else e.lab = null;
        if (e.cond) { const c = el('div', 'ch-condbox'); c.appendChild(e.cond); canvas.appendChild(c); e.cbox = c; } else e.cbox = null;
        nodes.push(e);
      });
      st.list.style.display = 'none'; root.appendChild(canvas); st.canvas = canvas;
      for (const e of nodes) {
        const r = rectOf(e.box); e.w = r.w; e.h = r.h;
        if (e.lab) { const q = rectOf(e.lab); e.lw = q.w; e.lh = q.h; } else e.lw = e.lh = 0;
        if (e.cbox) { const q = rectOf(e.cbox); e.cw = q.w; e.ch = q.h; } else e.cw = e.ch = 0;
      }
      const size = chainLayout(st.seq, o, want === 'row' ? Infinity : avail);
      if (size && (size.width <= avail + 0.5 || want === 'row')) { paintChain(st, size); mode = size.rows > 1 ? 'rows' : 'row'; rows = size.rows; break; }
      restoreChain(st);
    }
  }
  root.classList.toggle('is-row', mode !== 'column');
  root.dataset.applied = mode;
  st.stats = {mode, rows, ms: +(performance.now() - t0).toFixed(2), avail};
}

function paintChain(st, size) {
  const o = st.opts, svg = st.canvas.querySelector('svg');
  let out = '', maxX = size.width;   // merge curves and row-return connectors may reach past the widest node
  const wire = (d, tone) => '<path class="mm-wire l-solid t-' + (tone || 'plain') + '" d="' + d + '"/>';
  const run = (xs, e) => labelledRun(o, xs, e.ay, e.x, e, 'mm-wire l-' + e.line + ' t-' + e.tone, 'mm-head t-' + e.tone);
  const bend = (x1, y1, x2, y2) => { if (Math.abs(y2 - y1) < 0.5) return 'M' + x1 + ' ' + y1 + 'H' + x2; const c = (x2 - x1) * 0.55; return 'M' + x1 + ' ' + y1 + 'C' + (x1 + c) + ' ' + y1 + ',' + (x2 - c) + ' ' + y2 + ',' + x2 + ' ' + y2; };
  const lastNodes = s => { const e = s[s.length - 1]; return e.type === 'node' ? [e] : e.branches.flatMap(lastNodes); };
  // where the flow leaves element p: a node's right edge, or a fork's merge point (branch ends gathered)
  const exitOf = (p, ty) => {
    if (p.type === 'node') return {x: p.x + p.w, y: p.ay};
    const xm = p.x + p.split + p.bw, ends = p.branches.flatMap(lastNodes);
    for (const q of ends) if (q.x + q.w < xm - 0.5) out += wire('M' + (q.x + q.w) + ' ' + q.ay + 'H' + xm);
    const ys = ends.map(q => q.ay), y = ty == null ? (Math.min(...ys) + Math.max(...ys)) / 2 : ty;
    ends.forEach(q => { out += wire(bend(xm, q.ay, xm + o.curveW, y)); });
    maxX = Math.max(maxX, xm + o.curveW + 2);
    return {x: xm + o.curveW, y, merged: true};
  };
  function draw(s) {
    s.forEach((e, i) => {
      if (e.type === 'node') {
        e.box.style.left = e.x + 'px'; e.box.style.top = e.y + 'px';
        if (!i) return;
        const ex = exitOf(s[i - 1], e.wrap ? null : e.ay);
        if (e.wrap) {   // return connector: right, down to the gap between rows, back to the left margin, down, then in
          out += wire(roundPoly([[ex.x, ex.y], [ex.x + 10, ex.y], [ex.x + 10, e.wrap.yGap], [6, e.wrap.yGap], [6, e.ay], [7, e.ay]], 9), e.tone);
          maxX = Math.max(maxX, ex.x + 12);
          out += run(7, e);
        } else out += run(ex.x, e);
      } else {
        e.branches.forEach(b => draw(b));
        if (!i) return;
        const ex = exitOf(s[i - 1]);
        for (const b of e.branches) { const f = b[0]; if (f.type !== 'node') continue; out += wire(bend(ex.x, ex.y, e.x + o.curveW, f.ay), f.tone); out += run(e.x + o.curveW, f); }
      }
    });
  }
  draw(st.seq);
  const width = Math.ceil(maxX);
  st.canvas.style.width = width + 'px'; st.canvas.style.height = size.height + 'px';
  svg.setAttribute('width', width); svg.setAttribute('height', size.height);
  svg.setAttribute('viewBox', '0 0 ' + width + ' ' + size.height);
  svg.innerHTML = out;
}

function mountChain(root, opts) {
  if (root._ccchain) { layoutChain(root._ccchain); return root._ccchain; }
  const list = root.querySelector(':scope>ol.ch-seq');
  if (!list) return null;
  const st = {root, list, opts: Object.assign({}, DEF, opts || {}), seq: parseSeq(list), canvas: null};
  root._ccchain = st;
  observe(st, () => layoutChain(st));
  return st;
}

/* ---------- audit (used by screenshot checks) ---------- */
function audit(scope) {
  scope = scope || document;
  const boxes = [...scope.querySelectorAll('.mm-box,.ch-box,.mm-label,.ch-condbox')].filter(b => b.offsetParent).map(b => ({b, r: b.getBoundingClientRect()}));
  const overlaps = [];
  for (let i = 0; i < boxes.length; i++) for (let j = i + 1; j < boxes.length; j++) {
    const a = boxes[i].r, c = boxes[j].r;
    if (a.left < c.right - 1 && a.right > c.left + 1 && a.top < c.bottom - 1 && a.bottom > c.top + 1)
      overlaps.push([boxes[i].b.textContent.trim().slice(0, 14), boxes[j].b.textContent.trim().slice(0, 14)]);
  }
  let minNode = 99, minLabel = 99, narrowest = 9999;
  const walker = document.createTreeWalker(scope.body || scope, NodeFilter.SHOW_TEXT);
  while (walker.nextNode()) {
    const n = walker.currentNode, p = n.parentElement;
    if (!n.textContent.trim() || !p || !p.closest('.mm-node,.ch-node,.mm-rel,.ch-rel,.ch-cond')) continue;
    if (p.closest('math,svg,.ao-badge,sub,sup')) continue;      // scripts and badges follow their own floors
    const r = document.createRange(); r.selectNodeContents(n);
    const b = r.getBoundingClientRect(); if (!b.width) continue;
    const f = parseFloat(getComputedStyle(p).fontSize);
    if (p.closest('.mm-rel,.ch-rel')) minLabel = Math.min(minLabel, f); else minNode = Math.min(minNode, f);
  }
  scope.querySelectorAll('.mm-node,.ch-node').forEach(nd => { if (nd.offsetParent) narrowest = Math.min(narrowest, nd.clientWidth); });
  return {overlaps, minNodeFont: minNode, minLabelFont: minLabel, narrowestNode: narrowest,
    pageOverflowX: document.documentElement.scrollWidth > document.documentElement.clientWidth + 1,
    maps: [...scope.querySelectorAll('.ccmm')].map(m => Object.assign({id: m.id, folds: m.dataset.folds}, m._ccmap ? m._ccmap.stats : {})),
    chains: [...scope.querySelectorAll('.ccchain')].map(m => Object.assign({id: m.id}, m._ccchain ? m._ccchain.stats : {}))};
}

const API = {
  defaults: DEF, relSemantics, mapHTML, chainHTML, tidy, merge, separation, chainLayout, audit,
  mount(scope) {
    scope = scope || document;
    scope.querySelectorAll('.mm').forEach(m => mountMap(m));
    scope.querySelectorAll('.ccchain').forEach(c => mountChain(c));
  },
  mountMap, mountChain,
  render(container, json, opts) {
    opts = opts || {};
    container.innerHTML = '<div class="mm ccmm" data-layout="' + (opts.layout || 'auto') + '"' + (opts.edge ? ' data-edge="' + opts.edge + '"' : '') + '>' + mapHTML(json, opts) + '</div>';
    return mountMap(container.firstChild, opts);
  },
  renderChain(container, json, opts) {
    container.innerHTML = chainHTML(json, opts);
    return mountChain(container.firstChild, opts);
  },
  relayout(root) { const s = root._ccmap || root._ccchain; if (s) (s.seq ? layoutChain : layoutMap)(s); return s && s.stats; },
  cleanup() { live.forEach(s => { if (s.dispose) s.dispose(); delete s.root._ccmap; delete s.root._ccchain; }); live.clear(); }
};
G.CCMap = API;
// drop-in adapter for the ccpt-6 player (player.js calls ccptLayout(root, signal) and ccptLayoutCleanup())
if (typeof window !== 'undefined') {   // always take the newest engine in a long-lived reviewer page
  G.ccptLayout = (root, signal) => { API.mount(root); if (signal) signal.addEventListener('abort', API.cleanup, {once: true}); };
  G.ccptLayoutCleanup = API.cleanup;
}
if (typeof module === 'object' && module.exports) module.exports = API;
})(typeof window !== 'undefined' ? window : globalThis);
