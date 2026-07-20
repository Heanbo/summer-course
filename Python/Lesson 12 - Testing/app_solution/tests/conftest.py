"""
Pytest fixtures for integration tests.
These fixtures can be reused across multiple test files.
"""

import pytest
from book import Book
from library import Library
from analytics import LibraryAnalytics


@pytest.fixture
def sample_books():
    """Create a list of sample books for testing."""
    return [
        Book("978-0-13-468599-1", "The Pragmatic Programmer", "David Thomas", 2019, 3),
        Book("978-0-13-235088-4", "Clean Code", "Robert Martin", 2008, 2),
        Book("978-0-596-52068-7", "JavaScript: The Good Parts", "Douglas Crockford", 2008, 2),
        Book("978-0-13-468599-2", "Design Patterns", "Gang of Four", 1994, 1),
        Book("978-0-201-61622-4", "The Python Cookbook", "David Beazley", 2013, 4),
    ]


@pytest.fixture
def empty_library():
    """Create an empty library for testing."""
    return Library("Test Library")


@pytest.fixture
def populated_library(sample_books):
    """Create a library with sample books already added."""
    library = Library("City Public Library")
    for book in sample_books:
        library.add_book(book)
    return library


@pytest.fixture
def library_with_checkouts(populated_library):
    """Create a library with some books checked out."""
    # Checkout some books
    populated_library.checkout_book("978-0-13-468599-1")  # Pragmatic Programmer
    populated_library.checkout_book("978-0-13-468599-1")  # Pragmatic Programmer (2nd copy)
    populated_library.checkout_book("978-0-596-52068-7")  # JavaScript book
    return populated_library


@pytest.fixture
def analytics(populated_library):
    """Create an analytics object for a populated library."""
    return LibraryAnalytics(populated_library)


@pytest.fixture
def library_with_vintage_books():
    """Create a library with old books (pre-2000)."""
    library = Library("Vintage Library")
    library.add_book(Book("123", "Classic Book 1", "Old Author", 1980, 2))
    library.add_book(Book("456", "Classic Book 2", "Old Author", 1985, 1))
    library.add_book(Book("789", "Classic Book 3", "Another Author", 1990, 3))
    return library
