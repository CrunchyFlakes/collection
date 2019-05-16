#!/usr/bin/env


##vipernews fake email working but often missing articles
##easyusenet fake email not working
##usenetbucket fake email not working


password = 'thisisgoOdpassword22$$'

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.proxy import Proxy, ProxyType
from time import sleep
from datetime import datetime

proxy = input("input proxy: ")

firefox_capabilities = webdriver.DesiredCapabilities.FIREFOX
firefox_capabilities['marionette'] = True


firefox_capabilities['proxy'] = {
    "proxyType": "MANUAL",
    "httpProxy": proxy,
    "ftpProxy": proxy,
    "sslProxy": proxy
}


def return_new_email():
    browser.get('https://generator.email')
    return browser.find_element_by_xpath('//*[@id="email_ch_text"]').text

browser = webdriver.Firefox(capabilities=firefox_capabilities)

mail_address = return_new_email()

browser.get('https://www.vipernews.com/sign-up/?plan=3')

browser.find_element_by_name('email').send_keys(mail_address)
browser.find_element_by_name('password').send_keys(password)
browser.find_element_by_name('confirm_password').send_keys(password)

browser.find_element_by_xpath('//*[@id="period"]/option[1]').click()

browser.find_element_by_xpath('//*[@id="signup"]/div[2]/div[2]/button').click()