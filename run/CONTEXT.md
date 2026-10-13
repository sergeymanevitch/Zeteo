---
layer: L2
type: contract
---

# run — how both arms are run and recorded

One job: put the same questions to the same models with and without the Zeteo folder, and copy
what happened into the repository untouched.

The one variable is the folder. The prompt is the question exactly as written in
[../questions.md](../questions.md), nothing added; each question gets its own fresh session; the
models are Haiku, Sonnet and Opus, in that order. The control's folder holds the four Parquet files
of [../data/](../data/CONTEXT.md) and nothing else. The treatment's holds the same files plus the
folder — `CLAUDE.md`, `identity.md`, `rules.md`, `examples.md`, `reference/`, `query.py` — which Claude Code
loads by itself through `CLAUDE.md`. Both run outside any folder holding a `CLAUDE.md`, so nothing
of this workspace reaches either.

## Inputs

- [../questions.md](../questions.md): the prompts, the text after each `Q:` marker. Another file
  of the same shape, such as [../questions-unseen.md](../questions-unseen.md), is named by the
  `QUESTIONS` variable to both `ask.sh` and `collect.py`; `q<N>` is then its N-th question.
- [../data/](../data/CONTEXT.md): the Parquet files both arms get.
- For the treatment, the folder files listed in `FOLDER` of [make_arm.sh](make_arm.sh), their one
  home.

## Process

From the repository root, for each arm (`control` first, then `treatment`):

    run/make_arm.sh control                       # builds ~/zeteo-runs/control
    run/ask.sh ~/zeteo-runs/control haiku
    run/ask.sh ~/zeteo-runs/control sonnet
    run/ask.sh ~/zeteo-runs/control opus
    python3 run/collect.py control ~/zeteo-runs/control

[ask.sh](ask.sh) asks each question in order, each as its own `claude -p` session with
`--permission-mode bypassPermissions` (the run folder holds nothing but the arm's files; a
permission prompt would put a person's wait into the timings).

The same by hand, one session per question: `cd ~/zeteo-runs/control`, then
`claude --model haiku --permission-mode bypassPermissions`, paste one question, wait for the
reply, `/exit`; repeat. [collect.py](collect.py) reads either kind.

## Outputs

- `../<arm>/raw/<model>/q<N>-<session>.jsonl`: every session's transcript, a byte copy of what
  Claude Code recorded. An arm run more than once gets one round folder per run, named as the
  third argument of `collect.py` (`../treatment/01_folder-679d0fb/raw/…`), each from its own run
  folder (`run/make_arm.sh treatment ~/zeteo-runs/treatment-2`).
- `../<arm>/<arm>.md`: per session the question, the full final reply, seconds, model calls, tool
  calls, tokens and cost, written by [collect.py](collect.py) and never edited by hand.

## Human check

Sergey reads `<arm>.md` against the transcripts and commits both unedited. A failed, slow or
repeated session stays: it is listed, never dropped.
