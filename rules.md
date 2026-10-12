---
layer: L3
type: reference
---

# How Zeteo answers

## The procedure

1. **Read the question whole.** Name what is counted, summed, shared or looked up, and every
   condition on it: plant, location, work center, priority, type, status, code, period.
2. **Pick the table.** [reference/CONTEXT.md](reference/CONTEXT.md) says which table holds which
   thing. Notifications are `ZIW28_KG`, orders `ZW38_KG`, measuring-point readings `IK17_KG`,
   material costs `ZK22_KG`.
3. **Map every phrase to a column and a value.** Use [reference/codes.md](reference/codes.md) for
   codes and words, [reference/keys.md](reference/keys.md) for plant, location and dates, and the
   table's own file for its columns. A value goes into the query only as it is stored in the data.
4. **State the criteria** in one short list before querying.
5. **Write one SQL query and run it** with the DuckDB CLI from this folder:
   `duckdb -c "<query>"` over `'data/<TABLE>.parquet'`. Quote the column `"order"`.
6. **Answer from the result only**: the number first, then the criteria, then the exact SQL that
   produced it.

Never answer from memory, from an estimate, or from arithmetic done outside a query. If a query
fails, fix it and run it again; do not fall back to a guess.

## Defaults, when the question does not say

- **A month or year** ("in May 2026") filters on `created_on` — for `ZK22_KG`, which has one date,
  on `date`. Use a half-open range: `created_on >= DATE '2026-05-01' AND created_on < DATE '2026-06-01'`.
  The other dates are in [reference/keys.md](reference/keys.md); use one only when the question
  names it (released, closed, scheduled, required, actual).
- **A plant** is matched by the plant rule of [reference/keys.md](reference/keys.md#plant): never a
  plain `plant = 'N'` on notifications, where `65E` and `65I` are plant 65.
- **A count** counts rows. In `IK17_KG` a row is one reading of a point, so "how many points" counts
  readings; give the count of distinct points beside it when the two differ.
- **"Not performed"** points are `text_code IN ('Not performed', 'Not checked')`.
- **A percentage** is `100.0 * part / whole`, rounded to 2 decimals; say what the whole is.
- **A cost** is the net sum of `cost`: returns are negative rows and stay in the sum. Give the
  booked and returned parts beside it when there are returns.
- **A status** "has" a code when the code appears anywhere in the status field, which may hold
  several codes. When one notification number has more than one row, report every row with its
  notification system status, user status and order system status. Decode every code you report with [reference/codes.md](reference/codes.md).

## When the question can be read two ways

Take the reading the defaults give, answer it, and add one line: the other reading and the number
its query returns. Do not ask the user to choose; answer, then show the alternative.

## When the data cannot answer

Say what is missing — no such column, a code [reference/codes.md](reference/codes.md) marks unknown,
a period outside the data's dates, an identifier with no row — and give no number for it. A result
of zero rows is an answer ("0"), but say which filter left nothing.
