import os
from selenium import webdriver
from PIL import Image
from wand.image import Image
from selenium.webdriver.common.keys import Keys
import time 

os.environ['PATH'] = r"C:/Devlopment/SeleniumDrivers/chromedriver.exe"
basePricingPage = '../testScreenshot/testScreenshot1.png'
compPricingPage = '../testScreenshot/testimage1.png'
driver = webdriver.Chrome()
url = "http://localhost:3000"
driver.get(url) #local als auch 'on your network' funktioniert beides
#PATH = "C:\Devlopment\SeleniumDrivers\chromedriver.exe"
#es gibt mehrere driver, also cross browser testing maybe moeglich
def screenshotPricing():
    driver.implicitly_wait(3)
    time.sleep(0.5)
    pricing = driver.find_element("id" , "1234")
    pricing.click()
    driver.save_screenshot('../testScreenshot/testimage1.png')
    global compPricingPage 
    compPricingPage = '../testScreenshot/testimage1.png'
    test1 = compareScreenshot()
    print(test1)
    if test1 == True: 
        return True
    else:
        return False

def screenshotPricing():
    driver.implicitly_wait(3)
    time.sleep(0.5)
    pricing = driver.find_element("id" , "12345")
    pricing.click()
    driver.save_screenshot('../testScreenshot/testimage1.png')
    global compPricingPage 
    compPricingPage = '../testScreenshot/testimage1.png'
    test1 = compareScreenshot()
    print(test1)
    if test1 == True: 
        return True
    else:
        return False

def compareScreenshot():
    with Image(filename=basePricingPage) as base:
    #with Image(filename='../testScreenshot/testScreenshot1.png') as base:
        with Image(filename=compPricingPage) as img:
            base.fuzz = base.quantum_range * 0  # Threshold of 20%
            result_image, result_metric = base.compare(img)
            print(result_metric)
            with result_image:
                result_image.save(filename='../testScreenshot/diff.jpg')
    if result_metric == 0.75:
        return True
    else:
        return False



#def main():
    sp = screenshotPricing
    #ap etc
    #if alle true dann also base images anedern

screenshotPricing()

#taking images for every page, die dann uebergeben an compare screenshot function fuer jede page <- alles in main
