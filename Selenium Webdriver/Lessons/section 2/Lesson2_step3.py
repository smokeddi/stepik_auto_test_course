from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

try:
    link = "https://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, 'num1')
    x = x_element.text
    y_element = browser.find_element(By.ID, 'num2')
    y = y_element.text
    z = int(x) + int(y)
    print(z)
    select = Select(browser.find_element(By.ID, 'dropdown'))
    select.select_by_visible_text(str(z))
    button = browser.find_element(By.CLASS_NAME, 'btn')
    button.click()

finally:
    time.sleep(5)
    browser.quit()
