"""List exam-board fingerprints and unit-exclusive topics found in board/paper text.

Usage:
  python scripts/exam_fingerprint.py board.pdf page.png notes.txt   # PDFs/images are OCR'd when they lack text
  pdftotext -layout paper.pdf - | python scripts/exam_fingerprint.py -

The output is a set of graded clues for references/exam-lock.md, not a decision:
grade A = printed board/unit code, B = layout fingerprint or exclusive topic,
C = course labels. Handwriting and images still need to be read by eye; OCR text
from them can be piped in the same way.
"""
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

LAYOUT = [
    # (board, grade, label, regex)
    ('Pearson Edexcel', 'B', 'Pearson question total', r'\(Total for Question \d+ is \d+ marks?\)'),
    ('Pearson Edexcel', 'B', 'Pearson answer book page header', r'Write the answer to Question \d+ on these \d+ pages'),
    ('Pearson Edexcel', 'B', 'Pearson paper total', r'TOTAL FOR PAPER IS \d+ MARKS'),
    ('Pearson Edexcel', 'B', 'scanned marking columns (B/M/A per question)', r'\bQ\d{2}(?:B|M|A)\d?\b'),
    ('Pearson Edexcel', 'A', 'Pearson paper reference', r'Paper\s+[Rr]eference\s+(W[A-Z]{2}\d{2}/0\dA?|\d[A-Z]{2}\d/0\d)'),
    ('Pearson Edexcel', 'A', 'Pearson publications code', r'Publications Code\s+(\w+)'),
    ('Pearson Edexcel', 'A', 'IAL unit code', r'\b(WMA1[1-4]|WST0[1-3]|WME0[1-3]|WFM0[1-3]|WDM11|WEC1[1-4]|WPH1[1-6]|WCH1[1-6]|WBI1[1-6])(?:/0\dA?)?\b'),
    ('Pearson Edexcel', 'A', 'UK GCE code', r'\b(9MA0|9FM0|9EC0|9PH0|9CH0|9BI0)(?:/0\d)?\b'),
    ('Cambridge International', 'A', 'CIE component header', r'\b(9\d{3})/(\d)(\d)/(?:M/J|O/N|F/M)/\d{2}\b'),
    ('Cambridge International', 'B', 'UCLES copyright', r'©\s*UCLES\s*\d{4}'),
    ('Cambridge International', 'B', 'CIE page count line', r'This document (?:has|consists of) \d+ (?:printed )?pages'),
    ('Cambridge International', 'B', 'CIE structured total', r'\[Total:\s*\d+\]'),
    ('AQA', 'A', 'AQA file code', r'AQA-\d{4,5}-(?:QP|MS|WRE)-[A-Z]{3}\d{2}'),
    ('OCR', 'A', 'OCR component', r'\bH\d{3}/0\d\b'),
    ('IB', 'A', 'IB paper code', r'\b[MN]\d{2}/\d/[A-Z]+/[HS]P\d/ENG/TZ\d\b'),
    ('College Board AP', 'B', 'AP free-response heading', r'AP®?\s+[A-Z][\w ]+ Free-Response Questions'),
]

LABELS = [
    ('Pearson Edexcel', 'C', 'course label EDX/IAL', r'\b(?:EDX|Edexcel|IAL)\b'),
    ('Cambridge International', 'C', 'course label CIE/CAIE', r'\b(?:CIE|CAIE)\b'),
]

# Topic → where it is examined. Each entry is a pointer to verify in the spec text,
# recorded with the spec clause in exam.evidence; it is not proof by itself.
EXCLUSIVE = [
    (r'r\s*=\s*a\s*\+\s*[λt]\s*b|vector equation of (?:a|the) line', 'vector equation of a line',
     'Pearson IAL P4 (WMA14) 7.6; CIE 9709 P3; UK 9FM0 Core Pure — not UK 9MA0'),
    (r'sampling frame|sampling unit|sampling distribution|\bstatistic\b', 'population, sampling frame, statistic',
     'Pearson IAL S2 (WST02) 4.1–4.2 (enumerate all samples); S3 3.2 if σ²/n or CLT appears'),
    (r'central limit|σ\s*\^?2\s*/\s*n', 'distribution of the sample mean / CLT', 'Pearson IAL S3 (WST03) 3.2, 3.6'),
    (r'Poisson|Po\(', 'Poisson distribution', 'Pearson IAL S2 1.1–1.3; CIE 9709 P6; UK 9FM0 — not UK 9MA0'),
    (r'permutation|arrangements? of', 'permutations and combinations', 'CIE 9709 P5; absent from Pearson IAL'),
    (r'geometric distribution|Geo\(', 'geometric distribution', 'CIE 9709 P5; absent from Pearson IAL'),
    (r'Argand|complex number', 'complex numbers', 'CIE 9709 P3; Pearson IAL FP1/FP2 (not P1–P4)'),
    (r'large data set', 'large data set', 'UK 9MA0 statistics; absent from Pearson IAL'),
    (r'proof by contradiction', 'proof by contradiction', 'Pearson IAL P4 1.1; UK 9MA0 Paper 1/2'),
    (r'partial fraction', 'partial fractions', 'Pearson IAL P4 2.1 (incl. improper); CIE 9709 P3'),
    (r'property rights|nudge|pollution permit', 'property rights / nudge / permits', 'CIE 9708 A Level 8.1.1 (Paper 3/4), not AS'),
    (r'externalit', 'externalities', 'CIE 9708 AS 3.2 tools; A Level 7.4 and 8.1 evaluation'),
]


def scan(text):
    clues = []
    for board, grade, label, pattern in LAYOUT + LABELS:
        found = sorted({m.group(0).strip() for m in re.finditer(pattern, text)})
        if found:
            clues.append({'board': board, 'grade': grade, 'clue': label, 'matches': found[:6]})
    topics = []
    for pattern, topic, where in EXCLUSIVE:
        if re.search(pattern, text, re.I):
            topics.append({'topic': topic, 'examined_in': where, 'grade': 'B (verify in spec text)'})
    boards = {}
    for c in clues:
        boards.setdefault(c['board'], set()).add(c['grade'])
    ranking = sorted(boards.items(), key=lambda kv: min(kv[1]))
    return {'board_candidates': [{'board': b, 'best_grade': min(g)} for b, g in ranking], 'clues': clues, 'topics': topics,
            'next': 'Map every board topic to a clause of each candidate spec; record ruled_out with reasons (references/exam-lock.md).'}


def ocr(image):
    if not shutil.which('tesseract'):
        raise SystemExit('tesseract is needed to read images (apt install tesseract-ocr tesseract-ocr-chi-sim / brew install tesseract)')
    return subprocess.run(['tesseract', str(image), '-', '-l', 'eng+chi_sim'], capture_output=True, text=True).stdout


def read(path):
    if path == '-':
        return sys.stdin.read()
    p = Path(path)
    if p.suffix.lower() == '.pdf':
        text = subprocess.run(['pdftotext', '-layout', str(p), '-'], capture_output=True, text=True).stdout
        if len(text.strip()) > 200:
            return text
        with tempfile.TemporaryDirectory() as tmp:
            subprocess.run(['pdftoppm', '-r', '200', '-png', str(p), f'{tmp}/pg'], check=True)
            return '\n'.join(ocr(img) for img in sorted(Path(tmp).glob('pg*.png')))
    if p.suffix.lower() in ('.png', '.jpg', '.jpeg', '.webp', '.tif', '.tiff'):
        return ocr(p)
    return p.read_text(encoding='utf-8', errors='replace')


def main():
    paths = sys.argv[1:] or ['-']
    print(json.dumps(scan('\n'.join(read(p) for p in paths)), ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
