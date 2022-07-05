import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from funciones import Funciones_Globales
from selenium.webdriver import ActionChains

def test_login1():
    global driver
    driver = webdriver.Chrome()
    f = Funciones_Globales(driver)
    f.navigate_to("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
    f.write("//input[@id='Email']", "admin@yourstore.com")
    f.write("//input[@id='Password']", "123456")
    f.mouse("//button[@type='submit'][contains(.,'Log in')]")
    e1 = f.find("//div[contains(@class,'message-error validation-summary-errors')]")
    if "The credentials provided are incorrect" in e1.text:
        print("OK P1")
    sleep(3)
    driver.close()

def test_login2():
    global driver
    driver = webdriver.Chrome()
    f = Funciones_Globales(driver)
    f.navigate_to("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
    f.write("//input[@id='Email']", "")
    f.mouse("//button[@type='submit'][contains(.,'Log in')]")
    e2 = f.find("(//span[contains(.,'Please enter your email')])[2]")
    if e2.text == 'Please enter your email':
        print("OK P2")
    sleep(3)
    driver.close()

def test_login3():
    global driver
    driver = webdriver.Chrome()
    f = Funciones_Globales(driver)
    f.navigate_to("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
    f.write("//input[@id='Email']", "fede")
    f.mouse("//button[@type='submit'][contains(.,'Log in')]")
    e3 = f.find("//span[@id='Email-error']")
    if e3.text == 'Wrong email':
        print("OK P3")
    sleep(3)
    driver.close()

def test_login4():
    global driver
    driver = webdriver.Chrome()
    f = Funciones_Globales(driver)
    f.navigate_to("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
    f.write("//input[@id='Email']", "admin@yourstore.com")
    f.write("//input[@id='Password']", "admin")
    f.mouse("//button[@type='submit'][contains(.,'Log in')]")
    e1 = f.find("//h1[contains(.,'Dashboard')]")
    if "Dashboard" in e1.text:
        print("OK P4")
    sleep(3)
    driver.close()