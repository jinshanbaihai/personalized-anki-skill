"""Page narration: synthesize each segment once, tempo-adjust once, join with measured cues.

Every card has one MP3. Segments are synthesized at the voice's natural rate,
then sped up with a single ffmpeg atempo pass to the card's speed (2.0 by
default, 1.5 for genuinely complex cards). Cue times come from decoded PCM
sample counts, so highlighting follows the real audio rather than a guess.
"""
import asyncio
import hashlib
import json
import re
import subprocess
import tempfile
from pathlib import Path

from speech_backend import synthesize_original, resolve_voice

SAMPLE_RATE = 24000
FORMAT = 'ccpt6-pcm-cues-v1'


SYMBOLS = re.compile(r'[\\^_{}$→⇒⟹≥≤≠×÷√∑∫∞±≈∝]|[A-Za-z]{2,}/[A-Za-z]+')


def speech_lint(text):
    """Symbols a voice reads badly or not at all; write them as words in 〔读法〕 or speech."""
    return sorted(set(m.group(0) for m in SYMBOLS.finditer(text)))


def clip_name(voice, text, speed):
    digest = hashlib.sha256(f'{voice}\0{text}\0atempo={speed}'.encode()).hexdigest()[:20]
    return f'ccpt_{digest}.mp3'


def page_name(voice, parts, speed):
    signature = json.dumps({'voice': voice, 'parts': parts, 'speed': speed, 'format': FORMAT}, ensure_ascii=False, separators=(',', ':'))
    return 'ccpt_' + hashlib.sha256(signature.encode()).hexdigest()[:20] + '.mp3'


def duration(path):
    out = subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', str(path)], text=True)
    return float(out.strip())


def decodes(path):
    """A matching file name is not enough: the cached audio must decode."""
    path = Path(path)
    if not path.is_file() or path.stat().st_size < 100:
        return False
    try:
        if not duration(path) > 0:
            return False
        return subprocess.run(['ffmpeg', '-v', 'error', '-i', str(path), '-f', 'null', '-'], capture_output=True).returncode == 0
    except (OSError, ValueError, subprocess.SubprocessError):
        return False


def tempo_chain(speed):
    """atempo accepts 0.5–2.0 per instance on older ffmpeg; chain only when needed."""
    filters, remaining = [], float(speed)
    while remaining > 2.0:
        filters.append('atempo=2.0')
        remaining /= 2.0
    filters.append(f'atempo={remaining:g}')
    return ','.join(filters)


def plan(card_id, parts, voice, speed):
    """parts: [(target_or_None, text)] in reading order."""
    voice = resolve_voice(voice)
    segments = [{'target': target, 'text': text, 'file': clip_name(voice, text, speed)} for target, text in parts]
    return {'card': card_id, 'voice': voice, 'speed': speed, 'file': page_name(voice, [[s['target'], s['text']] for s in segments], speed),
            'text': '\n'.join(s['text'] for s in segments), 'segments': segments}


async def synthesize_clips(plans, media, concurrency=3, report=None):
    """Create every missing clip. Failures raise; nothing is silently replaced."""
    media.mkdir(parents=True, exist_ok=True)
    todo = {}
    for p in plans:
        for s in p['segments']:
            todo.setdefault(s['file'], (s['text'], p['voice'], p['speed']))
    limit = asyncio.Semaphore(concurrency)

    async def one(name, text, voice, speed):
        dest = media / name
        if decodes(dest):
            return 'cached'
        async with limit:
            with tempfile.TemporaryDirectory(dir=media) as tmp:
                original = Path(tmp) / 'original.mp3'
                provider = None
                for attempt in range(3):
                    try:
                        provider = await synthesize_original(text, voice, original)
                        break
                    except Exception:
                        if attempt == 2:
                            raise
                        await asyncio.sleep(1.5 * (attempt + 1))
                encoded = Path(tmp) / 'final.mp3'
                subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', str(original), '-af', tempo_chain(speed),
                                '-ar', str(SAMPLE_RATE), '-ac', '1', '-codec:a', 'libmp3lame', '-q:a', '3', str(encoded)], check=True)
                if not decodes(encoded):
                    raise RuntimeError(f'Encoded narration for {name} does not decode')
                ratio = duration(original) / duration(encoded)
                if abs(ratio - speed) > 0.12 * speed:
                    raise RuntimeError(f'{name}: measured speed-up {ratio:.2f} differs from requested {speed}')
                encoded.replace(dest)
                return provider

    results = await asyncio.gather(*(one(n, *args) for n, args in todo.items()))
    if report is not None:
        report.update({n: r for n, r in zip(todo, results)})


def assemble(p, media):
    """Join decoded clips into the page MP3 and return measured cues."""
    dest, sidecar = media / p['file'], media / (p['file'] + '.cues.json')
    hashes = [hashlib.sha256((media / s['file']).read_bytes()).hexdigest() for s in p['segments']]
    if decodes(dest) and sidecar.exists():
        try:
            cached = json.loads(sidecar.read_text())
            if cached['clip_hashes'] == hashes and cached['audio_sha256'] == hashlib.sha256(dest.read_bytes()).hexdigest():
                return cached['narration']
        except (KeyError, ValueError, OSError):
            pass
    cursor, cues = 0, []
    with tempfile.TemporaryDirectory(dir=media) as tmp:
        pcm = Path(tmp) / 'page.pcm'
        gap = b'\0\0' * int(SAMPLE_RATE * 0.12)  # a short breath between segments
        with pcm.open('wb') as stream:
            for i, s in enumerate(p['segments']):
                decoded = subprocess.check_output(['ffmpeg', '-v', 'error', '-i', str(media / s['file']), '-f', 's16le', '-ar', str(SAMPLE_RATE), '-ac', '1', '-'])
                if not decoded or len(decoded) % 2:
                    raise RuntimeError(f'Malformed narration segment {s["file"]}')
                if i:
                    stream.write(gap)
                    cursor += len(gap) // 2
                samples = len(decoded) // 2
                cues.append({'target': s['target'], 'start': round(cursor / SAMPLE_RATE, 3), 'end': round((cursor + samples) / SAMPLE_RATE, 3)})
                stream.write(decoded)
                cursor += samples
        pending = Path(tmp) / 'page.mp3'
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 's16le', '-ar', str(SAMPLE_RATE), '-ac', '1', '-i', str(pcm),
                        '-codec:a', 'libmp3lame', '-q:a', '3', str(pending)], check=True)
        if abs(duration(pending) - cursor / SAMPLE_RATE) > 0.15:
            raise RuntimeError('Joined narration and cue clock disagree')
        pending.replace(dest)
    narration = {'timing': 'decoded-pcm-samples', 'speed': p['speed'], 'voice': p['voice'], 'duration': round(cursor / SAMPLE_RATE, 3), 'cues': cues}
    sidecar.write_text(json.dumps({'clip_hashes': hashes, 'audio_sha256': hashlib.sha256(dest.read_bytes()).hexdigest(), 'narration': narration}, ensure_ascii=False, indent=2))
    return narration
