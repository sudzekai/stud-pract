from author import Author
from book import Book

class AuthorsBook(Author, Book):

    def __init__(self, author:Author, book:Book):
        self.title = book.title
        self._content = book._content
        self.country = author.country
        self.full_name = author.full_name

    def printInfo(self):
        print(f"Книга: {self.title} Автор: {self.full_name}")