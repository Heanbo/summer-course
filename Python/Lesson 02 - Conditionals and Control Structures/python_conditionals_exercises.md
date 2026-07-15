# Hands-On: Python Conditional Statements

These exercises focus on using `if`, `elif`, and `else` statements to control program flow. You'll work with comparison operators, logical operators, and data types from Lesson 1 to make decisions in your code.  Write each exercise as a separate python script.

---

## Hands-On #1:

---

### Exercise 1: Check if a Number is Positive

**Goal**: Write a Python Script that asks a user for an integer number, and then checks if the number is positive using an `if` statement.

number=int(input("Enter a number. "))
 if number > 0:
    print(f"The number {number} is positive!")
elif number == 0:
    print(f"That number is zero!")
elif number <0:
    print(f"The number {number} is negative!")


✅ *Check*: Should print "The number is positive" if the number is greater than 0.

---

### Exercise 2: Even or Odd

**Goal**: Write a Python script that asks a user for an integer number.  Check if the number is even or odd using `if` and `else`.

number=int(input("Enter a number. "))
remainder=number%2

if remainder > 0:
    print(f"The number {number} is ODD!")
else:
    print(f"The number {number} is EVEN!")



✅ *Check*: Should print "Even" or "Odd" based on the number.

---

### Exercise 3: Age Category

**Goal**: Write a python script that asks a user for their age, and then uses `if`, `elif`, and `else` to print the correct category for the person by based on their age.

- Under 13: "Child"
- 13-19: "Teenager"
- 20-64: "Adult"
- 65+: "Senior"


age=int(input("Enter your age"))

if age>=65:
    print("You are a Senior!")
elif age>=20:
    print("You are an Adult!")
elif age>=13:
    print("You are a Teenager!")
else:
    print("You are a Child!")



✅ *Check*: Should print the correct category based on age.

---

### Exercise 4: Compare Two Numbers

**Goal**: Write a Python Script that asks a user for two numbers.  Compare the two numbers and print which is larger, or if they're equal.

```python
a = 10
b = 20
```


number1=int(input("Enter a number. "))
number2=int(input("Enter another number. "))

if number1>number2:
    print(f"{number1} is Larger than {number2}.")
elif number1==number2:
    print("Both numbers are EQUAL")
elif number1<number2:
    print(f"{number2} is Larger than {number1}.")
else:
    print("ERROR")



✅ *Check*: Should print "{first_number} is larger", "{second_number} is larger", or "The numbers are equal".

---

### Exercise 5: Grade Converter

**Goal**: Write a Python Script that asks a user for a numeric grade, and then converts a numeric grade to a letter grade and prints the letter grade.

- 90+: A
- 80-89: B
- 70-79: C
- 60-69: D
- Below 60: F



score=int(input("Enter your grade"))
if score >= 90:
    print(“Grade: A”)
elif score >= 80:
    print(“Grade: B”)
elif score >= 70:
    print(“Grade: C”)
elif score >= 60:
    print(“Grade: D”)
else:
    print(“Grade: F”)




✅ *Check*: Should print the correct letter grade.

---

### Exercise 6: String Length Check

**Goal**: Write a Python Script that asks the user for an input string.  Then check if a string has more than 10 characters.  Print "Long string" if it is longer than 10 characters, print "Short string" if it is shorter.



✅ *Check*: Should print "Long string" if length is greater than 10, otherwise "Short string".

---

### Exercise 7: Logical AND Operator

**Goal**: Write a Python script that asks the user for a number.  Check if a number is between 10 and 20 (inclusive) using the `and` operator.  Print "Number is in range" if it is in between 10 and 20.  Otherwise it should print "Out of range."

```python
number = 15
```

number=int(input("Enter a number. "))
if number>10 and number<20:
    print("Number is in range")
else:
    print("Out of range.")




✅ *Check*: Should print "Number is in range" if between 10 and 20, otherwise should print "Out of range".

---

### Exercise 8: Logical OR Operator

**Goal**: Write a python script that checks if a character is a vowel using the `or` operator.  Print "vowel" or "consonant" depending on the input.


letter=input("Enter a letter. ")
if letter=="a" or letter=="e" or letter=="i" or letter=="o" or letter=="u":
    print("That is a vowel")
else:
    print("That is a Consnant")



✅ *Check*: Should print "Vowel" if the letter is a, e, i, o, or u, else "Consonant".

---

### Stretch:  Exercise 9: Leap Year Checker

**Goal**: Write a Python Script that asks the user for the year.  Determine if a year is a leap year.  Print the result.

Rules:
- Divisible by 4 AND not divisible by 100, OR
- Divisible by 400


✅ *Check*: Should print "Leap year" or "Not a leap year".

---

### Stretch:  Exercise 10: Nested Conditionals - BMI Calculator

**Goal**: Write a Python Script that asks the user for their weight in kilograms and their height in meters.  Calculate BMI category using correct `if-elif-else` structure.

- BMI < 18.5: "Underweight"
- BMI 18.5-24.9: "Normal weight"
- BMI 25-29.9: "Overweight"
- BMI 30+: "Obese"

Formula: BMI = weight (kg) / height (m)²



✅ *Check*: Should calculate BMI and print the correct category.



---
## Hands-On #2:
---

### Exercise 11: Create and Print a List

**Goal**: Create a list of your favorite colors and print each color using a `for` loop.

```python
colors = ["red", "blue", "green"]
```

✅ *Check*: Each color should be printed on a separate line.

---

### Exercise 12: List Length

**Goal**: Create a list of numbers and print how many items are in the list.

```python
numbers = [5, 10, 15, 20, 25]
```

✅ *Check*: Should print "The list has 5 items".

---

### Exercise 13: Append to a List

**Goal**: Start with an empty list and add 5 different items to it using `append()`.

```python
my_list = []
```

✅ *Check*: List should contain 5 items after appending.

---

### Exercise 14: Loop Through a Range

**Goal**: Use a `for` loop with `range()` to print numbers 1 through 10.

✅ *Check*: Should print numbers 1, 2, 3, ..., 10.

---

### Exercise 15: Sum Numbers in a List

**Goal**: Calculate the sum of all numbers in a list using a `for` loop.

```python
numbers = [4, 7, 2, 9, 12]
```

✅ *Check*: Should print the total sum: 34.

---

### Exercise 16: List Membership

**Goal**: Check if a fruit is in a list of available fruits.

```python
available_fruits = ["apple", "banana", "orange", "mango"]
fruit = "banana"
```

✅ *Check*: Should print "In stock" if fruit is in the list, else "Out of stock".

---

### Exercise 17: Count Even Numbers

**Goal**: Count how many even numbers are in a list using a `for` loop.

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

for number in numbers:

✅ *Check*: Should print "There are 5 even numbers".

---

### Exercise 18: While Loop Countdown

**Goal**: Use a `while` loop to count down from 10 to 1.

```python
count = 10
```

✅ *Check*: Should print 10, 9, 8, ..., 2, 1.

---

### Stretch: Exercise 19: While Loop with Condition

**Goal**: Use a `while` loop to keep doubling a number until it exceeds 100.

```python
number = 1
```

✅ *Check*: Should print: 1, 2, 4, 8, 16, 32, 64.

---

### Stretch: Exercise 20: Create a List with Range

**Goal**: Use `range()` to create a list of even numbers from 0 to 20.

✅ *Check*: Should create [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20].


list[]


---
## Hands-On #3:
---

### Exercise 21: Build a List with Loop

**Goal**: Create a new list containing the squares of numbers 1 through 5.

✅ *Check*: Should create [1, 4, 9, 16, 25].

---

### Exercise 22: Count Vowels in String

**Goal**: Count how many vowels are in a string using a loop.

```python
text = "Hello World"
vowels = "aeiouAEIOU"
```

✅ *Check*: Should count and print the number of vowels.

---

### Exercise 23: Find Maximum in List

**Goal**: Find the largest number in a list using a `for` loop.

```python
numbers = [23, 67, 12, 89, 45, 34]
```

✅ *Check*: Should print "The maximum is 89".

---

### Exercise 24: Break Statement

**Goal**: Loop through a list and stop when you find the number 7.

```python
numbers = [2, 5, 7, 10, 15]
```

✅ *Check*: Should print 2, 5, then stop before printing 7.

---

### Exercise 25: Continue Statement

**Goal**: Print numbers 1 to 10 but skip multiples of 3 using `continue`.

✅ *Check*: Should skip 3, 6, 9 and print all other numbers.

---

### Exercise 26: Nested Loops - Multiplication Table

**Goal**: Use nested `for` loops to create a 3x3 multiplication table.

✅ *Check*: Should print products for 1×1 through 3×3.

---

### Exercise 27: While Loop with User Input Simulation

**Goal**: Use a `while` loop to add numbers to a list until the sum exceeds 50.

```python
numbers = [5, 10, 8, 15, 12, 7]
```

✅ *Check*: Should stop adding when sum > 50 and print the final list.

---

### Exercise 28: Find Index of Item

**Goal**: Loop through a list to find the index position of a specific item.

```python
fruits = ["apple", "banana", "cherry", "date"]
target = "cherry"
```

✅ *Check*: Should print "cherry is at index 2".

---

### Stretch: Exercise 29: Reverse a List Manually

**Goal**: Create a new list that is the reverse of the original using a loop.

```python
original = [10, 20, 30, 40, 50]
```

✅ *Check*: Should create [50, 40, 30, 20, 10] without using `reverse()` or slicing.

---

### Stretch: Exercise 30: Stop After Printing Asterisks

**Goal**: Use nested loops to print asterisks in rows, but stop completely after printing exactly 10 asterisks total.  The number of asterisks in row `n` should be `n`

Hint: You'll need to track the total count of asterisks printed and use `break` to exit both loops.

```python
num_asterisks = 11
...

*
**
***
****
*

```

✅ *Check*: Should print exactly 10 asterisks total before stopping (e.g., 1 star, then 2 stars, then 3 stars, then 4 stars = 10 total).

---
