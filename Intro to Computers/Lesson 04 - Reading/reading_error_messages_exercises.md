# Reading

Hands-On exercises for learning to interpret and debug error messages in Python.

- [Reading](#reading)
  - [Hands-On #1: Understanding Python Error Messages](#hands-on-1-understanding-python-error-messages)
    - [Prerequisites](#prerequisites)
    - [Exercise 1: Anatomy of an Error Message](#exercise-1-anatomy-of-an-error-message)
    - [Exercise 2: SyntaxError - Missing Punctuation](#exercise-2-syntaxerror---missing-punctuation)
    - [Exercise 3: NameError - Undefined Variables](#exercise-3-nameerror---undefined-variables)
    - [Exercise 4: TypeError - Wrong Data Types](#exercise-4-typeerror---wrong-data-types)
    - [Exercise 5: IndexError - List Access Errors](#exercise-5-indexerror---list-access-errors)
    - [Exercise 6: KeyError - Dictionary Access Errors](#exercise-6-keyerror---dictionary-access-errors)
    - [Exercise 7: AttributeError - Wrong Methods](#exercise-7-attributeerror---wrong-methods)
    - [Exercise 8: IndentationError - Spacing Issues](#exercise-8-indentationerror---spacing-issues)
    - [Exercise 9: Reading Stack Traces](#exercise-9-reading-stack-traces)
    - [Exercise 10: FileNotFoundError - Missing Files](#exercise-10-filenotfounderror---missing-files)
    - [Stretch: Debugging Multiple Errors](#stretch-debugging-multiple-errors)
  - [Summary](#summary)


## Hands-On #1: Understanding Python Error Messages

**Goal**: Learn to read, interpret, and fix common Python error messages by understanding their structure and meaning.

Error messages are your friends! They tell you exactly what went wrong and where. Learning to read them properly is one of the most important programming skills.

### Prerequisites

Create a new directory for these exercises:

```bash
mkdir reading_errors
cd reading_errors
```

---

### Exercise 1: Anatomy of an Error Message

**Goal**: Understand the parts of a Python error message.

Create a file called `error_example.py` with this code:

```python
def greet(name):
    message = "Hello, " + name
    print(mesage)

greet("Alice")
```

Run it and observe the error:

```bash
python error_example.py
```

**Understanding the Error Message:**

```
Traceback (most recent call last):
  File "error_example.py", line 5, in <module>
    greet("Alice")
  File "error_example.py", line 3, in greet
    print(mesage)  # Typo: mesage instead of message
          ^^^^^^
NameError: name 'mesage' is not defined. Did you mean: 'message'?
```

**Identify these parts:**

1. **Traceback**: Shows the sequence of function calls that led to the error
2. **File name and line number**: Where the error occurred (`line 3`)
3. **Error Type**: `NameError` (tells you what kind of error)
4. **Error Message**: `name 'mesage' is not defined` (explains the problem)
5. **Helpful Suggestion**: `Did you mean: 'message'?` (Python tries to help!)
6. **Visual Indicator**: `^^^^^^` points to the exact problem

✅ *Check*: Fix the typo and verify the program runs successfully.

---

### Exercise 2: SyntaxError - Missing Punctuation

**Goal**: Learn to identify and fix syntax errors.

Create `syntax_errors.py`:

```python
# Error 1
def calculate_total(price, quantity):
    total = price * quantity
    print(f"Total: {total"
    return total

calculate_total(10, 5)
```

Run it and read the error message carefully.

**Questions to answer:**

1. What line number does the error point to?
2. What is the specific error message?
3. What punctuation is missing?

Fix the error, then add this code to the same file:

```python
# Error 2
def greet(name)
    print(f"Hello, {name}")

greet("Bob")
```

Run it again and answer the same questions.

**Common SyntaxErrors:**
- Missing colons (`:`) after `if`, `for`, `while`, `def`
- Unclosed brackets, parentheses, or quotes
- Invalid indentation

✅ *Check*: The file runs without errors and prints both results.

**Hint**: Read the error message from bottom to top: start with the error type and message, then look at the line number.

---

### Exercise 3: NameError - Undefined Variables

**Goal**: Understand NameError and when it occurs.

Create `name_errors.py`:

```python
# Error 1
print(user_name)
user_name = "Charlie"
```

Run it and observe the error.

**Exercise steps:**

1. Read the error message - what does it tell you?
2. Fix the error by reordering the lines
3. Add this code and run again:

```python
# Error 2
favorite_color = "blue"
print(f"My favorite color is {favourite_color}")
```

4. Read the error - does Python suggest a fix?
5. Fix the typo

**Common causes of NameError:**
- Using a variable before it's defined
- Typos in variable names (Python is case-sensitive!)
- Using variables from other files without importing

✅ *Check*: Both examples run successfully without errors.

**Hint**: Pay attention to Python's suggestions - modern Python often suggests the correct variable name!

---

### Exercise 4: TypeError - Wrong Data Types

**Goal**: Understand type mismatches and how to fix them.

Create `type_errors.py`:

```python
# Error 1
age = 25
message = "I am " + age + " years old"
print(message)
```

Run it and read the error.

**Questions:**

1. What types is Python trying to combine?
2. What operation is failing?
3. How can you fix it? (Two possible solutions)

Fix it using string conversion, then add:

```python
# Error 2
quantity = "5"
price = 10.50
total = quantity * price
print(total)
```

**Exercise:**

1. Predict what error you'll get before running it
2. Run it and check if you were right
3. Fix it by converting the string to a number

Add one more:

```python
# Error 3
scores = [85, 90, 78, 92]
index = "2"
print(scores[index])
```

✅ *Check*: All three examples work correctly.

**Hint**: Common fixes include `str()`, `int()`, `float()` conversions.

---

### Exercise 5: IndexError - List Access Errors

**Goal**: Understand list indexing boundaries.

Create `index_errors.py`:

```python
# Error 1
fruits = ["apple", "banana", "cherry"]
print(fruits[3])
```

**Exercise:**

1. Run the code and read the error
2. What index are you trying to access?
3. What is the valid range for this list?
4. Fix it by using a valid index

Then add:

```python
# Error 2
shopping_list = []
first_item = shopping_list[0]
print(first_item)
```

**Exercise:**

1. Read the error message
2. Why can't you access index 0?
3. Fix it by checking if the list is empty first:

```python
shopping_list = []
if len(shopping_list) > 0:
    first_item = shopping_list[0]
    print(first_item)
else:
    print("Shopping list is empty")
```

✅ *Check*: Understanding that lists are 0-indexed and you can't access indices beyond `len(list) - 1`.

**Hint**: Remember Python uses 0-based indexing: [0, 1, 2, ...]. A list of length 3 has valid indices 0, 1, 2.

---

### Exercise 6: KeyError - Dictionary Access Errors

**Goal**: Learn to safely access dictionary values.

Create `key_errors.py`:

```python
# Error 1
student = {
    "name": "Alice",
    "age": 20,
    "major": "Computer Science"
}
print(student["grade"])
```

**Exercise:**

1. Run and read the error - what key is missing?
2. Fix it by adding the missing key
3. Alternative fix: use `.get()` method:

```python
# Safer approach
grade = student.get("grade", "No grade available")
print(grade)
```

Then try this:

```python
# Error 2
inventory = {
    "apples": 10,
    "bananas": 5,
    "oranges": 8
}
print(f"We have {inventory['apple']} apples")  # Missing 's'
```

**Questions:**

1. What's the difference between the error message for a missing key vs a typo?
2. When should you use `dict[key]` vs `dict.get(key)`?

✅ *Check*: You can explain the difference between KeyError and using `.get()` for safe access.

**Hint**: Use `.get()` when you're not sure if a key exists; use `[key]` when you expect it to always exist.

---

### Exercise 7: AttributeError - Wrong Methods

**Goal**: Understand when objects don't have the attributes or methods you're trying to use.

Create `attribute_errors.py`:

```python
# Error 1
text = "hello world"
text.append("!")  # append() is for lists, not strings
print(text)
```

**Exercise:**

1. Run and read the error
2. What method did you try to use?
3. What type is `text`?
4. Fix it using the correct string method (hint: `+` or `.join()`)

Then add:

```python
# Error 2
numbers = [1, 2, 3, 4, 5]
numbers.appendd(6)  # Extra 'd'
print(numbers)
```

And:

```python
# Error 3
result = print("Hello")  # print() returns None
length = result.upper()  # Can't call .upper() on None
```

**Questions:**

1. Why does `print()` return `None`?
2. How can you check what methods are available for an object?
3. What's the difference between a method and an attribute?

✅ *Check*: All three examples are fixed and you understand the difference between methods for different types.

**Hint**: Use `dir(object)` or `help(object)` to see available methods.

---

### Exercise 8: IndentationError - Spacing Issues

**Goal**: Master Python's indentation rules.

Create `indentation_errors.py`:

```python
# Error 1
def calculate_sum(a, b):
result = a + b
return result

print(calculate_sum(5, 3))
```

**Exercise:**

1. Run and read the error
2. Which line has the problem?
3. Fix the indentation

Then add:

```python
# Error 2
def check_grade(score):
    if score >= 90:
        grade = "A"
      print(f"Grade: {grade}")  # Wrong indentation
    return grade

print(check_grade(95))
```
---

### Exercise 9: Reading Stack Traces

**Goal**: Learn to read multi-level error traces to find the root cause.

Create `stack_trace.py`:

```python
def divide_numbers(a, b):
    result = a / b
    return result

def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    avg = divide_numbers(total, count)
    return avg

def process_scores(score_list):
    average = calculate_average(score_list)
    print(f"Average score: {average}")
    return average

# This will cause an error
scores = []
process_scores(scores)
```

**Exercise:**

1. Run the code and look at the complete traceback
2. Answer these questions:
   - Which function was called first?
   - Which function was called last?
   - On which line did the actual error occur?
   - What is the error type and message?
3. Trace the execution path:
   - Line ?? calls `process_scores()`
   - Line ?? calls `calculate_average()`
   - Line ?? calls `divide_numbers()`
   - Line ?? causes the error

**Reading a stack trace (from bottom to top):**

1. Start with the error type and message (bottom)
2. Look at the line where the error occurred
3. Trace backward through the function calls
4. Understand the sequence that led to the error

✅ *Check*: You can trace the error back to the root cause (dividing by zero because the list is empty).

**Fix it:**

```python
def calculate_average(numbers):
    if len(numbers) == 0:
        return 0
    total = sum(numbers)
    count = len(numbers)
    avg = divide_numbers(total, count)
    return avg
```

**Hint**: The most recent call is at the bottom of the traceback, but the root cause might be several function calls earlier!

---

### Exercise 10: FileNotFoundError - Missing Files

**Goal**: Handle file-related errors properly.

Create `file_errors.py`:

```python
# Error 1
with open("nonexistent_file.txt", "r") as file:
    content = file.read()
    print(content)
```

**Exercise:**

1. Run and read the error
2. What file is Python looking for?
3. What directory is Python searching in?

**Fix it using exception handling:**

```python
import os

filename = "nonexistent_file.txt"

# Check if file exists first
if os.path.exists(filename):
    with open(filename, "r") as file:
        content = file.read()
        print(content)
else:
    print(f"Error: {filename} not found")
    print(f"Current directory: {os.getcwd()}")
```

Now add:

```python
# Error 2
data_file = "data/info.txt"  # Directory doesn't exist
with open(data_file, "r") as file:
    content = file.read()
```

**Exercise:**

1. Create the missing directory: `mkdir data`
2. Create the file: `echo "Sample data" > data/info.txt`
3. Run the code again

✅ *Check*: You understand how to check file existence and interpret file path errors.

**Hint**: Use `os.path.exists()` to check before opening, or use try/except for robust error handling.

---

### Stretch: Debugging Multiple Errors

**Goal**: Apply all your error-reading skills to debug a complex program.

Create `debug_challenge.py`:

```python
def calculate_student_grade(scores, student_name):
    total = 0
    for score in scores
        total = total + score
    
    average = total / len(scores)
    
    grade_info = {
        "name": student_name,
        "average": average,
        "total": total
    }
    
    if average >= 90:
        grade_info["letter"] = "A"
    elif average >= 80:
        grade_info["letter"] = "B"
    elif average >= 70
        grade_info["letter"] = "C"
    else:
        grade_info["letter"] = "F"
    
    return grade_info

# Test the function
student_scores = [85, 92, 78, 88]
result = calculate_student_grade(student_scores, "Alice")
print(f"{result['name']} earned a {result['letter']} with an average of {result[average]}")
```

**Challenge:**

1. Run the code and fix the **first** error
2. Run again and fix the **next** error
3. Repeat until the program runs successfully
4. Keep track of each error type you encountered

✅ *Check*: The program runs and outputs: `Alice earned a B with an average of 85.75`

**Reflection Questions:**

1. Which error was hardest to identify?
2. Did you read the error messages carefully or try to guess?
3. How did the line numbers help you?
4. What strategy did you develop for debugging multiple errors?

---

## Summary

You've now learned to read and interpret:

- **SyntaxError**: Missing punctuation, invalid syntax
- **NameError**: Undefined variables, typos
- **TypeError**: Mixing incompatible data types
- **IndexError**: Accessing invalid list indices
- **KeyError**: Accessing missing dictionary keys
- **AttributeError**: Using wrong methods for object types
- **IndentationError**: Incorrect spacing
- **FileNotFoundError**: Missing files or wrong paths
- **Stack Traces**: Multi-level function call errors

**Key Skills:**

✅ Read error messages from bottom to top  
✅ Identify error type, line number, and message  
✅ Use Python's helpful suggestions  
✅ Trace stack traces to find root causes  
✅ Use proper debugging strategies  

**Next Steps:**

- Practice reading errors in your own code
- Don't fear error messages - they're there to help!
- Learn to use a debugger for complex issues
- Study exception handling with try/except blocks
