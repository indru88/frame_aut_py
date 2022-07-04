import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from funciones.funciones import Funciones_Globales as FG


class base_test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test1(self):
        driver = self.driver
        f = FG(driver)
        f.navigate_to("https://demoqa.com/buttons")
        f.mouse("//button[@id='doubleClickBtn']", "double")
        f.mouse("//*[@id='rightClickBtn']", "right")
        f.mouse("(//button[contains(.,'Click Me')])[3]")
        sleep(3)
