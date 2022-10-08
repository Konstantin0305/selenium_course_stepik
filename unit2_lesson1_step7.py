from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

	

link = "http://suninjuly.github.io/get_attribute.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)

	def calc(x):
		return str(math.log(abs(12*math.sin(int(x)))))

	treasure = browser.find_element(By.CSS_SELECTOR, "#treasure")
	treasure_value = treasure.get_attribute("valuex")
	y = calc(treasure_value)
	

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