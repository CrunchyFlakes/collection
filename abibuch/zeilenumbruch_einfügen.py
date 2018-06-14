#!/usr/bin/env python3


xml = open("/home/mtoepperwien/PycharmProjects/collection/abibuch/alle_steckbriefe_mit_kommentaren.xml", "r").read()


xml = xml.replace("\n\"</comment>", "\"</comment>")
xml = xml.replace("</comment>", "platzhalterzeilenumbruch</comment>")
xml = xml.replace("</Frage>", "platzhalterzeilenumbruch</Frage>")


new_xml = open("/home/mtoepperwien/PycharmProjects/collection/abibuch/alle_steckbriefe_final.xml", "w")

new_xml.writelines(xml)