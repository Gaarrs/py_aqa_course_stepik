import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)

    x_elem = browser.find_element(By.ID, 'num1')
    x = int(x_elem.text)

    y_elem = browser.find_element(By.ID, 'num2')
    y = int(y_elem.text)

    result = x + y

    select_elem = Select(browser.find_element(By.ID, 'dropdown'))
    select_elem.select_by_visible_text(str(result))

    submit = browser.find_element(By.CLASS_NAME, 'btn')
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()