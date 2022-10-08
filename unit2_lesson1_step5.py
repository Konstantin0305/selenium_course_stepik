from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

	

link = "https://suninjuly.github.io/math.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)

	def calc(x):
		return str(math.log(abs(12*math.sin(int(x)))))


	x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
	x = x_element.text
	y = calc(x)
	
	
	

	input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
	input1.send_keys(y)

	input2 = browser.find_element(By.CSS_SELECTOR, '[type = checkbox]')
	input2.click()

	input3 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
	input3.click()

	button = browser.find_element(By.CSS_SELECTOR, ".btn")
	button.click()

finally:
    
	# ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
	# закрываем браузер после всех манипуляций
    browser.quit()

