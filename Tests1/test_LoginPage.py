from Config.config import TestData
from Pages.LoginPage import LoginPage
from Tests1.test_login_base import BaseLoginTest
from Pages.BasePage import BasePage


class TestLogin(BaseLoginTest):

    def test_login(self):
        self.loginPage = LoginPage(self.driver)
        self.basePage = BasePage(self.driver)
        self.loginPage.do_login(TestData.STANDARD_USER_NAME, TestData.PASSWORD)
        welcome_log=self.basePage.get_element_text(LoginPage.welcome_log)
        assert welcome_log == "Welcome Divya"

    def test_login_failure(self):
        self.loginPage = LoginPage(self.driver)
        self.basePage = BasePage(self.driver)
        self.loginPage.do_login("sak", "fgh")
        error = self.basePage.get_invalid_message(LoginPage.error_message)
        assert error == "Invalid credentials"

    def test_login_password_empty(self):
        self.loginPage = LoginPage(self.driver)
        self.basePage = BasePage(self.driver)
        self.loginPage.do_login(TestData.STANDARD_USER_NAME, "")
        error = self.basePage.get_invalid_message(LoginPage.error_message)
        assert error == "Password cannot be empty"

    def test_login_username_empty(self):
        self.loginPage = LoginPage(self.driver)
        self.basePage = BasePage(self.driver)
        self.loginPage.do_login("", "H752")
        error = self.basePage.get_invalid_message(LoginPage.error_message)
        assert error == "Username cannot be empty"