# Testing Quick Reference Guide

This guide provides common testing patterns you'll use in the exercises.

## Running Tests

```bash
# Run all tests with coverage
$env:PYTHONPATH="." ; pytest

# Run specific test file
$env:PYTHONPATH="." ; pytest tests/test_book.py

# Run specific test function
$env:PYTHONPATH="." ; pytest tests/test_book.py::TestBook::test_book_creation

# View coverage report in terminal
$env:PYTHONPATH="." ; pytest --cov=. --cov-report=term-missing

# Generate HTML coverage report
$env:PYTHONPATH="." ; pytest
# Then open htmlcov/index.html
```

## Basic Test Structure

```python
def test_function_name():
    """Test description."""
    # Arrange - Set up test data
    book = Book("123", "Title", "Author", 2000)
    
    # Act - Execute the function being tested
    result = book.checkout()
    
    # Assert - Verify the result
    assert result is True
    assert book.checked_out == 1
```

## Common Assertion Patterns

```python
# Equality
assert value == expected
assert result is True
assert result is False
assert result is None

# Comparisons
assert len(results) == 3
assert count > 0
assert rate >= 0.0 and rate <= 100.0

# Membership
assert "Python" in book.title
assert book in results

# Type checking
assert isinstance(result, Book)
```

## Testing Exceptions

```python
import pytest

def test_invalid_input_raises_error():
    """Test that invalid input raises ValueError."""
    with pytest.raises(ValueError):
        Book("", "Title", "Author", 2000)

# Match specific error message
def test_error_message():
    """Test specific error message."""
    with pytest.raises(ValueError, match="ISBN must be a non-empty string"):
        Book("", "Title", "Author", 2000)
```

## Testing Class Methods

```python
class TestBook:
    """Group related tests in a class."""
    
    def test_method_one(self):
        """Test description."""
        book = Book("123", "Title", "Author", 2000)
        assert book.is_available() is True
    
    def test_method_two(self):
        """Test description."""
        book = Book("123", "Title", "Author", 2000, 2)
        book.checkout()
        assert book.available_copies() == 1
```

## Testing Functions with Multiple Cases

```python
def test_validate_isbn_valid_formats():
    """Test validate_isbn with valid ISBN formats."""
    # Test 10-digit ISBN
    assert validate_isbn("1234567890") is True
    
    # Test 13-digit ISBN
    assert validate_isbn("1234567890123") is True
    
    # Test with hyphens
    assert validate_isbn("123-456-789-0") is True

def test_validate_isbn_invalid_formats():
    """Test validate_isbn with invalid formats."""
    # Test too short
    assert validate_isbn("123") is False
    
    # Test with letters
    assert validate_isbn("12345678AB") is False
    
    # Test non-string
    assert validate_isbn(1234567890) is False
```

## Using Fixtures

Fixtures are defined in `tests/conftest.py` and can be used in any test:

```python
def test_with_empty_library(empty_library):
    """Test using the empty_library fixture."""
    assert empty_library.total_books() == 0

def test_with_populated_library(populated_library):
    """Test using the populated_library fixture."""
    # Library already has sample books
    assert populated_library.total_books() == 5

def test_with_sample_books(sample_books):
    """Test using the sample_books fixture."""
    # List of Book objects
    assert len(sample_books) == 5
    assert all(isinstance(book, Book) for book in sample_books)
```

## Integration Test Pattern

```python
def test_complete_workflow(empty_library, sample_books):
    """Integration test for complete library workflow."""
    # Add books to library
    for book in sample_books:
        empty_library.add_book(book)
    
    # Search for books
    results = empty_library.search_by_title("Python")
    assert len(results) > 0
    
    # Check out a book
    isbn = results[0].isbn
    success = empty_library.checkout_book(isbn)
    assert success is True
    
    # Verify analytics
    analytics = LibraryAnalytics(empty_library)
    rate = analytics.utilization_rate()
    assert rate > 0
```

## Testing Return Values

```python
def test_function_returns_correct_type():
    """Test that function returns expected type."""
    library = Library("Test")
    books = library.available_books()
    assert isinstance(books, list)

def test_function_returns_correct_value():
    """Test that function returns expected value."""
    book = Book("123", "Title", "Author", 2000, 5)
    book.checkout()
    book.checkout()
    assert book.available_copies() == 3
```

## Testing with Empty/Edge Cases

```python
def test_empty_library():
    """Test analytics with empty library."""
    library = Library("Empty")
    analytics = LibraryAnalytics(library)
    rate = analytics.utilization_rate()
    assert rate == 0.0

def test_books_by_decade_empty_list():
    """Test with empty list."""
    result = books_by_decade([])
    assert result == {}
```

## Checking Multiple Conditions

```python
def test_availability_report(library_with_checkouts):
    """Test the availability report structure and values."""
    analytics = LibraryAnalytics(library_with_checkouts)
    report = analytics.availability_report()
    
    # Check all expected keys exist
    assert 'total_titles' in report
    assert 'available_titles' in report
    assert 'fully_checked_out' in report
    assert 'availability_percentage' in report
    
    # Check values are reasonable
    assert report['total_titles'] > 0
    assert report['available_titles'] >= 0
    assert report['availability_percentage'] >= 0
    assert report['availability_percentage'] <= 100
```

## Tips

1. **One concept per test** - Test one thing at a time
2. **Descriptive names** - Test name should describe what it's testing
3. **Arrange-Act-Assert** - Follow this structure for clarity
4. **Test edge cases** - Empty inputs, zero values, boundary conditions
5. **Test error cases** - Invalid inputs should raise appropriate exceptions
6. **Use fixtures** - Reuse setup code across tests
7. **Keep tests independent** - Tests should not depend on each other
