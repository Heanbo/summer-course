"""
Unit tests for the Book module.
Note: This file has incomplete coverage - some functions need tests!
"""

import pytest
from book import Book, validate_isbn


class TestBook:
    """Test cases for the Book class."""

    def test_book_creation(self):
        """Test creating a valid book."""
        book = Book("978-0-123456-78-9", "Test Book", "John Doe", 2020, 3)
        assert book.isbn == "978-0-123456-78-9"
        assert book.title == "Test Book"
        assert book.author == "John Doe"
        assert book.year == 2020
        assert book.copies == 3
        assert book.checked_out == 0

    def test_book_default_copies(self):
        """Test that default copies is 1."""
        book = Book("123", "Title", "Author", 2000)
        assert book.copies == 1

    def test_invalid_isbn_raises_error(self):
        """Test that invalid ISBN raises ValueError."""
        with pytest.raises(ValueError, match="ISBN must be a non-empty string"):
            Book("", "Title", "Author", 2000)

    def test_invalid_title_raises_error(self):
        """Test that invalid title raises ValueError."""
        with pytest.raises(ValueError, match="Title must be a non-empty string"):
            Book("123", "", "Author", 2000)

    def test_invalid_year_raises_error(self):
        """Test that invalid year raises ValueError."""
        with pytest.raises(ValueError, match="Year must be between 1000 and 2100"):
            Book("123", "Title", "Author", 999)

    def test_is_available_with_copies(self):
        """Test is_available returns True when copies available."""
        book = Book("123", "Title", "Author", 2000, 2)
        assert book.is_available() is True

    def test_checkout_success(self):
        """Test successful checkout."""
        book = Book("123", "Title", "Author", 2000, 2)
        result = book.checkout()
        assert result is True
        assert book.checked_out == 1

    def test_checkout_last_copy(self):
        """Test checking out the last available copy."""
        book = Book("123", "Title", "Author", 2000, 1)
        book.checkout()
        assert book.is_available() is False

    def test_checkout_when_none_available(self):
        """Test checkout fails when no copies available."""
        book = Book("123", "Title", "Author", 2000, 1)
        book.checkout()
        result = book.checkout()
        assert result is False
        assert book.checked_out == 1

    def test_return_book_success(self):
        """Test successful book return."""
        book = Book("123", "Title", "Author", 2000, 1)
        book.checkout()
        result = book.return_book()
        assert result is True
        assert book.checked_out == 0

    def test_available_copies(self):
        """Test available_copies calculation."""
        book = Book("123", "Title", "Author", 2000, 5)
        assert book.available_copies() == 5
        book.checkout()
        book.checkout()
        assert book.available_copies() == 3


# Note: The following functions have NO tests yet (0% coverage):
# - validate_isbn()
# - format_book_info()
# - books_by_decade()
