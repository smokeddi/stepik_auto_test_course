from selenium.webdriver.common.by import By
import pytest
import time

class Test_lesson6():
    def test_button_different_languages(self, browser):
        browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
        time.sleep(30)
        button = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
        assert button is not None, "Кнопка не найдена на странице"

if __name__ == "__main__":
    pytest.main()