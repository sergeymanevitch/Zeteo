# Zeteo

A folder that answers questions about four SAP plant-maintenance datasets — notifications, orders,
measuring-point readings and material costs — and the evidence of what it does that no folder does
not. Every answer comes from one DuckDB query over the shipped Parquet files, and the answer shows
the criteria and the SQL it ran.

**What the evidence says:** by the answer key, the folder tied no folder (6 of 15 against 6 of 15),
because the key is itself wrong three times. By what the data says, no folder got 9 of 15 and the
folder 12, then 14 in its last round — every point from a domain meaning the questions' author
supplied, one of them written after the runs. The folder is a third faster and a sixth dearer, and
most of what made no folder good was spent before the control ran, on cleaning the data both arms
got. On thirty questions the author did not write, the folder got 82 of 90 answers right and no
folder 49: the arms tie on plain questions, and the lead is the owner's meanings and an honest
"cannot" where the data holds no answer. The whole account, losses and ties included:
[results.md](results.md).

## What is here

| Path | What it is |
| --- | --- |
| [questions.md](questions.md) | five questions with the expected answers, committed before anything else (`fe7a35b`) |
| [questions-unseen.md](questions-unseen.md) | thirty questions the author did not write, committed before either arm was asked them |
| [data/](data/CONTEXT.md) | the four Parquet files both arms query, with their row counts and sha256 |
| [CLAUDE.md](CLAUDE.md) | the folder's entry: Claude Code loads it, and it routes to the rest |
| [identity.md](identity.md) | who Zeteo is: an analyst that answers only from a query |
| [rules.md](rules.md) | how to answer, step by step |
| [examples.md](examples.md) | worked questions with their SQL and what they return |
| [reference/](reference/CONTEXT.md) | the map of the data: tables, columns, codes, keys, which date |
| [query.py](query.py) | one read-only door to the four tables, used by the folder from round 3 |
| [control/](control/control.md) | the run without the folder, raw transcripts and a summary; `unseen/` the same on the thirty questions |
| [treatment/](treatment/CONTEXT.md) | the runs with the folder — four rounds and the thirty questions, raw transcripts and a summary each |
| [run/](run/CONTEXT.md) | the kit that builds each arm, asks the questions and records the sessions |
| [check/](check/CONTEXT.md) | a check that recomputes every number the folder states about the data; copied into no run |
| [results.md](results.md) | what changed, question by question, and what changed in the folder because of it |

The folder is the five files `CLAUDE.md`, `identity.md`, `rules.md`, `examples.md` and
`reference/`, plus `query.py`. This README is for people and is copied into no run.

## The data

Four SAP exports from one company's plant maintenance: 435,958 notifications, 70,241 orders,
729,886 measuring-point readings and 547,801 material bookings ([data/](data/CONTEXT.md)). They are
a slice prepared for this competition, kept to the minimum, but they hold the main, high-volume
part of the work — the tables a maintenance planner queries every day — so the folder is built and
tested on data at real volume, not on a sample. Some questions a planner asks need data that is not
here: whether a notification's work was done on time, for one — the day the work was reported
performed is there, but not what "on time" is measured against. The folder says so instead of
answering.

## How the experiment ran

The control gets the four Parquet files alone. The treatment gets the same files plus the folder.
Each question of [`questions.md`](questions.md) is the whole prompt, asked as written in its own fresh headless
`claude -p` session, on Haiku, then Sonnet, then Opus. Claude Code's session transcripts are copied
into the repository byte for byte, with a summary written from them by script.

The control ran once; the treatment ran four times, because the folder changed three times after
a treatment run. Each round's folder is named for the commit it ran on; [results.md](results.md)
says what changed and why.

## Re-running both arms

Requirements:

- [Claude Code](https://claude.com/claude-code), logged in. The recorded runs used 2.1.296.
- For the treatment: [`uv`](https://docs.astral.sh/uv/) (`uv run query.py` fetches `duckdb` 1.5.6,
  pinned since the run on the thirty unseen questions; the recorded runs asked for any `duckdb` from
  1.0 on and did not record which one they got), or a `python3` with the `duckdb` package installed.
- For recording: `python3` 3.9 or newer, standard library only.

From the repository root:

    run/make_arm.sh control                    # builds ~/zeteo-runs/control: the Parquet files only
    run/ask.sh ~/zeteo-runs/control haiku
    run/ask.sh ~/zeteo-runs/control sonnet
    run/ask.sh ~/zeteo-runs/control opus
    python3 run/collect.py control ~/zeteo-runs/control

    run/make_arm.sh treatment                  # builds ~/zeteo-runs/treatment: the files plus the folder
    run/ask.sh ~/zeteo-runs/treatment haiku
    run/ask.sh ~/zeteo-runs/treatment sonnet
    run/ask.sh ~/zeteo-runs/treatment opus
    python3 run/collect.py treatment ~/zeteo-runs/treatment 05_rerun

Things to know before you compare:

- Run the kit from a fresh clone, so that what it records sits beside nothing you need to keep.
- The run folder must sit outside any folder holding a `CLAUDE.md` or `AGENTS.md`, and must not
  exist yet; [`make_arm.sh`](run/make_arm.sh) refuses either. Pass another path as its second argument.
- [`ask.sh`](run/ask.sh) runs with `--permission-mode bypassPermissions`, so that no permission prompt puts a
  person's wait into the timings. The run folder holds nothing but the arm's files.
- `haiku`, `sonnet` and `opus` are aliases. The recorded runs resolved them to `claude-haiku-5-5`,
  `claude-sonnet-5-5` and `claude-opus-5-5`; pass a full model ID to `ask.sh` to pin one.
- [`collect.py`](run/collect.py) copies the sessions into the clone. Give the treatment a new round name (above,
  `05_rerun`) so that it writes beside the committed rounds. The control has no rounds: its
  transcripts land beside the committed ones and [`control/control.md`](control/control.md) is written again from the new
  sessions alone — `git diff` shows the old against the new.
- The current folder is round 4's plus the code meanings and decisions added after it and the
  fixes made after the unseen run, which move none of the five answers ([results.md](results.md),
  What changed). To re-run a round exactly, check out the commit it names (`679d0fb`, `b35316d`,
  `aa8e82a` or `d85d39b`; `236cc9f` for the thirty unseen questions) in a separate worktree and use
  the kit from there.
- Four of the thirty unseen questions are counted from the day they are asked: B5 ("last month"),
  B6 ("this year so far"), C6 and C9 ("this year"). Their expected answers in
  [`questions-unseen.md`](questions-unseen.md) hold for 13 October 2026, the day both arms ran;
  asked on another day, a right answer is another number. A3 ("right now"), B7 ("still open") and
  B8 ("still outstanding") read the status the export holds, and the export does not change, so
  they do not move.
- The control's sessions explored the files with whatever was installed: pandas and pyarrow on the
  recording machine, plus the DuckDB CLI 1.5.6 and a system Python holding `duckdb` 0.9.2. The
  treatment needs only [`query.py`](query.py) from round 3 on.

The expected spread, on the current folder (round 4): Q1 3 and Q5 `REJC` in both arms; Q2 170 with
the folder and 71 (or 60 distinct points) without; Q3 22.19 % with the folder and 19.98 % without;
Q4 9119.14 in both. Three of the committed expected
answers are wrong, and [results.md](results.md) says how.

## Asking it your own question

Build the treatment folder as above, `cd` into it, start `claude`, and ask in plain English. Or
query directly from this repository:

    uv run query.py --tables
    uv run query.py "SELECT count(*) FROM ZIW28_KG WHERE priority = 1"

To check that every number the folder states still holds against the data — the worked examples,
the counts of [reference/](reference/CONTEXT.md), and the SQL rules written the same way
everywhere — run `uv run check/check.py` from this repository ([check/](check/CONTEXT.md)).

## Limits

- The data is cleaned for both arms: values in four columns normalised, misspelt headers corrected,
  types set. The raw Excel exports are not published, and no arm was run on them.
- The questions and the folder's domain meanings come from one person, the data's owner.
- One run per model per question per round, on one machine.
