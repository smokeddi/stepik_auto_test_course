import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
# file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
# element.send_keys(file_path)
try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'test.txt')

    input1 = browser.find_element(By.NAME, 'firstname')
    input1.send_keys('test')
    input2 = browser.find_element(By.NAME, 'lastname')
    input2.send_keys('test')
    input2 = browser.find_element(By.NAME, 'email')
    input2.send_keys('test@test.ru')
    input3 = browser.find_element(By.NAME, 'file')
    input3.send_keys(file_path)
    button = browser.find_element(By.CLASS_NAME, 'btn')
    button.click()


finally:
    time.sleep(1)
    browser.quit()