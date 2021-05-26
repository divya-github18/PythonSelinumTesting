import pytest


@pytest.fixture
def input_value():
    input1 = 39
    return input1


def test_divisible_by_3(input_value):
    assert input_value % 3 == 0


@pytest.mark.skip
def test_divisible_by_6(input_value):
    assert input_value % 6 == 0


@pytest.mark.login
def test_login_fb_insta():
    assert "admin" == "admin123"