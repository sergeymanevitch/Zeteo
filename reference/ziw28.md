---
layer: L3
type: reference
---

# ZIW28_KG — maintenance notifications

File `data/ZIW28_KG.parquet`, 435,958 rows. One row is one notification: a request for maintenance
work on a functional location. 435,956 distinct numbers: `100381621` and `300001379` occur twice,
each as two identical rows — count `DISTINCT notification` when the question is about
notifications as such and the two counts differ.

| Column | Type | Holds |
| --- | --- | --- |
| `created_on` | DATE | the day the notification was opened; the date for "opened in" ([keys.md](keys.md#dates)) |
| `scheduled_end_date` | DATE | the scheduled end; 3 rows before 2000 are not real dates |
| `notification` | VARCHAR | the notification number |
| `notification_type` | VARCHAR | the type of order it is for: `R1` corrective, `R2` preventive, `R3` root cause problem elimination, `R5` from the technicians' preventive rounds, `R6` corrective, safety ([codes.md](codes.md)) |
| `priority` | INTEGER | urgency 1–6 ([codes.md](codes.md)); empty on 66,183 rows |
| `notification_system_status` | VARCHAR | SAP system status of the notification, codes separated by spaces |
| `notification_user_status` | VARCHAR | the plant's status of the notification, codes separated by commas |
| `order_system_status` | VARCHAR | system status of the order attached, codes separated by commas; empty on the 32,639 notifications without an order; truncated in the export ([codes.md](codes.md)) |
| `functional_location` | VARCHAR | where the work is ([keys.md](keys.md)); a whole plant on 641 rows |
| `main_work_center` | VARCHAR | the work center responsible: 225 values, plain numbers (`3211`) or names (`64MAINT`, `43PUMP`); empty on 6 rows |
| `required_start_date` | DATE | the day the work is required to start, used to plan it; the default for "notifications in a month" ([keys.md](keys.md#dates)); 3 rows before 2000 are not real dates |
| `plant` | VARCHAR | the plant in charge, which may differ from the location's ([keys.md](keys.md#plant)); a department letter (`65E`, `65I`) marks a synthetic plant that is left out of plant 65; empty on 3,887 rows — use the plant rule of [keys.md](keys.md#plant) |
| `reference_date` | DATE | the day the work was reported performed; set again when the notification is closed, so on one not yet completed it is no such day ([keys.md](keys.md#dates)); one row reads 9202-12-15 |
