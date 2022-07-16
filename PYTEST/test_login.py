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
from Page_Login import Funciones_Login


def test_login_uno():
    driver = webdriver.Chrome()
    fl = Funciones_Login(driver)
    fl.login("fede@gmail.com", "123456", "No customer account found", "Usuario Erroneo OK")
    fl.login("", "1234", "Please enter your email", "Email Vacio OK")

