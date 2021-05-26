
import selenium
from Config.config import TestData
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    # By Locators #
    user_name = (By.ID, "txtUsername")
    password = (By.ID, "txtPassword")
    login_button = (By.ID, "btnLogin")
    error_message = (By.XPATH, "//span[@id='spanMessage']")
    welcome_log = (By.XPATH, "//li[contains(text(),'Welcome Divya')]")

    # Page Actions #
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def do_login(self, username, password):
        self.send_keys(self.user_name, username)
        self.send_keys(self.password, password)
        self.press_button(self.login_button)

