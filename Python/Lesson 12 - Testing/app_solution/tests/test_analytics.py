"""
Unit tests for the Analytics module - COMPLETE SOLUTION.
"""

import pytest
from book import Book
from library import Library
from analytics import LibraryAnalytics


class TestLibraryAnalytics:
    """Test cases for the LibraryAnalytics class."""

    # Exercise 5 Solutions: Basic analytics tests
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

    # Stretch Solutions: Complete analytics tests
    def test_most_popular_books(self, library_with_checkouts):
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

    def test_most_popular_books_empty_library(self, empty_library):
        """Test most popular books with empty library."""
        analytics = LibraryAnalytics(empty_library)
        popular = analytics.most_popular_books()
        assert popular == []

    def test_average_books_per_author(self, populated_library):
        """Test average books per author."""
        analytics = LibraryAnalytics(populated_library)
        avg = analytics.average_books_per_author()
        assert avg >= 1.0

    def test_average_books_per_author_empty(self, empty_library):
        """Test average with empty library."""
        analytics = LibraryAnalytics(empty_library)
        avg = analytics.average_books_per_author()
        assert avg == 0.0

    def test_availability_report(self, populated_library):
        """Test availability report structure."""
        analytics = LibraryAnalytics(populated_library)
        report = analytics.availability_report()

        # Check structure
        assert "total_titles" in report
        assert "available_titles" in report
        assert "fully_checked_out" in report
        assert "availability_percentage" in report

        # Check value ranges
        assert report["total_titles"] > 0
        assert report["available_titles"] >= 0
        assert report["fully_checked_out"] >= 0
        assert 0 <= report["availability_percentage"] <= 100

    def test_collection_summary(self, populated_library):
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
