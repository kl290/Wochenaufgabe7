import pytest

from test_div import divide


def test_divide():
    with pytest.raises(ValueError):
        divide(1, 0)
