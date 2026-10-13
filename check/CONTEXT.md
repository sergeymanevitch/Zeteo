---
layer: L2
type: contract
---

# check — hold the documents to the data

One job: recompute the numbers its registry lists — the stated counts of
[`reference/`](../reference/CONTEXT.md), [`data/CONTEXT.md`](../data/CONTEXT.md) and README § The
data, the worked examples, and the `closed_on` and B4 numbers of [`results.md`](../results.md) — and fail when a document and the data disagree. A new number written into a
document is checked only once a row for it is added to the registry. Added after the run on the thirty unseen questions; no arm was run
with it, and no arm ever sees it.

It lives here, outside the folder, on purpose. The folder is the files `FOLDER` lists in
[../run/make_arm.sh](../run/make_arm.sh), their one home, and `make_arm.sh treatment` copies those
and nothing else; a check inside the folder would put its registry of expected numbers in front of
the model answering. It is not part of [../run/](../run/CONTEXT.md) either: that folder is the kit
that runs and records the arms.

## Inputs

- The documents, from the repository root or from `--root DIR`: [../examples.md](../examples.md),
  every file of [../reference/](../reference/CONTEXT.md), [../data/CONTEXT.md](../data/CONTEXT.md),
  [../README.md](../README.md) § The data, the `closed_on` and B4 numbers of
  [../results.md](../results.md) § What changed, and for the repeated rules also
  [../CLAUDE.md](../CLAUDE.md), [../identity.md](../identity.md) and [../rules.md](../rules.md).
- The data, always from this repository's [../data/](../data/CONTEXT.md), loaded by `connect()` of
  [../query.py](../query.py) itself, so the check reads the tables exactly as the folder does.

## Process

[check.py](check.py) runs three checks, each written as a table in the script. `EXAMPLES` and
`FACTS` run queries against the data; `RULES` reads the documents alone:

- **`EXAMPLES`** — for each of the ten worked examples: a sha256 prefix of its SQL block, the rows
  that SQL returns, and every number its `**A:**` paragraph writes, tied to a cell. The SQL must be
  the recorded SQL, it must return the recorded rows, and each written number must stand in the
  paragraph and, with commas, backticks, ` %` and the minus sign normalised, equal its cell.
- **`FACTS`** — `(file, phrase, sql)`: the phrase, with its stated numbers marked `{...}`, must stand
  in the file (whitespace collapsed), and the query's one row must equal the marked numbers in order
  (whole numbers exactly, decimals to the places written, dates as ISO strings). A statement that is
  no number — a set of codes, "a point belongs to one location" — has no marks and a query that
  returns one boolean, which must be true. A phrase must stand on its own: no digit or letter just
  before it, and none just after when it ends in a digit. The extra numbers of the `**A:**`
  paragraphs (228, 69, the next unit's 49, 79.62 %, the other 12, 439,717,316.60) are facts too.
- **`RULES`** — the SQL rules the documents repeat: the plant as a number, the plant of a location,
  a completed order, the first code of a status field. Every occurrence a loose anchor finds must be
  the canonical text once whitespace is collapsed, with the plant number and the field name as
  variables, followed by the end of a clause (the end of a line, `AND`, `)`, `;`, `--`, or a
  backtick); each file that holds a rule must still hold it. The plant anchor also finds `cast(plant`
  and `plant::`, so a plant read another way fails.

An example's SQL runs only if [../query.py](../query.py)'s own `one_read` accepts it as one statement
that reads, so a changed copy cannot write to the data the check holds open.

A query that fails is a failure, reported on its own line; the run goes on.

[test_check.py](test_check.py) copies the documents into a temporary directory, changes one thing
— a number of an example, the SQL of an example, a count of
[`codes.md`](../reference/codes.md), the completed-order rule in [`examples.md`](../examples.md),
the plant rule in [`keys.md`](../reference/keys.md) widened or deleted, closed orders in
[`zw38.md`](../reference/zw38.md) widened to `CMPL` with `NCMP`, a digit added in front of a
stated count, an eleventh example — and requires the check to fail on the copy, as it requires the
unchanged copy to pass. It also feeds the check registry rows the data contradicts (a whole number,
a decimal, a date, a NULL, a false statement, two rows for one phrase), a query that errors, and
recorded rows the SQL does not return, and checks the exit code. The data is loaded once.

From the repository root:

    uv run check/check.py                 # exit 0 and one summary line, or one line per failure and exit 1
    uv run check/check.py --root DIR      # the documents of DIR against this repository's data
    uv run check/test_check.py            # the negative tests

Both pin `duckdb` 1.5.6, as [../query.py](../query.py) does, need Python 3.10 or newer (`uv`
fetches one when the system Python is older), and write no `__pycache__`. The recorded rows of
`EXAMPLES` are the cells as `duckdb` 1.5.6 prints them; another version, run through a plain
`python3`, may format a cell differently.

## Outputs

Nothing on disk. Standard output: one line per failure, naming the file, the example or the phrase,
and what was stated against what was measured; or, when everything holds, one line with how many
examples, facts and rule occurrences were checked. Exit 1 on any failure, 0 otherwise.

## Human check

When a document changes a number, or an example's SQL changes, the check fails until the registry in
[check.py](check.py) is updated. Whoever updates it re-runs the query, reads the result, and only
then writes the new value in both places. A failing line is a question about the document or the
data, never a reason to edit the registry until it passes.

## Left out on purpose

Stated numbers the check does not recompute, and why:

- **The sha256 digests** of [../data/CONTEXT.md](../data/CONTEXT.md): they are of the files' bytes,
  not of their contents; `shasum -a 256 data/*.parquet` checks them, and git holds the files.
- **The shape of a functional location** in [../reference/keys.md](../reference/keys.md) — the
  sample `D-88-02-M-00700/03`, the segment meanings, "five digits, or four digits and a letter",
  `/03` the third unit, `D-65-02` an area: an illustration and a definition, not a count.
- **"Dates up to five years ahead occur"** in `keys.md` § A date later than today: the owner's reading
  of what a planned date can be, not a measurement.
- **The meanings of codes** in [../reference/codes.md](../reference/codes.md) and every "(Sergey, …)"
  decision: domain meanings, which the data cannot confirm.
- **The separators** of status fields (commas on notifications, one or two spaces on orders) and the
  sample status `TECO PRT GMPS MACM PRC SETC`: a format described for reading, not a count.
- **"Most of them completed by their system status"** of the first code `PLAN` in `codes.md`: what
  "completed" is for a notification and for an order is two definitions; the claim is left to a
  person.
- **"Most points are judged, not measured"** in [../reference/ik17.md](../reference/ik17.md): it
  follows from the two counts beside it, which are checked.
- **Sample values and types** — work centers `3211`, `64MAINT`, `43PUMP` in
  [../reference/ziw28.md](../reference/ziw28.md), beside a count of work centers that is checked;
  the columns' types, which `uv run query.py --tables` prints.
- **The numbers of the questions** in [../examples.md](../examples.md) (plants, months, priorities,
  the example run dates): they are what is asked, not what is answered.
- **Numbers outside the data**: the results, timings and costs of [../results.md](../results.md) and
  the rest of [../README.md](../README.md) come from the run transcripts, not from the Parquet
  files; only the `closed_on` and B4 numbers of `results.md` § What changed are data, and they are
  checked. The rules of [../rules.md](../rules.md) ("rounded to 2 decimals") are rules.
- **The expected answers** of [../questions.md](../questions.md) and
  [../questions-unseen.md](../questions-unseen.md): they are the committed record, edited only
  where the owner settled an answer after the runs (A9, A3), each in its own commit; where they
  disagree with the data, `results.md` says so.
