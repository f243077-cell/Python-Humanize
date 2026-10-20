"""Module under test : humanize.time        | Owner: Member 2
Functions covered    : naturaldelta, naturaltime, naturalday, naturaldate, precisedelta
Design notes         : see docs/ECP_BVA_Test_Design.md  (section 3)
"""
import datetime as dt

import pytest
import humanize

pytestmark = pytest.mark.time

td = dt.timedelta
NOW = dt.datetime(2024, 6, 15, 12, 0, 0)  # fixed "now" so naturaltime results never drift


# --------------------------------------------------------------- naturaldelta
class TestNaturaldelta:
    @pytest.mark.smoke
    @pytest.mark.run_order(10)
    def test_two_hours(self):
        assert humanize.naturaldelta(td(hours=2)) == "2 hours"

    @pytest.mark.ecp
    @pytest.mark.parametrize("value, expected", [
        (td(seconds=30), "30 seconds"),
        (td(minutes=2), "2 minutes"),
        (td(hours=2), "2 hours"),
        (td(days=2), "2 days"),
        (td(days=30), "a month"),
        (td(days=800), "2 years"),
    ], ids=["seconds", "minutes", "hours", "days", "months", "years"])
    def test_unit_classes(self, value, expected):
        assert humanize.naturaldelta(value) == expected

    @pytest.mark.ecp
    def test_months_false_counts_days(self):
        assert humanize.naturaldelta(td(days=45), months=False) == "45 days"

    @pytest.mark.ecp
    def test_int_input_is_seconds(self):
        assert humanize.naturaldelta(30) == "30 seconds"

    @pytest.mark.ecp
    def test_negative_delta_uses_absolute_value(self):
        assert humanize.naturaldelta(td(seconds=-30)) == "30 seconds"

    @pytest.mark.bva
    @pytest.mark.parametrize("seconds, expected", [
        (0, "a moment"), (0.5, "a moment"), (1, "a second"), (2, "2 seconds"),
        (59, "59 seconds"), (60, "a minute"), (3600, "an hour"), (86400, "a day"),
    ], ids=["zero", "half-second", "one-second", "two-seconds", "59s", "60s", "3600s", "86400s"])
    def test_unit_boundaries(self, seconds, expected):
        assert humanize.naturaldelta(td(seconds=seconds)) == expected


# ---------------------------------------------------------------- naturaltime
class TestNaturaltime:
    @pytest.mark.smoke
    @pytest.mark.run_order(11)
    def test_now(self):
        assert humanize.naturaltime(td(0)) == "now"

    @pytest.mark.ecp
    @pytest.mark.parametrize("value, expected", [
        (td(seconds=30), "30 seconds ago"),
        (td(hours=1), "an hour ago"),
        (td(days=2), "2 days ago"),
        (td(hours=-1), "an hour from now"),
        (td(days=-2), "2 days from now"),
    ], ids=["past-seconds", "past-hour", "past-days", "future-hour", "future-days"])
    def test_past_and_future(self, value, expected):
        assert humanize.naturaltime(value) == expected

    @pytest.mark.ecp
    @pytest.mark.parametrize("value, expected", [
        (NOW - td(hours=2), "2 hours ago"),
        (NOW + td(minutes=5), "5 minutes from now"),
    ], ids=["datetime-past", "datetime-future"])
    def test_datetime_input(self, value, expected):
        assert humanize.naturaltime(value, when=NOW) == expected

    @pytest.mark.bva
    @pytest.mark.parametrize("value, expected", [
        (td(0), "now"), (td(seconds=1), "a second ago"),
        (td(seconds=-1), "a second from now"), (td(seconds=60), "a minute ago"),
    ], ids=["zero", "+1s", "-1s", "60s"])
    def test_boundaries(self, value, expected):
        assert humanize.naturaltime(value) == expected


# ----------------------------------------------------------------- naturalday
class TestNaturalday:
    @pytest.mark.smoke
    @pytest.mark.run_order(12)
    def test_today(self):
        assert humanize.naturalday(dt.date.today()) == "today"

    @pytest.mark.bva
    @pytest.mark.parametrize("offset, expected", [
        (-1, "yesterday"), (0, "today"), (1, "tomorrow"),
    ], ids=["yesterday", "today", "tomorrow"])
    def test_relative_words(self, offset, expected):
        assert humanize.naturalday(dt.date.today() + td(days=offset)) == expected

    @pytest.mark.ecp
    @pytest.mark.parametrize("offset", [-5, 5, 2], ids=["past", "future", "just-after-tomorrow"])
    def test_other_days_use_month_day(self, offset):
        day = dt.date.today() + td(days=offset)
        assert humanize.naturalday(day) == day.strftime("%b %d")

    @pytest.mark.ecp
    def test_custom_format(self):
        assert humanize.naturalday(dt.date(2020, 3, 7), "%Y-%m-%d") == "2020-03-07"

    @pytest.mark.negative
    def test_invalid_returned_unchanged(self):
        assert humanize.naturalday("x") == "x"


# ---------------------------------------------------------------- naturaldate
class TestNaturaldate:
    @pytest.mark.smoke
    @pytest.mark.run_order(13)
    def test_tomorrow(self):
        assert humanize.naturaldate(dt.date.today() + td(days=1)) == "tomorrow"

    @pytest.mark.ecp
    @pytest.mark.parametrize("offset", [30, -30], ids=["future-month", "past-month"])
    def test_within_a_year_has_no_year(self, offset):
        day = dt.date.today() + td(days=offset)
        assert humanize.naturaldate(day) == day.strftime("%b %d")

    @pytest.mark.bva
    @pytest.mark.parametrize("offset", [366, -366, 800], ids=["+366d", "-366d", "+800d"])
    def test_far_dates_show_year(self, offset):
        day = dt.date.today() + td(days=offset)
        assert humanize.naturaldate(day) == day.strftime("%b %d %Y")


# --------------------------------------------------------------- precisedelta
class TestPrecisedelta:
    @pytest.mark.smoke
    @pytest.mark.run_order(14)
    def test_minutes_and_seconds(self):
        assert humanize.precisedelta(td(seconds=125)) == "2 minutes and 5 seconds"

    @pytest.mark.ecp
    @pytest.mark.parametrize("value, expected", [
        (td(seconds=3725), "1 hour, 2 minutes and 5 seconds"),
        (td(days=400), "1 year, 1 month and 4 days"),
        (td(days=2, hours=3, minutes=4), "2 days, 3 hours and 4 minutes"),
    ], ids=["h-m-s", "y-m-d", "d-h-m"])
    def test_equivalence_classes(self, value, expected):
        assert humanize.precisedelta(value) == expected

    @pytest.mark.ecp
    def test_minimum_unit(self):
        assert humanize.precisedelta(td(seconds=3725), minimum_unit="minutes") == "1 hour and 2.08 minutes"

    @pytest.mark.ecp
    def test_suppress_days(self):
        assert humanize.precisedelta(td(days=2, hours=3), suppress=["days"]) == "51 hours"

    @pytest.mark.bva
    def test_zero_delta(self):
        assert humanize.precisedelta(td(0)) == "0 seconds"

    @pytest.mark.bva
    def test_millisecond_precision(self):
        result = humanize.precisedelta(td(milliseconds=1500), minimum_unit="milliseconds")
        assert result == "1 second and 500 milliseconds"
