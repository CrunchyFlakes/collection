#!/usr/bin/env python3
# rename movie folder directories and files

import os

simpsons_skip = True
clone_directory_mode = True
working_directory = "/media/bigdisk/converted/"
clone_directories = ["/media/mtoepperwien/oldie/movies/", "/media/bigdisk/movies/"]


def renamer(current_working_directory):
        os.chdir(current_working_directory)
        directory_listed = os.listdir(current_working_directory)

        for object in directory_listed:
            if not "simpsons" in object.lower() or not simpsons_skip:
                object_path = (current_working_directory + object).replace(working_directory, "")
                print("rename " + object_path + " ? (enter for no change)")
                new_objectname = input()
                if not new_objectname == "":
                    if os.path.isfile(object):
                        new_objectname = new_objectname + "." + object.split(".")[1]
                    os.rename(current_working_directory + object, current_working_directory + new_objectname)
                    if clone_directory_mode:
                        for clone_directory in clone_directories:
                            os.rename((current_working_directory + object).replace(working_directory, clone_directory), (current_working_directory + new_objectname).replace(working_directory, clone_directory))
                    object = new_objectname
                elif os.path.isdir(current_working_directory + object):
                    os.rename(current_working_directory + object, current_working_directory + object.lower())
                    if clone_directory_mode:
                        for clone_directory in clone_directories:
                            os.rename((current_working_directory + object).replace(working_directory, clone_directory), (current_working_directory + object.lower()).replace(working_directory, clone_directory))
                    object = object.lower()
                if os.path.isdir(current_working_directory + object):
                    renamer(current_working_directory + object + "/")


renamer(working_directory)
