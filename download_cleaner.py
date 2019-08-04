#!/usr/bin/env python3
# delete files in download folder if older than specified here (uses first seen to determine how old the file is)

import os
from datetime import datetime

# Settings
# deletion_threshold in days
deletion_threshold = 7
# download folder path (full path)
download_directory = "/home/mtoepperwien/Downloads/"


def remove(path):
    if os.path.isdir(path):
        os.rmdir(path)
    elif os.path.isfile(path):
        os.remove(path)


def write_to_log(is_new, object_path):
    prefix = None
    if is_new:
        prefix = "+"
    else:
        prefix = "-"

    log_entry = prefix + current_time + " " + object_path
    log.insert(0, log_entry + "\n")

    log_file = open(log_path, "w")
    log_file.write("".join(log))
    log_file.close()




def is_folder_empty(folder_path):
    if len(os.listdir(folder_path)) == 0:
        return True
    else:
        return False


def has_been_seen(path):
    if path in file_seen_dict:
        return True
    else:
        return False


def timedifference_over_threshold(object_path):
    first_seen_datetime = datetime.strptime(file_seen_dict[object_path], "%d.%m.%Y")
    today_datetime = datetime.now()
    day_difference = (today_datetime - first_seen_datetime).days

    print(object_path + "   " + str(day_difference))

    if day_difference >= deletion_threshold:
        return True
    else:
        return False


log_path = download_directory + "download_cleaner_log.txt"
log = []
if os.path.exists(log_path):
    log_file = open(log_path, "r")
    log = log_file.readlines()
    log_file.close()

file_seen_dict = {}


# read file_seen dates
for entry in log:
    if entry[0] == "+":
        # get entry data
        date_seen = entry[1:][:10]
        file_path = entry[12:].replace("\n", "")

        # add to file_seen_dict
        file_seen_dict[file_path] = date_seen


# get currently downloaded files
def main(directory):
    for object in os.listdir(directory):
        # skip log file
        if object == "download_cleaner_log.txt":
            continue

        object_path = directory + object
        if os.path.isdir(object_path):
            object_path = object_path + "/"
            main(object_path)

            # skip folder if not empty
            if not is_folder_empty(object_path):
                continue

        if has_been_seen(object_path):
            if timedifference_over_threshold(object_path):
                print("removing: " + object_path)
                remove(object_path)
                write_to_log(False, object_path)
        else:
            write_to_log(True, object_path)











current_time = datetime.now().strftime("%d.%m.%Y")
main(download_directory)
