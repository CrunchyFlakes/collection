#!/usr/bin/env python3
# rename folders and files of copied simpsons dvds (only seasons and their disks)

import os
import sys

# get list of input parameters
target_directories = sys.argv
del target_directories[0]
target_directories = [os.getcwd()]
if len(target_directories) <= 0:
    sys.exit("Please input target directories as input parameters!")


def renamer(target_directory_path):

    def return_present_simpsons_directories():
        present_simpsons_directories = []
        for object in os.listdir(target_directory_path):
            if os.path.isdir(object) and "simpsons" in object.lower():
                present_simpsons_directories.append(object)
        return present_simpsons_directories

    def rename_folder(folder, season, disk=None):
        new_directory_name = "simpsons_s" + season
        if disk is not None:
            new_directory_name += "_d" + disk
        os.rename(form_directory_path(folder), form_directory_path(new_directory_name))

    def get_season(folder_path):
        folder_substrings = folder_path.lower().split("/")[-1].split("_")
        index_counter = 0
        for substring in folder_substrings:
            if substring == "season":
                return folder_substrings[index_counter + 1]
            elif "s" in substring and (len(substring) == 2 or len(substring) == 3):
                return substring.replace("s", "")
            index_counter += 1

    def form_directory_path(directory):
        return target_directory_path + "/" + directory

    for present_directory in return_present_simpsons_directories():
        renamer(form_directory_path(present_directory))

for working_directory in target_directories:
    print("now working in directory: " + working_directory)
    renamer(working_directory)