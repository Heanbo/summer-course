# ============================================================================
# Recursion Examples - Solutions from PowerPoint
# ============================================================================

# ----------------------------------------------------------------------------
# Example 1: Factorial
# ----------------------------------------------------------------------------
def factorial(n: int) -> int:
    if n == 1 or n == 0:
        return 1
    return n * factorial(n - 1)

print("Factorial Examples:")
print(f"5! = {factorial(5)}")
print(f"10! = {factorial(10)}")
print()


# ----------------------------------------------------------------------------
# Example 2: Sum of List (Single Recursion)
# ----------------------------------------------------------------------------
def re_sum_one(num_list: list[int]) -> int:
    if len(num_list) == 1:
        return num_list.pop()
    
    last = num_list.pop()
    print(f"Calculating {num_list[:]} + {last}")
    return re_sum_one(num_list[:]) + last

print("Sum of List (Single Recursion):")
numbers = list(range(1, 11))
print(f"Sum of {list(range(1, 11))} = {re_sum_one(numbers[:])}")
print()


# ----------------------------------------------------------------------------
# Example 3: Palindrome Checker
# ----------------------------------------------------------------------------
def is_palindrome(s: str) -> bool:
    # Remove spaces and convert to lowercase for comparison
    s = s.replace(" ", "").lower()
    
    # Base case: empty string or single character is a palindrome
    if len(s) <= 1:
        return True
    
    # Check if first and last characters match
    if s[0] != s[-1]:
        return False
    
    # Recursively check the middle portion
    return is_palindrome(s[1:-1])

print("Palindrome Checker:")
print(f"is_palindrome('racecar') = {is_palindrome('racecar')}")
print(f"is_palindrome('hello') = {is_palindrome('hello')}")
print(f"is_palindrome('A man a plan a canal Panama') = {is_palindrome('A man a plan a canal Panama')}")
print()


# ----------------------------------------------------------------------------
# Example 4: String to Integer
# ----------------------------------------------------------------------------
def string_to_int(s: str) -> int:
    # Base case: single digit
    if len(s) == 1:
        return int(s)
    
    # Recursive case: convert all but last digit, multiply by 10, add last digit
    return string_to_int(s[:-1]) * 10 + int(s[-1])

print("String to Integer:")
print(f"string_to_int('1234') = {string_to_int('1234')}")
print(f"string_to_int('99') = {string_to_int('99')}")
print()


# ----------------------------------------------------------------------------
# Example 5: Fibonacci (Multiple Recursion)
# ----------------------------------------------------------------------------
def fib(n: int) -> int:
    """
    0, 1, 2, 3, 4, 5, 6,  7,  8, ...
    0, 1, 1, 2, 3, 5, 8, 13, 21, ...
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return fib(n - 1) + fib(n - 2)

print("Fibonacci Sequence:")
print(f"fib(6) = {fib(6)}")
print(f"fib(10) = {fib(10)}")
print()


# ----------------------------------------------------------------------------
# Example 4: Sum of List (Divide and Conquer - Multiple Recursion)
# ----------------------------------------------------------------------------
def re_sum_half(num_list: list[int]) -> int:
    if len(num_list) == 1:
        return num_list[0]
    
    half = len(num_list) // 2
    return re_sum_half(num_list[:half]) + re_sum_half(num_list[half:])

print("Sum of List (Divide and Conquer):")
numbers = list(range(1, 9))
print(f"Sum of {numbers} = {re_sum_half(numbers[:])}")
print()


# ----------------------------------------------------------------------------
# Example 6: Max Value of Array
# ----------------------------------------------------------------------------
def max_value(arr: list[int]) -> int:
    # Base case: single element
    if len(arr) == 1:
        return arr[0]
    
    # Recursive case: max of first element and max of rest
    max_of_rest = max_value(arr[1:])
    return arr[0] if arr[0] > max_of_rest else max_of_rest

print("Max Value of Array:")
numbers = [3, 7, 2, 9, 1, 5]
print(f"max_value({numbers}) = {max_value(numbers)}")
print()


# ----------------------------------------------------------------------------
# Example 7: Grid Path Counter
# ----------------------------------------------------------------------------
def count_paths(row: int, col: int, m: int, n: int) -> int:
    """Count unique paths from (0,0) to (m-1, n-1) moving only right or down"""
    # Base case: reached destination
    if row == m - 1 and col == n - 1:
        return 1
    
    # Base case: out of bounds
    if row >= m or col >= n:
        return 0
    
    # Recursive case: paths going right + paths going down
    return count_paths(row + 1, col, m, n) + count_paths(row, col + 1, m, n)

print("Grid Path Counter:")
print(f"count_paths(0, 0, 3, 3) = {count_paths(0, 0, 3, 3)}")
print(f"count_paths(0, 0, 2, 2) = {count_paths(0, 0, 2, 2)}")
print()


# ----------------------------------------------------------------------------
# Example 8: Binary Search
# ----------------------------------------------------------------------------
def binary_search(arr, low, high, x):
    """assumes array is already sorted"""
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1

print("Binary Search:")
arr = [2, 3, 4, 10, 40]
x = 10
result = binary_search(arr, 0, len(arr) - 1, x)
if result != -1:
    print(f"Element {x} is present at index {result}")
else:
    print("Element is not present in array")
print()


# ----------------------------------------------------------------------------
# Example 9: Directory Traversal
# ----------------------------------------------------------------------------
import os

def list_dir_recursive(directory):
    for entry in os.listdir(directory):
        full_path = os.path.join(directory, entry)
        if os.path.isdir(full_path):
            list_dir_recursive(full_path)
        else:
            print(full_path)

# Uncomment to test (replace with a valid directory path):
# list_dir_recursive('.')


# ----------------------------------------------------------------------------
# Warning: Infinite Recursion Example (DO NOT UNCOMMENT)
# ----------------------------------------------------------------------------
# def bad():
#     return bad()
#
# bad()  # This will cause a Stack Overflow!
