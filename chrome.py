from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('https://google.com')
driver.maximize_window()
sleep(2)
driver.close()