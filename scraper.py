from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://en.wikipedia.org/wiki/Bitcoin")

elements = driver.find_elements(By.TAG_NAME, 'h1')
with open("output.txt", "w") as file:
    for e in elements:
        file.write(elements)

driver.quit()