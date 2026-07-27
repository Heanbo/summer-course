# Basic Algorithms

# Exercise 1

# What is the output of this block of code?


# def mut_example(list1, list2, list3):
#     if len(list1) > 2:
#         list1 = list1[:2]
#     list2[0] = "hi"
#     list3 = "".join(list2)

# a_list = [1, 2, 3]
# b_list = ["a", "b", "c"]
# a_str = "do-re-mi"
# mut_example(a_list, b_list, a_str)
# print(a_list)
# print(b_list)
# print(a_str)


# 1, 2, 3
# hi, b, c
# do-re-me

# # Exercise 2

# # What's the difference between sort and sorted?

# # Which one is a list method and which one is a function that works on lists?
# sort displays as a output, sorted creates a new item.
# # Please explain



# Exercise 3

# Write a function that doubles the elements in a list.

# def double(list):
#     for num in range(len(list)):
#         list[num] = 2 * list[num]

# my_list = [1, 2, 3, 4]
# double(my_list)
# print(my_list)


# Do you need to return anything here?
#NO


# Write a function that doubles the elements in a tuple.

def double_tuple(t):
    newlist = []
    for num in range(len(t)):
        newlist.append(2 * t[num])
    return tuple(newlist)
    
    
mytuple = (1, 2, 3)
newlist = double_tuple(mytuple)
print(newlist)

# Do you need to return anything here?



# Exercise 4

# Rewrite the pop, count, extend, reverse, and sort functions


# Return the results in a new list and do not modify the original list

# (do not use the function you are rewriting)


# Exercise 5

# Fractions can be reprsented by the tuple (numerator, denominator)

# Write a function that adds two fractions



# Write a function that multiplies two fractions


# Write a function that simplifies a fraction


# Exercise 6

# write a function to calculate distance between two cartesian coordinates



# extension: make it work for more than two dimensions

