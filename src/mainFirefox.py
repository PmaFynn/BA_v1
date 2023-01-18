from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from PIL import Image
from wand.image import Image
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True
firefoxDriver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
imagePath = './compImages/Firefox/'
url = "https://pmafynn.github.io/BA_v1/"
firefoxDriver.get(url)

def screenshot(width, height, id, webID):
    refImage = f'{imagePath}{id}/{id}Ref{width}x{height}.png'
    firefoxDriver.implicitly_wait(3)
    button = firefoxDriver.find_element("id" , webID)
    button.click()
    firefoxDriver.save_screenshot(f'{imagePath}{id}/{id}Comp{width}x{height}.png')
    compImage = f'{imagePath}{id}/{id}Comp{width}x{height}.png' 
    id = id #maybe ohne
    imageMatch = compareScreenshot(compImage, refImage, id, width, height)
    if imageMatch == True: 
        return True
    else:
        return False

def compareScreenshot(compImage, refImage, id, width, height):
    quantumRange = 1
    if width == 1400 and height == 1050:
        quantumRange = 1.0
    elif width == 1920 and height == 1080:
        quantumRange = 1.0
    elif width == 828 and height == 1792:
        quantumRange = 0.75
    elif width == 1280 and height == 800:
        quantumRange = 0.75
    else:
        print('Resolution does not exist')
        return False
    with Image(filename=refImage) as base:
        with Image(filename=compImage) as img:
            base.fuzz = base.quantum_range * 0  # Threshold of 10%
            result_image, result_metric = base.compare(img)
            print(result_metric, ' --', quantumRange, 'if', id, '-reference image and comparison image match.' )
            #https://github.com/PmaFynn/BA_v1/blob/CiServerImages/compImages/diffImageAbout.png
            #with result_image:
                #result_image.save(filename='./compImages/diff.jpg')    
    if result_metric <= quantumRange and result_metric > quantumRange - 0.001:
        return True
    else:
        result_image.save(filename=(f'{imagePath}{id}/diffImage{id}{width}x{height}.png'))
        return False
 
def takeNewRefImages(width, height):
    firefoxDriver.set_window_size(width, height)
    firefoxDriver.implicitly_wait(3)
    button = firefoxDriver.find_element("id" , "Home")
    button.click()
    firefoxDriver.save_screenshot(f'{imagePath}Home/HomeRef{width}x{height}.png')
    button = firefoxDriver.find_element("id" , "About")
    button.click()
    firefoxDriver.save_screenshot(f'{imagePath}About/AboutRef{width}x{height}.png')
    button = firefoxDriver.find_element("id" , "Pricing")
    button.click()
    firefoxDriver.save_screenshot(f'{imagePath}Pricing/PricingRef{width}x{height}.png')

def RefForAllSizes():
    takeNewRefImages(1400, 1050)
    takeNewRefImages(1920, 1080)
    takeNewRefImages(828, 1792)
    takeNewRefImages(1280, 800)
    firefoxDriver.quit()

def mainFirefox(width, height):
    firefoxDriver.set_window_size(width, height)
    sH = screenshot(width, height, 'Home', "Home")
    sP = screenshot(width, height, 'Pricing', "Pricing")
    sA = screenshot(width, height, 'About', "About")
    if sA and sP and sH == True:
        return True
    else:
        print("Visual Regression Test for", width, height, "failed. Reverting to last commit suggested to fix it")
        return False

#RefForAllSizes()
#mainFirefox(828, 1792)
#mainFirefox(1400, 1050)
#mainFirefox(1920, 1080)
#mainFirefox(1280, 800)
#