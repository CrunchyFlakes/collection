#!/usr/bin/env python3
# convert multiple files through handbrake and keep directory structure

import os

output_directory = "/media/bigdisk/converted/"

script_working_dir = "/media/bigdisk/movies/"


def get_output_file(input_file_path):
    output_file = output_directory + input_file_path.replace(script_working_dir, "")
    output_file = output_file.split(".")
    output_file[-1] = "mkv"
    output_file = ".".join(output_file)
    return output_file

output_script = open("Handbrake.sh", "w")
already_converted_txt = open("handbrakelog.txt", "r+")
already_converted_list = already_converted_txt.readlines()
already_converted_txt.close()
delete_decision = input("Want to delete last converted episode? (yes/no): ")
if delete_decision == "yes":
    print("deleting: " + get_output_file(already_converted_list[-1]))
    already_converted_txt = open("handbrakelog.txt", "w")
    already_converted_txt.writelines(already_converted_list[:-1])
    already_converted_txt.close()

    os.remove(get_output_file(already_converted_list[-1][:-1]))
    already_converted_list = already_converted_list[:-1]


def mainfunction(current_working_dir):
    directory_contents = os.listdir(current_working_dir)
    output_structured_directory = output_directory + current_working_dir.replace(script_working_dir, "")

    for content in directory_contents:
        input_file = current_working_dir + content
        if os.path.isfile(input_file):
            already_converted = None
            for converted_file in already_converted_list:
                if converted_file == input_file + "\n":
                    already_converted = True
            if not already_converted and "thrones" not in content: #and ("futurama_s01" in content or "futurama_s02" in content or "futurama_s03" in content or "futurama_s04" in content or "futurama_s05" in content): #and "simpsons" not in content:
                if not os.path.exists(output_structured_directory):
                    os.makedirs(output_structured_directory)
                output_file = get_output_file(input_file)
                output_script.write("echo \"" + input_file + "\"" + " >> handbrakelog.txt\n")
                if not os.path.exists(output_file):
                    output_script.write("HandBrakeCLI --preset-import-file /home/mtoepperwien/Documents/customOne.json --preset customOne -i \"" + input_file + "\" -o \"" + output_file + "\" --audio-lang-list deu,eng --all-audio -f av_mkv\n")
        elif os.path.isdir(input_file):
            mainfunction(input_file + "/")


mainfunction(script_working_dir)
output_script.write("echo Finished!\n")
output_script.close()
print("finished")
