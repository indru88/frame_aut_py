import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from PO.funciones.funciones import Funciones_Globales


class PageLogin():
    def __init__(self, driver):
        self.driver = driver
        self.f = Funciones_Globales(self.driver)

    def page_login(self, url):
        f = self.f
        f.navigate_to(url)

    def login_master(self, url, xpath_usr, usr, xpath_psw, psw, xpath_btn):
        f = self.f
        self.page_login(url)
        f.write(xpath_usr,usr)
        f.write(xpath_psw,psw)
        f.click(xpath_btn)
        f.salida()
