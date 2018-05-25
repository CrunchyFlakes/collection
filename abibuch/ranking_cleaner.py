#!/usr/bin/env python3
# clean everything except of the quotes

import xml.etree.ElementTree as ET

abstimmungen_tree = ET.parse('Rankings_without_quotes.xml')
abstimmungen_root = abstimmungen_tree.getroot()

newxml = ET.Element('root')

questions = abstimmungen_root[0][0][3]

question_counter = 0

for question in questions.findall('Frage'):
    question_sub = ET.SubElement(newxml, "Frage")
    question_counter += 1


    title_sub = ET.SubElement(question_sub, 'Titel')
    title_sub.text = question.find('Text').text + "platzhalterzeilenumbruch"
    print()
    print(title_sub.text)

    i = 0
    for placement in question.findall('Platzierung'):
        if int(placement.find('Platz').text) == 0:
            name_sub = ET.SubElement(question_sub, 'Name')
            name_sub.text = placement.find('Name').text + "platzhalterzeilenumbruch"
            print(name_sub.text)
        else:
            if i < 3:
                name_sub = ET.SubElement(question_sub, 'Name')
                name_sub.text = placement.find('Platz').text + ". " + placement.find('Name').text + "platzhalterzeilenumbruch"
                print(name_sub.text)
                i += 1



print("\n-----------\nnumber of questions: " + str(question_counter))
newxml_tree = ET.ElementTree(newxml)
newxml_tree.write('Rankings_cleaned.xml')
