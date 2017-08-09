


import os

working_directory = "/media/bigdisk/converted"

def renamer(target_directory):
    os.chdir(target_directory)

    def get_present_files():
        present_files = []
        for object in os.listdir(target_directory):
            if os.path.isfile(form_path(object)):
                present_files.append(object)
        return present_files

    def change_extension_to_mkv(file):
        new_filename = str(file).replace(".avi", ".mkv")
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
        file_ending = file.split(".")[-1]
        if file_ending == "avi":
            change_extension_to_mkv(file)

    for directory in get_present_directories():
        renamer(form_path(directory))

renamer(working_directory)