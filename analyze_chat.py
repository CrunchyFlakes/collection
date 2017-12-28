#!/usr/bin/env python3


chat = open("/home/mtoepperwien/Documents/python_data/chat_josi.txt")

word_count = {}
different_words_counted = 0
words_counted = 0

def delete_out_string(string, list):
    for substring in list:
        string.replace(substring, "")
    return string

for line in chat:
    if "Josefeen" in line:
        line = line[line.find(":") + 2:]
        line = line[line.find(":") + 2:]
        line = line.replace("\n", " ").replace(".", "").replace(",", "").replace("?", "").replace("!", "").replace(":", "").replace("  ", " ").replace("\"", "").replace("(", "").replace(")", "")
        line = line.split(" ")
        for word in line:
            word = word.lower()
            if word not in word_count:
                word_count[word] = 1
                different_words_counted += 1
            elif word is "":
                continue
            else:
                word_count[word] = word_count[word] + 1
            words_counted += 1

word_list = []

for word in word_count:
    word_list.append(word)


def swap(i_x, i_y):
    word_list[i_y], word_list[i_x] = word_list[i_x], word_list[i_y]

for x in range(1, len(word_list)):
    to_be_switched = x
    count_to_be_switched = word_count[word_list[to_be_switched]]
    while True:
        to_be_switched_with = to_be_switched - 1
        if to_be_switched_with < 0:
            break
        count_to_be_switched_with = word_count[word_list[to_be_switched_with]]
        if count_to_be_switched > count_to_be_switched_with:
            swap(to_be_switched, to_be_switched_with)
            to_be_switched += -1
        else:
            break


for word in word_list:
    print(word + ": " + str(word_count[word]) + " || " + str((word_count[word] / words_counted) * 100) + "%")

print("different words: " + str(different_words_counted))
print("words counted: " + str(words_counted))