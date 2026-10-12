---
layer: L3
type: reference
---

# Keys — location, plant, joins, dates

## Functional location

`D-88-02-M-00700/03` reads, segment by segment:

| Part | Here | Meaning |
| --- | --- | --- |
| `D` | `D` | no meaning; every location starts with it |
| plant | `88` | the plant |
| area | `02` | an area inside the plant |
| discipline | `M` | `M` mechanical, `E` electrical, `I` instrumentation, `G` gas, `S` safety; `C`, `K`, `N`, `P` also occur and are not relevant here; the owner's work centres on `M` |
| equipment | `00700` | the equipment number: five digits, or four digits and a letter (`0261F`) |
| unit | `/03` | the unit in a row of that equipment: `/03` is the third |

"700/3 in 88" and "700/03 in 88" mean the same unit: match it as
`functional_location LIKE 'D-88-%-00700/03'`, or exactly when the whole location is given.
Shorter locations name a higher level: `D-65` is the whole plant (641 notifications name a
whole plant, 589 of them `D-65`),
`D-65-02` an area, `D-65-02-M` a discipline in an area. To take everything under a level, use
`LIKE 'D-65-02-%'`.

## Plant

| Table | Plant of a row |
| --- | --- |
| `ZIW28_KG` | `plant`, read as a number; a value with a department letter (`64E`) or an empty value is no plant |
| `IK17_KG`, `ZK22_KG` | the 2nd segment of `functional_location` (no `plant` column) |
| `ZW38_KG` | `plant` as stored (no `functional_location`) |

On notifications a letter after the digits names a department, not a plant: `E` electrical, `I`
instrumentation. `65E` and `65I` are synthetic plants that say which department is in charge of
work done in plant 65. They are **not** counted as plant 65: a question about plant 65 means the
rows whose `plant` is `65` and nothing else (Sergey, 2026-10-12). Plants are numbers: `010` is
plant 10 and `1` is plant 01, so compare them as integers. For plant 65:

    try_cast(plant AS INTEGER) = 65                                                              -- ZIW28_KG
    split_part(functional_location, '-', 2) = '65'                                               -- IK17_KG, ZK22_KG
    plant = '65'                                                                                 -- ZW38_KG

Observed, not documented: in `ZIW28_KG`, `plant` is `88` on locations of plants 80 and 81, and
`70` on locations of plant 43; `plant` is empty on 3,887 rows; `010`, `06`, `1`, `4`,
`5`, `20`, `69` and `71` are plants too (Sergey). `ZW38_KG` has plants `13`, `32`, `43`, `56`, `64`, `65`,
`88` and `8100`; its `main_work_center` begins with the plant's digits (`4389` in plant 43), except
that work center `8811` serves both `88` and `8100`.

## Joins

- `functional_location` is shared by `IK17_KG`, `ZIW28_KG` and `ZK22_KG`: the way to put
  notifications, readings and material cost on the same equipment.
- `"order"` links `IK17_KG` and `ZK22_KG` for 134 orders only; do not rely on it.
- `ZW38_KG` has no order number and no location: it meets the others only by plant or work center.

## Dates

| Table | Default for "in a month / year" | Other dates (use only when the question names them) | Data runs |
| --- | --- | --- | --- |
| `ZIW28_KG` | `created_on` | `required_start_date`, `scheduled_end_date`, `reference_date` (undocumented) | 2019-01-01 to 2026-10-10 |
| `ZW38_KG` | `created_on` | `released_on`, `scheduled_start_date`, `scheduled_end_date`, `actual_start_date`, `actual_end_date`, `actual_start_date_2`, `required_end_date`, `closed_on` | 2018-05-03 to 2026-10-08 |
| `IK17_KG` | `created_on` | none | 2019-08-08 to 2026-10-08 |
| `ZK22_KG` | `date` | none | 2018-01-01 to 2026-09-30 |

The "Data runs" column is the range of the default date. What the other dates hold, and where they
cannot be trusted, is in each table's file.

A date later than today is an entry mistake, never a plan: people mistype years, and dates as
far as 2030 occur (Sergey).
