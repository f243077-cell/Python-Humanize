# Video Recording Script - Setup and Test Run (about 5 minutes)

Recording saved as `setup_video/screen recording.mp4`. Show the terminal at a readable font size.

## 1. Introduction (30 s)
- "This is Assignment 3 for Software Quality Engineering: unit test automation for the open-source Python project `humanize`."
- Show the GitHub page of `python-humanize/humanize` and our repo `f243077-cell/Python-Humanize`.

## 2. Local setup - Task 1 (1.5 min)
```bash
git clone https://github.com/python-humanize/humanize.git
git clone https://github.com/f243077-cell/Python-Humanize.git
cd Python-Humanize
python -m venv .venv && source .venv/bin/activate
pip install -e ../humanize
pip install -r requirements-test.txt
python -c "import humanize; print(humanize.intcomma(1234567))"   # 1,234,567
```
- Say: "humanize is installed from source, and the test tools come from requirements-test.txt."

## 3. Project tour (1 min)
- `tests/` - one file per module: `test_number.py`, `test_filesize.py`, `test_time.py`, and `test_csv_driven.py`.
- `data/` - the external CSV test data. `Test_Cases.xlsx` - the same cases with Expected vs Actual.
- `docs/ECP_BVA_Test_Design.md` - how the cases were derived.
- `pytest.ini` / `conftest.py` - markers and the group execution order.

## 4. Running the tests - Task 4 (1.5 min)
```bash
./run_tests.sh smoke        # 14 sanity tests run first
./run_tests.sh filesize     # one module
./run_tests.sh bva          # one technique group
./run_tests.sh all          # whole suite, serial, ordered (192 passed)
./run_tests.sh parallel     # same suite with pytest-xdist
./run_tests.sh report       # report.html, junit.xml, htmlcov/
```
- Open `report.html` and `htmlcov/index.html` in the browser and show that `filesize.py` is at 100% coverage.

## 5. Data-driven tests - Task 3 (30 s)
- Open `data/filesize_cases.csv`, then run `./run_tests.sh datadriven` and point out the ids F01-F08.
- Open `Test_Cases.xlsx` and show the Pass/Fail column and the Summary sheet.

## 6. Close (15 s)
- "All 192 tests pass in serial and parallel mode. The results and findings are in docs/Summary_Report.md."
