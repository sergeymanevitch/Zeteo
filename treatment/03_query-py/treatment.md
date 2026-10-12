---
layer: L4
type: record
---

# treatment — what was asked and what came back

Written by [collect.py](../../run/collect.py) from the raw transcripts in [raw/](raw/); never edited by hand. Every recorded session is listed, in the order it started.

Run folder: `/Users/Sergey/zeteo-runs/treatment-3`. Claude Code: 2.1.296.

Seconds run from the prompt to the last reply. Model calls count distinct model messages; tokens in include cache reads and writes.

| # | Model | Started (UTC) | Seconds | Model calls | Tool calls | Tokens in | Tokens out | Cost USD | Entry | Answer (start) | Transcript |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | claude-haiku-5-5 | 2026-10-12 20:36:46 | 10 | 4 | 3 | 125571 | 1038 | 0.0051 | sdk-cli bypassPermissions | **3 orders** — priority 1, plant 32, work center 3289, created in May 2025. Criteria: - T… | [q1-37407087.jsonl](raw/claude-haiku-5-5/q1-37407087.jsonl) |
| 2 | claude-haiku-5-5 | 2026-10-12 20:36:58 | 7 | 3 | 3 | 92374 | 1102 | 0.0044 | sdk-cli bypassPermissions | **170 readings, covering 119 distinct points, were not performed in plant 43 in August 20… | [q2-c4fdeee9.jsonl](raw/claude-haiku-5-5/q2-c4fdeee9.jsonl) |
| 3 | claude-haiku-5-5 | 2026-10-12 20:37:07 | 12 | 5 | 5 | 161277 | 1932 | 0.0057 | sdk-cli bypassPermissions | **19.98%** of plant 64's notifications created in September 2026 had priority 3: 240 of 1… | [q3-15b4709c.jsonl](raw/claude-haiku-5-5/q3-15b4709c.jsonl) |
| 4 | claude-haiku-5-5 | 2026-10-12 20:37:22 | 11 | 4 | 7 | 120450 | 2068 | 0.0050 | sdk-cli bypassPermissions | **May 2026 maintenance cost for D-65-02-M-00230/04: 9,119.14 (net)** The net is made of 1… | [q4-7f64f467.jsonl](raw/claude-haiku-5-5/q4-7f64f467.jsonl) |
| 5 | claude-haiku-5-5 | 2026-10-12 20:37:35 | 6 | 3 | 5 | 86583 | 988 | 0.0040 | sdk-cli bypassPermissions | The user status of notification 100022640 is **REJC**, which means rejected. The plant se… | [q5-6b10617a.jsonl](raw/claude-haiku-5-5/q5-6b10617a.jsonl) |
| 1 | claude-sonnet-5-5 | 2026-10-12 20:37:44 | 10 | 4 | 6 | 118921 | 827 | 0.0811 | sdk-cli bypassPermissions | There were **3** priority 1 orders in plant 32 for work center 3289 in May 2025. Criteria… | [q1-ca7da2c5.jsonl](raw/claude-sonnet-5-5/q1-ca7da2c5.jsonl) |
| 2 | claude-sonnet-5-5 | 2026-10-12 20:37:56 | 19 | 4 | 5 | 113444 | 1007 | 0.0720 | sdk-cli bypassPermissions | **170 readings** of measuring points in plant 43 were not performed in August 2026. These… | [q2-78512b20.jsonl](raw/claude-sonnet-5-5/q2-78512b20.jsonl) |
| 3 | claude-sonnet-5-5 | 2026-10-12 20:38:17 | 12 | 4 | 6 | 119092 | 1367 | 0.0875 | sdk-cli bypassPermissions | **19.98%** of the notifications in plant 64 in September 2026 had priority 3. That is 240… | [q3-d7e218d9.jsonl](raw/claude-sonnet-5-5/q3-d7e218d9.jsonl) |
| 4 | claude-sonnet-5-5 | 2026-10-12 20:38:32 | 11 | 4 | 6 | 114117 | 1121 | 0.0745 | sdk-cli bypassPermissions | The maintenance (material) cost for D-65-02-M-00230/04 in May 2026 was **9,119.14** net. … | [q4-070fe524.jsonl](raw/claude-sonnet-5-5/q4-070fe524.jsonl) |
| 5 | claude-sonnet-5-5 | 2026-10-12 20:38:46 | 9 | 4 | 5 | 115031 | 728 | 0.0724 | sdk-cli bypassPermissions | Notification 100022640 has user status **`REJC`**, which means rejected. The notification… | [q5-eb0db014.jsonl](raw/claude-sonnet-5-5/q5-eb0db014.jsonl) |
| 1 | claude-opus-5-5 | 2026-10-12 20:38:57 | 13 | 4 | 3 | 114637 | 960 | 0.1556 | sdk-cli bypassPermissions | **3 orders.** Criteria: - Table `ZW38_KG` (maintenance orders) - Plant is `32` - Work cen… | [q1-cca48154.jsonl](raw/claude-opus-5-5/q1-cca48154.jsonl) |
| 2 | claude-opus-5-5 | 2026-10-12 20:39:12 | 16 | 4 | 3 | 113476 | 1375 | 0.1595 | sdk-cli bypassPermissions | **170 readings were not performed in plant 43 in August 2026, covering 119 distinct measu… | [q2-4c796bf1.jsonl](raw/claude-opus-5-5/q2-4c796bf1.jsonl) |
| 3 | claude-opus-5-5 | 2026-10-12 20:39:30 | 13 | 4 | 3 | 114036 | 1028 | 0.1471 | sdk-cli bypassPermissions | **19.98%.** Of the 1,201 notifications created in plant 64 in September 2026, 240 have pr… | [q3-e75055c2.jsonl](raw/claude-opus-5-5/q3-e75055c2.jsonl) |
| 4 | claude-opus-5-5 | 2026-10-12 20:39:46 | 18 | 4 | 3 | 116953 | 1458 | 0.1687 | sdk-cli bypassPermissions | The material cost on **D-65-02-M-00230/04** in May 2026 was **9,119.14 net**. That's 18,0… | [q4-1b29e19d.jsonl](raw/claude-opus-5-5/q4-1b29e19d.jsonl) |
| 5 | claude-opus-5-5 | 2026-10-12 20:40:06 | 13 | 4 | 3 | 115575 | 878 | 0.1506 | sdk-cli bypassPermissions | The user status of notification 100022640 is **`REJC` (rejected)**. There is one row for … | [q5-4052e951.jsonl](raw/claude-opus-5-5/q5-4052e951.jsonl) |

## Answers in full

### Q1 — claude-haiku-5-5 — `37407087`

Prompt:

````text
how many orders with priority 1 there were in plant 32 in may 2025 for work center 3289?
````

Final reply:

````text
**3 orders** — priority 1, plant 32, work center 3289, created in May 2025.

Criteria:
- Table: `ZW38_KG` (maintenance orders)
- Plant `32` (`plant = '32'`)
- Priority 1 (immediately)
- Work center `3289` (`main_work_center = '3289'`)
- Period: `created_on` in May 2025, the default date for "in a month"

```sql
SELECT count(*) AS orders
FROM ZW38_KG
WHERE plant = '32' AND priority = 1 AND main_work_center = '3289'
  AND created_on >= DATE '2025-05-01' AND created_on < DATE '2025-06-01';
```
````

### Q2 — claude-haiku-5-5 — `c4fdeee9`

Prompt:

````text
how many points were not performed in plant 43 in august 2026?
````

Final reply:

````text
**170 readings, covering 119 distinct points, were not performed in plant 43 in August 2026.**

Criteria:
- **Table:** `IK17_KG` (measuring-point readings)
- **Plant 43:** the 2nd segment of `functional_location` is `43`
- **Not performed:** `text_code` is `Not performed` or `Not checked`
- **Period:** `created_on` falls in August 2026

SQL:

```sql
SELECT COUNT(*) AS readings, COUNT(DISTINCT point) AS points
FROM IK17_KG
WHERE split_part(functional_location, '-', 2) = '43'
  AND text_code IN ('Not performed', 'Not checked')
  AND created_on >= DATE '2026-08-01' AND created_on < DATE '2026-09-01'
```

The query was run with `uv run query.py`.
````

### Q3 — claude-haiku-5-5 — `15b4709c`

Prompt:

````text
what the precentage of notifications with priority 3 out of all notifications there were in plant 64 in september 2026?
````

Final reply:

````text
**19.98%** of plant 64's notifications created in September 2026 had priority 3: 240 of 1,201.

Criteria:
- Plant 64, read as a number, so `plant` = 64 only.
- Created in September 2026 (`created_on` from 2026-09-01 up to, not including, 2026-10-01).
- Priority 3 ("within a week") as a share of all notifications in that period, including the 21 with an empty priority.

Alternative reading: if the 21 notifications with an empty priority are left out of the whole, the share is 20.34% (240 of 1,180).

SQL, run with `uv run query.py`:

```sql
SELECT COUNT(*) AS total,
       COUNT(*) FILTER (WHERE try_cast(priority AS INTEGER) = 3) AS p3,
       ROUND(100.0 * COUNT(*) FILTER (WHERE try_cast(priority AS INTEGER) = 3) / COUNT(*), 2) AS pct
FROM ZIW28_KG
WHERE try_cast(plant AS INTEGER) = 64
  AND created_on >= DATE '2026-09-01' AND created_on < DATE '2026-10-01'
```

My first run used plant 65 by mistake; the figures above come from the corrected plant 64 query.
````

### Q4 — claude-haiku-5-5 — `7f64f467`

Prompt:

````text
what was the maintenance cost for functional location D-65-02-M-00230/04 in may 2026
````

Final reply:

````text
**May 2026 maintenance cost for D-65-02-M-00230/04: 9,119.14 (net)**

The net is made of 18,098.06 booked and −8,978.92 returned. The booked amount is order 1000335380 posted on 2026-05-03 (8,978.93) and again on 2026-05-25 (8,978.92). On 2026-05-25 the same order also has a −8,978.92 return, which cancels the second booking. Three small material postings on order 1000370723 on 2026-05-27 make up the rest.

Criteria:
- Table: `ZK22_KG` (material costs), since it is the only cost table in the reference files.
- Location: `functional_location` = `D-65-02-M-00230/04`, an exact match.
- Period: `date` in May 2026 (the table's only date).
- Measure: net `sum(cost)`, returns included.

Query:
```sql
SELECT count(*) AS rows, sum(cost) AS net_cost,
       sum(CASE WHEN cost > 0 THEN cost ELSE 0 END) AS booked,
       sum(CASE WHEN cost < 0 THEN cost ELSE 0 END) AS returned,
       min(date) AS first_date, max(date) AS last_date
FROM ZK22_KG
WHERE functional_location = 'D-65-02-M-00230/04'
  AND date >= DATE '2026-05-01' AND date < DATE '2026-06-01'
```
Result: 6 rows, net 9,119.14, booked 18,098.06, returned −8,978.92.

If "maintenance cost" means something broader, such as labour or order-level cost, this data does not hold it. I did not check the order table `ZW38_KG` for cost columns, so I can't say whether it holds one.
````

### Q5 — claude-haiku-5-5 — `6b10617a`

Prompt:

````text
what is the notification number 100022640 user status?
````

Final reply:

````text
The user status of notification 100022640 is **REJC**, which means rejected. The plant set this code, so it is the plant's own status.

Criteria:
- Table: `ZIW28_KG` (notifications)
- Notification number = 100022640

The query returned one row, so there is only one status row for this notification:

| Field | Value |
| --- | --- |
| notification_user_status | REJC (rejected) |
| notification_system_status | NOCO (notification completed, SAP) |
| order_system_status | NULL (no order attached) |
| notification_type | R1 |
| priority | 3 (within a week) |
| plant | 32 |
| functional_location | D-32-07-M-00705/00 |
| created_on | 2019-01-03 |

Query run:
```sql
SELECT * FROM ZIW28_KG WHERE CAST("notification" AS VARCHAR) LIKE '%100022640%'
```

Run with `uv run query.py` from the project folder.
````

### Q1 — claude-sonnet-5-5 — `ca7da2c5`

Prompt:

````text
how many orders with priority 1 there were in plant 32 in may 2025 for work center 3289?
````

Final reply:

````text
There were **3** priority 1 orders in plant 32 for work center 3289 in May 2025.

Criteria:
- Table `ZW38_KG` (maintenance orders), one row per order.
- `plant` = '32'.
- `main_work_center` = '3289'.
- `priority` = 1, which means "do it immediately".
- May 2025 is taken as the order's `created_on` date, in the range 2025-05-01 up to but not including 2025-06-01.

```sql
SELECT count(*) AS orders
FROM ZW38_KG
WHERE plant = '32'
  AND main_work_center = '3289'
  AND priority = 1
  AND created_on >= DATE '2025-05-01' AND created_on < DATE '2025-06-01'
```

I did not run the other possible readings, such as counting by release or scheduled-start date instead of creation date.
````

### Q2 — claude-sonnet-5-5 — `78512b20`

Prompt:

````text
how many points were not performed in plant 43 in august 2026?
````

Final reply:

````text
**170 readings** of measuring points in plant 43 were not performed in August 2026. These readings cover **119 distinct points**, because a point can be read more than once.

**Criteria**
- Table: `IK17_KG`, which holds measuring-point readings.
- Plant 43: the 2nd segment of `functional_location` is `43`.
- August 2026: `created_on` from 2026-08-01 up to, but not including, 2026-09-01.
- Not performed: `text_code` is `Not performed` or `Not checked`.
- A count is a count of rows, so the headline is 170 readings. Of these, 71 are `Not performed` and 99 are `Not checked`.

**Other reading:** if "points" means distinct measuring points, the answer is 119.

```sql
SELECT count(*) AS readings,
       count(DISTINCT point) AS points,
       count(*) FILTER (WHERE text_code='Not performed') AS np,
       count(*) FILTER (WHERE text_code='Not checked') AS nc
FROM IK17_KG
WHERE text_code IN ('Not performed','Not checked')
  AND split_part(functional_location,'-',2)='43'
  AND created_on >= DATE '2026-08-01' AND created_on < DATE '2026-09-01'
```
````

### Q3 — claude-sonnet-5-5 — `d7e218d9`

Prompt:

````text
what the precentage of notifications with priority 3 out of all notifications there were in plant 64 in september 2026?
````

Final reply:

````text
**19.98%** of the notifications in plant 64 in September 2026 had priority 3. That is 240 of 1,201 notifications.

**Criteria**
- Table: `ZIW28_KG` (notifications).
- Plant 64: `plant` read as the number 64. This leaves out department plants such as `64E`, and rows with an empty plant.
- September 2026: `created_on` from 2026-09-01 up to, but not including, 2026-10-01.
- Priority 3: "within a week" in `codes.md`.
- The whole is every notification in that plant and month, including the 21 with no priority. There are no duplicate notification numbers among them, so counting distinct numbers gives the same figures.

**Other reading:** if the whole is only notifications that have a priority (1,180), the share is 240 / 1,180 = **20.34%**.

```sql
SELECT count(*) AS total,
       count(*) FILTER (WHERE priority=3) AS p3,
       round(100.0*count(*) FILTER (WHERE priority=3)/count(*),2) AS pct,
       count(DISTINCT notification) AS d_total,
       count(DISTINCT notification) FILTER (WHERE priority=3) AS d_p3,
       count(*) FILTER (WHERE priority IS NOT NULL) AS with_prio,
       round(100.0*count(*) FILTER (WHERE priority=3)/count(*) FILTER (WHERE priority IS NOT NULL),2) AS pct_prio
FROM ZIW28_KG
WHERE try_cast(plant AS INTEGER)=64
  AND created_on >= DATE '2026-09-01' AND created_on < DATE '2026-10-01'
```
````

### Q4 — claude-sonnet-5-5 — `070fe524`

Prompt:

````text
what was the maintenance cost for functional location D-65-02-M-00230/04 in may 2026
````

Final reply:

````text
The maintenance (material) cost for D-65-02-M-00230/04 in May 2026 was **9,119.14** net.

The data has no currency column, so I can't state a currency.

| Part | Amount |
| --- | --- |
| Booked (cost > 0) | 18,098.06 |
| Returned (cost < 0) | −8,978.92 |
| **Net** | **9,119.14** |

**Criteria**
- **Table:** `ZK22_KG`, the material-cost table. It is the only table with costs.
- **Location:** exactly `D-65-02-M-00230/04`, so no other unit of equipment 00230 is included.
- **Period:** posting `date` from 2026-05-01 up to but not including 2026-06-01.
- **Measure:** net sum of `cost`, with returns kept in the sum. The result covers 6 rows.

**Other reading:** "maintenance cost" could also mean cost on the orders table (`ZW38_KG`). That table has no location or cost column, so it can't answer this.

```sql
SELECT count(*) AS n, sum(cost) AS net,
       sum(cost) FILTER (WHERE cost>0) AS booked,
       sum(cost) FILTER (WHERE cost<0) AS returned
FROM ZK22_KG
WHERE functional_location = 'D-65-02-M-00230/04'
  AND date >= DATE '2026-05-01' AND date < DATE '2026-06-01'
```
````

### Q5 — claude-sonnet-5-5 — `eb0db014`

Prompt:

````text
what is the notification number 100022640 user status?
````

Final reply:

````text
Notification 100022640 has user status **`REJC`**, which means rejected.

The notification table has one row for this number. The other status fields on it:
- **Notification system status:** `NOCO`, notification completed (SAP standard meaning, not verified on this system).
- **Order system status:** empty. The notification has no order attached.

Other details on the row: created 2019-01-03, type R1, priority 3 (within a week), functional location D-32-07-M-00705/00, plant 32.

**Criteria:** table `ZIW28_KG`, `notification` = '100022640', reading the `notification_user_status` column.

```sql
SELECT created_on, notification, notification_type, priority, notification_system_status,
       notification_user_status, order_system_status, functional_location, plant
FROM ZIW28_KG
WHERE notification = '100022640'
```
````

### Q1 — claude-opus-5-5 — `cca48154`

Prompt:

````text
how many orders with priority 1 there were in plant 32 in may 2025 for work center 3289?
````

Final reply:

````text
**3 orders.**

Criteria:
- Table `ZW38_KG` (maintenance orders)
- Plant is `32`
- Work center (`main_work_center`) is `3289`
- Priority is `1`, meaning "do it immediately"
- `created_on` falls in May 2025 (1 to 31 May). Creation date is the default when a question names a month.

```sql
SELECT count(*) AS orders
FROM ZW38_KG
WHERE plant = '32'
  AND main_work_center = '3289'
  AND priority = 1
  AND created_on >= DATE '2025-05-01' AND created_on < DATE '2025-06-01';
```

Work center 3289 has 63 priority-1 orders in total across all dates.
````

### Q2 — claude-opus-5-5 — `4c796bf1`

Prompt:

````text
how many points were not performed in plant 43 in august 2026?
````

Final reply:

````text
**170 readings were not performed in plant 43 in August 2026, covering 119 distinct measuring points.** A point can be read more than once in a month, which is why the two numbers differ.

| Result | Readings | Distinct points |
| --- | --- | --- |
| `Not checked` | 99 | 60 |
| `Not performed` | 71 | 59 |
| **Total** | **170** | **119** |

**Criteria:**
- Table: `IK17_KG` (measuring-point readings).
- Plant 43: the 2nd segment of `functional_location` is `43`.
- August 2026: `created_on` from 2026-08-01 up to, but not including, 2026-09-01.
- "Not performed": `text_code` is `'Not performed'` or `'Not checked'`. The project rules count both as not performed.

**The other way to read it:** if "not performed" means only the `Not performed` code, the answer is **71 readings, or 59 distinct points**.

```sql
SELECT count(*) AS readings,
       count(DISTINCT point) AS distinct_points,
       count(*) FILTER (WHERE text_code='Not performed') AS not_performed,
       count(*) FILTER (WHERE text_code='Not checked') AS not_checked,
       count(DISTINCT point) FILTER (WHERE text_code='Not performed') AS dp_np,
       count(DISTINCT point) FILTER (WHERE text_code='Not checked') AS dp_nc
FROM IK17_KG
WHERE split_part(functional_location, '-', 2) = '43'
  AND created_on >= DATE '2026-08-01' AND created_on < DATE '2026-09-01'
  AND text_code IN ('Not performed', 'Not checked');
```
````

### Q3 — claude-opus-5-5 — `e75055c2`

Prompt:

````text
what the precentage of notifications with priority 3 out of all notifications there were in plant 64 in september 2026?
````

Final reply:

````text
**19.98%.** Of the 1,201 notifications created in plant 64 in September 2026, 240 have priority 3 ("within a week").

**Criteria**
- Table: `ZIW28_KG` (notifications)
- Plant 64: rows where `plant` is 64 as a number. Department plants such as `64E` and `64I` are not included.
- September 2026: `created_on` from 2026-09-01 up to, but not including, 2026-10-01
- The whole is every notification that matches those filters, including the 21 that have no priority.

**The other reading:** if you leave out the 21 notifications with no priority, the whole is 1,180 and the share is **20.34%**.

**SQL**
```sql
SELECT count(*) AS total,
       count(*) FILTER (WHERE priority = 3) AS p3,
       count(priority) AS with_priority,
       round(100.0 * count(*) FILTER (WHERE priority = 3) / count(*), 2) AS pct_of_all,
       round(100.0 * count(*) FILTER (WHERE priority = 3) / count(priority), 2) AS pct_of_with_priority
FROM ZIW28_KG
WHERE try_cast(plant AS INTEGER) = 64
  AND created_on >= DATE '2026-09-01' AND created_on < DATE '2026-10-01'
```
````

### Q4 — claude-opus-5-5 — `1b29e19d`

Prompt:

````text
what was the maintenance cost for functional location D-65-02-M-00230/04 in may 2026
````

Final reply:

````text
The material cost on **D-65-02-M-00230/04** in May 2026 was **9,119.14 net**. That's 18,098.06 booked minus 8,978.92 returned, over 6 lines on 2 orders.

This is material cost only. The data holds no labour or service costs, so this isn't the full maintenance cost.

| Order | Date | Qty | Cost |
|---|---|---|---|
| 1000335380 | 2026-05-03 | 1 | 8,978.93 |
| 1000335380 | 2026-05-25 | 1 | 8,978.92 |
| 1000335380 | 2026-05-25 | −1 | −8,978.92 |
| 1000370723 | 2026-05-27 | 1 | 50.25 |
| 1000370723 | 2026-05-27 | 1 | 50.19 |
| 1000370723 | 2026-05-27 | 1 | 39.77 |

On order 1000335380, the 8,978.92 booked on 25 May was returned the same day. That leaves the 3 May booking of 8,978.93 as that order's actual cost. Order 1000370723 adds 140.21.

**Criteria**
- Table: `ZK22_KG` (material consumption on orders).
- `functional_location` is exactly `D-65-02-M-00230/04`.
- `date` (the posting date) falls in May 2026.
- The total is the net sum of `cost`, with returns included.

```sql
SELECT sum(cost) AS net_cost,
       sum(cost) FILTER (WHERE cost > 0) AS booked,
       sum(cost) FILTER (WHERE cost < 0) AS returned,
       count(*) AS lines,
       count(DISTINCT "order") AS orders
FROM ZK22_KG
WHERE functional_location = 'D-65-02-M-00230/04'
  AND date >= DATE '2026-05-01' AND date < DATE '2026-06-01';
```
````

### Q5 — claude-opus-5-5 — `4052e951`

Prompt:

````text
what is the notification number 100022640 user status?
````

Final reply:

````text
The user status of notification 100022640 is **`REJC` (rejected)**.

There is one row for this notification, so these are all the statuses it has:

| Field | Value | Meaning |
| --- | --- | --- |
| Notification user status | `REJC` | rejected |
| Notification system status | `NOCO` | notification completed |
| Order system status | empty | no order is attached |

It's an R1 notification with priority 3, created on 2019-01-03, for functional location `D-32-07-M-00705/00` in plant 32 under work center 3231.

**Criteria:** the notifications table (`ZIW28_KG`), where `notification` = `'100022640'`.

```sql
SELECT notification, notification_user_status, notification_system_status, order_system_status
FROM ZIW28_KG
WHERE notification = '100022640'
```
````
