import os
from selenium import webdriver
from PIL import Image
from wand.image import Image
from selenium.webdriver.common.keys import Keys
import time 

os.environ['PATH'] = r"C:/Devlopment/SeleniumDrivers/chromedriver.exe"
#PATH = "C:\Devlopment\SeleniumDrivers\chromedriver.exe"
#es gibt mehrere driver, also cross browser testing maybe moeglich
def main():
    driver = webdriver.Chrome()
    #orginal_size = driver.get_window_size()
    url = "http://localhost:3000"
    driver.get(url) #local als auch 'on your network' funktioniert beides
    driver.implicitly_wait(3)
    time.sleep(0.5)
    pricing = driver.find_element("id" , "1234")
    pricing.click()
    driver.save_screenshot('../testScreenshot/testimage1.png')
    compareScreenshot()
    #screenshot = Image.open('../testScreenshot/testScreenshot1.png')
    #screenshot.show()

def compareScreenshot():
    with Image(filename='../testScreenshot/testScreenshot1.png') as base:
        with Image(filename='../testScreenshot/testimage1.png') as img:
            base.fuzz = base.quantum_range * 0  # Threshold of 20%
            result_image, result_metric = base.compare(img)
            print(result_metric)
            with result_image:
                result_image.save(filename='../testScreenshot/diff.jpg')

main()


