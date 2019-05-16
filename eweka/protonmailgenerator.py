#!/usr/bin/env python3


password = 'thisisgoOdpassword22$$'

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from datetime import datetime

def wait_for_xpath(xpath):
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))


def wait_for_username_check():
    while browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/p').text == "Checking username":
        sleep(0.5)

browser = webdriver.Firefox()

browser.get('https://mail.protonmail.com/create/new?language=en')

#wait for website


mail_name = "highnonymous"
mail_end_number = 6
##fill out form
username_frame_xpath = '//*[@id="mainContainer"]/div/div/div[1]/form/div[1]/div[1]/div/div/div[2]/iframe'
wait_for_xpath(username_frame_xpath)
browser.switch_to.frame(browser.find_element_by_xpath(username_frame_xpath))
wait_for_xpath('//*[@id="username"]')
browser.find_element_by_xpath('//*[@id="username"]').send_keys(mail_name + str(mail_end_number))
#check if available
wait_for_xpath('/html/body/div/div/div/div[2]')
wait_for_username_check()
is_available = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/p').text
while is_available != "Username available":
    mail_end_number += 1
    browser.find_element_by_xpath('//*[@id="username"]').clear()
    browser.find_element_by_xpath('//*[@id="username"]').send_keys(mail_name + str(mail_end_number))
    sleep(1)
    wait_for_username_check()
    is_available = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/p').text


browser.switch_to_default_content()
browser.find_element_by_name('password').send_keys(password)
browser.find_element_by_name('passwordc').send_keys(password)


##submit
browser.switch_to.frame(browser.find_element_by_xpath(username_frame_xpath))
browser.find_element_by_xpath('//*[@id="app"]/div/footer/button').click()
browser.find_element_by_id('confirmModalBtn').click()

##TODO: wait for captcha solving

browser.find_element_by_xpath('//*[@id="verification-panel"]/p[3]/button').click()


