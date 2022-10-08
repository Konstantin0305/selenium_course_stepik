from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/execute_script.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)

	x_variable = num1 = browser.find_element(By.CSS_SELECTOR, "#input_value")
	x_variable_text = x_variable.text
	x_int = int(x_variable_text)

	def calc(x):
		return math.log(abs(12*math.sin(int(x))))
	answer = calc(x_int)

	button = browser.find_element(By.CSS_SELECTOR, ".btn")
	browser.execute_script("return arguments[0].scrollIntoView(true);", button)
	button.click()

	input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
	input1.send_keys(answer)
	
	input2 = browser.find_element(By.CSS_SELECTOR, '[type = checkbox]')
	input2.click()

	input3 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
	input3.click()

	
	button.click()

finally:
    
	# ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
	# закрываем браузер после всех манипуляций
    browser.quit()