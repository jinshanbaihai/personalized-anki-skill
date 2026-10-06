"""Cut tall board exports (ClassIn long images, scrolling screenshots, PDF pages) into
overlapping slices that can be read at full detail, and write an index of the slices.

Usage:
  python scripts/slice_board.py board.webp out/slices/            # images
  python scripts/slice_board.py lesson.pdf out/slices/ --dpi 200  # every PDF page, then slices

Each slice keeps the original pixel scale (narrow images are enlarged so text is not
downsampled again when viewed). The index records which original rows every slice
covers, so a board point can be cited as "p2 slice 3, rows 1800–2600" and nothing
between slices is skipped.
"""
import argparse
import json
import subprocess
import tempfile
from pathlib import Path

from PIL import Image

Image.MAX_IMAGE_PIXELS = None


def slices_for(image, target_width=1200, aspect=1.25, overlap=0.15):
    scale = max(1.0, target_width / image.width)
    if scale > 1:
        image = image.resize((round(image.width * scale), round(image.height * scale)), Image.LANCZOS)
    height = round(image.width * aspect)
    step = max(1, round(height * (1 - overlap)))
    top, out = 0, []
    while True:
        bottom = min(image.height, top + height)
        out.append((image.crop((0, top, image.width, bottom)), round(top / scale), round(bottom / scale)))
        if bottom >= image.height:
            return out
        top += step


def pages(path, dpi):
    if path.suffix.lower() != '.pdf':
        yield path.stem, Image.open(path).convert('RGB')
        return
    with tempfile.TemporaryDirectory() as tmp:
        subprocess.run(['pdftoppm', '-r', str(dpi), '-png', str(path), f'{tmp}/p'], check=True)
        for page in sorted(Path(tmp).glob('p*.png')):
            yield f'{path.stem}-{page.stem}', Image.open(page).convert('RGB')


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('inputs', nargs='+', type=Path)
    ap.add_argument('output', type=Path)
    ap.add_argument('--dpi', type=int, default=200)
    ap.add_argument('--width', type=int, default=1200, help='enlarge narrower images to this width')
    a = ap.parse_args()
    a.output.mkdir(parents=True, exist_ok=True)
    index = []
    for path in a.inputs:
        for name, image in pages(path, a.dpi):
            for i, (crop, top, bottom) in enumerate(slices_for(image, a.width), 1):
                file = a.output / f'{name}-s{i:02d}.png'
                crop.save(file)
                index.append({'source': str(path), 'page': name, 'slice': i, 'rows': [top, bottom], 'original_size': list(image.size), 'file': str(file)})
    (a.output / 'index.json').write_text(json.dumps(index, ensure_ascii=False, indent=1))
    print(json.dumps({'slices': len(index), 'index': str(a.output / 'index.json')}, ensure_ascii=False))


if __name__ == '__main__':
    main()
