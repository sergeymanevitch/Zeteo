---
layer: L3
type: reference
---

# Codes — what the values mean

Source of each meaning: **plant** — given by the plant's maintenance engineer; **SAP** — the SAP
standard meaning, which the plant uses as it stands (Sergey, 2026-10-13); **unknown** — nobody has
documented it. Never
invent a meaning for an unknown code; report the code as stored and say it is undocumented.

## Priority (`priority` in `ZIW28_KG` and `ZW38_KG`) — plant

How urgently the work must be done. Empty on 66,183 notifications and 33,187 orders.

| Priority | Do it | Notifications | Orders |
| --- | --- | --- | --- |
| 1 | immediately | 70,430 | 7,433 |
| 2 | within 24 hours | 58,000 | 2,496 |
| 3 | within a week | 121,640 | 11,233 |
| 4 | within a month | 89,177 | 10,089 |
| 5 | within three months | 16,601 | 2,945 |
| 6 | at the yearly shutdown | 13,927 | 2,858 |

## Order type (`ZW38_KG.order_type`) — plant

| Code | Meaning | Orders |
| --- | --- | --- |
| `RPM1` | maintenance (corrective) | 32,294 |
| `RPM2` | preventive maintenance | 37,902 |
| `RPM3` | safety-related work | 2 |
| `RPM7` | root cause analysis (RCA) | 33 |
| `1126` | the project department (Sergey, 2026-10-13) | 10 |

## Notification type (`ZIW28_KG.notification_type`) — plant

The type of order the notification is for (Sergey, 2026-10-13). It is **not** the urgency: every
type holds every priority.

| Code | Meaning | Notifications |
| --- | --- | --- |
| `R1` | corrective maintenance | 292,084 |
| `R2` | preventive maintenance | 80,833 |
| `R3` | root cause problem elimination | 976 |
| `R5` | an order raised on the technicians' preventive rounds in the field | 54,902 |
| `R6` | corrective maintenance, safety | 7,163 |

## Reading result (`IK17_KG.text_code`) — plant

| Value | Readings | Note |
| --- | --- | --- |
| `OK` | 593,958 | |
| `Performed` | 58,890 | |
| `Not checked` | 50,695 | counts as not performed |
| `Not OK` | 21,902 | a fault found |
| `Not performed` | 4,047 | counts as not performed |
| `Handled` | 173 | |
| `To be checked` | 42 | |
| `Yes` / `No` | 9 / 8 | |
| `Does not exist` | 1 | |
| empty | 161 | |

## Units (`IK17_KG.units`)

`h` hours, `°C`, `m/s`, `pcs` pieces, `L` litres, `mm`, `BAR`, `PSI`, `%`, `A`, `V`, `Hz`, `g`,
`Ω`, `N`, `RPM`, `N⋅m`, `m`. As exported, meanings from the plant (Sergey, 2026-10-13): `2MS`
millimetres per second squared (3,555 readings), `M3H` cubic metres per hour (2,172), `LMN` litres
per minute (1,733). Empty on 74 readings.

## User status (`ZIW28_KG.notification_user_status`, `ZW38_KG.user_status`)

A field may hold several codes: commas separate them on notifications (`PLND,EXE,COMP`), one or two
spaces on orders (`PLAN EXE  COMP`). As in every status field, the first code from the left is the
current status and the rest are history (below, under the system status): `PLND,EXE,COMP` is
planned now, and was executed and completed on the way. The first code is `PLAN` on 369,198
notifications and 65,890 orders, most of them completed by their system status; say so when it
shapes an answer. Match a code anywhere with `regexp_matches(field, '\bEXE\b')`.

| Code | Meaning | Source |
| --- | --- | --- |
| `PLAN` | awaiting planning | plant |
| `PLND` | planned | plant |
| `EXE` | executed | plant |
| `COMP` | completed | plant |
| `REJC` | rejected | plant |
| `WFAP` | waiting for approval | plant |
| `ITEM`, `CRPA` | awaiting material or parts | plant |
| `CDON` | closed by a contractor | plant |
| `PMBK` | the central planned maintenance department | plant |
| `RPLN` | for re-planning | plant |
| `IMPR` | improvement works | plant |
| `WFD` | waiting for additional information or documentation | plant |
| `WPRV` | waiting for approval | plant |
| `CNCL` | cancelled | plant |
| `SCSH` | second shift | plant |
| `Approved`, `Open`, `Closed`, `Refurbished`, `Frozen` | as the word says; used alone | plant |

## System status (`ZIW28_KG.notification_system_status`, `ZIW28_KG.order_system_status`, `ZW38_KG.system_status`)

Codes separated by spaces; on `ZIW28_KG.order_system_status`, by commas. `order_system_status` on
notifications is the status of the order attached to the notification; it is empty on the 32,639
notifications that have no order.

**In every status field, system or user, the first code from the left is the current status; the
codes after it are history** (Sergey, 2026-10-13). `TECO PRT GMPS MACM PRC SETC` is an order that is technically completed now. A
question about the status something is in ("orders released", "notifications in process") reads
the first code:

    regexp_extract(system_status, '^\s*([^ ,]+)', 1) = 'REL'

A question about what happened on the way ("orders delayed for lack of people") looks for the code
anywhere in the field, `regexp_matches(system_status, '\bMSCP\b')`. The first code is `NOCO`,
`NOPR`, `NOPO`, `ATCO`, `OSNO` or `DLFL` on notifications, and `TECO`, `CMPL`, `CRTD`, `REL` or
`LKD` on orders.

**A completed notification** (Sergey, 2026-10-13) has `NOCO` as the first code of
`notification_system_status`: 378,589 notifications.

    regexp_extract(notification_system_status, '^\s*([^ ,]+)', 1) = 'NOCO'

**A completed order** (Sergey, 2026-10-13) has `TECO` in `ZW38_KG.system_status`, or `CMPL`
without `NCMP`. An order with both `CMPL` and `NCMP` was closed without the work being done and is
not completed. In the data: 62,493 orders with `TECO`, 5,024 with `CMPL` and `NCMP`, 142 with
`CMPL` alone; no order holds `TECO` with either. `CMPL` is always the first code; `TECO` is first on
61,832 orders and second, after `LKD` (locked), on the other 661 — they count as completed.

    regexp_matches(system_status, '\bTECO\b')
      OR (regexp_matches(system_status, '\bCMPL\b') AND NOT regexp_matches(system_status, '\bNCMP\b'))

| Code | Meaning | Source |
| --- | --- | --- |
| `TECO` | technically completed: the work was performed | plant |
| `CMPL` | completed — closed; with `NCMP` beside it, closed without the work being done | plant |
| `NCMP` | not for completion: beside `CMPL`, the order was closed and nothing was done | plant |
| `NOCO` | notification completed | SAP |
| `NOPR` | notification in process | SAP |
| `NOPO` | notification postponed | SAP |
| `OSNO` | outstanding notification | SAP |
| `NOPT` | notification printed | SAP |
| `ORAS` | order assigned to the notification | SAP |
| `OSTS` | outstanding task(s) | SAP |
| `ATCO` | all tasks completed | SAP |
| `DLFL` | deletion flag | SAP |
| `CRTD` | created, not released | SAP |
| `REL` | released | SAP |
| `PCNF` | partially confirmed | SAP |
| `CNF` | confirmed | SAP |
| `PRC` | pre-costed | SAP |
| `ESTC` | estimated costs | SAP |
| `SETC` | settlement rule created | SAP |
| `CSER` | error in cost calculation | SAP |
| `NMAT` | no material components | SAP |
| `MACM` | material committed | SAP |
| `MANC` | material availability not checked | SAP |
| `GMPS` | goods movement posted | SAP |
| `PRT` | printed | SAP |
| `PPRT` | partially printed | SAP |
| `LKD` | locked | SAP |
| `SSAP` | object created (internal to SAP) | plant |
| `RELR` | the release was postponed | plant |
| `NTUP` | the dates are not updated | plant |
| `MSCP` | not enough people (human resources) | plant |
| `MSPT` | not enough materials | plant |
| `MSPR` | not enough people, tools or heavy equipment | plant |
| `GMCO` | material movement in a collaborative order | plant |

`ZIW28_KG.order_system_status` was cut short in the export: the fragments `NMA`, `MAC`, `MA`, `MAN`,
`N`, `NM`, `NT`, `SSA`, `SS`, `S`, `GMP`, `GM`, `G`, `CSE`, `CS`, `C`, `M` are truncated codes. A
code may therefore be missing from the end of that field. `ZW38_KG.system_status` also holds a
stray `*` on 16 orders, on one of them glued to the code before it (`NTUP*`).
