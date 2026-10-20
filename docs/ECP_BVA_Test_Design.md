# Test Design Notes (ECP + BVA) - project: `humanize`

Project: https://github.com/python-humanize/humanize (Python, MIT). Three modules under test.
Technique key: **ECP** = Equivalence Class Partitioning, **BVA** = Boundary Value Analysis, **NEG** = invalid input.

## 1. `humanize.number` (Member 1) - `tests/test_number.py`
| Function | Valid classes (ECP) | Boundaries (BVA) | Invalid (NEG) |
|---|---|---|---|
| `intcomma(v, ndigits)` | +int, -int, numeric string, float, huge int | -1000, -999, 0, 999, 1000, 1001 | `"abc"`, `None` -> returned as text |
| `intword(v, format)` | thousand, million, billion, negative, string, float, custom format | 0, 999, 1e3, 1e6, 1e9, 1e12 | `"abc"`, `None` |
| `ordinal(v)` | st / nd / rd / th, 21st, 102nd | 0, 10-14 (teen exception), 111, 112 | `"x"`, `None`; negative `-1` -> `-1th` (observed behaviour) |
| `apnumber(v)` | int, float, numeric string | -1, 0, 1, 9, 10, 11 (words only for 0-9) | `"x"`, `None` |
| `fractional(v)` | proper, mixed, whole, string | 0 -> `0/1` (observed behaviour) | `"a"`, `None` |
| `scientific(v, precision)` | +exp, -exp, exp 0, custom precision | 0, 1 | `"x"` |

## 2. `humanize.filesize` (Member 2) - `tests/test_filesize.py`
| Mode | ECP | BVA | NEG |
|---|---|---|---|
| decimal (kB, MB, ...) | bytes, kB, MB, GB, TB, numeric string, negative, custom `format` | 0, 1 (singular "Byte"), 2, 999, 1000, 1001, 999999 (rolls to MB), 1e6 | `None` -> TypeError, `"abc"` -> ValueError |
| `binary=True` (KiB...) | 1000 stays in Bytes | 0, 1023, 1024, 1025, 1024^2, 1024^3 | - |
| `gnu=True` (K, M, G) | B, K, M, G | 0, 1023, 1024 | - |

## 3. `humanize.time` (Member 2) - `tests/test_time.py`
| Function | ECP | BVA | NEG |
|---|---|---|---|
| `naturaldelta` | seconds, minutes, hours, days, months, years; `months=False`; int input; negative delta | 0, 0.5s, 1s, 2s, 59s, 60s, 3600s, 86400s | - |
| `naturaltime` | past vs future, seconds/hours/days, `datetime` input | 0 ("now"), +-1s, 60s | - |
| `naturalday` | other days -> `Mon DD` | yesterday / today / tomorrow | `"x"` returned as text |
| `naturaldate` | within a year (no year), tomorrow | +-366 days & 800 days (year appears) | - |
| `precisedelta` | min+sec, h+m+s, y+d, d+h+m, `minimum_unit`, `suppress` | 0 delta, ms precision | - |

## Data-driven set (Task 3) - `data/*.csv` -> `tests/test_csv_driven.py` and `Test_Cases.xlsx`
26 rows (10 number, 8 filesize, 8 time) with IDs N01-N10, F01-F08, T01-T08.
