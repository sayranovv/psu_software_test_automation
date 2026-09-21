from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = 'https://SunInJuly.github.io/execute_script.html';

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = str(math.log(abs(12*math.sin(int(x)))))

    browser.execute_script("return arguments[0].scrollIntoView(true);", browser.find_element(By.CSS_SELECTOR, "#answer"))

    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)

    option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    option1.click()

    option2 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    option2.click()

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
finally:
    time.sleep(30)
    browser.quit()