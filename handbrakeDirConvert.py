#!/usr/bin/env python3
# convert multiple files through handbrake and keep directory structure

import os
import subprocess

output_directory = "/media/bigdisk/converted/"

script_working_dir = "/media/bigdisk/movies/"


def mainfunction(current_working_dir):
    directory_contents = os.listdir(current_working_dir)
    output_structured_directory = output_directory + current_working_dir.replace(script_working_dir, "")
    if not os.path.exists(output_structured_directory):
        os.makedirs(output_structured_directory)

    for content in directory_contents:
        inputfile = current_working_dir + content
        if os.path.isfile(inputfile):
            outputfile = output_directory + inputfile.replace(script_working_dir, "")
            print(outputfile)
            output = subprocess.Popen(
                ["HandBrakeCLI", "--preset-import-gui", "customOne", "-i", inputfile, "-o", outputfile,
                 " --audio-lang-list deu,eng", "--all-audio"],
                stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            line = output.stdout.readline()
            output.wait()
        elif os.path.isdir(inputfile):
            mainfunction(inputfile + "/")


mainfunction(script_working_dir)
print("finished")
