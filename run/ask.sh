#!/bin/sh
# Ask every question of questions.md, in order, each in its own fresh headless session.
#
#   run/ask.sh ARM_DIR MODEL        e.g.  run/ask.sh ~/zeteo-runs/control haiku
#
# QUESTIONS names another questions file in the repository root, e.g.
# QUESTIONS=questions-unseen.md run/ask.sh ~/zeteo-runs/control-unseen haiku
#
# The prompt is the text after "Q: " in questions.md, exactly as written. Claude Code keeps each
# session's transcript under ~/.claude/projects/; run/collect.py copies them into the repository.
set -eu

dir=${1:-}
model=${2:-}
if [ -z "$dir" ] || [ -z "$model" ]; then
    echo "usage: run/ask.sh ARM_DIR MODEL" >&2
    exit 2
fi
repo=$(cd "$(dirname "$0")/.." && pwd)
cd "$dir"

sed -n 's/^Q: //p' "$repo/${QUESTIONS:-questions.md}" | while IFS= read -r question; do
    echo "=== $model: $question"
    claude -p "$question" --model "$model" --permission-mode bypassPermissions </dev/null
    echo
done
