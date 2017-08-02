#!/usr/bin/env python3
# scrape football match dates and add them to calendar

from lxml import html
import requests

page = requests.get("http://www.fussball.de/mannschaft/sv-teutonia-gross-lafferde-sv-teutonia-gross-lafferde-niedersachsen/-/saison/1718/team-id/012NAV1I3G000000VV0AG811VUPV8FHO#!/section/id-team-matchplan")
tree = html.fromstring(page.content)
table = tree.xpath('//*[@id="id-team-matchplan-table"]/table/tbody')
date_list = []
for row in table:
    table_trs = row.xpath("./tr")
    for table_tr in table_trs:
        if "row-competition" in str(table_tr.get("class")):
            for table_td in table_tr.xpath("./td"):
                if "date" in str(table_td.get("class")):
                    date_strings = [x.strip() for x in table_td.xpath('.//text()')]
                    day = date_strings[0].split(" ")[0]
                    date = date_strings[0].split(" ")[1]
                    time = date_strings[1]
                    date_list.append(day + " " + date + " " + time)


for date in date_list:
    print(date)