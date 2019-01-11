#!/usr/bin/env python
import requests
from lxml import html
import urllib2
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

url = 'https://www.magicformulainvesting.com/Account/LogOn'

driver = webdriver.Safari()

# Go to your page url
driver.get(url)

username=driver.find_element_by_name("Email")
password=driver.find_element_by_name("Password")

## ENTER YOUR EMAIL AND PASSWORD
username.send_keys("EMAIL")
password.send_keys("PASSWORD")

button=driver.find_element_by_name("login")
button.click()

'''
This is where i could wait explicitly for the element to appear. will do implicitly for now
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((ID, "myDynamicElement"))
    )
finally:
    driver.quit()
'''
#url = 'https://www.magicformulainvesting.com/Screening/StockScreening'
driver.implicitly_wait(10) # seconds
time.sleep(.1)

print(driver.current_url) #check redirect

## TODO: add clicking for 50 button. default is 30
# an error is often reached here. the script usually works fine but will sometimes catch on line 47/48
#radio = driver.find_element_by_xpath('//input[@value="false" and contains(@name,"Select30")]')
radio = driver.find_element_by_xpath('//input[@name="Select30" and contains(@value,"false")]')
radio.click()

button2=driver.find_element_by_name("stocks")
button2.click()

time.sleep(.5)

# this gets 15 of all companies and tickers
# to get all 30 i would need to follow the following hierarchy
# --> table class = divheight screeningdata
#     --> tbody
#         --> tr (all trs, not just class=altrow
# update: done below using xpath!

trs=driver.find_elements_by_xpath('//table[@class="divheight screeningdata"]/tbody/tr')

for tr in trs:
    td = tr.find_elements_by_xpath(".//td")
    print td[0].get_attribute("innerHTML").encode("UTF-8") +"\t"+td[1].get_attribute("innerHTML").encode("UTF-8")

time.sleep(2)
driver.quit() 