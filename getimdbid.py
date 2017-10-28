#!/usr/bin/env python3

from imdbpie import Imdb
import os
import sys


imdb = Imdb()

to_be_searched = sys.argv
del to_be_searched[0]

for item in to_be_searched:
    item_results = imdb.search_for_title(item)
    print("####" + item + "####")
    i = 0
    for result in item_results:
        print(str(result)[:-1][1:])
        if i == 2:
            break
        i += 1
