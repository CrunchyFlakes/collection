#!/usr/bin/env python3
# convert multiple files through handbrake and keep directory structure

import os
import subprocess

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
        inputfile = current_working_dir + content
        if os.path.isfile(inputfile):
            already_converted = None
            for converted_file in already_converted_list:
                if converted_file == inputfile + "\n":
                    already_converted = True
            if not already_converted:
                outputfile = output_directory + inputfile.replace(script_working_dir, "")
                output_script.write("HandBrakeCLI --preset-import-file /home/mtoepperwien/Documents/customOne.json --preset customOne -i \"" + inputfile + "\" -o \"" + outputfile + "\" --audio-lang-list deu,eng --all-audio\n")
                output_script.write("echo \"" + inputfile + "\"" + " >> handbrakelog.txt\n")
            #output = subprocess.Popen(
            #    ["HandBrakeCLI", "--preset-import-gui", "customOne", "-i", inputfile, "-o", outputfile,
            #     " --audio-lang-list deu,eng", " --all-audio"],
            #    stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            #output.wait()
        elif os.path.isdir(inputfile):
            mainfunction(inputfile + "/")


mainfunction(script_working_dir)
output_script.write("echo Finished!\n")
output_script.close()
print("finished")
