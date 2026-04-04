import functions

def main():
    task1()
    task2()
    task3()
    task4()
    task5()
    task6()

def task1():
    print("\nTask 1\n")
    a = 10.35
    b = 5
    print(functions.power(a, b))
    print(functions.power(a))

def task2():
    print("\nTask 2\n")
    print(functions.factorial(5))
    functions.try_execute(functions.factorial, "12")

def task3():
    print("\nTask 3\n")
    functions.some_action(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    functions.try_execute(functions.some_action, "1", 2, 3, 4, 5, 6)

def task4():
    print("\nTask 4\n")
    arr = [1, 2, 3, 4, 5, 6]
    arr2 = ["1", 2, 3, 4, 5]
    functions.multiply_list(arr, 2)
    print(" ".join(map(str, arr)))
    functions.try_execute(functions.multiply_list, arr2)

def task5():
    print("\nTask 5\n")
    print(functions.lambda_function(10, 12, 2))

def task6():
    print("\nTask 6\n")
    math_scores = [85, 92, 78, 88, 95, 70, 82, 90, 76, 84, 88, 91, 79]
    russian_scores = [78, 89, 82, 85, 91, 75, 80, 88, 74, 83, 86, 90, 77]
    computer_scores = [90, 88, 85, 92, 96, 72, 84, 89, 78, 86, 91, 93, 80]
    names = [
        "Иванов Иван", "Петров Петр", "Сидоров Алексей", 
        "Кузнецова Мария", "Смирнов Дмитрий", "Васильева Анна",
        "Михайлов Сергей", "Федорова Екатерина", "Николаев Андрей",
        "Алексеева Ольга", "Дмитриев Павел", "Егорова Татьяна",
        "Сергеев Владимир"
    ]

    full = { names[i] : {"math" : math_scores[i], "rus" : russian_scores[i], "comp" : computer_scores[i]} for i in range(names.__len__())}
    print(f"{"Имя":<20} | Мат | Рус | Комп")
    for name, scores in full.items():
        print(f"{name:<20} | {scores["math"]:<3} | {scores["rus"]:<3} |  {scores["comp"]:<3}")
    
if __name__ == "__main__":
    main()