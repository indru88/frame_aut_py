import allure
import pytest
from time import sleep

from allure_commons.types import AttachmentType
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

def get_data():
   return [
       ("rodrigo", "123"),
       ("Admin", "admin123"),
   ]

@pytest.fixture()
def log_on_failure(request):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="Error", attachment_type=AttachmentType.PNG)

@pytest.mark.login
@pytest.mark.usefixtures("log_on_failure")
@pytest.mark.parametrize("usr,psw", get_data())
def test_login(usr, psw):
    global driver
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
    driver.maximize_window()
    driver.implicitly_wait(20)
    f = Funciones_Globales(driver)
    f.write("//input[@id='txtUsername']", usr)
    f.write("//input[@id='txtPassword']", psw)
    f.mouse("//input[@id='btnLogin']")
    if usr != 'Admin':
        assert 2==3

def teardown_function():
    print("FIN")
    driver.close()