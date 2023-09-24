import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
#print(os.path.abspath(__file__))
file = os.path.join(os.path.dirname(__file__), 'smth.txt')
print(file)

try:
    # открываем страницу
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)
    time.sleep(1)

    # находим инпут с именем
    input_name = browser.find_element(By.CSS_SELECTOR, "[placeholder='Enter first name']")
    input_name.send_keys('Boris')

    input_lastname = browser.find_element(By.NAME, 'lastname')
    input_lastname.send_keys('Volkov')

    input_email = browser.find_element(By.NAME, 'email')
    input_email.send_keys('bolkov@gmail.com')

    # находим кнопку загрузки файла
    upload_button = browser.find_element(By.ID, 'file')
    upload_button.send_keys(file)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()