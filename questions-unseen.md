# Questions the author did not write

Thirty questions written on 2026-10-13 by a separate Claude Opus session that read only the data
and its column names — not the folder, the five questions' runs or their results. Group A tests
choice points the folder handles, group B the gaps found on 2026-10-13, group C the writer's own
choice. The questions were committed alone (`4866ad0`) before either arm was asked them. "Last
month" and "this year" are read from 2026-10-13.

The expected answers were computed on 2026-10-13, before either arm was asked, by query, with the
folder's definitions — the meanings the data's owner gave — so they favour an answer that reads
the data as the folder does. Where a question reads two ways, the other reading follows its
number. Sergey checks them.

## A1

Q: How many work orders did plant 88 release in July 2026?
A: 307

## A2

Q: How many notifications did plant 64E raise in August 2026?
A: 57 opened (`created_on`); 39 by `required_start_date`

## A3

Q: Of the notifications plant 64 opened in July 2026, how many are being executed right now?
A: 5 (`EXE` is the current user status); 130 have `EXE` anywhere in it

## A4

Q: How many measuring points got readings on D-65-02-M-00237/00 in July 2026?
A: 147 readings of 46 distinct points

## A5

Q: Of the orders plant 56 created in 2026, how many are completed?
A: 689 of 731 (none closed without the work done)

## A6

Q: How many readings in plant 32 were out of limits in May 2026?
A: 159

## A7

Q: What did we spend on materials for D-32-07-M-00100/00 in August 2026?
A: −66,900.15 net: 45,519.45 booked, −112,419.60 returned

## A8

Q: What percentage of plant 43's notifications in Q1 2026 were R1?
A: 51.51 % (1,653 of 3,209, by `required_start_date`); 53.34 % of 3,099 by `created_on`

## A9

Q: How many electrical notifications did plant 65 raise in Q2 2026?
A: 51 (plant 65, discipline `E`); 171 under the department plant `65E` — Sergey to confirm which

## A10

Q: Order 2000100534 logged some Not OK readings. What did it spend on materials?
A: 19.13 (one booking, 2026-08-31); the order has 12 readings, 2 Not OK

## B1

Q: How many of plant 88's September 2026 notifications are completed?
A: 166 of 427 (`NOCO` first, by `required_start_date`); 131 of 409 by `created_on`

## B2

Q: Is notification 100377365 finished?
A: No: system status `NOPR ORAS`, in process (the user status `PLND,COMP` holds `COMP`, but not first)

## B3

Q: On average, how many days did plant 43 orders created in 2025 wait between creation and release?
A: 44.77 days on average (median 22), over the 958 of 1,020 orders that were released

## B4

Q: What's the median number of days from creation to closing for plant 32 orders closed in Q2 2026?
A: 49 days, over 357 orders with `TECO` closed in Q2 2026

## B5

Q: How many notifications did plant 65 open last month?
A: 891 (September 2026, `created_on`)

## B6

Q: Plant 43 notifications this year so far against the same months last year: up or down, and by how much?
A: Down 297 (−2.96 %): 9,738 against 10,035, 1 January to 13 October, by `required_start_date`; up 276 (+2.80 %), 10,123 against 9,847, by `created_on`

## B7

Q: Of the notifications plant 32 opened in March 2026, how many are still open?
A: 169 of 719 (`NOPR` 142, `NOPO` 20, `ATCO` 7)

## B8

Q: How many notifications are still outstanding for work center 6531?
A: 382 (`NOPR` 261, `NOPO` 105, `ATCO` 13, `OSNO` 3) of 20,859

## B9

Q: What share of plant 88's 2025 orders were finished on time?
A: Cannot be answered: no column says when an order was due against when it was done

## B10

Q: What did labour cost on D-64-04-M-0361E/03 in 2026?
A: Cannot be answered: the data holds material cost only, no labour

## C1

Q: Top 5 functional locations by number of notifications in plant 64 for 2026?
A: D-64-04-M-0361E/03 255, D-64-05-M-0515E/00 242, D-64-05-M-0515C/01 175, D-64-03-M-0375B/01 174, then D-64-10-E-01000/00 and D-64-03-M-0375F/04 tied at 171 (by `required_start_date`)

## C2

Q: Which work center in plant 88 created the most orders in Q3 2026, and how many?
A: 8811, 726 orders

## C3

Q: Give me plant 43's notifications month by month, January to September 2026.
A: 1,129 · 945 · 1,135 · 879 · 1,336 · 1,130 · 958 · 1,020 · 865 (by `required_start_date`)

## C4

Q: Break down plant 65's August 2026 notifications by type.
A: R1 520, R2 201, R5 141, R6 34 (896, by `required_start_date`)

## C5

Q: Did plant 32 or plant 65 log more priority 1 notifications in 2026?
A: Plant 65: 1,106 against 1,010

## C6

Q: For D-64-04-M-0361E/03: how many notifications this year, and how much spent on materials?
A: 255 notifications (268 by `created_on`); 412,889.10 net on materials (429,516.97 booked, −16,627.87 returned)

## C7

Q: Which functional location in plant 43 had the highest material cost in Q3 2026?
A: D-43-07-O-07250/01, 354,241.00

## C8

Q: RPM1 vs RPM2: how many of each did plant 13 open in 2026?
A: RPM1 190, RPM2 432

## C9

Q: What was the highest temperature reading on D-65-03-M-00330/00 this year?
A: 67 °C, on 2026-07-28

## C10

Q: How many notifications did work center 8130 log in June 2026?
A: 1 notification, stored on 2 identical rows (100381621)
