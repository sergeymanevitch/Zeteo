---
layer: L4
type: record
---

# Results — what the folder changed

**The headline: by the answer key as committed, the folder tied no folder, 6 of 15 against 6 of
15, in every round.** By what the data says, the folder won one question of five (Q2), and that
one win comes from a definition the questions' own author supplied. Most of the folder's advantage
was spent before the control ran, on cleaning the data both arms got.

## The setup

Two arms, one variable. The same five questions of [questions.md](questions.md), in the same order,
each in its own fresh headless Claude Code session, on Haiku, Sonnet and Opus (`claude-haiku-5-5`,
`claude-sonnet-5-5`, `claude-opus-5-5`; Claude Code 2.1.296). The **control** ran in a folder that
held the four Parquet files of [data/](data/CONTEXT.md) and nothing else. The **treatment** ran in a
folder that held the same files plus the Zeteo folder ([CLAUDE.md](CLAUDE.md),
[identity.md](identity.md), [rules.md](rules.md), [examples.md](examples.md),
[reference/](reference/CONTEXT.md), and from round 3 [query.py](query.py)), which Claude Code loads
through `CLAUDE.md`. The prompt was the question as written, nothing added. How to repeat both
arms: [run/CONTEXT.md](run/CONTEXT.md).

The control ran once. The treatment ran three times, because the folder changed twice after a
treatment run (§ What changed in the folder because of the runs). Every session that ran is
committed, raw; none was repeated or dropped.

| Arm | Ran on | Summary and transcripts |
| --- | --- | --- |
| control | the four Parquet files alone | [control/control.md](control/control.md) |
| treatment, round 1 | folder at `679d0fb` | [treatment/01_folder-679d0fb/](treatment/01_folder-679d0fb/treatment.md) |
| treatment, round 2 | folder at `b35316d`: the plant rule changed | [treatment/02_plant-rule/](treatment/02_plant-rule/treatment.md) |
| treatment, round 3 | folder at `aa8e82a`: every query through `query.py` | [treatment/03_query-py/](treatment/03_query-py/treatment.md) |

The order is in the git history (times Israel, 2026-10-12):

| Commit | Time | What |
| --- | --- | --- |
| `fe7a35b` | 21:06 | the questions and their expected answers |
| `24ae59b` | 22:26 | the data and the run kit |
| `df4bae6` | 23:04 | the control run (sessions 22:52–22:57) |
| `679d0fb` | 23:05 | the folder |
| `53ccdda` | 23:11 | treatment round 1 (sessions 23:07–23:10) |
| `b35316d` | 23:18 | the plant rule changed |
| `790b725` | 23:32 | treatment round 2 |
| `aa8e82a` | 23:33 | `query.py` added |
| `4f93111` | 23:40 | treatment round 3 (sessions 23:36–23:40) |

## The answer key was wrong three times

The expected answers were written by the data's owner before any run, read off the Excel exports
by hand. Checked against the data afterwards, three of five do not hold. They stay in
[`questions.md`](questions.md) as committed; every arm is scored against them, and against what the data says.

| # | Key | What the data says | Why the key differs |
| --- | --- | --- | --- |
| 2 | 171 | 170 | the hand count included the Excel header row |
| 3 | 22.26 | 22.19 on the reading the key used (`required_start_date`, `plant = '64'`) | the residual 0.07 is unexplained |
| 4 | 9869.97 | 9119.14 for May 2026 | 9869.97 is the sum for **June** 2026 |

## Question by question

Each cell is Haiku · Sonnet · Opus; ×3 means all three models gave the same.

| # | Key | Control | Round 1 | Round 2 | Round 3 | Verdict |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 3 | 3 ×3 | 3 ×3 | 3 ×3 | 3 ×3 | **tie** — both right |
| 2 | 171 | 71 · 71 · 60 | 170 ×3 | 170 ×3 | 170 ×3 | **folder wins** on meaning; both miss the key |
| 3 | 22.26 | 19.98 ×3 | 19.79 ×3 | 19.98 ×3 | 19.98 ×3 | **folder lost in round 1**, tied after a rule change; neither arm matches the key |
| 4 | 9869.97 | 9119.14 ×3 | 9119.14 ×3 | 9119.14 ×3 | 9119.14 ×3 | **tie** — both right for May, both wrong by the key |
| 5 | REJC | REJC ×3 | REJC ×3 | REJC ×3 | REJC ×3 | **tie** on the value; the folder decoded it, the control guessed |

| Scored | Control | Round 1 | Round 2 | Round 3 |
| --- | --- | --- | --- | --- |
| by the key as committed | 6 / 15 | 6 / 15 | 6 / 15 | 6 / 15 |
| by what the data says (Q2 = 170, Q4 = 9119.14, Q3 wrong for all) | 9 / 15 | 12 / 15 | 12 / 15 | 12 / 15 |

The whole difference is question 2.

### 1 — orders by priority, plant, work center, month

Both arms found `ZW38_KG`, filtered on `created_on`, and answered 3 on every model in every round.
The folder added nothing to the number. It made the answer faster: 8–14 s with the folder (Opus 21 s
in round 2) against 14–29 s without.

### 2 — points not performed

The control read "not performed" literally — only `text_code = 'Not performed'`, 71 readings (Opus
gave 60 distinct points, with 71 as the alternative). The folder's rule counts `Not performed` and
`Not checked` together, which is what the plant means by the phrase: every model in every round
answered 170 and gave 119 distinct points beside it; eight of the nine named 71 as the other
reading (round 3's Haiku did not).

This is the folder's one real win, and its source must be stated: the rule came from Sergey, the
owner of the data and the author of the questions, on 2026-10-12, after the questions were
committed and before any run. It is his meaning of the phrase, the same one his key used. A
stranger who asks about points "not performed" gets the same reading — whether that is the reading
the stranger meant is what the folder asserts and cannot prove.

### 3 — share of priority-3 notifications in a plant and month

**Round 1 lost.** The control took `plant = '64'` and `created_on`: 19.98 % (240 of 1,201). The
folder's first plant rule also counted `64E` and `64I` (the electrical and instrumentation
departments booked under plant 64) and fell back to the functional location when `plant` was empty:
19.79 % (244 of 1,233) on all three models — further from the key than no folder.

Sergey read round 1's answers and decided that a question about plant 64 means the notifications
whose plant is 64; the department plants and empty plants are left out (`b35316d`). Rounds 2 and 3
then gave 19.98 % on every model, the control's number. **The loss was reversed by a rule written
after seeing it.** That is the folder fitted to an answer, and it is stated here as such: it moved
the folder to what no folder already did, not to the key.

Neither arm reaches 22.26. The key's own reading was `required_start_date` with `plant = '64'`
(22.19 %); the folder's default date is `created_on`, Sergey's choice made knowing the key used
another date. Changing the default date would have moved the treatment toward the key, and been
the folder built to pass the question. It was not done. From round 2 every model also offered a
second reading — 20.34 % if the 21 notifications with no priority are left out of the whole.

### 4 — maintenance cost of one location in a month

Both arms summed `ZK22_KG.cost` for May 2026 and gave 9119.14 on every model in every round, net
of a returned line. The key holds June's sum. The control was right without the folder; the folder
changed nothing but the wording ("material cost", booked and returned parts beside the net). Opus
was dearer with the folder on this question in every round (0.169–0.171 USD against 0.135) and
slower in round 1 (21 s against 20).

### 5 — a notification's user status

Both arms returned `REJC` on every model. The control hedged its meaning — Haiku "usually means
'rejected', but I haven't checked", Sonnet "probably 'Rejected'", Opus "most likely means
Rejected"; the treatment, from the folder's code list in
[reference/codes.md](reference/codes.md), as "rejected" without hedging, in every round. Same
value, firmer reading.

## Speed, tokens and cost

Totals over the five questions, per model:

| Model | | Control | Round 1 | Round 2 | Round 3 |
| --- | --- | --- | --- | --- | --- |
| Haiku | seconds | 79 | 46 | 45 | 46 |
| | tool calls | 24 | 23 | 26 | 23 |
| | tokens out | 10,789 | 7,896 | 7,567 | 7,128 |
| | cost USD | 0.0242 | 0.0258 | 0.0259 | 0.0242 |
| Sonnet | seconds | 75 | 51 | 49 | 61 |
| | tool calls | 19 | 28 | 28 | 28 |
| | tokens out | 5,504 | 5,197 | 4,670 | 5,050 |
| | cost USD | 0.3860 | 0.3818 | 0.3831 | 0.3875 |
| Opus | seconds | 107 | 74 | 82 | 73 |
| | tool calls | 19 | 15 | 15 | 15 |
| | tokens out | 7,404 | 5,937 | 5,991 | 5,699 |
| | cost USD | 0.8190 | 0.7718 | 0.7908 | 0.7815 |

- **Faster: yes, about a third**, on every model in every round (all fifteen sessions: 261 s
  without the folder, 171–180 s with it).
- **Cheaper: no.** Cost barely moved (1.229 USD without, 1.179–1.200 with). Reading the folder costs
  about what exploring the files cost. Haiku cost more with the folder in rounds 1 and 2 and the
  same in round 3; Sonnet's round 3 cost more than its control.
- **Fewer tool calls: not for Sonnet.** Sonnet made 28 tool calls with the folder against 19
  without, because it read the reference files one by one. Opus made fewer (15 against 19); Haiku
  about the same (23–26 against 24).
- **Per question the folder was twice slower.** Sonnet on Q2 in round 3 took 19 s against 15 s
  without; Opus on Q4 in round 1, 21 s against 20 (above). Without the folder, Sonnet's and Opus's first
  question was their dearest (Opus 0.283 USD on Q1 against 0.154–0.162 with the folder).

Seconds run from the prompt to the last reply in the transcript, not including Claude Code's
start-up. Cost is the `totalCostUSD` Claude Code recorded.

## How they worked

- **Control:** 13 of 15 sessions never called DuckDB — they listed the folder, loaded the Parquet
  files with pandas (Haiku's Q4 with pyarrow) and explored the columns; the two that used the DuckDB
  CLI were the status lookups of Q5 (Haiku, Opus). No control answer shows its query.
- **Treatment:** all 45 sessions read [`identity.md`](identity.md) and [`rules.md`](rules.md) first (by `Read` or `cat`), then
  the reference files their question needed, then queried. Every treatment answer states its
  criteria and its SQL. Rounds 1 and 2 queried with DuckDB; round 3 queried only through
  [`query.py`](query.py), every session.

## What changed in the folder because of the runs

- **Because of the control: nothing.** The folder was written before the control's answers were
  read. Between the control run and the folder's commit it changed only from Sergey's answers to
  questions asked before the control ran: plants compared as numbers (`010` is plant 10), the
  discipline letters, a future date read as an entry mistake, duplicate notifications reported row
  by row, `cost` the value of the whole line.
- **Because of round 1's Q3 (`b35316d`):** the plant rule. A plant is the `plant` column alone,
  compared as a number; `64E`, `64I` and empty plants are left out. [rules.md](rules.md),
  [reference/keys.md](reference/keys.md), [reference/ziw28.md](reference/ziw28.md) and two
  examples followed. Effect: Q3 19.79 → 19.98, the control's number. Nothing else moved.
- **After round 2 (`aa8e82a`), not because of an answer:** [query.py](query.py), one read-only door
  to the four tables, at Sergey's request: it loads the Parquet files as tables named after them,
  closes DuckDB to the file system and runs one statement that reads. Effect on the answers:
  none — round 3 gave round 2's numbers on every cell.

## What this says, and what it does not

- **The folder did not beat no folder on the key.** 6 against 6, every round. On these five
  questions, with this data, a capable model without the folder already gets right whatever the
  columns say.
- **Most of the advantage was spent before the control ran.** The Parquet files the control got are
  already cleaned: Hebrew values translated, misspelt headers corrected, dates typed. That work was
  done for both arms, and it is likely why the control did so well. The raw exports, in Hebrew with
  headers such as `quantety` and `schedualed_end_date`, were never tested.
- **The folder wins where an answer depends on a word, not a column.** "Not performed" (Q2) and
  `REJC` (Q5) are domain meanings no column states. That is the folder's job, and the only place it
  changed a number.
- **A folder can move an answer the wrong way** (Q3, round 1) when a rule is written as a
  definition and the definition is wrong for the question. The fix was a new definition, written
  after seeing the miss.
- **The folder made the models agree.** With the folder all three models gave the same number on
  every question in every round; without it they differed on Q2.
- **One run per cell per round.** Variance between runs of one cell is not measured; three rounds
  of the treatment on nearly the same folder gave the same answers wherever the rule did not change.

## Known flaws in this comparison

- The message of commit `df4bae6` says no folder file existed in the repository during the
  control. The folder files were on disk, uncommitted, while it ran. They were never in the
  control's run folder, which `run/make_arm.sh control` fills with `data/*.parquet` alone. The
  commit is pushed and was not rewritten.
- The questions' author also supplied the folder's domain meanings (Q2's definition, the plant
  rule of Q3).
- The data was cleaned for both arms (translation, header names, types). The raw exports are not
  published and were never tested.
- The folder changed twice between treatment rounds; round 2's Q3 result was bought by a rule
  written after round 1's miss.
- One run per cell per round; both arms ran on one machine with the same user-level Claude Code
  configuration, not a clean profile. The system Python there holds the `duckdb` package (0.9.2)
  and the DuckDB CLI 1.5.6 is installed; both arms had both.
- Every question was written by the data's owner. Whether the advantage holds on a question he
  did not write is not tested here.
