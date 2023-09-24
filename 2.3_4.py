import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Chrome()
#browser.execute_script("document.title='Script executing';alert('Robots at work');")

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    # открываем страницу
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)
    time.sleep(1)

    link_btn = browser.find_element(By.XPATH, '//button[contains(text(), "I want to go on a magical journey!")]')
    link_btn.click()

    confirm_box = browser.switch_to.alert
    confirm_box.accept()

    # находим элемент со значеением и нужное значение
    x_elem = browser.find_element(By.ID, 'input_value')
    x = x_elem.text

    # считаем функцию
    y = calc(int(x))

    input1 = browser.find_element(By.ID,'answer')
    input1.send_keys(y)

    button = browser.find_element(By.XPATH, '//button[contains(text(), "Submit")]')
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()