import os
import getpass as gt
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from time import sleep

def profile(ruta):
    for file in os.listdir(ruta):
        if '.default' in file:
            return file

options = Options()
options.add_argument("-profile")
usr = gt.getuser()
prof = f'/home/{usr}/snap/firefox/common/.mozilla/firefox/'
archivo = profile(prof)
options.add_argument(f'/home/{usr}/snap/firefox/common/.mozilla/firefox/{archivo}')
driver = webdriver.Firefox(options=options)
driver.get('https://google.com')
driver.maximize_window()
sleep(1)
driver.close()