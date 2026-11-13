
from hypothesis import given, strategies as st
from processor import (
    calculate_dimensional_weight,
    format_tracking_label,
    parse_package_manifest
)


# Test 1: Dimensional weight should not crash
@given(st.text() | st.none())
def test_calculate_dimensional_weight_no_crash(s):
    try:
        calculate_dimensional_weight(s)
    except Exception as e:
        assert False, f"calculate_dimensional_weight crashed with input {s!r}: {e}"


# Test 2: Tracking label should not crash
@given(st.text() | st.none())
def test_format_tracking_label_safe(s):
    try:
        format_tracking_label(s)
    except Exception as e:
        assert False, f"format_tracking_label crashed with input {s!r}: {e}"


# Test 3: Package manifest should not crash
@given(st.text() | st.none())
def test_parse_package_manifest_safe(s):
    try:
        parse_package_manifest(s)
    except Exception as e:
        assert False, f"parse_package_manifest crashed with input {s!r}: {e}"
