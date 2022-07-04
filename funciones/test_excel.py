import unittest
from time import sleep
from funciones_excel import *
from selenium import webdriver
from funciones import Funciones_Globales as FG


class base_test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test1(self):
        f = FG(self.driver)
        fe = FuncionesExcel(self.driver)
        f.navigate_to("https://demoqa.com/text-box")
        ruta = "//home//fede//PycharmProjects//pythonProject1//src//ejemplo.xlsx"
        filas = fe.get_row_count(ruta, "Hoja1")
        for r in range(2, filas+1):
            f.write("//input[@id='userName']", fe.read_data(ruta, "Hoja1", r, 1))
            f.write("//input[@id='userEmail']", fe.read_data(ruta, "Hoja1", r, 2))
            f.write("//textarea[@id='currentAddress']", fe.read_data(ruta, "Hoja1", r, 3))
            f.write("//textarea[@id='permanentAddress']", fe.read_data(ruta, "Hoja1", r, 4))
            f.click("//button[@id='submit']")
            sleep(2)