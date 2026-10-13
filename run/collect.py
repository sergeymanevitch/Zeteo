"""Copy one arm's raw session transcripts into the repository and write the arm's summary.

    python3 run/collect.py control   ~/zeteo-runs/control
    python3 run/collect.py treatment ~/zeteo-runs/treatment-2 02_plant-rule

An optional third argument names a round folder inside the arm, for an arm run more than once.
QUESTIONS names another questions file in the repository root, as for run/ask.sh; q<N> is then
the N-th question of that file.

Reads every Claude Code session recorded for ARM_DIR (~/.claude/projects/<ARM_DIR encoded>/).
Writes <arm>[/<round>]/raw/<model>/q<N>-<session>.jsonl, each a byte copy, and <arm>.md beside raw/.
Nothing is filtered: a session whose prompt is not a question of questions.md is copied as
unmatched-<session>.jsonl and listed; a question asked twice is listed twice.
Safe to re-run; it never edits a transcript.
"""

import json
import os
import pathlib
import re
import shutil
import sys
from datetime import datetime

REPO = pathlib.Path(__file__).resolve().parent.parent


def questions():
    text = (REPO / os.environ.get("QUESTIONS", "questions.md")).read_text(encoding="utf-8")
    return [line[3:].strip() for line in text.splitlines() if line.startswith("Q: ")]


def prompt_text(content):
    if isinstance(content, str):
        return content
    parts = [b.get("text", "") for b in content if isinstance(b, dict) and b.get("type") == "text"]
    return "\n".join(parts) if parts else None


def when(stamp):
    return datetime.fromisoformat(stamp.replace("Z", "+00:00"))


def read_session(path):
    s = {"path": path, "prompts": [], "models": [], "messages": {}, "tools": 0,
         "answer": "", "first": None, "last": None, "cost": None, "version": None,
         "mode": None, "entry": None, "session": path.stem}
    for line in path.read_text(encoding="utf-8").splitlines():
        r = json.loads(line)
        kind = r.get("type")
        if kind == "user" and isinstance(r.get("message"), dict):
            text = prompt_text(r["message"].get("content"))
            if text is not None and not text.startswith("<"):
                s["prompts"].append(text.strip())
                if s["first"] is None:
                    s["first"] = r["timestamp"]
                    s["version"] = r.get("version")
                    s["mode"] = r.get("permissionMode")
                    s["entry"] = r.get("entrypoint")
        elif kind == "assistant" and isinstance(r.get("message"), dict):
            m = r["message"]
            model = m.get("model")
            if model and model != "<synthetic>" and model not in s["models"]:
                s["models"].append(model)
            if m.get("id"):
                s["messages"][m["id"]] = m.get("usage") or {}
            for block in m.get("content") or []:
                if block.get("type") == "tool_use":
                    s["tools"] += 1
                elif block.get("type") == "text" and block.get("text", "").strip():
                    s["answer"] = block["text"].strip()
            s["last"] = r["timestamp"]
        elif kind == "cost-state":
            s["cost"] = r.get("totalCostUSD")
    return s


def tokens(s):
    out = sum(u.get("output_tokens", 0) for u in s["messages"].values())
    inp = sum(u.get("input_tokens", 0) + u.get("cache_read_input_tokens", 0)
              + u.get("cache_creation_input_tokens", 0) for u in s["messages"].values())
    return inp, out


def one_line(text, width=90):
    text = " ".join(text.split()).replace("|", "\\|")
    return text if len(text) <= width else text[: width - 1] + "…"


def main():
    if len(sys.argv) not in (3, 4) or sys.argv[1] not in ("control", "treatment"):
        sys.exit("usage: python3 run/collect.py control|treatment ARM_DIR [ROUND]")
    arm = sys.argv[1]
    arm_dir = os.path.realpath(os.path.expanduser(sys.argv[2]))
    source = pathlib.Path.home() / ".claude" / "projects" / re.sub(r"[^A-Za-z0-9]", "-", arm_dir)
    if not source.is_dir():
        sys.exit(f"no sessions recorded for {arm_dir} (looked in {source})")

    asked = questions()
    sessions = [read_session(p) for p in source.glob("*.jsonl")]
    sessions = [s for s in sessions if s["first"]]
    sessions.sort(key=lambda s: s["first"])

    out_dir = REPO / arm / sys.argv[3] if len(sys.argv) == 4 else REPO / arm
    tool = os.path.relpath(REPO / "run" / "collect.py", out_dir)
    rows = []
    for s in sessions:
        number = asked.index(s["prompts"][0]) + 1 if s["prompts"][0] in asked else None
        model = s["models"][0] if s["models"] else "no-model"
        name = (f"q{number}" if number else "unmatched") + f"-{s['session'][:8]}.jsonl"
        target = out_dir / "raw" / model / name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(s["path"], target)
        seconds = (when(s["last"]) - when(s["first"])).total_seconds() if s["last"] else None
        rows.append((number, model, s, target, seconds))

    lines = [
        "---", "layer: L4", "type: record", "---", "",
        f"# {arm} — what was asked and what came back", "",
        f"Written by [collect.py]({tool}) from the raw transcripts in [raw/](raw/); "
        "never edited by hand. Every recorded session is listed, in the order it started.", "",
        f"Run folder: `{arm_dir}`. "
        f"Claude Code: {', '.join(sorted({s['version'] or '?' for _, _, s, _, _ in rows}))}.", "",
        "Seconds run from the prompt to the last reply. Model calls count distinct model "
        "messages; tokens in include cache reads and writes.", "",
        "| # | Model | Started (UTC) | Seconds | Model calls | Tool calls | Tokens in | Tokens out "
        "| Cost USD | Entry | Answer (start) | Transcript |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for number, model, s, target, seconds in rows:
        tin, tout = tokens(s)
        cost = f"{s['cost']:.4f}" if s["cost"] is not None else ""
        lines.append(
            f"| {number or '—'} | {model} | {s['first'][:19].replace('T', ' ')} "
            f"| {seconds:.0f} | {len(s['messages'])} | {s['tools']} | {tin} | {tout} | {cost} "
            f"| {s['entry']} {s['mode']} | {one_line(s['answer'])} "
            f"| [{target.name}]({target.relative_to(out_dir).as_posix()}) |"
        )
    lines += ["", "## Answers in full", ""]
    for number, model, s, target, seconds in rows:
        lines += [f"### Q{number or ' unmatched'} — {model} — `{s['session'][:8]}`", "",
                  "Prompt:", "", "````text", *s["prompts"][:1], "````", ""]
        if len(s["prompts"]) > 1:
            lines += [f"The session holds {len(s['prompts']) - 1} more prompt(s); see the transcript.", ""]
        lines += ["Final reply:", "", "````text", s["answer"] or "(no text reply)", "````", ""]
    (out_dir / f"{arm}.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"{len(rows)} sessions -> {out_dir / (arm + '.md')}")


if __name__ == "__main__":
    main()
