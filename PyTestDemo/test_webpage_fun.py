import pytest
from selenium import webdriver
import time

print("test case started")
driver = None


@pytest.fixture(scope="module")
def fun():
    global driver
    print("---driver set up method---")
    driver = webdriver.Chrome(r"C:\Users\dboyapalli\PycharmProjects\pythonProject\Browsers\chromedriver.exe")

    yield
    print("---driver tear down method---")
    driver.quit()


@pytest.mark.usefixtures("fun")
def test_open_google():
    driver.get("https://www.google.com/")
    assert driver.title == "Google"
    time.sleep(2)


@pytest.mark.usefixtures("fun")
def test_open_fb():
    driver.get("https://www.facebook.com/")
    assert driver.title == "Facebook – log in or sign up"
    time.sleep(2)
