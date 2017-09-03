#!/usr/bin/env python3
# convert multiple files through handbrake and keep directory structure

import os

output_directory = "/this/is/a/test/"

script_working_dir = "/media/bigdisk/movies/"

leave_out_list = []

# order matters (last converted first)
preference_list = ["futurama", "rick"]


def get_output_file_path(input_file_path):
    output_file = output_directory + input_file_path.replace(script_working_dir, "")
    output_file = output_file.split(".")
    output_file[-1] = "mkv"
    output_file = ".".join(output_file)
    return output_file


def delete_last_converted_file():
    os.remove(get_output_file_path(already_converted_list[-1][:-1]))


output_script = open("Handbraketest.sh", "w")
already_converted_txt = open("handbrakelogtest.txt", "r+")
already_converted_list = already_converted_txt.readlines()
already_converted_txt.close()
print("deleting: " + get_output_file_path(already_converted_list[-1]))
already_converted_txt = open("handbrakelogtest.txt", "w")
#delete_last_converted_file()
already_converted_list = already_converted_list[:-1]
already_converted_txt.writelines(already_converted_list)

already_converted_txt.close()


def mainfunction(current_working_dir):

    def is_in_leave_out(input_file_path):
        for leave_out_item in leave_out_list:
            if leave_out_item in input_file_path:
                return True
        return None

    def is_already_converted(input_file):
        for converted_file in already_converted_list:
            if converted_file == input_file + "\n":
                return True
        return None

    def write_commands_into_output_script(input_object_path):
        output_file_path = get_output_file_path(input_object_path)
        output_script.write("echo \"" + input_object_path + "\"" + " >> handbrakelog.txt\n")
        output_script.write(
            "HandBrakeCLI --preset-import-file /home/mtoepperwien/Documents/customOne.json --preset customOne -i \"" + input_object_path + "\" -o \"" + output_file_path + "\" --audio-lang-list deu,eng --all-audio -f av_mkv\n")

    def sort_to_be_converted_through_preference():
        for preference in preference_list:
            for x in range(1, (len(to_be_converted) - 1)):
                if preference == "rick":
                    print("rick")
                if preference in to_be_converted[x]:
                    preference_file = to_be_converted[x]
                    preference_position = x
                    index = x - 1
                    while True:
                        if preference in to_be_converted[index] or index == -1:
                            break
                        temporary_switch_file = to_be_converted[index]
                        to_be_converted[index] = preference_file
                        to_be_converted[index + 1] = temporary_switch_file
                        index += -1


    directory_contents = os.listdir(current_working_dir)
    current_output_directory = output_directory + current_working_dir.replace(script_working_dir, "")

    to_be_converted = []

    for content in directory_contents:
        input_object_path = current_working_dir + content
        output_file_path = get_output_file_path(input_object_path)
        if os.path.isfile(input_object_path) and not is_already_converted(input_object_path) and not is_in_leave_out(input_object_path) and not os.path.exists(output_file_path):
            #if not os.path.exists(current_output_directory):
                #os.makedirs(current_output_directory)
            to_be_converted.append(input_object_path)
        elif os.path.isdir(input_object_path):
            mainfunction(input_object_path + "/")

    sort_to_be_converted_through_preference()
    for file in to_be_converted:
        print(file)

mainfunction(script_working_dir)
output_script.write("echo Finished!\n")
output_script.close()
print("finished")