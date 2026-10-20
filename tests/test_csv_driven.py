"""Data-driven tests (Task 3/4): test data comes from external CSV files in data/.
Each CSV row is one test case; the same IDs appear in Test_Cases.xlsx."""
import datetime as dt

import pytest
import humanize
from conftest import read_csv

pytestmark = [pytest.mark.datadriven]


def _rows(name):
    return [pytest.param(r, id=r["test_id"]) for r in read_csv(name)]


@pytest.mark.number
@pytest.mark.parametrize("row", _rows("number_cases.csv"))
def test_number_from_csv(row):
    func = getattr(humanize, row["function"])
    assert func(int(row["value"])) == row["expected"]


@pytest.mark.filesize
@pytest.mark.parametrize("row", _rows("filesize_cases.csv"))
def test_filesize_from_csv(row):
    result = humanize.naturalsize(
        int(row["value"]),
        binary=row["binary"] == "true",
        gnu=row["gnu"] == "true",
    )
    assert result == row["expected"]


@pytest.mark.time
@pytest.mark.parametrize("row", _rows("time_cases.csv"))
def test_time_from_csv(row):
    func = getattr(humanize, row["function"])
    assert func(dt.timedelta(seconds=int(row["seconds"]))) == row["expected"]
