#!/usr/bin/env python3

password = 'thisisgoOdpassword22$$'

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from datetime import datetime

def wait_for_profile_page(driver):
    element = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"logo\"]/table/tbody/tr/td[1]/a/img")))


proxy = input("input proxy: ")

firefox_capabilities = webdriver.DesiredCapabilities.FIREFOX
firefox_capabilities['marionette'] = True


firefox_capabilities['proxy'] = {
    "proxyType": "MANUAL",
    "httpProxy": proxy,
    "ftpProxy": proxy,
    "sslProxy": proxy
}

profile = webdriver.FirefoxProfile()
profile.set_preference("browser.privatebrowsing.autostart", True)


browser = webdriver.Firefox(capabilities=firefox_capabilities, firefox_profile=profile)
browser.get('https://generator.email')


mail_address = browser.find_element_by_xpath('//*[@id="email_ch_text"]').text

browser.get('https://nzbgeek.info/member.php?action=register')

browser.find_element_by_name('agree').click()

browser.find_element_by_name('username').send_keys(mail_address)
browser.find_element_by_name('password').send_keys(password)
browser.find_element_by_name('password2').send_keys(password)
browser.find_element_by_name('email').send_keys(mail_address)
browser.find_element_by_name('email2').send_keys(mail_address)

captcha_frame = browser.find_element_by_xpath('//iframe[contains(@src, "recaptcha")]')
browser.switch_to_frame(captcha_frame)
print("waiting for captcha completion...")
while browser.find_element_by_xpath('//*[@id="recaptcha-anchor"]').get_attribute('aria-checked') != 'true':
    sleep(1)
browser.switch_to_default_content()
sleep(4)

browser.find_element_by_name('regsubmit').click()


wait_for_profile_page(browser)

##save login data
with open('login_information.txt', "a") as login_information_file:
    timestamp = datetime.now().strftime('%d.%m.%Y  %H:%M')
    login_information_file.write(timestamp + "    " + mail_address + ":" + password + "\n")
    login_information_file.close()

browser.get('https://nzbgeek.info/vigsubscription.php')
browser.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/div[2]/center/table/tbody/tr/td[1]/form').click()

wait_for_profile_page(browser)

browser.get('https://nzbgeek.info/geekseek.php?profile')
text_with_api_key = browser.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div/div[2]/center/div/form/div/div[2]/table/tbody/tr[4]/td/table/tbody/tr/td[3]/font[10]').text
api_key = text_with_api_key.split("\n")[0].split(" ")[-1]
print(api_key)
browser.close()



