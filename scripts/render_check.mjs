// Render every preview page in real Chromium, screenshot it and collect ccptAudit().
// Usage: node scripts/render_check.mjs out/ [--only=ID,ID] [--dark] [--phone] [--play]
// --play also exercises the player: Space starts narration, highlight follows cues, the speed button toggles 2×/1.5×.
// Needs Playwright (npm i -g playwright, or NODE_PATH pointing at a global install) and a Chromium:
// CHROMIUM_PATH=/path/to/chrome overrides the browser (find one with: which chromium chromium-browser google-chrome).
// Screenshots show layout and typography only; Anki's desktop shortcuts are checked natively.
import fs from 'node:fs';
import path from 'node:path';
import { createRequire } from 'node:module';

const require = createRequire(import.meta.url);
function loadPlaywright() {
  const tries = ['playwright', '/opt/node22/lib/node_modules/playwright', ...(process.env.NODE_PATH || '').split(':').filter(Boolean).map(p => path.join(p, 'playwright'))];
  for (const t of tries) { try { return require(t); } catch { /* next */ } }
  throw new Error('Playwright not found: npm i -g playwright (or set NODE_PATH)');
}
const { chromium } = loadPlaywright();

const args = process.argv.slice(2);
const dir = args.find(a => !a.startsWith('--'));
if (!dir) { console.error('usage: node render_check.mjs out/ [--only A,B] [--dark] [--phone]'); process.exit(2); }
const only = (args.find(a => a.startsWith('--only='))?.slice(7) || '').split(',').filter(Boolean);
const modes = [{ name: 'desktop', width: 1280, height: 800 }];
if (args.includes('--phone')) modes.push({ name: 'phone', width: 390, height: 844 });
const schemes = args.includes('--dark') ? ['light', 'dark'] : ['light'];
const exe = [process.env.CHROMIUM_PATH, '/opt/pw-browsers/chromium-1194/chrome-linux/chrome'].find(p => p && fs.existsSync(p));
const browser = await chromium.launch({ ...(exe ? { executablePath: exe } : {}), args: ['--autoplay-policy=no-user-gesture-required'] });
const outDir = path.join(dir, 'check');
fs.mkdirSync(outDir, { recursive: true });
const pages = fs.readdirSync(dir).filter(f => f.endsWith('.html') && (!only.length || only.includes(f.replace(/\.html$/, ''))));
const results = {};
let problems = 0;
for (const file of pages) {
  for (const mode of modes) {
    for (const scheme of schemes) {
      const page = await browser.newPage({ viewport: { width: mode.width, height: mode.height }, deviceScaleFactor: 1 });
      const errors = [];
      page.on('pageerror', e => errors.push(String(e)));
      await page.goto('file://' + path.resolve(dir, file));
      if (scheme === 'dark') await page.evaluate(() => { document.body.classList.add('nightMode', 'night_mode'); window.dispatchEvent(new Event('resize')); });
      await page.evaluate(() => document.fonts.ready);
      // Full-page captures: sticky header/footer would otherwise cover content mid-image.
      // relative (not static) keeps the header as the phone player's containing block, as in Anki.
      await page.addStyleTag({ content: '.cc-head,.cc-foot{position:relative!important;top:auto!important;bottom:auto!important}' });
      await page.waitForTimeout(250);
      const audit = await page.evaluate(() => window.ccptAudit ? window.ccptAudit() : null);
      const key = `${file.replace(/\.html$/, '')}-${mode.name}-${scheme}`;
      await page.screenshot({ path: path.join(outDir, key + '.png'), fullPage: true });
      const issues = [];
      let play = null;
      if (args.includes('--play') && mode.name === 'desktop' && scheme === 'light') {
        play = await page.evaluate(async () => {
          const root = document.querySelector('.ccpt6'), audio = root.querySelector('audio'), speed = root.querySelector('.speed');
          if (!audio.getAttribute('src')) return { skipped: 'no audio' };
          document.dispatchEvent(new KeyboardEvent('keydown', { code: 'Space', key: ' ', bubbles: true }));
          await new Promise(r => setTimeout(r, 1500));
          const first = { playing: !audio.paused, time: audio.currentTime, highlighted: root.querySelector('.narrating')?.dataset.node || null };
          speed.click();
          const toggled = { label: speed.textContent, rate: audio.playbackRate };
          document.dispatchEvent(new KeyboardEvent('keydown', { code: 'Space', key: ' ', bubbles: true }));
          await new Promise(r => setTimeout(r, 200));
          return { first, toggled, pausedAfterSecondSpace: audio.paused, status: root.querySelector('.audio-status').textContent };
        });
        if (!play.skipped && (!play.first.playing || !(play.first.time > 0) || !play.pausedAfterSecondSpace)) issues.push('player did not start/pause with Space: ' + JSON.stringify(play));
      }
      if (!audit) issues.push('ccptAudit missing');
      else {
        if (audit.smallText.length) issues.push('small text: ' + audit.smallText.map(r => `${r.kind} ${r.font}px "${r.text.slice(0, 20)}"`).join(' | '));
        if (audit.horizontalOverflow) issues.push('page scrolls horizontally');
        if (audit.mapOverlaps) issues.push(`${audit.mapOverlaps} overlapping map nodes`);
        if (audit.clipped.length) issues.push(`clipped blocks ${audit.clipped.join(',')}`);
        const hiddenMath = (audit.scrollers || []).filter(s => s.startsWith('math:'));
        if (mode.name === 'phone' && hiddenMath.length) issues.push('formula wider than the phone (end hidden): ' + hiddenMath.join(', ') + ' — break the chain with <br> or shorter steps');
        if (audit.players !== 1) issues.push('page needs exactly one player');
        if (audit.brokenImages && audit.brokenImages.length) issues.push('board images missing: ' + audit.brokenImages.join(', '));
        // Handwriting shrunk below 45% of its pixels is hard to read: crop narrower, or split the crop.
        if (audit.boardScale < 0.45) issues.push(`board crop shown at ${audit.boardScale}× of its pixels: crop narrower or split it`);
        if (audit.fontsFailed && audit.fontsFailed.length) issues.push('fonts failed to load: ' + [...new Set(audit.fontsFailed)].join(', '));
        if (audit.lineStartPunct && audit.lineStartPunct.length) issues.push('punctuation starts a line: ' + audit.lineStartPunct.join(' | '));
      }
      if (errors.length) issues.push(...errors.map(e => 'script error: ' + e));
      problems += issues.length;
      results[key] = { audit, issues, play };
      await page.close();
    }
  }
}
await browser.close();
fs.writeFileSync(path.join(outDir, 'audit.json'), JSON.stringify(results, null, 1));
for (const [k, v] of Object.entries(results)) console.log((v.issues.length ? '✗ ' : '✓ ') + k + (v.issues.length ? ' — ' + v.issues.join('; ') : ` (min font ${v.audit.minFont}px, height ${v.audit.pageHeight}px)`));
process.exit(problems ? 1 : 0);
