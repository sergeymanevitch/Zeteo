---
layer: L4
type: record
---

# Results — what the folder changed

**The headline: by the answer key as committed, the folder tied no folder — 6 of 15 against 6 of
15, in every one of four rounds — because the key is itself wrong three times.** Scored against
what the data says, no folder got 9 of 15 and the folder 12, then 14 in its last round. Every point
of that lead came from a domain meaning the questions' author supplied, and one of them (Q3) was
written into the folder after the runs and the key had been seen. The folder made the answers
about a third faster and **15–21 % dearer**, not cheaper as its first three rounds seemed to show.
Most of what made no folder good was spent before the control ran: on cleaning the data both arms
got.

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

The control ran once. The treatment ran four times, because the folder changed three times after a
treatment run (§ What changed in the folder because of the runs). Every session that ran is
committed, raw; none was repeated or dropped.

| Arm | Ran on | Summary and transcripts |
| --- | --- | --- |
| control | the four Parquet files alone | [control/control.md](control/control.md) |
| treatment, round 1 | folder at `679d0fb` | [treatment/01_folder-679d0fb/](treatment/01_folder-679d0fb/treatment.md) |
| treatment, round 2 | folder at `b35316d`: the plant rule changed | [treatment/02_plant-rule/](treatment/02_plant-rule/treatment.md) |
| treatment, round 3 | folder at `aa8e82a`: every query through `query.py` | [treatment/03_query-py/](treatment/03_query-py/treatment.md) |
| treatment, round 4 | folder at `d85d39b`: a date picked by what the question asks | [treatment/04_date-rule/](treatment/04_date-rule/treatment.md) |

Sergey launched the control and rounds 1–3 from his terminal. Round 4 was launched by the agent
that built the folder, on his word, with `run/ask.sh` under `env -i` (only `HOME`, `USER`,
`LOGNAME`, `SHELL`, `TERM`, `LANG`, `PATH` and `TMPDIR` passed), so that no setting of the agent's
own Claude Code session reached the runs.

The order is in the git history (times Israel):

| Commit | Time | What |
| --- | --- | --- |
| `fe7a35b` | 10-12 21:06 | the questions and their expected answers |
| `24ae59b` | 10-12 22:26 | the data and the run kit |
| `df4bae6` | 10-12 23:04 | the control run (sessions 22:52–22:57) |
| `679d0fb` | 10-12 23:05 | the folder |
| `53ccdda` | 10-12 23:11 | treatment round 1 (sessions 23:07–23:10) |
| `b35316d` | 10-12 23:18 | the plant rule changed |
| `790b725` | 10-12 23:32 | treatment round 2 |
| `aa8e82a` | 10-12 23:33 | `query.py` added |
| `4f93111` | 10-12 23:40 | treatment round 3 (sessions 23:36–23:40) |
| `d85d39b` | 10-13 08:49 | dates by what the question asks; a completed order; no future date read as a mistake |
| `2ba053f` | 10-13 09:03 | treatment round 4 (sessions 08:58–09:02) |

## The answer key was wrong three times

The expected answers were written by the data's owner before any run, read off the Excel exports
by hand. Checked against the data afterwards, three of five do not hold. They stay in
[`questions.md`](questions.md) as committed; every arm is scored against them, and against what
the data says.

| # | Key | What the data says | Why the key differs |
| --- | --- | --- | --- |
| 2 | 171 | 170 | the hand count included the Excel header row |
| 3 | 22.26 | 22.19: 231 of 1,041 on the reading the key used (`plant = '64'`, `required_start_date`) | the hand count included the Excel header row in both counts: 232 of 1,042 |
| 4 | 9869.97 | 9119.14 for May 2026 | 9869.97 is the sum for **June** 2026 |

## Question by question

Each cell is Haiku · Sonnet · Opus; ×3 means all three models gave the same.

| # | Key | Data | Control | Round 1 | Round 2 | Round 3 | Round 4 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 3 | 3 | 3 ×3 | 3 ×3 | 3 ×3 | 3 ×3 | 3 ×3 |
| 2 | 171 | 170 | 71 · 71 · 60 | 170 ×3 | 170 ×3 | 170 ×3 | **119** · 170 · 170 |
| 3 | 22.26 | 22.19 | 19.98 ×3 | 19.79 ×3 | 19.98 ×3 | 19.98 ×3 | 22.19 ×3 |
| 4 | 9869.97 | 9119.14 | 9119.14 ×3 | 9119.14 ×3 | 9119.14 ×3 | 9119.14 ×3 | 9119.14 ×3 |
| 5 | REJC | REJC | REJC ×3 | REJC ×3 | REJC ×3 | REJC ×3 | REJC ×3 |

| Scored | Control | Round 1 | Round 2 | Round 3 | Round 4 |
| --- | --- | --- | --- | --- | --- |
| by the key as committed | 6 / 15 | 6 / 15 | 6 / 15 | 6 / 15 | 6 / 15 |
| by what the data says | 9 / 15 | 12 / 15 | 12 / 15 | 12 / 15 | 14 / 15 |

| # | Verdict |
| --- | --- |
| 1 | **tie** — every arm right in every round |
| 2 | **folder wins** on a meaning its author supplied before any run; round 4's Haiku slipped |
| 3 | **folder lost in round 1, tied in rounds 2–3, won in round 4** — each change written after seeing the answers |
| 4 | **tie** — every arm right for May; the key holds June |
| 5 | **tie** on the value; the folder decoded it, the control guessed |

### 1 — orders by priority, plant, work center, month

Both arms found `ZW38_KG`, filtered on `created_on`, and answered 3 on every model in every round.
The folder added nothing to the number. It made the answer faster: 8–14 s with the folder (Opus 21 s
in round 2) against 14–29 s without. In round 4 every model also gave the other reading the new
date rule names: 6 orders if "in May" means scheduled to start in May.

### 2 — points not performed

The control read "not performed" literally — only `text_code = 'Not performed'`, 71 readings (Opus
gave 60 distinct points, with 71 as the alternative). The folder's rule counts `Not performed` and
`Not checked` together, which is what the plant means by the phrase, and counts readings: rounds
1–3 answered 170 on every model, with 119 distinct points beside it.

**Round 4's Haiku broke the rule.** It led with "119 measuring points", 170 readings second, where
[rules.md](rules.md) says a count of points counts readings and gives distinct points beside it.
The rule did not change between rounds 3 and 4; this is the variance one run per cell cannot
measure, and it is scored as a miss. Sonnet and Opus answered 170.

This is the folder's one win that no rule change made, and its source must be stated: the
definition came from Sergey, the owner of the data and the author of the questions, on 2026-10-12,
after the questions were committed and before any run. It is his meaning of the phrase, the same
one his key used. A stranger who asks about points "not performed" gets the same reading — whether
that is the reading the stranger meant is what the folder asserts and cannot prove.

### 3 — share of priority-3 notifications in a plant and month

The question names a month and no event. Three things happened to it, each after a treatment run.

- **Round 1 lost.** The control took `plant = '64'` and `created_on`: 19.98 % (240 of 1,201). The
  folder's first plant rule also counted `64E` and `64I` (the electrical and instrumentation
  departments booked under plant 64) and fell back to the functional location when `plant` was
  empty: 19.79 % (244 of 1,233) on all three models — further from the key than no folder.
- **Rounds 2–3 tied.** Sergey read round 1's answers and decided that a question about plant 64
  means the notifications whose plant is 64 (`b35316d`). The folder then gave 19.98 %, the
  control's number.
- **Round 4 won.** Sergey then set the default date for notifications to `required_start_date`, the
  day the work is required, by which the plant plans it (`d85d39b`): 22.19 % (231 of 1,041) on
  every model, the data's answer on the key's own reading. Every model gave 19.98 % (opened in
  September) as the other reading.

**This win was written after the runs and the key were seen.** Earlier drafts of this file said
that changing the default date would be the folder built to pass the question, and that it was not
done. It was done, on 2026-10-13, as a domain decision of the data's owner: he states that the
plant reads notifications in a month by `required_start_date`, and opened notifications by
`created_on`. Both are now in [reference/keys.md](reference/keys.md#dates) with every other date of
every table. The decision may be right; this test cannot show it, because the only question that
exercises it is the one it was fixed on.

### 4 — maintenance cost of one location in a month

Both arms summed `ZK22_KG.cost` for May 2026 and gave 9119.14 on every model in every round, net
of a returned line. The key holds June's sum. The control was right without the folder; the folder
changed nothing but the wording ("material cost", booked and returned parts beside the net). Opus
was dearer with the folder on this question in every round (0.169–0.175 USD against 0.135) and
slower in round 1 (21 s against 20).

### 5 — a notification's user status

Both arms returned `REJC` on every model. The control hedged its meaning — Haiku "usually means
'rejected', but I haven't checked", Sonnet "probably 'Rejected'", Opus "most likely means
Rejected"; the treatment, from the folder's code list in
[reference/codes.md](reference/codes.md), as "rejected" without hedging, in every round. Same
value, firmer reading.

## Speed, tokens and cost

Totals over the five questions, per model:

| Model | | Control | Round 1 | Round 2 | Round 3 | Round 4 |
| --- | --- | --- | --- | --- | --- | --- |
| Haiku | seconds | 79 | 46 | 45 | 46 | 48 |
| | tool calls | 24 | 23 | 26 | 23 | 21 |
| | tokens out | 10,789 | 7,896 | 7,567 | 7,128 | 7,198 |
| | cost USD | 0.0242 | 0.0258 | 0.0259 | 0.0242 | 0.0293 |
| Sonnet | seconds | 75 | 51 | 49 | 61 | 55 |
| | tool calls | 19 | 28 | 28 | 28 | 27 |
| | tokens out | 5,504 | 5,197 | 4,670 | 5,050 | 4,821 |
| | cost USD | 0.3860 | 0.3818 | 0.3831 | 0.3875 | 0.4607 |
| Opus | seconds | 107 | 74 | 82 | 73 | 74 |
| | tool calls | 19 | 15 | 15 | 15 | 15 |
| | tokens out | 7,404 | 5,937 | 5,991 | 5,699 | 6,104 |
| | cost USD | 0.8190 | 0.7718 | 0.7908 | 0.7815 | 0.9446 |
| All | seconds | 261 | 171 | 176 | 180 | 177 |
| | cost USD | 1.2292 | 1.1794 | 1.1998 | 1.1932 | 1.4346 |

- **Faster: yes, about a third**, on every model in every round (all fifteen sessions: 261 s
  without the folder, 171–180 s with it).
- **Cheaper: no — the folder costs 15–21 % more.** Rounds 1–3 seemed to cost the same as the
  control (1.18–1.20 USD against 1.23). Round 4 showed why: the first question of each model pays to
  write Claude Code's prompt cache when it is cold. The control met a cold cache (Sonnet and Opus
  wrote 27–28 thousand cache tokens on Q1); rounds 1–3 ran minutes after it and after each other
  and met a warm one (14–15 thousand); round 4 ran nine hours later and met a cold one again
  (31–35 thousand), and cost 1.43 USD. Over questions 2–5, where every arm met a warm cache, the
  control cost 0.81 USD and the folder 0.93–0.97: reading the folder costs more than exploring the
  files did.
- **Fewer tool calls: not for Sonnet.** Sonnet made 27–28 tool calls with the folder against 19
  without, because it read the reference files one by one. Opus made fewer (15 against 19); Haiku
  about the same (21–26 against 24).
- **Per question the folder was three times slower.** Sonnet on Q2 in round 3 (19 s against 15)
  and on Q3 in round 4 (16 s against 14); Opus on Q4 in round 1 (21 s against 20).

Seconds run from the prompt to the last reply in the transcript, not including Claude Code's
start-up. Cost is the `totalCostUSD` Claude Code recorded.

## How they worked

- **Control:** 13 of 15 sessions never called DuckDB — they listed the folder, loaded the Parquet
  files with pandas (Haiku's Q4 with pyarrow) and explored the columns; the two that used the DuckDB
  CLI were the status lookups of Q5 (Haiku, Opus). No control answer shows its query.
- **Treatment:** all 60 sessions read [`identity.md`](identity.md) and [`rules.md`](rules.md) first
  (by `Read` or `cat`), then the reference files their question needed, then queried. Every
  treatment answer states its criteria and its SQL. Rounds 1 and 2 queried with DuckDB; rounds 3
  and 4 queried only through [`query.py`](query.py), every session.

## What changed in the folder because of the runs

- **Because of the control: nothing.** The folder was written before the control's answers were
  read. Between the control run and the folder's commit it changed only from Sergey's answers to
  questions asked before the control ran: plants compared as numbers (`010` is plant 10), the
  discipline letters, a future date read as an entry mistake (withdrawn in `d85d39b`, below),
  duplicate notifications reported row by row, `cost` the value of the whole line.
- **Because of round 1's Q3 (`b35316d`):** the plant rule. A plant is the `plant` column alone,
  compared as a number; `64E`, `64I` and empty plants are left out. [rules.md](rules.md),
  [reference/keys.md](reference/keys.md), [reference/ziw28.md](reference/ziw28.md) and two
  examples followed. Effect: Q3 19.79 → 19.98, the control's number. Nothing else moved.
- **After round 2 (`aa8e82a`), not because of an answer:** [query.py](query.py), one read-only door
  to the four tables, at Sergey's request: it loads the Parquet files as tables named after them,
  closes DuckDB to the file system and runs one statement that reads. Effect on the answers:
  none — round 3 gave round 2's numbers on every cell.
- **After round 3 and the key's check (`d85d39b`):** the dates, from Sergey on 2026-10-13. Every
  date of every table is mapped to what a question asks about — opened, due, planned, released,
  started, closed ([reference/keys.md § Dates](reference/keys.md#dates)); notifications in a period
  with no event named default to `required_start_date`, orders to `created_on`. In the same commit:
  a completed order (`TECO`, or `CMPL` without `NCMP`); a date later than today no longer read as an
  entry mistake, since these exports cannot tell a mistyped date from a plan up to five years
  ahead; "done on time" declared unanswerable, since no column holds when a notification's work was
  done; three examples added. Effect: Q3 19.98 → 22.19; Q1 gained an other reading (6, scheduled);
  nothing else moved.

## What this says, and what it does not

- **The folder did not beat no folder on the key.** 6 against 6, every round. The key is wrong on
  three questions, so it cannot rank the arms; by the data the folder leads 12 or 14 to 9.
- **Every point of the lead is a domain meaning from the questions' author.** "Not performed" (Q2)
  was in the folder before any run. The plant of Q3 and the date of Q3 were written after runs that
  showed what they would change. `REJC` (Q5) is decoded with confidence but scores the same.
- **Most of the advantage was spent before the control ran.** The Parquet files the control got are
  already cleaned: Hebrew values translated, misspelt headers corrected, dates typed. That work was
  done for both arms, and it is likely why the control did so well. The raw exports, in Hebrew with
  headers such as `quantety` and `schedualed_end_date`, were never tested.
- **A folder can move an answer the wrong way** (Q3, round 1) when a rule is written as a
  definition and the definition is wrong for the question.
- **A folder does not remove variance.** Rounds 1–3 gave the same number on all three models on
  every question; round 4's Haiku then broke a rule that had not changed (Q2).
- **The folder buys speed and pays for it.** A third faster, a sixth to a fifth dearer.

## Known flaws in this comparison

- The message of commit `df4bae6` says no folder file existed in the repository during the
  control. The folder files were on disk, uncommitted, while it ran. They were never in the
  control's run folder, which `run/make_arm.sh control` fills with `data/*.parquet` alone. The
  commit is pushed and was not rewritten.
- The questions' author also supplied the folder's domain meanings (Q2's definition, the plant
  and the date of Q3).
- The folder changed three times between treatment rounds. Two of the changes moved Q3 and were
  written after seeing it: round 4's 15th point was bought by a rule written after the answers and
  the key were known.
- The data was cleaned for both arms (translation, header names, types). The raw exports are not
  published and were never tested.
- One run per cell per round; both arms ran on one machine with the same user-level Claude Code
  configuration, not a clean profile. The system Python there holds the `duckdb` package (0.9.2)
  and the DuckDB CLI 1.5.6 is installed; both arms had both.
- The prompt cache was warm for rounds 1–3 and cold for the control and round 4 (§ Speed, tokens
  and cost); totals over five questions compare unlike things, and the questions 2–5 figures are
  the fair ones.
- Round 4 was launched by the build agent from a cleaned environment, the other runs by Sergey
  from his terminal.
- Every question was written by the data's owner. Whether the advantage holds on a question he
  did not write is not tested here.
