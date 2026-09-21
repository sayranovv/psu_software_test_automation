from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = 'http://suninjuly.github.io/file_input.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("ivan.petrov@example.com")

    file_input = browser.find_element(By.ID, "file")
    file_input.send_keys("/Users/eldarsayranov/psu_autoQA_stepik/selenium_python/1.txt")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    time.sleep(30)
    browser.quit()