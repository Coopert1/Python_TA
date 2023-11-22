from tasks.task_01 import *
import pytest


@pytest.mark.parametrize("minutes, hours", [(360, 6.0), (239, 3.9833), (0, 0)])
def test_to_hours(minutes, hours):
    assert to_hours(minutes) == hours


@pytest.mark.parametrize("hours, minutes", [(5, 300), (24, 1440), (0, 0)])
def test_to_minutes(hours, minutes):
    assert to_minutes(6) == 360


@pytest.mark.parametrize("a, b,  expected_result", [(12, 3, True), (2, 3, False)])
def test_is_whole_div(a, b, expected_result):
    assert is_whole_div(a, b) == expected_result