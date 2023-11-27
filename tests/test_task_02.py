from tasks.task_02 import *
import pytest

input_data_1 = [1, 11, 3, 3, 5, 6, 9, 11, 11, 3]
input_data_2 = [-1, 1, 1, 0, 4, 5, 2, 3]


@pytest.mark.parametrize("input_data, expected_result", [(input_data_1, [10, 6, 4, [3, 11], [3, 3]]),
                                                         (input_data_2, [8, 7, 6, [1], [2]])])
def test_to_hours(input_data, expected_result):
    assert stats(input_data) == expected_result
