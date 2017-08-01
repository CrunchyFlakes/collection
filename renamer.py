#!/usr/bin/env python3
# rename movie folder directories and files

import os

simpsons_skip = None
clone_directory_mode = True
working_directory = "/media/bigdisk/converted/"
clone_directory = "/media/bigdisk/movies/"

def renamer(current_working_directory):
        os.chdir(current_working_directory)
        directory_listed = os.listdir(current_working_directory)

        for object in directory_listed:
            if not "simpsons" in object.lower() or not simpsons_skip:
                object_path = (current_working_directory + object).replace(working_directory, "")
                print("rename " + object_path + " ? (enter for no change)")
                new_objectname = input()
                if not new_objectname == "":
                    os.rename(object, new_objectname)
                    if clone_directory_mode:
                        os.rename((current_working_directory + object).replace(working_directory, clone_directory))
                if object == "testing":
                    nothing = None
                if os.path.isdir(current_working_directory + object):
                    renamer(current_working_directory + object + "/")


renamer(working_directory)