from imdbpie import Imdb
import os

imdb = Imdb()

target_director= "/media/bigdisk/converted"
clone_director= None
leave_out = ["simpsons", "tv_shows", "game_of_thrones"]


def renamer(target_directory):

    def rename(object_path, new_name_path):
        os.rename(object_path, new_name_path)
        if clone_director is not None:
            os.rename(object_path.replace(target_director, clone_director), new_name_path.replace(target_director, clone_director))

    def get_imdb_infos(object):
        return imdb.search_for_title(object)

    def form_path_to_object(working_directory, *args):
        path = working_directory
        for arg in args:
            path = path + "/" + arg
        return path

    def get_directories(directory):
        directories = []
        for object in os.listdir(directory):
            if os.path.isdir(form_path_to_object(directory, object)):
                directories.append(object)
        return directories

    def get_files(directory_path):
        files = []
        for object in os.listdir(directory_path):
            if os.path.isfile(form_path_to_object(directory_path, object)):
                files.append(object)
        return files

    def check_if_in_leave_out(object):
        for to_be_skipped in leave_out:
            if to_be_skipped in object:
                return True
        return None

    for directory in get_directories(target_directory):
        if not check_if_in_leave_out(directory) and "(" not in directory:
            current_directory = form_path_to_object(target_directory, directory)
            renamer(current_directory)
            imdb_infos = get_imdb_infos(directory.replace("_", " "))
            if len(imdb_infos) > 0:
                print("Choose title for (10 to not rename) " + directory)
                if len(imdb_infos) > 2:
                    title_range = 3
                else:
                    title_range = len(imdb_infos)
                for x in range(0, title_range):
                    print(str(x) + ": " + imdb_infos[x]["title"])
                inputo = input()
                if inputo == "10":
                    continue
                chosen_one = imdb_infos[int(inputo)]
                imdb_id = chosen_one["imdb_id"]
                year = chosen_one["year"]
                title = chosen_one["title"]
                title = title + " (" + year + ")"
            else:
                title = "not found"
                continue

            # rename file inside directory
            print("Choose file to be renamed:")
            i = 0
            files = get_files(current_directory)
            for file in files:
                print(str(i) + ": " + file)
                i += 1
            if i == 1:
                file_to_be_renamed = files[0]
            else:
                file_to_be_renamed = files[int(input())]
            target_file_name = title + "." + file_to_be_renamed.split(".")[-1]
            print(file_to_be_renamed + " renamed to:  " + target_file_name)
            rename(form_path_to_object(current_directory, file_to_be_renamed), form_path_to_object(current_directory, target_file_name))
            print(directory + " renamed to:  " + title.lower() + "\n")
            rename(current_directory, form_path_to_object(target_directory, title.lower().replace(" ", "_")))


renamer(target_director)