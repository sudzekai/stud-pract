from author import Author
from book import Book
from authors_book import AuthorsBook

def main():
    task1()
    task2()
    task3()
    task4()
    task5()

def task1():
    print("\nTask 1\n")
    author = Author()
    author.full_name = "Артемий Автухов"
    author.country = "Автуховия"
    author.print_info()

def task2():
    print("\nTask 2\n")
    book = Book("Книга 1")
    del book

def task3():
    print("\nTask 3\n")
    book = Book("Книга 2")
    book.add_creation("Омагад")
    book.add_creation("Не верю")
    book.add_creation("Это ООП")
    print(book.__len__())

def task4():
    print("\nTask 4\n")
    book = Book("Книга 2")
    book.add_creation("Омагад")
    book.add_creation("Не верю")
    book.add_creation("Это ООП")
    book.print_info()

def task5():
    print("\nTask 5\n")
    author = Author()
    author.full_name = "Евгений"
    author.country = "Россия"
    book = Book("Название")
    book.add_creation("Омагад")
    book.add_creation("Не верю")
    book.add_creation("Это ООП")
    authors_book = AuthorsBook(author=author, book=book)
    authors_book.print_info()
    
if __name__ == "__main__":
    main()