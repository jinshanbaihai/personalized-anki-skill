"""Synthesize the original-speed clips a build asked for, on any computer that can reach the Edge voice service.

Usage:  python synth_originals.py needed.json originals/

needed.json comes from  build_cards.py deck.json out --export-narration needed.json  on the computer that makes
the cards (for example a cloud sandbox whose proxy blocks speech.platform.bing.com). This file runs alone: copy it
and needed.json anywhere with Python 3.9+ and  pip install edge-tts ; no ffmpeg, no deck and no other script is needed.

Each clip is written as originals/<key>.mp3, exactly what a direct build would cache: the requested voice at +0%
rate in Edge's default 24 kHz mono MP3. Nothing is substituted: a voice the service does not offer is an error.
Clips already in the folder are kept, so an interrupted run resumes. Bring the folder back and run
python scripts/narration_handoff.py import needed.json originals/  there.
"""
import argparse
import asyncio
import hashlib
import json
import sys
import tempfile
from pathlib import Path

SCHEMA = 'ccpt6-narration-handoff-v1'
RATE = '+0%'
FORMAT = 'audio-24khz-48kbitrate-mono-mp3'


def original_key(voice, text):
    """Same formula as narration.original_key (repeated here so this file runs on its own)."""
    return hashlib.sha256(f'{voice}\0{text}\0rate={RATE}\0{FORMAT}'.encode()).hexdigest()


def load(path):
    data = json.loads(Path(path).read_text(encoding='utf-8'))
    if data.get('schema') != SCHEMA:
        raise SystemExit(f'✗ {path}: not a narration handoff list (schema {data.get("schema")!r}, expected {SCHEMA})')
    if data.get('rate') != RATE or data.get('format') != FORMAT:
        raise SystemExit(f'✗ {path}: asks for rate {data.get("rate")} / {data.get("format")}; this script makes {RATE} / {FORMAT}')
    for item in data['items']:
        if original_key(item['voice'], item['text']) != item['key']:
            raise SystemExit(f'✗ {path}: the key of {item["text"][:30]!r} does not match its voice and text (the list was edited)')
    return data['items']


async def synthesize(items, folder, concurrency=4, attempts=3, communicate=None):
    """Return the items that still failed after the retries."""
    if communicate is None:
        try:
            import edge_tts
        except ImportError:
            raise SystemExit('✗ edge-tts is not installed here: python -m pip install edge-tts') from None
        communicate = edge_tts.Communicate
    folder.mkdir(parents=True, exist_ok=True)
    limit = asyncio.Semaphore(concurrency)
    failed, done = [], [0]

    async def one(item):
        dest = folder / f'{item["key"]}.mp3'
        if dest.is_file() and dest.stat().st_size >= 100:
            return
        async with limit:
            error = None
            for attempt in range(attempts):
                with tempfile.TemporaryDirectory(dir=folder) as tmp:
                    pending = Path(tmp) / 'clip.mp3'
                    try:
                        await communicate(item['text'], item['voice'], rate=RATE).save(str(pending))
                        if pending.stat().st_size < 100:
                            raise RuntimeError('the service returned no usable audio')
                        pending.replace(dest)  # a failed request never leaves a partial file under a usable name
                        done[0] += 1
                        return
                    except Exception as exc:  # noqa: BLE001 - retried, then reported by name
                        error = exc
                if attempt + 1 < attempts:
                    await asyncio.sleep(1.5 * (attempt + 1))
            failed.append((item, f'{type(error).__name__}: {error}'))

    await asyncio.gather(*(one(i) for i in items))
    print(f'  {done[0]} synthesized, {len(items) - done[0] - len(failed)} already there, {len(failed)} failed')
    return failed


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('needed', type=Path, help='the list written by build_cards.py --export-narration')
    ap.add_argument('folder', type=Path, help='where <key>.mp3 files go')
    ap.add_argument('--concurrency', type=int, default=4)
    a = ap.parse_args(argv)
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    items = load(a.needed)
    print(f'{len(items)} clip(s), voices: {", ".join(sorted({i["voice"] for i in items})) or "none"}')
    failed = asyncio.run(synthesize(items, a.folder, a.concurrency))
    if failed:
        for item, error in failed[:10]:
            print(f'✗ {item["voice"]} {item["text"][:40]!r}: {error}', file=sys.stderr)
        sys.exit('✗ some clips failed; run the same command again (finished clips are kept). '
                 'If every clip fails, this computer cannot reach speech.platform.bing.com either.')
    print(f'✓ {a.folder} is complete; bring it back and run: python scripts/narration_handoff.py import {a.needed.name} {a.folder}')


if __name__ == '__main__':
    main()
