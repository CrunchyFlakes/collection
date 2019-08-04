#!/usr/bin/env python3
# Delete all programs in a folder older than X days
import os
import time
import sys
from send2trash import send2trash


# Define parameters
DOWNLOAD_DIRECTORY = "/home/mtoepperwien/Downloads/"
DELETION_THRESHOLD = 7


# Log time formatting
timeFormat = '%Y/%m/%d %H:%M:%S'

# Counters
deleteCounter = 0
retainedCounter = 0


def sec_to_days(secs):
    """Convert seconds to days and return days"""
    return int(secs * (1/60) * (1/60) * (1/24))


def get_script_path():
    return os.path.dirname(os.path.realpath(sys.argv[0]))


def remove_old(directory, deletion_threshold):
    """Iterate over files and folders and delete them if older than specified threshold in days.
    Prints also log infos
    """
    current_time = time.time()

    for file in os.listdir(directory):
        #skip own log
        print(file)

        modifiedTime = os.path.getmtime(directory + file)
        # Difference of time now and last modified date
        time_difference = current_time - modifiedTime
        day_difference = sec_to_days(time_difference)

        # Delete file if older than deletion threshold
        if day_difference > DELETION_THRESHOLD:
            global deleteCounter
            global retainedCounter

            print(directory + file)
            print("last modified: " + time.strftime(timeFormat, time.localtime(modifiedTime)))
            print("difference in days: " + str(day_difference))
            if os.path.isfile(directory + file):
                send2trash(directory + file)
                deleteCounter += 1
                print("deleted")
                print()
            elif os.path.isdir(directory + file):
                print("Trying to remove in folder: " + directory + file)
                remove_old(directory + file + "/", file + "/")

                # Check if directory is now empty and delete if it is
                if not os.listdir(directory + file):
                    send2trash(directory + file)
                    deleteCounter += 1
                    print("deleted: " + directory + file)
                    print()

        else:
            retainedCounter += 1


# Redirect output to log file
sys.stdout = open(get_script_path() + '/CleanerLog.txt', 'a')

# Print date for logging
print("#### " + time.strftime(timeFormat, time.localtime(time.time())))
remove_old(DOWNLOAD_DIRECTORY, DELETION_THRESHOLD)
print("Removed: " + str(deleteCounter ) + " || Retained: " + str(retainedCounter) + "\n")
