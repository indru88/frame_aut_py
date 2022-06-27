import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from funciones.funciones import Funciones_Globales as FG
from funciones.page_login import Page_Login

class base_test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test1(self):
        f = FG(self.driver)
        f.navigate_to("https://libgen.is/")
        f.check_multiples("//input[@type='radio' and @value='md5']","//input[@type='radio' and @value='fiction']","//input[@type='radio' and @name='phrase' and @value=0]")


        sleep(2)
        # PL = Page_Login(self.driver)
        # PL.login_master("https://www.saucedemo.com/","//input[@id='user-name']","standard_user","//input[@id='password']","secret_sauce","//input[@id='login-button']")
    #    f.navigate_to('https://saucedemo.com')
    #    f.write("//input[contains(@id,'user-name')]", 'asd')
    #    f.write("//input[@id='password']", "asdas")
    #    f.click("//input[@id='login-button']")
    #    sleep(2)
    #    self.driver.close()
