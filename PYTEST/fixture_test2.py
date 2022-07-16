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
driver = ''
f = ''


@pytest.fixture(scope='module')
def setup_login_uno():
    global driver,f
    driver = webdriver.Chrome()
    f = Funciones_Globales(driver)
    f.navigate_to("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
    f.write("//input[@id='Email']", "admin@yourstore.com")
    f.write("//input[@id='Password']", "admin")
    f.mouse("//button[@type='submit'][contains(.,'Log in')]")
    print("\rIniciando login uno")
    yield
    print("\rSaliendo de login uno")
    driver.close()

@pytest.fixture(scope='module')
def setup_login_dos():
    global driver,f
    driver = webdriver.Chrome()
    f = Funciones_Globales(driver)
    f.navigate_to("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
    f.write("//input[contains(@id,'txtUsername')]", "Admin")
    f.write("//input[@id='txtPassword']", "admin123")
    f.mouse("//input[@id='btnLogin']")
    print("\rIniciando login dos")
    yield
    print("\rSaliendo de login dos")
    driver.close()

@pytest.mark.usefixtures("setup_login_uno")
def test_uno():
    f.mouse("(//p[contains(.,'Customers')])[1]")
    f.mouse("(//p[contains(.,'Customers')])[2]")
    f.write("//input[@id='SearchFirstName']", "Victoria")
    f.mouse("//button[@id='search-customers']")
    # Creando nuevo usuario
    f.mouse("//i[@class='fas fa-plus-square']")
    f.write("//input[@id='Email']", "sarasa@gmail.com")
    f.write("//input[@id='Password']", 'AsdAsd123!#')
    f.write("//input[@id='FirstName']", "Juan Carlos")
    f.write("//input[@id='LastName']", "Sarasa")
    f.mouse('//*[@id="Gender_Male"]')
    f.write('//*[@id="DateOfBirth"]', '4/4/2000')
    f.write("//input[@id='Company']", "La Poronga S.A.")
    f.mouse('//*[@id="IsTaxExempt"]')
    f.mouse("(//div[contains(@class,'k-multiselect-wrap k-floatwrap')])[1]")
    f.mouse("//li[contains(.,'Test store 2')]")
    f.select("//select[contains(@id,'VendorId')]", "1", "value")
    f.write("//textarea[@id='AdminComment']", "sarasa sarasa")
    f.mouse("(//button[@type='submit'][contains(.,'Save')])[1]")
    sleep(4)

@pytest.mark.usefixtures("setup_login_dos")
def test_dos():
    print("Entrando")