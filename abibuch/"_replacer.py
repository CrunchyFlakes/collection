#!/usr/bin/env python3
# replaces !CDATA \"                !!!!only run once!!!!

xml = open("/home/mtoepperwien/PycharmProjects/collection/abibuch/alle_steckbriefe_mit_kommentaren_before_return.xml", "r").read()


xml = xml.replace("![CDATA[\"", "![CDATA[")
xml = xml.replace("\"]]", "]]")


xml = xml.replace("\n\"</comment>", "\"</comment>")
xml = xml.replace("</comment>", "platzhalterzeilenumbruch</comment>")
xml = xml.replace("</Frage>", "platzhalterzeilenumbruch</Frage>")


new_xml = open("/home/mtoepperwien/PycharmProjects/collection/abibuch/alle_Steckbriefe_return_testing.xml", "w")

new_xml.writelines(xml)