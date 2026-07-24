#Lesson 06 Exercises

#Exercise 1

import random

with open('output.txt', 'w') as output_file:
    for i in range(100):
        random_number = str(random.randint(1,1000))
        output_file.write(random_number + "\n")

with open('output.txt', 'r') as input_file:
    lines = input_file.readlines()
    print(lines)

    new_list = []
    for line in lines:
        line = line.strip()
        line = int(line)
        new_list.append(line)
    print(new_list)

    lines_stripped = [int(line.strip()) for line in lines]
    # print(lines_stripped)

min = 1000
max = 0
count = 0
sum = 0

for line in lines_stripped:
    if line > max:
        max = line

    if line < min:
        min = line

    count += 1
    sum += line

average = sum/count