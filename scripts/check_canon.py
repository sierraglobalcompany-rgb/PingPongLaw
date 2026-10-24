#!/usr/bin/env python3
"""Structural checks for the six-law canon; not a claim of agent execution."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
CANON = 'docs/engineering/LEYES_IMPLEMENTACION_1_A_6.md'
SKILL = '.agents/skills/pingponglaw/SKILL.md'
LAW_SKILLS = (
    'l1-kiss-ponytail', 'l2-antirruido', 'l3-antiparches',
    'l4-diseno-humano', 'l5-verificacion-independiente', 'l6-anti-ping-pong',
)
DESIGN_SKILLS = ('l4-anti-ui-slop', 'l4-ui-ux-pro-max')
ALL_SKILLS = ('pingponglaw',) + LAW_SKILLS + DESIGN_SKILLS
SKILL_PATHS = tuple(f'.agents/skills/{name}/SKILL.md' for name in ALL_SKILLS)
SKILL_DOCS = (
    'docs/SKILLS_ARQUITECTURA.md',
    'docs/FUENTES_EXTERNAS.md',
    'docs/ROADMAP_SKILLS_AVANZADO.md',
)
REQUIRED = (
    'README.md', 'AGENTS.md', CANON, SKILL,
    'docs/CHATGPT_START.md', 'docs/CODEX_INSTALL.md',
    'docs/INTEGRACION_REPOS.md', 'docs/PONYTAIL_RESEARCH.md',
    'docs/ROADMAP_FASES.md', 'docs/VALIDACION_OPERATIVA.md',
    'scripts/check_canon.py', '.github/workflows/verify-canon.yml',
    *SKILL_PATHS, *SKILL_DOCS,
)
LINK = re.compile(r'(?<!!)\[[^\]]*\]\(([^)]+)\)')
HEAD = re.compile(r'^## L([1-6])\s+[—-]', re.MULTILINE)


def without_code_fences(s):
    """Examples within code fences are not actual Markdown navigation links."""
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
    if agents and 'docs/SKILLS_ARQUITECTURA.md' not in agents:
        errors.append('AGENTS missing skills architecture reference')

    names_seen = set()
    for name in ALL_SKILLS:
        path = f'.agents/skills/{name}/SKILL.md'
        body = texts.get(path, '')
        if not body:
            continue
        match = re.match(r'\A---\n([\s\S]*?)\n---\n', body)
        if not match:
            errors.append(f'bad skill frontmatter: {path}')
            continue
        meta = match.group(1)
        declared = re.search(r'(?m)^name:[ \t]*([a-z0-9-]+)[ \t]*$', meta)
        actual = declared.group(1) if declared else ''
        if actual != name or actual in names_seen:
            errors.append(f'wrong or duplicate skill name: {path}')
        names_seen.add(actual)
        if not re.search(r'(?m)^description:[ \t]*\S', meta):
            errors.append(f'missing skill description: {path}')
        if name != 'pingponglaw' and CANON not in body:
            errors.append(f'skill has no canon link: {path}')

    router = texts.get(SKILL, '')
    for name in LAW_SKILLS + DESIGN_SKILLS:
        if router and name not in router:
            errors.append(f'router missing subskill: {name}')

    readme = texts.get('README.md', '')
    for path in (CANON, 'docs/CHATGPT_START.md', 'docs/CODEX_INSTALL.md',
                 'docs/ROADMAP_FASES.md') + SKILL_DOCS:
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
    print('PASS: six laws, nine skills, router, metadata and Markdown links')
    print('LIMIT: does not prove agent use, hooks, installation or runtime')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
