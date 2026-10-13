---
layer: L3
type: routing
---

# data — the dataset both arms query

Four Parquet files, one per SAP maintenance export. Both the control and the treatment get exactly
these files and nothing else from this folder: this `CONTEXT.md` is not copied into either run
(see [../run/](../run/CONTEXT.md)). What the columns mean is the folder's job, in `reference/`.

| File | Rows |
| --- | --- |
| [IK17_KG.parquet](IK17_KG.parquet) | 729,886 |
| [ZIW28_KG.parquet](ZIW28_KG.parquet) | 435,958 |
| [ZK22_KG.parquet](ZK22_KG.parquet) | 547,801 |
| [ZW38_KG.parquet](ZW38_KG.parquet) | 70,241 |

Prepared on 2026-10-12 from four Excel exports that are not published. Changed, and nothing else:
misspelt column names corrected, values in four columns normalised (`IK17_KG.text_code` and
`units`, both user statuses), dates typed as `DATE`, measures as `DOUBLE`, cost as `DECIMAL(18,2)`,
priority as `INTEGER`. No row was added, removed or
repaired; codes and identifiers are text exactly as exported. The files are written by script and
never edited by hand.

| File | sha256 |
| --- | --- |
| `IK17_KG.parquet` | `26a1a886bce481f7b23256a697d9256aacb402334804256b34168d93d68fdf97` |
| `ZIW28_KG.parquet` | `57d3d6db1e924443900c3748a236ef8318bf14b6343bafd2bd17f821eb9604c5` |
| `ZK22_KG.parquet` | `7bfe202f85645cc19d544cb7a23c2c4ef3ffeb6f07ec976f4634f6a464fb6c0b` |
| `ZW38_KG.parquet` | `c228ee81091d29add7ab0c18c9979fd25743c963f07f9baa0202a6b8e4ae86a5` |
