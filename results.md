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

**On thirty questions its author did not write, the folder got 80 of 90 answers right and no folder
49** (§ Thirty questions the author did not write) — 82 against 49 as first graded, before the owner
changed A3's expected answer after the runs. On the eleven questions that need no reading
of the data's meaning, every model in both arms was right. The lead is the owner's meanings — which
date a month means, when a notification is completed, which status is current — and one honest
habit: asked the two questions written to be unanswerable (B9, B10), no folder made a number up in
five answers of six, the folder in one. On A3, which the owner's reading after the runs made
unanswerable, every answer of both arms gave a number.

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
| control, unseen questions | the four Parquet files alone | [control/unseen/](control/unseen/control.md) |
| treatment, unseen questions | folder at `236cc9f` | [treatment/unseen/](treatment/unseen/treatment.md) |

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
| `4866ad0` | 10-13 12:25 | thirty questions the author did not write |
| `929a58d` | 10-13 12:34 | their expected answers |
| `1a1bfe6` | 10-13 13:59 | both arms on the thirty questions (sessions 12:35–13:44) |

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

## Thirty questions the author did not write

The five questions above are the data owner's. To see whether the folder's lead holds on questions
he did not write, a separate Claude Opus session wrote thirty ([questions-unseen.md](questions-unseen.md)).
It could query the data and read the column names; it was told not to open the folder, the
questions above, their runs or these results. Ten test the choice points the folder handles (A),
ten the gaps found on 2026-10-13 (B), ten its own choice (C). The questions were committed first,
then the expected answers, then both arms were asked, each question in its own fresh session, on
the three models, launched by a subagent under `env -i`. The treatment ran on the folder at
`236cc9f` — round 4's folder plus the code meanings and the three decisions recorded under § What
changed. All 180 sessions are committed, none repeated.

**The key leans toward the folder.** The expected answers were computed by the folder's author, by
query, with the folder's definitions — the meanings the owner gave. One answer, A9, was settled by
the owner after both arms had run: "electrical notifications of plant 65" is the electrical
department plant `65E`, 171 (his own Excel count read 172, the header row counted again). The
folder had read it as discipline `E` on plant 65 and lost it. A second, A3, was changed by the owner
after both arms had run: what is being executed right now cannot be answered from these tables — it
needs the order operations of SAP transaction IW37N — and `EXE` as the first user-status code means
cleared for execution, not being executed. The key had read 5 (`EXE` the current user status). Both
grades are given below: by the key as it stands, and as first graded, before A3's change (A9
already at 171).

Graded by the build agent from the final replies: **✓** the main answer is the key's; **≈** the main
answer is the other reading the key gives beside it (almost always another date); **✗** neither.

| | Haiku | Sonnet | Opus | ✓ | ✓ or ≈ |
| --- | --- | --- | --- | --- | --- |
| no folder | 15 ✓ · 8 ≈ · 7 ✗ | 16 · 10 · 4 | 18 · 8 · 4 | **49 / 90** | 75 / 90 |
| folder | 26 · 1 · 3 | 26 · 2 · 2 | 28 · 1 · 1 | **80 / 90** | 84 / 90 |
| no folder, A3 as first graded | 15 · 9 · 6 | 16 · 11 · 3 | 18 · 8 · 4 | 49 / 90 | 77 / 90 |
| folder, A3 as first graded | 27 · 1 · 2 | 27 · 2 · 1 | 28 · 1 · 1 | 82 / 90 | 86 / 90 |

| # | Tests | No folder H · S · O | Folder H · S · O | What decided it |
| --- | --- | --- | --- | --- |
| A1 | released date | ✓✓✓ | ✓✓✓ | |
| A2 | department plant `64E` | ✓✓✓ | ≈✓✓ | folder Haiku took the default date though the question says "raise" |
| A3 | being executed now — cannot be answered | ✗✗✗ (was ≈≈✗) | ✗✗✗ (was ✓✓✗) | the owner's reading after the runs: it needs IW37N. Every answer gave a number: no folder `EXE` anywhere (130; Opus 20, in process too), folder Haiku and Sonnet `EXE` first (5, the key as first written), folder Opus `NOPR` (251) |
| A4 | rows or distinct points | ≈≈✓ | ✓✓✓ | no folder Haiku and Sonnet counted only points with a measured value (8) |
| A5 | a completed order | ✓≈✓ | ✓✓✓ | `CMPL` without `NCMP` counts |
| A6 | out of limits | ✓✓≈ | ✓✓✓ | no folder Opus dropped duplicates and swapped limits (132) |
| A7 | cost with returns | ✓✓✓ | ✓✓✓ | |
| A8 | percentage | ≈≈≈ | ✓✓✓ | default date |
| A9 | "electrical" | ✗✓✓ | ✗✗≈ | the owner's reading, `65E`, given after the runs |
| A10 | readings to cost by order | ✓✓✓ | ✓✓✓ | |
| B1 | completed notification | ≈≈≈ | ✓✓✓ | default date |
| B2 | is one notification finished | ✗✗✓ | ✓✓✓ | no folder Haiku and Sonnet looked for a Claude Code notification, not the data's |
| B3 | duration, average | ✓✓✓ | ✓✓✓ | |
| B4 | duration, median | ✓≈✓ | ✓✓✓ | a closed order is a completed order (`TECO`, or `CMPL` without `NCMP`); the folder said `closed_on` only on `TECO`, corrected after the runs |
| B5 | last month | ✓✓✓ | ✓✓✓ | |
| B6 | this year against last | ≈≈≈ | ✓≈✓ | by opened date up, by required date down |
| B7 | still open | ✓✓✓ | ✓✓✓ | |
| B8 | outstanding now | ✗✗✗ | ✓≈✓ | no folder looked for `NOCO` anywhere (372, not 382) |
| B9 | on time — unanswerable | ✗✗✗ | ✗✓✓ | every no-folder model, and folder Haiku, gave a percentage |
| B10 | labour cost — not in the data | ✗✓✗ | ✓✓✓ | no folder Haiku and Opus derived "labour" from an hourly rate (≈23,790 and ≈€24,195) |
| C1 | top 5 locations | ≈≈≈ | ✓✓✓ | default date |
| C2 | top work center | ✓✓✓ | ✓✓✓ | |
| C3 | by month | ≈≈≈ | ✓✓✓ | default date |
| C4 | by type | ≈≈≈ | ✓✓✓ | default date |
| C5 | plants compared | ✓✓✓ | ✓✓✓ | |
| C6 | one location, two tables | ≈≈≈ | ✓✓✓ | default date |
| C7 | top location by cost | ✓✓✓ | ✓✓✓ | |
| C8 | order types | ✗✓✓ | ✓✓✓ | no folder Haiku read "open" as still open |
| C9 | highest temperature | ✓✓✓ | ✓✓✓ | |
| C10 | a duplicated notification | ✓✓✓ | ✓✓✓ | |

Totals over thirty questions, seconds / USD, each model's first question on a cold cache in both
arms:

| Model | No folder | Folder |
| --- | --- | --- |
| Haiku | 665 / 0.18 | 390 / 0.19 |
| Sonnet | 505 / 2.15 | 391 / 2.76 |
| Opus | 1,028 / 5.56 | 636 / 5.79 |
| **All** | **2,198 / 7.89** | **1,417 / 8.74** |

The folder was 36 % faster and 11 % dearer — the same shape as on the five questions.

What the thirty show:

- **Plain questions need no folder.** Eleven need no reading of the data's meaning (A1, A7, A10,
  B3, B5, B7, C2, C5, C7, C9, C10); all 66 answers to them are right in both arms.
- **The lead is the owner's meanings.** 21 of no folder's 26 ≈ are the default date alone: it
  read every period by the day a notification was opened, the owner reads it by the day the work
  is required. Counting ≈ as right, the gap narrows to 84 against 75 (86 against 77 as first
  graded).
- **The folder says "cannot" where the data cannot.** On B9 and B10 no folder produced a number in
  five answers of six — an on-time percentage on a date that is only the scheduled one copied, and
  a labour cost reverse-engineered from hourly rates. The folder did so once. On A3, which only
  the owner's reading after the runs made unanswerable, all six answers of both arms gave a number.
- **Where the folder has no rule, it guesses like anyone.** A9 ("electrical") and A3 ("being
  executed") were readings the folder did not fix when it ran, and it lost both: A9 to no folder,
  A3 with every answer of both arms. Both are in the folder now (§ What changed); no round was run
  on them.

Sergey also ran the treatment folder on the thirty questions on another computer, all in one
Claude Opus session, in about four minutes. Only the answers file exists, no transcript, so the
run is not counted; graded the same way it gives 26 ✓, 2 ≈ (B6, C10) and 2 ✗ (A3, A9). The session
named its own choices: "raised", "opened" and "logged" read by the opened date, "electrical" as
electrical locations, "being executed" as the SAP in-process status — the two places it lost.

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
- **After round 4, not because of an answer:** the meanings of every code the folder had marked
  unknown, from Sergey on 2026-10-13 — notification types `R1`–`R6` (the type of order: corrective,
  preventive, root cause, from the technicians' rounds, safety), eight user statuses, seven system
  statuses (`MSCP` not enough people, `NTUP` dates not updated, …), three units, four disciplines,
  order type `1126` (the project department); the SAP-standard codes confirmed as used. With them:
  in every status field the first code is the current status and the rest history;
  `reference_date` is the day the work was reported performed, set again at closing; a location's
  plant is where the equipment stands and `plant` who is in charge; `88`, `80`, `81` and `8100` are
  sub-plants of one plant, for now treated separately. Effect on the five answers: none by query —
  no question reads a system status, a discipline or those plants, and Q5's user status holds one
  code. No round was run on it.
- **After the analysis of what can be asked, not because of an answer:** from Sergey on
  2026-10-13, a completed notification (`NOCO` first), durations in calendar days, relative periods
  read as the user names them and compared like with like. Effect on the five answers: none — no
  question asks about any of them. No round was run on it.
- **After the unseen run, not because of an answer:** fixes from a review of the folder on
  2026-10-13, approved by Sergey. No answer was re-run on them.
  - `closed_on` was stated wrongly in [reference/zw38.md](reference/zw38.md) and
    [reference/keys.md § Dates](reference/keys.md#dates): a closing day on `TECO` orders only, and
    a value running into the future on the 7,748 others. Measured: it holds a real day on three groups
    of orders — `TECO` 62,493, `CMPL` with `NCMP` 5,024, `CMPL` alone 142, none later than
    2026-10-13 — and no closing day on the 2,582 orders that are neither (first code `CRTD` 1,912,
    `REL` 669, `LKD` 1), 320 of them later than 2026-10-13, up to 2027-11-18. Which of the three
    are closed orders is Sergey's reading, below.
  - What it means for B4 (plant 32, orders closed in Q2 2026): 357 orders with `TECO`, median 49
    days — the key and every folder answer; none with `CMPL` alone; 2 with `CMPL` and `NCMP`, which
    make 359 with the same median, 49; the 24 orders that are neither and carry a Q2 `closed_on` stay
    out under every text. By Sergey's reading below, orders closed are completed orders and the 2 are
    closed without execution, so B4's key, 357, is confirmed and does not move; the B4 row above
    stays as recorded.
  - [identity.md](identity.md) said Zeteo turns the criteria into "one SQL query", while
    [rules.md](rules.md) asks for the other reading's number too; it now says one query for each
    reading.
  - [query.py](query.py) pins `duckdb` 1.5.6 instead of any version from 1.0. The recorded runs did
    not record which version `uv` fetched. `duckdb` 1.5.6 needs Python 3.10 or newer, so the script
    now asks for it; `uv` fetches a managed Python when the system one is older.
  - [reference/codes.md](reference/codes.md) said a stray `*` stands in `ZW38_KG.system_status` on
    15 orders; it is on 16, on one of them glued to `NTUP`. Found by [check/](check/CONTEXT.md),
    added with these fixes outside the folder, which recomputes the numbers its registry lists — the
    stated counts of the reference files, the examples, and the `closed_on` paragraph above — and
    fails when a document and the data disagree.

  Effect on the recorded answers: none of the five reads `closed_on` or a stray `*`. Of the thirty,
  B4 does not move, by Sergey's reading of a closed order below; two of the folder's three B9 answers (Sonnet, Opus) cite `closed_on` as a
  closing day on `TECO` orders only, which does not change their verdict, that the question cannot
  be answered. Nothing else reads what changed.
- **After the unseen run, because of A3 and A9:** four decisions of Sergey's on 2026-10-13, given
  after he read both arms' answers. No answer was re-run on them.
  - "Electrical" for a plant is its department plant with the letter `E`: electrical notifications
    of plant 65 are `plant = '65E'`; "electrical" alone is that, not the discipline letter `E` of a
    location ([reference/keys.md § Plant](reference/keys.md#plant), with a pointer in
    [rules.md](rules.md)) — the last part replaced by the next decision, below. A9's key, 171, was
    already this reading.
  - When the system status and the user status disagree about the current state, the system status
    wins ([reference/codes.md](reference/codes.md), under the user status; pointer in
    [rules.md](rules.md)).
  - `EXE` as the first user-status code means the work is cleared for execution, not that it is
    being executed; the code table read "executed", and the worked reading of `PLND,EXE,COMP` said
    "was executed" ([reference/codes.md](reference/codes.md)).
  - What is being executed right now cannot be answered from the four tables: it needs the order
    operations of SAP transaction IW37N, which are not in this data
    ([rules.md § When the data cannot answer](rules.md#when-the-data-cannot-answer)).

  Effect on the recorded answers: none of the five reads "electrical" or `EXE`, and the one that
  reads a status, Q5, asks for the user status by name (its notification's system status is
  `NOCO`), so which status wins does not move it. Of the thirty, A3's key changes to "cannot be answered", in its own commit,
  as A9's key was set after the runs; every A3 answer of both arms gave a number and is regraded ✗
  (§ Thirty questions the author did not write). The folder now states the reading A9's key holds;
  its A9 answers, which read the discipline letter, stay as recorded. No other key moves.
- **After the unseen run, two more readings of Sergey's** on 2026-10-13. No answer was re-run on
  them.
  - A closed order is a completed order — `TECO`, or `CMPL` without `NCMP` — and "orders closed" in
    a period counts only these. `CMPL` with `NCMP` is closed without execution, a category of its
    own, neither closed nor completed, reported apart when it matters. `closed_on` stays a real day
    on all three groups. [reference/codes.md](reference/codes.md), [rules.md](rules.md),
    [reference/zw38.md](reference/zw38.md) and [reference/keys.md § Dates](reference/keys.md#dates)
    follow; the last two had called `CMPL` with `NCMP` closed orders.
  - The discipline `E` of a functional location means electrical equipment. "Electrical" for a
    plant's notifications stays the department plant, `65E` for plant 65; "electrical equipment" is
    the location's discipline `E` ([reference/keys.md](reference/keys.md), with the pointer in
    [rules.md](rules.md)). The earlier sentence that "electrical" alone was never the discipline
    letter is replaced.

  Effect on the recorded answers: none of the five reads a closed order or a discipline. Of the
  thirty, B4's key, 357, is confirmed and does not move: 2 orders of plant 32 with a Q2 `closed_on`
  are closed without execution and stay out. A9 asks for electrical notifications, so its key stays
  `65E`, 171. No other key moves.
- **After the unseen run, one more reading of Sergey's** on 2026-10-13: the last two digits of a
  work center name its trade, `21` electrical and `31` instrumentation (controllers). Orders carry
  no department plant, so a plant's electrical orders are those whose `main_work_center` ends in
  `21`, instrumentation `31`; on notifications "electrical" stays the department plant, and the
  department plants' work centers agree, measured
  ([reference/keys.md § Plant](reference/keys.md#plant), [reference/zw38.md](reference/zw38.md),
  [rules.md](rules.md)). No answer was re-run. Effect on the recorded answers: none — no question of
  the five or the thirty asks for electrical or instrumentation orders, and A9 asks for
  notifications, so its key stays `65E`, 171.
- **After the unseen run, two more decisions of Sergey's** on 2026-10-13. No answer was re-run on them.
  - On readings and material costs "electrical" is the discipline `E` of the functional location,
    its 4th segment: those tables carry neither a department plant nor a work center
    ([reference/keys.md § Plant](reference/keys.md#plant), pointer in [rules.md](rules.md)). The
    folder now reads "electrical" per table: notifications the department plant `<plant>E`, orders
    a work center ending `21`, readings and costs the location's discipline `E`.
  - Step 5 of [rules.md](rules.md) said "Write one SQL query"; it now says one query for each
    reading the answer gives, as [identity.md](identity.md) does.

  Effect on the recorded answers: none — no question of the five or the thirty asks for electrical
  readings or costs, and step 5 changes no number, only how many queries an answer runs.
- **After the unseen run, one more reading of Sergey's** on 2026-10-13: "instrumentation"
  (controllers) is read per table as "electrical" is — notifications the department plant
  `<plant>I` (`65I` for plant 65), orders a work center ending `31` (written before), readings and
  material costs the location's discipline `I`, and instrumentation equipment the discipline `I`
  ([reference/keys.md § Plant](reference/keys.md#plant), pointer in [rules.md](rules.md)). No answer
  was re-run. Effect on the recorded answers: none — no question of the five or the thirty uses the
  word instrumentation or controllers; B8 names work center `6531`, which this reading does not
  touch.

## What this says, and what it does not

- **The folder did not beat no folder on the key.** 6 against 6, every round. The key is wrong on
  three questions, so it cannot rank the arms; by the data the folder leads 12 or 14 to 9.
- **Every point of the lead is a domain meaning from the questions' author.** "Not performed" (Q2)
  was in the folder before any run. The plant of Q3 and the date of Q3 were written after runs that
  showed what they would change. `REJC` (Q5) is decoded with confidence but scores the same.
- **Most of the advantage was spent before the control ran.** The Parquet files the control got are
  already cleaned: values in four columns normalised, misspelt headers corrected, dates typed. That
  work was done for both arms, and it is likely why the control did so well. The raw exports, with
  headers such as `quantety` and `schedualed_end_date`, were never tested.
- **A folder can move an answer the wrong way** (Q3, round 1) when a rule is written as a
  definition and the definition is wrong for the question.
- **A folder does not remove variance.** Rounds 1–3 gave the same number on all three models on
  every question; round 4's Haiku then broke a rule that had not changed (Q2).
- **The folder buys speed and pays for it.** A third faster, a sixth to a fifth dearer.
- **On questions its author did not write, the lead holds:** 80 of 90 against 49 (82 as first
  graded), and every point
  of it is a meaning the owner gave or an honest "cannot". On plain questions the arms tie.

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
- The data was cleaned for both arms (values, header names, types). The raw exports are not
  published and were never tested.
- One run per cell per round; both arms ran on one machine with the same user-level Claude Code
  configuration, not a clean profile. The system Python there holds the `duckdb` package (0.9.2)
  and the DuckDB CLI 1.5.6 is installed; both arms had both.
- The prompt cache was warm for rounds 1–3 and cold for the control and round 4 (§ Speed, tokens
  and cost); totals over five questions compare unlike things, and the questions 2–5 figures are
  the fair ones.
- Round 4 was launched by the build agent from a cleaned environment, the other runs by Sergey
  from his terminal.
- Four of the thirty unseen questions are counted from the day they are asked: B5 ("last month"),
  B6 ("this year so far"), C6 and C9 ("this year"). Their expected answers hold for 13 October 2026,
  the day both arms ran, as [questions-unseen.md](questions-unseen.md) says, and only for that day:
  a re-run on another day has other right numbers. B7 ("still open") and B8 ("still outstanding")
  read the status the export holds, which does not change, so they do not move; A3 ("right now")
  cannot be answered from this data on any day.
- The five questions were written by the data's owner. The thirty unseen ones were written by a
  separate session, but their expected answers were computed by the folder's author with the
  folder's definitions, A9's and A3's were settled after the runs, and the grading (✓, ≈, ✗) is the build
  agent's reading of each final reply.
