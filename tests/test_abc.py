import pytest


class TestClass:

    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "check"), "x should be hello "

    @pytest.mark.login
    def test_login_fb(self):
        assert "admin" == "admin"