"""Module under test : humanize.number      | Owner: Member 1
Functions covered    : intcomma, intword, ordinal, apnumber, fractional, scientific
Design notes         : see docs/ECP_BVA_Test_Design.md  (section 1)
"""
import pytest
import humanize

pytestmark = pytest.mark.number


# ------------------------------------------------------------------ intcomma
class TestIntcomma:
    @pytest.mark.smoke
    @pytest.mark.run_order(1)
    def test_basic_thousands(self):
        assert humanize.intcomma(1234567) == "1,234,567"

    @pytest.mark.ecp
    @pytest.mark.parametrize("value, expected", [
        (5000, "5,000"),
        (-5000, "-5,000"),
        ("1234567", "1,234,567"),
        (1234.5678, "1,234.5678"),
        (10**12, "1,000,000,000,000"),
    ], ids=["pos-int", "neg-int", "num-string", "float", "huge"])
    def test_equivalence_classes(self, value, expected):
        assert humanize.intcomma(value) == expected

    @pytest.mark.bva
    @pytest.mark.parametrize("value, expected", [
        (0, "0"), (999, "999"), (1000, "1,000"), (1001, "1,001"),
        (-999, "-999"), (-1000, "-1,000"),
    ], ids=["zero", "just-below-1000", "at-1000", "just-above-1000", "neg-999", "neg-1000"])
    def test_comma_boundary(self, value, expected):
        assert humanize.intcomma(value) == expected

    @pytest.mark.ecp
    def test_ndigits_rounds_and_pads(self):
        assert humanize.intcomma(1234.5678, 2) == "1,234.57"

    @pytest.mark.negative
    @pytest.mark.parametrize("value", ["abc", None], ids=["non-numeric-string", "none"])
    def test_non_numeric_returned_unchanged(self, value):
        assert humanize.intcomma(value) == str(value)


# ------------------------------------------------------------------- intword
class TestIntword:
    @pytest.mark.smoke
    @pytest.mark.run_order(2)
    def test_million(self):
        assert humanize.intword(1_200_000) == "1.2 million"

    @pytest.mark.ecp
    @pytest.mark.parametrize("value, expected", [
        (1_500, "1.5 thousand"),
        (2_500_000, "2.5 million"),
        (3_000_000_000, "3.0 billion"),
        (-1_000_000, "-1.0 million"),
        ("1200000", "1.2 million"),
        (1.5e6, "1.5 million"),
    ], ids=["thousand", "million", "billion", "negative", "string", "float"])
    def test_equivalence_classes(self, value, expected):
        assert humanize.intword(value) == expected

    @pytest.mark.bva
    @pytest.mark.parametrize("value, expected", [
        (0, "0"), (999, "999"), (1000, "1.0 thousand"),
        (10**6, "1.0 million"), (10**9, "1.0 billion"), (10**12, "1.0 trillion"),
    ], ids=["zero", "999", "1e3", "1e6", "1e9", "1e12"])
    def test_scale_boundaries(self, value, expected):
        assert humanize.intword(value) == expected

    @pytest.mark.ecp
    def test_custom_format(self):
        assert humanize.intword(1_234_567, "%0.3f") == "1.235 million"

    @pytest.mark.negative
    @pytest.mark.parametrize("value", ["abc", None])
    def test_invalid_returned_unchanged(self, value):
        assert humanize.intword(value) == str(value)


# ------------------------------------------------------------------- ordinal
class TestOrdinal:
    @pytest.mark.smoke
    @pytest.mark.run_order(3)
    def test_first(self):
        assert humanize.ordinal(1) == "1st"

    @pytest.mark.ecp
    @pytest.mark.parametrize("value, expected", [
        (1, "1st"), (2, "2nd"), (3, "3rd"), (4, "4th"), (21, "21st"), (102, "102nd"),
    ], ids=["st", "nd", "rd", "th", "21st", "102nd"])
    def test_suffix_classes(self, value, expected):
        assert humanize.ordinal(value) == expected

    @pytest.mark.bva
    @pytest.mark.parametrize("value, expected", [
        (0, "0th"), (10, "10th"), (11, "11th"), (12, "12th"), (13, "13th"),
        (14, "14th"), (111, "111th"), (112, "112th"),
    ], ids=["zero", "10", "11-teen", "12-teen", "13-teen", "14", "111", "112"])
    def test_teens_exception_boundary(self, value, expected):
        assert humanize.ordinal(value) == expected

    @pytest.mark.negative
    @pytest.mark.parametrize("value", ["x", None])
    def test_invalid_returned_unchanged(self, value):
        assert humanize.ordinal(value) == str(value)

    @pytest.mark.negative
    def test_negative_number_documented_behaviour(self):
        # Observed behaviour: negative numbers get the generic "th" suffix.
        assert humanize.ordinal(-1) == "-1th"


# ------------------------------------------------------------------ apnumber
class TestApnumber:
    @pytest.mark.smoke
    @pytest.mark.run_order(4)
    def test_seven(self):
        assert humanize.apnumber(7) == "seven"

    @pytest.mark.bva
    @pytest.mark.parametrize("value, expected", [
        (-1, "-1"), (0, "zero"), (1, "one"), (9, "nine"), (10, "10"), (11, "11"),
    ], ids=["below-range", "lower", "lower+1", "upper", "above-range", "above+1"])
    def test_range_0_to_9(self, value, expected):
        assert humanize.apnumber(value) == expected

    @pytest.mark.ecp
    @pytest.mark.parametrize("value, expected", [("3", "three"), (3.0, "three"), (5, "five")],
                             ids=["string", "float", "int"])
    def test_input_types(self, value, expected):
        assert humanize.apnumber(value) == expected

    @pytest.mark.negative
    @pytest.mark.parametrize("value", ["x", None])
    def test_invalid_returned_unchanged(self, value):
        assert humanize.apnumber(value) == str(value)


# ---------------------------------------------------------------- fractional
class TestFractional:
    @pytest.mark.smoke
    @pytest.mark.run_order(5)
    def test_half(self):
        assert humanize.fractional(0.5) == "1/2"

    @pytest.mark.ecp
    @pytest.mark.parametrize("value, expected", [
        (0.25, "1/4"), (1.5, "1 1/2"), (2.75, "2 3/4"), (1, "1"), ("0.333", "333/1000"),
    ], ids=["proper", "mixed", "mixed-2", "whole", "string"])
    def test_equivalence_classes(self, value, expected):
        assert humanize.fractional(value) == expected

    @pytest.mark.bva
    def test_zero(self):
        # Observed behaviour: with no whole part the result is always "n/d", so 0 -> "0/1".
        assert humanize.fractional(0) == "0/1"

    @pytest.mark.negative
    @pytest.mark.parametrize("value", ["a", None])
    def test_invalid_returned_unchanged(self, value):
        assert humanize.fractional(value) == str(value)


# ---------------------------------------------------------------- scientific
class TestScientific:
    @pytest.mark.smoke
    @pytest.mark.run_order(6)
    def test_basic(self):
        assert humanize.scientific(12345) == "1.23 x 10⁴"

    @pytest.mark.ecp
    @pytest.mark.parametrize("value, expected", [
        (1000, "1.00 x 10³"), (12345, "1.23 x 10⁴"), (0.00012, "1.20 x 10⁻⁴"), (1, "1.00 x 10⁰"),
    ], ids=["pos-exp", "pos-exp-2", "neg-exp", "exp-zero"])
    def test_equivalence_classes(self, value, expected):
        assert humanize.scientific(value) == expected

    @pytest.mark.bva
    def test_zero(self):
        assert humanize.scientific(0) == "0.00 x 10⁰"

    @pytest.mark.ecp
    def test_precision_argument(self):
        assert humanize.scientific(12345, 3).startswith("1.2")

    @pytest.mark.negative
    def test_invalid_returned_unchanged(self):
        assert humanize.scientific("x") == "x"
