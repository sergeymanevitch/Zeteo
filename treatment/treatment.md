---
layer: L4
type: record
---

# treatment — what was asked and what came back

Written by [collect.py](../run/collect.py) from the raw transcripts in [raw/](raw/); never edited by hand. Every recorded session is listed, in the order it started.

Run folder: `/Users/Sergey/zeteo-runs/treatment`. Claude Code: 2.1.296.

Seconds run from the prompt to the last reply. Model calls count distinct model messages; tokens in include cache reads and writes.

| # | Model | Started (UTC) | Seconds | Model calls | Tool calls | Tokens in | Tokens out | Cost USD | Entry | Answer (start) | Transcript |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | claude-haiku-5-5 | 2026-10-12 20:07:20 | 10 | 5 | 8 | 163311 | 1574 | 0.0056 | sdk-cli bypassPermissions | **3 orders** — priority 1, plant 32, work center 3289, created in May 2025. Criteria: - T… | [q1-cbbce760.jsonl](raw/claude-haiku-5-5/q1-cbbce760.jsonl) |
| 2 | claude-haiku-5-5 | 2026-10-12 20:07:33 | 9 | 4 | 3 | 125780 | 1655 | 0.0055 | sdk-cli bypassPermissions | **170 readings were not performed in plant 43 in August 2026, covering 119 distinct measu… | [q2-8008f345.jsonl](raw/claude-haiku-5-5/q2-8008f345.jsonl) |
| 3 | claude-haiku-5-5 | 2026-10-12 20:07:44 | 12 | 5 | 5 | 164020 | 2258 | 0.0061 | sdk-cli bypassPermissions | **19.79%** of the notifications in plant 64 in September 2026 had priority 3 (244 of 1,23… | [q3-861053b3.jsonl](raw/claude-haiku-5-5/q3-861053b3.jsonl) |
| 4 | claude-haiku-5-5 | 2026-10-12 20:07:58 | 8 | 4 | 3 | 118354 | 1343 | 0.0045 | sdk-cli bypassPermissions | The maintenance cost for functional location **D-65-02-M-00230/04** in May 2026 is **9,11… | [q4-8164f0eb.jsonl](raw/claude-haiku-5-5/q4-8164f0eb.jsonl) |
| 5 | claude-haiku-5-5 | 2026-10-12 20:08:09 | 7 | 3 | 4 | 86659 | 1066 | 0.0041 | sdk-cli bypassPermissions | The user status of notification 100022640 is **REJC** (rejected). This is the plant's cod… | [q5-b264c8ab.jsonl](raw/claude-haiku-5-5/q5-b264c8ab.jsonl) |
| 1 | claude-sonnet-5-5 | 2026-10-12 20:08:18 | 10 | 4 | 6 | 118744 | 925 | 0.0824 | sdk-cli bypassPermissions | There were **3** priority 1 orders in plant 32 for work center 3289 in May 2025. Criteria… | [q1-d44441e8.jsonl](raw/claude-sonnet-5-5/q1-d44441e8.jsonl) |
| 2 | claude-sonnet-5-5 | 2026-10-12 20:08:31 | 10 | 4 | 5 | 113122 | 988 | 0.0715 | sdk-cli bypassPermissions | **170 points were not performed in plant 43 in August 2026.** That is 170 readings, cover… | [q2-e9f61b52.jsonl](raw/claude-sonnet-5-5/q2-e9f61b52.jsonl) |
| 3 | claude-sonnet-5-5 | 2026-10-12 20:08:43 | 11 | 4 | 6 | 115095 | 1484 | 0.0810 | sdk-cli bypassPermissions | **19.79%** of the notifications in plant 64 in September 2026 had priority 3. That is 244… | [q3-c834c57f.jsonl](raw/claude-sonnet-5-5/q3-c834c57f.jsonl) |
| 4 | claude-sonnet-5-5 | 2026-10-12 20:08:57 | 12 | 4 | 6 | 114077 | 1132 | 0.0754 | sdk-cli bypassPermissions | The material cost booked on D-65-02-M-00230/04 in May 2026 was **9,119.14** net. The data… | [q4-15656ad3.jsonl](raw/claude-sonnet-5-5/q4-15656ad3.jsonl) |
| 5 | claude-sonnet-5-5 | 2026-10-12 20:09:11 | 8 | 4 | 5 | 114734 | 668 | 0.0715 | sdk-cli bypassPermissions | Notification 100022640 has user status **`REJC`**, which means rejected (the plant's own … | [q5-bb04991e.jsonl](raw/claude-sonnet-5-5/q5-bb04991e.jsonl) |
| 1 | claude-opus-5-5 | 2026-10-12 20:09:22 | 14 | 4 | 3 | 114726 | 1143 | 0.1616 | sdk-cli bypassPermissions | Work center 3289 in plant 32 had **3** priority-1 orders in May 2025, counting orders cre… | [q1-a880a199.jsonl](raw/claude-opus-5-5/q1-a880a199.jsonl) |
| 2 | claude-opus-5-5 | 2026-10-12 20:09:38 | 13 | 4 | 3 | 111252 | 1184 | 0.1477 | sdk-cli bypassPermissions | In plant 43, **170 point readings were not performed in August 2026**. They cover **119 d… | [q2-86fb14c8.jsonl](raw/claude-opus-5-5/q2-86fb14c8.jsonl) |
| 3 | claude-opus-5-5 | 2026-10-12 20:09:54 | 14 | 4 | 3 | 112656 | 1245 | 0.1544 | sdk-cli bypassPermissions | **19.79%.** Of the 1,233 notifications created in plant 64 in September 2026, 244 had pri… | [q3-c5e27acb.jsonl](raw/claude-opus-5-5/q3-c5e27acb.jsonl) |
| 4 | claude-opus-5-5 | 2026-10-12 20:10:11 | 21 | 4 | 3 | 114966 | 1476 | 0.1702 | sdk-cli bypassPermissions | The net material cost for **D-65-02-M-00230/04** in May 2026 was **9,119.14**. That figur… | [q4-88da029d.jsonl](raw/claude-opus-5-5/q4-88da029d.jsonl) |
| 5 | claude-opus-5-5 | 2026-10-12 20:10:35 | 12 | 4 | 3 | 111067 | 889 | 0.1379 | sdk-cli bypassPermissions | Notification **100022640** has the user status **`REJC`**, which means rejected. It has o… | [q5-3a10f038.jsonl](raw/claude-opus-5-5/q5-3a10f038.jsonl) |

## Answers in full

### Q1 — claude-haiku-5-5 — `cbbce760`

Prompt:

````text
how many orders with priority 1 there were in plant 32 in may 2025 for work center 3289?
````

Final reply:

````text
**3 orders** — priority 1, plant 32, work center 3289, created in May 2025.

Criteria:
- Table: `ZW38_KG` (maintenance orders)
- Plant 32: `plant = '32'`, the plant rule for orders
- Work center 3289: `main_work_center = '3289'`
- Priority 1 ("immediately"): `priority = 1`
- Period: `created_on` in May 2025, as a half-open range

```sql
SELECT COUNT(*) AS orders
FROM 'data/ZW38_KG.parquet'
WHERE plant = '32'
  AND main_work_center = '3289'
  AND priority = 1
  AND created_on >= DATE '2025-05-01'
  AND created_on < DATE '2025-06-01';
```

The other reading uses the release date instead of the creation date, since `released_on` is the other date that could be meant. Filtering on `released_on` in May 2025 gives **5** orders.
````

### Q2 — claude-haiku-5-5 — `8008f345`

Prompt:

````text
how many points were not performed in plant 43 in august 2026?
````

Final reply:

````text
**170 readings were not performed in plant 43 in August 2026, covering 119 distinct measuring points.**

Criteria:
- Table: `IK17_KG` (measuring-point readings).
- Plant 43: 2nd segment of `functional_location`, since `IK17_KG` has no plant column.
- Period: `created_on` in August 2026.
- Not performed: `text_code IN ('Not performed', 'Not checked')`, which the rules count as not performed. That is 71 "Not performed" and 99 "Not checked" readings.

```sql
SELECT count(*) AS readings, count(DISTINCT point) AS points
FROM 'data/IK17_KG.parquet'
WHERE split_part(functional_location, '-', 2) = '43'
  AND created_on >= DATE '2026-08-01' AND created_on < DATE '2026-09-01'
  AND text_code IN ('Not performed', 'Not checked');
```

For comparison, plant 43 had 4,198 readings in August 2026 across 2,164 points, of which the 170 above are the not-performed ones.

The other reading, counting only the text code "Not performed" and excluding "Not checked", gives 71 readings on 59 points.
````

### Q3 — claude-haiku-5-5 — `861053b3`

Prompt:

````text
what the precentage of notifications with priority 3 out of all notifications there were in plant 64 in september 2026?
````

Final reply:

````text
**19.79%** of the notifications in plant 64 in September 2026 had priority 3 (244 of 1,233).

**Criteria**
- Table: `ZIW28_KG` (notifications).
- Plant 64 by the plant rule, so `64E` and `64I` count and empty `plant` rows are read from the functional location.
- `created_on` in September 2026 (`>= 2026-09-01` and `< 2026-10-01`).
- Part: `priority = 3` ("within a week"). Whole: all notifications in that plant and month, including the 45 with no priority.
- Notifications are counted as rows. No notification number appears twice in this set, so rows and distinct numbers give the same result.

**Query**
```sql
SELECT count(*) FILTER (WHERE priority = 3) AS p3,
       count(*) AS all_notifications,
       round(100.0 * count(*) FILTER (WHERE priority = 3) / count(*), 2) AS pct
FROM 'data/ZIW28_KG.parquet'
WHERE coalesce(try_cast(regexp_extract(plant, '^[0-9]+') AS INTEGER), try_cast(split_part(functional_location, '-', 2) AS INTEGER)) = 64
  AND created_on >= DATE '2026-09-01' AND created_on < DATE '2026-10-01';
```
The first query returned 244 of 1,233, which gives 19.79%.

**Alternative reading:** if the 45 notifications with no priority are left out of the whole, the share is 20.54% (244 of 1,188).
````

### Q4 — claude-haiku-5-5 — `8164f0eb`

Prompt:

````text
what was the maintenance cost for functional location D-65-02-M-00230/04 in may 2026
````

Final reply:

````text
The maintenance cost for functional location **D-65-02-M-00230/04** in May 2026 is **9,119.14** (net).

The result comes from material costs, the only cost table in the data. Labour and other order costs are not in these files.

- **Booked:** 18,098.06 across 6 rows
- **Returned:** −8,978.92, included in the net
- **Orders:** 2

**Criteria:**
- Table: `ZK22_KG` (material costs)
- Functional location: exactly `D-65-02-M-00230/04`
- Period: `date` in May 2026 (`date >= 2026-05-01` and `date < 2026-06-01`)
- Measure: net `sum(cost)`, returns included

**Query:**
```sql
SELECT count(*) AS rows, count(DISTINCT "order") AS orders,
       sum(cost) AS net_cost,
       sum(cost) FILTER (WHERE cost > 0) AS booked,
       sum(cost) FILTER (WHERE cost < 0) AS returned
FROM 'data/ZK22_KG.parquet'
WHERE functional_location = 'D-65-02-M-00230/04'
  AND date >= DATE '2026-05-01' AND date < DATE '2026-06-01';
```

If you meant the cost of maintenance orders that were created in May 2026 against this location, that would need the order-level data, but `ZW38_KG` has no functional location column, so it can't be matched to this unit directly.
````

### Q5 — claude-haiku-5-5 — `b264c8ab`

Prompt:

````text
what is the notification number 100022640 user status?
````

Final reply:

````text
The user status of notification 100022640 is **REJC** (rejected). This is the plant's code, per [reference/codes.md](reference/codes.md).

The notification has one row in `ZIW28_KG`:

| Field | Value |
| --- | --- |
| notification_user_status | REJC (rejected) |
| notification_system_status | NOCO (notification completed, SAP) |
| notification_type | R1 |
| priority | 3 (within a week) |
| functional_location | D-32-07-M-00705/00 |
| plant | 32 |
| created_on | 2019-01-03 |

Criteria: notification number = 100022640 (one row, so no other status rows to report).

Query:

```sql
SELECT * FROM 'data/ZIW28_KG.parquet'
WHERE CAST(notification AS VARCHAR) LIKE '%100022640%'
```

I matched with `LIKE` on the cast value rather than `=`. It returned exactly one row with the exact number, so the result is the same, but an exact match is the stricter form if you rerun it.
````

### Q1 — claude-sonnet-5-5 — `d44441e8`

Prompt:

````text
how many orders with priority 1 there were in plant 32 in may 2025 for work center 3289?
````

Final reply:

````text
There were **3** priority 1 orders in plant 32 for work center 3289 in May 2025.

Criteria:
- Table: `ZW38_KG` (maintenance orders), where one row is one order.
- Plant: `plant = '32'`.
- Work center: `main_work_center = '3289'`. Plant 32 has two work centers, 3215 and 3289.
- Priority: `priority = 1`, which means "do it immediately".
- Month: `created_on` in May 2025. I used the creation date because the question names no other date.

```sql
SELECT count(*) AS orders
FROM 'data/ZW38_KG.parquet'
WHERE plant = '32'
  AND priority = 1
  AND main_work_center = '3289'
  AND created_on >= DATE '2025-05-01' AND created_on < DATE '2025-06-01';
```

I did not run the other reading, which would filter May on another date such as `released_on` or `scheduled_start_date`. I can run it if you want it.
````

### Q2 — claude-sonnet-5-5 — `e9f61b52`

Prompt:

````text
how many points were not performed in plant 43 in august 2026?
````

Final reply:

````text
**170 points were not performed in plant 43 in August 2026.** That is 170 readings, covering 119 distinct measuring points. The same point can be read more than once in the month, so the two counts differ.

**Criteria**
- Table: `IK17_KG`, where one row is one reading of a measuring point.
- Plant 43: the 2nd segment of `functional_location` is `'43'`.
- Not performed: `text_code` is `Not performed` or `Not checked`. Of the 170 readings, 71 are `Not performed` and 99 are `Not checked`.
- August 2026: `created_on` from 2026-08-01 up to, but not including, 2026-09-01.

**Query**
```sql
SELECT count(*) AS readings,
       count(DISTINCT point) AS points,
       count(*) FILTER (text_code='Not performed') np,
       count(*) FILTER (text_code='Not checked') nc
FROM 'data/IK17_KG.parquet'
WHERE split_part(functional_location,'-',2)='43'
  AND text_code IN ('Not performed','Not checked')
  AND created_on >= DATE '2026-08-01' AND created_on < DATE '2026-09-01'
```

If you meant distinct points, the answer is 119. I did not run a query for any other reading of the question.
````

### Q3 — claude-sonnet-5-5 — `c834c57f`

Prompt:

````text
what the precentage of notifications with priority 3 out of all notifications there were in plant 64 in september 2026?
````

Final reply:

````text
**19.79%** of the notifications in plant 64 in September 2026 had priority 3. That is 244 of 1,233 notifications.

**Criteria**
- Table: `ZIW28_KG` (notifications).
- Plant 64: the plant rule from `reference/keys.md`. It takes the leading digits of `plant`, or the 2nd segment of `functional_location` when `plant` is empty.
- September 2026: `created_on` from 2026-09-01 up to, but not including, 2026-10-01.
- Priority 3: `priority = 3`, which means "within a week".
- The whole is every plant 64 notification created in the month, including the 45 with no priority.
- Counting distinct notification numbers gives the same 244 and 1,233, so no duplicates affect this month.

**Other reading:** if the 45 notifications with no priority are left out of the whole, the share is 244 of 1,188, which is **20.54%**.

**SQL**
```sql
SELECT count(*) AS total,
       count(*) FILTER (WHERE priority=3) AS p3,
       round(100.0*count(*) FILTER (WHERE priority=3)/count(*),2) AS pct,
       count(DISTINCT notification) AS dtotal,
       count(DISTINCT notification) FILTER (WHERE priority=3) AS dp3,
       count(*) FILTER (WHERE priority IS NULL) AS nullprio,
       round(100.0*count(*) FILTER (WHERE priority=3)/count(priority),2) AS pct_of_prioritised
FROM 'data/ZIW28_KG.parquet'
WHERE coalesce(try_cast(regexp_extract(plant, '^[0-9]+') AS INTEGER),
               try_cast(split_part(functional_location, '-', 2) AS INTEGER)) = 64
  AND created_on >= DATE '2026-09-01' AND created_on < DATE '2026-10-01'
```
````

### Q4 — claude-sonnet-5-5 — `15656ad3`

Prompt:

````text
what was the maintenance cost for functional location D-65-02-M-00230/04 in may 2026
````

Final reply:

````text
The material cost booked on D-65-02-M-00230/04 in May 2026 was **9,119.14** net. The data holds no currency, so I can't say which one.

- **Booked:** 18,098.06
- **Returned:** −8,978.92
- **Rows:** 6 material lines on 2 orders

**Criteria**
- I used `ZK22_KG`, the material-cost table. It is the only table with a cost column.
- The location is matched exactly, `D-65-02-M-00230/04`, since the full location was given.
- "May 2026" is the posting `date`, from 2026-05-01 up to but not including 2026-06-01.
- The cost is the net sum of `cost`, with returns left in.

**Reading limit:** "maintenance cost" here means material cost only. The data has no labour or other cost, so I can't give a total maintenance cost.

**SQL**
```sql
SELECT count(*) n, sum(cost) net,
       sum(cost) FILTER (WHERE cost>0) booked,
       sum(cost) FILTER (WHERE cost<0) returned,
       count(DISTINCT "order") orders
FROM 'data/ZK22_KG.parquet'
WHERE functional_location = 'D-65-02-M-00230/04'
  AND date >= DATE '2026-05-01' AND date < DATE '2026-06-01';
```
````

### Q5 — claude-sonnet-5-5 — `bb04991e`

Prompt:

````text
what is the notification number 100022640 user status?
````

Final reply:

````text
Notification 100022640 has user status **`REJC`**, which means rejected (the plant's own definition).

It has one row, created 2019-01-03:

| Field | Value | Meaning |
| --- | --- | --- |
| `notification_user_status` | `REJC` | rejected |
| `notification_system_status` | `NOCO` | notification completed (SAP standard meaning, not verified on this system) |
| `order_system_status` | empty | no order is attached |

**Criteria:** table `ZIW28_KG`, `notification = '100022640'`, with no other filter.

```sql
SELECT notification, notification_system_status, notification_user_status, order_system_status, created_on
FROM 'data/ZIW28_KG.parquet'
WHERE notification = '100022640';
```
````

### Q1 — claude-opus-5-5 — `a880a199`

Prompt:

````text
how many orders with priority 1 there were in plant 32 in may 2025 for work center 3289?
````

Final reply:

````text
Work center 3289 in plant 32 had **3** priority-1 orders in May 2025, counting orders created that month.

**Criteria:**
- Table: `ZW38_KG` (maintenance orders)
- Plant: `plant = '32'`
- Work center: `main_work_center = '3289'`
- Priority: `priority = 1` (do it immediately)
- Month: `created_on` from 2025-05-01 up to but not including 2025-06-01

```sql
SELECT count(*) AS orders
FROM 'data/ZW38_KG.parquet'
WHERE plant = '32' AND main_work_center = '3289' AND priority = 1
  AND created_on >= DATE '2025-05-01' AND created_on < DATE '2025-06-01';
```

If you count by the release date instead (`released_on` in May 2025), the same filters give **5** orders.
````

### Q2 — claude-opus-5-5 — `86fb14c8`

Prompt:

````text
how many points were not performed in plant 43 in august 2026?
````

Final reply:

````text
In plant 43, **170 point readings were not performed in August 2026**. They cover **119 distinct measuring points**, because some points were read more than once.

- 71 readings are recorded as `Not performed` and 99 as `Not checked`. The project's rules count both as not performed.
- For scale, plant 43 had 4,198 readings in total that month.

**Other reading:** if you count only the `Not performed` result and leave out `Not checked`, the answer is **71**.

**Criteria**
- Table `IK17_KG`, the measuring-point readings.
- Plant 43: the 2nd segment of `functional_location` is `'43'`.
- August 2026: `created_on` from 2026-08-01 up to, but not including, 2026-09-01.
- Not performed: `text_code IN ('Not performed', 'Not checked')`.

**Query**
```sql
SELECT count(*) AS readings,
       count(DISTINCT point) AS distinct_points,
       count(*) FILTER (WHERE text_code = 'Not performed') AS not_performed,
       count(*) FILTER (WHERE text_code = 'Not checked')   AS not_checked
FROM 'data/IK17_KG.parquet'
WHERE split_part(functional_location, '-', 2) = '43'
  AND created_on >= DATE '2026-08-01' AND created_on < DATE '2026-09-01'
  AND text_code IN ('Not performed', 'Not checked');
```
````

### Q3 — claude-opus-5-5 — `c5e27acb`

Prompt:

````text
what the precentage of notifications with priority 3 out of all notifications there were in plant 64 in september 2026?
````

Final reply:

````text
**19.79%.** Of the 1,233 notifications created in plant 64 in September 2026, 244 had priority 3 ("within a week").

**How I counted:**
- **Table:** `ZIW28_KG` (notifications).
- **Plant 64:** I took the number at the start of `plant`. Where `plant` is empty, I used the second part of `functional_location` instead.
- **September 2026:** notifications with `created_on` from 2026-09-01 up to, but not including, 2026-10-01.
- **Priority 3:** `priority = 3`.
- **Total:** all 1,233 notifications, including those with no priority. Each notification number appears only once.

```sql
SELECT count(*) AS all_notifs,
       count(*) FILTER (WHERE priority = 3) AS p3,
       round(100.0 * count(*) FILTER (WHERE priority = 3) / count(*), 2) AS pct_of_all
FROM 'data/ZIW28_KG.parquet'
WHERE coalesce(try_cast(regexp_extract(plant, '^[0-9]+') AS INTEGER),
               try_cast(split_part(functional_location, '-', 2) AS INTEGER)) = 64
  AND created_on >= DATE '2026-09-01' AND created_on < DATE '2026-10-01';
```

**Excluding notifications with no priority:** 45 of the notifications have no priority. Leaving them out of the total gives 244 of 1,188, or **20.54%**.
````

### Q4 — claude-opus-5-5 — `88da029d`

Prompt:

````text
what was the maintenance cost for functional location D-65-02-M-00230/04 in may 2026
````

Final reply:

````text
The net material cost for **D-65-02-M-00230/04** in May 2026 was **9,119.14**. That figure is 18,098.06 booked minus 8,978.92 returned, across 6 lines on 2 orders.

| Order | Date | Qty | Cost |
| --- | --- | --- | --- |
| 1000335380 | 2026-05-03 | 1 | 8,978.93 |
| 1000335380 | 2026-05-25 | 1 | 8,978.92 |
| 1000335380 | 2026-05-25 | −1 | −8,978.92 |
| 1000370723 | 2026-05-27 | 1 | 50.25 |
| 1000370723 | 2026-05-27 | 1 | 50.19 |
| 1000370723 | 2026-05-27 | 1 | 39.77 |

Almost all of the total comes from order 1000335380. The same item was booked twice (3 and 25 May) and returned once (25 May), so one booking of about 8,979 stays in the total.

**Criteria**
- Table `ZK22_KG` (material costs). This is the only cost data the folder has: labour and other order costs aren't in these files, so "maintenance cost" here means material cost.
- `functional_location` is exactly `D-65-02-M-00230/04`.
- `date` (posting date) is from 2026-05-01 up to, but not including, 2026-06-01.
- The total is the net `sum(cost)`, with returns included.

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

### Q5 — claude-opus-5-5 — `3a10f038`

Prompt:

````text
what is the notification number 100022640 user status?
````

Final reply:

````text
Notification **100022640** has the user status **`REJC`**, which means rejected.

It has one row in `ZIW28_KG`, created on 2019-01-03:

| Field | Value | Meaning |
| --- | --- | --- |
| User status | `REJC` | rejected |
| Notification system status | `NOCO` | notification completed |
| Order system status | empty | no order is attached to this notification |

**Criteria:** table `ZIW28_KG`, where the notification number ends in `100022640`. Only one row came back, and its number is exactly 100022640.

```sql
SELECT notification, notification_system_status, notification_user_status, order_system_status, created_on
FROM 'data/ZIW28_KG.parquet'
WHERE CAST(notification AS VARCHAR) LIKE '%100022640'
```
````
