class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        return f"Book: {self.title} by {self.author}"
    pass

class EBook(Book):
    def __init__(self, title, author, file_size: int):
        self.file_size = file_size
        super().__init__(title, author)
        return f"{self.title} by {self.author}, File Size: {file_size}"
    pass

class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int):
        self.page_count = page_count
        super().__init__(title, author)
        return f"{self.title} by {self.author}, Page Count: {page_count}"
    pass


class Library():
    def __init__(self, books):
        self.books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
        elif isinstance(book, EBook):
            self.books.append(book)
        elif isinstance(book, PrintBook):
            self.books.append(book)
        else:
            pass

    def list_books(self):
        for book in self.books:
            return book