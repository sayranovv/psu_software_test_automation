import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/get_attribute.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    image = browser.find_element(By.CSS_SELECTOR, "#treasure")
    x = image.get_attribute("valuex")
    y = calc(x)

    inputCheckbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    inputCheckbox.click()
    inputRadio = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    inputRadio.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    inputAnswer = browser.find_element(By.CSS_SELECTOR, "#answer")
    inputAnswer.send_keys(y)
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
