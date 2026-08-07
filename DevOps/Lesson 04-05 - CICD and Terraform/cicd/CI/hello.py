"""
hello.py — A simple greeting program 👋

This file shows a basic Python function that CI will test automatically.
Every time you push code, GitHub Actions runs the tests in test_hello.py
to make sure this function still works correctly!
"""


def greet(name):
    """Return a friendly greeting for the given name."""
    if not name:
        raise ValueError("Name cannot be empty!")
    return f"Hello, {name}! Welcome to CI/CD! 🚀"


def add(a, b):
    """Add two numbers together.

    This is a super simple function — but even simple functions
    need tests so we know they always work correctly!
    """
    return a + b


if __name__ == "__main__":
    # This runs when you execute: python hello.py
    print(greet("World"))
    print(f"2 + 3 = {add(2, 3)}")
