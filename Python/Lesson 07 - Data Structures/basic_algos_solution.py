# Basic Algorithms

# Exercise 1

### What is the output of this block of code?

print('\n\nEx 1\n')

def mut_example(list1, list2, list3):
    if len(list1) > 2:
        list1 = list1[:2]
    list2[0] = "hi"
    list3 = "".join(list2)

a_list = [1, 2, 3]
b_list = ["a", "b", "c"]
a_str = "do-re-mi"
mut_example(a_list, b_list, a_str)
print(a_list)
print(b_list)
print(a_str)

'''
# output:
[1, 2, 3]
['hi', 'b', 'c']
do-re-mi
'''

## Exercise 2

### What's the difference between sort and sorted?

### Which one is a list method and which one is a function that works on lists?
'''
Solution:

sort() is a list method that operates on a list (mutable) in place. sort() returns 'None'.

sorted() is a function that takes a list as input and returns a sorted copy. The list IS NOT implicitly over-written.
'''
## Exercise 3

### Write a function that doubles the elements in a list.

# without return statement:
print('\n\nEx 3\n')

def double(my_list):
    for i in range(len(my_list)):
        my_list[i] = 2 * my_list[i]

my_list = [1, 2, 3]
double(my_list)
print(my_list)
# output: [2, 4, 6]


# with list comprehension (requires return statement)

def double(my_list):
    return [x * 2 for x in my_list]

my_list = [1, 2, 3]
new_list = double(my_list)
print(my_list)
print(new_list)
# output: [1, 2, 3]
#         [2, 4, 6]


### Do you need to return anything here?

'''If the list is being operated on by the function, no return statement is needed. 
If the elements are being operated on, a return statment is needed.
'''
### Write a function that doubles the elements in a tuple.


def tuple_double(my_tuple):
    return tuple(x * 2 for x in my_tuple)

my_tuple = (1, 2, 3)
new_tuple = tuple_double(my_tuple)
print(my_tuple)
print(new_tuple)

'''# output: (1, 2, 3)
             (2, 4, 6)
'''
### Do you need to return anything here?

'''Yes, because tuple is an immutable data structure. 
A new tuple must be created and returned from data from the original tuple.
'''
## Exercise 4

print('\n\nEx 4\n')


### Rewrite the pop, count, extend, reverse, and sort functions

# pop()
def my_pop(my_list):
    return my_list[:-1]

# count()
def my_count(my_list):
    counter = 0
    for _ in my_list:
        counter += 1
    return counter

# extend
def my_extend(my_list, other_data):
    other_data = list(other_data)
    return my_list + other_data

# reverse
def my_reverse(my_list):
    return my_list[::-1]

# sort
def my_sort(my_list):
    sorted_list = []
    for i in range(len(my_list)):
        min_idx = i
        for j in range(i + 1, len(my_list)):
            if my_list[j] < my_list[min_idx]:
                min_idx = j
        # Swap the found minimum element with the first element
        my_list[i], my_list[min_idx] = my_list[min_idx], my_list[i]
    return my_list

my_list = [5, 3, 25, 4, 10]
popped = my_pop(my_list)
counted = my_count(my_list)
my_tuple = (1, 2)
extended = my_extend(my_list, my_tuple)
revrsd = my_reverse(my_list)
sortsort = my_sort(my_list)

print(popped)
print(counted)
print(extended)
print(revrsd)
print(sortsort)

'''
output:

[5, 3, 25, 4]
5
[5, 3, 25, 4, 10, 1, 2]
[10, 4, 25, 3, 5]
[3, 4, 5, 10, 25]
'''


### Return the results in a new list and do not modify the original list

### (do not use the function you are rewriting)


## Exercise 5

### Fractions can be reprsented by the tuple (numerator, denominator)

### Write a function that adds two fractions

print('\n\nEx 5\n')


def add_fractions(frac1, frac2):
    return ((frac1[0] * frac2[1] + frac1[1] * frac2[0]), frac1[1] * frac2[1])


### Write a function that multiplies two fractions

def multiply_fractions(frac1, frac2):
    return (frac1[0] * frac2[0], frac1[1] * frac2[1])


### Write a function that simplifies a fraction

def simplify_fractions(frac):
    # handle simple case
    if frac[1] % frac[0] == 0:
        return (1, int(frac[1] / frac[0]))
    # evaluate from numerator to 2 for simplifications
    for i in range(frac[0], 1, -1):
        if frac[0] % i == 0 and frac[1] % i == 0:
            return (int(frac[0] / i), int(frac[1] / i))
    # handle case with no simplification possible
    return frac

### Example output:

frac1 = (1, 3)
frac2 = (4, 5)
print(add_fractions(frac1, frac2))
print(multiply_fractions(frac1, frac2))

frac = (5, 25)
print(simplify_fractions(frac))
'''
output:
(17, 15)
(4, 15)
(1, 5)
'''

## Exercise 6

### write a function to calculate distance between two cartesian coordinates

print('\n\nEx 6\n')


import math


# 2-dimensional (flat plane)
def cartesian_distance(point1, point2):
    return math.sqrt(
        ((point2[0] - point1[0]) ** 2)
        + ((point2[1] - point1[1]) ** 2))


point1 = (1, 3)
point2 = (4, 7)
print(cartesian_distance(point1, point2))


### extension: make it work for more than two dimensions

# import math


# multi-dimensional space. extends to N-dimensions
def euclidian_distance(point1, point2):
    under_root = 0
    for i in range(len(point1)):
        under_root += (point2[i] - point1[i]) ** 2
    return math.sqrt(under_root)


point1 = (1, 3, 5, 7)
point2 = (3, 5, 7, 9)
print(euclidian_distance(point1, point2))

