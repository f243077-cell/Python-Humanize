#!/usr/bin/env bash
# Test runner for Assignment 3 (Task 4: groups, order, serial vs parallel, reports).
# Usage: ./run_tests.sh [all|parallel|smoke|ecp|bva|negative|datadriven|number|filesize|time|report]
set -euo pipefail
cd "$(dirname "$0")"

PYTEST="python -m pytest"
TARGET="${1:-all}"

case "$TARGET" in
  all)
    # whole suite, serial: groups run smoke -> ecp -> bva -> negative -> datadriven (conftest.py)
    $PYTEST -v
    ;;
  parallel)
    # each module stays on one worker so its internal order is kept
    $PYTEST -v -n auto --dist loadscope
    ;;
  smoke|ecp|bva|negative|datadriven|regression)
    $PYTEST -v -m "$TARGET"
    ;;
  number|filesize|time)
    $PYTEST -v -m "$TARGET"
    ;;
  report)
    $PYTEST -v \
      --html=report.html --self-contained-html \
      --junitxml=junit.xml \
      --cov=humanize --cov-report=term-missing --cov-report=html
    echo "Reports: report.html, junit.xml, htmlcov/index.html"
    ;;
  *)
    echo "Unknown target: $TARGET"
    echo "Usage: $0 [all|parallel|smoke|ecp|bva|negative|datadriven|number|filesize|time|report]"
    exit 1
    ;;
esac
