from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://en.wikipedia.org/wiki/Bitcoin")

elements = driver.find_elements(By.TAG_NAME, 'h1')
for e in elements:
    print(e.text)

driver.quit()