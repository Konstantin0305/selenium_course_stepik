from selenium import webdriver
from selenium.webdriver.common.by import By
import os 
import time

link = "http://suninjuly.github.io/file_input.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)

	input1 = browser.find_element(By.CSS_SELECTOR, '[name = "firstname"]')
	input1.send_keys("Ivan")

	input2 = browser.find_element(By.CSS_SELECTOR, '[name = "lastname"]')
	input2.send_keys("Petrov")

	input3 = browser.find_element(By.CSS_SELECTOR, '[name = "email"]')
	input3.send_keys("email")

	current_dir = os.path.abspath(os.path.dirname(__file__))
	file_name = "kek.txt"  
	file_path = os.path.join(current_dir, file_name)
	element = browser.find_element(By.CSS_SELECTOR, "#file")           
	element.send_keys(file_path)
	
	button = browser.find_element(By.CSS_SELECTOR, ".btn")
	button.click()

finally:
    
	# ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
	# закрываем браузер после всех манипуляций
    browser.quit()