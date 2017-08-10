#!/usr/bin/env python3
# convert multiple files through handbrake and keep directory structure

import os

output_directory = "/media/bigdisk/converted/"

script_working_dir = "/media/bigdisk/movies/"

output_script = open("Handbrake.sh", "w")

already_converted_txt = open("handbrakelog.txt", "r+")
already_converted_list = already_converted_txt.readlines()
already_converted_txt.close()


def mainfunction(current_working_dir):
    directory_contents = os.listdir(current_working_dir)
    output_structured_directory = output_directory + current_working_dir.replace(script_working_dir, "")
    if not os.path.exists(output_structured_directory):
        os.makedirs(output_structured_directory)

    for content in directory_contents:
        input_file = current_working_dir + content
        if os.path.isfile(input_file):
            already_converted = None
            for converted_file in already_converted_list:
                if converted_file == input_file + "\n":
                    already_converted = True
            already_converted = None  # disable log checking!
            if not already_converted:
                output_file = output_directory + input_file.replace(script_working_dir, "")
                if not os.path.exists(output_file):
                    output_script.write("HandBrakeCLI --preset-import-file /home/mtoepperwien/Documents/customOne.json --preset customOne -i \"" + input_file + "\" -o \"" + output_file + "\" --audio-lang-list deu,eng --all-audio -f av_mkv\n")
                    output_script.write("echo \"" + input_file + "\"" + " >> handbrakelog.txt\n")
        elif os.path.isdir(input_file):
            mainfunction(input_file + "/")


mainfunction(script_working_dir)
output_script.write("echo Finished!\n")
output_script.close()
print("finished")
