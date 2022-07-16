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


@pytest.mark.run
def test_uno():
    a = 10
    b = 13
    assert a==b, "No son iguales"

@pytest.mark.run
def test_dos():
    a = 10
    b = 10
    assert a==b, "No son iguales"

@pytest.mark.run
def test_tres():
    a = 10
    b = 9
    assert a==b, "No son iguales"

@pytest.mark.run
def test_cuatro():
    a = 10
    b = 10
    assert a!=b, "Son iguales"
    assert a>b, "A no es mayor que B"