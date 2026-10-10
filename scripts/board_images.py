"""Board crops for board cards (板书卡): the learner's own ClassIn board, cut by knowledge point, is the card.

Two jobs:

1. Propose regions (author tool). A ClassIn export is one tall column; ink blocks are separated by blank rows.
     python scripts/board_images.py board.png out/regions/
   writes regions.json (numbered boxes in original pixels, ready-to-paste crop objects) and overlay
   pages regions-pNN.png with the boxes drawn and numbered, so the author can read the board and say
   "this knowledge point = R03 + R04 + R11". Adjacent regions are joined with --union:
     python scripts/board_images.py --union out/regions/regions.json R03 R04

2. Prepare crops at build time (build_cards.py calls prepare()). Each board block names a source image
   and its crops; every crop is cut from the original pixels (masks painted out first), saved once under a
   content-hashed media name, and given its tone (light/dark board) so the page can blend it into the
   theme paper instead of showing a white rectangle (dry-eye rule, see references/visual-themes.md).
   The delivered folder gets a copy of each source that keeps only the cropped areas (masks applied),
   so the hand-off never carries names or regions the cards do not show.
"""
import argparse
import hashlib
import io
import json
import re
import sys
from collections import Counter
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageFont

from slice_board import upright_rgb, MIN_WIDTH

Image.MAX_IMAGE_PIXELS = None
MAX_CROP_WIDTH = 1800      # wider crops are scaled down: the card column is at most 1120 css px
TONES = ('auto', 'light', 'dark', 'keep')
MEDIA_PREFIX = 'ccpt6-board-'


class BoardError(ValueError):
    pass


def fail(where, message):
    raise BoardError(f'{where}: {message}')


# ---------------------------------------------------------------- colour helpers

def background(image):
    """The board colour: the most common colour bucket of a small copy (ink is rare, paper is not), averaged
    over the pixels in that bucket so a pure white board stays pure white."""
    small = image.copy()
    small.thumbnail((240, 240))
    pixels = list(flat(small))
    buckets = Counter(tuple(v // 16 for v in px[:3]) for px in pixels)
    top = buckets.most_common(1)[0][0]
    members = [px for px in pixels if tuple(v // 16 for v in px[:3]) == top]
    return tuple(round(sum(px[i] for px in members) / len(members)) for i in range(3))


def flat(image):
    """Pixel values in reading order (Pillow 12 renamed getdata)."""
    return image.get_flattened_data() if hasattr(image, 'get_flattened_data') else image.getdata()


def luminance(rgb):
    def lin(c):
        c /= 255
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (lin(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def tone_of(rgb):
    """light: a white or pale board (blended into the theme paper, inverted at night); dark: a black or green
    chalk board (shown as it is); keep: a photo or mid-tone page that must not be recoloured."""
    y = luminance(rgb)
    return 'light' if y >= 0.6 else 'dark' if y <= 0.2 else 'keep'


def ink_mask(image, bg, threshold=40):
    """'L' mask, 255 where a pixel differs visibly from the board colour."""
    diff = ImageChops.difference(image, Image.new('RGB', image.size, bg))
    r, g, b = diff.split()
    return ImageChops.lighter(ImageChops.lighter(r, g), b).point(lambda v: 255 if v > threshold else 0)


def profile(mask, axis):
    """Ink fraction per row (axis=0) or per column (axis=1), from a box-filtered float resize."""
    f = mask.convert('F')
    size = (1, mask.height) if axis == 0 else (mask.width, 1)
    return [v / 255 for v in flat(f.resize(size, Image.BOX))]


def runs(values, floor, min_gap):
    """[start, end) runs where values exceed floor; runs closer than min_gap are joined."""
    out, start = [], None
    for i, v in enumerate(values + [0]):
        if v > floor and start is None:
            start = i
        elif v <= floor and start is not None:
            if out and start - out[-1][1] < min_gap:
                out[-1][1] = i
            else:
                out.append([start, i])
            start = None
    return out


# ---------------------------------------------------------------- 1. region proposals

def split_gap(rows, width):
    """Blank rows that end a block. Lines of one block sit closer than blocks do, so the blanks fall into two groups:
    cut at the widest jump between them (at least 1.8×); with evenly spaced lines, ~28 px per 1300 px of width."""
    default = max(16, round(28 * width / 1300))
    lines = runs(rows, 0.0015, 1)
    blanks = sorted(b[0] - a[1] for a, b in zip(lines, lines[1:]) if b[0] - a[1] >= 4)
    best = None
    for a, b in zip(blanks, blanks[1:]):
        if b >= 1.8 * a and (best is None or b / a > best[0]):
            best = (b / a, (a + b) // 2 + 1)
    return min(max(default // 2, best[1]) if best else default, round(width * 0.12))


def propose(image, threshold=40, gap=None, col_gap=None, pad=10):
    """Ink blocks of a board, top to bottom (and left to right within a band): [{id, box}]."""
    bg = background(image)
    mask = ink_mask(image, bg, threshold)
    rows = profile(mask, 0)
    if not gap:
        gap = split_gap(rows, image.width)
    col_gap = col_gap or max(60, round(image.width * 0.12))
    regions = []
    for y0, y1 in runs(rows, 0.0015, gap):
        if y1 - y0 < 6:
            continue
        band = mask.crop((0, y0, image.width, y1))
        for x0, x1 in runs(profile(band, 1), 0.0, col_gap):
            if x1 - x0 < 6:
                continue
            piece = band.crop((x0, 0, x1, y1 - y0))
            rows = runs(profile(piece, 0), 0.0, gap)
            top, bottom = (rows[0][0], rows[-1][1]) if rows else (0, y1 - y0)
            box = [max(0, x0 - pad), max(0, y0 + top - pad), min(image.width, x1 + pad), min(image.height, y0 + bottom + pad)]
            regions.append(box)
    regions.sort(key=lambda b: (b[1], b[0]))
    return bg, [{'id': f'R{i:02d}', 'box': box} for i, box in enumerate(regions, 1)]


def label_font(size):
    try:
        return ImageFont.load_default(size=size)
    except TypeError:  # Pillow < 10.1: bitmap default font only
        return ImageFont.load_default()


def overlay_pages(image, regions, out, stem, aspect=1.3):
    """The board with numbered region boxes, cut into readable pages (overlap 10%)."""
    sheet = image.copy()
    draw = ImageDraw.Draw(sheet)
    size = max(18, round(image.width / 40))
    font = label_font(size)
    colours = [(214, 40, 40), (16, 110, 190), (20, 140, 70), (170, 70, 170)]
    for i, r in enumerate(regions):
        c = colours[i % len(colours)]
        x0, y0, x1, y1 = r['box']
        draw.rectangle((x0, y0, x1, y1), outline=c, width=max(2, size // 8))
        tag = r['id']
        tw = draw.textlength(tag, font=font) if hasattr(draw, 'textlength') else size * len(tag)
        # the tag sits outside the box (above it, else to its right) so it never covers the first words of the block
        if y0 >= size + 10:
            tx, ty = x0, y0 - size - 10
        elif x1 + tw + 14 <= image.width:
            tx, ty = x1 + 4, y0
        else:
            tx, ty = x1 - tw - 10, y0
        draw.rectangle((tx, ty, tx + tw + 10, ty + size + 8), fill=c)
        draw.text((tx + 5, ty + 3), tag, fill=(255, 255, 255), font=font)
    height = round(image.width * aspect)
    step = max(1, round(height * 0.9))
    files, top, n = [], 0, 1
    while True:
        bottom = min(image.height, top + height)
        path = out / f'{stem}-regions-p{n:02d}.png'
        page = sheet.crop((0, top, image.width, bottom))
        if page.width > 1400:
            page = page.resize((1400, round(page.height * 1400 / page.width)), Image.LANCZOS)
        page.save(path)
        files.append({'file': str(path), 'rows': [top, bottom],
                      'regions': [r['id'] for r in regions if r['box'][1] < bottom and r['box'][3] > top]})
        if bottom >= image.height:
            return files
        top += step
        n += 1


def union(boxes):
    return [min(b[0] for b in boxes), min(b[1] for b in boxes), max(b[2] for b in boxes), max(b[3] for b in boxes)]


# ---------------------------------------------------------------- 2. build-time preparation

def need_box(value, where, size=None):
    if not (isinstance(value, list) and len(value) == 4 and all(isinstance(v, int) and not isinstance(v, bool) for v in value)):
        fail(where, 'a box is [x0, y0, x1, y1] in whole pixels of the original board image')
    x0, y0, x1, y1 = value
    if not (x0 < x1 and y0 < y1 and x0 >= 0 and y0 >= 0):
        fail(where, f'box {value} must have x0 < x1, y0 < y1 and no negative coordinates')
    if size and (x1 > size[0] or y1 > size[1]):
        fail(where, f'box {value} reaches outside the image ({size[0]}×{size[1]} px); check the coordinates against regions.json')
    return value


def png_bytes(image):
    buf = io.BytesIO()
    image.save(buf, format='PNG', optimize=True)
    return buf.getvalue()


class Sources:
    """Each source image is opened once, turned upright and flattened; masks apply to every crop of it."""

    def __init__(self, base):
        self.base, self.images, self.masks, self.crops, self.pitches = Path(base), {}, {}, {}, {}

    def path(self, src, where):
        if not isinstance(src, str) or not src.strip():
            fail(where, '"src" names the board image (a path relative to deck.json)')
        if src.lower().endswith('.pdf'):
            fail(where, 'render the PDF page to PNG first (pdftoppm -r 200 -png board.pdf page) and point "src" at the PNG')
        path = (self.base / src).resolve()
        if not path.is_file():
            fail(where, f'board image not found: {src} (paths are relative to the folder of deck.json)')
        return path

    def image(self, path):
        if path not in self.images:
            self.images[path] = upright_rgb(Image.open(path))
        return self.images[path]

    def pitch(self, path):
        """Typical text-line height of the board in its own pixels: the median ink row run (8–80 px tall)."""
        if path not in self.pitches:
            image = self.image(path)
            heights = sorted(b - a for a, b in runs(profile(ink_mask(image, background(image)), 0), 0.0015, 1) if 8 <= b - a <= 80)
            self.pitches[path] = heights[len(heights) // 2] if heights else max(16, round(image.width / 50))
        return self.pitches[path]


def board_blocks(data):
    for c in data.get('cards', []):
        if not isinstance(c, dict):
            continue
        for i, b in enumerate(c.get('blocks', []) or []):
            if isinstance(b, dict) and b.get('type') == 'board':
                yield c, i, b


def prepare(data, base, media, deliver=None):
    """Cut every board crop into media/ and return ({card id: blocks with '_media' filled}, files, warnings, delivered src map).

    deliver: a folder; when given, each source is copied there keeping only its cropped areas (masks applied),
    and the returned map says which new relative path replaces each original src in the delivered deck.json."""
    sources = Sources(base)
    media = Path(media)
    media.mkdir(parents=True, exist_ok=True)
    # Masks first: a name hidden in one crop must stay hidden in every crop of the same image.
    for card, i, b in board_blocks(data):
        where = f'card {card.get("id")}.blocks[{i}]'
        path = sources.path(b.get('src'), where)
        size = sources.image(path).size
        masks = b.get('masks', [])
        if not isinstance(masks, list):
            fail(where, '"masks" is a list of boxes to paint out (names, IDs, dates) before cropping')
        for j, m in enumerate(masks):
            sources.masks.setdefault(path, []).append(need_box(m, f'{where}.masks[{j}]', size))
    prepared, files, warnings = {}, [], {}
    for card, i, b in board_blocks(data):
        where = f'card {card.get("id")}.blocks[{i}]'
        path = sources.path(b['src'], where)
        image = sources.image(path)
        bg = background(image)
        if image.width < MIN_WIDTH:
            warnings.setdefault(card['id'], []).append(
                f'板书原图只有 {image.width}px 宽（低于 {MIN_WIDTH}px，多半被聊天软件压缩过）：卡面就是这张图，小字可能看不清；'
                '交付说明里请用户补发 ClassIn 原图，补来后同一 deck.json 重建即可原位更新')
        tone_default = b.get('tone', 'auto')
        if tone_default not in TONES:
            fail(where, f'"tone" is one of {list(TONES)}')
        crops = b.get('crops')
        if not isinstance(crops, list) or not crops:
            fail(where, '"crops" lists the parts of the board this knowledge point needs, in reading order')
        block = dict(b)
        block['crops'] = []
        for j, crop in enumerate(crops):
            w = f'{where}.crops[{j}]'
            if not isinstance(crop, dict):
                fail(w, 'each crop is an object: {"box": [x0, y0, x1, y1], "speech": "…", "spots": […]}')
            box = need_box(crop.get('box'), f'{w}.box', image.size)
            piece = image.crop(box)
            paint = ImageDraw.Draw(piece)
            for m in sources.masks.get(path, []):
                x0, y0, x1, y1 = max(m[0], box[0]), max(m[1], box[1]), min(m[2], box[2]), min(m[3], box[3])
                if x0 < x1 and y0 < y1:
                    paint.rectangle((x0 - box[0], y0 - box[1], x1 - box[0] - 1, y1 - box[1] - 1), fill=bg)
            sources.crops.setdefault(path, []).append((box, piece.copy()))
            if piece.width > MAX_CROP_WIDTH:
                piece = piece.resize((MAX_CROP_WIDTH, round(piece.height * MAX_CROP_WIDTH / piece.width)), Image.LANCZOS)
            tone = crop.get('tone', tone_default)
            if tone not in TONES:
                fail(w, f'"tone" is one of {list(TONES)}')
            if tone == 'auto':
                tone = tone_of(background(piece))
            data_bytes = png_bytes(piece)
            name = MEDIA_PREFIX + hashlib.sha1(data_bytes).hexdigest()[:16] + '.png'
            target = media / name
            if not target.is_file():
                target.write_bytes(data_bytes)
            files.append(name)
            spots = []
            for k, s in enumerate(crop.get('spots', []) or []):
                sw = f'{w}.spots[{k}]'
                if not isinstance(s, dict):
                    fail(sw, 'each spot is an object: {"box": [x0, y0, x1, y1], "speech": "…"}')
                sb = need_box(s.get('box'), f'{sw}.box', image.size)
                x0, y0, x1, y1 = max(sb[0], box[0]), max(sb[1], box[1]), min(sb[2], box[2]), min(sb[3], box[3])
                if not (x0 < x1 and y0 < y1):
                    fail(sw, f'spot {sb} lies outside its crop {box}; spots use the same original-pixel coordinates as the crop')
                cw, ch = box[2] - box[0], box[3] - box[1]
                spots.append({'left': round(100 * (x0 - box[0]) / cw, 3), 'top': round(100 * (y0 - box[1]) / ch, 3),
                              'width': round(100 * (x1 - x0) / cw, 3), 'height': round(100 * (y1 - y0) / ch, 3)})
            lines = max(1, round((box[3] - box[1]) / sources.pitch(path)))
            block['crops'].append(dict(crop, _media={'file': name, 'w': piece.width, 'h': piece.height, 'tone': tone, 'spots': spots,
                                                     'src': b['src'], 'box': box, 'lines': lines}))
        blocks = prepared.setdefault(card['id'], list(card['blocks']))
        blocks[i] = block
    delivered = {}
    if deliver is not None:
        deliver = Path(deliver)
        for path, crops in sources.crops.items():
            image = sources.image(path)
            sheet = Image.new('RGB', image.size, background(image))
            for box, piece in crops:
                sheet.paste(piece, (box[0], box[1]))
            data_bytes = png_bytes(sheet)
            stem = re.sub(r'\.[0-9a-f]{10}$', '', path.stem)  # a rebuild from the delivered folder keeps the same name
            name = f'{stem}.{hashlib.sha1(data_bytes).hexdigest()[:10]}.png'
            deliver.mkdir(parents=True, exist_ok=True)
            if not (deliver / name).is_file():
                (deliver / name).write_bytes(data_bytes)
            delivered[path] = f'{deliver.name}/{name}'
    return prepared, sorted(set(files)), warnings, {'map': delivered, 'resolve': sources.path}


def delivered_deck(data, base, delivered):
    """A copy of the deck whose board sources point at the delivered (crop-only) copies."""
    out = json.loads(json.dumps(data, ensure_ascii=False))
    for _, _, b in board_blocks(out):
        path = delivered['resolve'](b['src'], 'deliver')
        if path in delivered['map']:
            b['src'] = delivered['map'][path]
            b.pop('masks', None)  # already painted into the delivered copy
    return out


# ---------------------------------------------------------------- CLI

def main(argv=None):
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('inputs', nargs='*', type=Path, help='board image(s), then the output folder')
    ap.add_argument('--threshold', type=int, default=40, help='colour difference that counts as ink (raise for noisy photos)')
    ap.add_argument('--gap', type=int, help='blank rows that separate two regions (default ~28 px per 1300 px of width)')
    ap.add_argument('--col-gap', type=int, help='blank columns that split a band into side-by-side regions (default 12%% of width)')
    ap.add_argument('--union', nargs='+', metavar=('REGIONS_JSON', 'ID'), help='print the box that joins these regions')
    a = ap.parse_args(argv)
    if a.union:
        info = json.loads(Path(a.union[0]).read_text(encoding='utf-8'))
        regions = {r['id']: r['box'] for r in info['regions']}
        missing = [i for i in a.union[1:] if i not in regions]
        if missing or len(a.union) < 2:
            sys.exit(f'✗ unknown or missing region ids: {missing or "give at least one"}')
        print(json.dumps({'box': union([regions[i] for i in a.union[1:]]), 'regions': a.union[1:]}))
        return
    if len(a.inputs) < 2:
        ap.error('give one or more board images and an output folder (or --union regions.json R01 R02)')
    *images, out = a.inputs
    out.mkdir(parents=True, exist_ok=True)
    summary = []
    for path in images:
        image = upright_rgb(Image.open(path))
        bg, regions = propose(image, a.threshold, a.gap, a.col_gap)
        pages = overlay_pages(image, regions, out, path.stem)
        info = {'source': str(path), 'size': list(image.size), 'background': '#%02x%02x%02x' % bg, 'tone': tone_of(bg),
                'legibility': 'low' if image.width < MIN_WIDTH else 'ok', 'regions': regions, 'pages': pages,
                'crop_template': [{'region': r['id'], 'box': r['box'], 'where': f'板书约 {round(100 * r["box"][1] / image.height)}% 处',
                                   'points': [], 'speech': ''} for r in regions]}
        target = out / ('regions.json' if len(images) == 1 else f'{path.stem}.regions.json')
        target.write_text(json.dumps(info, ensure_ascii=False, indent=1), encoding='utf-8')
        summary.append({'source': str(path), 'regions': len(regions), 'pages': len(pages), 'json': str(target), 'tone': info['tone'],
                        'legibility': info['legibility']})
        if len(regions) == 1 and regions[0]['box'][3] - regions[0]['box'][1] > 0.8 * image.height:
            print(f'⚠ {path.name}: one region covers the whole board (grid or ruled background?). Try --threshold 70, or read the slices '
                  'from slice_board.py and write the boxes by row ranges.', file=sys.stderr)
    print(json.dumps(summary, ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
