#!/usr/bin/env python3


print("Input grades (first three LK). Hit Enter to calculate and stop input")
counter = 0
sum = 0
while True:
    counter += 1
    grade = input(str(counter) + ": ")
    if grade == "":
        counter -= 1
        break
    if counter < 7:
        counter += 1
        sum += int(grade)
    sum += int(grade)

print("Average: " + str(sum / counter))
print(str((17 - (sum / counter)) / 3))
