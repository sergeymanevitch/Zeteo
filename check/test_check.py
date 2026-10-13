# /// script
# requires-python = ">=3.10"
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

import contextlib  # noqa: E402
import importlib.util  # noqa: E402
import io  # noqa: E402
import pathlib  # noqa: E402
import shutil  # noqa: E402
import tempfile  # noqa: E402
import unittest  # noqa: E402
from unittest import mock  # noqa: E402

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parent
DOCUMENTS = ("CLAUDE.md", "identity.md", "rules.md", "examples.md", "README.md", "results.md", "reference",
             "data/CONTEXT.md")


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

    def test_plant_rule_widened_in_keys(self):
        self.change("reference/keys.md", "try_cast(plant AS INTEGER) = 65 ",
                    "try_cast(plant AS INTEGER) = 65 OR plant = '65E' ")
        failures = self.assertFails("reference/keys.md", "the plant as a number is written differently")
        self.assertEqual(len(failures), 1, failures)

    def test_plant_rule_deleted_from_keys(self):
        path = self.root / "reference/keys.md"
        lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
        kept = [line for line in lines if "try_cast(plant AS INTEGER) = 65" not in line]
        self.assertEqual(len(kept), len(lines) - 1)
        path.write_text("".join(kept), encoding="utf-8")
        self.assertFails("reference/keys.md", "the plant as a number found 0 times")

    def test_digit_in_front_of_a_stated_count(self):
        self.change("reference/ik17.md", "30,964 points", "130,964 points")
        failures = self.assertFails("reference/ik17.md", "phrase not found", "30,964 points")
        self.assertEqual(len(failures), 1, failures)

    def test_example_not_registered(self):
        path = self.root / "examples.md"
        path.write_text(path.read_text(encoding="utf-8")
                        + "\n## 11. One more\n\n```sql\nSELECT 1;\n```\n\n**A:** 1.\n", encoding="utf-8")
        self.assertFails("example 11 is not in check.py's EXAMPLES")

    def test_example_number_twice(self):
        self.change("examples.md", "## 8. Notifications in a month", "## 7. Notifications in a month")
        self.assertFails("example 7 appears twice")

    def test_example_sql_that_writes_is_not_run(self):
        self.change("examples.md", "SELECT count(*) AS orders\nFROM ZW38_KG\nWHERE main_work_center = '6415'",
                    "CREATE TABLE ZW38_COPY AS SELECT count(*) AS orders\nFROM ZW38_KG\n"
                    "WHERE main_work_center = '6415'")
        self.assertFails("example 7", "not one statement that reads")
        tables = [t for (t,) in self.con.execute("SELECT table_name FROM information_schema.tables").fetchall()]
        self.assertNotIn("ZW38_COPY", tables)

    def test_recorded_rows_differ_from_the_sql(self):
        digest = check.EXAMPLES[7][0]
        with mock.patch.dict(check.EXAMPLES, {7: (digest, [("444",)], [])}):
            failures = self.failures()
        self.assertEqual(len(failures), 1, failures)
        self.assertIn("example 7: its SQL returns", failures[0])

    def test_written_in_reads_a_whole_number(self):
        self.assertTrue(check.written_in("4,202", "114 of 4,202 readings"))
        self.assertFalse(check.written_in("4,202", "114 of 14,202 readings"))
        self.assertFalse(check.written_in("4,202", "114 of 4,202.5 readings"))

    def test_exit_codes(self):
        out = io.StringIO()
        with mock.patch.object(check, "connect", return_value=self.con), contextlib.redirect_stdout(out):
            self.assertEqual(check.main(["--root", str(self.root)]), 0)
            self.change("examples.md", "**A:** 443.", "**A:** 442.")
            self.assertEqual(check.main(["--root", str(self.root)]), 1)

    def facts(self, *facts):
        return check.check_facts(self.root, self.con, list(facts))[0]

    def test_wrong_decimal(self):
        failures = self.facts(("examples.md", "125 completed ({79.62} %)", "SELECT 79.63"))
        self.assertEqual(failures, ["examples.md: '125 completed (79.62 %)': stated 79.62; measured 79.63"])

    def test_wrong_date(self):
        failures = self.facts(("reference/keys.md", "One row reads {9202-12-15}", "SELECT DATE '9202-12-16'"))
        self.assertEqual(len(failures), 1, failures)
        self.assertIn("stated 9202-12-15; measured 9202-12-16", failures[0])

    def test_null_result(self):
        failures = self.facts(("reference/codes.md", "| 1 | immediately | {70,430} |", "SELECT NULL"))
        self.assertEqual(len(failures), 1, failures)
        self.assertIn("stated 70,430; measured None", failures[0])

    def test_statement_that_does_not_hold(self):
        failures = self.facts(("reference/ik17.md", "a point belongs to one location", "SELECT false"))
        self.assertEqual(len(failures), 1, failures)
        self.assertIn("does not hold", failures[0])

    def test_two_rows_for_one_phrase(self):
        failures = self.facts(("reference/codes.md", "| 1 | immediately | {70,430} |",
                               "SELECT 70430 UNION ALL SELECT 70430"))
        self.assertEqual(len(failures), 1, failures)
        self.assertIn("expected one row", failures[0])

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
