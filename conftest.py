"""Shared fixtures + execution-order control.

Execution order of GROUPS (Task 4):   smoke -> ecp -> bva -> negative -> datadriven
Inside a group, tests are ordered by  @pytest.mark.run_order(n)  (default 100),
then by their original position (stable sort).
Strict ordering is guaranteed in serial mode; with xdist (-n) the order is
preserved per worker / per module (--dist loadscope).
"""
import csv
from pathlib import Path

import pytest

DATA_DIR = Path(__file__).parent / "data"
GROUP_ORDER = ["smoke", "ecp", "bva", "negative", "datadriven"]


def read_csv(name):
    """Return the rows of data/<name> as a list of dicts (external test data)."""
    with open(DATA_DIR / name, newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def _group_rank(item):
    for rank, name in enumerate(GROUP_ORDER):
        if item.get_closest_marker(name):
            return rank
    return len(GROUP_ORDER)


def _explicit_order(item):
    marker = item.get_closest_marker("run_order")
    return marker.args[0] if marker and marker.args else 100


def pytest_collection_modifyitems(config, items):
    items.sort(key=lambda it: (_group_rank(it), _explicit_order(it)))  # stable
    for item in items:                       # every test is part of the regression suite
        item.add_marker(pytest.mark.regression)


@pytest.fixture(scope="session")
def data_dir():
    return DATA_DIR
