import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

@pytest.mark.ui
def test_check_incorrect_username():
    # Створення об'єкту для керування браузером
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # відкриваємо сторінку https://github.com/login 
    driver.get("https://github.com/login")

    # Знаходимо поле, в яке будемо вводити неправильне ім'я користувача або поштову адресу
    login_elem = driver.find_element(By.ID, "login_field")

    # Вводимо неправильне ім'я користувача або поштову адресу
    login_elem.send_keys("sergiibutenko@mistakeinemail.com")
    
    # Знаходимо поле, в яке будемо вводити неправильний пароль
    pass_elem = driver.find_element(By.ID, "password")

    # Вводимо неправильний пароль
    pass_elem.send_keys("wrong password")
    time.sleep(3)
    
    # Знаходимо кнопку sign in
    btn_elem = driver.find_element(By.NAME, "commit")

    # Емулюємо клік лівою кнопкою мишки
    btn_elem.click()

    # Перевіряємо, що назва сторінки така, яку ми очікуємо
    assert driver.title == "Sign in to GitHub · GitHub"

    # Закриваємо браузер
    driver.close()
