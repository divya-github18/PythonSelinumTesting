from selenium import webdriver
driver = webdriver.Chrome(r"C:\Users\dboyapalli\PycharmProjects\pythonProject\Browsers\chromedriver.exe")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/")  #get method to hit url on  browser
print(driver.title)
print(driver.current_url)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.minimize_window()
driver.back()
driver.refresh()
driver.close()









