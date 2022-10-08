from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


link = "http://suninjuly.github.io/selects1.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)

	num1 = browser.find_element(By.CSS_SELECTOR, "#num1")
	num1_text = num1.text

	
	num2 = browser.find_element(By.CSS_SELECTOR, "#num2")
	num2_text = num2.text

	
	result = int(num1_text) + int(num2_text)

	result_string = str(result)

	select = Select(browser.find_element(By.CSS_SELECTOR, "#dropdown"))
	select.select_by_value(result_string)

	button = browser.find_element(By.CSS_SELECTOR, ".btn")
	button.click()

finally:
    
	# ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
	# закрываем браузер после всех манипуляций
    browser.quit()