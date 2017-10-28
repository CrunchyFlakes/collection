import os
import sys

target_directories = sys.argv
del target_directories[0]




def renamer(target_directory):
    os.chdir(target_directory)

    def get_present_files():
        present_files = []
        for object in os.listdir(target_directory):
            if os.path.isfile(form_path(object)):
                present_files.append(object)
        return present_files

    def replace_space_with_underscore(file):
        new_filename = str(file).replace(" ", "_").lower()
        os.rename(form_path(file), form_path(new_filename))

    def change_extension_to_mkv(file):
        new_filename = str(file).replace(".avi", ".mkv").replace(" ", "_").lower()
        os.rename(form_path(file), form_path(new_filename))

    def get_present_directories():
        present_directories = []
        for object in os.listdir(target_directory):
            if os.path.isdir(form_path(object)):
                present_directories.append(object)
        return present_directories

    def form_path(object):
        return target_directory + "/" + object

    for file in get_present_files():
        replace_space_with_underscore(file)


    for directory in get_present_directories():
        renamer(form_path(directory))
        replace_space_with_underscore(directory)


for target_directory in target_directories:
    if target_directory[-1] == "/":
        target_directory = target_directory[:-1]
    renamer(target_directory)
