#Lesson 05 Notes


# def money(principal: float, interest: float, t: int, n: int = 1) -> float:
#     return principal * (1 + interest/n) ** (n * t)

# new_amount = money(1000, 0.0061, 10, 1)

# print(new_amount)


#File IO

import random
with open('file.txt', 'w') as file:
    for line in range(100):
        random_number = random.randint(50,100)
        file.write(str(random_number) + "\n")

#Open this file, find max, min, and average

with open('file.txt', 'r') as input_file:  
    lines = input_file.readlines()
    # lines_stripped = [line.strip() for line in lines]
    # print(lines)
    count = 0
    min = 1000
    max = 0
    sum = 0
    for line in lines:
        amount = int(line)
        sum += amount
        count += 1
        if amount > max:
            max = amount
        if amount < min:
            min = amount
    average = sum/ count

    print(f"Max: {max}, Min: {min}, Average: {average}")