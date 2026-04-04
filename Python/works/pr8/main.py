import byteactions
import module

def main():
    task1()
    task2()
    task3()
    task4()
    task5()

def task1():
    print("\nTask 1\n")
    module.hello("Name")
    module.hello()

def task2():
    print("\nTask 2\n")
    print(module.change_base(100, 2))
    print(module.change_base(100, 3))
    print(module.change_base(100, 4))
    print(module.change_base(100, 5))

def task3():
    print("\nTask 3\n")
    print(module.get_multiline("Очень. Крутой. Текст. Без. Новых. Строк."))

def task4():
    print("\nTask 4")
    print(module.get_caesar_string("абвгдеёжзийклмнопрстуфхцчшщъыьэюя", -1))
    print(module.get_caesar_string("абвгдеёжзийклмнопрстуфхцчшщъыьэюя", 5))
    print(module.get_caesar_string("абвгдеёжзийклмнопрстуфхцчшщъыьэюя", 2))

def task5():
    print("\nTask 5\n")
    print(f"5 and 3: {byteactions.get_and(5, 3)}")
    print(f"5 or 3: {byteactions.get_or(5, 3)}")
    print(f"5 xor 3: {byteactions.get_xor(5, 3)}")
    print(f"not 5: {byteactions.get_not(5)}")
    print(f"5 left shift by 3 bytes: {byteactions.get_left_shift(5, 3)}")
    print(f"5 right shift by 2 bytes: {byteactions.get_right_shift(5, 2)}")


if __name__ == "__main__":
    main()