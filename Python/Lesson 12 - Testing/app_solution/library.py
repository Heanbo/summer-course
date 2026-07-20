"""
Library module for managing book collections.
"""

from book import Book


class Library:
    """Manages a collection of books."""

    def __init__(self, name):
        """
        Initialize a library.

        Args:
            name (str): Library name
        """
        if not name or not isinstance(name, str):
            raise ValueError("Library name must be a non-empty string")

        self.name = name
        self.books = {}  # isbn -> Book object

    def add_book(self, book):
        """
        Add a book to the library.

        Args:
            book (Book): Book object to add

        Returns:
            bool: True if added, False if book already exists
        """
        if not isinstance(book, Book):
            raise TypeError("Must provide a Book object")

        if book.isbn in self.books:
            return False

        self.books[book.isbn] = book
        return True

    def remove_book(self, isbn):
        """
        Remove a book from the library.

        Args:
            isbn (str): ISBN of book to remove

        Returns:
            bool: True if removed, False if not found
        """
        if isbn in self.books:
            del self.books[isbn]
            return True
        return False

    def find_book(self, isbn):
        """
        Find a book by ISBN.

        Args:
            isbn (str): ISBN to search for

        Returns:
            Book: Book object if found, None otherwise
        """
        return self.books.get(isbn)

    def search_by_title(self, title_query):
        """
        Search for books by title (case-insensitive partial match).

        Args:
            title_query (str): Title search string

        Returns:
            list: List of matching Book objects
        """
        query_lower = title_query.lower()
        results = []
        for book in self.books.values():
            if query_lower in book.title.lower():
                results.append(book)
        return results

    def search_by_author(self, author_query):
        """
        Search for books by author (case-insensitive partial match).

        Args:
            author_query (str): Author search string

        Returns:
            list: List of matching Book objects
        """
        query_lower = author_query.lower()
        results = []
        for book in self.books.values():
            if query_lower in book.author.lower():
                results.append(book)
        return results

    def total_books(self):
        """Get total number of unique book titles."""
        return len(self.books)

    def total_copies(self):
        """Get total number of book copies in library."""
        return sum(book.copies for book in self.books.values())

    def available_books(self):
        """
        Get list of books that have available copies.

        Returns:
            list: List of Book objects with available copies
        """
        return [book for book in self.books.values() if book.is_available()]

    def checkout_book(self, isbn):
        """
        Check out a book by ISBN.

        Args:
            isbn (str): ISBN of book to checkout

        Returns:
            bool: True if successful, False otherwise
        """
        book = self.find_book(isbn)
        if book:
            return book.checkout()
        return False

    def return_book(self, isbn):
        """
        Return a book by ISBN.

        Args:
            isbn (str): ISBN of book to return

        Returns:
            bool: True if successful, False otherwise
        """
        book = self.find_book(isbn)
        if book:
            return book.return_book()
        return False

    def __str__(self):
        """String representation of the library."""
        return f"{self.name} - {self.total_books()} books, {self.total_copies()} copies"
