import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from PIL import Image
#import random
#import uuid
from wand.image import Image
from selenium.webdriver.common.keys import Keys
import time 

#
#chrome_service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())

chrome_options = Options()
options = [
    "--headless",
    "--disable-gpu",
    "--window-size=1400,1050",
    "--ignore-certificate-errors",
    "--disable-extensions",
    "--no-sandbox",
    "--disable-dev-shm-usage"
]
for option in options:
    chrome_options.add_argument(option)


#fill in  the brackets below: service=chrome_service
driver = webdriver.Chrome(options=chrome_options)
os.environ['PATH'] = r"C:/Devlopment/SeleniumDrivers/chromedriver.exe"
imagePath = './compImages/'
basePricingPage = './compImages/PricingRef.png'
baseAboutPage = './compImages/AboutRef.png'
baseHomePage = './compImages/HomeRef.png'
#driver = webdriver.Chrome()
driver.set_window_size(1400, 1050)
#url = "http://localhost:3000" #local
url = "https://pmafynn.github.io/BA_v1/"
driver.get(url) #local als auch 'on your network' funktioniert beides
#PATH = "C:\Devlopment\SeleniumDrivers\chromedriver.exe"
#es gibt mehrere driver, also cross browser testing maybe moeglich
def screenshotPricing():
    refImage = basePricingPage
    driver.implicitly_wait(3)
    pricing = driver.find_element("id" , "1234")
    pricing.click()
    driver.save_screenshot('./compImages/PricingComp.png')
    compImage = './compImages/PricingComp.png' #muss bei erfolg zu neuem global ref image werden
    id = 'Pricing'
    test1 = compareScreenshot(compImage, refImage, id)
    if test1 == True: 
        return True
    else:
        return False

def screenshotHome():
    refImage = baseHomePage
    driver.implicitly_wait(3)
    driver.save_screenshot('./compImages/HomeComp.png')
    compImage = './compImages/HomeComp.png' #muss bei erfolg zu neuem global ref image werden
    id = 'Home'
    test1 = compareScreenshot(compImage, refImage, id)
    if test1 == True: 
        return True
    else:
        return False

def screenshotAbout():
    refImage = baseAboutPage
    driver.implicitly_wait(3)
    about = driver.find_element("id" , "12345")
    about.click()
    driver.save_screenshot('./compImages/AboutComp.png')
    compImage = './compImages/AboutComp.png' 
    id = 'About'
    test1 = compareScreenshot(compImage, refImage, id)
    if test1 == True: 
        return True
    else:
        return False

def compareScreenshot(compImage, refImage, id):
    with Image(filename=refImage) as base:
        with Image(filename=compImage) as img:
            base.fuzz = base.quantum_range * 0  # Threshold of 20%
            result_image, result_metric = base.compare(img)
            print(result_metric, ' -- 1.0 if reference image and comparison image match. If the images do not match see https://github.com/PmaFynn/BA_v1/blob/CiServerImages/compImages/ for the resulting difference image! ' )
            #https://github.com/PmaFynn/BA_v1/blob/CiServerImages/compImages/diffImageAbout.png
            #with result_image:
                #result_image.save(filename='./compImages/diff.jpg')
    if result_metric == 1.0:
        return True
    else:
        result_image.save(filename=(f'{imagePath}diffImage{id}.png'))
        return False
 
def takeNewRefImages():
    driver.implicitly_wait(3)
    driver.save_screenshot('./compImages/HomeRef.png')
    about = driver.find_element("id" , "12345")
    about.click()
    driver.save_screenshot('./compImages/AboutRef.png')
    pricing = driver.find_element("id" , "1234")
    pricing.click()
    driver.save_screenshot('./compImages/PricingRef.png')

def takeCompAndDiffImages():
    screenshotAbout()
    screenshotHome()
    screenshotPricing()   

def main():
    sH = screenshotHome()
    sP = screenshotPricing()
    sA = screenshotAbout()
    if sA and sP and sH == True:
        #print(True)
        return True
    else:
        #print(False)
        return False



#takeNewRefImages()

#main()

#eine Funktion fuer Aenderungen der reference Variabeln waere vllt:
    #eine andere python selenium datei welche ein neues Bild macht und das als ref speichert, da immer ueberschrieben wird -> easy

#main()
#changeRefImages()


#alle neuen images als neue ref images setzen
            #maybe trivial, da die ja alle gleich sind.
        #stattdessen Gedanken druber machen, wie neue Testfaelle eingefuegt werden koennen
            #wohl moeglich eigene python datei welche das uebernimmt?