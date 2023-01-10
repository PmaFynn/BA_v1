import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 

os.environ['PATH'] = r"C:/Devlopment/SeleniumDrivers/chromedriver.exe"
#PATH = "C:\Devlopment\SeleniumDrivers\chromedriver.exe"
#es gibt mehrere driver, also cross browser testing maybe moeglich
def test():
    driver = webdriver.Chrome()
    driver.get("http://localhost:3000") #local als auch 'on your network' funktioniert beides
    driver.implicitly_wait(3)
    time.sleep(0.5)
    pricing = driver.find_element("id" , "1234")
    pricing.click()
    while(True):
       pass
test()
