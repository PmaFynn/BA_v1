from main import CompImages
import os
from selenium import webdriver

os.environ['PATH'] = r"C:/Devlopment/SeleniumDrivers/chromedriver.exe"

#CompImages.main(webdriver.Chrome(), 'http://localhost:3000/')

testwebsite = CompImages(
    './compImages/',
    './compImages/PricingRef.png',
    './compImages/AboutRef.png',
    './compImages/HomeRef.png',
    webdriver.Chrome(),
    'http://localhost:3000/'   
)
testwebsite.main('http://localhost:3000/')