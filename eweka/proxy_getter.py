#!/usr/bin/env python3
# get proxies from free-proxy-list.net and check them

import sys
from lxml import html
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import requests

def wait_for_100_in_check():
    print("waiting for completion")
    while browser.find_element_by_xpath('//*[@id="s_persent"]').text != "100":
        sleep(1)
    print("proceeding")

url = "https://free-proxy-list.net/"
page = requests.get(url)
max_proxies = 100

proxy_table_html = html.fromstring(page.content).xpath("//*[@id=\"proxylisttable\"]/tbody")

proxy_list = []

for row in proxy_table_html:
    proxy_table_rows = row.xpath("./tr")
    proxy_counter = 0
    for table_row in proxy_table_rows:
        table_row_items = table_row.xpath("./td")

        td_counter = 0
        proxy = []
        while td_counter < 2:
            proxy.append(table_row_items[td_counter].text)
            td_counter += 1
        proxy_list.append(tuple(proxy))
        proxy_counter += 1
        if proxy_counter >= max_proxies:
            break

proxies = []

proxy_list_string = ""

for proxy in proxy_list:
    proxy_ip_port = proxy[0] + ":" + proxy[1]
    print(proxy_ip_port)
    proxy_list_string += proxy_ip_port + "\n"
    proxies.append(proxy_ip_port)

browser = webdriver.Firefox()
browser.get('https://hidemyna.me/en/proxy-checker/')

browser.find_element_by_xpath('//*[@id="f_in"]').send_keys(proxy_list_string)
browser.find_element_by_xpath('//*[@id="chkb1"]').click()

proxy_speed_list = []

wait_for_100_in_check()









#print(proxy_check_table)
proxy_check_table = html.fromstring(browser.page_source).xpath('//*[@id="list"]/tbody')

for row in proxy_check_table:
    proxy_check_table_rows = row.xpath('./tr')
    i = 0
    for table_row in proxy_check_table_rows:
        table_row_items = table_row.xpath('./td')
        if i == 0:
            i += 1
            continue
        ##check if failed and if not for speed in ms
        speed = table_row_items[3][0][0].text
        try:
            speed = speed.split(" ")[0]
            if int(speed) > 1000:
                continue
        except:
            continue

        ip_address = table_row_items[0].text
        port = table_row_items[1].text
        proxy = ip_address + ":" + port
        proxy_speed_list.append((proxy, int(speed)))


working_proxy_string = ""

sorted_by_speed = sorted(proxy_speed_list, key=lambda x: x[1])

for entry in sorted_by_speed:
    print(entry)
    working_proxy_string += entry[0] + "\n"




with open('working_proxy_list.txt', "w") as working_proxy_file:
    working_proxy_file.write(working_proxy_string)
    working_proxy_file.close()

browser.close()

