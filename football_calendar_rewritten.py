#!/usr/bin/env python3
# football thingy rewritten

from lxml import html
import requests
from datetime import datetime

page_link = "http://www.fussball.de/mannschaft/sv-teutonia-gross-lafferde-sv-teutonia-gross-lafferde-niedersachsen/-/saison/1718/team-id/012NAV1I3G000000VV0AG811VUPV8FHO#!/section/id-team-matchplan"
page = requests.get(page_link)
table = html.fromstring(page.content).xpath('//*[@id="id-team-matchplan-table"]/table/tbody')


def get_dates():
    date_times = []
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
                        date = datetime(int(date[2]) + 2000, int(date[1]), int(date[0]), int(time[0]), int(time[1]))
                        date = date.strftime("%A")[:3] + " " + "{:0>2}.{:0>2}.{:0>4} {:0>2}:{:0>2}".format(date.day, date.month, date.year, date.hour, date.minute)
                        date_times.append(date)
    return date_times


def get_enemies():
    enemies = []
    for row in table:
        table_trs = row.xpath("./tr")
        for table_tr in table_trs:
            for table_td in table_tr.xpath("./td"):
                if "club" in str(table_td.get("class")):
                    table_a = table_td.xpath("./a")[0]
                    table_div = table_a.xpath("./div")[1]
                    club_name = [x.strip() for x in table_div.xpath('.//text()')][0]
                    if "Groß Lafferde" not in club_name:
                        enemies.append(club_name)
    return enemies


print(datetime.now().strftime("%A")[:3] + " " +  "{:0>2}.{:0>2}.{:0>4}".format(datetime.now().day, datetime.now().month, datetime.now().year) + " (today)")
dates = get_dates()
enemies = get_enemies()

i = 0
while i < len(enemies):
    print(dates[i] + "  " + enemies[i])
    i += 1

print("\n\n")
print("Website: " + page_link)

