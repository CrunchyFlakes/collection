#!/usr/bin/env python3
# rename folders and files of copied simpsons dvds

import os

working_directory = None

def renamer(current_working_directory):
    directory_listed = os.listdir(current_working_directory)
    no_directory_found = True

    for object in directory_listed:
        # TODO: remove
        object = str(object)
        if os.path.isdir(current_working_directory + "/" + object) and "simpsons" in object.lower():
            no_directory_found = None
            object_lower = object.lower().split("_")
            index_counter = 0
            season = None
            disc = None
            for string in object_lower:
                if string == "season":
                    season = object_lower[index_counter + 1]
                elif "s" in string and (len(string) == 2 or len(string) == 3):
                    season = string.replace("s", "")
                if "d" in string and len(string) == 2:
                    disc = string[1]
                elif string == "disc":
                    disc = object_lower[index_counter + 1]
                index_counter += 1
            new_directory_name = "simpsons_" + "s" + season
            if not disc == None:
                print("season: " + season + " disc: " + disc)
                new_directory_name += "_d" + disc
            # rename subdirectories
            renamer(current_working_directory + "/" + object)
            # rename this directory
            os.rename(current_working_directory + "/" + object, current_working_directory + "/" + new_directory_name)

    if no_directory_found and "simpsons" in current_working_directory.split("/")[-1].lower():
        episode_rename_map = {}
        for episode in directory_listed:
            if "title" in episode:
                episode_split = episode.split(".")
                # get number
                number = int(episode_split[0].replace("title", ""))
                episode_rename_map[number] = episode
        sorted_keys = sorted(episode_rename_map.items())
        i = 0
        while i < len(sorted_keys):
            old_episode_name = current_working_directory + "/" + sorted_keys[i][1]
            new_episode_name = current_working_directory + "/" + current_working_directory.split("/")[-1].lower() + "_e" + str(i + 1) + ".mkv"
            os.rename(old_episode_name, new_episode_name)
            i += 1


renamer("/media/bigdisk/converted/")