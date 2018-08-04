#!/usr/bin/env python3
# enter which money I get back from my parents

import json
import datetime

date = datetime.datetime.now().strftime("%Y-%m-%d")


def loadEntriesFile():
    entries_file = open("money_parents.json", "r")
    global entries
    entries = json.load(entries_file)

try:
    loadEntriesFile()
except:
    print("No database file found. Creating new one.")
    entries = []



def addEntry(amount, date, comment):
    entry = []
    entry.append(amount)
    entry.append(date)
    entry.append(comment)
    entries.append(entry)

def deleteEntry(index):
    entries.pop(index)

def displayEntries():
    entry_index = 0
    for entry in entries:
        print(entry[1] + ": " + str(entry[0]) + "€  " + entry[2] + "   [" + str(entry_index) + "]")
        entry_index += 1

def returnSum():
    sum = 0
    for entry in entries:
        sum += entry[0]
    return sum



print("Create new entry (0 to show entries, \"del\" to delete entry):")
amount = input("Amount of money in €: ")
if amount == "0":
    displayEntries()
    print("Sum: " + str(returnSum()))
elif amount == "del":
    displayEntries()
    delete_index = input("delete entry number (index) or \"all\": ")
    if delete_index == "all":
        if input("Sure? (y/n): ").lower() == "y":
            entries = []
    else:
        deleteEntry(int(delete_index))
else:
    amount = int(amount)
    comment = input("Comment/Note: ")
    addEntry(amount, date, comment)



entries_file = open("money_parents.json", "w")

json.dump(entries, entries_file)

entries_file.close()