#!/usr/bin/env python3
# calculate when to go to bed

import sys

try:
    wake_up_time = float(sys.argv[1])
except:
    wake_up_time = 6.25

go_to_bed_time = wake_up_time

def convert_dec_time_to_time_string(dec_time):
    dec_time = str(dec_time).split(".")
    hours = dec_time[0]
    if len(dec_time[0]) == 1:
        hours = "0" + hours
    minutes = str(int(float("0." + dec_time[1]) * 60))
    if len(minutes) == 1:
        minutes += "0"
    time_string = hours + ":" + minutes
    return time_string

for x in range(0,6):
    go_to_bed_time = go_to_bed_time - 1.5
    if go_to_bed_time < 0:
        go_to_bed_time += 24
    print(convert_dec_time_to_time_string(go_to_bed_time))