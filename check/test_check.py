# /// script
# requires-python = ">=3.9"
# dependencies = ["duckdb==1.5.6"]
# ///
"""Negative tests of check.py: a copy of the documents, changed in one place, must fail.

    uv run check/test_check.py

Each test copies the documents into a temporary directory, changes one thing, and runs the check
on the copy with --root; the data is loaded once for all of them. Nothing is written beside the
repository, not even __pycache__.
"""

import sys

sys.dont_write_bytecode = True

import importlib.util  # noqa: E402
import pathlib  # noqa: E402
import shutil  # noqa: E402
import tempfile  # noqa: E402
import unittest  # noqa: E402

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parent
DOCUMENTS = ("CLAUDE.md", "identity.md", "rules.md", "examples.md", "README.md", "reference", "data/CONTEXT.md")


def load_check():
    spec = importlib.util.spec_from_file_location("zeteo_check", HERE / "check.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


check = load_check()


class CheckTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.con = check.connect()

    def setUp(self):
        self.root = pathlib.Path(tempfile.mkdtemp(prefix="zeteo-check-"))
        self.addCleanup(shutil.rmtree, self.root)
        for name in DOCUMENTS:
            source, target = REPO / name, self.root / name
            target.parent.mkdir(parents=True, exist_ok=True)
            if source.is_dir():
                shutil.copytree(source, target)
            else:
                shutil.copy2(source, target)

    def change(self, name, old, new):
        path = self.root / name
        text = path.read_text(encoding="utf-8")
        self.assertEqual(text.count(old), 1, f"{old!r} must stand once in {name}")
        path.write_text(text.replace(old, new), encoding="utf-8")

    def failures(self):
        return check.run(self.root, self.con)[0]

    def assertFails(self, *words):
        failures = self.failures()
        self.assertTrue(failures, "the changed copy passed")
        self.assertTrue(any(all(w in line for w in words) for line in failures),
                        f"no failure names {words}: {failures}")
        return failures

    def test_unchanged_copy_passes(self):
        self.assertEqual(self.failures(), [])

    def test_example_number_changed(self):
        self.change("examples.md", "**A:** 187.", "**A:** 188.")
        failures = self.assertFails("example 1", "'187'")
        self.assertEqual(len(failures), 1, failures)

    def test_example_sql_changed(self):
        self.change("examples.md", "  AND priority = 2\n", "  AND priority = 3\n")
        self.assertFails("example 1", "the SQL of example 1 changed")

    def test_codes_count_changed(self):
        self.change("reference/codes.md", "| 70,430 |", "| 70,431 |")
        failures = self.assertFails("reference/codes.md", "phrase not found", "| 70,430 |")
        self.assertEqual(len(failures), 1, failures)

    def test_completed_order_changed_in_examples(self):
        self.change("examples.md", "AND NOT regexp_matches(system_status, '\\bNCMP\\b'))) AS completed",
                    "AND NOT regexp_matches(system_status, '\\bNCMP\\b')\n   OR false)) AS completed")
        self.assertFails("examples.md", "a completed order is written differently")

    def test_plant_rule_changed_in_keys(self):
        self.change("reference/keys.md", "try_cast(plant AS INTEGER) = 65", "try_cast(plant AS BIGINT) = 65")
        failures = self.assertFails("reference/keys.md", "the plant as a number is written differently")
        self.assertEqual(len(failures), 1, failures)

    def test_fact_wrong_against_the_data(self):
        facts = [("reference/codes.md", "| 1 | immediately | {70,430} |", "SELECT 70431")]
        failures = check.check_facts(self.root, self.con, facts)[0]
        self.assertEqual(len(failures), 1, failures)
        self.assertIn("stated 70,430; measured 70431", failures[0])

    def test_query_error_is_a_failure(self):
        facts = [("reference/codes.md", "| 1 | immediately | {70,430} |", "SELECT nothing FROM nowhere"),
                 ("reference/codes.md", "| 2 | within 24 hours | {58,000} |",
                  "SELECT count(*) FROM ZIW28_KG WHERE priority = 2")]
        failures = check.check_facts(self.root, self.con, facts)[0]
        self.assertEqual(len(failures), 1, failures)
        self.assertIn("failed", failures[0])


if __name__ == "__main__":
    unittest.main(verbosity=2)
