#!/usr/bin/env python3
# replaces !CDATA \"                !!!!only run once!!!!

xml = open("/home/mtoepperwien/PycharmProjects/collection/abibuch/alle_Steckbriefe.xml", "r").read()


xml = xml.replace("![CDATA[\"", "![CDATA[")
xml = xml.replace("\"]]", "]]")


# xml = xml.replace("\n\"</comment>", "\"</comment>")
# xml = xml.replace("</comment>", "platzhalterzeilenumbruch</comment>")
# xml = xml.replace("</Frage>", "platzhalterzeilenumbruch</Frage>")


new_xml = open("/home/mtoepperwien/PycharmProjects/collection/abibuch/alle_Steckbriefe_without_quotes.xml", "w")

new_xml.writelines(xml)