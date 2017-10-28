#!/usr/bin/env python3

from stem import Signal
from stem.control import Controller
from splinter import Browser
import time
import os
import signal
import subprocess


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
                  "network.proxy.http": proxyIP,
                  "network.proxy.http_port": proxyPort}
browser = Browser('firefox', profile_preferences=proxy_settings)



def checkIP():
    browser.visit("https://whoer.net/")
    ip = browser.find_by_xpath("/html/body/div[1]/div/div/div[3]/div/div[1]/div/strong").first.text
    print(ip)





checkIP()
input()


browser.quit()

