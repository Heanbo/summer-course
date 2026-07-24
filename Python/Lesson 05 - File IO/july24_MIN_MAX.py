## read july.txt find min, max, and average value of 100 rand int, do not use min() or max() functions


### Imports ###
import os


### VARIABLES ###


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

def Banner():
    os.system('cls')
    #print(f'\n\n\n')
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("=                  Number Gen and Min_Max_AVG Conversions                =")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("")
    
def menu():
    Banner()
    try:
        null = input("Computer > Press Enter to Begin... \nComputer > Or press CTR + C to Exit \nYou > ")
        execution()
    except:
        print("Program Exited")

def execution():
    run = 'yes'
    while run.upper() == 'YES':
        gen = 'NONE'
        gen = input("Computer > Do you want to generate a new number set? (Yes/No): \nYou > ")
        if gen.upper() == 'YES':
            numbergen(100)
        min_max_avg('july.txt')
        print("")
        run = input("Computer > Do you want to run again? (Yes/No):\nYou > ")
        Banner()


### Execution ###
menu()

Banner()
print("Computer > Goodbye.")
