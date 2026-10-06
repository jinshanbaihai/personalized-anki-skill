"""Write ccpt_single_face.ankiaddon (double-click to install in Anki desktop).

Usage: python scripts/package_addon.py out/
"""
import json
import sys
import zipfile
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / 'single_face_addon.py'
MANIFEST = {'package': 'ccpt_single_face', 'name': 'CCPT 单面阅读卡（Space 播音 · Enter 继续 · 1 隔天再看）',
            'conflicts': [], 'mod': 1790000000}


def write_addon(folder):
    folder = Path(folder)
    folder.mkdir(parents=True, exist_ok=True)
    target = folder / 'ccpt_single_face.ankiaddon'
    with zipfile.ZipFile(target, 'w', zipfile.ZIP_DEFLATED) as z:
        z.writestr('__init__.py', SOURCE.read_text())
        z.writestr('manifest.json', json.dumps(MANIFEST, ensure_ascii=False, indent=1))
    return target


if __name__ == '__main__':
    print(write_addon(sys.argv[1] if len(sys.argv) > 1 else '.'))
