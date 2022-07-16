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
    print("\rEmpezando login del sistema")
    yield
    print("\rSaliendo del sistema - Prueba OK")

@pytest.mark.usefixtures('setup_login')
def test_uno():
    print("\r--------------> Pruebas Test 1 <----------------------")


