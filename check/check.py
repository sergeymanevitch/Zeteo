# /// script
# requires-python = ">=3.10"
# dependencies = ["duckdb==1.5.6"]
# ///
"""Hold Zeteo's documents to its data.

    uv run check/check.py              # from the repository root
    uv run check/check.py --root DIR   # read the documents from DIR; the data stays this repo's

Three checks. (a) and (b) query the four Parquet files loaded by query.py's own connect();
(c) reads the documents alone:

(a) EXAMPLES  every worked example of examples.md: its SQL is the SQL recorded here (a sha256
              prefix), it still returns the recorded rows, and the numbers its **A:** paragraph
              writes are those rows.
(b) FACTS     the stated counts of reference/*.md, data/CONTEXT.md, README.md § The data, the
              numbers of an **A:** paragraph its own SQL does not return, and the closed_on
              paragraph of results.md § What changed: the sentence is in the file, and a query
              returns what it says. Only what the registry lists is checked; a new number needs a
              new row.
(c) RULES     every SQL rule the documents repeat is written the same way everywhere.

One line per failure and exit 1; otherwise one summary line and exit 0. A query that fails is a
failure, reported, and the run goes on.
"""

import sys

sys.dont_write_bytecode = True

import argparse  # noqa: E402
import decimal  # noqa: E402
import hashlib  # noqa: E402
import importlib.util  # noqa: E402
import pathlib  # noqa: E402
import re  # noqa: E402

REPO = pathlib.Path(__file__).resolve().parent.parent

# The files the rules are looked for in, relative to the root.
RULE_FILES = ("CLAUDE.md", "identity.md", "rules.md", "examples.md", "reference/*.md")

# --- (a) the worked examples -------------------------------------------------------------------
# number: (sha256 prefix of the SQL block, the rows it returns as str(cell),
#          [(row, column, the form the **A:** paragraph writes it in)])
EXAMPLES = {
    1: ("06d609dadcce", [("187",)], [(0, 0, "187")]),
    2: ("41fca801eac4", [("114", "4202", "2.71")],
        [(0, 2, "2.71 %"), (0, 0, "114"), (0, 1, "4,202")]),
    3: ("6449f049dac5", [("4317.12", "439760620.29", "-439756303.17", "30")],
        [(0, 0, "4,317.12"), (0, 3, "30"), (0, 1, "439,760,620.29"), (0, 2, "\u2212439,756,303.17")]),
    4: ("767c20017e35",
        [("100381621", "2026-06-24", "3", "OSNO", "WFAP", "None")] * 2,
        [(0, 4, "`WFAP`"), (0, 3, "`OSNO`"), (0, 1, "2026-06-24"), (0, 2, "3")]),
    5: ("f78a27b1b842", [("1338", "2226")], [(0, 0, "1,338"), (0, 1, "2,226")]),
    6: ("e42b258bbc17", [("D-56-03-M-00630/00", "59", "12322.91")],
        [(0, 0, "`D-56-03-M-00630/00`"), (0, 1, "59"), (0, 2, "12,322.91")]),
    7: ("395df2d4fe1c", [("443",)], [(0, 0, "443")]),
    8: ("50b61e85bbf1", [("58",)], [(0, 0, "58")]),
    9: ("c84a77b8ac0e", [("1",)], [(0, 0, "1")]),
    10: ("05f9a6679f0a", [("157", "125", "20")], [(0, 0, "157"), (0, 1, "125"), (0, 2, "20")]),
}

# --- (b) the stated facts ----------------------------------------------------------------------
# (file, phrase, sql). A number the phrase states is marked {...}; the phrase without the braces
# must be in the file, and the braced values, in order, must be the query's one row. A phrase with
# no braces is a statement: its query returns one boolean, and it must be true.
FIRST = r"regexp_extract({}, '^\s*([^ ,]+)', 1)"
TECO = r"regexp_matches(system_status, '\bTECO\b')"
CMPL = r"regexp_matches(system_status, '\bCMPL\b')"
NCMP = r"regexp_matches(system_status, '\bNCMP\b')"
ZW38_PLANTS = ("SELECT (SELECT count(DISTINCT plant) FROM ZW38_KG) = 8 AND (SELECT count(*) FROM ZW38_KG "
               "WHERE plant IS NULL OR plant NOT IN ('13', '32', '43', '56', '64', '65', '88', '8100')) = 0")
WHOLE_PLANT = r"regexp_matches(functional_location, '^D-[^-]+$')"
OUTSIDE = "reading < lower_limit OR reading > upper_limit"


def _count(table, where):
    return f"SELECT count(*) FROM {table} WHERE {where}"


def _counts(*pairs):
    return "SELECT " + ", ".join(f"({_count(t, w)})" for t, w in pairs)


FACTS = [
    # reference/CONTEXT.md
    ("reference/CONTEXT.md", "| {729,886} | [ik17.md](ik17.md) |", "SELECT count(*) FROM IK17_KG"),
    ("reference/CONTEXT.md", "| {435,958} | [ziw28.md](ziw28.md) |", "SELECT count(*) FROM ZIW28_KG"),
    ("reference/CONTEXT.md", "| {547,801} | [zk22.md](zk22.md) |", "SELECT count(*) FROM ZK22_KG"),
    ("reference/CONTEXT.md", "| {70,241} | [zw38.md](zw38.md) |", "SELECT count(*) FROM ZW38_KG"),

    # data/CONTEXT.md
    ("data/CONTEXT.md", "| [IK17_KG.parquet](IK17_KG.parquet) | {729,886} |", "SELECT count(*) FROM IK17_KG"),
    ("data/CONTEXT.md", "| [ZIW28_KG.parquet](ZIW28_KG.parquet) | {435,958} |", "SELECT count(*) FROM ZIW28_KG"),
    ("data/CONTEXT.md", "| [ZK22_KG.parquet](ZK22_KG.parquet) | {547,801} |", "SELECT count(*) FROM ZK22_KG"),
    ("data/CONTEXT.md", "| [ZW38_KG.parquet](ZW38_KG.parquet) | {70,241} |", "SELECT count(*) FROM ZW38_KG"),

    # README.md, § The data
    ("README.md", "{435,958} notifications, {70,241} orders, {729,886} measuring-point readings and "
                  "{547,801} material bookings",
     "SELECT (SELECT count(*) FROM ZIW28_KG), (SELECT count(*) FROM ZW38_KG), "
     "(SELECT count(*) FROM IK17_KG), (SELECT count(*) FROM ZK22_KG)"),

    # reference/keys.md
    ("reference/keys.md", "({641} notifications name a whole plant, {589} of them `D-65`)",
     f"SELECT count(*) FILTER (WHERE {WHOLE_PLANT}), count(*) FILTER (WHERE functional_location = 'D-65') "
     "FROM ZIW28_KG"),
    ("reference/keys.md", "`plant` is `88` on {4,406} notifications at locations of plant 80 and {968} of "
                          "plant 81, and `70` on {1,451} at locations of plant 43",
     _counts(("ZIW28_KG", "plant = '88' AND split_part(functional_location, '-', 2) = '80'"),
             ("ZIW28_KG", "plant = '88' AND split_part(functional_location, '-', 2) = '81'"),
             ("ZIW28_KG", "plant = '70' AND split_part(functional_location, '-', 2) = '43'"))),
    ("reference/keys.md", "`plant` is empty on {3,887} notifications", _count("ZIW28_KG", "plant IS NULL")),
    ("reference/keys.md", "`010`, `06`, `1`, `4`, `5`, `20`, `69` and `71` are plants too",
     "SELECT count(DISTINCT plant) = 8 FROM ZIW28_KG "
     "WHERE plant IN ('010', '06', '1', '4', '5', '20', '69', '71')"),
    ("reference/keys.md", "`ZW38_KG` has plants `13`, `32`, `43`, `56`, `64`, `65`, `88` and `8100`", ZW38_PLANTS),
    ("reference/keys.md", "its `main_work_center` begins with the plant's digits (`4389` in plant 43), and "
                          "work center `8811` serves both `88` and `8100`",
     "SELECT (SELECT count(*) FROM ZW38_KG WHERE NOT starts_with(main_work_center, plant) "
     "AND NOT (plant = '8100' AND main_work_center = '8811')) = 0 "
     "AND (SELECT count(*) FROM ZW38_KG WHERE main_work_center = '4389' AND plant <> '43') = 0 "
     "AND (SELECT list(DISTINCT plant ORDER BY plant) FROM ZW38_KG WHERE main_work_center = '8811') "
     "= ['8100', '88']"),
    ("reference/keys.md", "ends in `21` (`1321`, `5621`, `8821` in `ZW38_KG`) and its instrumentation orders those "
                          "ending in `31` (`8831`)",
     "SELECT (SELECT list(DISTINCT main_work_center ORDER BY main_work_center) FROM ZW38_KG "
     "WHERE main_work_center LIKE '%21') = ['1321', '5621', '8821'] "
     "AND (SELECT list(DISTINCT main_work_center ORDER BY main_work_center) FROM ZW38_KG "
     "WHERE main_work_center LIKE '%31') = ['8831']"),
    ("reference/keys.md", "Only plants 13, 56 and 88 have such an electrical work center among their orders, and only "
                          "88 an instrumentation one",
     "SELECT (SELECT list(DISTINCT plant ORDER BY plant) FROM ZW38_KG WHERE main_work_center LIKE '%21') "
     "= ['13', '56', '88'] AND (SELECT list(DISTINCT plant) FROM ZW38_KG WHERE main_work_center LIKE '%31') = ['88']"),
    ("reference/keys.md", "of the notifications of `65E`, {6,223} of {6,494} have work center `6521`; `64E` {853} of "
                          "{880} `6421`; `43E` {187} of {224} `4321`; `32E` {171} of {230} `3221`; `88E` {7} of {16} "
                          "`8821`; of `65I`, {3,890} of {4,087} have `6531`; `43I` {552} of {604} `4331`; `32I` {356} "
                          "of {463} `3231`; `64I` {177} of {206} `6431`; `88I` {16} of {26} `8831`",
     "SELECT " + ", ".join(
         f"count(*) FILTER (WHERE plant = '{p}' AND main_work_center = '{w}'), count(*) FILTER (WHERE plant = '{p}')"
         for p, w in [("65E", "6521"), ("64E", "6421"), ("43E", "4321"), ("32E", "3221"), ("88E", "8821"),
                      ("65I", "6531"), ("43I", "4331"), ("32I", "3231"), ("64I", "6431"), ("88I", "8831")])
     + " FROM ZIW28_KG"),
    ("reference/keys.md", "work center `6521` is on {10,141} notifications, {3,503} of them on plant `65`",
     "SELECT count(*), count(*) FILTER (WHERE plant = '65') FROM ZIW28_KG WHERE main_work_center = '6521'"),
    ("reference/keys.md", "`IK17_KG` holds no location of discipline `E` or `I` (its disciplines are `M`, `K` and `N`)",
     "SELECT list(DISTINCT split_part(functional_location, '-', 4) ORDER BY split_part(functional_location, '-', 4)) "
     "= ['K', 'M', 'N'] FROM IK17_KG"),
    ("reference/keys.md", "`ZK22_KG` holds {23,948} rows of discipline `E` and {2,282} of `I`",
     "SELECT count(*) FILTER (WHERE split_part(functional_location, '-', 4) = 'E'), "
     "count(*) FILTER (WHERE split_part(functional_location, '-', 4) = 'I') FROM ZK22_KG"),
    ("reference/keys.md", "`\"order\"` links `IK17_KG` and `ZK22_KG` for {134} orders only",
     'SELECT count(DISTINCT i."order") FROM IK17_KG i JOIN ZK22_KG z ON i."order" = z."order"'),
    ("reference/keys.md", "`required_start_date` runs from {2008-05-01} to {2028-12-21}; {3} rows before 2000 "
                          "are not real dates",
     "SELECT min(required_start_date) FILTER (WHERE required_start_date >= DATE '2000-01-01'), "
     "max(required_start_date), count(*) FILTER (WHERE required_start_date < DATE '2000-01-01') FROM ZIW28_KG"),
    ("reference/keys.md", "`created_on` runs from {2019-01-01} to {2026-10-10}",
     "SELECT min(created_on), max(created_on) FROM ZIW28_KG"),
    ("reference/keys.md", "most often `created_on` ({26,419} of the {36,722} whose system status begins `NOPR`)",
     "SELECT count(*) FILTER (WHERE reference_date = created_on), count(*) FROM ZIW28_KG "
     f"WHERE {FIRST.format('notification_system_status')} = 'NOPR'"),
    ("reference/keys.md", "One row reads {9202-12-15}",
     "SELECT CASE WHEN count(*) = 1 THEN min(reference_date) END FROM ZIW28_KG "
     "WHERE reference_date > DATE '2100-01-01'"),
    ("reference/keys.md", "which is {70,238} of {70,241} rows",
     "SELECT count(*) FILTER (WHERE actual_end_date = scheduled_end_date), count(*) FROM ZW38_KG"),
    ("reference/keys.md", "no closing day on the {2,582} orders with neither `TECO` nor `CMPL`",
     _count("ZW38_KG", f"NOT {TECO} AND NOT {CMPL}")),
    ("reference/keys.md", "`created_on` runs from {2018-05-03} to {2026-10-08}",
     "SELECT min(created_on), max(created_on) FROM ZW38_KG"),
    ("reference/keys.md", "`IK17_KG` has one date, `created_on`, the day of the reading ({2019-08-08} to "
                          "{2026-10-08})",
     "SELECT min(created_on), max(created_on) FROM IK17_KG"),
    ("reference/keys.md", "`ZK22_KG` has one date, `date`, the day of the booking ({2018-01-01} to {2026-09-30})",
     "SELECT min(date), max(date) FROM ZK22_KG"),

    # reference/codes.md
    ("reference/codes.md", "Empty on {66,183} notifications and {33,187} orders",
     _counts(("ZIW28_KG", "priority IS NULL"), ("ZW38_KG", "priority IS NULL"))),
    ("reference/codes.md", "| 1 | immediately | {70,430} | {7,433} |",
     _counts(("ZIW28_KG", "priority = 1"), ("ZW38_KG", "priority = 1"))),
    ("reference/codes.md", "| 2 | within 24 hours | {58,000} | {2,496} |",
     _counts(("ZIW28_KG", "priority = 2"), ("ZW38_KG", "priority = 2"))),
    ("reference/codes.md", "| 3 | within a week | {121,640} | {11,233} |",
     _counts(("ZIW28_KG", "priority = 3"), ("ZW38_KG", "priority = 3"))),
    ("reference/codes.md", "| 4 | within a month | {89,177} | {10,089} |",
     _counts(("ZIW28_KG", "priority = 4"), ("ZW38_KG", "priority = 4"))),
    ("reference/codes.md", "| 5 | within three months | {16,601} | {2,945} |",
     _counts(("ZIW28_KG", "priority = 5"), ("ZW38_KG", "priority = 5"))),
    ("reference/codes.md", "| 6 | at the yearly shutdown | {13,927} | {2,858} |",
     _counts(("ZIW28_KG", "priority = 6"), ("ZW38_KG", "priority = 6"))),
    ("reference/codes.md", "| `RPM1` | maintenance (corrective) | {32,294} |", _count("ZW38_KG", "order_type = 'RPM1'")),
    ("reference/codes.md", "| `RPM2` | preventive maintenance | {37,902} |", _count("ZW38_KG", "order_type = 'RPM2'")),
    ("reference/codes.md", "| `RPM3` | safety-related work | {2} |", _count("ZW38_KG", "order_type = 'RPM3'")),
    ("reference/codes.md", "| `RPM7` | root cause analysis (RCA) | {33} |", _count("ZW38_KG", "order_type = 'RPM7'")),
    ("reference/codes.md", "| `1126` | the project department (Sergey, 2026-10-13) | {10} |",
     _count("ZW38_KG", "order_type = '1126'")),
    ("reference/codes.md", "| `R1` | corrective maintenance | {292,084} |", _count("ZIW28_KG", "notification_type = 'R1'")),
    ("reference/codes.md", "| `R2` | preventive maintenance | {80,833} |", _count("ZIW28_KG", "notification_type = 'R2'")),
    ("reference/codes.md", "| `R3` | root cause problem elimination | {976} |",
     _count("ZIW28_KG", "notification_type = 'R3'")),
    ("reference/codes.md", "| `R5` | an order raised on the technicians' preventive rounds in the field | {54,902} |",
     _count("ZIW28_KG", "notification_type = 'R5'")),
    ("reference/codes.md", "| `R6` | corrective maintenance, safety | {7,163} |",
     _count("ZIW28_KG", "notification_type = 'R6'")),
    ("reference/codes.md", "| `OK` | {593,958} |", _count("IK17_KG", "text_code = 'OK'")),
    ("reference/codes.md", "| `Performed` | {58,890} |", _count("IK17_KG", "text_code = 'Performed'")),
    ("reference/codes.md", "| `Not checked` | {50,695} |", _count("IK17_KG", "text_code = 'Not checked'")),
    ("reference/codes.md", "| `Not OK` | {21,902} |", _count("IK17_KG", "text_code = 'Not OK'")),
    ("reference/codes.md", "| `Not performed` | {4,047} |", _count("IK17_KG", "text_code = 'Not performed'")),
    ("reference/codes.md", "| `Handled` | {173} |", _count("IK17_KG", "text_code = 'Handled'")),
    ("reference/codes.md", "| `To be checked` | {42} |", _count("IK17_KG", "text_code = 'To be checked'")),
    ("reference/codes.md", "| `Yes` / `No` | {9} / {8} |",
     _counts(("IK17_KG", "text_code = 'Yes'"), ("IK17_KG", "text_code = 'No'"))),
    ("reference/codes.md", "| `Does not exist` | {1} |", _count("IK17_KG", "text_code = 'Does not exist'")),
    ("reference/codes.md", "| empty | {161} |", _count("IK17_KG", "text_code IS NULL")),
    ("reference/codes.md", "`h` hours, `°C`, `m/s`, `pcs` pieces, `L` litres, `mm`, `BAR`, `PSI`, `%`, `A`, `V`, "
                           "`Hz`, `g`, `Ω`, `N`, `RPM`, `N⋅m`, `m`. As exported, meanings from the plant",
     "SELECT list(DISTINCT units ORDER BY units) = list_sort(['h', '°C', 'm/s', 'pcs', 'L', 'mm', 'BAR', 'PSI', "
     "'%', 'A', 'V', 'Hz', 'g', 'Ω', 'N', 'RPM', 'N⋅m', 'm', '2MS', 'M3H', 'LMN']) "
     "FROM IK17_KG WHERE units IS NOT NULL"),
    ("reference/codes.md", "`2MS` millimetres per second squared ({3,555} readings), `M3H` cubic metres per hour "
                           "({2,172}), `LMN` litres per minute ({1,733}). Empty on {74} readings.",
     _counts(("IK17_KG", "units = '2MS'"), ("IK17_KG", "units = 'M3H'"), ("IK17_KG", "units = 'LMN'"),
             ("IK17_KG", "units IS NULL"))),
    ("reference/codes.md", "The first code is `PLAN` on {369,198} notifications and {65,890} orders",
     _counts(("ZIW28_KG", f"{FIRST.format('notification_user_status')} = 'PLAN'"),
             ("ZW38_KG", f"{FIRST.format('user_status')} = 'PLAN'"))),
    ("reference/codes.md", "it is empty on the {32,639} notifications that have no order",
     _count("ZIW28_KG", "order_system_status IS NULL")),
    ("reference/codes.md", "The first code is `NOCO`, `NOPR`, `NOPO`, `ATCO`, `OSNO` or `DLFL` on notifications, "
                           "and `TECO`, `CMPL`, `CRTD`, `REL` or `LKD` on orders.",
     f"SELECT (SELECT list_sort(list(DISTINCT {FIRST.format('notification_system_status')})) FROM ZIW28_KG) "
     "= list_sort(['NOCO', 'NOPR', 'NOPO', 'ATCO', 'OSNO', 'DLFL']) "
     f"AND (SELECT list_sort(list(DISTINCT {FIRST.format('system_status')})) FROM ZW38_KG) "
     "= list_sort(['TECO', 'CMPL', 'CRTD', 'REL', 'LKD'])"),
    ("reference/codes.md", "`notification_system_status`: {378,589} notifications.",
     _count("ZIW28_KG", f"{FIRST.format('notification_system_status')} = 'NOCO'")),
    ("reference/codes.md", "In the data: {62,493} orders with `TECO`, {5,024} with `CMPL` and `NCMP`, {142} with "
                           "`CMPL` alone;",
     _counts(("ZW38_KG", TECO), ("ZW38_KG", f"{CMPL} AND {NCMP}"), ("ZW38_KG", f"{CMPL} AND NOT {NCMP}"))),
    ("reference/codes.md", "no order holds `TECO` with either.",
     f"SELECT count(*) = 0 FROM ZW38_KG WHERE {TECO} AND ({CMPL} OR {NCMP})"),
    ("reference/codes.md", "`CMPL` is always the first code;",
     f"SELECT count(*) = 0 FROM ZW38_KG WHERE {CMPL} AND {FIRST.format('system_status')} <> 'CMPL'"),
    ("reference/codes.md", "`TECO` is first on {61,832} orders and second, after `LKD` (locked), on the other {661}",
     _counts(("ZW38_KG", f"{FIRST.format('system_status')} = 'TECO'"),
             ("ZW38_KG", r"regexp_matches(system_status, '^\s*LKD\s+TECO\b')"))),
    ("reference/codes.md", "the fragments `NMA`, `MAC`, `MA`, `MAN`, `N`, `NM`, `NT`, `SSA`, `SS`, `S`, `GMP`, `GM`, "
                           "`G`, `CSE`, `CS`, `C`, `M` are truncated codes",
     "WITH codes AS (SELECT DISTINCT trim(unnest(string_split(order_system_status, ','))) AS code FROM ZIW28_KG) "
     "SELECT count(*) = 17 FROM codes WHERE code IN ('NMA', 'MAC', 'MA', 'MAN', 'N', 'NM', 'NT', 'SSA', 'SS', "
     "'S', 'GMP', 'GM', 'G', 'CSE', 'CS', 'C', 'M')"),
    ("reference/codes.md", "`ZW38_KG.system_status` also holds a stray `*` on {16} orders",
     _count("ZW38_KG", "contains(system_status, '*')")),
    ("reference/codes.md", "on one of them glued to the code before it (`NTUP*`)",
     "SELECT count(*) = 1 AND bool_and(contains(system_status, 'NTUP*')) FROM ZW38_KG "
     "WHERE contains(system_status, '*') AND NOT regexp_matches(system_status, '(^|\\s)\\*(\\s|$)')"),

    # reference/ik17.md
    ("reference/ik17.md", "File `data/IK17_KG.parquet`, {729,886} rows.", "SELECT count(*) FROM IK17_KG"),
    ("reference/ik17.md", "{30,964} points, {12,846} orders, {1,589} functional locations",
     'SELECT count(DISTINCT point), count(DISTINCT "order"), count(DISTINCT functional_location) FROM IK17_KG'),
    ("reference/ik17.md", "a point belongs to one location",
     "SELECT max(n) = 1 FROM (SELECT count(DISTINCT functional_location) AS n FROM IK17_KG GROUP BY point)"),
    ("reference/ik17.md", "empty on {106,533} rows — a data-entry defect", _count("IK17_KG", '"order" IS NULL')),
    ("reference/ik17.md", "present on {151,779} rows only", _count("IK17_KG", "reading IS NOT NULL")),
    ("reference/ik17.md", "lower limit of the reading, where set ({641,855} rows)",
     _count("IK17_KG", "lower_limit IS NOT NULL")),
    ("reference/ik17.md", "upper limit of the reading, where set ({144,027} rows)",
     _count("IK17_KG", "upper_limit IS NOT NULL")),
    ("reference/ik17.md", "`TECO` closed as performed ({623,191}), `REL` still open ({162})",
     _counts(("IK17_KG", "order_status = 'TECO'"), ("IK17_KG", "order_status = 'REL'"))),
    ("reference/ik17.md", f"is `{OUTSIDE}` ({{13,274}} rows)", _count("IK17_KG", OUTSIDE)),

    # reference/ziw28.md
    ("reference/ziw28.md", "File `data/ZIW28_KG.parquet`, {435,958} rows.", "SELECT count(*) FROM ZIW28_KG"),
    ("reference/ziw28.md", "{435,956} distinct numbers", "SELECT count(DISTINCT notification) FROM ZIW28_KG"),
    ("reference/ziw28.md", "`100381621` and `300001379` occur twice, each as two identical rows",
     "SELECT (SELECT list(notification ORDER BY notification) FROM (SELECT notification FROM ZIW28_KG "
     "GROUP BY notification HAVING count(*) > 1)) = ['100381621', '300001379'] "
     "AND (SELECT count(*) FROM ZIW28_KG WHERE notification IN ('100381621', '300001379')) = 4 "
     "AND (SELECT count(*) FROM (SELECT DISTINCT * FROM ZIW28_KG "
     "WHERE notification IN ('100381621', '300001379'))) = 2"),
    ("reference/ziw28.md", "the scheduled end; {3} rows before 2000 are not real dates",
     _count("ZIW28_KG", "scheduled_end_date < DATE '2000-01-01'")),
    ("reference/ziw28.md", "urgency 1–6 ([codes.md](codes.md)); empty on {66,183} rows",
     _count("ZIW28_KG", "priority IS NULL")),
    ("reference/ziw28.md", "empty on the {32,639} notifications without an order",
     _count("ZIW28_KG", "order_system_status IS NULL")),
    ("reference/ziw28.md", "a whole plant on {641} rows", _count("ZIW28_KG", WHOLE_PLANT)),
    ("reference/ziw28.md", "{225} values, plain numbers (`3211`) or names (`64MAINT`, `43PUMP`); empty on {6} rows",
     "SELECT count(DISTINCT main_work_center), count(*) FILTER (WHERE main_work_center IS NULL) FROM ZIW28_KG"),
    ("reference/ziw28.md", "([keys.md](keys.md#dates)); {3} rows before 2000 are not real dates",
     _count("ZIW28_KG", "required_start_date < DATE '2000-01-01'")),
    ("reference/ziw28.md", "empty on {3,887} rows — use the plant rule", _count("ZIW28_KG", "plant IS NULL")),
    ("reference/ziw28.md", "one row reads {9202-12-15}",
     "SELECT CASE WHEN count(*) = 1 THEN min(reference_date) END FROM ZIW28_KG "
     "WHERE reference_date > DATE '2100-01-01'"),

    # reference/zk22.md
    ("reference/zk22.md", "File `data/ZK22_KG.parquet`, {547,801} rows.", "SELECT count(*) FROM ZK22_KG"),
    ("reference/zk22.md", "{121,072} orders, {5,938} functional locations.",
     'SELECT count(DISTINCT "order"), count(DISTINCT functional_location) FROM ZK22_KG'),
    ("reference/zk22.md", "negative on a return ({15,751} rows); 0 on {38,936} value-only rows",
     _counts(("ZK22_KG", "quantity < 0"), ("ZK22_KG", "quantity = 0"))),
    ("reference/zk22.md", "negative on a return or a value credit ({33,014} rows)", _count("ZK22_KG", "cost < 0")),
    ("reference/zk22.md", "order `1000097414` on 2021-01-26 holds +{439,717,316.60} and {\u2212439,717,316.60}",
     "SELECT max(cost), min(cost) FROM ZK22_KG WHERE \"order\" = '1000097414' AND date = DATE '2021-01-26'"),

    # reference/zw38.md
    ("reference/zw38.md", "File `data/ZW38_KG.parquet`, {70,241} rows.", "SELECT count(*) FROM ZW38_KG"),
    ("reference/zw38.md", "On the {2,582} other orders it is no closing day: {320} of them are later than "
                          "2026-10-13, up to {2027-11-18}",
     f"SELECT count(*), count(*) FILTER (WHERE closed_on > DATE '2026-10-13'), max(closed_on) FROM ZW38_KG "
     f"WHERE NOT {TECO} AND NOT {CMPL}"),
    ("reference/zw38.md", "the closing day on closed orders, `TECO` or `CMPL` without `NCMP`",
     f"SELECT count(*) = 0 FROM ZW38_KG WHERE ({TECO} OR ({CMPL} AND NOT {NCMP})) "
     "AND (closed_on IS NULL OR closed_on > DATE '2026-10-13')"),
    ("reference/zw38.md", "on `CMPL` with `NCMP`, which are closed without execution and not closed orders, "
                          "the day it was closed without execution",
     f"SELECT count(*) = 0 FROM ZW38_KG WHERE {CMPL} AND {NCMP} "
     "AND (closed_on IS NULL OR closed_on > DATE '2026-10-13')"),
    ("reference/zw38.md", "the day the order was released; empty on {6,936} rows",
     _count("ZW38_KG", "released_on IS NULL")),
    ("reference/zw38.md", "which is {70,238} of {70,241} rows",
     "SELECT count(*) FILTER (WHERE actual_end_date = scheduled_end_date), count(*) FROM ZW38_KG"),
    ("reference/zw38.md", "the real start of work; empty on {54,983} rows", _count("ZW38_KG", "actual_start_date IS NULL")),
    ("reference/zw38.md", "empty on {33,187} rows, mostly preventive orders",
     _count("ZW38_KG", "priority IS NULL")),
    ("reference/zw38.md", "mostly preventive orders",
     "SELECT count(*) FILTER (WHERE order_type = 'RPM2') * 2 > count(*) FROM ZW38_KG WHERE priority IS NULL"),
    ("reference/zw38.md", "equals `scheduled_start_date` on {70,239} of {70,241} rows",
     "SELECT count(*) FILTER (WHERE actual_start_date_2 = scheduled_start_date), count(*) FROM ZW38_KG"),
    ("reference/zw38.md", "the work center: {19} values", "SELECT count(DISTINCT main_work_center) FROM ZW38_KG"),
    ("reference/zw38.md", "the required end; empty on {31} rows", _count("ZW38_KG", "required_end_date IS NULL")),
    ("reference/zw38.md", "the plant: `13`, `32`, `43`, `56`, `64`, `65`, `88`, `8100`", ZW38_PLANTS),

    # examples.md: the numbers of an **A:** paragraph that its own SQL does not return
    ("examples.md", "the count would be {228}",
     "SELECT count(*) FROM ZIW28_KG WHERE (try_cast(plant AS INTEGER) = 65 OR plant IN ('65E', '65I') "
     "OR (plant IS NULL AND split_part(functional_location, '-', 2) = '65')) AND priority = 2 "
     "AND created_on >= DATE '2026-03-01' AND created_on < DATE '2026-04-01'"),
    ("examples.md", "Almost all of it is one booking of {439,717,316.60} reversed the same day.",
     "SELECT max(b.cost) FROM ZK22_KG b JOIN ZK22_KG r ON r.functional_location = b.functional_location "
     "AND r.date = b.date AND r.cost = -b.cost WHERE b.functional_location = 'D-64-02-M-0261F/04' "
     "AND b.date >= DATE '2021-01-01' AND b.date < DATE '2021-02-01' AND b.cost > 0"),
    ("examples.md", "The next unit has {49}.",
     "SELECT count(*) AS n FROM ZIW28_KG WHERE try_cast(plant AS INTEGER) = 56 "
     "AND created_on >= DATE '2025-01-01' AND created_on < DATE '2026-01-01' AND functional_location LIKE '%/%' "
     "GROUP BY functional_location ORDER BY n DESC, functional_location LIMIT 1 OFFSET 1"),
    ("examples.md", "Counted by the day they were opened (`created_on` in August 2026), {69}.",
     "SELECT count(*) FROM ZIW28_KG WHERE try_cast(plant AS INTEGER) = 13 "
     "AND created_on >= DATE '2026-08-01' AND created_on < DATE '2026-09-01'"),
    ("examples.md", "None of that work center's orders was created that day.",
     "SELECT count(*) = 0 FROM ZW38_KG WHERE plant = '32' AND main_work_center = '3215' "
     "AND created_on = DATE '2026-10-05'"),
    ("examples.md", "125 completed ({79.62} %)",
     f"SELECT 100.0 * count(*) FILTER (WHERE {TECO} OR ({CMPL} AND NOT {NCMP})) / count(*) FROM ZW38_KG "
     "WHERE plant = '43' AND created_on >= DATE '2026-05-01' AND created_on < DATE '2026-06-01'"),
    ("examples.md", "the other {12} are neither",
     f"SELECT count(*) FILTER (WHERE NOT {TECO} AND NOT {CMPL}) FROM ZW38_KG "
     "WHERE plant = '43' AND created_on >= DATE '2026-05-01' AND created_on < DATE '2026-06-01'"),
]

# results.md § What changed: the closed_on paragraph and what it means for B4
B4 = "plant = '32' AND closed_on >= DATE '2026-04-01' AND closed_on < DATE '2026-07-01'"
MEDIAN = "median(date_diff('day', created_on, closed_on))"
FACTS += [
    ("results.md", "a value running into the future on the {7,748} others", _count("ZW38_KG", f"NOT {TECO}")),
    ("results.md", "three groups of orders — `TECO` {62,493}, `CMPL` with `NCMP` {5,024}, `CMPL` alone {142}",
     _counts(("ZW38_KG", TECO), ("ZW38_KG", f"{CMPL} AND {NCMP}"), ("ZW38_KG", f"{CMPL} AND NOT {NCMP}"))),
    ("results.md", "`CMPL` alone 142, none later than 2026-10-13",
     f"SELECT count(*) = 0 FROM ZW38_KG WHERE ({TECO} OR {CMPL}) AND closed_on > DATE '2026-10-13'"),
    ("results.md", "no closing day on the {2,582} orders that are neither (first code `CRTD` {1,912}, "
                   "`REL` {669}, `LKD` {1}), {320} of them later than 2026-10-13, up to {2027-11-18}",
     f"SELECT count(*), count(*) FILTER (WHERE {FIRST.format('system_status')} = 'CRTD'), "
     f"count(*) FILTER (WHERE {FIRST.format('system_status')} = 'REL'), "
     f"count(*) FILTER (WHERE {FIRST.format('system_status')} = 'LKD'), "
     "count(*) FILTER (WHERE closed_on > DATE '2026-10-13'), max(closed_on) "
     f"FROM ZW38_KG WHERE NOT {TECO} AND NOT {CMPL}"),
    ("results.md", "{357} orders with `TECO`, median {49} days",
     f"SELECT count(*), {MEDIAN} FROM ZW38_KG WHERE {B4} AND {TECO}"),
    ("results.md", "none with `CMPL` alone;",
     f"SELECT count(*) = 0 FROM ZW38_KG WHERE {B4} AND {CMPL} AND NOT {NCMP}"),
    ("results.md", "{2} with `CMPL` and `NCMP`, which make {359} with the same median, {49}",
     f"SELECT count(*) FILTER (WHERE {CMPL} AND {NCMP}), count(*), {MEDIAN} FROM ZW38_KG "
     f"WHERE {B4} AND ({TECO} OR {CMPL})"),
    ("results.md", "the {24} orders that are neither and carry a Q2 `closed_on`",
     _count("ZW38_KG", f"{B4} AND NOT {TECO} AND NOT {CMPL}")),
    ("results.md", "B4's key, {357}, is confirmed and does not move: {2} orders of plant 32 with a Q2 "
                   "`closed_on` are closed without execution",
     f"SELECT count(*) FILTER (WHERE {TECO} OR ({CMPL} AND NOT {NCMP})), "
     f"count(*) FILTER (WHERE {CMPL} AND {NCMP}) FROM ZW38_KG WHERE {B4}"),
]

# --- (c) the repeated SQL rules ----------------------------------------------------------------
# (name, loose anchor, canonical text, {file: occurrences it must hold at least}).
# In the canonical text {N} is a plant number, {FIELD} a column name and {CODE} a status code; the
# rest must stand exactly, once whitespace is collapsed, and be followed by the end of a clause.
RULES = [
    ("the plant as a number", r"(?:try_)?cast\s*\(\s*plant\b|\bplant\s*::", "try_cast(plant AS INTEGER) = {N}",
     {"reference/keys.md": 1, "examples.md": 3}),
    ("the plant of a location", r"split_part\s*\(", "split_part(functional_location, '-', 2) = '{N}'",
     {"reference/keys.md": 1, "examples.md": 1}),
    ("a completed order", r"regexp_matches\s*\([^()]*TECO",
     r"regexp_matches(system_status, '\bTECO\b') OR (regexp_matches(system_status, '\bCMPL\b') "
     r"AND NOT regexp_matches(system_status, '\bNCMP\b'))",
     {"reference/codes.md": 1, "examples.md": 1}),
    ("the first code", r"regexp_extract\s*\(", r"regexp_extract({FIELD}, '^\s*([^ ,]+)', 1) = '{CODE}'",
     {"reference/codes.md": 2}),
]


_QUERY = []


def load_query():
    """query.py itself, loaded once from this repository: its connect() loads the data, its
    one_read() decides whether an example's SQL may run."""
    if not _QUERY:
        spec = importlib.util.spec_from_file_location("zeteo_query", REPO / "query.py")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        _QUERY.append(module)
    return _QUERY[0]


def connect():
    return load_query().connect()


def collapse(text):
    return re.sub(r"\s+", " ", text).strip()


def normalise(written):
    return (written.replace(",", "").replace("\u2212", "-").replace("`", "").replace(" %", "")).strip()


def read(root, name):
    path = root / name
    try:
        return path.read_text(encoding="utf-8")
    except OSError as error:
        return error


def run_sql(con, sql):
    return con.execute(sql.strip().rstrip(";")).fetchall()


def agrees(written, measured):
    """Whether a value written in a document says what the query measured."""
    if measured is None:
        return False
    value = normalise(written)
    try:
        if re.fullmatch(r"-?\d+", value):
            return decimal.Decimal(str(measured)) == decimal.Decimal(value)
        if re.fullmatch(r"-?\d+\.\d+", value):
            places = decimal.Decimal(1).scaleb(-len(value.split(".")[1]))
            rounded = decimal.Decimal(str(measured)).quantize(places, rounding=decimal.ROUND_HALF_UP)
            return rounded == decimal.Decimal(value)
    except decimal.InvalidOperation:
        return False
    return str(measured) == value


def written_in(form, paragraph):
    """Whether a form stands in a paragraph as a whole value, not as part of a longer number."""
    pattern = r"(?<![0-9A-Za-z])(?<![0-9][.,])" + re.escape(form) + r"(?![0-9A-Za-z])(?![.,][0-9])"
    return re.search(pattern, paragraph) is not None


def stands_in(phrase, text):
    """Whether a phrase stands in a text on its own: no letter, digit or '.' just before it, and,
    when it ends in a digit, no letter or digit just after it, as written_in() reads a number."""
    pattern = r"(?<![0-9A-Za-z.])(?<![0-9],)" + re.escape(phrase)
    if phrase[-1:].isdigit():
        pattern += r"(?![0-9A-Za-z])(?![.,][0-9])"
    return re.search(pattern, text) is not None


# --- (a) ---------------------------------------------------------------------------------------

def parse_examples(text):
    """{number: (the SQL block, the **A:** paragraph whitespace-collapsed)}, and the numbers that
    head more than one section."""
    found = {}
    twice = []
    sections = re.split(r"^## (\d+)\. .*$", text, flags=re.M)
    for number, body in zip(sections[1::2], sections[2::2]):
        sql = re.search(r"^```sql\n(.*?)^```", body, flags=re.S | re.M)
        answer = re.search(r"^\*\*A:\*\*(.*?)(?:\n\s*\n|\Z)", body, flags=re.S | re.M)
        if int(number) in found:
            twice.append(int(number))
        found[int(number)] = (sql.group(1) if sql else None, collapse(answer.group(1)) if answer else None)
    return found, twice


def check_examples(root, con):
    failures = []
    text = read(root, "examples.md")
    if isinstance(text, Exception):
        return [f"examples.md: cannot be read: {text}"], 0
    found, twice = parse_examples(text)
    for number in sorted(set(twice)):
        failures.append(f"examples.md: example {number} appears twice")
    for number in sorted(set(found) - set(EXAMPLES)):
        failures.append(f"examples.md: example {number} is not in check.py's EXAMPLES")
    for number, (digest, rows, pairs) in EXAMPLES.items():
        where = f"examples.md: example {number}"
        if number not in found:
            failures.append(f"{where}: not found")
            continue
        sql, answer = found[number]
        if sql is None or answer is None:
            failures.append(f"{where}: no ```sql block or no **A:** paragraph")
            continue
        if hashlib.sha256(sql.encode("utf-8")).hexdigest()[:len(digest)] != digest:
            failures.append(f"{where}: the SQL of example {number} changed; update EXAMPLES in check.py "
                            "once its result is checked")
        statement = sql.strip().rstrip(";").strip()
        measured = None
        if not load_query().one_read(con, statement):
            failures.append(f"{where}: its SQL is not one statement that reads, as query.py requires; not run")
        else:
            try:
                measured = [tuple(str(cell) for cell in row) for row in run_sql(con, statement)]
            except Exception as error:  # a query error is a failure, not a crash
                failures.append(f"{where}: its SQL failed: {error}")
        if measured is not None and measured != rows:
            failures.append(f"{where}: its SQL returns {measured}, recorded {rows}")
        for row, column, form in pairs:
            if not written_in(form, answer):
                failures.append(f"{where}: {form!r} is not in its **A:** paragraph")
            elif normalise(form) != rows[row][column]:
                failures.append(f"{where}: {form!r} is written, the recorded cell is {rows[row][column]!r}")
    return failures, len(EXAMPLES)


# --- (b) ---------------------------------------------------------------------------------------

def check_facts(root, con, facts=None):
    failures = []
    texts = {}
    for name, phrase, sql in FACTS if facts is None else facts:
        if name not in texts:
            text = read(root, name)
            texts[name] = text if isinstance(text, Exception) else collapse(text)
        text = texts[name]
        plain = collapse(phrase.replace("{", "").replace("}", ""))
        if isinstance(text, Exception):
            line = f"{name}: cannot be read: {text}"
            if line not in failures:
                failures.append(line)
            continue
        if not stands_in(plain, text):
            failures.append(f"{name}: phrase not found: {plain}")
            continue
        stated = re.findall(r"\{([^{}]*)\}", phrase)
        try:
            rows = run_sql(con, sql)
        except Exception as error:  # a query error is a failure, not a crash
            failures.append(f"{name}: the query for '{plain}' failed: {error}")
            continue
        if not stated:
            if rows != [(True,)]:
                failures.append(f"{name}: does not hold: '{plain}' (the query returned {rows})")
            continue
        if len(rows) != 1 or len(rows[0]) != len(stated):
            failures.append(f"{name}: '{plain}': the query returned {rows}, expected one row of {len(stated)}")
            continue
        if not all(agrees(w, m) for w, m in zip(stated, rows[0])):
            measured = ", ".join(str(m) for m in rows[0])
            failures.append(f"{name}: '{plain}': stated {', '.join(stated)}; measured {measured}")
    return failures, len(FACTS if facts is None else facts)


# --- (c) ---------------------------------------------------------------------------------------

# What may follow a rule: the end of a line or of the text, AND, a closing parenthesis, a semicolon,
# a SQL comment, or the backtick that closes inline code.
CLAUSE_END = r"[ \t]*(?:$|AND\b|\)|;|--|`)"


def rule_pattern(canonical):
    """The canonical text with its variables, any run of white space where it has one space, and
    the end of a clause after it."""
    parts = re.split(r"(\{N\}|\{FIELD\}|\{CODE\}| )", canonical)
    pieces = {"{N}": r"\d+", "{FIELD}": r"\w+", "{CODE}": r"[A-Z]+", " ": r"\s+"}
    return re.compile("".join(pieces.get(p, re.escape(p)) for p in parts) + CLAUSE_END, re.M)


def check_rules(root):
    failures = []
    checked = 0
    names = []
    for pattern in RULE_FILES:
        names += sorted(p.relative_to(root).as_posix() for p in root.glob(pattern) if p.is_file())
    texts = {}
    for name in names:
        text = read(root, name)
        if isinstance(text, Exception):
            failures.append(f"{name}: cannot be read: {text}")
            text = ""
        texts[name] = text
    for rule, anchor, canonical, required in RULES:
        exact = rule_pattern(canonical)
        width = len(canonical) + 15
        for name in names:
            found = 0
            for match in re.finditer(anchor, texts[name]):
                found += 1
                checked += 1
                if not exact.match(texts[name], match.start()):
                    snippet = collapse(texts[name][match.start():match.start() + 3 * width])[:width]
                    failures.append(f"{name}: {rule} is written differently: '{snippet}' "
                                    f"(the rule is '{canonical}')")
            if found < required.get(name, 0):
                failures.append(f"{name}: {rule} found {found} times, expected at least {required[name]}")
        for name in sorted(set(required) - set(names)):
            failures.append(f"{name}: not found, and {rule} is expected in it")
    return failures, checked


def run(root, con):
    """Every failure, and the summary line printed when there is none."""
    root = pathlib.Path(root).resolve()
    example_failures, examples = check_examples(root, con)
    fact_failures, facts = check_facts(root, con)
    rule_failures, rules = check_rules(root)
    summary = (f"check: all hold: {examples} examples, {facts} facts, "
               f"{rules} occurrences of {len(RULES)} repeated SQL rules")
    return example_failures + fact_failures + rule_failures, summary


def main(argv=None):
    parser = argparse.ArgumentParser(description="Hold Zeteo's documents to its data.")
    parser.add_argument("--root", default=str(REPO), help="read the documents from DIR (default: this repository)")
    args = parser.parse_args(argv)
    failures, summary = run(args.root, connect())
    for line in failures:
        print(line)
    if failures:
        return 1
    print(summary)
    return 0


if __name__ == "__main__":
    sys.exit(main())
