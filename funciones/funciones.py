import unittest
import warnings
from time import sleep
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Funciones_Globales():

    ##
    DEFAULT_WAIT = 5
    DEFAULT_SLEEP = 0.5
    ##

    def __init__(self, driver):
        self.driver = driver

    def dormir(self):
        sleep(self.DEFAULT_SLEEP)

    def navigate_to(self, url):
        self.driver.get(url)
        print(f"Pagina Abierta: {url}")
        self.driver.maximize_window()

    def find(self, xpath, wait=DEFAULT_WAIT):
        try:
            return WebDriverWait(self.driver, wait).until(EC.visibility_of_element_located((By.XPATH, xpath)))
        except TimeoutException as err:
            print(err.msg)
            self.driver.close()

    def scroll(self, xpath):
        element = self.find(xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)


    def write(self, xpath, text):
        element = self.find(xpath)
        self.scroll(xpath)
        self.dormir()
        element.clear()
        element.send_keys(text)
        print(f"Escribiendo en el elemento {xpath} el texto -> {text}")

    def click(self, xpath):
        element = self.find(xpath)
        self.scroll(xpath)
        self.dormir()
        element.click()
        print(f"Click en el elemento {xpath}")

    def select(self, xpath, val, tipo="index"):
        element = self.find(xpath)
        self.scroll(xpath)
        element = Select(element)
        match tipo:
            case "text":
                element.select_by_visible_text(val)
            case "value":
                element.select_by_value(val)
            case "index":
                element.select_by_index(val)
        print(f"El elemento seleccionado en {xpath} por {tipo} es -> {val}")

    def upload(self, xpath, ruta):
        element = self.find(xpath)
        self.scroll(xpath)
        element.send_keys(ruta)
        print(f"Se carga la imagen de la ruta -> {ruta}")

    def salida(self):
        self.driver.close()
        print("Se termina la prueba exitosamente")

    def re_pag(self, n=-1):
        self.driver.execute_script(f"window.history.go({n})")
        self.dormir()

    def av_pag(self, n=1):
        self.driver.execute_script(f"window.history.go({n})")
        self.dormir()

    # Selecciones Multiples
    def check_multiples(self, *xpaths):
        for n in xpaths:
            element = self.find(n)
            self.scroll(n)
            self.dormir()
            element.click()

    # Mouse Actions
    def mouse(self, xpath, tipo="left"):
        element = self.find(xpath)
        self.scroll(xpath)
        act = ActionChains(self.driver)
        match tipo:
            case "double":
                act.double_click(element).perform()
            case "right":
                act.context_click(element).perform()
            case "left":
                act.click(element).perform()
        self.dormir()