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
Each raster page gets a legibility verdict from its width; for a PDF, from the width of the largest
image embedded in each page (a scanned or exported board is an image inside the PDF, and rendering it
at a high dpi does not add detail). Pure vector pages pass. Below about 800 px wide, small
handwriting is no longer reliably readable: mark the affected board points legibility "low", confirm
their content from official sources (confirmed_by), never fill in guessed words, and ask
the user for the original export in the delivery note.
"""
import argparse
import json
import re
import shutil
import subprocess
import sys
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


def legibility(image, embedded_width=None, pdf=False):
    """Width-based gate. Line-height estimates proved unreliable across white, green and dark boards,
    so the verdict uses the one robust signal: a full-width board line holds 20–40 handwritten characters,
    and below ~800 px that leaves fewer than ~20 px per character. For a PDF page the source pixels are
    those of its largest embedded image, not the rendered page."""
    if pdf and embedded_width is None:
        return {'width': image.width, 'verdict': 'ok', 'why': 'vector PDF page (no embedded image)'}
    width = embedded_width if pdf else image.width
    low = width < MIN_WIDTH
    source = 'embedded image' if pdf else 'image'
    why = f'{source} width {width}px < {MIN_WIDTH}px: probably recompressed by a chat app or a low-resolution scan' if low else ''
    return {'width': width, 'verdict': 'low' if low else 'ok', 'why': why}


INSTALL_POPPLER = ('  macOS: brew install poppler    Linux: sudo apt install poppler-utils    '
                   'Windows: install a Poppler build and add its bin folder to PATH, or  pip install pymupdf\n'
                   '  Without either, read the PDF pages directly by eye and say so in the delivery note.')


def embedded_widths(path):
    """{page number: width of the largest embedded image} from pdfimages, or PyMuPDF when poppler is absent."""
    if shutil.which('pdfimages'):
        out = subprocess.run(['pdfimages', '-list', str(path)], capture_output=True, text=True, encoding='utf-8', errors='replace').stdout
        widths = {}
        for line in out.splitlines()[2:]:
            cols = line.split()
            if len(cols) > 4 and cols[0].isdigit() and cols[3].isdigit() and cols[2] in ('image', 'stencil'):
                widths[int(cols[0])] = max(widths.get(int(cols[0]), 0), int(cols[3]))
        return widths
    try:
        import fitz  # PyMuPDF
    except ImportError:
        return None
    with fitz.open(str(path)) as doc:
        return {i + 1: max(img[2] for img in page.get_images(full=True)) for i, page in enumerate(doc) if page.get_images(full=True)}


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
    """(name, page number or None, image) for an image file or every page of a PDF."""
    if path.suffix.lower() != '.pdf':
        yield path.stem, None, upright_rgb(Image.open(path))
        return
    if shutil.which('pdftoppm'):
        with tempfile.TemporaryDirectory() as tmp:
            subprocess.run(['pdftoppm', '-r', str(dpi), '-png', str(path), f'{tmp}/p'], check=True)
            for page in sorted(Path(tmp).glob('p*.png'), key=lambda p: int(re.findall(r'\d+', p.stem)[-1])):
                yield f'{path.stem}-{page.stem}', int(re.findall(r'\d+', page.stem)[-1]), upright_rgb(Image.open(page))
        return
    try:
        import fitz  # PyMuPDF renders pages when poppler is not installed
    except ImportError:
        sys.exit('✗ poppler_missing: pdftoppm is needed to render PDF pages.\n' + INSTALL_POPPLER)
    with fitz.open(str(path)) as doc:
        for i, page in enumerate(doc, 1):
            pix = page.get_pixmap(dpi=dpi)
            yield f'{path.stem}-p-{i}', i, upright_rgb(Image.frombytes('RGB', (pix.width, pix.height), pix.samples))


def main():
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('inputs', nargs='+', type=Path)
    ap.add_argument('output', type=Path)
    ap.add_argument('--dpi', type=int, default=200)
    ap.add_argument('--width', type=int, default=1200, help='enlarge narrower images to this width')
    a = ap.parse_args()
    a.output.mkdir(parents=True, exist_ok=True)
    index, quality = [], {}
    for path in a.inputs:
        pdf = path.suffix.lower() == '.pdf'
        widths = embedded_widths(path) if pdf else {}
        if pdf and widths is None:
            print('⚠ pdfimages (poppler) and PyMuPDF are both missing: embedded image sizes of this PDF were not checked;'
                  ' judge legibility by eye and record it.', file=sys.stderr)
        for name, number, image in pages(path, a.dpi):
            quality[name] = legibility(image, (widths or {}).get(number), pdf=pdf and widths is not None)
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
