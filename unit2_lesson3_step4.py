from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    btn = browser.find_element(By.CSS_SELECTOR, ".btn")
    btn.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x_variable = num1 = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x_variable_text = x_variable.text
    x_int = int(x_variable_text)

    def calc(x):
        return math.log(abs(12*math.sin(int(x))))
    answer = calc(x_int)

    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(answer)

    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()

finally:
    
    time.sleep(5)
    browser.quit()