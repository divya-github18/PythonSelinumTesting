import pytest


def fun(x):
    return 3+x


@pytest.mark.xfail
def test_fun():
    assert fun(3) == 7


def f():
    raise SystemExit(1)


def test_my_test():
    with pytest.raises(SystemExit):
        f()


def f1():
    print(1/0)


def test_my_test1():
    with pytest.raises(ZeroDivisionError):
        f1()


def test_recursion_depth():
    with pytest.raises(RuntimeError) as exc_info:

        def f():
            f()

        f()
    assert "maximum recursion" in str(exc_info.value)


@pytest.mark.login
def test_login_gmail():
    assert "admin" == "admin"


@pytest.mark.login
def test_divisible_by_6():
    assert 3 % 6 == 0