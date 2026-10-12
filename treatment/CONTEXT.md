---
layer: L2
type: routing
---

# treatment — the runs with the folder

The treatment ran more than once, because the folder changed after its first run. Each round is a
folder named for what it ran on, holding the raw transcripts and the summary
[collect.py](../run/collect.py) wrote from them. No round is dropped or edited.

| Round | Folder it ran on | What changed before it |
| --- | --- | --- |
| [01_folder-679d0fb/](01_folder-679d0fb/treatment.md) | commit `679d0fb` | — |
| [02_plant-rule/](02_plant-rule/treatment.md) | commit `b35316d` | a plant is the `plant` column alone; `64E`, `64I` and empty plants left out |

The round-1 files were moved here from `treatment/` unchanged; its summary was written again by
`collect.py` from the same sessions, and differs only in the link to `collect.py`.
