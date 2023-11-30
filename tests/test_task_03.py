from tasks.task_03 import *
import pytest


@pytest.mark.parametrize("input_data, divider, expected_result", [("123456987654", 6, "234561876549"),
                                                                  ("123456987653", 6, "234561356789"),
                                                                  ("66443875", 4, "44668753"),
                                                                  ("66443875", 8, "64438756"),
                                                                  ("664438769", 8, "67834466"),
                                                                  ("123456779", 8, "23456771"),
                                                                  ("", 8, ""),
                                                                  ("123456779", 0, "")])
def test_convert(input_data, divider, expected_result):
    assert convert(input_data, divider) == expected_result
