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
| discipline | `M` | `M` mechanical, `E` electrical, `I` instrumentation, `G` gas, `S` safety, `C` IT, `K` general, `N` HVAC and air conditioning, `P` piping; the owner's work centres on `M` |
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
| `ZIW28_KG` | `plant`, read as a number: the plant in charge; a value with a department letter (`64E`) or an empty value is no plant |
| `IK17_KG`, `ZK22_KG` | the 2nd segment of `functional_location`: the plant where the equipment stands (no `plant` column) |
| `ZW38_KG` | `plant` as stored (no `functional_location`) |

On notifications a letter after the digits names a department, not a plant: `E` electrical, `I`
instrumentation. `65E` and `65I` are synthetic plants that say which department is in charge of
work done in plant 65. They are **not** counted as plant 65: a question about plant 65 means the
rows whose `plant` is `65` and nothing else (Sergey, 2026-10-12). Plants are numbers: `010` is
plant 10 and `1` is plant 01, so compare them as integers. For plant 65:

    try_cast(plant AS INTEGER) = 65                                                              -- ZIW28_KG
    split_part(functional_location, '-', 2) = '65'                                               -- IK17_KG, ZK22_KG
    plant = '65'                                                                                 -- ZW38_KG

A location's plant and a notification's plant can differ: the location says where the equipment
stands, `plant` which plant is in charge of it (Sergey, 2026-10-13). In `ZIW28_KG`, `plant` is `88`
on 4,406 notifications at locations of plant 80 and 968 of plant 81, and `70` on 1,451 at locations
of plant 43. `88`, `80`, `81` and `8100` are one plant divided into sub-plants (Sergey,
2026-10-13); for now they are treated separately (Sergey, 2026-10-13): a question naming one of
them means that code alone, as for any plant.

`plant` is empty on 3,887 notifications; `010`, `06`, `1`, `4`, `5`, `20`, `69` and `71` are plants
too (Sergey). `ZW38_KG` has plants `13`, `32`, `43`, `56`, `64`, `65`, `88` and `8100`; its
`main_work_center` begins with the plant's digits (`4389` in plant 43), and work center `8811`
serves both `88` and `8100`, sub-plants of one plant.

## Joins

- `functional_location` is shared by `IK17_KG`, `ZIW28_KG` and `ZK22_KG`: the way to put
  notifications, readings and material cost on the same equipment.
- `"order"` links `IK17_KG` and `ZK22_KG` for 134 orders only; do not rely on it.
- `ZW38_KG` has no order number and no location: it meets the others only by plant or work center.

## Dates

Every table has several dates, and each answers a different question. Pick the column by what the
question asks about — opened, due, planned, released, started, closed — from the tables below.
When the question names a period and no event ("notifications in plant 64 in September 2026"),
use the table's default. A day is `col = DATE '2026-10-05'`; a month or a year is a half-open range,
`col >= DATE '2026-09-01' AND col < DATE '2026-10-01'`. Name the column in the criteria, and when
another date would give a different reading, give its number on the line for the other reading.

### Notifications, `ZIW28_KG`

The default is `required_start_date`: the plant reads a notification by the day its work is
required, to plan the work (Sergey, 2026-10-13).

| The question asks | Column |
| --- | --- |
| notifications in a period, no event named | `required_start_date` (default) |
| when the work is required, due, to be done by; planning | `required_start_date` |
| when notifications were opened, created, raised, reported; comparing how many were opened in one month with another | `created_on` |
| when the work is scheduled to end | `scheduled_end_date` |
| when the work was reported performed | `reference_date` (below) |

`required_start_date` runs from 2008-05-01 to 2028-12-21; 3 rows before 2000 are not real dates.
`created_on` runs from 2019-01-01 to 2026-10-10. `reference_date` is the day the work was reported
performed (Sergey, 2026-10-13). It is filled on every row and set again when the notification is
closed: before that it holds another day, most often `created_on` (26,419 of the 36,722 whose
system status begins `NOPR`), so read it on notifications whose system status begins `NOCO`
(completed). On a closed notification it can still equal `created_on`: the work was done the day
it was reported, or the order was opened only after the work, recorded and closed at once. One row reads
9202-12-15. The plant has not said what "on time" is measured against, so whether work was done on
time is not answered from this data; say so, and give the dates the question needs.

### Orders, `ZW38_KG`

The default is `created_on`: how many orders were opened in a period, and how many of those were
then completed — completed as [codes.md](codes.md) defines it under the system status (Sergey,
2026-10-13).

| The question asks | Column |
| --- | --- |
| orders in a period, no event named; orders opened, created | `created_on` (default) |
| orders planned or scheduled for a day or a period; scheduled to start | `scheduled_start_date` |
| scheduled to end | `scheduled_end_date` |
| required to end, due | `required_end_date` |
| released | `released_on` |
| when work actually started | `actual_start_date` (empty on most orders; say how many have none) |
| actually ended | `actual_end_date` — it equals `scheduled_end_date` when the order was done on its scheduled day, which is 70,238 of 70,241 rows |
| closed, technically completed | `closed_on`, on orders with `TECO` only ([zw38.md](zw38.md)) |

`created_on` runs from 2018-05-03 to 2026-10-08. `actual_start_date_2` is described in
[zw38.md](zw38.md) and used only when named.

### Readings and material cost

`IK17_KG` has one date, `created_on`, the day of the reading (2019-08-08 to 2026-10-08).
`ZK22_KG` has one date, `date`, the day of the booking (2018-01-01 to 2026-09-30).

### A date later than today

A date later than today is kept and counted as stored. Planned dates run ahead by design, and
dates up to five years ahead occur and can be real; with these exports alone a mistyped date cannot
be told from a real one (Sergey, 2026-10-13). When an answer counts rows dated later than today,
say how many.
