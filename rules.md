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
5. **Write one SQL query for each reading the answer gives and run each** — the default reading,
   and the other one when [§ When the question can be read two ways](#when-the-question-can-be-read-two-ways)
   applies — with [query.py](query.py) from this folder: `uv run query.py "<query>"` (or
   `python3 query.py "<query>"` where the `duckdb` package is installed). The tables are named
   `IK17_KG`, `ZIW28_KG`, `ZK22_KG`, `ZW38_KG`; `query.py --tables` lists their columns. Quote the
   column `"order"`. `query.py` reads; it runs no other statement.
6. **Answer from the result only**: the number first, then the criteria, then the exact SQL that
   produced it.

Never answer from memory, from an estimate, or from arithmetic done outside a query. If a query
fails, fix it and run it again; do not fall back to a guess.

## Defaults, when the question does not say

- **A date or a period** filters on the column the question asks about — opened, due, planned,
  released, started, closed — by [reference/keys.md § Dates](reference/keys.md#dates). When it
  names a period and no event, the default is `required_start_date` for notifications, `created_on`
  for orders and readings, `date` for material cost. A day is `col = DATE '2026-10-05'`; a month a
  half-open range: `col >= DATE '2026-05-01' AND col < DATE '2026-06-01'`.
- **A relative period** — this year, last month, these months against the same months last year —
  is read as the user names it, counted from today's date, and compared like with like: years with
  years, months with the same months (Sergey, 2026-10-13). When the period is not over, or the
  table's dates end before it does, say so and give the last date the table holds.
- **A duration** is in calendar days, the plant works around the clock (Sergey, 2026-10-13):
  `date_diff('day', start, end)` between the two dates the question names, read by
  [reference/keys.md § Dates](reference/keys.md#dates).
- **A plant** is matched by the plant rule of [reference/keys.md](reference/keys.md#plant). On
  notifications, plant 65 is `plant` = 65 as a number; the department plants `65E` and `65I` are
  not plant 65 and are left out. "Electrical" and "instrumentation" are read per table: for a
  plant's notifications the department plant, `plant = '65E'` or `plant = '65I'` for plant 65;
  orders have no department plant, so electrical orders are those whose `main_work_center` ends in
  `21`, instrumentation orders `31`; on readings and material costs, and for electrical or instrumentation
  equipment, the discipline `E` or `I` of the location ([reference/keys.md](reference/keys.md#plant)).
- **A count** counts rows. In `IK17_KG` a row is one reading of a point, so "how many points" counts
  readings; give the count of distinct points beside it when the two differ.
- **"Not performed"** points are `text_code IN ('Not performed', 'Not checked')`.
- **A percentage** is `100.0 * part / whole`, rounded to 2 decimals; say what the whole is.
- **A cost** is the net sum of `cost`: returns are negative rows and stay in the sum. Give the
  booked and returned parts beside it when there are returns.
- **A completed order** has `TECO` in `system_status`, or `CMPL` without `NCMP`; a closed order is
  the same. `CMPL` with `NCMP` is closed without execution, neither closed nor completed; report it
  apart when it matters ([reference/codes.md](reference/codes.md), under the system status).
- **A completed notification** has `NOCO` as the first code of `notification_system_status`
  (Sergey, 2026-10-13).
- **A status** field may hold several codes. In every status field, system or user, the first
  code from the left is the current status and the rest are history: "orders released" reads the
  first code, "orders delayed for lack of people" looks for `MSCP` anywhere
  ([reference/codes.md](reference/codes.md), under the system status). When the system status and
  the user status disagree about the current state, the system status wins
  ([reference/codes.md](reference/codes.md), under the user status). When
  one notification number has more than one row, report every row with its
  notification system status, user status and order system status. Decode every code you report with [reference/codes.md](reference/codes.md).

## When the question can be read two ways

Take the reading the defaults give, answer it, and add one line: the other reading and the number
its query returns. Do not ask the user to choose; answer, then show the alternative.

## When the data cannot answer

Say what is missing — no such column, a code [reference/codes.md](reference/codes.md) marks unknown,
a period outside the data's dates, an identifier with no row — and give no number for it. A result
of zero rows is an answer ("0"), but say which filter left nothing.

What is being executed right now is not in this data: it needs the order operations of SAP
transaction IW37N, which are not among the four tables (Sergey, 2026-10-13). `EXE` as the first
user-status code means the work is cleared for execution, not that it is being executed
([reference/codes.md](reference/codes.md), under the user status).
