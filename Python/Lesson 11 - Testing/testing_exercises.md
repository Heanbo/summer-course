# Unit Testing with pytest

This exercise set focuses on writing unit tests and achieving code coverage goals.

- [Unit Testing with pytest](#unit-testing-with-pytest)
  - [Hands-On #1: Unit Testing and Code Coverage](#hands-on-1-unit-testing-and-code-coverage)
    - [Exercise 1: Check Initial Coverage](#exercise-1-check-initial-coverage)
    - [Exercise 2: Test the `validate_isbn()` Function](#exercise-2-test-the-validate_isbn-function)
    - [Exercise 3: Test the `format_book_info()` Function](#exercise-3-test-the-format_book_info-function)
    - [Exercise 4: Test the `books_by_decade()` Function](#exercise-4-test-the-books_by_decade-function)
    - [Exercise 5: Reach 80% Code Coverage](#exercise-5-reach-80-code-coverage)
    - [Stretch (Optional) Test Edge Cases in Analytics](#stretch-optional-test-edge-cases-in-analytics)
  - [Hands-On #2: Integration Testing](#hands-on-2-integration-testing)
    - [Exercise 1: Library Workflow Integration](#exercise-1-library-workflow-integration)
    - [Exercise 2: Analytics Integration Test](#exercise-2-analytics-integration-test)
    - [Exercise 3: Search and Checkout Workflow](#exercise-3-search-and-checkout-workflow)
    - [Exercise 4: Complete Library Lifecycle](#exercise-4-complete-library-lifecycle)
    - [Stretch (Optional) Custom Fixture for Specialized Testing](#stretch-optional-custom-fixture-for-specialized-testing)


## Hands-On #1: Unit Testing and Code Coverage

Navigate to the `app/` directory and set up your environment:

```bash
cd app
pip install -r requirements.txt
```

You'll be working with a small library management system consisting of three modules:

- `book.py` - Book data model
- `library.py` - Library collection management
- `analytics.py` - Statistics and reporting

Run tests with coverage:

```powershell
# Windows PowerShell
$env:PYTHONPATH="." ; pytest
```

```bash
# Linux/Mac
PYTHONPATH=. pytest
```

---

### Exercise 1: Check Initial Coverage

**Goal**: Run the test suite and identify which functions have 0% test coverage.

1. Run pytest with coverage reporting
2. Open the HTML coverage report: `htmlcov/index.html`
3. Identify at least 5 functions with 0% coverage
4. List them in a comment at the top of your test file

✅ *Check*: All existing tests pass (23 tests), and you can see coverage percentages for each module.

**Hint**: Look for lines highlighted in red in the HTML report - those are not covered by tests.

---

### Exercise 2: Test the `validate_isbn()` Function

**Goal**: Add unit tests for the `validate_isbn()` function in `book.py`.

This function validates ISBN format (simplified - checks for 10 or 13 digits).

Add tests in `tests/test_book.py` that verify:

1. Valid 10-digit ISBN returns `True` (e.g., `"1234567890"`)
2. Valid 13-digit ISBN returns `True` (e.g., `"1234567890123"`)
3. ISBN with hyphens is valid (e.g., `"123-456-789-0"`)
4. ISBN with spaces is valid (e.g., `"123 456 789 0"`)
5. Invalid formats return `False`:
   - Too short: `"123"`
   - Too long: `"12345678901234"`
   - Contains letters: `"12345678AB"`
6. Non-string input returns `False` (e.g., `1234567890`)

✅ *Check*: All tests pass, and `validate_isbn()` shows 100% coverage in the report.

**Hint**: You can test multiple cases in one test function or create separate test functions for each case.

---

### Exercise 3: Test the `format_book_info()` Function

**Goal**: Add unit tests for the `format_book_info()` function in `book.py`.

This function formats book information for display, showing availability.

Add tests in `tests/test_book.py` that verify:

1. Formats a book with all copies available correctly
2. Formats a book with some copies checked out
3. Formats a book with no copies available (0/N available)
4. Output includes title, author, year, and availability

✅ *Check*: All tests pass, and `format_book_info()` shows 100% coverage in the report.

**Example output format**: `"Clean Code by Robert Martin (2008) - 2/2 available"`

---

### Exercise 4: Test the `books_by_decade()` Function

**Goal**: Add unit tests for the `books_by_decade()` function in `book.py`.

This function groups a list of books by their publication decade.

Add tests in `tests/test_book.py` that verify:

1. Books from different decades are grouped correctly
   - Create books from 1990s, 2000s, and 2010s
   - Verify they're grouped under keys 1990, 2000, 2010
2. Books from the same decade are in the same group
3. Empty list returns empty dictionary
4. Single book returns dictionary with one decade key

✅ *Check*: All tests pass, and `books_by_decade()` shows 100% coverage in the report.

**Hint**: The function returns a dictionary like `{1990: [book1, book2], 2000: [book3]}`

---

### Exercise 5: Reach 80% Code Coverage

**Goal**: Add enough tests to bring the total code coverage to at least 80%.

Check your current coverage, then add tests for untested functions:

**In `tests/test_library.py`, add tests for:**

1. `remove_book()` - Test successful removal and removal of non-existent book
2. `search_by_author()` - Test case-insensitive search and partial matching

**In `tests/test_analytics.py`, add tests for:**

3. `utilization_rate()` - Test with no checkouts (should return 0.0), with some checkouts, and with empty library
4. `author_statistics()` - Test counting books per author
5. `books_by_year()` - Test grouping books by publication year

**Steps:**

1. Run pytest to check current coverage percentage
2. Add tests for the functions above
3. Re-run pytest until coverage is at least 80%

✅ *Check*: Total code coverage is 80% or higher, and all tests pass.

**Hint**: You can use the fixtures defined in `tests/conftest.py`:
- `sample_books` - List of 5 pre-made books
- `empty_library` - Fresh library instance
- `populated_library` - Library with books already added
- `analytics` - Analytics object for the populated library

**Example using a fixture:**
```python
def test_utilization_rate(analytics):
    """Test utilization rate calculation."""
    rate = analytics.utilization_rate()
    assert rate >= 0.0 and rate <= 100.0
```

---

### Stretch (Optional) Test Edge Cases in Analytics

**Goal**: Add comprehensive tests for the remaining `LibraryAnalytics` methods.

Add tests in `tests/test_analytics.py` for:

1. `most_popular_books()` - Test with limit parameter, verify sorting
2. `average_books_per_author()` - Test with multiple authors, single author, empty library
3. `availability_report()` - Test dictionary structure and value ranges
4. `collection_summary()` - Test string formatting and content

For each test:
- Test normal cases
- Test edge cases (empty library, single item, maximum values)
- Verify return types and data structures

✅ *Check*: All `LibraryAnalytics` methods have 100% coverage, and all tests pass.

---

## Hands-On #2: Integration Testing

Integration tests verify that multiple components work together correctly. Unlike unit tests that test individual functions in isolation, integration tests ensure that different parts of your application interact properly.

You'll write tests in `tests/test_integration.py` that use multiple modules together.

**Key concepts:**
- Testing workflows that span multiple components
- Using fixtures to set up realistic test scenarios
- Verifying end-to-end functionality

**Available fixtures** (defined in `tests/conftest.py`):
- `sample_books` - List of 5 pre-made Book objects
- `empty_library` - Fresh Library instance
- `populated_library` - Library with sample books already added
- `library_with_checkouts` - Library with some books checked out
- `analytics` - LibraryAnalytics object for the populated library

---

### Exercise 1: Library Workflow Integration

**Goal**: Test a complete workflow: adding books → searching → checking out → returning.

Add a test in `tests/test_integration.py` that:

1. Creates an empty library
2. Adds several books (use `sample_books` fixture)
3. Searches for a book by title
4. Checks out the found book
5. Verifies the book's checkout count increased
6. Returns the book
7. Verifies the book's checkout count decreased

✅ *Check*: Test passes and verifies that Library and Book components work together correctly.

**Hint**: Use both `empty_library` and `sample_books` fixtures as parameters to your test function.

---

### Exercise 2: Analytics Integration Test

**Goal**: Test that analytics accurately reflect the library state after operations.

Add a test in `tests/test_integration.py` that:

1. Uses the `library_with_checkouts` fixture (has books with some checked out)
2. Creates a `LibraryAnalytics` object for this library
3. Calls `utilization_rate()` and verifies it's greater than 0
4. Calls `availability_report()` and verifies:
   - `total_titles` matches the library's book count
   - `available_titles` is less than or equal to `total_titles`
   - `availability_percentage` is between 0 and 100
5. Checks out another book
6. Verifies the utilization rate increased

✅ *Check*: Test passes and confirms analytics accurately track library operations.

---

### Exercise 3: Search and Checkout Workflow

**Goal**: Test searching by author, then checking out multiple books from that author.

Add a test in `tests/test_integration.py` that:

1. Uses the `populated_library` fixture
2. Searches for books by a specific author
3. Verifies at least one book was found
4. Checks out all books by that author
5. Verifies all checkouts were successful
6. Uses analytics to verify those books appear in `most_popular_books()`

✅ *Check*: Test passes and verifies search, checkout, and analytics work together.

**Hint**: Look at the books in `sample_books` (in `conftest.py`) to know which authors to search for.

---

### Exercise 4: Complete Library Lifecycle

**Goal**: Test a realistic end-to-end scenario without using fixtures (build everything from scratch).

Add a test in `tests/test_integration.py` that:

1. Creates a new Library
2. Creates and adds at least 3 Book objects with different authors and years
3. Checks out some books
4. Creates a LibraryAnalytics object
5. Generates a collection summary using `collection_summary()`
6. Verifies the summary string contains:
   - Library name
   - Correct total book count
   - Non-zero utilization rate
7. Tests `books_by_year()` returns correct groupings
8. Tests `author_statistics()` returns correct counts

✅ *Check*: Test passes without fixtures, demonstrating you understand the full system workflow.

**Hint**: This is the most comprehensive test - it shows you can work with all three modules together.

---

### Stretch (Optional) Custom Fixture for Specialized Testing

**Goal**: Create your own fixture and use it for testing specific scenarios.

In `tests/conftest.py`, add a new fixture:

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

Then in `tests/test_integration.py`, add tests using this fixture:

1. Test that `books_by_decade()` correctly groups these vintage books
2. Test analytics on a library of only old books
3. Test that all books are from decades before 2000

✅ *Check*: Custom fixture works, and tests using it pass.

**Learning**: This demonstrates fixture creation and reuse - a key skill for efficient testing.
