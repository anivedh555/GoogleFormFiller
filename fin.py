#!/usr/bin/python3
#https://forms.gle/11SCBq4FsgKtZaMH8


from selenium import webdriver
import random

option = webdriver.ChromeOptions()
option.add_argument("-incognito")
option.add_experimental_option("excludeSwitches", ['enable-automation']);
#option.add_argument("--headless")
#option.add_argument("disable-gpu")
browser = webdriver.Chrome(executable_path='./chromedriver', options=option)

browser.get("https://forms.gle/11SCBq4FsgKtZaMH8")


divlist=["i19","i22","i25","i28"]
yearlist=["i9","i12"]
residencelist=["i55","i58"]

name= browser.find_elements_by_class_name("quantumWizTextinputPaperinputInput")
year = browser.find_element_by_id(random.choice(yearlist))
div = browser.find_element_by_id(random.choice(divlist))

lecs = browser.find_element_by_id("i38")

pracs = browser.find_element_by_id("i48")

residence = browser.find_element_by_id(random.choice(residencelist))


parents = browser.find_element_by_id("i68")


submitbutton=browser.find_element_by_class_name("appsMaterialWizButtonPaperbuttonContent")

with open('../names.txt') as f:
    lines=f.read().splitlines()
print("Done..")

name[0].send_keys(random.choice(lines))
year.click()
div.click()
lecs.click()
pracs.click()
residence.click()
parents.click()
submitbutton.click()
browser.close()

