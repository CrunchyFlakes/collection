#!/usr/bin/env python3

import os


working_dir = "/media/bigdisk/movies/simpson4/"
os.chdir(working_dir)

def form_path(folder_path, file):
    if folder_path[-1] == "/":
        folder_path = folder_path[:-1]
    return folder_path + "/" + file

def get_season(name):
    name_split = name.lower().split("_")
    for substring in name_split:
        if "season" in substring:
            return substring.replace("season", "")
        elif "s" in substring and len(substring) == 2:
            return substring.replace("s", "")

def get_disk(name):
    name_split = name.lower().split("_")
    for substring in name_split:
        if "d" in substring and len(substring) == 2:
            return substring[1]


for disk_folder in os.listdir(working_dir):
    disk_folder_path = form_path(working_dir, disk_folder)
    if "simpsons" in disk_folder.lower() and "d" in disk_folder.lower() and os.path.isdir(disk_folder_path):
        for file in os.listdir(disk_folder_path):
            file_path = form_path(disk_folder_path, file)

            episode_number_and_ending = file.replace("title", "")

            new_filename = "the_simpsons" + "_s" + get_season(disk_folder) + "e_" + get_disk(disk_folder) + episode_number_and_ending

            os.rename(file_path, form_path(working_dir, new_filename))


file_list = []

for file in os.listdir(working_dir):
    file_path = form_path(working_dir, file)
    if os.path.isfile(file_path):
        file_list.append(file)

file_list = sorted(file_list)

episode_number = 1

for entry in file_list:
    entry_path = form_path(working_dir, entry)
    season_number = "04"
    episode_number_used = episode_number
    if episode_number < 10:
        episode_number_used = "0" + str(episode_number)
    new_filename = "simpsons_s" + season_number + "_e" + str(episode_number_used) + ".mkv"
    new_filename_path = form_path(working_dir, new_filename)
    os.rename(entry_path, new_filename_path)
    episode_number += 1