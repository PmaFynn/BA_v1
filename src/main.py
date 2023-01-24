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
#driver = webdriver.Chrome() #So sehe ich den driver
driver = webdriver.Chrome(options=chrome_options) #so nicht
os.environ['PATH'] = r"C:/Devlopment/SeleniumDrivers/chromedriver.exe"
imagePath = './compImages/'
imagePath2 = '/compImages/'
#driver = webdriver.Chrome()
#driver.set_window_size(1400, 1050)
#url = "http://localhost:3000" #local
url = "https://pmafynn.github.io/BA_v1/"
driver.get(url) #local als auch 'on your network' funktioniert beides
#PATH = "C:\Devlopment\SeleniumDrivers\chromedriver.exe"
#es gibt mehrere driver, also cross browser testing maybe moeglich

def screenshot(width, height, id, webID):
    refImage = f'{imagePath}{id}/{id}Ref{width}x{height}.png'
    driver.implicitly_wait(3)
    button = driver.find_element("id" , webID)
    button.click()
    driver.save_screenshot(f'{imagePath}{id}/{id}Comp{width}x{height}.png')
    compImage = f'{imagePath}{id}/{id}Comp{width}x{height}.png' 
    id = id #maybe ohne
    imageMatch = compareScreenshot(compImage, refImage, id, width, height)
    if imageMatch == True: 
        return True
    else:
        return False

def screenshotPricing(width, height):
    refImage = f'{imagePath}PricingRef.png'
    driver.implicitly_wait(3)
    pricing = driver.find_element("id" , "1234")
    pricing.click()
    driver.save_screenshot(f'{imagePath}PricingComp{width}{height}.png')
    compImage = f'{imagePath}PricingComp{width}{height}.png' #muss bei erfolg zu neuem global ref image werden
    id = 'Pricing'
    test1 = compareScreenshot(compImage, refImage, id, width, height)
    if test1 == True: 
        return True
    else:
        return False

def screenshotHome(width, height):
    refImage = f'{imagePath}HomeRef.png'
    driver.implicitly_wait(3)
    driver.save_screenshot(f'{imagePath}HomeComp{width}{height}.png')
    compImage = f'{imagePath}HomeComp{width}{height}.png' #muss bei erfolg zu neuem global ref image werden
    id = 'Home'
    test1 = compareScreenshot(compImage, refImage, id, width, height)
    if test1 == True: 
        return True
    else:
        return False

def screenshotAbout(width, height):
    refImage = f'{imagePath}AboutRef.png'
    driver.implicitly_wait(3)
    about = driver.find_element("id" , "12345")
    about.click()
    driver.save_screenshot(f'{imagePath}AboutComp{width}{height}.png')
    compImage = f'{imagePath}AboutComp{width}{height}.png' #muss bei erfolg zu neuem global ref image werden
    id = 'About'
    test1 = compareScreenshot(compImage, refImage, id, width, height)
    #print(test1)
    if test1 == True: 
        return True
    else:
        return False

def compareScreenshot(compImage, refImage, id, width, height):
    quantumRange = 1
    if width == 1400 and height == 1050:
        quantumRange = 1.0
    elif width == 1920 and height == 1080:
        quantumRange = 0.75
    elif width == 828 and height == 1792:
        quantumRange = 0.75
    elif width == 1280 and height == 800:
        quantumRange = 0.75
    else:
        print('Resolution does not exist')
        return False
    with Image(filename=refImage) as base:
        with Image(filename=compImage) as img:
            base.fuzz = base.quantum_range * 0  # Threshold of 20%
            result_image, result_metric = base.compare(img)
            print(result_metric, ' --', quantumRange, 'if', id, f'-reference image and comparison image match. Difference images can be seen at https://github.com/PmaFynn/BA_v1/tree/dev{imagePath2}{id}' )
            #https://github.com/PmaFynn/BA_v1/blob/CiServerImages/compImages/diffImageAbout.png
            #with result_image:
                #result_image.save(filename='./compImages/diff.jpg')    
    if result_metric == quantumRange:
        return True
    else:
        result_image.save(filename=(f'{imagePath}{id}/diffImage{id}{width}x{height}.png'))
        return False
 
def takeNewRefImages(width, height):
    driver.set_window_size(width, height)
    driver.implicitly_wait(3)
    button = driver.find_element("id" , "Home")
    button.click()
    driver.save_screenshot(f'{imagePath}Home/HomeRef{width}x{height}.png')
    button = driver.find_element("id" , "About")
    button.click()
    driver.save_screenshot(f'{imagePath}About/AboutRef{width}x{height}.png')
    button = driver.find_element("id" , "Pricing")
    button.click()
    driver.save_screenshot(f'{imagePath}Pricing/PricingRef{width}x{height}.png')

def RefForAllSizes():
    takeNewRefImages(1400, 1050)
    takeNewRefImages(1920, 1080)
    takeNewRefImages(828, 1792)
    takeNewRefImages(1280, 800)

def main(width, height):
    driver.set_window_size(width, height)
    sH = screenshot(width, height, 'Home', "Home")
    sP = screenshot(width, height, 'Pricing', "Pricing")
    sA = screenshot(width, height, 'About', "About")
    if sA and sP and sH == True:
        #print(True)
        return True
    else:
        print("Visual Regression Test for", width, height, "failed. Reverting to last commit suggested to fix it")
        return False

def takeImagesForPush():
    driver.set_window_size(1400, 1050)
    sh = screenshot(1400, 1050, 'Home', "Home")
    sp = screenshot(1400, 1050, 'Pricing', "Pricing")
    sa = screenshot(1400, 1050, 'About', "About")
    if sa and sp and sh == True:
        x1 = True
    driver.set_window_size(1920, 1080)
    sh = screenshot(1920, 1080, 'Home', "Home")
    sp = screenshot(1920, 1080, 'Pricing', "Pricing")
    sa = screenshot(1920, 1080, 'About', "About")
    if sa and sp and sh == True:
        y1 = True   
    driver.set_window_size(828, 1792)
    sh = screenshot(828, 1792, 'Home', "Home")
    sp = screenshot(828, 1792, 'Pricing', "Pricing")
    sa = screenshot(828, 1792, 'About', "About")
    if sa and sp and sh == True:
        y1 = True
    driver.set_window_size(1280, 800)
    sh = screenshot(1280, 800, 'Home', "Home")
    sp = screenshot(1280, 800, 'Pricing', "Pricing")
    sa = screenshot(1280, 800, 'About', "About")
    if sa and sp and sh == True:
        z1 = True
    if z1 and x1 and y1 == True:
        print("VRT has been succesfull")
        return True
    else:
        print ("VRT has failed -> Revert to last working commit suggested")
        return True 

takeImagesForPush()

#takeNewRefImages()
#RefForAllSizes()
#main()

#eine Funktion fuer Aenderungen der reference Variabeln waere vllt:
    #eine andere python selenium datei welche ein neues Bild macht und das als ref speichert, da immer ueberschrieben wird -> easy

#main()
#changeRefImages()


#alle neuen images als neue ref images setzen
            #maybe trivial, da die ja alle gleich sind.
        #stattdessen Gedanken druber machen, wie neue Testfaelle eingefuegt werden koennen
            #wohl moeglich eigene python datei welche das uebernimmt?