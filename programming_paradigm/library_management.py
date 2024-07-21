class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out_book(self):
        #Checks out book
        if not self._is_checked_out:
            self._is_checked_out == True
            return True
        return False

    def return_book(self):
        #Mark the book as returned.
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        #Check if the book is available.
        return not self._is_checked_out

    def __str__(self):
        return f"{self.title} by {self.author}"

class Library:
    #A class representing a library.
    def __init__(self):
        self._books = []

    def add_book(self, book):
        #Add a book to the library.
        self._books.append(book)

    def check_out_book(self, title):
        #Check out a book by title.
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return True
        return False

    def return_book(self, title):
       #Return a book by title.
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return True
        return False

    def list_available_books(self):
        #List all available books in the library.
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            print("No available books.")
        for book in available_books:
            print(book)