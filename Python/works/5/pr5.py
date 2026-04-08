def main():
    task1()
    task2()
    task3()
    task4()
    task5()
    task6()
    task7()
    task8()
    task9()

def task1():
    print("\nTask 1\n")

    string = input("Введите строку: ")
    print(f"{string} " * 5)
    print(f"Длина строки: {string.__len__()}")

    print("Символы с индексами:")
    for i in range(string.__len__()):
        print(f"{i:<3} | {string[i]:>3}")

    print("Чётные:")
    for i in range(1, string.__len__(), 2):
        print(f"{i+1:<3} | {string[i]:>3}")

def task2():
    print("\nTask 2\n")

    string = input("Введите строку: ")
    start, end = map(int, input("Введите позиции начала и старта через пробел для получения подстроки: ").split(" "))

    print(string[start:end-1])

def task3():
    print("\nTask 3\n")

    string = input("Введите строку: ")
    result = f"#{string[1:-1]}#"
    print(result)

def task4():
    print("\nTask 4\n")

    string = input("Введите строку: ")

    if string.isdigit():
        print(f"Только цифры")
    elif string.isalpha():
        print(f"Только буквы")
    elif string.isalnum():
        print(f"Буквы и цифры")
    else:
        print("Доп символы")


def task5():
    print("\nTask 5\n")

    string = input("Введите строку с пробелами: ").split(" ")

    print(", ".join(string))

def task6():
    print("\nTask 6\n")

    string = input("Введите строку: ")
    substring = input("Введите подстроку: ")
    indexes = []
    counter = 0

    while substring in string:
        indexes.append(string.find(substring))
        string = string.replace(substring, " "*substring.__len__(), 1)
        counter += 1
    
    print(f"Количество вхождений: {counter}\nИндексы: {", ".join(map(str, indexes))}")
    


def task7():
    print("\nTask 7\n")

    string = input("Введите строку: ")
    string = string.lower()

    if (string == "".join(reversed(string))):
        print("Палиндром")
    else:
        print("Не палиндром")

def task8():
    print("\nTask 8\n")

    string = input("Введите строку: ")

    while "  " in string:
        string = string.replace("  ", " ")
    
    print(string)


def task9():
    print("\nTask 9\n")

    string = input("Введите ответ: ")
    answer = "ответ"

    if string.lower() == answer.lower():
        print("Ответ верен")
    else:
        print("Ответ неверен")

if __name__ == "__main__":
    main()