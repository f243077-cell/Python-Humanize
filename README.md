# Assignment 3 - Unit Test Automation for `humanize`
Project under test: [python-humanize/humanize](https://github.com/python-humanize/humanize). Quick start: see `docs/SETUP.md`.

| Command | What it does |
|---|---|
| `./run_tests.sh all` | whole suite, serial, ordered |
| `./run_tests.sh parallel` | modules in parallel (xdist) |
| `./run_tests.sh smoke` / `ecp` / `bva` / `negative` / `datadriven` | one group |
| `./run_tests.sh number` / `filesize` / `time` | one module suite |
| `./run_tests.sh report` | HTML + JUnit + coverage reports |
