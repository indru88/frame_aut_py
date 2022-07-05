import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
from funciones.funciones import Funciones_Globales as FG


class base_test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test1(self):
        driver = self.driver
        f = FG(driver)
        # f.navigate_to("https://demoqa.com/buttons")
        # f.mouse("//button[@id='doubleClickBtn']", "double")
        # f.mouse("//*[@id='rightClickBtn']", "right")
        # f.mouse("(//button[contains(.,'Click Me')])[3]")
        # sleep(3)

        ##

        # f.navigate_to("https://testpages.herokuapp.com/styled/drag-drop-javascript.html")
        # f.mouse_drag_and_drop("//div[@id='draggable1']", "//div[@id='droppable1']")
        # f.mouse_drag_and_drop("//div[@id='draggable2']", "//div[@id='droppable2']")
        # sleep(3)

        ##

        # f.navigate_to("https://jqueryui.com/draggable/")
        # f.mouse_drag_and_dropXY("//div[@id='draggable']", "330", "300")
        # sleep(3)

        ##
        # f.navigate_to("https://jqueryui.com/draggable/")
        # f.mouse_xy("//a[@href='https://jqueryui.com/download/']", 100, 0)
        # sleep(3)

        ##
        # f.navigate_to("https://google.com")
        # f.write("//input[@type='text']", "motos")
        # f.mouse_xy("//input[@type='text']", 0, 200)
        # sleep(3)

        ##
