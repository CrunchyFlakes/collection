#!/usr/bin/env python3
#get new files uploaded on studip and log files already downloaded

from bs4 import BeautifulSoup
from selenium import webdriver
import os
from datetime import datetime

from selenium.webdriver.support.wait import WebDriverWait

USERNAME = "5WM-9M0"
format = "%d.%m.%Y %H:%M:%S"


def wait_for_downloads(driver):
    def every_download(driver):
        if not driver.current_url.startswith("chrome://downloads"):
            driver.get("chrome://downloads/")
        return driver.execute_script("""
                var items = downloads.Manager.get().items_;
                if (items.every(e => e.state === "COMPLETE"))
                    return items.map(e => e.fileUrl || e.file_url);
                """)

    WebDriverWait(driver, 120, 1)


def split_object_into_array(object):
    return str(object).split("\n")


def get_inside_quotes(string):
    return string.split("\"")[1]


def get_second_inside_quotes(string):
    return string.split("\"")[3]


def convert_string_to_datetime(time_string):
    return datetime.strptime(time_string, format)


file_list_url = "https://studip.uni-hannover.de/dispatch.php/widgets/execute/14303/28601/list"
browser = webdriver.Chrome()
browser.get(file_list_url)

#click on login
login_element = browser.find_element_by_class_name("login_link")
login_element.click()

#input username
username_field = browser.find_element_by_id("username")
username_field.send_keys(USERNAME)

#click into password box and wait for user to login
password_field = browser.find_element_by_id("password")
password_field.click()
print("please input password and login!")

#check if user logged in
input("press enter after you logged in.")

#go to file list
browser.get(file_list_url)

#logic for
soup = BeautifulSoup(browser.page_source, 'html.parser')

file_entries = soup.find('tbody').find_all('tr')

#TODO read log file and save
last_download_timestamp = None
try:
    time_stamp = open("time_stamp_files.txt","r")
    last_download_timestamp = convert_string_to_datetime(time_stamp.readline())
except:
    last_download_timestamp = datetime.strptime("01.01.1000 01:01:01", format)

#every entry one file as array
# [0] timestamp as datetime [1] file_link [2] file_source [3] file_reference
file_data = []
for file_entry in file_entries:
    file_split = split_object_into_array(file_entry)

    file_reference = get_inside_quotes(file_split[0])

    file_source = get_inside_quotes(file_split[16]).replace(" ", "_")

    time_stamp = get_second_inside_quotes(file_split[20])
    time_stamp = convert_string_to_datetime(time_stamp)

    file_site = get_second_inside_quotes(file_split[6])
    browser.get(file_site)
    file_link = browser.find_element_by_css_selector("#layout_content > footer > a").get_property("href")

    #break if older or same than last downloaded item (all older files will be ignored)
    if last_download_timestamp >= time_stamp:
        break

    data = [time_stamp, file_link, file_source, file_reference]
    file_data.append(data)


for file in file_data:
    browser.get(file[1])


wait_for_downloads(browser)

browser.close()

last_download_timestamp = file_data[0][0].strftime(format)
time_stamp = open("time_stamp_files.txt", "w")
time_stamp.write(last_download_timestamp)
time_stamp.close()