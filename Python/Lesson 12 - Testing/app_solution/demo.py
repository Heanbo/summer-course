"""
Demo script showing the library management system in action.
"""

from book import Book, validate_isbn, format_book_info
from library import Library
from analytics import LibraryAnalytics


def main():
    """Run a demo of the library system."""

    # Create a library
    print("Creating City Public Library...")
    library = Library("City Public Library")
    print(f"✓ {library}\n")

    # Add some books
    print("Adding books to the library...")
    books_to_add = [
        Book("978-0-13-468599-1", "The Pragmatic Programmer", "David Thomas", 2019, 3),
        Book("978-0-13-235088-4", "Clean Code", "Robert Martin", 2008, 2),
        Book("978-0-596-52068-7", "JavaScript: The Good Parts", "Douglas Crockford", 2008, 2),
        Book("978-0-13-468599-2", "Design Patterns", "Gang of Four", 1994, 1),
        Book("978-0-201-61622-4", "The Python Cookbook", "David Beazley", 2013, 4),
    ]

    for book in books_to_add:
        library.add_book(book)
        print(f"  + {format_book_info(book)}")

    print(f"\n{library}\n")

    # Search for books
    print("Searching for Python books...")
    results = library.search_by_title("Python")
    for book in results:
        print(f"  • {book}")
    print()

    # Check out some books
    print("Checking out books...")
    library.checkout_book("978-0-13-468599-1")
    library.checkout_book("978-0-13-468599-1")
    library.checkout_book("978-0-596-52068-7")
    print("  ✓ Checked out 3 books\n")

    # Generate analytics
    print("=== Library Analytics ===")
    analytics = LibraryAnalytics(library)
    print(analytics.collection_summary())

    print("\n\nAvailability Report:")
    report = analytics.availability_report()
    for key, value in report.items():
        print(f"  {key}: {value}")

    print("\n\nAuthor Statistics:")
    author_stats = analytics.author_statistics()
    for author, count in sorted(author_stats.items(), key=lambda x: x[1], reverse=True):
        print(f"  {author}: {count} book(s)")


if __name__ == "__main__":
    main()
