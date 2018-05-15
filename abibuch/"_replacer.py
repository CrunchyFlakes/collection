#!/usr/bin/env python3
# replaces !CDATA \"                !!!!only run once!!!!

xml = open("/home/mtoepperwien/Documents/alle_Steckbriefe.xml", "r").read()

xml = xml.replace("[CDATA[\"", "[CDATA[")
xml = xml.replace("\"]]", "]]")

new_xml = open("/home/mtoepperwien/Documents/alle_Steckbriefe_neu.xml", "w")

new_xml.writelines(xml)