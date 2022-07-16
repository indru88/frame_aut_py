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

class Funciones_Login():
    def __init__(self, driver):
        self.driver = driver

    def login1(self, email, clave, message, prueba):
        driver = self.driver
        f = Funciones_Globales(driver)
        f.navigate_to("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
        f.write("//input[@id='Email']", email)
        f.write("//input[@id='Password']", clave)
        f.mouse("//button[@type='submit'][contains(.,'Log in')]")
        e1 = f.find("/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[1]/ul/li")
        if e1.text == message:
            print(f"Prueba -> {prueba} -> OK")
        else:
            print(f"Prueba -> {prueba} -> FAIL")
        sleep(3)
        driver.close()

    def test_login2(self, email, clave, message, prueba):
        driver = self.driver
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

