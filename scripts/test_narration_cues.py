"""Verify real audio cue timing and player attention lifecycle without cloud calls.

Synthetic tones exercise FFmpeg/MP3 padding rather than pretend to verify speech
quality. The JS test exercises the production player with a small media-event DOM.
Native Anki and an actual speech delivery still need their own acceptance check.
"""
import copy
import hashlib
import html
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import zipfile

import build_map_deck
from build_map_deck import narration_plan, assemble_narration, render, SPEECH, ASSETS


def check_audio():
    card = json.loads((ASSETS / 'map-example.json').read_text())['cards'][0]
    card['reading_order'] = card['reading_order'][1:] + card['reading_order'][:1]
    SPEECH.clear()
    plan = narration_plan(card, 'zh-CN-YunxiNeural', True)
    assert plan['segments'][0]['node'] is None
    assert [s['node'] for s in plan['segments'][1:]] == card['reading_order']
    assert plan['file'] not in SPEECH, 'Final audio must not be synthesized twice'
    with tempfile.TemporaryDirectory() as tmp:
        media = Path(tmp)
        for index, segment in enumerate(plan['segments']):
            subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'lavfi', '-i', f'sine=frequency={330 + index * 100}:duration={0.211 + index * 0.071}', '-ar', '24000', '-ac', '1', str(media / segment['file'])], check=True)
        narration = assemble_narration(plan, media)
        assert narration['timing'] == 'decoded-pcm-samples'
        assert narration['cues'][0]['start'] == 0
        measured_samples = 0
        for segment, cue in zip(plan['segments'], narration['cues']):
            pcm = subprocess.check_output(['ffmpeg', '-v', 'error', '-i', str(media / segment['file']), '-f', 's16le', '-ar', '24000', '-ac', '1', '-'])
            samples = len(pcm) // 2
            assert cue['start'] == measured_samples / 24000
            measured_samples += samples
            assert cue['end'] == measured_samples / 24000
        final_pcm = subprocess.check_output(['ffmpeg', '-v', 'error', '-i', str(media / plan['file']), '-f', 's16le', '-ar', '24000', '-ac', '1', '-'])
        assert len(final_pcm) // 2 == measured_samples, 'Encoder padding caused a cue drift'
        stamp = (media / plan['file']).stat().st_mtime_ns
        assert assemble_narration(plan, media) == narration
        assert (media / plan['file']).stat().st_mtime_ns == stamp, 'Unchanged clips should reuse the final audio'
        sidecar = media / (plan['file'] + '.cues.json')
        old_hash = json.loads(sidecar.read_text())['audio_sha256']
        (media / plan['file']).write_bytes(b'corrupted')
        assert assemble_narration(plan, media) == narration
        assert hashlib.sha256((media / plan['file']).read_bytes()).hexdigest() == old_hash
        page = render(card, plan['file'], narration)
        payload = re.search(r'<div hidden class="map-data">(.*?)</div>', page).group(1)
        assert json.loads(html.unescape(payload))['narration'] == narration
        assert page.count('class="speak"') == 1 and page.count('<audio ') == 1
        preview = render(card, plan['file'])
        payload = re.search(r'<div hidden class="map-data">(.*?)</div>', preview).group(1)
        assert json.loads(html.unescape(payload))['narration'] is None, 'Preview cannot invent unmeasured cues'


def check_player():
    harness = r'''
const fs=require('fs'),vm=require('vm'),assert=require('assert');
class Element extends EventTarget{
 constructor(){super();this.classList={values:new Set(),add(x){this.values.add(x)},remove(x){this.values.delete(x)},contains(x){return this.values.has(x)},toggle(x,v){if(v)this.add(x);else this.remove(x)}};this.style={};this.dataset={};this.offsetWidth=300;this.offsetHeight=100;this.clientWidth=900;this.clientHeight=600;this.offsetLeft=0;this.offsetTop=0;this.attributes={};}
 setAttribute(k,v){this.attributes[k]=v}append(){}querySelectorAll(){return []}
}
const a=new Element(),b=new Element(),title=new Element(),root=new Element(),board=new Element(),vp=new Element(),svg=new Element(),button=new Element(),status=new Element();a.dataset.node='a';b.dataset.node='b';
const audio=new Element();audio.paused=true;audio.ended=false;audio.currentTime=0;
audio.play=function(){this.paused=false;this.ended=false;this.dispatchEvent(new Event('play'));return Promise.resolve()};
audio.pause=function(){this.paused=true;this.dispatchEvent(new Event('pause'))};
button.click=()=>button.dispatchEvent(new Event('click'));
const data={edges:[],reading_order:['b','a'],narration:{timing:'decoded-pcm-samples',cues:[{node:null,start:0,end:.2},{node:'b',start:.2,end:.5},{node:'a',start:.5,end:1}]}};
root.querySelector=s=>({'.map-board':board,'.map-viewport':vp,'.map-edges':svg,'.map-data':{textContent:JSON.stringify(data)},'audio':audio,'.speak':button,'.audio-status':status,'h1':title})[s];
root.querySelectorAll=s=>s==='[data-node]'?[a,b]:s==='.speak'?[button]:[];
const document={querySelector:()=>root,fonts:{ready:Promise.resolve()},createElementNS:()=>new Element()};
let disconnected=false,singleCleaned=false;const window=new EventTarget();window.ccptSingleCleanup=()=>{singleCleaned=true};
const ctx={window,document,AbortController,ResizeObserver:class{observe(){}disconnect(){disconnected=true}},SVGElement:Element,console};
vm.runInNewContext(fs.readFileSync(process.argv[1],'utf8'),ctx);
button.click();assert(title.classList.contains('narrating'));
audio.currentTime=.25;audio.dispatchEvent(new Event('timeupdate'));assert(b.classList.contains('narrating'));assert(!title.classList.contains('narrating'));assert(!a.classList.contains('narrating'));
button.click();assert(audio.paused);assert(b.classList.contains('narrating'));assert(root.classList.contains('narration-paused'));
button.click();assert(!audio.paused);assert(!root.classList.contains('narration-paused'));
audio.currentTime=.6;audio.dispatchEvent(new Event('seeking'));assert(a.classList.contains('narrating'));assert(!b.classList.contains('narrating'));
audio.ended=true;audio.paused=true;audio.dispatchEvent(new Event('ended'));assert(!a.classList.contains('narrating'));
button.click();assert.strictEqual(audio.currentTime,0);assert(title.classList.contains('narrating'));
window.ccptCleanup();assert(audio.paused);assert(disconnected&&singleCleaned);assert(!title.classList.contains('narrating'));assert.strictEqual(audio.currentTime,0);
audio.currentTime=.6;audio.dispatchEvent(new Event('timeupdate'));assert(!a.classList.contains('narrating'));button.click();assert(audio.paused);
'''
    subprocess.run(['node', '-e', harness, str(ASSETS / 'map-card.js')], check=True)


def check_package():
    """Exercise the actual builder; test audio does not contact a voice service."""
    fixture = json.loads((ASSETS / 'map-example.json').read_text())
    fixture['narration_follow'] = True
    fixture['cards'].append(copy.deepcopy(fixture['cards'][0]))
    fixture['cards'][1]['id'] += '-second'
    fixture['cards'][1]['title'] += ' second test'
    saved_argv = sys.argv
    saved_synthesize = build_map_deck.synthesize

    async def synthetic_clips(media):
        for entry in SPEECH.values():
            subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'lavfi', '-i', 'sine=frequency=440:duration=0.15', '-ar', '24000', '-ac', '1', str(media / entry['file'])], check=True)

    try:
        build_map_deck.synthesize = synthetic_clips
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp)
            source = tmp / 'input.json'
            source.write_text(json.dumps(fixture))
            sys.argv = ['build_map_deck.py', str(source), str(tmp / 'out')]
            build_map_deck.main()
            entries = json.loads((tmp / 'out/speech-manifest.json').read_text())
            assert len(entries) == 2 and all(e['available'] and e['narration_follow']['cues'] for e in entries)
            with zipfile.ZipFile(tmp / 'out/CCPT-test.apkg') as package:
                imported = json.loads(package.read('media'))
                assert set(imported.values()) == {e['file'] for e in entries}
                assert len(imported) == 2, 'Only each page-level MP3 belongs in Anki media'
            for card in fixture['cards']:
                page = (tmp / f'out/{card["id"]}-read.html').read_text()
                assert 'decoded-pcm-samples' in page and page.count('<audio ') == 1
    finally:
        sys.argv = saved_argv
        build_map_deck.synthesize = saved_synthesize


if __name__ == '__main__':
    check_audio()
    check_player()
    check_package()
    print(json.dumps({'measured_pcm_cues': True, 'mp3_padding_no_drift': True, 'cache_and_corruption_recovery': True, 'single_player': True, 'preview_has_no_fake_cues': True, 'pause_resume_seek_end_and_cleanup': True, 'only_page_audio_imported': True}))
