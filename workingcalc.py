#!/usr/bin/env python3
#

import os
import json
import datetime
import sys

os.chdir(os.path.dirname(os.path.realpath(sys.argv[0])))

hourlywage = 8.84
workingdays = 35

if os.path.isfile("workedhours.txt"):
    hourtable = json.load(open("workedhours.txt", "r"))
else:
    hourtable = dict()

today = datetime.datetime.now().strftime("%Y-%m-%d")
if today not in hourtable or input("Wanna overwrite today(y/n)?") == "y":
    todayhours = input("Input working hours for today: ")
    if todayhours != "0":
        hourtable[today] = todayhours


i = 0
wage = 0.0
for hours in hourtable:
    i += 1
    wage += (hourlywage * float(hourtable[hours]))

average_working_hours = (wage / hourlywage) / i
standard_deviation_end_time = 0.0
for hours in hourtable:
    standard_deviation_end_time += (float(hourtable[hours]) - average_working_hours) ** 2
standard_deviation_end_time = (standard_deviation_end_time / i) ** 0.5
deviation_split = str(standard_deviation_end_time).split('.')
standard_deviation_end_time = deviation_split[0] + 'h ' + str(int(float(deviation_split[1][:2]) * 0.6)) + 'm'
probable_end_wage = (wage / i) * workingdays

average_end_time = str(average_working_hours + 8.75)[:5].split(".")
average_end_time = average_end_time[0] + ":" + str(int(float(average_end_time[1]) * 0.6))


probable_end_wage = str(probable_end_wage).split(".")
probable_end_wage = probable_end_wage[0] + "." + probable_end_wage[1][:2]
print("Days: " + str(i))
print("Average working hours: " + str(average_working_hours))
print("Average end time: " + average_end_time)
print("Standard deviation: " + standard_deviation_end_time)
print("Current wage: " + str(wage) + "€")
print("Probable end wage: " + str(probable_end_wage) + "€")

json.dump(hourtable, open("workedhours.txt", "w"))
