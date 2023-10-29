from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    name = browser.find_element(By.NAME, 'firstname')
    name.send_keys('Ivan')
    lastname = browser.find_element(By.NAME, 'lastname')
    lastname.send_keys('Ivanov')
    email = browser.find_element(By.NAME, 'e-mail')
    email.send_keys('test@test.ru')
    elements = browser.find_elements(By.TAG_NAME, 'input')
    for element in elements:
        element.send_keys("Мой ответ")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла