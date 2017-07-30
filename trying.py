already_converted_txt = open("testlog.txt", "r+")
already_converted_list = already_converted_txt.readlines()
#os.remove(already_converted_list[-1])
already_converted_list = already_converted_list[:-1]
for thingy in already_converted_list:
    print(thingy)
already_converted_txt.seek(0)
already_converted_txt.truncate()
already_converted_txt.writelines(already_converted_list)
already_converted_txt.close()
