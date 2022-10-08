from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    price = WebDriverWait (browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    book = browser.find_element(By.ID, "book")
    book.click()

    x_variable = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x_variable_text = x_variable.text
    x_int = int(x_variable_text)

    def calc(x):
        return math.log(abs(12*math.sin(int(x))))
    answer = calc(x_int)

    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(answer)

    button = browser.find_element(By.CSS_SELECTOR, "#solve")
    button.click()

finally:
    
    time.sleep(10)
    browser.quit()