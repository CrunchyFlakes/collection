import os
import sys

input_arguments = sys.argv
del input_arguments[0]

target_directories = []
replace_map = {}
input_arguments.append("-replace")
input_arguments.append("simpsons:the_simpsons")

i = 0
current_option = None
for argument in input_arguments:
    if argument[0] == "-":
        current_option = argument
        continue
    if current_option is None:
        target_directories.append(argument)
    elif current_option == "-replace":
        argument_splitted = argument.split(":")
        replace_map[argument_splitted[0]] = argument_splitted[1]
    i += 1


def renamer(target_directory):
    os.chdir(target_directory)

    def get_present_files():
        present_files = []
        for object in os.listdir(target_directory):
            if os.path.isfile(form_path(object)):
                present_files.append(object)
        return present_files

    def replace_with(file):
        for replace_key in replace_map:
            if replace_key in file and not replace_map[replace_key] in file:
                new_filename = file.replace(replace_key, replace_map[replace_key])
                os.rename(form_path(file), form_path(new_filename))
                return new_filename
                break

    def replace_space_with_underscore(file):
        new_filename = str(file).replace(" ", "_").lower()
        os.rename(form_path(file), form_path(new_filename))
        return new_filename

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
        file = replace_space_with_underscore(file)
        file = replace_with(file)


    for directory in get_present_directories():
        renamer(form_path(directory))
        replace_space_with_underscore(directory)


for target_directory in target_directories:
    if target_directory[-1] == "/":
        target_directory = target_directory[:-1]
    renamer(target_directory)
