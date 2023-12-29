import pytest
from tasks.task_04_regex import User


@pytest.mark.parametrize("input_data, expected_result", [('Test123@#', 'Test123@#'),
                                                         ('est123dfdsf', ValueError),
                                                         ('Test$#$R#%##', ValueError)])
def test_user_password(input_data, expected_result):
    p = User('Test', 'Taskqweerrtty@3')
    if expected_result != ValueError:
        p.update_password(input_data)
        assert p.password == expected_result
    else:
        with pytest.raises(ValueError):
            p.update_password(input_data)
