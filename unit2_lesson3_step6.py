import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    troll = browser.find_element(By.CSS_SELECTOR, ".btn")
    troll.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_variable = browser.find_element(By.CSS_SELECTOR, "#input_value")
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
    
    time.sleep(10)
    browser.quit()