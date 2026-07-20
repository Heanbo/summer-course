# Python Classes (Object-Oriented Programming)

This repository explores the principles of **Object-Oriented Programming (OOP)** in Python, focusing on how to use classes to encapsulate data and behavior into reusable objects.


## 🎯 Lesson Objectives

* Implement **classes** in Python to encapsulate functionality.
* Discuss the use of classes and their **interactions** within a program.
* Master core OOP concepts like **encapsulation, polymorphism, and magic methods**.


## 🏗️ Object-Oriented Programming (OOP)

OOP is a paradigm based on modeling software after real-world objects that have attributes and can perform actions.


### Core Concepts

- **Encapsulation:** Hiding internal complexity behind a simple public interface.
- **Class:** A "blueprint" or template used to construct objects.
- **Object (Instance):** A specific instantiation of a class.
- **Attributes:** Data or properties stored within a class (what an object *is*).
- **Methods:** Functions defined within a class that describe what it can do (what an object *does*).


## 🐍 Writing Python Classes

### The `self` Keyword

In Python, the `self` keyword refers to the specific instance of the object being manipulated. It allows attributes and methods to access the data belonging to that specific instance.

### The Constructor (`__init__`)

The `__init__` method is a special function called automatically when a new object is created. It is primarily used to set initial attributes.

```python
class Spacecraft:
    def __init__(self, name, fuel):
        self.name = name  # Instance attribute
        self.fuel = fuel  # Instance attribute

```


## ✨ Magic Methods and Overloading

Python includes "magic methods" (identified by double underscores, e.g., `__init__`) that allow you to define how objects behave with standard Python operations.

| Category | Magic Method | Purpose |
| --- | --- | --- |
| **Lifecycle** | `__init__` | The constructor used for initialization.
| **Representation** | `__str__` | Defines what is shown when the object is printed.
| **Comparison** | `__eq__`, `__lt__` | Allows the use of `==`, `<`, etc., between objects.
| **Arithmetic** | `__add__`, `__sub__` | Allows the use of `+` and `-` with objects.
| **Container** | `__len__` | Allows the use of `len()` on the object.


## 🛠️ Advanced Principles

- **Polymorphism:** The ability of a single interface to support multiple underlying forms (data types).
- **Convention:** Attributes or methods starting with an underscore (e.g., `_variable`) are intended for internal use and should not be accessed directly from outside the class.
- **Inspection:** Use the `dir()` function to see all available methods and attributes of an object.
