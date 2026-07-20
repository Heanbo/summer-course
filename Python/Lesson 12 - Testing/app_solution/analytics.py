"""
Analytics module for library statistics and reporting.
"""

from collections import Counter


class LibraryAnalytics:
    """Provides analytics and reporting for library data."""

    def __init__(self, library):
        """
        Initialize analytics for a library.

        Args:
            library (Library): Library object to analyze
        """
        self.library = library

    def utilization_rate(self):
        """
        Calculate what percentage of books are currently checked out.

        Returns:
            float: Percentage (0-100) of books checked out
        """
        total = self.library.total_copies()
        if total == 0:
            return 0.0

        checked_out = sum(book.checked_out for book in self.library.books.values())
        return (checked_out / total) * 100

    def most_popular_books(self, limit=5):
        """
        Get the most checked-out books.

        Args:
            limit (int): Maximum number of books to return

        Returns:
            list: List of tuples (Book, checkout_count) sorted by popularity
        """
        book_popularity = [(book, book.checked_out) for book in self.library.books.values()]
        book_popularity.sort(key=lambda x: x[1], reverse=True)
        return book_popularity[:limit]

    def books_by_year(self):
        """
        Group books by publication year.

        Returns:
            dict: Dictionary with year as key and list of books as value
        """
        years = {}
        for book in self.library.books.values():
            if book.year not in years:
                years[book.year] = []
            years[book.year].append(book)
        return years

    def author_statistics(self):
        """
        Calculate statistics by author.

        Returns:
            dict: Dictionary with author names as keys and book count as values
        """
        author_counts = Counter()
        for book in self.library.books.values():
            author_counts[book.author] += 1
        return dict(author_counts)

    def average_books_per_author(self):
        """
        Calculate average number of books per author.

        Returns:
            float: Average books per author
        """
        author_stats = self.author_statistics()
        if not author_stats:
            return 0.0
        return sum(author_stats.values()) / len(author_stats)

    def availability_report(self):
        """
        Generate a report of book availability.

        Returns:
            dict: Dictionary with availability statistics
        """
        total = self.library.total_books()
        available = len(self.library.available_books())
        fully_checked = sum(
            1 for book in self.library.books.values() if book.available_copies() == 0
        )

        return {
            "total_titles": total,
            "available_titles": available,
            "fully_checked_out": fully_checked,
            "availability_percentage": (available / total * 100) if total > 0 else 0,
        }

    def collection_summary(self):
        """
        Generate a comprehensive summary of the collection.

        Returns:
            str: Formatted summary report
        """
        lines = [
            f"=== {self.library.name} Collection Summary ===",
            f"Total Books: {self.library.total_books()}",
            f"Total Copies: {self.library.total_copies()}",
            f"Utilization Rate: {self.utilization_rate():.1f}%",
            f"Average Books per Author: {self.average_books_per_author():.1f}",
            "",
        ]

        popular = self.most_popular_books(3)
        if popular:
            lines.append("Most Popular Books:")
            for book, count in popular:
                if count > 0:
                    lines.append(f"  - {book.title}: {count} checkouts")

        return "\n".join(lines)
