"""
test_hello.py — Tests for our hello.py program 🧪

These tests are run automatically by GitHub Actions every time
you push code. They check that our functions still work correctly!

Think of tests like a checklist:
  ✅ Does greet("Alice") return the right message?
  ✅ Does add(2, 3) equal 5?
  ✅ Does greet("") raise an error?

If all checks pass, CI shows a green checkmark. 
If something breaks, CI shows a red X and tells you what went wrong!
"""

import pytest
from hello import add, greet


# ---------- Tests for greet() ----------

def test_greet_returns_message():
    """Check that greet() returns a message containing the name."""
    result = greet("Alice")
    assert "Alice" in result, "The greeting should include the person's name!"


def test_greet_starts_with_hello():
    """Check that greet() starts with 'Hello'."""
    result = greet("Bob")
    assert result.startswith("Hello"), "The greeting should start with 'Hello'!"


def test_greet_different_names():
    """Check that greet() works for different names."""
    assert "Charlie" in greet("Charlie")
    assert "Dave" in greet("Dave")


def test_greet_empty_name_raises_error():
    """Check that greet() raises an error when name is empty.

    Sometimes we WANT our code to raise an error — and we can test for that too!
    """
    with pytest.raises(ValueError):
        greet("")


# ---------- Tests for add() ----------

def test_add_two_positive_numbers():
    """Check that add() correctly adds two positive numbers."""
    assert add(2, 3) == 5, "2 + 3 should equal 5!"


def test_add_with_zero():
    """Check that add() works when one number is zero."""
    assert add(0, 7) == 7, "0 + 7 should equal 7!"
    assert add(5, 0) == 5, "5 + 0 should equal 5!"


def test_add_negative_numbers():
    """Check that add() works with negative numbers."""
    assert add(-1, -2) == -3, "-1 + -2 should equal -3!"


def test_add_returns_correct_type():
    """Check that add() returns a number."""
    result = add(1, 2)
    assert isinstance(result, (int, float)), "add() should return a number!"
