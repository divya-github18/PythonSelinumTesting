import pytest
from selenium import webdriver
from Config.config import TestData
from Pages.LoginPage import LoginPage


web_driver = None


@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    global web_driver
    if request.param == "chrome":
        web_driver = webdriver.Chrome(executable_path=TestData.CHROME_EXECUTABLE_PATH)
    web_driver.set_window_size(1552, 840)
    web_driver.delete_all_cookies()
    request.cls.driver = web_driver
    request.cls.loginPage = LoginPage(web_driver)
    yield
    web_driver.close()
