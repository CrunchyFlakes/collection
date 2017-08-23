#!/usr/bin/env python3


print("Input grades (first three LK). Hit Enter to calculate and stop input")
counter = 0
dividend = 0
sum = 0
while True:
    counter += 1
    grade = input(str(counter) + ": ")
    if grade == "":
        break
    if counter <= 3:
        dividend += 1
        sum += int(grade)
    sum += int(grade)
    dividend += 1

print("Average: " + str(sum / dividend))
print("         ≙" + str((17 - (sum / dividend)) / 3))
