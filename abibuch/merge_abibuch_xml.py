#!/usr/bin/env python3
# merge "alle Steckbriefe" with "Kommentare"

import xml.etree.ElementTree as ET

def return_commentlist(name):
    commentlist = []
    for person_data in kommentare_root[0]:
        person_name = str(person_data[0].text).replace("\"", "")
        if person_name == name:
            for data in person_data:
                if data.tag == "Kommentar":
                    commentlist.append(str(data[1].text))
            return commentlist

steckbriefe_tree = ET.parse('alle_Steckbriefe_without_quotes.xml')
steckbriefe_root = steckbriefe_tree.getroot()

kommentare_tree = ET.parse('Kommentare.xml')
kommentare_root = kommentare_tree.getroot()


## add comments to right person
i = 0
for steckbrief in steckbriefe_root[0]:
    name = str(steckbriefe_root[0][i][0].text)
    commentlist = return_commentlist(name)
    if not commentlist:
        print(name, ": WARNING empty list")
    else:
        print(name, ": processing")
    comments = ET.SubElement(steckbrief, "comments")
    for comment in commentlist:
        comment_subelement = ET.SubElement(comments, "comment")
        comment_subelement.text = comment
    i += 1

## sort via first name
steckbriefe_tree = ET.ElementTree(steckbriefe_root)
names = []
for rootobj in steckbriefe_tree.find('Steckbriefe').findall('Steckbrief'):
    print("here")
    #print(ET.tostring(rootobj).decode())
    #print(rootobj[0].text)
    names.append(rootobj[0].text)

newxml = ET.Element('root')
for name in sorted(names):
    print(name)
    for rootobj in steckbriefe_tree.find('Steckbriefe').findall('Steckbrief'):
        if name == rootobj.find('Name').text:
            newxml.append(rootobj)

newxml_tree = ET.ElementTree(newxml)
newxml_tree.write('alle_steckbriefe_mit_kommentaren.xml')