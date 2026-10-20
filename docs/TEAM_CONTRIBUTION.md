# Team Contribution

| Member | Name | Responsibility |
|---|---|---|
| Member 1 | Tanzeel Hussain (f243077) | `humanize.number` |
| Member 2 | Faizan | `humanize.filesize` and `humanize.time` |

## Member 1 - Tanzeel Hussain
- Project README and `.gitignore`
- `pytest.ini` (markers, test groups) and `conftest.py` (execution order, CSV reader fixture)
- `docs/ECP_BVA_Test_Design.md` (ECP/BVA tables for all three modules)
- `tests/test_number.py` (78 tests: `intcomma`, `intword`, `ordinal`, `apnumber`, `fractional`, `scientific`)
- `tests/test_csv_driven.py`, `data/number_cases.csv`, `make_excel.py`, `Test_Cases.xlsx`
- `docs/SETUP.md` and the setup screen recording (`setup_video/`)

## Member 2 - Faizan
- `tests/test_filesize.py` (35 tests: `naturalsize` in decimal, binary and GNU modes)
- `tests/test_time.py` (53 tests: `naturaldelta`, `naturaltime`, `naturalday`, `naturaldate`, `precisedelta`)
- `data/filesize_cases.csv` (F01-F08) and `data/time_cases.csv` (T01-T08)
- `run_tests.sh` (group/module/serial/parallel/report targets), `tox.ini`, `requirements-test.txt`
- `docs/Summary_Report.md`, `docs/Video_Recording_Script.md`, `SUBMISSION_CHECKLIST.md`

## Shared
- Test design review and the 26-row data-driven set (N01-N10, F01-F08, T01-T08)
- Final run of the full suite (192 tests passing) before submission
