#!/usr/bin/env python3
# rename folders and files of copied simpsons dvds (only seasons and their disks)

import os
import sys

# get list of input parameters
target_directories = sys.argv
del target_directories[0]
target_directories = []
if len(target_directories) <= 0:
    sys.exit("Please input target directories as input parameters!")


def renamer(target_directory_path):

    def get_present_simpsons_directories():
        present_simpsons_directories = []
        for object in os.listdir(target_directory_path):
            if os.path.isdir(form_path(object)) and "simpsons" in object.lower():
                present_simpsons_directories.append(object)
        return present_simpsons_directories

    def get_present_simpsons_files():
        present_simpsons_files = []
        for object in os.listdir(target_directory_path):
            if os.path.isfile(form_path(object)) and "simpsons" in object.lower():
                present_simpsons_files.append(object)
            return present_simpsons_files

    def rename_folder(folder, season, disk=None):
        new_directory_name = "simpsons_s" + str(season)
        if disk is not None:
            new_directory_name += "_d" + disk
        os.rename(form_path(folder), form_path(new_directory_name))

    def rename_file(file, season, episode, disk=None):
        new_file_name = "simpsons_s" + season
        if disk is not None:
            new_file_name += "_d" + disk
        new_file_name += "_e" + str(episode) + "." + file.split(".")[-1]
        os.rename(form_path(file), form_path(new_file_name))

    def get_ordered_simpsons_files(files):
        episodes_numbered = {}
        for episode in files:
            if "title" in episode:
                episode_split = episode.split(".")
                # get number
                number = int(episode_split[0].replace("title", ""))
                episodes_numbered[number] = episode
            elif "_e" in episode:
                episode_split = episode.split(".")[0].split("_")
                number = int(episode_split[-1].replace("e", ""))
                episodes_numbered[number] = episode
            else:
                try:
                    for substring in episode.split("."):
                        if "s" in substring.lower() and "e" in substring.lower() and len(substring) == 6:
                            number = int(substring[-2:])
                            episodes_numbered[number] = episode
                except:
                    print(episode + " could not get information")
        return sorted(episodes_numbered.items())

    def get_season(folder_path):
        folder_substrings = folder_path.lower().split("/")[-1].split("_")
        index_counter = 0
        for substring in folder_substrings:
            if substring == "season":
                return folder_substrings[index_counter + 1]
            elif "s" in substring and (len(substring) == 2 or len(substring) == 3):
                return substring.replace("s", "")
            index_counter += 1

    def get_disk(folder_path):
        folder_substrings = folder_path.lower().split("/")[-1].split("_")
        index_counter = 0
        for substring in folder_substrings:
            if "d" in substring and len(substring) == 2:
                return substring[1]
            elif substring == "disc":
                return folder_substrings[index_counter + 1]
            index_counter += 1

    def form_path(object):
        return target_directory_path + "/" + object

    episode_number = 1
    for present_pair in get_ordered_simpsons_files(get_present_simpsons_files()):
        rename_file(present_pair[1], get_season(target_directory_path), episode_number)
        episode_number += 1

    for present_directory in get_present_simpsons_directories():
        rename_folder(present_directory, get_season(form_path(present_directory)), get_disk(form_path(present_directory)))

    for present_directory in get_present_simpsons_directories():
        new_target_directory = form_path(present_directory)
        renamer(new_target_directory)


for working_directory in target_directories:
    print("now working in directory: " + working_directory)
    renamer(working_directory)