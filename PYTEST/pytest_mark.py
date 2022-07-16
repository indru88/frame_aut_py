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
    print("Test uno")

@pytest.mark.run
def test_dos():
    print("Test dos")

@pytest.mark.notrun
def test_tres():
    print("Test tres")

@pytest.mark.notrun
def test_cuatro():
    print("Test cuatro")

@pytest.mark.notrun
def test_lalala():
    print("Test cuatro")