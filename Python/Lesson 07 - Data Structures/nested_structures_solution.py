# Exercise 1:  Given a list of numbers, convert the list into a list of triples
# [1, 2, 3, 4, 5, 6] => [(1, 2, 3), (4, 5, 6)]
my_list = list(range(1, 7))
tuple_list = [tuple(my_list[0:3]), tuple(my_list[3:])]

print('\n\nEx. 1')

print('tupled list: ', tuple_list)

# Exercise 2:  Find the last element of a nested list
# [[1, 2, 3], [4, 5, 6]] => 6
my_nested_list = [[1, 2, 3], [4, 5, 6]]
last = my_nested_list[-1][-1]

print('\n\nEx. 2')

print('last element: ', last)

# Exercise 3:  Create a function that lists the first N numbers in a table
# format with C columns.  Fill any remaining values with None.


import math


def list_numbers(N, C, my_numbers):
    rows = math.ceil(N / C)
    counter = 0
    my_table = []
    while counter < rows * C:
        for row in range(rows):
            new_row = []
            for col in range(C):
                if counter < len(my_numbers):
                    new_row.append(my_numbers[counter])
                else:
                    new_row.append(None)
                counter += 1
            my_table.append(new_row)
    return my_table


my_numbers = [x for x in range(25)]

print('\n\nEx. 3')

print(list_numbers(16, 4, my_numbers))


# Exercise 4: Create a function called make_table() that takes a number n as its only parameter.  
# Your function should create a table of size n x n containing random numbers from 1 through 9.
import random

def make_table(n):
    table = []
    for row in range(n):
        elems = []
        for col in range(n):
            elems.append(random.randint(1, 9))
        table.append(elems)
    return table


my_table = make_table(5)

print('\n\nEx. 4')

print(my_table)



# Exercise 5:  Given a list of items, write a program that generates a list of 
# lists in the following form:
# [a, b, c, ... , z] => [[z], [z, y], [z, y, x], ...]

def list_list(data):
    my_list = []
    for elem in range(2, len(data) + 2):
        my_list.append(data[:-elem:-1])
    return my_list


print('\n\nEx. 5')

data = ['a', 'b', 'c', 'd', 'e']

print(list_list(data))


# Exercise 6:  You have a list of numbers stored as [[1, 2, 3], [4, 5, 6]]
# Convert the numbers to their digit representation

def digit_gen(my_list):
    for i in range(len(my_list)):
        num = 0
        for j in range(len(my_list[i])):
            num += (10 ** j) * my_list[i][-(j + 1)]
        my_list[i] = num
    return my_list


print('\n\nEx. 6')

my_list = [[1, 2, 3], [4, 5, 6]]

print(digit_gen(my_list))


# Exercise 7:  Write a function to create the tabula recta and return it
# https://www.dcode.fr/tools/vigenere/images/table.png

def tabula_recta():
    data = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    tabula = {}
    for i in range(len(data)):
        tabula[data[i]] = (data[i:] + data[0:i])
    return tabula


print('\n\nEx. 7')

print(tabula_recta())


# Exercise 8:  Write a function to print the tabula recta in the correct format

def print_tabula_recta():
    tabula = tabula_recta()
    print('   ', '    '.join(tabula['A']))
    for i in tabula:
        print(i, tabula[i])


print('\n\nEx. 8')

print_tabula_recta()

# Exercise 9:  Write a function to encode a message using the tabula recta
# It will need three agurments, the table, a message, and the key
# (it might be easier to write another function to "encode" a single letter
# you can then verify that against the tabula recta)


def encode(tabula, message, key):
    cryptic = ''
    for letter in message.upper():
        if letter.isalpha():
            cryptic += tabula[key][ord(letter) - ord('A')]
        else:
            cryptic += letter
    return cryptic


message = 'Python is fun!'
key = 'E'
print('\n\nEx 9')

cryptic = encode(tabula_recta(), message, key)

print(cryptic)

# Exercise 10:  Write a function to decode a message using the tabula recta
# It will need three arguments, the table, a message, and the key


def decode(tabula, cryptic, key):
    message = ''
    for letter in cryptic.upper():
        if letter.isalpha():
            message += tabula[letter][ord('A') - ord(key)]
        else:
            message += letter
    return message


print('\n\nEx 10')

message = decode(tabula_recta(), cryptic, key)

print(message)
