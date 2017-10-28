#!/usr/bin/env python3

from stem import Signal
from stem.control import Controller
from splinter import Browser
import time
import os
import signal
import subprocess


# specify email here !!!
email = "imhidden@protonmail.com"

# open torbrowser
torbrowser = subprocess.Popen("tor-browser-en.sh", stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid)
time.sleep(3)


switch_counter = 0
proxyIP = "127.0.0.1"
proxyPort = 9150

# proxy_settings = {"network.proxy.type": 1,
#                   "network.proxy.ssl": proxyIP,
#                   "network.proxy.ssl_port": proxyPort,
#                   "network.proxy.socks": proxyIP,
#                   "network.proxy.socks_port": proxyPort,
#                   "network.proxy.socks_remote_dns": True,
#                   "network.proxy.ftp": proxyIP,
#                   "network.proxy.ftp_port": proxyPort
#                   }

proxy_settings = {"network.proxy.type": 1,
                  "network.proxy.socks": proxyIP,
                  "network.proxy.socks_port": proxyPort}
browser = Browser('firefox', profile_preferences=proxy_settings)

def fillIn():
    browser.visit("https://www.eweka.nl/en/free_trial/")
    browser.fill("email", email)
    button = browser.find_by_name("submit")
    button.click()


def checkIP():
    browser.visit("https://whoer.net/")
    ip = browser.find_by_xpath("/html/body/div[1]/div/div/div[3]/div/div[1]/div/strong").first.text
    print(ip)


#fillIn()

already_used = None
try:
    already_used = browser.find_by_xpath("/html/body/div[1]/div[2]/div/div/div/form/div/p/strong").first.text
    already_used = True
except:
    already_used = None


def switchIP():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate()
        controller.signal(Signal.NEWNYM)
        newnym_wait = controller.get_newnym_wait()
        print("wait: " + str(int(newnym_wait)))
        time.sleep(newnym_wait)


while True:
    switchIP()
    checkIP()
    #fillIn()
    try:
        already_used = browser.find_by_xpath("/html/body/div[1]/div[2]/div/div/div/form/div/p/strong").first.text
        already_used = True
        switch_counter += 1
    except:
        already_used = None


browser.quit()
print(str(switch_counter))
time.sleep(1)
# kill torbrowser
os.killpg(os.getpgid(torbrowser.pid), signal.SIGTERM)
