"""Preview must disclose missing media and preserve genuinely playable caches."""
import json
import subprocess
import sys
import tempfile
from pathlib import Path
from build_map_deck import narration_plan, preview_audio_available, SPEECH
from validate_package import inspect_page

ROOT = Path(__file__).resolve().parent.parent
fixture = json.loads((ROOT / 'assets/map-example.json').read_text())
card = fixture['cards'][0]
SPEECH.clear()
filename = narration_plan(card, 'zh-CN-YunxiNeural')['file']
with tempfile.TemporaryDirectory() as temp:
    temp = Path(temp)
    source = temp / 'input.json'
    source.write_text(json.dumps(fixture))
    output = temp / 'out'
    media = output / 'media'
    media.mkdir(parents=True)
    audio = media / filename

    def preview():
        result = subprocess.run([sys.executable, str(ROOT / 'scripts/build_logic_deck.py'), str(source), str(output), '--preview'], capture_output=True, text=True)
        assert result.returncode == 0, result.stderr
        rendered = json.loads((output / 'rendered.json').read_text())[card['id']]['page']
        html = (output / (card['id'] + '-read.html')).read_text()
        assert not (output / 'CCPT-test.apkg').exists(), 'A preview must not export a package'
        return rendered, html

    for state in ('absent', 'empty', 'corrupt'):
        if state == 'empty':
            audio.write_bytes(b'')
        elif state == 'corrupt':
            audio.write_bytes(b'Not a playable MP3')
        assert not preview_audio_available(audio)
        rendered, html = preview()
        assert inspect_page(rendered, allow_pending=True) is None
        assert '图文预览，未生成语音' in rendered
        assert 'Space 播音' not in rendered
        assert filename not in rendered and filename not in html, 'Missing media must not cause a fetch'
        try:
            inspect_page(rendered)
        except AssertionError:
            pass
        else:
            raise AssertionError('An audio-free preview was accepted as a finished audio card')

    # Synthetic audio exercises media availability, not speech quality or voice identity.
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'lavfi', '-i', 'sine=frequency=440:duration=0.4', str(audio)], check=True)
    assert preview_audio_available(audio)
    rendered, html = preview()
    assert inspect_page(rendered) == filename
    assert 'data-audio-pending' not in rendered
    assert 'src="media/' + filename + '"' in html
    assert 'Space 播音' in rendered
print(json.dumps({'absent_empty_and_corrupt_media_disclosed': True, 'missing_media_not_requested': True, 'pending_not_accepted_as_complete': True, 'valid_cached_media_stays_playable': True, 'preview_exports_no_package': True}))
