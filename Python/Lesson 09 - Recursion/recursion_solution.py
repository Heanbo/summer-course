# Hands-On: Recursion in Python - SOLUTIONS
# This file contains solutions to the recursion exercises

# ============================================================================
# Hands-On #1: Single Recursion
# ============================================================================

# Exercise 1: Factorial
def factorial(n: int) -> int:
    # Base case: 0! = 1 and 1! = 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: n! = n * (n-1)!
    return n * factorial(n - 1)

# Test
print("Exercise 1 - Factorial:")
print(f"factorial(5) = {factorial(5)}")  # Should be 120
print(f"factorial(0) = {factorial(0)}")  # Should be 1
print()


# Exercise 2: Sum of List
def sum_list(num_list: list[int]) -> int:
    # Base case: if only one element, return it
    if len(num_list) == 1:
        return num_list[0]
    # Recursive case: last element + sum of rest
    return num_list[-1] + sum_list(num_list[:-1])

# Test
print("Exercise 2 - Sum of List:")
print(f"sum_list([1, 2, 3, 4, 5]) = {sum_list([1, 2, 3, 4, 5])}")  # Should be 15
print()


# Exercise 3: Countdown
def countdown(n: int) -> None:
    # Base case: if n is 0, stop
    if n == 0:
        return
    # Recursive case: print n, then countdown from n-1
    print(n, end=" ")
    countdown(n - 1)

# Test
print("Exercise 3 - Countdown:")
print("countdown(5):", end=" ")
countdown(5)
print()
print()


# Exercise 4: Power Function
def power(base: int, exponent: int) -> int:
    # Base case: anything to the power of 0 is 1
    if exponent == 0:
        return 1
    # Recursive case: base * base^(exponent-1)
    return base * power(base, exponent - 1)

# Test
print("Exercise 4 - Power Function:")
print(f"power(2, 5) = {power(2, 5)}")  # Should be 32
print(f"power(3, 3) = {power(3, 3)}")  # Should be 27
print()


# Bonus Exercise: Reverse a String
def reverse_string(s: str) -> str:
    # Base case: empty string or single character
    if len(s) <= 1:
        return s
    # Recursive case: last character + reverse of rest
    return s[-1] + reverse_string(s[:-1])

# Test
print("Bonus - Reverse a String:")
print(f"reverse_string('hello') = {reverse_string('hello')}")  # Should be "olleh"
print(f"reverse_string('python') = {reverse_string('python')}")  # Should be "nohtyp"
print()


# ============================================================================
# Hands-On #2: Multiple Recursion
# ============================================================================

# Exercise 1: Fibonacci Sequence
def fibonacci(n: int) -> int:
    # Base cases
    if n == 0:
        return 0
    if n == 1:
        return 1
    # Recursive case: sum of previous two numbers
    return fibonacci(n - 1) + fibonacci(n - 2)

# Test
print("Exercise 1 - Fibonacci:")
print(f"fibonacci(6) = {fibonacci(6)}")  # Should be 8
print(f"fibonacci(10) = {fibonacci(10)}")  # Should be 55
print()


# Exercise 2: Sum of List (Divide and Conquer)
def sum_list_split(num_list: list[int]) -> int:
    # Base case: single element
    if len(num_list) == 1:
        return num_list[0]
    # Recursive case: split in half and sum each half
    mid = len(num_list) // 2
    left_sum = sum_list_split(num_list[:mid])
    right_sum = sum_list_split(num_list[mid:])
    return left_sum + right_sum

# Test
print("Exercise 2 - Sum of List (Divide and Conquer):")
print(f"sum_list_split([1, 2, 3, 4, 5, 6, 7, 8]) = {sum_list_split([1, 2, 3, 4, 5, 6, 7, 8])}")  # Should be 36
print()


# Exercise 3: Count Paths in Grid
def count_paths(row: int, col: int, m: int, n: int) -> int:
    # Base case: reached the destination
    if row == m - 1 and col == n - 1:
        return 1
    # Base case: out of bounds
    if row >= m or col >= n:
        return 0
    # Recursive case: paths going right + paths going down
    return count_paths(row + 1, col, m, n) + count_paths(row, col + 1, m, n)

# Test
print("Exercise 3 - Count Paths in Grid:")
print(f"count_paths(0, 0, 3, 3) = {count_paths(0, 0, 3, 3)}")  # Should be 6
print(f"count_paths(0, 0, 2, 2) = {count_paths(0, 0, 2, 2)}")  # Should be 2
print()


# Exercise 4: Binary Search
def binary_search(arr: list[int], low: int, high: int, x: int) -> int:
    # Base case: element not found
    if high < low:
        return -1
    
    # Calculate middle index
    mid = (low + high) // 2
    
    # Base case: found the element
    if arr[mid] == x:
        return mid
    # Recursive case: search left half
    elif arr[mid] > x:
        return binary_search(arr, low, mid - 1, x)
    # Recursive case: search right half
    else:
        return binary_search(arr, mid + 1, high, x)

# Test
print("Exercise 4 - Binary Search:")
arr = [2, 3, 4, 10, 40]
x = 10
result = binary_search(arr, 0, len(arr) - 1, x)
if result != -1:
    print(f"Element {x} is present at index {result}")
else:
    print("Element is not present in array")
print()


# Bonus Exercise: Generate All Binary Strings
def generate_binary_strings(n: int) -> list[str]:
    # Base case: no more digits to add
    if n == 0:
        return [""]
    
    # Recursive case: get all strings of length n-1
    smaller_strings = generate_binary_strings(n - 1)
    
    # For each smaller string, create two new strings (with '0' and '1')
    result = []
    for s in smaller_strings:
        result.append(s + "0")
        result.append(s + "1")
    
    return result

# Alternative more concise solution:
def generate_binary_strings_concise(n: int) -> list[str]:
    if n == 0:
        return [""]
    smaller = generate_binary_strings_concise(n - 1)
    return [s + bit for s in smaller for bit in ["0", "1"]]

# Test
print("Bonus - Generate All Binary Strings:")
print(f"generate_binary_strings(3) = {generate_binary_strings(3)}")
# Should be ['000', '001', '010', '011', '100', '101', '110', '111']
print()


# ============================================================================
# Additional Examples
# ============================================================================

# Example: Infinite Recursion (DO NOT UNCOMMENT)
# This will cause a RecursionError because there's no base case
'''
def bad_recursion():
    return bad_recursion()

bad_recursion()  # This will crash!
'''
