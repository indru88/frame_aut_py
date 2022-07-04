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
        f.navigate_to("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        f.write("//input[@id='txtUsername']", "Admin")
        f.write("//input[@id='txtPassword']", "admin123")
        f.click("//input[@id='btnLogin']")
        sleep(1)
        admin = driver.find_element(By.XPATH, "//b[contains(.,'Admin')]")
        sub1 = driver.find_element(By.XPATH, "//a[@id='menu_admin_UserManagement']")
        sub2 = driver.find_element(By.XPATH, "//a[@id='menu_admin_viewSystemUsers']")

        act = ActionChains(driver)
        act.move_to_element(admin).move_to_element(sub1).move_to_element(sub2).click().perform()
        sleep(3)
        driver.close()

