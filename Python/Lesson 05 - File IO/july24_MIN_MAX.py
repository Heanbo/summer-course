## read july.txt find min, max, and average value of 100 rand int, do not use min() or max() functions


### Imports ###
import os


### VARIABLES ###
run = 'Yes'
runup = run.upper()

### FUNCTIONS ###
def numbergen (lines:int) -> int:
    import random
    count = 0
    with open('july.txt', 'w') as file:
        file.write('')
    while count < lines:
        random_integer = random.randint(50, 100)
        with open('july.txt', 'a') as file:
            file.write(f"{random_integer}\n")
        count += 1

def min_max_avg(file_path: str) -> None:
    total = 0
    number_of_lines = 0
    min_value = None
    max_value = None
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for lines in lines:
            #print(int(lines))
            number_of_lines += 1
            total = total + int(lines)
            if min_value is None or int(lines) < min_value:
                min_value = int(lines)
            if max_value is None or int(lines) > max_value:
                max_value = int(lines)
    
    print(f"Total: {total}")
    print(f"Count: {number_of_lines}")
    print(f"Min: {min_value}, Max: {max_value}")
    print(f"Average: {total / number_of_lines}")


### WELCOME MESSAGE ###
os.system('cls')
#print(f'\n\n\n')
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("=                  Number Gen and Min_Max_AVG Conversions                =")
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("")


### EXECUTION ###
while run.upper() != 'Yes':
    print(f"DEBUG: EXECUTION {run.upper} {runup}")
    gen = 'NONE'
    gen = input("Computer > Do you want to generate a new number set? (Yes/No): \nYou > ")
    if gen.upper == 'Yes':
        numbergen(100)
    min_max_avg('july.txt')
    print("")
    run = input("Computer > Do you want to run again? (Yes/No):\nYou > ")

print("END OF CODE")
