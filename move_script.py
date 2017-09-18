#!/usr/bin/env python3

import os

directory_listed = os.listdir(os.getcwd())

for object in directory_listed:
    object_path = os.getcwd() + "/" + object
    season = None
    series = None
    if os.path.isfile(object_path):
        object_splitted = object.split("_")
        for splitter in object_splitted:
            if "s" in splitter and len(splitter) < 4:
                season = int(splitter.replace("s", ""))
                series = os.getcwd().split("/")[-1]
                season_folder_path = os.getcwd() + "/" + str(series) + "_s" + str(season)
                if not os.path.exists(season_folder_path):
                    os.makedirs(season_folder_path)
                new_object_path = season_folder_path + "/" + object_path.split("/")[-1]
                os.rename(object_path, new_object_path)
                print(object_path + " moved to: " + season_folder_path + "/" + object_path.split("/")[-1])
                if " " in object_path:
                    new_object_path_split = new_object_path.split("/")
                    new_object_path_split[-1] = new_object_path_split[-1].replace(" ", "_").lower()
                    new_object_path = "/".join(new_object_path_split)
                    os.rename(object_path, new_object_path)

print("finished")
