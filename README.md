## Assignment 3 - Test Automation & Execution Summary

### Test Suite Execution
To run the automated unit test suite implemented for `humanize`:

- **All Tests:** `./run_tests.sh all`
- **Specific Techniques:** 
  - Smoke: `./run_tests.sh smoke`
  - Equivalence Partitioning (ECP): `./run_tests.sh ecp`
  - Boundary Value Analysis (BVA): `./run_tests.sh bva`
  - Negative Testing: `./run_tests.sh negative`
  - Data-Driven Testing: `./run_tests.sh datadriven`
- **Module Suites:** `./run_tests.sh number` | `./run_tests.sh filesize` | `./run_tests.sh time`
- **Generate Test & Coverage Reports:** `./run_tests.sh report`

### Test Reports
Execution reports, HTML coverage, and JUnit XML outputs will be generated in the `reports/` or `htmlcov/` directory after running the `./run_tests.sh report` command.

