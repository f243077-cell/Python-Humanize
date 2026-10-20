# Submission Checklist - Assignment 3 (SQE)

## Task 1 - Project setup
- [x] Open-source project chosen: `python-humanize/humanize` (Python, MIT)
- [x] Setup steps in `docs/SETUP.md`
- [x] Test dependencies in `requirements-test.txt`
- [x] Setup video in `setup_video/screen recording.mp4` (script: `docs/Video_Recording_Script.md`)

## Task 2 - Unit tests (ECP + BVA)
- [x] Test design tables in `docs/ECP_BVA_Test_Design.md`
- [x] `tests/test_number.py` - `humanize.number` (Member 1)
- [x] `tests/test_filesize.py` - `humanize.filesize` (Member 2)
- [x] `tests/test_time.py` - `humanize.time` (Member 2)
- [x] Negative / invalid-input cases for each module

## Task 3 - Data-driven testing
- [x] External test data: `data/number_cases.csv`, `data/filesize_cases.csv`, `data/time_cases.csv` (26 rows)
- [x] `tests/test_csv_driven.py` reads the CSV files
- [x] `Test_Cases.xlsx` built from the same CSVs by `make_excel.py`

## Task 4 - Test execution control
- [x] Groups and markers in `pytest.ini` (smoke, ecp, bva, negative, datadriven, regression, per module)
- [x] Execution order in `conftest.py` (smoke -> ecp -> bva -> negative -> datadriven, then `run_order`)
- [x] Serial and parallel runs: `./run_tests.sh all` / `./run_tests.sh parallel`
- [x] Reports: `./run_tests.sh report` (HTML, JUnit XML, coverage)
- [x] Multi-environment runs with `tox.ini`

## Documentation
- [x] `README.md` - quick start and commands
- [x] `docs/Summary_Report.md` - scope, counts, coverage, findings
- [x] `docs/TEAM_CONTRIBUTION.md` - who did what

## Final check before submitting
- [x] `./run_tests.sh all` -> 192 passed
- [x] `./run_tests.sh parallel` -> 192 passed
- [ ] Repository pushed to https://github.com/f243077-cell/Python-Humanize
- [ ] Repository link (and video, if required separately) submitted on the portal
