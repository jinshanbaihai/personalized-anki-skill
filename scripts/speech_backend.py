"""Synthesize the requested Microsoft voice at original speed; never substitute voices."""
import asyncio
import os
import re
import urllib.request
from pathlib import Path
from xml.sax.saxutils import escape, quoteattr

import edge_tts

DEFAULT_VOICE = 'zh-CN-YunyiMultilingualNeural'
DEFAULT_SPEED = 1.5
_voices_task = None


async def edge_voice_names():
    global _voices_task
    if _voices_task is None or _voices_task.get_loop() is not asyncio.get_running_loop():
        _voices_task = asyncio.create_task(edge_tts.list_voices())
    return {v['ShortName'] for v in await _voices_task}


def azure_synthesize(text, voice, output):
    key = os.environ.get('AZURE_SPEECH_KEY')
    region = os.environ.get('AZURE_SPEECH_REGION')
    if not key or not region:
        raise RuntimeError(f'Requested voice {voice} is unavailable via Edge. Configure an authorized Azure Speech key and region; no voice substitution was made.')
    if not re.fullmatch(r'[a-z0-9-]+', region):
        raise ValueError('Invalid Azure Speech region')
    ssml = '<speak version="1.0" xml:lang="zh-CN"><voice name=' + quoteattr(voice) + '>' + escape(text) + '</voice></speak>'
    req = urllib.request.Request(
        f'https://{region}.tts.speech.microsoft.com/cognitiveservices/v1',
        data=ssml.encode('utf-8'),
        headers={'Ocp-Apim-Subscription-Key': key, 'Content-Type': 'application/ssml+xml',
                 'X-Microsoft-OutputFormat': 'audio-24khz-48kbitrate-mono-mp3', 'User-Agent': 'anki-ccpt-skill'})
    with urllib.request.urlopen(req, timeout=45) as response:
        audio = response.read()
        if not response.headers.get('Content-Type', '').lower().startswith('audio/') or len(audio) < 100:
            raise RuntimeError('Azure returned no usable audio')
    Path(output).write_bytes(audio)


async def synthesize_original(text, voice, output):
    voice = voice or DEFAULT_VOICE
    try:
        available = voice in await asyncio.wait_for(edge_voice_names(), timeout=30)
    except Exception:
        if not (os.environ.get('AZURE_SPEECH_KEY') and os.environ.get('AZURE_SPEECH_REGION')):
            raise RuntimeError('Cannot verify Edge voice availability; no authorized Azure Speech configuration is present.') from None
        available = False
    if available:
        await edge_tts.Communicate(text, voice, rate='+0%').save(str(output))
        return 'edge'
    await asyncio.to_thread(azure_synthesize, text, voice, output)
    return 'azure'
