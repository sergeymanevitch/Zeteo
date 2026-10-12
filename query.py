# /// script
# requires-python = ">=3.9"
# dependencies = ["duckdb>=1.0"]
# ///
"""Run one read-only SQL query over Zeteo's data and print the result.

    uv run query.py "SELECT count(*) FROM ZIW28_KG WHERE priority = 1"
    python3 query.py "..."          # where the duckdb package is installed
    uv run query.py --tables        # every table and its columns
    echo "SELECT ..." | uv run query.py -

The four Parquet files of data/ are loaded as tables named after their files: IK17_KG, ZIW28_KG,
ZK22_KG, ZW38_KG. After loading, the database is closed to the file system, so a query can read
these tables and nothing else. One statement per call; it must read, not write.
"""

import pathlib
import sys

try:
    import duckdb
except ImportError:
    sys.exit("the duckdb package is missing: run `uv run query.py ...`, or `pip install duckdb` first")

DATA = pathlib.Path(__file__).resolve().parent / "data"
READS = ("select", "with", "describe", "summarize", "show", "from", "values", "(")
SHOWN = 200


def connect():
    con = duckdb.connect()
    files = sorted(DATA.glob("*.parquet"))
    if not files:
        sys.exit(f"no Parquet files in {DATA}")
    for path in files:
        con.execute(f'CREATE TABLE "{path.stem}" AS SELECT * FROM read_parquet(?)', [str(path)])
    con.execute("SET enable_external_access = false")
    con.execute("SET lock_configuration = true")
    return con


def one_read(con, sql):
    if not sql.lower().startswith(READS):
        return False
    if hasattr(con, "extract_statements"):
        try:
            statements = con.extract_statements(sql)
        except duckdb.Error:
            return True  # a parse error is reported when the query runs
        return len(statements) == 1 and statements[0].type == duckdb.StatementType.SELECT
    return ";" not in sql


def cell(value):
    if value is None:
        return "NULL"
    return str(value).replace("|", "\\|").replace("\n", " ")


def show(con, sql):
    result = con.execute(sql)
    names = [d[0] for d in result.description]
    rows = result.fetchmany(SHOWN + 1)
    print("| " + " | ".join(names) + " |")
    print("|" + "---|" * len(names))
    for row in rows[:SHOWN]:
        print("| " + " | ".join(cell(v) for v in row) + " |")
    more = len(rows) > SHOWN
    tail = result.fetchall() if more else []
    total = len(rows) + len(tail)
    print(f"\n{total} row{'' if total == 1 else 's'}" + (f"; the first {SHOWN} shown" if more else ""))


def main():
    args = sys.argv[1:]
    if not args:
        sys.exit(__doc__)
    con = connect()
    if args == ["--tables"]:
        for (table,) in con.execute("SELECT table_name FROM information_schema.tables ORDER BY 1").fetchall():
            cols = con.execute(
                "SELECT column_name || ' ' || data_type FROM information_schema.columns "
                "WHERE table_name = ? ORDER BY ordinal_position", [table]).fetchall()
            count = con.execute(f'SELECT count(*) FROM "{table}"').fetchone()[0]
            print(f"{table} ({count} rows): " + ", ".join(c for (c,) in cols))
        return
    sql = sys.stdin.read() if args == ["-"] else " ".join(args)
    sql = sql.strip().rstrip(";").strip()
    if not one_read(con, sql):
        sys.exit("query.py runs one query that reads (SELECT, WITH, DESCRIBE, SUMMARIZE, SHOW)")
    try:
        show(con, sql)
    except duckdb.Error as error:
        sys.exit(f"query failed: {error}")


if __name__ == "__main__":
    main()
