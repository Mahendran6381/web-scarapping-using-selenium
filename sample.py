from selenium import webdriver
import os
os.environ["PATH"] += f"C:\Selenium\drivers"
driver = webdriver.Chrome()
list = ["mahendran","Kamiyo","killyo","sivyo","practicepython"]
for i in range(len(list)):
    driver.get("https://www.hackerrank.com/auth/login")
    driver.implicitly_wait(15)
    email = driver.find_element_by_id("input-1")
    password = driver.find_element_by_id("input-2")
    btn = driver.find_element_by_css_selector('button[data-analytics="LoginPassword"]')
    email.send_keys("mahendran638161@gmail.com")
    password.send_keys(list[i])
    btn.click()
