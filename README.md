# Assignment 3: Unit Test Automation for `humanize`

**Project Under Test:** [`python-humanize/humanize`](https://github.com/python-humanize/humanize)  
**Quick Start Guide:** Refer to [`docs/SETUP.md`](docs/SETUP.md) for environment configuration and setup instructions.

---

## 📌 Project Overview

This repository contains the automated unit testing framework designed for the [`humanize`](https://github.com/python-humanize/humanize) Python library as part of **Assignment 3**. 

The primary objective of this assignment is to design, automate, and execute comprehensive unit test suites using structured software testing methodologies, including:
* **Equivalence Class Partitioning (ECP)**
* **Boundary Value Analysis (BVA)**
* **Smoke Testing & Sanity Checks**
* **Negative & Exception Testing**
* **Data-Driven & Parameterized Testing**

---

## 🚀 Test Execution Commands

The custom test execution script `./run_tests.sh` provides flexible modes to run test suites serially, in parallel, or isolated by testing technique and functional module.

### Complete Command Reference

| Command | Category | Description & Scope |
| :--- | :--- | :--- |
| `./run_tests.sh all` | **Full Suite** | Executes the entire test suite sequentially in standard order. |
| `./run_tests.sh parallel` | **Parallel Execution** | Runs all test modules concurrently using `pytest-xdist` for rapid execution. |
| `./run_tests.sh smoke` | **Test Technique** | Runs essential high-priority sanity tests to verify core library functionality. |
| `./run_tests.sh ecp` | **Test Technique** | Runs Equivalence Class Partitioning tests across valid and invalid partitions. |
| `./run_tests.sh bva` | **Test Technique** | Runs Boundary Value Analysis tests targeting boundary limits and edge cases. |
| `./run_tests.sh negative` | **Test Technique** | Verifies exception handling, invalid data types, and out-of-range parameters. |
| `./run_tests.sh datadriven` | **Test Technique** | Executes parameterized test cases utilizing structured datasets and test vectors. |
| `./run_tests.sh number` | **Module Suite** | Runs unit tests specifically targeting the `humanize.number` module. |
| `./run_tests.sh filesize` | **Module Suite** | Runs unit tests specifically targeting the `humanize.filesize` module. |
| `./run_tests.sh time` | **Module Suite** | Runs unit tests specifically targeting `humanize.time` / natural time functions. |
| `./run_tests.sh report` | **Reporting** | Generates detailed HTML coverage reports, JUnit XML, and execution summary. |

---

## 🛠️ Quick Start & Environment Setup

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/python-humanize/humanize.git](https://github.com/python-humanize/humanize.git)
   cd humanize

