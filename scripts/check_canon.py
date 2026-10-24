#!/usr/bin/env python3
"""Check PingPongLaw's durable entrypoints, not execution of AI agents."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
CANON = 'docs/engineering/LEYES_IMPLEMENTACION_1_A_6.md'
SKILL = '.agents/skills/pingponglaw/SKILL.md'
REQUIRED = (
    'README.md', 'AGENTS.md', CANON, SKILL,
    'docs/CHATGPT_START.md', 'docs/CODEX_INSTALL.md',
    'docs/INTEGRACION_REPOS.md', 'docs/PONYTAIL_RESEARCH.md',
    'docs/ROADMAP_FASES.md', 'docs/VALIDACION_OPERATIVA.md',
    'scripts/check_canon.py', '.github/workflows/verify-canon.yml',
)
LINK = re.compile(r'(?<!!)\[[^\]]*\]\(([^)]+)\)')
HEAD = re.compile(r'^## L([1-6])\s+[—-]', re.MULTILINE)


def without_code_fences(s):
    """Example links in fenced blocks are not navigational references."""
    return re.sub(r'(?ms)^\s*(\x60{3}|~~~)[^\n]*\n.*?^\s*\1[^\n]*$', '', s)


def check(root=ROOT):
    root = Path(root).resolve()
    errors = []
    texts = {}
    for path in REQUIRED:
        target = root / path
        if not target.is_file() or not target.stat().st_size:
            errors.append(f'missing or empty: {path}')
        elif target.suffix in ('.md', '.py', '.yml'):
            try:
                texts[path] = target.read_text(encoding='utf-8')
            except UnicodeError:
                errors.append(f'not UTF-8: {path}')

    canon = texts.get(CANON, '')
    if canon:
        ids = HEAD.findall(without_code_fences(canon))
        if ids != list('123456'):
            errors.append(f'canonical headings not exactly L1-L6 in order: {ids}')
        if 'DietrichGebert/ponytail' not in canon:
            errors.append('Ponytail source missing in canon')
        if '.agents/skills/kiss-ponytail/SKILL.md' in canon:
            errors.append('canon refers to obsolete kiss-ponytail skill')

    agents = texts.get('AGENTS.md', '')
    for path in (CANON, SKILL):
        if agents and path not in agents:
            errors.append(f'AGENTS missing reference to {path}')

    skill = texts.get(SKILL, '')
    if skill and not re.match(r'\A---\n(?:(?!\n---\n)[\s\S])*\n---\n', skill):
        errors.append('skill YAML frontmatter missing or unterminated')
    elif skill and not re.search(r'(?m)^name:\s*pingponglaw\s*$', skill):
        errors.append('skill name does not match pingponglaw')

    readme = texts.get('README.md', '')
    for path in (CANON, 'docs/CHATGPT_START.md', 'docs/CODEX_INSTALL.md', 'docs/ROADMAP_FASES.md'):
        if readme and f']({path})' not in readme:
            errors.append(f'README missing clickable local link: {path}')

    for path, contents in texts.items():
        if not path.endswith('.md'):
            continue
        for match in LINK.finditer(without_code_fences(contents)):
            dest = match.group(1).strip().split(' ', 1)[0].strip('<>')
            if not dest or dest.startswith(('#', '/', 'mailto:')) or '://' in dest:
                continue
            filepart = dest.split('#', 1)[0].split('?', 1)[0]
            if not filepart:
                continue
            target = ((root / path).parent / filepart).resolve()
            if target != root and root not in target.parents:
                errors.append(f'link escapes repo in {path}: {dest}')
            elif not target.exists():
                errors.append(f'broken relative link in {path}: {dest}')
    return errors


def main():
    errors = check()
    for error in errors:
        print('FAIL:', error, file=sys.stderr)
    if errors:
        return 1
    print('PASS: Six laws, skill, entrypoint paths and Markdown local links')
    print('LIMIT: Does not prove semantic compliance, hooks, installation or runtime')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
