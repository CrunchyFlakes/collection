#!/usr/bin/env python3
# scrape football match dates and add them to calendar

from lxml import html
import requests
from datetime import datetime


page = requests.get("http://www.fussball.de/mannschaft/sv-teutonia-gross-lafferde-sv-teutonia-gross-lafferde-niedersachsen/-/saison/1718/team-id/012NAV1I3G000000VV0AG811VUPV8FHO#!/section/id-team-matchplan")
tree = html.fromstring(page.content)
table = tree.xpath('//*[@id="id-team-matchplan-table"]/table/tbody')
datetimes = []
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
                    time = time.split(":")
                    date = date.split(".")
                    datetimes.append(datetime(int(date[2]) + 2000, int(date[1]), int(date[0]), int(time[0]), int(time[1])))


print("{:0>2}.{:0>2}".format(datetime.now().day, datetime.now().month))
for date in datetimes:
    print(date.strftime("%A")[:3] + " " + "{:0>2}.{:0>2}.{:0>4} {:0>2}:{:0>2}".format(date.day, date.month, date.year, date.hour, date.minute))
