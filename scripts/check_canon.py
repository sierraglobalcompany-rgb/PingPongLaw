#!/usr/bin/env python3
"""Small stdlib-only structural check for PingPongLaw; not an audit of applications."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
CANON = 'docs/engineering/LEYES_IMPLEMENTACION_1_A_6.md'
SKILL = '.agents/skills/pingponglaw/SKILL.md'
REQUIRED = [
    'README.md', 'AGENTS.md', CANON, SKILL,
    'docs/ROADMAP_FASES.md', 'docs/CHATGPT_START.md',
    'docs/CODEX_INSTALL.md', 'docs/PONYTAIL_RESEARCH.md',
    'docs/INTEGRACION_REPOS.md',
]

def main() -> int:
    errors = []
    for path in REQUIRED:
        f = ROOT / path
        if not f.is_file() or f.stat().st_size == 0:
            errors.append(f'missing or empty: {path}')
    if (ROOT / CANON).is_file():
        text = (ROOT / CANON).read_text(encoding='utf-8')
        found = re.findall(r'(?m)^## L([1-6])\s+[—-]', text)
        if found != list('123456'):
            errors.append(f'expected exactly ordered L1-L6 headings, found {found}')
        if 'DietrichGebert/ponytail' not in text:
            errors.append('source Ponytail reference missing from canon')
    if (ROOT / SKILL).is_file():
        txt = (ROOT / SKILL).read_text(encoding='utf-8')
        if not txt.startswith('---\n') or 'name: pingponglaw' not in txt:
            errors.append('skill frontmatter not valid')
    if (ROOT / 'AGENTS.md').is_file():
        txt = (ROOT / 'AGENTS.md').read_text(encoding='utf-8')
        for path in (CANON, SKILL):
            if path not in txt:
                errors.append(f'AGENTS missing reference to {path}')
    if errors:
        for message in errors:
            print('FAIL:', message, file=sys.stderr)
        return 1
    print('PASS: 6 laws and PingPongLaw entrypoints structurally intact')
    print('NOTE: Does NOT prove Codex loaded instructions or plugin hooks are active')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
