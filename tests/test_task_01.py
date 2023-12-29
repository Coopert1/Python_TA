from tasks.task_01 import *
from helpers.custom_exeption import WrongOperatorError
import pytest


@pytest.mark.parametrize("minutes, hours", [(360, 6.0), (239, 3.9833), (0, 0)])
def test_to_hours(minutes, hours):
    assert to_hours(minutes) == hours


@pytest.mark.parametrize("hours, minutes", [(5, 300), (24, 1440), (0, 0)])
def test_to_minutes(hours, minutes):
    assert to_minutes(hours) == minutes


@pytest.mark.parametrize("a, b,  expected_result", [(12, 3, True), (2, 3, False), (512, 8, True)])
def test_is_whole_div(a, b, expected_result):
    assert is_whole_div(a, b) == expected_result


@pytest.mark.parametrize("a, b, operator, expected_result", [(12, 3, '+', 15),
                                                             (2, 3, '*', 6),
                                                             (8, 2, '//', 4),
                                                             (3, 4, '/', 0.75),
                                                             (5, 2, '%', 1),
                                                             (4, 3, '3', WrongOperatorError)])
def test_calculator(a, b, operator, expected_result):

    if expected_result != WrongOperatorError:
        assert calculator(a, b, operator) == expected_result
    else:
        with pytest.raises(WrongOperatorError, match="Error: Chose ONLY operator from list"):
            calculator(a, b, operator)

