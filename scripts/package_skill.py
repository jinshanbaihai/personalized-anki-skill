"""Package the skill as a zip that can be uploaded to Claude (Settings → Capabilities → Skills) or unpacked
into any agent's skills folder.

Usage: python scripts/package_skill.py [out_dir]     → <out_dir>/anki-ccpt-skill.zip

The zip holds one folder, anki-ccpt-skill/, with SKILL.md, references/, scripts/ and assets/. Tests, caches
and build outputs are left out. The SKILL.md front matter is checked against the upload limits
(name: lowercase letters, digits and hyphens, at most 64 characters; description at most 1024 characters).
"""
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NAME = 'anki-ccpt-skill'
INCLUDE = ('SKILL.md', 'README.md', 'LICENSE', 'references', 'scripts', 'assets')
SKIP = re.compile(r'(__pycache__|\.pytest_cache|\.pyc$|test_ccpt6\.py$|conftest\.py$|\.DS_Store$|\.apkg$)')


def front_matter():
    text = (ROOT / 'SKILL.md').read_text(encoding='utf-8')
    m = re.match(r'---\n(.*?)\n---\n', text, re.S)
    if not m:
        raise SystemExit('SKILL.md needs a front matter block')
    fields = dict(line.split(': ', 1) for line in m.group(1).splitlines() if ': ' in line)
    name, description = fields.get('name', ''), fields.get('description', '')
    if not re.fullmatch(r'[a-z0-9-]{1,64}', name):
        raise SystemExit(f'name {name!r}: lowercase letters, digits and hyphens, at most 64 characters')
    if not 0 < len(description) <= 1024:
        raise SystemExit(f'description has {len(description)} characters; the limit is 1024')
    return name


def package(out_dir='.'):
    front_matter()
    out = Path(out_dir) / f'{NAME}.zip'
    out.parent.mkdir(parents=True, exist_ok=True)
    count = 0
    with zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED) as z:
        for top in INCLUDE:
            path = ROOT / top
            files = [path] if path.is_file() else sorted(p for p in path.rglob('*') if p.is_file())
            for f in files:
                rel = f.relative_to(ROOT).as_posix()
                if SKIP.search(rel):
                    continue
                z.write(f, f'{NAME}/{rel}')
                count += 1
    return out, count


if __name__ == '__main__':
    target, n = package(sys.argv[1] if len(sys.argv) > 1 else '.')
    print(f'{target} ({n} files, {target.stat().st_size / 1e6:.1f} MB)')
