#!/usr/bin/env python
# scraper.py
# web scraper for magicformulainvesting.com
# pulls company information from site to save time that would be spent manually typing out the info
# Gavin Inglis
# January 2019

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
import csv
import sys
import getpass

# login url for site
url = 'https://www.magicformulainvesting.com/Account/LogOn'

# declare driver as safari instance
driver = webdriver.Safari()

# go to page url
driver.get(url)

# find the input elements for logging in
username=driver.find_element_by_name("Email")
password=driver.find_element_by_name("Password")

# enter email and password. uses getpass to hide password (i.e. not using plaintext)
email=raw_input("Please enter your email for magicformulainvesting.com: ")
your_password=getpass.getpass("Please enter your password for magicformulainvesting.com:")
username.send_keys(email)
password.send_keys(your_password)

# click login button
button=driver.find_element_by_name("login")
button.click()

# sleep script for a second to allow time for page redirect
# the sleep time could be less, but I want to ensure that 
# the redirect happens. 1 extra second of runtime is still
# better than about a half hour of manual typing
time.sleep(1) # seconds

# use xpathing to find the radio button element for 50 stocks and click it
radio = driver.find_element_by_xpath('//input[@value="false" and contains(@name,"Select30")]')
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

# open csv file and declare writer
company_file=open('companies.csv','wb')
writer=csv.writer(company_file)

# find all td elements, write needed elements to file
trs=driver.find_elements_by_xpath('//table[@class="divheight screeningdata"]/tbody/tr')
for tr in trs:
    td = tr.find_elements_by_xpath(".//td")
    # encode company info as string to write to file
    company_name=td[0].get_attribute("innerHTML").encode("UTF-8")
    company_tikr=td[1].get_attribute("innerHTML").encode("UTF-8")
    # write to csv file
    writer.writerow([company_name,company_tikr])

driver.quit() 