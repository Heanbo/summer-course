# Recursion

This repository explains the concept of **Recursion**, a fundamental programming technique where an algorithm is defined in terms of itself to solve complex problems by breaking them down into smaller sub-problems. 


## 🎯 Lesson Objectives

* Understand the definition and core requirements of **recursion**. 
* Identify the difference between a **base case** and a **recursive step**. 
* Analyze the **order of execution** and how the system stack manages recursive calls. 


## 🔄 What is Recursion?

A common joke to define the concept is: "To understand recursion, you must understand recursion." In technical terms, it is an algorithm that uses itself in its own definition. 


### The Two Essential Requirements

For a recursive function to work correctly and avoid infinite loops, it must have: 

1. **Base Case:** The "terminating step" that stops the recursion. 
2. **Recursive Step:** The part of the function that calls itself with a smaller input, gradually moving toward the base case. 


## 💻 Code Examples

### 1. Factorial

A classic example where . 

- **Base Case:** If  is 0 or 1, return 1. 
- **Recursive Step:** Return  multiplied by `factorial(n - 1)`. 

```python
def factorial(n: int):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n - 1)

```


### 2. Multiple Recursion (Fibonacci)

Multiple recursion occurs when a function calls itself more than once in a single step. 

- **Base Cases:** If  is 0, return 0; if  is 1, return 1. 
- **Recursive Step:** Return the sum of the two previous Fibonacci numbers. 

```python
def fib(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return fib(n-1) + fib(n-2)

```


## 🧠 Execution and the Stack

Recursive calls are managed by the **system stack**. Each time a function calls itself, a new "frame" is pushed onto the stack. Once the base case is reached, the functions begin returning values, and the stack "unwinds." 


### Warning: Stack Overflow

If you forget a **base case** or the input does not get smaller, the function will call itself infinitely until the system runs out of memory, resulting in a **Stack Overflow**. 


## 🔍 Common Applications

Recursion is highly efficient for: 

- **Binary Search:** Assumes a sorted array and repeatedly halves the search area. 
- **Tree Traversals:** Navigating hierarchical data structures. 
- **Mathematical sequences:** Such as Factorials and Fibonacci numbers. 
