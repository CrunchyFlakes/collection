#/usr/bin/env python3
# rename movie files and their folders accordingly to the imdb website infos

# NOT READY YET !!
from imdbpie import Imdb
import os

imdb = Imdb()

working_directory = "/media/bigdisk/movies"
if working_directory[-1] == "/":
    working_directory = working_directory[:-1]
leave_out = ["tv_shows"]

def renamer(target_directory):

    def rename(object_path, imdb_object):
        new_name = imdb_object["title"] + " (" + imdb_object["year"] + ")"
        parent_directory = object_path.split("/")[:-1]
        parent_directory = "/".join(parent_directory)
        if os.path.isdir(object_path):
            new_name = new_name.replace(" ", "_").lower()
            new_name_path = form_path_to_object(parent_directory, new_name)
        elif os.path.isfile(object_path):
            new_name_path = form_path_to_object(parent_directory, new_name)
        os.rename(object_path, new_name_path)


    def get_directories(directory_path):
        directories = []
        for object in os.listdir(directory_path):
            if os.path.isdir(form_path_to_object(directory_path, object)):
                directories.append(object)
        return directories

    def get_files(directory_path):
        files = []
        for object in os.listdir(directory_path):
            if os.path.isfile(form_path_to_object(directory_path, object)):
                files.append(object)
        return files

    def let_user_choose_imdb_object_and_return(imdb_objects):
        if len(imdb_objects) > 0:
            i = 0
            for imdb_object in imdb_objects:
                print(str(i + 1) + ": \"" + imdb_object["title"] + "\"")
                if i == 2:
                    break
                i += 1
            decision = int(input("\"0\" to not rename: "))  - 1
            if decision == -1:
                return None
        else:
            return None
        return imdb_objects[decision]

    def get_imdb_objects(search_term):
        return imdb.search_for_title(search_term)

    def in_leave_out(object):
        for to_be_skipped in leave_out:
            if to_be_skipped in object:
                return True

    def already_renamed(object):
        return "(" in object

    def form_path_to_object(directory, object):
        return directory + "/" + object


    for directory in get_directories(target_directory):
        if not in_leave_out(directory) and not already_renamed(directory):
            current_directory_path = form_path_to_object(target_directory, directory)

            # rename movies inside this folder
            renamer(current_directory_path)

            imdb_objects = get_imdb_objects(directory.replace("_", " "))
            target_imdb_object = let_user_choose_imdb_object_and_return(imdb_objects)

            # skip to next movie if no match is found
            if target_imdb_object is None:
                print("     \"" + directory + "\" not renamed!\n")
                continue

            rename(current_directory_path, target_imdb_object)
            print("     \"" + directory + "\" renamed.\n")

renamer(working_directory)