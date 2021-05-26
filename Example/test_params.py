import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support import expected_conditions as ec



@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass


class Test_HubSpot(BaseTest):
    @pytest.mark.parametrize(
        "username,password",
        [
            ("admin@gmail.com", "admin123"),
            ("smita@gmail.com", "smita@123")
        ]
    )
    def send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator)).send_keys(text)

    def test_login(self, username, password):
        """
        this method is used to login to hub spot application
        :param username:
        :param password:
        :return:
        """
        self.driver.get("https://app.hubspot.com/login")
        self.driver.find_element(By.ID, 'username'.send_keys(username))
        time.sleep(3)
        self.driver.find_element(By.ID, 'password'.send_keys(password))
        time.sleep(3)
