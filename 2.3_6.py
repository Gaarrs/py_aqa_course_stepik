import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Chrome()
browser.implicitly_wait(5)
#browser.execute_script("document.title='Script executing';alert('Robots at work');")

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    # открываем страницу
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)

    first_window = browser.window_handles[0]

    link_btn = browser.find_element(By.CLASS_NAME, 'trollface')
    link_btn.click()

    second_window = browser.window_handles[1]
    browser.switch_to.window(second_window)

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