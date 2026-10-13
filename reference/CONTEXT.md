---
layer: L2
type: routing
---

# reference — the map of the data

What each table is, what its columns hold, what its codes mean, and how the tables meet. Stable
material: it changes only when the data or a definition does. The files are in
[../data/](../data/); every count below was read from them with DuckDB.

| Table | One row is | Rows | File |
| --- | --- | --- | --- |
| `IK17_KG` | one reading of a measuring point, normally inside an inspection order | 729,886 | [ik17.md](ik17.md) |
| `ZIW28_KG` | one maintenance notification | 435,958 | [ziw28.md](ziw28.md) |
| `ZK22_KG` | one material consumption (or return) on an order | 547,801 | [zk22.md](zk22.md) |
| `ZW38_KG` | one maintenance order | 70,241 | [zw38.md](zw38.md) |

| For | Read |
| --- | --- |
| functional location, the plant rule, joins, which date a question asks about | [keys.md](keys.md) |
| priorities, types, text codes, units, user and system statuses | [codes.md](codes.md) |
