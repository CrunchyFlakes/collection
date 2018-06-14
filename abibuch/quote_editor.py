#!/usr/bin/env python3
# replaces !CDATA \"                !!!!only run once!!!!

xml = open("/home/mtoepperwien/PycharmProjects/collection/abibuch/Zitate.xml", "r").read()





xml = xml.replace("\n\"]]></Zitat>", "\"]]></Zitat>")
xml = xml.replace("<Zitat><![CDATA[\"\"]]></Zitat>", "<Zitat><![CDATA[]]></Zitat>")
xml = xml.replace("\"]]></Zitat>", "\"platzhalterzeilenumbruchplatzhalterzeilenumbruch]]></Zitat>")
xml = xml.replace("<Zitat><![CDATA[\"", "<Zitat><![CDATA[")
xml = xml.replace("\"platzhalterzeilenumbruchplatzhalterzeilenumbruch]]></Zitat>", "platzhalterzeilenumbruchplatzhalterzeilenumbruch]]></Zitat>")



new_xml = open("/home/mtoepperwien/PycharmProjects/collection/abibuch/Zitate_final.xml", "w")

new_xml.writelines(xml)