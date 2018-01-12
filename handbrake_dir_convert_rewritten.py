#!/usr/bin/env python3
# convert multiple files through handbrake and keep directory structure

import os
import sys
import subprocess



output_directory = "/media/bigdisk/converted/"

script_working_dir = "/media/bigdisk/movies/"

# put in series to leave out
leave_out_list = []

# order matters (last converted first)
preference_list = ["rick"]

to_be_converted = []

# only convert one (per input arguments)
only_one = False

input_arguments = sys.argv
del input_arguments[0]

i = 0
for argument in input_arguments:
    if argument == "-pref":
        i += 1
        preference_list.append(input_arguments[i])
        while True:
            try:
                if not input_arguments[i + 1][0] == "-":
                    i += 1
                    preference_list.append(input_arguments[i])
                else:
                    break
            except:
                break
    elif argument == "-out":
        i += 1
        leave_out_list.append(input_arguments[i])
        while True:
            try:
                if not input_arguments[i + 1][0] == "-":
                    i += 1
                    leave_out_list.append(input_arguments[i])
                else:
                    break
            except:
                break
    elif argument == "-one":
        only_one = True
    i += 1


def sort_to_be_converted_through_preference():
    def swap(i_x, i_y):
        to_be_converted[i_y], to_be_converted[i_x] = to_be_converted[i_x], to_be_converted[i_y]

    for preference in preference_list:
        for x in range(1, (len(to_be_converted))):
            if preference in to_be_converted[x]:
                to_be_switched_with = x - 1
                while True:
                    if preference in to_be_converted[to_be_switched_with] or to_be_switched_with == -1:
                        break
                    swap(to_be_switched_with, to_be_switched_with + 1)
                    to_be_switched_with += -1


def get_output_file_path(input_file_path):
    output_file = output_directory + input_file_path.replace(script_working_dir, "")
    output_file = output_file.split(".")
    output_file[-1] = "mkv"
    output_file = ".".join(output_file)
    return output_file


def delete_last_converted_file():
    os.remove(get_output_file_path(already_converted_list[-1][:-1]))


output_script = open("Handbrake.sh", "w")
already_converted_txt = open("handbrakelog.txt", "r")
already_converted_list = already_converted_txt.readlines()
already_converted_txt.close()


if already_converted_list[-1][-2] != "1":
    already_converted_txt = open("handbrakelog.txt", "w")
    delete_last_converted_file()
    print("deleted: " + get_output_file_path(already_converted_list[-1][:-1]))
    already_converted_list = already_converted_list[:-1]
    already_converted_txt.writelines(already_converted_list)
    already_converted_txt.close()


def mainfunction(current_working_dir):
    global to_be_converted
    def is_in_leave_out(input_file_path):
        for leave_out_item in leave_out_list:
            if leave_out_item in input_file_path:
                return True
        return None

    def is_already_converted(input_file):
        for converted_file in already_converted_list:
            if input_file in converted_file:
                return True
        return None

    def write_commands_into_output_script(input_object_path):
        output_file_path = get_output_file_path(input_object_path)
        output_script.write("echo \"" + input_object_path + "\"" + " >> handbrakelog.txt\n")
        output_script.write(
            "HandBrakeCLI --preset-import-file /home/mtoepperwien/Documents/customOne.json --preset customOne -i \"" + input_object_path + "\" -o \"" + output_file_path + "\" --audio-lang-list deu,eng --all-audio -f av_mkv\n")



    directory_contents = os.listdir(current_working_dir)
    current_output_directory = output_directory + current_working_dir.replace(script_working_dir, "")

    for content in directory_contents:
        input_object_path = current_working_dir + content
        output_file_path = get_output_file_path(input_object_path)
        if os.path.isfile(input_object_path) and not is_already_converted(input_object_path) and not is_in_leave_out(
                input_object_path) and not os.path.exists(output_file_path):
            if not os.path.exists(current_output_directory):
                os.makedirs(current_output_directory)
            to_be_converted.append(input_object_path)
        elif os.path.isdir(input_object_path):
            mainfunction(input_object_path + "/")


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



mainfunction(script_working_dir)
to_be_converted.sort(key=str.lower)
sort_to_be_converted_through_preference()

total_length = 0

for input_file in to_be_converted:
    total_length += getLength(input_file)

    output_script.write("echo -n \"" + input_file + "\"" + " >> handbrakelog.txt\n")
    output_script.write(
        "HandBrakeCLI --preset-import-file /home/mtoepperwien/Documents/customOne.json --preset customOne -i \"" + input_file + "\" -o \"" + get_output_file_path(input_file) + "\" --audio-lang-list deu,eng --all-audio -f av_mkv\n")
    output_script.write("echo \" 1\" >> handbrakelog.txt\n")
    if only_one is True:
        break
output_script.write("echo Finished!\n")
output_script.close()
print("total length: " + str(total_length) + "m")
print("finished")
