#!/bin/sh
# Build the folder one arm runs in, outside this repository.
#
#   run/make_arm.sh control   [DEST]   the four Parquet files, nothing else
#   run/make_arm.sh treatment [DEST]   the same files plus the Zeteo folder
#
# DEST defaults to $HOME/zeteo-runs/<arm>. It must not exist yet, and no folder above it may
# hold a CLAUDE.md or AGENTS.md: Claude Code would load it into the run.
set -eu

arm=${1:-}
case $arm in
    control|treatment) ;;
    *) echo "usage: run/make_arm.sh control|treatment [DEST]" >&2; exit 2 ;;
esac
repo=$(cd "$(dirname "$0")/.." && pwd)
dest=${2:-$HOME/zeteo-runs/$arm}

# The files the treatment gets and the control does not. One home: here.
FOLDER="CLAUDE.md identity.md rules.md examples.md reference query.py"

if [ -e "$dest" ]; then
    echo "$dest exists; remove it or name another" >&2
    exit 1
fi
parent=$(dirname "$dest")
mkdir -p "$parent"
up=$(cd "$parent" && pwd -P)
while :; do
    for f in CLAUDE.md AGENTS.md; do
        if [ -e "$up/$f" ]; then
            echo "$up/$f would be loaded into the run; pick a DEST outside that folder" >&2
            exit 1
        fi
    done
    [ "$up" = / ] && break
    up=$(dirname "$up")
done

if [ "$arm" = treatment ]; then
    for f in $FOLDER; do
        [ -e "$repo/$f" ] || { echo "$repo/$f is missing; the folder is not built yet" >&2; exit 1; }
    done
fi

mkdir -p "$dest/data"
cp "$repo"/data/*.parquet "$dest/data/"
if [ "$arm" = treatment ]; then
    for f in $FOLDER; do
        cp -R "$repo/$f" "$dest/$f"
    done
fi
echo "$arm ready: $dest"
find "$dest" -type f | sort
