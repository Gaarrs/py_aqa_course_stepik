import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
browser = webdriver.Chrome()
#browser.execute_script("document.title='Script executing';alert('Robots at work');")

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    # открываем страницу
    browser = webdriver.Chrome()
    link = "http://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    time.sleep(1)

    # находим элемент со значеением и нужное значение
    x_elem = browser.find_element(By.ID, 'input_value')
    x = x_elem.text

    # считаем функцию
    y = calc(int(x))

    input1 = browser.find_element(By.ID,'answer')
    input1.send_keys(y)

    # находим, скроллим и нажимаем кнопку
    check_box = browser.find_element(By.ID, 'robotCheckbox')
    browser.execute_script("return arguments[0].scrollIntoView(true);", check_box)
    check_box.click()

    radio = browser.find_element(By.ID, 'robotsRule')
    radio.click()

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()