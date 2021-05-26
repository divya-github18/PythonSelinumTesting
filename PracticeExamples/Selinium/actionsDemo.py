import time
from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(r"C:\Users\dboyapalli\PycharmProjects\pythonProject\Browsers\chromedriver.exe")
#ActionChains

driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
action = ActionChains(driver)
action.context_click(driver.find_element_by_id("double-click")).perform()
print("-------------------------------------")
time.sleep(5)
action.double_click(driver.find_element_by_id("double-click")).perform()
time.sleep(5)
print("-------------------------------------")
alert = driver.switch_to.alert
assert "You double clicked me!!!, You got to be kidding me" == alert.text
alert.accept()
driver.close()
