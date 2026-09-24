"""Synthesize the requested Microsoft voice at original speed; never substitute voices."""
import asyncio
import argparse
import json
import tempfile
import os
import re
import urllib.request
from pathlib import Path
from xml.sax.saxutils import escape, quoteattr

import edge_tts

DEFAULT_VOICE = 'zh-CN-YunxiNeural'
DEFAULT_SPEED = 1.5
_voices_task = None


async def edge_voice_names():
    global _voices_task
    if (_voices_task is None or _voices_task.get_loop() is not asyncio.get_running_loop() or _voices_task.cancelled() or (_voices_task.done() and _voices_task.exception() is not None)):
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


def configured_azure():
    return bool(os.environ.get('AZURE_SPEECH_KEY') and os.environ.get('AZURE_SPEECH_REGION'))


async def inspect_voice(voice):
    """Availability is separate from a successful synthesis. Never expose credentials."""
    report = {'voice': voice, 'azure_configured': configured_azure()}
    try:
        names = await asyncio.wait_for(edge_voice_names(), timeout=30)
        report.update(edge_list_available=True, edge_voice_available=voice in names,
                      edge_chinese_voices=sorted(v for v in names if v.startswith('zh-CN-')))
    except Exception as exc:
        report.update(edge_list_available=False, edge_voice_available=None,
                      edge_error=type(exc).__name__)
    report['route'] = ('edge' if report['edge_voice_available'] else
                       'azure' if report['azure_configured'] else 'unavailable')
    return report


async def synthesize_original(text, voice, output):
    voice = voice or DEFAULT_VOICE
    report = await inspect_voice(voice)
    output = Path(output)
    output.parent.mkdir(parents=True, exist_ok=True)
    # Failed requests cannot leave a zero-byte or partial file under a usable name.
    with tempfile.TemporaryDirectory(dir=output.parent) as tmp:
        pending = Path(tmp) / 'speech.mp3'
        if report['edge_voice_available']:
            try:
                await edge_tts.Communicate(text, voice, rate='+0%').save(str(pending))
                if pending.stat().st_size < 100:
                    raise RuntimeError('Edge returned no usable audio')
                pending.replace(output)
                return 'edge'
            except Exception:
                if not configured_azure():
                    raise RuntimeError(f'Edge lists {voice}, but synthesis failed. Retry the same voice or configure authorized Azure Speech; no voice substitution was made.') from None
        elif not configured_azure():
            reason = ('does not offer this voice' if report['edge_list_available']
                      else 'voice list could not be reached')
            raise RuntimeError(f'Requested {voice}: Edge {reason}; no authorized Azure Speech configuration. Use --check to diagnose. No voice substitution was made.')
        await asyncio.to_thread(azure_synthesize, text, voice, pending)
        pending.replace(output)
        return 'azure'


async def _cli(args):
    report = await inspect_voice(args.voice)
    if args.probe:
        try:
            report['provider'] = await synthesize_original(
                '语音接口检查。Price 是价格，quantity 是数量。', args.voice, args.probe)
            report['synthesis_ok'] = True
            report['bytes'] = args.probe.stat().st_size
        except Exception as exc:
            report['synthesis_ok'] = False
            report['error'] = str(exc) if isinstance(exc, RuntimeError) else type(exc).__name__
    print(json.dumps(report, ensure_ascii=False, indent=2))
    if report['route'] == 'unavailable' or report.get('synthesis_ok') is False:
        raise SystemExit(2)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Check the requested Microsoft voice without silently substituting it.')
    parser.add_argument('--voice', default=DEFAULT_VOICE)
    parser.add_argument('--check', action='store_true', help='Check providers and configuration; does not synthesize')
    parser.add_argument('--probe', type=Path, help='Actually synthesize a short diagnostic clip to this path')
    asyncio.run(_cli(parser.parse_args()))
