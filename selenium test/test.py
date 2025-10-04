from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

path= "C:/Users/hp/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe"
driver=webdriver.Chrome(service=Service(path))
driver.get('http://127.0.0.1:8000/')
driver.set_window_size(1120, 1000)
print("Test Passed")
print(driver.title)


time.sleep(2)
driver.close()