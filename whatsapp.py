from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
driver = webdriver.Chrome(
    executable_path='E:\\chromedriver_win32\\chromedriver.exe')
driver.get('https://web.whatsapp.com/')
