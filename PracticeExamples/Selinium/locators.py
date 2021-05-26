import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(r"C:\Users\dboyapalli\PycharmProjects\pythonProject\Browsers\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.implicitly_wait(5)
driver.find_element_by_css_selector("input[name='name']").send_keys("Rahul")
driver.find_element_by_name("email").send_keys("Shetty")

driver.find_element_by_id("exampleCheck1").click()

dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
time.sleep(4)
dropdown.select_by_index(0)

time.sleep(4)
driver.find_element_by_xpath("//input[@type='submit']").click()
time.sleep(4)
message = driver.find_element_by_class_name("alert-success").text
time.sleep(4)
assert "success" in message
driver.close()