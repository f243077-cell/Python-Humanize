"""Module under test : humanize.filesize    | Owner: Member 2
Functions covered    : naturalsize (decimal, binary=True, gnu=True, format)
Design notes         : see docs/ECP_BVA_Test_Design.md  (section 2)
"""
import pytest
import humanize

pytestmark = pytest.mark.filesize


# ------------------------------------------------------- decimal (default)
class TestNaturalsizeDecimal:
    @pytest.mark.smoke
    @pytest.mark.run_order(7)
    def test_basic_megabytes(self):
        assert humanize.naturalsize(3_000_000) == "3.0 MB"

    @pytest.mark.ecp
    @pytest.mark.parametrize("value, expected", [
        (300, "300 Bytes"),
        (3_000, "3.0 kB"),
        (3_000_000, "3.0 MB"),
        (3_000_000_000, "3.0 GB"),
        (3 * 10**12, "3.0 TB"),
        ("1000", "1.0 kB"),
        (-1000, "-1.0 kB"),
    ], ids=["bytes", "kB", "MB", "GB", "TB", "num-string", "negative"])
    def test_equivalence_classes(self, value, expected):
        assert humanize.naturalsize(value) == expected

    @pytest.mark.bva
    @pytest.mark.parametrize("value, expected", [
        (0, "0 Bytes"), (1, "1 Byte"), (2, "2 Bytes"), (999, "999 Bytes"),
        (1000, "1.0 kB"), (1001, "1.0 kB"), (999_999, "1.0 MB"), (10**6, "1.0 MB"),
    ], ids=["zero", "singular-1", "plural-2", "just-below-kB", "at-kB", "just-above-kB",
            "rolls-to-MB", "at-MB"])
    def test_unit_boundaries(self, value, expected):
        assert humanize.naturalsize(value) == expected

    @pytest.mark.ecp
    def test_custom_format(self):
        assert humanize.naturalsize(1_234_567, format="%.3f") == "1.235 MB"

    @pytest.mark.negative
    def test_none_raises_type_error(self):
        with pytest.raises(TypeError):
            humanize.naturalsize(None)

    @pytest.mark.negative
    def test_non_numeric_string_raises_value_error(self):
        with pytest.raises(ValueError):
            humanize.naturalsize("abc")


# ------------------------------------------------------------ binary=True
class TestNaturalsizeBinary:
    @pytest.mark.smoke
    @pytest.mark.run_order(8)
    def test_basic_kibibyte(self):
        assert humanize.naturalsize(1024, binary=True) == "1.0 KiB"

    @pytest.mark.ecp
    def test_1000_stays_in_bytes(self):
        # 1000 is a kB in decimal mode but still below one KiB in binary mode.
        assert humanize.naturalsize(1000, binary=True) == "1000 Bytes"

    @pytest.mark.bva
    @pytest.mark.parametrize("value, expected", [
        (0, "0 Bytes"), (1023, "1023 Bytes"), (1024, "1.0 KiB"), (1025, "1.0 KiB"),
        (1024**2, "1.0 MiB"), (1024**3, "1.0 GiB"),
    ], ids=["zero", "just-below-KiB", "at-KiB", "just-above-KiB", "at-MiB", "at-GiB"])
    def test_unit_boundaries(self, value, expected):
        assert humanize.naturalsize(value, binary=True) == expected


# --------------------------------------------------------------- gnu=True
class TestNaturalsizeGnu:
    @pytest.mark.smoke
    @pytest.mark.run_order(9)
    def test_basic_kilo(self):
        assert humanize.naturalsize(1024, gnu=True) == "1.0K"

    @pytest.mark.ecp
    @pytest.mark.parametrize("value, expected", [
        (500, "500B"), (3000, "2.9K"), (1024**2, "1.0M"), (1024**3, "1.0G"),
    ], ids=["B", "K", "M", "G"])
    def test_equivalence_classes(self, value, expected):
        assert humanize.naturalsize(value, gnu=True) == expected

    @pytest.mark.bva
    @pytest.mark.parametrize("value, expected", [
        (0, "0B"), (1023, "1023B"), (1024, "1.0K"),
    ], ids=["zero", "just-below-K", "at-K"])
    def test_unit_boundaries(self, value, expected):
        assert humanize.naturalsize(value, gnu=True) == expected
