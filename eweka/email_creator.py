#!/usr/bin/env

from splinter import Browser
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from lxml import html

standard_password = "idontmindthis22"


email_page = "https://app.tutanota.com/#register"
new_mail = "highnonymous_1"

browser = Browser('firefox')

browser.visit(email_page)





not_clickable = True
while not_clickable:
    try:
        browser.find_by_id('termsInput').click()
        not_clickable = None
    except:
        print("waiting")
        time.sleep(0.5)

email_taken = True
while email_taken:
    print("insert: " + new_mail)
    browser.find_by_id('mailAddress').fill(new_mail)
    if browser.driver.page_source.__contains__("not available"):
        new_mail_split = new_mail.split("_")
        number = int(new_mail_split[1]) + 1
        new_mail = new_mail_split[0] + "_" + str(number)
        print(new_mail)
    elif browser.driver.page_source.__contains__("Email address available"):
        email_taken = None
    else:
        time.sleep(5)


browser.find_by_id('newpassword').fill(standard_password)
browser.find_by_id('newpassword2').fill(standard_password)


not_clickable = True
while not_clickable:
    try:
        if browser.is_text_present("Verifying email address"):
            time.sleep(1)
            print("waiting")
        else:
            browser.find_by_xpath("/html/body/div[2]/div[1]/div[8]/div/form/div[7]/div[2]/button[1]").click()
            not_clickable = None
    except:
        print("waiting")
        time.sleep(0.5)