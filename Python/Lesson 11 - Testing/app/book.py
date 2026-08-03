"""
Book module for library management system.
Handles book data and validation.
"""


class Book:
    """Represents a book in the library."""

    def __init__(self, isbn, title, author, year, copies=1):
        """
        Initialize a book.

        Args:
            isbn (str): International Standard Book Number
            title (str): Book title
            author (str): Book author
            year (int): Publication year
            copies (int): Number of copies available
        """
        if not isbn or not isinstance(isbn, str):
            raise ValueError("ISBN must be a non-empty string")
        if not title or not isinstance(title, str):
            raise ValueError("Title must be a non-empty string")
        if not author or not isinstance(author, str):
            raise ValueError("Author must be a non-empty string")
        if not isinstance(year, int) or year < 1000 or year > 2100:
            raise ValueError("Year must be between 1000 and 2100")
        if not isinstance(copies, int) or copies < 0:
            raise ValueError("Copies must be a non-negative integer")

        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies
        self.checked_out = 0

    def is_available(self):
        """Check if book has available copies."""
        return self.copies > self.checked_out

    def checkout(self):
        """
        Check out a copy of the book.

        Returns:
            bool: True if checkout successful, False otherwise
        """
        if self.is_available():
            self.checked_out += 1
            return True
        return False

    def return_book(self):
        """
        Return a copy of the book.

        Returns:
            bool: True if return successful, False otherwise
        """
        if self.checked_out > 0:
            self.checked_out -= 1
            return True
        return False

    def available_copies(self):
        """Get number of available copies."""
        return self.copies - self.checked_out

    def __str__(self):
        """String representation of the book."""
        return f"{self.title} by {self.author} ({self.year})"

    def __repr__(self):
        """Developer-friendly representation."""
        return f"Book(isbn='{self.isbn}', title='{self.title}', author='{self.author}', year={self.year}, copies={self.copies})"


def validate_isbn(isbn):
    """
    Validate ISBN format (simplified - checks for 10 or 13 digits).

    Args:
        isbn (str): ISBN to validate

    Returns:
        bool: True if valid format, False otherwise
    """
    if not isinstance(isbn, str):
        return False

    # Remove hyphens and spaces
    clean_isbn = isbn.replace("-", "").replace(" ", "")

    # Check if all characters are digits and length is 10 or 13
    if not clean_isbn.isdigit():
        return False

    return len(clean_isbn) in [10, 13]


def format_book_info(book):
    """
    Format book information for display.

    Args:
        book (Book): Book object to format

    Returns:
        str: Formatted book information
    """
    availability = f"{book.available_copies()}/{book.copies} available"
    return f"{book.title} by {book.author} ({book.year}) - {availability}"


def books_by_decade(books):
    """
    Group books by decade.

    Args:
        books (list): List of Book objects

    Returns:
        dict: Dictionary with decade as key and list of books as value
    """
    decades = {}
    for book in books:
        decade = (book.year // 10) * 10
        if decade not in decades:
            decades[decade] = []
        decades[decade].append(book)
    return decades
