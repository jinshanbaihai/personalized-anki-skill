"""Package the skill as a zip that can be uploaded to Claude (Settings → Capabilities → Skills) or unpacked
into any agent's skills folder.

Usage: python scripts/package_skill.py [out_dir]     → <out_dir>/anki-ccpt-skill.zip

The zip holds one folder, anki-ccpt-skill/, with SKILL.md, references/, scripts/ and assets/. Only files
tracked by git are packed (a stray .env, collection or marked scan in the working tree never ships), tests,
caches and build outputs are left out, and the packer refuses to write when it finds untracked files in those
folders or anything that looks like an e-mail address, a Google Drive link or a secret. The SKILL.md front
matter is checked against the upload limits (name: lowercase letters, digits and hyphens, at most 64
characters; description at most 1024 characters).
"""
import re
import subprocess
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NAME = 'anki-ccpt-skill'
INCLUDE = ('SKILL.md', 'README.md', 'LICENSE', 'references', 'scripts', 'assets')
SKIP = re.compile(r'(__pycache__|\.pytest_cache|\.pyc$|(^|/)test_[\w-]*\.py$|conftest\.py$|requirements-dev\.txt$|\.DS_Store$|\.apkg$)')
TEXT = re.compile(r'\.(md|py|mjs|js|json|css|txt|html)$|(^|/)(LICENSE|SKILL\.md|README\.md)$')
LEAKS = [
    ('e-mail address', re.compile(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}')),
    ('Google Drive link', re.compile(r'drive\.google\.com|docs\.google\.com/(?:document|spreadsheets)/d/')),
    ('secret assignment', re.compile(r'(?m)^\s*(?:export\s+)?[A-Z][A-Z0-9_]*(?:KEY|SECRET|TOKEN|PASSWORD)\s*[=:]\s*[\'"]?[A-Za-z0-9/+_.-]{8,}')),
]
ALLOWED = {'noreply@anthropic.com'}


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


def git(*args):
    return subprocess.run(['git', '-C', str(ROOT), *args], capture_output=True, text=True, encoding='utf-8', check=True).stdout.splitlines()


def tracked_files(strict=True):
    """Files git tracks under INCLUDE; untracked files there stop the packer instead of slipping in."""
    try:
        files = git('ls-files', '--', *INCLUDE)
        untracked = [f for f in git('ls-files', '--others', '--exclude-standard', '--', *INCLUDE) if not SKIP.search(f)]
    except (OSError, subprocess.CalledProcessError):
        raise SystemExit('package from a git checkout of the skill: only tracked files are packed')
    if untracked and strict:
        raise SystemExit('untracked files in the skill folders (commit or remove them first):\n  ' + '\n  '.join(untracked[:20]))
    return [f for f in files if (ROOT / f).is_file() and not SKIP.search(f)]


def leaks(rel, data):
    if not TEXT.search(rel):
        return []
    text = data.decode('utf-8', errors='replace')
    found = []
    for label, pattern in LEAKS:
        for m in pattern.finditer(text):
            if m.group(0) in ALLOWED:
                continue
            line = text.count('\n', 0, m.start()) + 1
            found.append(f'{rel}:{line}: {label}: {m.group(0)[:60]}')
    return found


def package(out_dir='.', files=None):
    front_matter()
    files = tracked_files() if files is None else files
    problems = [hit for rel in files for hit in leaks(rel, (ROOT / rel).read_bytes())]
    if problems:
        raise SystemExit('refusing to package; remove personal data or secrets first:\n  ' + '\n  '.join(problems[:30]))
    out = Path(out_dir) / f'{NAME}.zip'
    out.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED) as z:
        for rel in sorted(files):
            z.write(ROOT / rel, f'{NAME}/{rel}')
    return out, len(files)


if __name__ == '__main__':
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    target, n = package(sys.argv[1] if len(sys.argv) > 1 else '.')
    print(f'{target} ({n} files, {target.stat().st_size / 1e6:.1f} MB)')
