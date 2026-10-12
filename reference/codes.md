---
layer: L3
type: reference
---

# Codes — what the values mean

Source of each meaning: **plant** — given by the plant's maintenance engineer; **SAP** — SAP
standard meaning, not verified on this system; **unknown** — nobody has documented it. Never
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
| `1126` | unknown | 10 |

## Notification type (`ZIW28_KG.notification_type`) — unknown

`R1` 292,084, `R2` 80,833, `R3` 976, `R5` 54,902, `R6` 7,163. A classifier for filtering, almost
never used. It is **not** the urgency: every type holds every priority.

## Reading result (`IK17_KG.text_code`) — plant (translated from Hebrew)

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

## Units (`IK17_KG.units`) — translated from Hebrew where they were Hebrew

`h` hours, `°C`, `m/s`, `pcs` pieces, `L` litres, `mm`, `BAR`, `PSI`, `%`, `A`, `V`, `Hz`, `g`,
`Ω`, `N`, `RPM`, `N⋅m`, `m`. As exported and undocumented: `2MS`, `M3H` (reads as m³/h), `LMN`
(reads as l/min). Empty on 74 readings.

## User status (`ZIW28_KG.notification_user_status`, `ZW38_KG.user_status`)

A field may hold several codes: commas separate them on notifications (`PLND,EXE,COMP`), one or two
spaces on orders (`PLAN EXE  COMP`). Match a code with `regexp_matches(field, '\bEXE\b')`.

| Code | Meaning | Source |
| --- | --- | --- |
| `PLAN` | awaiting planning | plant |
| `PLND` | planned | plant |
| `EXE` | executed | plant |
| `COMP` | completed | plant |
| `REJC` | rejected | plant |
| `WFAP` | waiting for approval | plant |
| `ITEM`, `CRPA` | awaiting material or parts (which one is set depends on the combination of keys) | plant |
| `Approved`, `Open`, `Closed`, `Refurbished`, `Frozen` | as the word says; translated from Hebrew, used alone | plant |
| `CDON`, `PMBK`, `RPLN`, `IMPR`, `WFD`, `CNCL`, `WPRV`, `SCSH` | — | unknown |

## System status (`ZIW28_KG.notification_system_status`, `ZIW28_KG.order_system_status`, `ZW38_KG.system_status`)

Codes separated by spaces. `order_system_status` on notifications is the status of the order
attached to the notification; it is empty on the 32,639 notifications that have no order.

| Code | Meaning | Source |
| --- | --- | --- |
| `TECO` | technically completed: the work was performed | plant |
| `CMPL` | completed | plant |
| `NCMP` | not for completion | plant |
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
| `SSAP`, `RELR`, `NTUP`, `MSCP`, `MSPT`, `MSPR`, `GMCO` | — | unknown |

`ZIW28_KG.order_system_status` was cut short in the export: the fragments `NMA`, `MAC`, `MA`, `MAN`,
`N`, `NM`, `NT`, `SSA`, `SS`, `S`, `GMP`, `GM`, `G`, `CSE`, `CS`, `C`, `M` are truncated codes. A
code may therefore be missing from the end of that field. `ZW38_KG.system_status` also holds a
stray `*` on 15 orders.
