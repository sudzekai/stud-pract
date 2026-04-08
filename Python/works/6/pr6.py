import math

class SignedValueError(Exception):
    pass

def main():

    task5()

def task1():
    a, b = map(int, input("Введите делимое и делитель через пробел: ").split(" "))

    if b == 0:
        print("На ноль делить нельзя!")
    else:
        print(f"{a}:{b}={a/b}")
    
def task2():
    try:     
        a = int(input("Введите делимое: "))

        while True:
            try:
                b = int(input("Введите делитель: "))
                if (b == 0):
                    raise ZeroDivisionError("Деление на 0 невозможно")
                break

            except ZeroDivisionError as e:
                print(e)
    except ValueError as e:
        print(e)
    finally:
        if (b != 0):
            print(f"{a}:{b}={a/b}")
        else:
            print("Операция не может быть выполнена")

def task3_4():
    print("\nTask 3\n")

    while True:
        try:
            x, y, z = map(int, input("Введите числа x, y, z через пробел: ").split())
            if (x - y + z) == 0:
                raise ZeroDivisionError("Знаменатель равен 0! Деление на ноль невозможно.")
            if (x - y + z) < 0:
                raise SignedValueError("Под корнем отрицательное число!")
            break 
                
        except ValueError:
            print("Ошибка: необходимо ввести три целых числа через пробел!")
        except ZeroDivisionError as e:
            print(f"Ошибка: {e}")
        except SignedValueError as e:
            print(f"Ошибка: {e}")

    result = math.sqrt(x + y + z) / ((x - y + z) ** 2)
    print(f"Результат: sqrt({x}+{y}+{z})/(({x}-{y}+{z})^2) = {result:.3f}")


def task5():
    books = {
        "Книга1" : "Автор1", 
        "Книга2" : "Автор2"
    }

    while True:
        x = int(input("""Меню:
1. Список книг
2. Удалить книгу
3. Создать книгу
0. Выход
"""))
        if x == 1:
            for title, author in books.items():
                print(f"Название: {title:<10} | Автор: {author}")
        elif x == 2:
            key = input("Введите название книги для удаления: ")
            if key in books:
                del books[key]
                print("Книга удалена")
            else:
                print("Такой книги нет в списке")
        elif x == 3:
            try:
                title, author = input("Введите название книги и ее автора через запятую: ").split(",")
                if title in books:
                    print("Книга с таким названием уже существует")
                    continue
                books[title] = author
                print("Книга добавлена")
            except Exception as e:
                print(f"Ошибка добавления книги: {e}")
        elif x == 0:
            break
        else:
            print("Неизвестная команда")

if __name__ == "__main__":
    main()