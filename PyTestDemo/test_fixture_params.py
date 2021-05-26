from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from webdriver_manager.firefox import GeckoDriverManager

web_driver = None


@pytest.fixture(params=["chrome", "firefox"],scope='class')
def init__driver(request):

    global web_driver
    if request.param == "chrome":
        web_driver = webdriver.Chrome(ChromeDriverManager().install())
    if request.param == "firefox":
        web_driver = webdriver.Firefox(executable_path=r"C:\Users\dboyapalli\PycharmProjects\pythonProject\Browsers\geckodriver.exe")
    request.cls.driver = web_driver
    yield
    web_driver.close()


@pytest.mark.usefixtures("init__driver")
class BaseTest:
    pass


class TestGoogle(BaseTest):

    def test_google_title(self):
        self.driver.get("http://www.google.com")
        assert self.driver.title == "Google"
