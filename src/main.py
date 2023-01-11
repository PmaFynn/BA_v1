import os
from selenium import webdriver
from PIL import Image
#import random
#import uuid
from wand.image import Image
from selenium.webdriver.common.keys import Keys
import time 

os.environ['PATH'] = r"C:/Devlopment/SeleniumDrivers/chromedriver.exe"
imagePath = './compImages/'
basePricingPage = './compImages/PricingRef.png'
baseAboutPage = './compImages/AboutRef.png'
baseHomePage = './compImages/HomeRef.png'
driver = webdriver.Chrome()
driver.set_window_size(1400, 1050)
url = "http://localhost:3000"
driver.get(url) #local als auch 'on your network' funktioniert beides

#PATH = "C:\Devlopment\SeleniumDrivers\chromedriver.exe"
#es gibt mehrere driver, also cross browser testing maybe moeglich
def screenshotPricing():
    refImage = basePricingPage
    driver.implicitly_wait(3)
    time.sleep(0.5)
    pricing = driver.find_element("id" , "1234")
    pricing.click()
    driver.save_screenshot('./compImages/PricingComp.png')
    compImage = './compImages/PricingComp.png' #muss bei erfolg zu neuem global ref image werden
    id = 'Pricing'
    test1 = compareScreenshot(compImage, refImage, id)
    #print(test1)
    if test1 == True: 
        return True
    else:
        return False

def screenshotHome():
    refImage = baseHomePage
    driver.implicitly_wait(3)
    time.sleep(0.5)
    driver.save_screenshot('./compImages/HomeComp.png')
    compImage = './compImages/HomeComp.png' #muss bei erfolg zu neuem global ref image werden
    id = 'Home'
    test1 = compareScreenshot(compImage, refImage, id)
    #print(test1)
    if test1 == True: 
        return True
    else:
        return False

def screenshotAbout():
    refImage = baseAboutPage
    driver.implicitly_wait(3)
    time.sleep(0.5)
    about = driver.find_element("id" , "12345")
    about.click()
    driver.save_screenshot('./compImages/AboutComp.png')
    compImage = './compImages/AboutComp.png' #muss bei erfolg zu neuem global ref image werden
    id = 'About'
    test1 = compareScreenshot(compImage, refImage, id)
    #print(test1)
    if test1 == True: 
        return True
    else:
        return False

def compareScreenshot(compImage, refImage, id):
    with Image(filename=refImage) as base:
        with Image(filename=compImage) as img:
            base.fuzz = base.quantum_range * 0  # Threshold of 20%
            result_image, result_metric = base.compare(img)
            print(result_metric)
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

def main():
    sH =screenshotHome()
    sP = screenshotPricing()
    sA = screenshotAbout()
    if sA and sP and sH == True:
        print(True)
        return True
    else:
        print(False)
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