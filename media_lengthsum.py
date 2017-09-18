#!/usr/bin/env python3

import os
import subprocess
import sys

lengthsum = 0

target_directory = "/media/bigdisk/converted"

try:
    target_directory = sys.argv[1]
    if target_directory[-1] == "/":
        target_directory = target_directory[:-1]
except:




def renamer(target_directory_path):

    def get_present_directories():
        present_simpsons_directories = []
        for object in os.listdir(target_directory_path):
            if os.path.isdir(form_path(object)):
                present_simpsons_directories.append(object)
        return present_simpsons_directories

    def get_present_files():
        present_simpsons_files = []
        for object in os.listdir(target_directory_path):
            if os.path.isfile(form_path(object)):
                present_simpsons_files.append(object)
        return present_simpsons_files

    def form_path(object):
        return target_directory_path + "/" + object

    def getLength(file_path):

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
            try:
                duration_string = duration_string.replace(',', '')
                duration_strings = duration_string.split(":")

                duration_in_minutes = ( 60 * int(duration_strings[0]) ) + int(duration_strings[1]) + round( float(duration_strings[2]) / 60 )
            except:
                duration_in_minutes = 0
                print("fail: " + file_path)

            return duration_in_minutes



        ffprobe_result = subprocess.Popen(["ffprobe", file_path],
                                  stdout = subprocess.PIPE, stderr=subprocess.STDOUT)

        return convertDurationStringToInt(getDurationString(ffprobe_result.stdout.readlines()))


    for present_directory in get_present_directories():
        new_target_directory = form_path(present_directory)
        renamer(new_target_directory)

    for present_file in get_present_files():
        global lengthsum
        lengthsum += getLength(form_path(present_file))

renamer(target_directory)
print("Sum: ")
print("     " + str(lengthsum) + "m")
print("     " + str(lengthsum / 60) + "h")
print("     " + str((lengthsum / 60) / 60) + "d")