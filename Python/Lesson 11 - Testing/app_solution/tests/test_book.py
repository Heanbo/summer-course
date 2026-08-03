"""
Unit tests for the Book module - COMPLETE SOLUTION.
"""

import pytest
from book import Book, validate_isbn, format_book_info, books_by_decade


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


# Exercise 2 Solutions: validate_isbn tests
def test_validate_isbn_valid_10_digit():
    """Test that valid 10-digit ISBN returns True."""
    assert validate_isbn("1234567890") is True


def test_validate_isbn_valid_13_digit():
    """Test that valid 13-digit ISBN returns True."""
    assert validate_isbn("1234567890123") is True


def test_validate_isbn_with_hyphens():
    """Test that ISBN with hyphens is valid."""
    assert validate_isbn("123-456-789-0") is True


def test_validate_isbn_with_spaces():
    """Test that ISBN with spaces is valid."""
    assert validate_isbn("123 456 789 0") is True


def test_validate_isbn_too_short():
    """Test that too-short ISBN returns False."""
    assert validate_isbn("123") is False


def test_validate_isbn_too_long():
    """Test that too-long ISBN returns False."""
    assert validate_isbn("12345678901234") is False


def test_validate_isbn_with_letters():
    """Test that ISBN with letters returns False."""
    assert validate_isbn("12345678AB") is False


def test_validate_isbn_non_string():
    """Test that non-string input returns False."""
    assert validate_isbn(1234567890) is False


# Exercise 3 Solutions: format_book_info tests
def test_format_book_info_all_available():
    """Test formatting book with all copies available."""
    book = Book("123", "Clean Code", "Robert Martin", 2008, 3)
    result = format_book_info(book)
    assert "Clean Code" in result
    assert "Robert Martin" in result
    assert "2008" in result
    assert "3/3 available" in result


def test_format_book_info_some_checked_out():
    """Test formatting book with some copies checked out."""
    book = Book("123", "Test Book", "Author", 2020, 5)
    book.checkout()
    book.checkout()
    result = format_book_info(book)
    assert "3/5 available" in result


def test_format_book_info_none_available():
    """Test formatting book with no copies available."""
    book = Book("123", "Test Book", "Author", 2020, 2)
    book.checkout()
    book.checkout()
    result = format_book_info(book)
    assert "0/2 available" in result


# Exercise 4 Solutions: books_by_decade tests
def test_books_by_decade_multiple_decades():
    """Test grouping books from different decades."""
    books = [
        Book("1", "Book1", "Author", 1995),
        Book("2", "Book2", "Author", 2005),
        Book("3", "Book3", "Author", 2015),
    ]
    result = books_by_decade(books)
    assert 1990 in result
    assert 2000 in result
    assert 2010 in result
    assert len(result[1990]) == 1
    assert len(result[2000]) == 1
    assert len(result[2010]) == 1


def test_books_by_decade_same_decade():
    """Test grouping books from the same decade."""
    books = [
        Book("1", "Book1", "Author", 2001),
        Book("2", "Book2", "Author", 2005),
        Book("3", "Book3", "Author", 2009),
    ]
    result = books_by_decade(books)
    assert 2000 in result
    assert len(result[2000]) == 3


def test_books_by_decade_empty_list():
    """Test with empty list."""
    result = books_by_decade([])
    assert result == {}


def test_books_by_decade_single_book():
    """Test with single book."""
    books = [Book("1", "Book1", "Author", 1995)]
    result = books_by_decade(books)
    assert 1990 in result
    assert len(result[1990]) == 1
    assert result[1990][0].title == "Book1"
