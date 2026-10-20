# Summary Report - Assignment 3: Unit Test Automation for `humanize`

Project under test: [python-humanize/humanize](https://github.com/python-humanize/humanize) (Python, MIT).
Test framework: `pytest` with `pytest-xdist` (parallel), `pytest-cov` (coverage), `pytest-html` (HTML report), `tox` (multi-env).

## 1. Scope
| Module | Functions under test | Test file | Owner |
|---|---|---|---|
| `humanize.number` | `intcomma`, `intword`, `ordinal`, `apnumber`, `fractional`, `scientific` | `tests/test_number.py` | Member 1 |
| `humanize.filesize` | `naturalsize` (decimal, `binary=True`, `gnu=True`, `format`) | `tests/test_filesize.py` | Member 2 |
| `humanize.time` | `naturaldelta`, `naturaltime`, `naturalday`, `naturaldate`, `precisedelta` | `tests/test_time.py` | Member 2 |
| all three | data-driven cases read from `data/*.csv` | `tests/test_csv_driven.py` | Member 1 + 2 |

## 2. Test design
Cases were derived with **Equivalence Class Partitioning (ECP)**, **Boundary Value Analysis (BVA)** and
**negative (invalid input)** testing. The class/boundary tables are in `docs/ECP_BVA_Test_Design.md`.
Each test is tagged with a pytest marker for its technique (`ecp`, `bva`, `negative`), plus `smoke`,
`datadriven`, and a module marker (`number`, `filesize`, `time`). Every test is also tagged `regression`.

## 3. Test counts (192 tests, all passing)
| File | Tests |
|---|---|
| `tests/test_number.py` | 78 |
| `tests/test_filesize.py` | 35 |
| `tests/test_time.py` | 53 |
| `tests/test_csv_driven.py` (26 CSV rows: N01-N10, F01-F08, T01-T08) | 26 |
| **Total** | **192** |

| Group (marker) | Tests | | Module (marker) | Tests |
|---|---|---|---|---|
| `smoke` | 14 | | `number` | 88 |
| `ecp` | 72 | | `filesize` | 43 |
| `bva` | 65 | | `time` | 61 |
| `negative` | 15 | | | |
| `datadriven` | 26 | | | |

## 4. Execution control (Task 4)
- **Order:** `conftest.py` sorts groups as `smoke -> ecp -> bva -> negative -> datadriven`, then by
  `@pytest.mark.run_order(n)` inside a group. Smoke tests use `run_order` 1-14 so they run first.
- **Serial:** `./run_tests.sh all` (strict order).
- **Parallel:** `./run_tests.sh parallel` (`-n auto --dist loadscope`, so each module stays on one worker and keeps its order).
- **Single group / module:** `./run_tests.sh smoke|ecp|bva|negative|datadriven|number|filesize|time`.
- **Reports:** `./run_tests.sh report` writes `report.html`, `junit.xml` and `htmlcov/`.
- **tox:** `tox` runs the suite on py311/py312/py313 and in parallel mode (`tox -e parallel`).

## 5. Data-driven testing (Task 3)
Inputs and expected outputs live in `data/number_cases.csv`, `data/filesize_cases.csv` and `data/time_cases.csv`.
`tests/test_csv_driven.py` turns each row into one test, with the CSV `test_id` as the pytest id.
`make_excel.py` reads the same CSVs to build `Test_Cases.xlsx` (Expected vs Actual, with a Pass/Fail formula and a Summary sheet).

## 6. Results
All 192 tests pass in serial and parallel mode (humanize 4.16.0, Python 3.14, pytest 9.1).

Statement coverage of the modules under test (`./run_tests.sh report`):
| Module | Coverage |
|---|---|
| `humanize/filesize.py` | 100% |
| `humanize/time.py` | 78% |
| `humanize/number.py` | 64% |
| whole `humanize` package | 73% |

Uncovered lines are mostly functions outside the assignment scope (e.g. `metric`, `clamp`, `natural_list`,
i18n `activate`/`deactivate`) and rare branches (overflow, `inf`/`nan`).

## 7. Observations (behaviour documented by the tests)
| Function | Input | Observed result | Note |
|---|---|---|---|
| `naturalsize` | `None` / `"abc"` | `TypeError` / `ValueError` | unlike `number` functions, which return the input as text |
| `naturalsize` | `999999` | `1.0 MB` | rounding moves the value into the next unit |
| `naturalsize(binary=True)` | `1000` | `1000 Bytes` | binary units start at 1024 |
| `naturaldelta` | `-30 s` | `30 seconds` | the sign is dropped; use `naturaltime` for past/future |
| `naturaldate` | +-366 days | `Mon DD YYYY` | the year appears once the date is about 5 months or more away |
| `ordinal` | `-1` | `-1th` | negative numbers get the generic suffix |
| `fractional` | `0` | `0/1` | no whole part, so it is always `n/d` |

## 8. Conclusion
The suite covers the three chosen modules with ECP, BVA, negative and data-driven cases. Tests can run
by group, by module, serially in a fixed order or in parallel, and produce HTML, JUnit and coverage reports.
