from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import math

link = 'http://suninjuly.github.io/explicit_wait2.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    wait = WebDriverWait(browser, 12)
    price = browser.find_element(By.ID, "price")
    button = wait.until(
        EC.element_to_be_clickable((By.ID, "book"))
    )
    wait.until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button.click()

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text

    y = str(math.log(abs(12*math.sin(int(x)))))

    inputAnswer = browser.find_element(By.ID, "answer")
    inputAnswer.send_keys(y)

    button = browser.find_element(By.ID, "solve")
    button.click()
finally:
    time.sleep(30)
    browser.quit()