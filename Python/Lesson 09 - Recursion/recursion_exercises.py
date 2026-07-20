# Hands-On: Recursion in Python
# This file contains exercises on recursion, split into two sections:
# - Hands-On #1: Single Recursion (one recursive call per function)
# - Hands-On #2: Multiple Recursion (two or more recursive calls per function)

# ============================================================================
# Hands-On #1: Single Recursion
# ============================================================================

# Exercise 1: Factorial
# Goal: Calculate n! = n × (n-1) × (n-2) × ... × 1 using recursion

def factorial(n: int) -> int:
    pass

# Test your function
# ✅ Check: factorial(5) should return 120
# print(factorial(5))


# Exercise 2: Sum of List
# Goal: Sum all integers in a list by processing one element at a time
# 🤚 Hint: Use list slicing to remove the last element

def sum_list(num_list: list[int]) -> int:
    pass

# Test your function
# ✅ Check: sum_list([1, 2, 3, 4, 5]) should return 15
# print(sum_list([1, 2, 3, 4, 5]))


# Exercise 3: Countdown
# Goal: Print numbers from n down to 1 using recursion

def countdown(n: int) -> None:
    pass

# Test your function
# ✅ Check: countdown(5) should print: 5 4 3 2 1
# countdown(5)


# Exercise 4: Power Function
# Goal: Calculate base^exponent using recursion (no ** operator)
# 🤚 Hint: Remember that x^3 = x × x^2

def power(base: int, exponent: int) -> int:
    pass

# Test your function
# ✅ Check: power(2, 5) should return 32
# print(power(2, 5))


# Bonus Exercise: Reverse a String
# Goal: Reverse a string using recursion
# 🎯 Extra: Try solving this without using string slicing [-1]

def reverse_string(s: str) -> str:
    pass

# Test your function
# ✅ Check: reverse_string("hello") should return "olleh"
# print(reverse_string("hello"))


# ============================================================================
# Hands-On #2: Multiple Recursion
# ============================================================================

# Exercise 1: Fibonacci Sequence
# Goal: Calculate the nth Fibonacci number using recursion
# Sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21...

def fibonacci(n: int) -> int:
    pass

# Test your function
# ✅ Check: fibonacci(6) should return 8
# print(fibonacci(6))


# Exercise 2: Sum of List (Divide and Conquer)
# Goal: Sum a list by splitting it in half recursively
# 🤚 Hint: Find the midpoint with len(list) // 2

def sum_list_split(num_list: list[int]) -> int:
    pass

# Test your function
# ✅ Check: sum_list_split([1, 2, 3, 4, 5, 6, 7, 8]) should return 36
# print(sum_list_split([1, 2, 3, 4, 5, 6, 7, 8]))


# Exercise 3: Count Paths in Grid
# Goal: Count unique paths from (0,0) to (m-1, n-1) in an m×n grid
# You can only move right or down
# 🤚 Hint: Your current position is (row, col), check if row >= m or col >= n

def count_paths(row: int, col: int, m: int, n: int) -> int:
    pass

# Test your function
# ✅ Check: count_paths(0, 0, 3, 3) should return 6
# print(count_paths(0, 0, 3, 3))


# Exercise 4: Binary Search
# Goal: Search for element x in a sorted array using recursion
# 🤚 Hint: Calculate mid = (low + high) // 2

def binary_search(arr: list[int], low: int, high: int, x: int) -> int:
    pass

# Test your function
arr = [2, 3, 4, 10, 40]
x = 10
result = binary_search(arr, 0, len(arr) - 1, x)
# ✅ Check: Should find 10 at index 3
# if result != -1:
#     print(f"Element is present at index {result}")
# else:
#     print("Element is not present in array")


# Bonus Exercise: Generate All Binary Strings
# Goal: Generate all binary strings of length n
# 🎯 Extra: Try modifying this to generate all subsets of a list
# 🤚 Hint: For each string from the recursive call, create two new strings

def generate_binary_strings(n: int) -> list[str]:
    pass

# Test your function
# ✅ Check: generate_binary_strings(3) should return ['000', '001', '010', '011', '100', '101', '110', '111']
# print(generate_binary_strings(3))