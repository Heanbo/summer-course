"""
Integration tests for the library management system - COMPLETE SOLUTION.
These tests verify that multiple components work together correctly.
"""

import pytest
from book import Book, books_by_decade
from library import Library
from analytics import LibraryAnalytics


# Exercise 1 Solution: Library Workflow Integration
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


# Exercise 2 Solution: Analytics Integration Test
def test_analytics_integration(library_with_checkouts):
    """Test that analytics accurately reflect library state."""
    # Create analytics for library with checkouts
    analytics = LibraryAnalytics(library_with_checkouts)

    # Check initial utilization rate
    initial_rate = analytics.utilization_rate()
    assert initial_rate > 0, "Should have some books checked out"

    # Check availability report
    report = analytics.availability_report()
    assert report["total_titles"] == library_with_checkouts.total_books()
    assert report["available_titles"] <= report["total_titles"]
    assert 0 <= report["availability_percentage"] <= 100

    # Check out another book
    available = library_with_checkouts.available_books()
    if available:
        library_with_checkouts.checkout_book(available[0].isbn)

        # Verify utilization rate increased
        new_rate = analytics.utilization_rate()
        assert new_rate > initial_rate


# Exercise 3 Solution: Search and Checkout Workflow
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


# Exercise 4 Solution: Complete Library Lifecycle
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


# Stretch Solution: Custom Fixture Tests
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
