# MESSY_CALCULATOR
# Below you are given a simple calculator function. Follow the Hands On exercises to implement Clean Code methodology.

# Hands On 1: Using PEP 8
# Goal: Fix basic formatting like indentation and spacing.
# This code is "messy" because of inconsistent indentation and missing spaces around operators.
v1 = int(input("Please enter the first number:"))
v2 = int(input("Please enter the second number: "))
z = x + y  # Error: x and y are not defined here
return z   # Error: 'return' can only be used inside a function


# Hands On 2: Naming Conventions
# Goal: Replace ambiguous names (v1, v2, z) with descriptive ones.
# We use 'snake_case' for variables to make the code self-documenting.
first_val = int(input("Please enter the first number: "))
second_val = int(input("Please enter the second number: "))
result = first_val + second_val


# Hands On 3: Functions
# Goal: Modularize code into "Pure Functions" with a single responsibility.
def get_user_input():    
    """Asks the user for two integers and returns them as a tuple."""
    # We remove the parameters from the definition because input() creates new values.
    first = int(input("Please enter the first number: "))
    second = int(input("Please enter the second number: "))
    return first, second

def calc(num_1, num_2):
    """Takes two numbers as arguments and returns their mathematical sum."""
    return num_1 + num_2

#Test
#calc(get_user_input())


# Hands On 4: Python Built-Ins
# Goal: Use the standard sum() function correctly.
# sum() requires an 'iterable' (like a list), not individual comma-separated numbers.
def calc_with_sum(num_1, num_2): 
    # We group the arguments into a list [] so sum() can iterate over them.
    add_vals = [num_1, num_2]
    return sum(add_vals)


# Hands On 5: Pylint
# Goal: Finalize the code to pass automated style checks.
# At this stage, we add 'Type Hints' and 'Docstrings' to explain the module.
"""Module for performing basic arithmetic calculations."""

def get_user_input():    
    """Asks the user for two integers and returns them as a tuple."""
    first_val = int(input("Please enter the first number: "))
    second_val = int(input("Please enter the second number: "))
    return first_val, second_val

def calc(num_1, num_2): 
    """Takes two numbers as arguments and returns their mathematical sum using sum()."""
    add_vals = [num_1, num_2]
    return sum(add_vals)


# Hands On Extra Credit: Optimize
# Goal: Use advanced Python features like List Comprehensions and Default Arguments.
def get_optimized_sum(count: int = 2) -> int:
    """
    1. 'range(count)' creates a loop for the specified number of times.
    2. The List Comprehension runs 'input()' and 'int()' conversion in one line.
    3. 'sum()' aggregates the resulting list into a single final total.
    """
    return sum([int(input(f"Enter number {i+1}: ")) for i in range(count)])