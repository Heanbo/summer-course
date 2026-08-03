# Unit Testing with pytest - Solutions

This file contains complete solutions for Hands-On #1.

- [Unit Testing with pytest - Solutions](#unit-testing-with-pytest---solutions)
  - [Exercise 1: Check Initial Coverage](#exercise-1-check-initial-coverage)
  - [Exercise 2: Test the `validate_isbn()` Function](#exercise-2-test-the-validate_isbn-function)
  - [Exercise 3: Test the `format_book_info()` Function](#exercise-3-test-the-format_book_info-function)
  - [Exercise 4: Test the `books_by_decade()` Function](#exercise-4-test-the-books_by_decade-function)
  - [Exercise 5: Reach 80% Code Coverage](#exercise-5-reach-80-code-coverage)
    - [Add to `tests/test_library.py`:](#add-to-teststest_librarypy)
    - [Add to `tests/test_analytics.py`:](#add-to-teststest_analyticspy)
  - [Expected Coverage After All Exercises](#expected-coverage-after-all-exercises)
  - [Stretch Solution](#stretch-solution)
    - [Complete Analytics Tests](#complete-analytics-tests)
  - [Hands-On #2: Integration Testing Solutions](#hands-on-2-integration-testing-solutions)
    - [Exercise 1: Library Workflow Integration](#exercise-1-library-workflow-integration)
    - [Exercise 2: Analytics Integration Test](#exercise-2-analytics-integration-test)
    - [Exercise 3: Search and Checkout Workflow](#exercise-3-search-and-checkout-workflow)
    - [Exercise 4: Complete Library Lifecycle](#exercise-4-complete-library-lifecycle)
  - [Stretch Solution: Custom Fixture](#stretch-solution-custom-fixture)
  - [Running All Tests](#running-all-tests)


## Exercise 1: Check Initial Coverage

Run pytest with coverage:
```powershell
$env:PYTHONPATH="." ; pytest
```

Functions with 0% coverage:
- `validate_isbn()` in book.py
- `format_book_info()` in book.py
- `books_by_decade()` in book.py
- `remove_book()` in library.py
- `search_by_author()` in library.py
- All methods in analytics.py

---

## Exercise 2: Test the `validate_isbn()` Function

Add to `tests/test_book.py`:

```python
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
```

---

## Exercise 3: Test the `format_book_info()` Function

Add to `tests/test_book.py`:

```python
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
```

---

## Exercise 4: Test the `books_by_decade()` Function

Add to `tests/test_book.py`:

```python
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
```

---

## Exercise 5: Reach 80% Code Coverage

### Add to `tests/test_library.py`:

```python
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
```

### Add to `tests/test_analytics.py`:

```python
"""
Unit tests for the Analytics module.
"""

import pytest
from book import Book
from library import Library
from analytics import LibraryAnalytics


class TestLibraryAnalytics:
    """Test cases for the LibraryAnalytics class."""
    
    def test_utilization_rate_no_checkouts(self):
        """Test utilization rate with no checkouts."""
        library = Library("Test Library")
        library.add_book(Book("123", "Book1", "Author", 2000, 5))
        analytics = LibraryAnalytics(library)
        
        rate = analytics.utilization_rate()
        assert rate == 0.0
    
    def test_utilization_rate_with_checkouts(self):
        """Test utilization rate with some checkouts."""
        library = Library("Test Library")
        book = Book("123", "Book1", "Author", 2000, 4)
        library.add_book(book)
        book.checkout()
        book.checkout()
        analytics = LibraryAnalytics(library)
        
        rate = analytics.utilization_rate()
        assert rate == 50.0
    
    def test_utilization_rate_empty_library(self):
        """Test utilization rate with empty library."""
        library = Library("Test Library")
        analytics = LibraryAnalytics(library)
        
        rate = analytics.utilization_rate()
        assert rate == 0.0
    
    def test_author_statistics(self):
        """Test counting books per author."""
        library = Library("Test Library")
        library.add_book(Book("123", "Book1", "Robert Martin", 2000))
        library.add_book(Book("456", "Book2", "Robert Martin", 2001))
        library.add_book(Book("789", "Book3", "Martin Fowler", 2002))
        analytics = LibraryAnalytics(library)
        
        stats = analytics.author_statistics()
        assert stats["Robert Martin"] == 2
        assert stats["Martin Fowler"] == 1
    
    def test_author_statistics_empty_library(self):
        """Test author statistics with empty library."""
        library = Library("Test Library")
        analytics = LibraryAnalytics(library)
        
        stats = analytics.author_statistics()
        assert stats == {}
    
    def test_books_by_year(self):
        """Test grouping books by publication year."""
        library = Library("Test Library")
        library.add_book(Book("123", "Book1", "Author", 2000))
        library.add_book(Book("456", "Book2", "Author", 2000))
        library.add_book(Book("789", "Book3", "Author", 2001))
        analytics = LibraryAnalytics(library)
        
        by_year = analytics.books_by_year()
        assert 2000 in by_year
        assert 2001 in by_year
        assert len(by_year[2000]) == 2
        assert len(by_year[2001]) == 1
    
    def test_books_by_year_empty_library(self):
        """Test books by year with empty library."""
        library = Library("Test Library")
        analytics = LibraryAnalytics(library)
        
        by_year = analytics.books_by_year()
        assert by_year == {}
```

---

## Expected Coverage After All Exercises

After completing all exercises, you should have approximately 80-85% code coverage:

```
Module           Coverage
─────────────────────────────────────
book.py          ~95%
library.py       ~95%
analytics.py     ~60%
─────────────────────────────────────
TOTAL            ~80%
```

Run the final coverage check:
```powershell
$env:PYTHONPATH="." ; pytest --cov=. --cov-report=term-missing
```

---

## Stretch Solution

### Complete Analytics Tests

Add to `tests/test_analytics.py`:

```python
def test_most_popular_books(library_with_checkouts):
    """Test getting most popular books."""
    analytics = LibraryAnalytics(library_with_checkouts)
    popular = analytics.most_popular_books(limit=3)
    
    # Should return list of tuples (Book, count)
    assert len(popular) <= 3
    assert isinstance(popular[0], tuple)
    assert isinstance(popular[0][0], Book)
    assert isinstance(popular[0][1], int)
    
    # Should be sorted by popularity
    if len(popular) > 1:
        assert popular[0][1] >= popular[1][1]

def test_most_popular_books_empty_library(empty_library):
    """Test most popular books with empty library."""
    analytics = LibraryAnalytics(empty_library)
    popular = analytics.most_popular_books()
    assert popular == []

def test_average_books_per_author(populated_library):
    """Test average books per author."""
    analytics = LibraryAnalytics(populated_library)
    avg = analytics.average_books_per_author()
    assert avg >= 1.0

def test_average_books_per_author_empty(empty_library):
    """Test average with empty library."""
    analytics = LibraryAnalytics(empty_library)
    avg = analytics.average_books_per_author()
    assert avg == 0.0

def test_availability_report(populated_library):
    """Test availability report structure."""
    analytics = LibraryAnalytics(populated_library)
    report = analytics.availability_report()
    
    # Check structure
    assert 'total_titles' in report
    assert 'available_titles' in report
    assert 'fully_checked_out' in report
    assert 'availability_percentage' in report
    
    # Check value ranges
    assert report['total_titles'] > 0
    assert report['available_titles'] >= 0
    assert report['fully_checked_out'] >= 0
    assert 0 <= report['availability_percentage'] <= 100

def test_collection_summary(populated_library):
    """Test collection summary formatting."""
    analytics = LibraryAnalytics(populated_library)
    summary = analytics.collection_summary()
    
    # Should be a string
    assert isinstance(summary, str)
    
    # Should contain key information
    assert "Collection Summary" in summary
    assert "Total Books:" in summary
    assert "Total Copies:" in summary
    assert "Utilization Rate:" in summary
```

---

## Hands-On #2: Integration Testing Solutions

### Exercise 1: Library Workflow Integration

Add to `tests/test_integration.py`:

```python
"""
Integration tests for the library management system.
These tests verify that multiple components work together correctly.
"""

import pytest
from book import Book
from library import Library
from analytics import LibraryAnalytics


def test_library_workflow_integration(empty_library, sample_books):
    """Test complete workflow: add books → search → checkout → return."""
    # Add books to library
    for book in sample_books:
        empty_library.add_book(book)
    
    assert empty_library.total_books() == 5
    
    # Search for a book
    results = empty_library.search_by_title("Python")
    assert len(results) > 0
    
    # Get the first result
    book = results[0]
    initial_checkout_count = book.checked_out
    
    # Check out the book
    success = empty_library.checkout_book(book.isbn)
    assert success is True
    assert book.checked_out == initial_checkout_count + 1
    
    # Return the book
    success = empty_library.return_book(book.isbn)
    assert success is True
    assert book.checked_out == initial_checkout_count
```

---

### Exercise 2: Analytics Integration Test

Add to `tests/test_integration.py`:

```python
def test_analytics_integration(library_with_checkouts):
    """Test that analytics accurately reflect library state."""
    # Create analytics for library with checkouts
    analytics = LibraryAnalytics(library_with_checkouts)
    
    # Check initial utilization rate
    initial_rate = analytics.utilization_rate()
    assert initial_rate > 0, "Should have some books checked out"
    
    # Check availability report
    report = analytics.availability_report()
    assert report['total_titles'] == library_with_checkouts.total_books()
    assert report['available_titles'] <= report['total_titles']
    assert 0 <= report['availability_percentage'] <= 100
    
    # Check out another book
    available = library_with_checkouts.available_books()
    if available:
        library_with_checkouts.checkout_book(available[0].isbn)
        
        # Verify utilization rate increased
        new_rate = analytics.utilization_rate()
        assert new_rate > initial_rate
```

---

### Exercise 3: Search and Checkout Workflow

Add to `tests/test_integration.py`:

```python
def test_search_and_checkout_workflow(populated_library):
    """Test searching by author and checking out their books."""
    # Search for books by an author (using one from sample_books)
    results = populated_library.search_by_author("David")
    assert len(results) > 0
    
    # Track which books we're checking out
    checked_out_isbns = []
    
    # Check out all books by this author
    for book in results:
        success = populated_library.checkout_book(book.isbn)
        assert success is True
        checked_out_isbns.append(book.isbn)
    
    # Verify all checkouts were successful
    for isbn in checked_out_isbns:
        book = populated_library.find_book(isbn)
        assert book.checked_out > 0
    
    # Use analytics to verify popularity
    analytics = LibraryAnalytics(populated_library)
    popular = analytics.most_popular_books(limit=5)
    
    # At least one of our checked-out books should be in the popular list
    popular_isbns = [book.isbn for book, count in popular if count > 0]
    assert any(isbn in popular_isbns for isbn in checked_out_isbns)
```

---

### Exercise 4: Complete Library Lifecycle

Add to `tests/test_integration.py`:

```python
def test_complete_library_lifecycle():
    """Test realistic end-to-end scenario without fixtures."""
    # Create a new library
    library = Library("Community Library")
    
    # Create and add books
    books = [
        Book("111", "Python Crash Course", "Eric Matthes", 2019, 3),
        Book("222", "Clean Code", "Robert Martin", 2008, 2),
        Book("333", "The Pragmatic Programmer", "David Thomas", 1999, 2),
    ]
    
    for book in books:
        library.add_book(book)
    
    assert library.total_books() == 3
    
    # Check out some books
    library.checkout_book("111")
    library.checkout_book("222")
    library.checkout_book("222")  # Check out second copy
    
    # Create analytics
    analytics = LibraryAnalytics(library)
    
    # Test collection summary
    summary = analytics.collection_summary()
    assert isinstance(summary, str)
    assert "Community Library" in summary
    assert "Total Books: 3" in summary
    assert library.total_copies() > 0
    
    # Verify utilization rate is non-zero
    rate = analytics.utilization_rate()
    assert rate > 0
    
    # Test books_by_year
    by_year = analytics.books_by_year()
    assert 2019 in by_year
    assert 2008 in by_year
    assert 1999 in by_year
    assert len(by_year[2019]) == 1
    assert len(by_year[2008]) == 1
    assert len(by_year[1999]) == 1
    
    # Test author statistics
    author_stats = analytics.author_statistics()
    assert author_stats["Eric Matthes"] == 1
    assert author_stats["Robert Martin"] == 1
    assert author_stats["David Thomas"] == 1
    assert len(author_stats) == 3
```

---

## Stretch Solution: Custom Fixture

Add to `tests/conftest.py`:

```python
@pytest.fixture
def library_with_vintage_books():
    """Create a library with old books (pre-2000)."""
    library = Library("Vintage Library")
    library.add_book(Book("123", "Classic Book 1", "Old Author", 1980, 2))
    library.add_book(Book("456", "Classic Book 2", "Old Author", 1985, 1))
    library.add_book(Book("789", "Classic Book 3", "Another Author", 1990, 3))
    return library
```

Add to `tests/test_integration.py`:

```python
from book import books_by_decade


def test_vintage_books_by_decade(library_with_vintage_books):
    """Test books_by_decade with vintage books."""
    books = list(library_with_vintage_books.books.values())
    by_decade = books_by_decade(books)
    
    assert 1980 in by_decade
    assert 1990 in by_decade
    assert len(by_decade[1980]) == 2  # Two books from 1980s
    assert len(by_decade[1990]) == 1  # One book from 1990s


def test_vintage_library_analytics(library_with_vintage_books):
    """Test analytics on vintage books."""
    analytics = LibraryAnalytics(library_with_vintage_books)
    
    # Test utilization rate with no checkouts
    rate = analytics.utilization_rate()
    assert rate == 0.0
    
    # Test author statistics
    author_stats = analytics.author_statistics()
    assert author_stats["Old Author"] == 2
    assert author_stats["Another Author"] == 1


def test_all_books_pre_2000(library_with_vintage_books):
    """Test that all books are from before 2000."""
    for book in library_with_vintage_books.books.values():
        assert book.year < 2000, f"Book {book.title} is not vintage"
```

---

## Running All Tests

After completing both Hands-On #1 and #2, you should have approximately 40-50 tests.

Run all tests:
```powershell
$env:PYTHONPATH="." ; pytest -v
```

Check final coverage:
```powershell
$env:PYTHONPATH="." ; pytest --cov=. --cov-report=term-missing --cov-report=html
```

Expected results:
- All tests pass
- Coverage >= 80%
- Integration tests demonstrate multi-component workflows
