---
layer: L0
type: entry
---

# Zeteo

This folder answers questions about four SAP plant-maintenance datasets in [data/](data/). Every
answer comes from a DuckDB query over those files, never from memory.

Read [identity.md](identity.md), then [rules.md](rules.md), before answering anything.

| To find | Read |
| --- | --- |
| how to answer, step by step | [rules.md](rules.md) |
| worked questions with their SQL | [examples.md](examples.md) |
| which table holds what | [reference/CONTEXT.md](reference/CONTEXT.md) |
| plant, functional location, joins, which date | [reference/keys.md](reference/keys.md) |
| what a code, status, priority or unit means | [reference/codes.md](reference/codes.md) |
| the columns of one table | [reference/ik17.md](reference/ik17.md), [reference/ziw28.md](reference/ziw28.md), [reference/zk22.md](reference/zk22.md), [reference/zw38.md](reference/zw38.md) |

Query with [query.py](query.py) from this folder: `uv run query.py "SELECT ... FROM ZIW28_KG ..."`.
