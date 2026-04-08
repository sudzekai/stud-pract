import os
import fnmatch
from datetime import datetime

current_dir = os.getcwd()

def set_directory(path):
    global current_dir
    if os.path.isdir(path):
        current_dir = path
    else:
        print("Директория не существует")


def create_file(name):
    with open(os.path.join(current_dir, name), 'w') as f:
        pass

def delete_file(name):
    path = os.path.join(current_dir, name)
    if os.path.exists(path):
        os.remove(path)

def edit_file(name, text):
    with open(os.path.join(current_dir, name), 'w') as f:
        f.write(text)

def search_mask(mask):
    return fnmatch.filter(os.listdir(current_dir), mask)

def search_ext(ext):
    return [f for f in os.listdir(current_dir) if f.endswith(ext)]

def search_size(min_size):
    result = []
    for f in os.listdir(current_dir):
        path = os.path.join(current_dir, f)
        if os.path.isfile(path):
            if os.path.getsize(path) >= min_size:
                result.append(f)
    return result

def search_date(date_str):
    result = []
    target = datetime.strptime(date_str, "%Y-%m-%d")

    for f in os.listdir(current_dir):
        path = os.path.join(current_dir, f)

        if os.path.isfile(path):
            t = datetime.fromtimestamp(os.path.getmtime(path))
            if t.date() == target.date():
                result.append(f)

    return result


def menu():
    print("\n" + "=" * 45)
    print("        ФАЙЛОВЫЙ МЕНЕДЖЕР")
    print("Текущая директория:", current_dir)
    print("=" * 45)
    print("1. Создать файл")
    print("2. Удалить файл")
    print("3. Изменить файл")
    print("4. Поиск по маске")
    print("5. Поиск по расширению")
    print("6. Поиск по размеру")
    print("7. Поиск по дате")
    print("8. Сменить директорию")
    print("0. Выход")
    print("=" * 45)


while True:
    menu()
    var = input("Выберите действие: ")

    if var == '1':
        create_file(input("Имя файла: "))

    elif var == '2':
        delete_file(input("Имя файла: "))

    elif var == '3':
        edit_file(input("Имя файла: "), input("Текст: "))

    elif var == '4':
        print("Результат:", search_mask(input("Маска (*.txt): ")))

    elif var == '5':
        print("Результат:", search_ext(input("Расширение (.txt): ")))

    elif var == '6':
        print("Результат:", search_size(int(input("Минимальный размер (байт): "))))

    elif var == '7':
        print("Результат:", search_date(input("Дата (YYYY-MM-DD): ")))

    elif var == '8':
        set_directory(input("Введите путь к директории: "))

    elif var == '0':
        print("Выход...")
        break

    else:
        print("Неверная команда!")