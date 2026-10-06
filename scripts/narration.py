"""Page narration: synthesize each segment once at natural speed, trim its edge silence,
speed it up once with ffmpeg atempo, then join segments with designed pauses and
measured cues.

- Originals are cached globally by (voice, text) only, so 2× and 1.5× versions are
  derived offline and a speed change never needs the network.
- Edge clips carry ~0.19 s leading and 0.6–0.97 s trailing silence; trimming them
  and inserting fixed pauses keeps 2× listening brisk and predictable.
- Cue times come from decoded PCM sample counts, not estimates.
"""
import asyncio
import hashlib
import json
import os
import re
import subprocess
import tempfile
from pathlib import Path

from speech_backend import synthesize_original, resolve_voice

SAMPLE_RATE = 24000
PIPELINE = 'ccpt6-trim-atempo-v2'
FORMAT = 'ccpt6-pcm-cues-v2'
TRIM = ('silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.04,areverse,'
        'silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.06,areverse')
PAUSE_SAME_BLOCK = 0.30   # between steps, rows or branches of one block (final timeline)
PAUSE_NEW_BLOCK = 0.50    # between blocks, and after the title
SYMBOLS = re.compile(r'[\\^_{}$→⇒⟹√∑∫∞±∝]|[A-Za-z]{2,}/[A-Za-z]+')
# Anything outside Chinese, Latin letters, digits and ordinary punctuation is read badly or skipped by the voice.
PLAIN = re.compile(r'[\u4e00-\u9fff\u3400-\u4dbfA-Za-z0-9\s，。、；：？！“”‘’（）《》【】—…·,.;:?!\'"()%+\-=/&#@~]')
TEX_REMNANT = re.compile(r'\\[A-Za-z]+|[\^_{}$⟦]')
DEFAULT_LEXICON = {'λ': 'lambda', 'μ': 'mu', 'σ': 'sigma', 'θ': 'theta', 'π': 'pi', 'α': 'alpha', 'β': 'beta',
                   'γ': 'gamma', 'δ': 'delta', 'ε': 'epsilon', 'ρ': 'rho', 'φ': 'phi', 'χ': 'chi', 'ω': 'omega',
                   'Σ': 'sigma 求和', 'Δ': 'delta', '≥': '大于等于', '≤': '小于等于', '≠': '不等于', '≈': '约等于',
                   '↑': '上升', '↓': '下降', '∴': '所以', '∵': '因为', '∈': '属于', '°': '度', '²': '的平方', '³': '的立方', '½': '二分之一',
                   'e.g.': '例如', 'i.e.': '也就是', 'vs': '对比', '<': '小于', '>': '大于', '×': '乘以', '÷': '除以'}


def cache_root():
    return Path(os.environ.get('CCPT_TTS_CACHE') or Path(os.environ.get('XDG_CACHE_HOME') or Path.home() / '.cache') / 'ccpt-tts' / 'v1')


def speech_lint(text, lexicon=None):
    """Symbols a voice reads badly or not at all; write them as words in 〔读法〕 or speech."""
    odd = set(m.group(0) for m in SYMBOLS.finditer(text))
    spoken = apply_lexicon(text, lexicon)
    odd |= {ch for ch in spoken if not PLAIN.match(ch)}
    return sorted(odd)


def apply_lexicon(text, lexicon):
    """Edge accepts plain text only (no <sub>/<phoneme>), so readings are substituted before synthesis."""
    # U+2212 is "减" after an operand (x − 2, MPC − s) and "负" anywhere else (斜率为 −2、(−1, 1)、= −x).
    text = re.sub(r'−(?=\s*[\dA-Za-z(（])', lambda m: '减' if re.search(r'[A-Za-z0-9)\]}）²³′″*!%\u0370-\u03ff]$', text[:m.start()].rstrip()) else '负', text)
    text = re.sub(r'(^|[=(（\s，,：:、；\[])-(?=\d)', r'\1负', text)  # an ASCII hyphen only in clear negative positions
    text = re.sub(r'(?<=[A-Za-z])\*', ' 星', text)  # Q* → Q 星, as in the formula readings
    merged = dict(DEFAULT_LEXICON, **(lexicon or {}))
    merged.setdefault('−', '减')
    for written in sorted(merged, key=len, reverse=True):
        if re.fullmatch(r'[A-Za-z0-9.]+', written):
            text = re.sub(r'(?<![A-Za-z0-9])' + re.escape(written) + r'(?![A-Za-z0-9])', merged[written], text)
        else:
            text = text.replace(written, merged[written])
    return text


def original_key(voice, text):
    return hashlib.sha256(f'{voice}\0{text}\0rate=+0%\0audio-24khz-48kbitrate-mono-mp3'.encode()).hexdigest()


def original_path(voice, text):
    key = original_key(voice, text)
    return cache_root() / 'originals' / voice / key[:2] / f'{key}.mp3'


def clip_name(voice, text, speed):
    digest = hashlib.sha256(f'{original_key(voice, text)}\0{PIPELINE}\0speed={speed}'.encode()).hexdigest()[:20]
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


def plan(card_id, parts, voice, speed, lexicon=None):
    """parts: [(target_or_None, text)] in reading order. Lexicon readings are applied here."""
    voice = resolve_voice(voice)
    segments = []
    for target, text in parts:
        spoken = apply_lexicon(text, lexicon)
        segments.append({'target': target, 'text': spoken, 'file': clip_name(voice, spoken, speed)})
    return {'card': card_id, 'voice': voice, 'speed': speed, 'file': page_name(voice, [[s['target'], s['text']] for s in segments], speed),
            'text': '\n'.join(s['text'] for s in segments), 'segments': segments}


def missing_originals(plans):
    return sorted({(p['voice'], s['text']) for p in plans for s in p['segments'] if not decodes(original_path(p['voice'], s['text']))})


async def synthesize_clips(plans, media, concurrency=3, report=None):
    """Create every missing clip. Failures raise; nothing is silently replaced."""
    media.mkdir(parents=True, exist_ok=True)
    todo = {}
    for p in plans:
        for s in p['segments']:
            todo.setdefault(s['file'], (s['text'], p['voice'], p['speed']))
    limit = asyncio.Semaphore(concurrency)

    async def original(text, voice):
        path = original_path(voice, text)
        if decodes(path):
            return path, 'cache'
        path.parent.mkdir(parents=True, exist_ok=True)
        async with limit:
            with tempfile.TemporaryDirectory(dir=path.parent) as tmp:
                pending = Path(tmp) / 'original.mp3'
                provider = None
                for attempt in range(3):
                    try:
                        provider = await synthesize_original(text, voice, pending)
                        break
                    except Exception:
                        if attempt == 2:
                            raise
                        await asyncio.sleep(1.5 * (attempt + 1))
                if not decodes(pending):
                    raise RuntimeError('Voice service returned audio that does not decode')
                pending.replace(path)
                return path, provider

    async def one(name, text, voice, speed):
        dest = media / name
        if decodes(dest):
            return 'cached'
        source, provider = await original(text, voice)
        with tempfile.TemporaryDirectory(dir=media) as tmp:
            trimmed = Path(tmp) / 'trimmed.wav'
            subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', str(source), '-af', TRIM, '-ar', str(SAMPLE_RATE), '-ac', '1', str(trimmed)], check=True)
            if not decodes(trimmed):
                raise RuntimeError(f'{name}: nothing left after trimming silence; check the narration text')
            encoded = Path(tmp) / 'final.mp3'
            subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', str(trimmed), '-af', tempo_chain(speed),
                            '-ar', str(SAMPLE_RATE), '-ac', '1', '-codec:a', 'libmp3lame', '-q:a', '3', str(encoded)], check=True)
            # MP3 frames add a few tens of milliseconds; beyond that the length must match the tempo exactly.
            expected, measured = duration(trimmed) / speed, duration(encoded)
            if abs(measured - expected) > max(0.03 * expected, 0.08):
                raise RuntimeError(f'{name}: {measured:.2f}s after atempo, expected {expected:.2f}s for {speed}×')
            encoded.replace(dest)
        return provider

    results = await asyncio.gather(*(one(n, *args) for n, args in todo.items()))
    if report is not None:
        report.update({n: r for n, r in zip(todo, results)})


def block_of(target):
    return None if target in (None, 'title') else str(target).split('-')[0]


def assemble(p, media):
    """Join decoded clips into the page MP3 with designed pauses and return measured cues."""
    dest, sidecar = media / p['file'], media / (p['file'] + '.cues.json')
    hashes = [hashlib.sha256((media / s['file']).read_bytes()).hexdigest() for s in p['segments']]
    if decodes(dest) and sidecar.exists():
        try:
            cached = json.loads(sidecar.read_text(encoding='utf-8'))
            if cached['clip_hashes'] == hashes and cached['audio_sha256'] == hashlib.sha256(dest.read_bytes()).hexdigest():
                return cached['narration']
        except (KeyError, ValueError, OSError):
            pass
    cursor, cues, previous = 0, [], None
    with tempfile.TemporaryDirectory(dir=media) as tmp:
        pcm = Path(tmp) / 'page.pcm'
        with pcm.open('wb') as stream:
            for i, s in enumerate(p['segments']):
                decoded = subprocess.check_output(['ffmpeg', '-v', 'error', '-i', str(media / s['file']), '-f', 's16le', '-ar', str(SAMPLE_RATE), '-ac', '1', '-'])
                if not decoded or len(decoded) % 2:
                    raise RuntimeError(f'Malformed narration segment {s["file"]}')
                if i:
                    pause = PAUSE_SAME_BLOCK if block_of(s['target']) == previous and previous is not None else PAUSE_NEW_BLOCK
                    gap = b'\0\0' * int(SAMPLE_RATE * pause)
                    stream.write(gap)
                    cursor += len(gap) // 2
                samples = len(decoded) // 2
                cues.append({'target': s['target'], 'start': round(cursor / SAMPLE_RATE, 3), 'end': round((cursor + samples) / SAMPLE_RATE, 3)})
                stream.write(decoded)
                cursor += samples
                previous = block_of(s['target'])
        pending = Path(tmp) / 'page.mp3'
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 's16le', '-ar', str(SAMPLE_RATE), '-ac', '1', '-i', str(pcm),
                        '-codec:a', 'libmp3lame', '-q:a', '3', str(pending)], check=True)
        if abs(duration(pending) - cursor / SAMPLE_RATE) > 0.15:
            raise RuntimeError('Joined narration and cue clock disagree')
        pending.replace(dest)
    narration = {'timing': 'decoded-pcm-samples', 'pipeline': PIPELINE, 'speed': p['speed'], 'voice': p['voice'],
                 'duration': round(cursor / SAMPLE_RATE, 3), 'cues': cues}
    sidecar.write_text(json.dumps({'clip_hashes': hashes, 'audio_sha256': hashlib.sha256(dest.read_bytes()).hexdigest(), 'narration': narration}, ensure_ascii=False, indent=2), encoding='utf-8')
    return narration


# ---------------------------------------------------------------- speed rule
# Default 2×. 1.5× only when a card is genuinely dense (references/narration.md):
# hard triggers H1–H4, or a soft score of 3+. Length or map depth alone never slows a card.
NUMBER = re.compile(r'(?<![\w.])(\d+(?:\.\d+)?(?:/\d+)?)(?![\w.])')
PROOF = re.compile(r'contradiction|induction|反证|归纳|show that|证明', re.I)


def strings(value):
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for v in value.values():
            yield from strings(v)
    elif isinstance(value, list):
        for v in value:
            yield from strings(v)


def block_speech(block):
    """What the listener actually hears for one block (citations, sources and badges excluded)."""
    from blocks import render_block, BlockError  # local import: blocks does not depend on narration
    try:
        return ' '.join(p.text for p in render_block(block, 'm', 'metrics')[1])
    except BlockError:
        return ''


def speed_metrics(card, narration_text, seen_terms):
    from blocks import MATH
    source = '\n'.join(strings(card.get('blocks', []))) + '\n' + card.get('title', '')
    spoken = [m.group(4) for m in MATH.finditer(source) if m.group(4) and m.group(4).strip()]  # inline $…$ and display $$…$$
    explicit = sum(b.get('speech', '') != '' and '$' in json.dumps(b, ensure_ascii=False) for b in card['blocks'] if isinstance(b, dict))
    # Only dependent derivation steps count; causal chains and maps carry their structure visibly.
    steps = sum(len([i for i in b.get('items', []) if isinstance(i, dict) and not i.get('trivial')]) for b in card['blocks'] if b.get('type') == 'steps')
    # Numbers the listener must hold, from the narration only: tables, figures, chains and maps are on screen,
    # exam blocks list where a point was examined, and step numbers, mark badges and years are not values.
    heard = [block_speech(b) for b in card['blocks'] if b.get('type') not in ('table', 'figure', 'chain', 'map', 'exam')]
    values = [re.sub(r'第\d+步|(?<![A-Za-z])[MABCD] \d+|(?<!\d)(?:19|20)\d\d(?!\d)', ' ', t) for t in heard]
    numbers = max([len({n for n in NUMBER.findall(t) if n not in ('0', '1', '2', '3')}) for t in values] or [0])
    conditional = sum(len(re.findall(r'仅当|除非|前提是|取决于', t)) for t in heard)
    terms = [t for b in card['blocks'] if b.get('type') == 'definition' for t in [b.get('term', '')] if t and t not in seen_terms]
    seen_terms.update(terms)
    han = len(re.findall(r'[\u4e00-\u9fff]', narration_text)) or 1
    english = len(re.findall(r'[A-Za-z]{2,}', narration_text))
    m_share = sum(len(s) for s in spoken) / max(1, len(narration_text))
    proof = bool(PROOF.search(source)) and card['genre'] in ('derivation', 'method')
    return {'S': steps, 'M': len(spoken) + explicit, 'm_share': round(m_share, 3), 'T': len(terms), 'E': round(english * 100 / han, 1),
            'N': numbers, 'C': conditional, 'proof': proof, 'worked': card['genre'] in ('derivation', 'method', 'formula')}


def decide_speed(m):
    reasons = []
    if m['S'] >= 4 and m['M'] >= 4:
        reasons.append(f'{m["S"]} 步推导 · {m["M"]} 处公式读法')
    if m['m_share'] >= 0.35:
        reasons.append(f'公式读法占 {round(m["m_share"] * 100)}%')
    if m['proof'] and m['S'] >= 3:
        reasons.append('证明结构')
    if m['N'] >= 4 and m.get('worked', True):  # values to hold matter in worked problems, not in term or essay cards
        reasons.append(f'需同时记住 {m["N"]} 个数值')
    if reasons:
        return 1.5, '；'.join(reasons)
    # Steps weigh 2 only when they carry spoken formulas; a formula-free procedure needs more traits to slow down.
    score = ((2 if m['M'] >= 1 else 1) if m['S'] >= 3 else 0) + (m['M'] >= 3) + (m['T'] >= 3) + (m['E'] >= 8) + (m['C'] >= 2)
    if score >= 3:
        return 1.5, f'密度分 {score}（步骤 {m["S"]}、公式 {m["M"]}、新术语 {m["T"]}、English 密度 {m["E"]}、条件 {m["C"]}）'
    return 2.0, ''
