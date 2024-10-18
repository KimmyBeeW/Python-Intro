class Book:
    """
    Doctests: python3 -m doctest lab07.py
    >>> b1 = Book(0, "A Tale of Two Cities", "Charles Dickens")
    >>> repr(b1)
    "Book(0, 'A Tale of Two Cities', 'Charles Dickens')"
    >>> str(b1)
    'A Tale of Two Cities by Charles Dickens'
    >>> print(b1)  # recall that print() calls str()
    'A Tale of Two Cities by Charles Dickens'
    """
    def __init__(self, id, title, author):
        self.id = id
        self.title = title
        self.author = author
        self.times_read = 0

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __repr__(self):
        return f"Book({self.id}, '{self.title}', '{self.author}')"


class Library:
    """A Library takes in an arbitrary amount of books, and has a
    dictionary of id numbers as keys, and Books as values.
    Doctests: python3 -m doctest lab07.py
    >>> b1 = Book(0, "A Tale of Two Cities", "Charles Dickens")
    >>> b2 = Book(1, "The Hobbit", "J.R.R. Tolkien")
    >>> b3 = Book(2, "The Fellowship of the Ring", "J.R.R. Tolkien")
    >>> l = Library(b1, b2, b3)
    >>> l.books[0].title
    'A Tale of Two Cities'
    >>> l.books[0].author
    'Charles Dickens'
    >>> l.read_book(1)
    'The Hobbit has been read 1 time(s)'
    >>> l.read_book(3) # No book with this id

    >>> l.read_author("Charles Dickens")
    'A Tale of Two Cities has been read 1 time(s)'
    >>> l.read_author("J.R.R. Tolkien")
    'The Hobbit has been read 2 time(s)\\nThe Fellowship of the Ring has been read 1 time(s)'
    >>> b1.times_read
    1
    >>> b2.times_read
    2
    """

    def __init__(self, *args):
        """Takes in an arbitrary number of book objects and 
        puts them in a books dictionary which takes the book 
        id as the key and the book object as the value"""
        self.books = {}
        self.collection = {}
        for book in args:
            self.books[book.id] = book

    def read_book(self, id):
        """Takes in an id of the book read, and
        returns that book's title and the number
        of times it has been read."""
        if id in self.books:
            self.books[id].times_read += 1
            return f"{self.books[id].title} has been read {self.books[id].times_read} time(s)"
        return None

    def read_author(self, author):
        """Takes in the name of an author, and
        returns the total output of reading every
        book written by that author in a single string.
        Hint: Each book output should be on a different line."""
        total = []
        for id in self.books:
            if author == self.books[id].author:
                total.append(self.read_book(id))
        return '\n'.join(total)

    def add_book(self, book):
        """Takes in a book object and adds it to the books
        dictionary if the book id is not already taken.
        >>> b1 = Book(0, "A Tale of Two Cities", "Charles Dickens")
        >>> b2 = Book(1, "The Hobbit", "J.R.R. Tolkien")
        >>> l = Library(b1, b2)
        >>> str(l)
        'A Tale of Two Cities by Charles Dickens | The Hobbit by J.R.R. Tolkien'
        >>> l.add_book(Book(2, "The Fellowship of the Ring", "J.R.R. Tolkien"))
        >>> l.add_book(Book(2, "The Sorcerer's Stone", "J.K. Rowling"))
        >>> str(l)
        'A Tale of Two Cities by Charles Dickens | The Hobbit by J.R.R. Tolkien | The Fellowship of the Ring by J.R.R. Tolkien'
        """
        if book.id in self.books:
            return None
        else:
            self.books[book.id] = book

    def __str__(self):
        lib = []
        for book in self.books:
            lib.append(str(self.books[book]))
        return ' | '.join(lib)

    def __repr__(self):
        repl = []
        for book in self.books:
            repl.append(repr(self.books[book]))
        return "Library(" + ', '.join(repl) + ")"


if __name__ == "__main__":
    b1 = Book(0, "A Tale of Two Cities", "Charles Dickens")
    print(b1.id)
    b2 = Book(1, "The Hobbit", "J.R.R. Tolkien")
    b3 = Book(2, "The Fellowship of the Ring", "J.R.R. Tolkien")
    lst = [1, 2, 3, 4, 5]
    lst2 = [2,3,4,5,6]
    print(lst[2])
    l = Library(b1, b2, b3)
    print(l.collection)
    lst_master = [lst, lst2]
    print(lst_master)

    # print(l.books[0].title)
    # print(l.books[0].author)
    # print(l.read_book(1))
    # print(l.read_author('J.R.R. Tolkien'))
    # repr(l)
    # print(repr(l))
