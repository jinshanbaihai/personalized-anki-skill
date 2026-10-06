"""Cut tall board exports (ClassIn long images, scrolling screenshots, PDF pages) into
overlapping slices that can be read at full detail, and write an index of the slices.

Usage:
  python scripts/slice_board.py board.webp out/slices/            # images
  python scripts/slice_board.py lesson.pdf out/slices/ --dpi 200  # every PDF page, then slices

Each slice keeps the original pixel scale (narrow images are enlarged so text is not
downsampled again when viewed). The index records which original rows every slice
covers, so a board point can be cited as "p2 slice 3, rows 1800–2600" and nothing
between slices is skipped.

Input quality gate: chat apps often recompress a long board to a few hundred pixels wide.
Each raster page gets a legibility verdict from its width. Below about 800 px wide, small
handwriting is no longer reliably readable: mark the affected board points legibility "low", confirm
their content from official sources (confirmed_by), never fill in guessed words, and ask
the user for the original export in the delivery note.
"""
import argparse
import json
import subprocess
import tempfile
from pathlib import Path

from PIL import Image, ImageOps

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


MIN_WIDTH = 800


def legibility(image, rendered_pdf=False):
    """Width-based gate. Line-height estimates proved unreliable across white, green and dark boards,
    so the verdict uses the one robust signal: a full-width board line holds 20–40 handwritten characters,
    and below ~800 px that leaves fewer than ~20 px per character."""
    if rendered_pdf:
        return {'width': image.width, 'verdict': 'ok', 'why': 'PDF page rendered at the requested dpi'}
    low = image.width < MIN_WIDTH
    why = f'width {image.width}px < {MIN_WIDTH}px: probably recompressed by a chat app' if low else ''
    return {'width': image.width, 'verdict': 'low' if low else 'ok', 'why': why}


def upright_rgb(image):
    """Phone photos carry their rotation in EXIF; transparent exports need a white page behind the ink."""
    image = ImageOps.exif_transpose(image)
    if image.mode in ('RGBA', 'LA') or (image.mode == 'P' and 'transparency' in image.info):
        rgba = image.convert('RGBA')
        page = Image.new('RGB', rgba.size, 'white')
        page.paste(rgba, mask=rgba.getchannel('A'))
        return page
    return image.convert('RGB')


def pages(path, dpi):
    if path.suffix.lower() != '.pdf':
        yield path.stem, upright_rgb(Image.open(path))
        return
    with tempfile.TemporaryDirectory() as tmp:
        subprocess.run(['pdftoppm', '-r', str(dpi), '-png', str(path), f'{tmp}/p'], check=True)
        for page in sorted(Path(tmp).glob('p*.png')):
            yield f'{path.stem}-{page.stem}', upright_rgb(Image.open(page))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('inputs', nargs='+', type=Path)
    ap.add_argument('output', type=Path)
    ap.add_argument('--dpi', type=int, default=200)
    ap.add_argument('--width', type=int, default=1200, help='enlarge narrower images to this width')
    a = ap.parse_args()
    a.output.mkdir(parents=True, exist_ok=True)
    index, quality = [], {}
    for path in a.inputs:
        for name, image in pages(path, a.dpi):
            quality[name] = legibility(image, rendered_pdf=path.suffix.lower() == '.pdf')
            for i, (crop, top, bottom) in enumerate(slices_for(image, a.width), 1):
                file = a.output / f'{name}-s{i:02d}.png'
                crop.save(file)
                index.append({'source': str(path), 'page': name, 'slice': i, 'rows': [top, bottom], 'original_size': list(image.size), 'file': str(file)})
    (a.output / 'index.json').write_text(json.dumps({'quality': quality, 'slices': index}, ensure_ascii=False, indent=1), encoding='utf-8')
    low = {k: v['why'] for k, v in quality.items() if v['verdict'] == 'low'}
    print(json.dumps({'slices': len(index), 'index': str(a.output / 'index.json'), 'quality': quality}, ensure_ascii=False))
    if low:
        print('⚠ low legibility: ' + json.dumps(low, ensure_ascii=False)
              + '\n  Mark affected board points legibility "low" with confirmed_by; do not guess words; ask for the original export in the delivery note.')


if __name__ == '__main__':
    main()
