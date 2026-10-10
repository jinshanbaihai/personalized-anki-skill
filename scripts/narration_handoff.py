"""Install original-speed clips synthesized on another computer into this computer's narration cache.

Usage:  python scripts/narration_handoff.py import needed.json originals/
        python scripts/narration_handoff.py status needed.json

The round trip, for a computer that cannot reach the voice service but has ffmpeg and the deck:
  1. python scripts/build_cards.py deck.json out --export-narration needed.json [--term-sampler]
  2. elsewhere: python synth_originals.py needed.json originals/      (Python + edge-tts only)
  3. here:      python scripts/narration_handoff.py import needed.json originals/
  4. here:      python scripts/build_cards.py deck.json out [--term-sampler]   (now finds every clip in the cache)

Every clip is checked before it enters the cache: its key must match the voice and text, and it must decode with
ffmpeg. A missing or broken clip is reported and left out, so the build in step 4 stops on it instead of shipping
silence; nothing is substituted.
"""
import argparse
import json
import shutil
import sys
import tempfile
from pathlib import Path

import narration


def load(path):
    data = json.loads(Path(path).read_text(encoding='utf-8'))
    if data.get('schema') != narration.HANDOFF_SCHEMA:
        raise SystemExit(f'✗ {path}: not a narration handoff list (schema {data.get("schema")!r})')
    if data.get('rate') != narration.ORIGINAL_RATE or data.get('format') != narration.ORIGINAL_FORMAT:
        raise SystemExit(f'✗ {path}: made for rate {data.get("rate")} / {data.get("format")}, but this skill caches '
                         f'{narration.ORIGINAL_RATE} / {narration.ORIGINAL_FORMAT}; export the list again')
    return data['items']


def install(items, folder):
    """Copy each verified clip to narration.original_path; return (installed, already, problems)."""
    found = {p.stem: p for p in Path(folder).rglob('*.mp3')}
    installed = already = 0
    problems = []
    for item in items:
        voice, text = item['voice'], item['text']
        if narration.original_key(voice, text) != item['key']:
            problems.append(f'key mismatch (the list was edited): {text[:40]!r}')
            continue
        dest = narration.original_path(voice, text)
        if narration.decodes(dest):
            already += 1
            continue
        source = found.get(item['key'])
        if source is None:
            problems.append(f'missing {item["key"]}.mp3: {voice} {text[:40]!r}')
            continue
        if not narration.decodes(source):
            problems.append(f'does not decode {source.name}: {text[:40]!r}')
            continue
        dest.parent.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(dir=dest.parent) as tmp:
            pending = Path(tmp) / 'original.mp3'
            shutil.copyfile(source, pending)
            pending.replace(dest)
        installed += 1
    return installed, already, problems


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest='command', required=True)
    imp = sub.add_parser('import', help='verify the clips and put them in the cache')
    imp.add_argument('needed', type=Path)
    imp.add_argument('folder', type=Path)
    st = sub.add_parser('status', help='how many listed clips the cache already holds')
    st.add_argument('needed', type=Path)
    a = ap.parse_args(argv)
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    narration.require_tools()
    items = load(a.needed)
    if a.command == 'status':
        have = sum(narration.decodes(narration.original_path(i['voice'], i['text'])) for i in items)
        print(f'{have}/{len(items)} clip(s) in {narration.cache_root()}')
        sys.exit(0 if have == len(items) else 1)
    installed, already, problems = install(items, a.folder)
    print(f'{installed} installed, {already} already cached, {len(problems)} problem(s) → {narration.cache_root()}')
    for line in problems[:20]:
        print(f'  ✗ {line}', file=sys.stderr)
    if problems:
        sys.exit('✗ synthesize the missing clips again (synth_originals.py keeps the finished ones) and import again')
    print('✓ every listed clip is cached; run the same build_cards.py command without --export-narration')


if __name__ == '__main__':
    main()
