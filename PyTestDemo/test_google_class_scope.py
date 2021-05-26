import pytest
from selenium import webdriver
import time


print("test case started")


@pytest.fixture(scope="class")
def fun_setup_chrome(request):
    print("---chrome driver set up method---")
    ch_driver = webdriver.Chrome(r"C:\Users\dboyapalli\PycharmProjects\pythonProject\Browsers\chromedriver.exe")
    request.cls.driver = ch_driver

    yield
    print("---chrome driver tear down method---")
    ch_driver.quit()


@pytest.mark.usefixtures("fun_setup_chrome")
class BaseChromeTest:
    pass


class TestGoogleChrome(BaseChromeTest):
    @pytest.mark.skip
    def test_open_google(self):
        self.driver.get("https://www.google.com/")
        assert self.driver.title == "Google"
        time.sleep(2)




