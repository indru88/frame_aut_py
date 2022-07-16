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


@pytest.fixture(scope='module')
def setup_login():
    global driver,f
    driver = webdriver.Chrome()
    f = Funciones_Globales(driver)
    f.navigate_to("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
    f.write("//input[contains(@id,'txtUsername')]", "Admin")
    f.write("//input[@id='txtPassword']", "admin123")
    f.mouse("//input[@id='btnLogin']")

def teardown_function():
    driver.close()

# @pytest.mark.login
@pytest.mark.usefixtures("setup_login")
def test_uno():
    etiqueta = f.find("//h1[contains(.,'Dashboard')]")
    assert etiqueta.text == "Dashboard", "No encontro el h1"