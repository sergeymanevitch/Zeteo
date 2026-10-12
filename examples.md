---
layer: L3
type: reference
---

# Worked examples

Each was run with `uv run query.py` from this folder on 2026-10-12; the result is what it returned.
They show the shape of an answer, not answers to reuse: every new question gets its own query.

## 1. A count with a plant, a priority and a month

**Q:** How many urgent (24-hour) notifications were opened for plant 65 in March 2026?

Criteria: table `ZIW28_KG`; plant 65 by the plant rule (`plant` = 65; `65E`, `65I` left out); priority 2
("within 24 hours"); `created_on` in March 2026.

```sql
SELECT count(*) AS notifications
FROM ZIW28_KG
WHERE try_cast(plant AS INTEGER) = 65
  AND priority = 2
  AND created_on >= DATE '2026-03-01' AND created_on < DATE '2026-04-01';
```

**A:** 187. With the department plants `65E` and `65I` and the empty plants of locations in plant 65
added, the count would be 228; they are not plant 65.

## 2. A share

**Q:** What percentage of the readings taken in plant 32 in June 2026 were "Not OK"?

Criteria: table `IK17_KG`; plant = 2nd segment of `functional_location` = `32`; `created_on` in
June 2026; part `text_code = 'Not OK'`, whole all readings.

```sql
SELECT count(*) FILTER (WHERE text_code = 'Not OK') AS not_ok,
       count(*) AS readings,
       round(100.0 * count(*) FILTER (WHERE text_code = 'Not OK') / count(*), 2) AS pct
FROM IK17_KG
WHERE split_part(functional_location, '-', 2) = '32'
  AND created_on >= DATE '2026-06-01' AND created_on < DATE '2026-07-01';
```

**A:** 2.71 % — 114 of 4,202 readings.

## 3. A cost with returns

**Q:** What did material cost on D-64-02-M-0261F/04 in January 2021?

Criteria: table `ZK22_KG`; `functional_location` exactly `D-64-02-M-0261F/04`; `date` in
January 2021; net sum of `cost`, returns included.

```sql
SELECT sum(cost) AS net_cost,
       sum(cost) FILTER (WHERE cost > 0) AS booked,
       sum(cost) FILTER (WHERE cost < 0) AS returned,
       count(*) AS lines
FROM ZK22_KG
WHERE functional_location = 'D-64-02-M-0261F/04'
  AND date >= DATE '2021-01-01' AND date < DATE '2021-02-01';
```

**A:** 4,317.12 net, over 30 lines: 439,760,620.29 booked and −439,756,303.17 returned. Almost all
of it is one booking of 439,717,316.60 reversed the same day.

## 4. A status, decoded

**Q:** Where does notification 100381621 stand?

Criteria: table `ZIW28_KG`; `notification = '100381621'`; report every row with its three statuses
(notification system, user, order system) and decode them.

```sql
SELECT notification, created_on, priority, notification_system_status, notification_user_status,
       order_system_status
FROM ZIW28_KG
WHERE notification = '100381621';
```

**A:** Waiting for approval — user status `WFAP`, system status `OSNO` (outstanding notification);
no order yet (order system status empty); created 2026-06-24, priority 3 (within a week). The
number appears on two rows, identical in every status.

## 5. Distinct points against readings

**Q:** How many measuring points in area 02 of plant 65 were read in September 2026?

Criteria: table `IK17_KG`; `functional_location LIKE 'D-65-02-%'`; `created_on` in September 2026;
the question names points, and points are read more than once, so give both counts.

```sql
SELECT count(DISTINCT point) AS points, count(*) AS readings
FROM IK17_KG
WHERE functional_location LIKE 'D-65-02-%'
  AND created_on >= DATE '2026-09-01' AND created_on < DATE '2026-10-01';
```

**A:** 1,338 distinct points, read 2,226 times.

## 6. Two tables joined on the location

**Q:** Which equipment unit in plant 56 had the most notifications in 2025, and what did its
material cost that year?

Criteria: `ZIW28_KG` for notifications, plant 56 by the plant rule, `created_on` in 2025, units only
(location with `/`); `ZK22_KG` for cost on the same `functional_location`, `date` in 2025.

```sql
WITH top AS (
  SELECT functional_location, count(*) AS notifications
  FROM ZIW28_KG
  WHERE try_cast(plant AS INTEGER) = 56
    AND created_on >= DATE '2025-01-01' AND created_on < DATE '2026-01-01'
    AND functional_location LIKE '%/%'
  GROUP BY functional_location
  ORDER BY notifications DESC, functional_location
  LIMIT 1
)
SELECT top.functional_location, top.notifications, coalesce(sum(z.cost), 0) AS net_material_cost
FROM top
LEFT JOIN ZK22_KG z
  ON z.functional_location = top.functional_location
 AND z.date >= DATE '2025-01-01' AND z.date < DATE '2026-01-01'
GROUP BY top.functional_location, top.notifications;
```

**A:** `D-56-03-M-00630/00`, 59 notifications, 12,322.91 net material cost. The next unit has 49.

## 7. Orders by work center and type

**Q:** How many preventive maintenance orders did work center 6415 open in 2025?

Criteria: table `ZW38_KG`; `main_work_center = '6415'`; `order_type = 'RPM2'` (preventive);
`created_on` in 2025.

```sql
SELECT count(*) AS orders
FROM ZW38_KG
WHERE main_work_center = '6415' AND order_type = 'RPM2'
  AND created_on >= DATE '2025-01-01' AND created_on < DATE '2026-01-01';
```

**A:** 443.
