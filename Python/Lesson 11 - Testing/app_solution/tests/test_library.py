"""
Unit tests for the Library module - COMPLETE SOLUTION.
"""

import pytest
from book import Book
from library import Library


class TestLibrary:
    """Test cases for the Library class."""

    def test_library_creation(self):
        """Test creating a library."""
        library = Library("City Library")
        assert library.name == "City Library"
        assert library.total_books() == 0

    def test_invalid_library_name(self):
        """Test that invalid name raises ValueError."""
        with pytest.raises(ValueError, match="Library name must be a non-empty string"):
            Library("")

    def test_add_book(self):
        """Test adding a book to library."""
        library = Library("City Library")
        book = Book("123", "Title", "Author", 2000)
        result = library.add_book(book)
        assert result is True
        assert library.total_books() == 1

    def test_add_duplicate_book(self):
        """Test adding duplicate book returns False."""
        library = Library("City Library")
        book = Book("123", "Title", "Author", 2000)
        library.add_book(book)
        result = library.add_book(book)
        assert result is False
        assert library.total_books() == 1

    def test_add_invalid_type(self):
        """Test adding non-Book object raises TypeError."""
        library = Library("City Library")
        with pytest.raises(TypeError, match="Must provide a Book object"):
            library.add_book("not a book")

    def test_find_book(self):
        """Test finding a book by ISBN."""
        library = Library("City Library")
        book = Book("123", "Title", "Author", 2000)
        library.add_book(book)
        found = library.find_book("123")
        assert found is book

    def test_find_nonexistent_book(self):
        """Test finding book that doesn't exist."""
        library = Library("City Library")
        found = library.find_book("999")
        assert found is None

    def test_search_by_title(self):
        """Test searching books by title."""
        library = Library("City Library")
        library.add_book(Book("123", "Python Programming", "Author", 2000))
        library.add_book(Book("456", "Java Programming", "Author", 2000))
        library.add_book(Book("789", "The Python Cookbook", "Author", 2000))

        results = library.search_by_title("Python")
        assert len(results) == 2
        assert all("Python" in book.title for book in results)

    def test_total_copies(self):
        """Test calculating total copies."""
        library = Library("City Library")
        library.add_book(Book("123", "Title1", "Author", 2000, 3))
        library.add_book(Book("456", "Title2", "Author", 2000, 2))
        assert library.total_copies() == 5

    def test_available_books(self):
        """Test getting available books."""
        library = Library("City Library")
        book1 = Book("123", "Title1", "Author", 2000, 1)
        book2 = Book("456", "Title2", "Author", 2000, 2)
        library.add_book(book1)
        library.add_book(book2)

        book1.checkout()  # Make book1 unavailable

        available = library.available_books()
        assert len(available) == 1
        assert available[0] is book2

    def test_checkout_book(self):
        """Test checking out a book through library."""
        library = Library("City Library")
        book = Book("123", "Title", "Author", 2000, 1)
        library.add_book(book)

        result = library.checkout_book("123")
        assert result is True
        assert book.checked_out == 1

    def test_return_book(self):
        """Test returning a book through library."""
        library = Library("City Library")
        book = Book("123", "Title", "Author", 2000, 1)
        library.add_book(book)
        book.checkout()

        result = library.return_book("123")
        assert result is True
        assert book.checked_out == 0


# Exercise 5 Solutions: remove_book and search_by_author tests
def test_remove_book_success():
    """Test successfully removing a book."""
    library = Library("Test Library")
    book = Book("123", "Title", "Author", 2000)
    library.add_book(book)

    result = library.remove_book("123")
    assert result is True
    assert library.total_books() == 0


def test_remove_book_not_found():
    """Test removing non-existent book returns False."""
    library = Library("Test Library")
    result = library.remove_book("999")
    assert result is False


def test_search_by_author_case_insensitive():
    """Test searching by author is case-insensitive."""
    library = Library("Test Library")
    library.add_book(Book("123", "Book1", "Martin Fowler", 2000))
    library.add_book(Book("456", "Book2", "Robert Martin", 2000))

    results = library.search_by_author("martin")
    assert len(results) == 2


def test_search_by_author_partial_match():
    """Test searching by author with partial match."""
    library = Library("Test Library")
    library.add_book(Book("123", "Book1", "Robert C. Martin", 2000))
    library.add_book(Book("456", "Book2", "Martin Fowler", 2000))

    results = library.search_by_author("Robert")
    assert len(results) == 1
    assert results[0].author == "Robert C. Martin"


def test_search_by_author_no_matches():
    """Test searching when no matches found."""
    library = Library("Test Library")
    library.add_book(Book("123", "Book1", "Author", 2000))

    results = library.search_by_author("Nobody")
    assert len(results) == 0
