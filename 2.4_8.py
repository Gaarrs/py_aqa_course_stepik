import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.implicitly_wait(5)
#browser.execute_script("document.title='Script executing';alert('Robots at work');")

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    # открываем страницу
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)

    price_needed = WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element((By.ID, 'price'),'$100'))

    book = browser.find_element(By.ID, 'book')
    book.click()

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