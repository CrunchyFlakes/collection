#!/usr/bin/env python3


xml = open("Rankings.xml", "r").read()


xml = xml.replace("\n\"</comment>", "\"</comment>")
xml = xml.replace("</comment>", "platzhalterzeilenumbruch</comment>")
xml = xml.replace("</Frage>", "platzhalterzeilenumbruch</Frage>")


new_xml = open("Rankings_without_quotes.xml", "w")

new_xml.writelines(xml)