import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "src"))

from mmu_cli import agents_md  # noqa: E402
from mmu_cli.cli import command_agents, command_init  # noqa: E402


class MergeTests(unittest.TestCase):
    def test_new_file_gets_template_and_block(self):
        merged = agents_md.merge(None, f"{agents_md.BEGIN_MARKER}\nX\n{agents_md.END_MARKER}")
        self.assertTrue(merged.startswith("# AGENTS.md"))
        self.assertIn(agents_md.BEGIN_MARKER, merged)
        self.assertIn(agents_md.END_MARKER, merged)

    def test_existing_block_is_replaced_and_user_content_kept(self):
        block_v1 = f"{agents_md.BEGIN_MARKER}\nold\n{agents_md.END_MARKER}"
        block_v2 = f"{agents_md.BEGIN_MARKER}\nnew\n{agents_md.END_MARKER}"
        existing = f"# Mine\n\nabove\n\n{block_v1}\n\nbelow\n"
        merged = agents_md.merge(existing, block_v2)
        self.assertIn("above", merged)
        self.assertIn("below", merged)
        self.assertIn("new", merged)
        self.assertNotIn("old", merged)
        self.assertEqual(merged.count(agents_md.BEGIN_MARKER), 1)

    def test_file_without_markers_gets_block_appended(self):
        existing = "# Hand-written agent notes\n"
        block = f"{agents_md.BEGIN_MARKER}\nX\n{agents_md.END_MARKER}"
        merged = agents_md.merge(existing, block)
        self.assertTrue(merged.startswith("# Hand-written agent notes"))
        self.assertIn(agents_md.BEGIN_MARKER, merged)


class CommandTests(unittest.TestCase):
    def test_create_then_update_is_idempotent(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            command_init(root, force=False)

            result = command_agents(root)
            self.assertEqual(result.exit_code, 0)
            self.assertTrue(result["created"])
            path = root / "AGENTS.md"
            first = path.read_text(encoding="utf-8")
            self.assertIn("Launch context (Make Me Unicorn)", first)

            path.write_text(first + "\n## Team rules\n- be kind\n", encoding="utf-8")
            result2 = command_agents(root)
            self.assertFalse(result2["created"])
            second = path.read_text(encoding="utf-8")
            self.assertIn("## Team rules", second)
            self.assertEqual(second.count(agents_md.BEGIN_MARKER), 1)

    def test_stdout_mode_prints_block_without_writing(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            command_init(root, force=False)
            result = command_agents(root, stdout=True)
            self.assertEqual(result.exit_code, 0)
            self.assertIn(agents_md.BEGIN_MARKER, result["messages"][0])
            self.assertFalse((root / "AGENTS.md").exists())


if __name__ == "__main__":
    unittest.main()
