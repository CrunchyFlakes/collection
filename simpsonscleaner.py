#!/usr/bin/env python3
# filter out short clips of the dvds to only get whole episodes

import subprocess
import os

deletion_threshold_in_minutes = 20

def getLength(filename):

    def getDurationString(ffprobe_output):
        for line in ffprobe_output:
            if "Duration" in str(line):
                line = str(line).split(" ")
                index_counter = 0
                for lineSnippet in line:
                    if lineSnippet == "Duration:":
                        return line[index_counter + 1]
                    index_counter += 1

    def convertDurationStringToInt(duration_string):
        duration_string = duration_string.replace(',', '')
        duration_strings = duration_string.split(":")

        duration_in_minutes = ( 60 * int(duration_strings[0]) ) + int(duration_strings[1]) + round( float(duration_strings[2]) / 60 )

        return duration_in_minutes



    ffprobe_result = subprocess.Popen(["ffprobe", filename],
                              stdout = subprocess.PIPE, stderr=subprocess.STDOUT)

    return convertDurationStringToInt(getDurationString(ffprobe_result.stdout.readlines()))

for file in os.listdir(os.getcwd()):
    if ".mkv" in file:
        file_length = getLength(file)
        if file_length < deletion_threshold_in_minutes or file_length > 30:
            os.remove(file)
            print(file + "with length: " + str(file_length) + "m" + " was removed!")
        else:
            print(file + "with length: " + str(file_length) + "m" + " was retained.")