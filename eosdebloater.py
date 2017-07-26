#!/usr/bin/env python3
# Script hiding unwanted elementary os preinstalled programs
import os

import sys

globalDeskEntries = '/usr/share/applications/'
#localDeskEntries = '~/.local/share/applications/'

entriesToHide = []
entriesToHide.extend(["org.pantheon.scratch.desktop", "JB-jvisualvm-jdk8.desktop", "JB-jconsole-jdk8.desktop", "JB-mission-control-jdk8.desktop", "JB-java-jdk8.desktop", "JB-javaws-jdk8.desktop", "maya-calendar.desktop", "org.pantheon.snap.desktop", "epiphany.desktop", "org.pantheon.mail.desktop", "gala-multitaskingview.desktop", "org.pantheon.noise.desktop", "org.pantheon.photos.desktop", "simple-scan.desktop", "org.pantheon.audience.desktop" ])

# check if run with root permissions
if not os.geteuid() == 0:
    sys.exit("\nMissing root permissions! Run with sudo or as root.")

for entry in entriesToHide:
    try:
        # copy content of entry into fileContents
        entryFile = open((globalDeskEntries + entry), "r")
        fileContents = entryFile.readlines()
        entryFile.close()

        # search for "[Desktop Entry]" in fileContents
        lineIndex = 0
        targetLine = 0
        replace = None
        for line in fileContents:
            lineIndex += 1
            if line == "[Desktop Entry]\n":
                targetLine = lineIndex
            elif line == "NoDisplay=true\n" or line == "NoDisplay=false\n":
                targetLine = lineIndex
                replace = True


        if not replace:
            # add line for hiding entry in fileContents
            fileContents.insert(targetLine, "NoDisplay=true\n")
        elif replace:
            fileContents[targetLine - 1] = "NoDisplay=true\n"

        # write fileContents back to entryFile
        entryFile = open((globalDeskEntries + entry), "w")
        entryFile.writelines(fileContents)
        entryFile.close()

        print(entry + " is now hidden.")
    except:
        print(entry + "could not be made hidden")

print("finished")