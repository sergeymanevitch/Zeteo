---
layer: L4
type: record
---

# treatment — what was asked and what came back

Written by [collect.py](../../run/collect.py) from the raw transcripts in [raw/](raw/); never edited by hand. Every recorded session is listed, in the order it started.

Run folder: `/Users/Sergey/zeteo-runs/treatment-2`. Claude Code: 2.1.296.

Seconds run from the prompt to the last reply. Model calls count distinct model messages; tokens in include cache reads and writes.

| # | Model | Started (UTC) | Seconds | Model calls | Tool calls | Tokens in | Tokens out | Cost USD | Entry | Answer (start) | Transcript |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | claude-haiku-5-5 | 2026-10-12 20:27:13 | 8 | 4 | 6 | 126788 | 1263 | 0.0049 | sdk-cli bypassPermissions | **3 orders.** Criteria: - Table: `ZW38_KG` (maintenance orders) - `plant` = '32' - `prior… | [q1-ce90b065.jsonl](raw/claude-haiku-5-5/q1-ce90b065.jsonl) |
| 2 | claude-haiku-5-5 | 2026-10-12 20:27:23 | 9 | 4 | 3 | 121178 | 1559 | 0.0050 | sdk-cli bypassPermissions | **170 readings were not performed in plant 43 in August 2026**, covering **119 distinct m… | [q2-eed95aa5.jsonl](raw/claude-haiku-5-5/q2-eed95aa5.jsonl) |
| 3 | claude-haiku-5-5 | 2026-10-12 20:27:35 | 8 | 4 | 3 | 127477 | 1558 | 0.0051 | sdk-cli bypassPermissions | **19.98%** of plant 64's notifications created in September 2026 had priority 3: 240 of 1… | [q3-38dfeca4.jsonl](raw/claude-haiku-5-5/q3-38dfeca4.jsonl) |
| 4 | claude-haiku-5-5 | 2026-10-12 20:27:46 | 12 | 6 | 9 | 195642 | 2098 | 0.0064 | sdk-cli bypassPermissions | **Material cost for D-65-02-M-00230/04 in May 2026: 9,119.14 net.** This is the net sum o… | [q4-f5dfd963.jsonl](raw/claude-haiku-5-5/q4-f5dfd963.jsonl) |
| 5 | claude-haiku-5-5 | 2026-10-12 20:28:01 | 8 | 5 | 5 | 145429 | 1089 | 0.0045 | sdk-cli bypassPermissions | The user status of notification 100022640 is **REJC (rejected)**. It is the only row for … | [q5-0b39b534.jsonl](raw/claude-haiku-5-5/q5-0b39b534.jsonl) |
| 1 | claude-sonnet-5-5 | 2026-10-12 20:28:11 | 9 | 4 | 6 | 118680 | 776 | 0.0803 | sdk-cli bypassPermissions | **3** orders. Criteria (table `ZW38_KG`, one row per order): - plant = `32` - `main_work_… | [q1-7f27201d.jsonl](raw/claude-sonnet-5-5/q1-7f27201d.jsonl) |
| 2 | claude-sonnet-5-5 | 2026-10-12 20:28:22 | 10 | 4 | 5 | 113228 | 952 | 0.0712 | sdk-cli bypassPermissions | **170** "not performed" point readings in plant 43 in August 2026. They cover **119 disti… | [q2-a68140be.jsonl](raw/claude-sonnet-5-5/q2-a68140be.jsonl) |
| 3 | claude-sonnet-5-5 | 2026-10-12 20:28:34 | 11 | 4 | 6 | 118907 | 1210 | 0.0858 | sdk-cli bypassPermissions | **19.98%** of the notifications in plant 64 created in September 2026 had priority 3 (240… | [q3-843e7a07.jsonl](raw/claude-sonnet-5-5/q3-843e7a07.jsonl) |
| 4 | claude-sonnet-5-5 | 2026-10-12 20:28:47 | 11 | 4 | 6 | 114020 | 1086 | 0.0744 | sdk-cli bypassPermissions | The maintenance cost for D-65-02-M-00230/04 in May 2026 was **9,119.14** net. The data ha… | [q4-e4311719.jsonl](raw/claude-sonnet-5-5/q4-e4311719.jsonl) |
| 5 | claude-sonnet-5-5 | 2026-10-12 20:29:00 | 8 | 4 | 5 | 114814 | 646 | 0.0714 | sdk-cli bypassPermissions | Notification 100022640 has user status **REJC**, which means **rejected**. The plant's ma… | [q5-613b8ceb.jsonl](raw/claude-sonnet-5-5/q5-613b8ceb.jsonl) |
| 1 | claude-opus-5-5 | 2026-10-12 20:29:10 | 21 | 4 | 3 | 115263 | 1093 | 0.1541 | sdk-cli bypassPermissions | **3 orders.** Plant 32 had 3 orders with priority 1 ("do it immediately") at work center … | [q1-606ef46b.jsonl](raw/claude-opus-5-5/q1-606ef46b.jsonl) |
| 2 | claude-opus-5-5 | 2026-10-12 20:29:33 | 14 | 4 | 3 | 112819 | 1171 | 0.1536 | sdk-cli bypassPermissions | In August 2026, plant 43 had **170 point readings that were not performed**. They cover *… | [q2-e7a9ee6b.jsonl](raw/claude-opus-5-5/q2-e7a9ee6b.jsonl) |
| 3 | claude-opus-5-5 | 2026-10-12 20:29:49 | 15 | 4 | 3 | 114727 | 1345 | 0.1599 | sdk-cli bypassPermissions | **19.98%.** In plant 64, 240 of the 1,201 notifications created in September 2026 had pri… | [q3-331bd831.jsonl](raw/claude-opus-5-5/q3-331bd831.jsonl) |
| 4 | claude-opus-5-5 | 2026-10-12 20:30:06 | 17 | 4 | 3 | 115042 | 1529 | 0.1713 | sdk-cli bypassPermissions | The net maintenance (material) cost on **D-65-02-M-00230/04 in May 2026 was 9,119.14**. T… | [q4-f0b0378e.jsonl](raw/claude-opus-5-5/q4-f0b0378e.jsonl) |
| 5 | claude-opus-5-5 | 2026-10-12 20:30:26 | 15 | 4 | 3 | 114083 | 853 | 0.1519 | sdk-cli bypassPermissions | Notification **100022640** has the user status **`REJC`**, which means **rejected** (a me… | [q5-0e0d6870.jsonl](raw/claude-opus-5-5/q5-0e0d6870.jsonl) |

## Answers in full

### Q1 — claude-haiku-5-5 — `ce90b065`

Prompt:

````text
how many orders with priority 1 there were in plant 32 in may 2025 for work center 3289?
````

Final reply:

````text
**3 orders.**

Criteria:
- Table: `ZW38_KG` (maintenance orders)
- `plant` = '32'
- `priority` = 1
- `main_work_center` = '3289'
- `created_on` in May 2025 (`>= 2025-05-01` and `< 2025-06-01`), the default date for "in a month"

Query:

```sql
SELECT COUNT(*) AS orders
FROM 'data/ZW38_KG.parquet'
WHERE plant = '32'
  AND priority = 1
  AND main_work_center = '3289'
  AND created_on >= DATE '2025-05-01'
  AND created_on < DATE '2025-06-01';
```
````

### Q2 — claude-haiku-5-5 — `eed95aa5`

Prompt:

````text
how many points were not performed in plant 43 in august 2026?
````

Final reply:

````text
**170 readings were not performed in plant 43 in August 2026**, covering **119 distinct measuring points**.

- **Not checked:** 99 readings, 60 points
- **Not performed:** 71 readings, 59 points

The question asks how many points, and points are read more than once, so both counts are shown. Each point appears under only one of the two codes, so the point counts add to 119.

Criteria:
- Table: `IK17_KG` (measuring-point readings)
- Plant 43: the second segment of `functional_location` is `43`
- Month: `created_on` from 2026-08-01 up to, but not including, 2026-09-01
- Not performed: `text_code IN ('Not performed', 'Not checked')`, per the rules

```sql
SELECT count(*) AS readings, count(DISTINCT point) AS points
FROM 'data/IK17_KG.parquet'
WHERE split_part(functional_location, '-', 2) = '43'
  AND created_on >= DATE '2026-08-01' AND created_on < DATE '2026-09-01'
  AND text_code IN ('Not performed', 'Not checked');
```

Alternative reading: if "not performed" means only the `Not performed` code, the count is 71 readings. Other plant 43 results in the month (OK, Performed, Not OK) are not included.
````

### Q3 — claude-haiku-5-5 — `38dfeca4`

Prompt:

````text
what the precentage of notifications with priority 3 out of all notifications there were in plant 64 in september 2026?
````

Final reply:

````text
**19.98%** of plant 64's notifications created in September 2026 had priority 3: 240 of 1,201.

**Criteria**
- Table: `ZIW28_KG` (notifications)
- Plant 64: `try_cast(plant AS INTEGER) = 64`
- Period: `created_on` in September 2026 (`>= 2026-09-01` and `< 2026-10-01`)
- Numerator: `priority = 3`
- Denominator: all notifications in the period, including the 21 with no priority. Each notification number appears once, so rows and distinct notifications give the same result.

**Query**
```sql
SELECT round(100.0 * count(*) FILTER (WHERE priority = 3) / count(*), 2) AS pct
FROM 'data/ZIW28_KG.parquet'
WHERE try_cast(plant AS INTEGER) = 64
  AND created_on >= DATE '2026-09-01' AND created_on < DATE '2026-10-01';
```

**Other reading:** If the 21 notifications with no priority are left out of the denominator, the share is **20.34%** (240 of 1,180).
````

### Q4 — claude-haiku-5-5 — `f5dfd963`

Prompt:

````text
what was the maintenance cost for functional location D-65-02-M-00230/04 in may 2026
````

Final reply:

````text
**Material cost for D-65-02-M-00230/04 in May 2026: 9,119.14 net.**

This is the net sum of `cost` in `ZK22_KG`, returns included. It covers 6 lines, of which 1 is a return:
- Booked: 18,098.06
- Returned: −8,978.92

Criteria:
- Table: `ZK22_KG` (material costs). The data has no cost column in `ZW38_KG`, so orders carry no cost here.
- Location: `functional_location` exactly `D-65-02-M-00230/04`.
- Period: `date` from 2026-05-01 up to, but not including, 2026-06-01.

```sql
SELECT sum(cost) AS net_cost,
       sum(cost) FILTER (WHERE cost > 0) AS booked,
       sum(cost) FILTER (WHERE cost < 0) AS returned,
       count(*) AS lines,
       count(*) FILTER (WHERE cost < 0) AS return_lines
FROM 'data/ZK22_KG.parquet'
WHERE functional_location = 'D-65-02-M-00230/04'
  AND date >= DATE '2026-05-01' AND date < DATE '2026-06-01';
```

The other reading is the whole equipment, all units under `D-65-02-M-00230`. That gives 23,746.55 net over 23 lines, using `functional_location LIKE 'D-65-02-M-00230/%'`.
````

### Q5 — claude-haiku-5-5 — `0b39b534`

Prompt:

````text
what is the notification number 100022640 user status?
````

Final reply:

````text
The user status of notification 100022640 is **REJC (rejected)**.

It is the only row for this notification. Its notification system status is NOCO (notification completed, set by SAP). The notification is type R1, priority 3, plant 32, on functional location D-32-07-M-00705/00, created 2019-01-03.

**Criteria**
- `notification` = 100022640 (matched as text in `ZIW28_KG`)

**SQL**
```sql
SELECT * FROM 'data/ZIW28_KG.parquet'
WHERE CAST("notification" AS VARCHAR) LIKE '%100022640%'
```
````

### Q1 — claude-sonnet-5-5 — `7f27201d`

Prompt:

````text
how many orders with priority 1 there were in plant 32 in may 2025 for work center 3289?
````

Final reply:

````text
**3** orders.

Criteria (table `ZW38_KG`, one row per order):
- plant = `32`
- `main_work_center` = `3289`
- `priority` = 1 (do it immediately)
- "May 2025" is read as `created_on` in that month, which is the default date for "in a month"

```sql
SELECT count(*) AS orders
FROM 'data/ZW38_KG.parquet'
WHERE plant = '32'
  AND main_work_center = '3289'
  AND priority = 1
  AND created_on >= DATE '2025-05-01' AND created_on < DATE '2025-06-01';
```

I didn't run the other readings of "in May 2025", such as orders released, scheduled or closed that month. Tell me if you want one of those.
````

### Q2 — claude-sonnet-5-5 — `a68140be`

Prompt:

````text
how many points were not performed in plant 43 in august 2026?
````

Final reply:

````text
**170** "not performed" point readings in plant 43 in August 2026. They cover **119 distinct measuring points**, because a point can be read more than once.

Criteria:
- **Table:** `IK17_KG`, where one row is one reading of a point.
- **Plant 43:** the 2nd segment of `functional_location` is `43`, since this table has no `plant` column.
- **August 2026:** `created_on` from 2026-08-01 up to but not including 2026-09-01.
- **Not performed:** `text_code` is `Not performed` or `Not checked`. Of the 170 readings, 71 are `Not performed` and 99 are `Not checked`.

If you meant only `Not performed` and not `Not checked`, the count is 71.

```sql
SELECT count(*) AS readings, count(DISTINCT point) AS points,
       count(*) FILTER (text_code='Not performed') np,
       count(*) FILTER (text_code='Not checked') nc
FROM 'data/IK17_KG.parquet'
WHERE split_part(functional_location,'-',2)='43'
  AND created_on >= DATE '2026-08-01' AND created_on < DATE '2026-09-01'
  AND text_code IN ('Not performed','Not checked')
```
````

### Q3 — claude-sonnet-5-5 — `843e7a07`

Prompt:

````text
what the precentage of notifications with priority 3 out of all notifications there were in plant 64 in september 2026?
````

Final reply:

````text
**19.98%** of the notifications in plant 64 created in September 2026 had priority 3 (240 of 1,201).

**Criteria**
- **Table:** `ZIW28_KG` (notifications), where one row is one notification.
- **Plant 64:** `try_cast(plant AS INTEGER) = 64`. Department plants such as `64E` and rows with an empty plant are left out.
- **September 2026:** `created_on` from 2026-09-01 up to, but not including, 2026-10-01.
- **Priority 3:** `priority = 3`, which means "within a week".
- **Whole:** all 1,201 notifications in plant 64 that month, including 21 with no priority. There are no duplicate notification numbers among them.

**Other reading:** if the 21 notifications with no priority are left out of the whole, the share is 240 of 1,180, or **20.34%**.

**SQL**
```sql
SELECT count(*) AS total,
       count(*) FILTER (WHERE priority=3) AS p3,
       round(100.0*count(*) FILTER (WHERE priority=3)/count(*),2) AS pct
FROM 'data/ZIW28_KG.parquet'
WHERE try_cast(plant AS INTEGER)=64
  AND created_on >= DATE '2026-09-01' AND created_on < DATE '2026-10-01'
```
````

### Q4 — claude-sonnet-5-5 — `e4311719`

Prompt:

````text
what was the maintenance cost for functional location D-65-02-M-00230/04 in may 2026
````

Final reply:

````text
The maintenance cost for D-65-02-M-00230/04 in May 2026 was **9,119.14** net. The data has no currency column, so I can't state the currency.

- **Booked:** 18,098.06
- **Returned:** −8,978.92
- **Net (booked plus returned):** 9,119.14
- **Rows:** 6 material postings across 2 orders

**Criteria**
- **Table:** `ZK22_KG`, the material-cost table. It is the only table with costs, so this figure covers material only.
- **Location:** exactly `D-65-02-M-00230/04`.
- **Period:** posting `date` from 2026-05-01 up to but not including 2026-06-01.
- **Cost:** the net sum of `cost`, with returns kept in as negatives.

**Query**
```sql
SELECT count(*) AS n, sum(cost) AS net,
       sum(cost) FILTER (WHERE cost>0) AS booked,
       sum(cost) FILTER (WHERE cost<0) AS returned,
       count(DISTINCT "order") AS orders
FROM 'data/ZK22_KG.parquet'
WHERE functional_location='D-65-02-M-00230/04'
  AND date >= DATE '2026-05-01' AND date < DATE '2026-06-01'
```
````

### Q5 — claude-sonnet-5-5 — `613b8ceb`

Prompt:

````text
what is the notification number 100022640 user status?
````

Final reply:

````text
Notification 100022640 has user status **REJC**, which means **rejected**. The plant's maintenance engineer documented this meaning in `reference/codes.md`.

The notification has one row. It also carries these statuses:
- **Notification system status:** `NOCO`, notification completed. This is the SAP standard meaning, not verified on this system.
- **Order system status:** empty. The notification has no order attached.

**Criteria:** table `ZIW28_KG`, `notification` = '100022640', no other filter.

```sql
SELECT notification, notification_system_status, notification_user_status, order_system_status
FROM 'data/ZIW28_KG.parquet'
WHERE notification = '100022640'
```
````

### Q1 — claude-opus-5-5 — `606ef46b`

Prompt:

````text
how many orders with priority 1 there were in plant 32 in may 2025 for work center 3289?
````

Final reply:

````text
**3 orders.** Plant 32 had 3 orders with priority 1 ("do it immediately") at work center 3289 that were created in May 2025.

What I counted, in the orders table (`ZW38_KG`):
- Plant is `32`.
- Work center (`main_work_center`) is `3289`.
- Priority is `1`.
- "May 2025" means the creation date, from 2025-05-01 up to but not including 2025-06-01. This is the project's default when a question doesn't name a date.

```sql
SELECT count(*)
FROM 'data/ZW38_KG.parquet'
WHERE plant = '32'
  AND main_work_center = '3289'
  AND priority = 1
  AND created_on >= DATE '2025-05-01' AND created_on < DATE '2025-06-01';
```

If you meant orders *released* in May 2025 rather than created, the same filters with `released_on` give **5**.
````

### Q2 — claude-opus-5-5 — `e7a9ee6b`

Prompt:

````text
how many points were not performed in plant 43 in august 2026?
````

Final reply:

````text
In August 2026, plant 43 had **170 point readings that were not performed**. They cover **119 distinct measuring points**, because some points were read more than once in the month.

- 71 readings have the result `Not performed`.
- 99 have `Not checked`, which the project rules also count as not performed.
- Out of all 4,198 readings in plant 43 that month, 170 were not performed.

If you count only readings marked `Not performed` and leave out `Not checked`, the answer is **71**.

**How I counted:**
- Table: `IK17_KG` (measuring-point readings).
- Plant 43: the second part of `functional_location` is `43`.
- August 2026: by `created_on`, from 2026-08-01 up to but not including 2026-09-01.
- Not performed: `text_code` is `Not performed` or `Not checked`.

```sql
SELECT count(*) AS readings,
       count(DISTINCT point) AS distinct_points,
       count(*) FILTER (WHERE text_code = 'Not performed') AS not_performed,
       count(*) FILTER (WHERE text_code = 'Not checked')   AS not_checked
FROM 'data/IK17_KG.parquet'
WHERE split_part(functional_location, '-', 2) = '43'
  AND text_code IN ('Not performed', 'Not checked')
  AND created_on >= DATE '2026-08-01' AND created_on < DATE '2026-09-01';
```
````

### Q3 — claude-opus-5-5 — `331bd831`

Prompt:

````text
what the precentage of notifications with priority 3 out of all notifications there were in plant 64 in september 2026?
````

Final reply:

````text
**19.98%.** In plant 64, 240 of the 1,201 notifications created in September 2026 had priority 3 ("within a week").

**Criteria**
- Table: `ZIW28_KG` (notifications).
- Plant 64: `plant` read as the number 64. The department plants `64E` and `64I` are not plant 64, so they're left out.
- Month: `created_on` from 2026-09-01 up to, but not including, 2026-10-01.
- Part: notifications with `priority = 3`.
- Whole: every plant 64 notification in that month, including the 21 with no priority recorded.
- Each notification number appears only once, so counting rows gives the same result as counting distinct notifications.

**The other way to read it:** if the whole is only the 1,180 notifications that have a priority recorded, the share is **20.34%**.

```sql
SELECT count(*) FILTER (WHERE priority = 3) AS p3,
       count(*) AS all_notifications,
       round(100.0 * count(*) FILTER (WHERE priority = 3) / count(*), 2) AS pct_of_all,
       count(priority) AS with_priority,
       round(100.0 * count(*) FILTER (WHERE priority = 3) / count(priority), 2) AS pct_of_prioritised
FROM 'data/ZIW28_KG.parquet'
WHERE try_cast(plant AS INTEGER) = 64
  AND created_on >= DATE '2026-09-01' AND created_on < DATE '2026-10-01';
```
````

### Q4 — claude-opus-5-5 — `f0b0378e`

Prompt:

````text
what was the maintenance cost for functional location D-65-02-M-00230/04 in may 2026
````

Final reply:

````text
The net maintenance (material) cost on **D-65-02-M-00230/04 in May 2026 was 9,119.14**. That covers 6 lines on 2 orders: 18,098.06 booked and −8,978.92 returned.

Most of it is one item. On 2026-05-03, order 1000335380 booked 8,978.93. On 2026-05-25 the same order booked 8,978.92 again and returned it the same day, so only the first booking remains in the total. The other 140.21 is three small lines on order 1000370723, all on 2026-05-27.

| order | date | quantity | cost |
| --- | --- | --- | --- |
| 1000335380 | 2026-05-03 | 1 | 8,978.93 |
| 1000335380 | 2026-05-25 | 1 | 8,978.92 |
| 1000335380 | 2026-05-25 | −1 | −8,978.92 |
| 1000370723 | 2026-05-27 | 1 | 50.25 |
| 1000370723 | 2026-05-27 | 1 | 50.19 |
| 1000370723 | 2026-05-27 | 1 | 39.77 |

**Criteria**
- Table: `ZK22_KG`, the material costs table. The data has no labour or other cost columns, so "maintenance cost" here means material cost only.
- Location: `functional_location` is exactly `D-65-02-M-00230/04`.
- Month: posting `date` in May 2026, from 2026-05-01 up to but not including 2026-06-01.
- Total: net sum of `cost`, with returns kept in.

**Query**
```sql
SELECT sum(cost) AS net_cost,
       sum(cost) FILTER (WHERE cost > 0) AS booked,
       sum(cost) FILTER (WHERE cost < 0) AS returned,
       count(*) AS lines,
       count(DISTINCT "order") AS orders
FROM 'data/ZK22_KG.parquet'
WHERE functional_location = 'D-65-02-M-00230/04'
  AND date >= DATE '2026-05-01' AND date < DATE '2026-06-01';
```
````

### Q5 — claude-opus-5-5 — `0e0d6870`

Prompt:

````text
what is the notification number 100022640 user status?
````

Final reply:

````text
Notification **100022640** has the user status **`REJC`**, which means **rejected** (a meaning given by the plant).

There is one row for this number:

| Field | Value | Meaning |
| --- | --- | --- |
| User status | `REJC` | rejected |
| Notification system status | `NOCO` | notification completed (SAP standard meaning, not checked on this system) |
| Order system status | empty | no order is attached to this notification |
| Created on | 2019-01-03 | |
| Plant | 32 | |

So the notification was rejected and closed without an order being raised.

**Criteria:** table `ZIW28_KG` (notifications), where `notification = '100022640'`.

```sql
SELECT notification, notification_user_status, notification_system_status,
       order_system_status, created_on, plant
FROM 'data/ZIW28_KG.parquet'
WHERE notification = '100022640';
```
````
