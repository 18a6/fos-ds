from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://www.binance.com/en/price/bitcoin")

price = driver.find_element(By.CLASS_NAME, 'css-12ujz79')
with open("output.txt", "a") as output:
    output.write(f'{price.text}\n')

driver.quit()