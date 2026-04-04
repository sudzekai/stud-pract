import random
import math

def __main__():
    task4()
    task5()

def task1():
    print("Task 1 \n")
    for j in range(10):
        x = random.randint(1, 1000)
        isSimple = True
        
        if x < 2:
            isSimple = False
        elif x == 2:
            isSimple = True
        elif x % 2 == 0:
            isSimple = False
        else:
            for i in range(3, int(math.sqrt(x)) + 1, 2):
                if x % i == 0:
                    isSimple = False
                    break
        
        print(f"{x} - {'Простое' if isSimple else 'Не простое'}")


def task2():
    print("\nTask 2\n")
    x = random.randint(1, 10)
    while True:
        answer = int(input("Введите число:"))
        if answer == x:
            print("Молодец")
            break
        print("Загаданное число больше" if answer < x else "Загаданное число меньше")

def task3():
    for i in range(100, 0, -10):
        print(f"{i} C\t| {i*1.8+32} F")

def task4():
    a = int(input("Введите сумму покупки: "))
    b = 0
    while a > b:
        b += int(input(f"Введите сумму оплаты (Осталось {a - b}): "))

    if (a < b):
        print(f"Возьмите сдачу: {math.fabs(a-b)}")
    print("Оплата прошла успешно")

def task5():
    a, b, x1, x2 = map(float, input("Введите a, b, x1, x2 через пробел: ").split())
    N = int(input("Введите число N: "))
    step = (x2 - x1) / N
    
    for i in range(N - 1):
        x = x1 + i * step
        print(f"x = {x} y = {a * x + b}")
    
    print(f"x = {x2:.2f} y = {a * x2 + b:.2f}")

if __name__ == "__main__":
    __main__()