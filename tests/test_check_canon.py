"""Regression fixtures: structural gate must reject broken law manifests."""
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from scripts.check_canon import CANON, SKILL, REQUIRED, check


class CanonContractTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        for path in REQUIRED:
            file = self.root / path
            file.parent.mkdir(parents=True, exist_ok=True)
            file.write_text('present\n', encoding='utf-8')
        laws = '\n'.join(f'## L{i} — Law {i}' for i in range(1, 7))
        self.write(CANON, laws + '\nhttps://github.com/DietrichGebert/ponytail\n')
        self.write(SKILL, '---\nname: pingponglaw\ndescription: valid\n---\n# Skill\n')
        self.write('AGENTS.md', f'Read {CANON} and {SKILL}\n')
        self.write('README.md', ''.join(f'[Doc]({path})\n' for path in (
            CANON, 'docs/CHATGPT_START.md', 'docs/CODEX_INSTALL.md', 'docs/ROADMAP_FASES.md')))

    def write(self, path, text):
        (self.root / path).write_text(text, encoding='utf-8')

    def test_valid_fixture(self):
        self.assertEqual(check(self.root), [])

    def test_missing_law(self):
        self.write(CANON, (self.root / CANON).read_text().replace('## L6 — Law 6', ''))
        self.assertTrue(any('headings' in x for x in check(self.root)))

    def test_duplicate_law(self):
        self.write(CANON, (self.root / CANON).read_text() + '\n## L6 — duplicate\n')
        self.assertTrue(any('headings' in x for x in check(self.root)))

    def test_outdated_skill_ref(self):
        self.write(CANON, (self.root / CANON).read_text() + '\n.agents/skills/kiss-ponytail/SKILL.md\n')
        self.assertTrue(any('obsolete' in x for x in check(self.root)))

    def test_broken_markdown_link(self):
        self.write('README.md', (self.root / 'README.md').read_text() + '\n[Missing](docs/nope.md)\n')
        self.assertTrue(any('broken relative link' in x for x in check(self.root)))

    def test_missing_agents_instruction(self):
        self.write('AGENTS.md', 'no links\n')
        self.assertTrue(any('AGENTS missing reference' in x for x in check(self.root)))

    def test_bad_skill_frontmatter(self):
        self.write(SKILL, '# not frontmatter\n')
        self.assertTrue(any('frontmatter' in x for x in check(self.root)))

    def test_missing_file(self):
        (self.root / 'docs/CODEX_INSTALL.md').unlink()
        self.assertTrue(any('missing or empty' in x for x in check(self.root)))

    def test_ignore_fenced_example_links(self):
        example = '\n' + chr(96) * 3 + 'markdown\n[Example](not-a-file.md)\n' + chr(96) * 3 + '\n'
        self.write('README.md', (self.root / 'README.md').read_text() + example)
        self.assertEqual(check(self.root), [])


if __name__ == '__main__':
    unittest.main()
