#!/usr/bin/env python3


import lxml
from lxml.html import parse
from urllib.request import urlopen
import subprocess

title = lxml.html.parse(urlopen("https://forum.xda-developers.com/oneplus-6/development/kernel-t3800965")).findtext(".//title")

file = open("blu_spark_version.txt", "r")

version_installed = file.readline()
file.close()

version_index = title.find("blu_spark r")
string_length = 13
version = title[version_index:version_index + 13]

if version_installed == version:
    print("newest version installed: " + version_installed)
else:
    print("new version: " + version)
    print("current version: " + version_installed)
    notification_command = "termux-notification -t \"blu_spark Update\" -c \"New version " + version + "\" --action \"termux-open-url https://forum.xda-developers.com/devdb/project/?id=27466#downloads\""
    notification = subprocess.Popen(notification_command, shell=True)
    file = open("blu_spark_version.txt", "w")
    file.writelines(version)
    file.close()




