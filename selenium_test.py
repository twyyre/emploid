from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

driver.get("http://localhost:1040/#/")

input()

elements = driver.find_elements(By.XPATH, "//*")

for element in elements:
    print(element.text)

