import random

def __main__():
    # task1()
    # task2()
    # task3()
    task6()
    task7()
    task9()

def task1():
    num = int(input("Введите количество элементов в массиве: "))
    arr = []
    for i in range(num):
        arr.append(random.randint(0, 100))
    
    for i in range(arr.__len__()):
        print(f"{arr[i]:<4} | {i}")

def task2():
    num = int(input("Введите количество элементов в массиве: "))
    arr = []
    for i in range(num):
        arr.append(input("Введите новый элемент массива: "))
    
    print(", ".join(arr))

def task3():
    print("\nTask 3\n")
    arr1, arr2 = [], []
    for i in range(40):
        arr1.append(random.randint(0, 100))

    for i in range(arr1.__len__()):
        if arr1[i] % 2 != 0:
            arr2.append(arr1[i])
    
    print("arr1")
    print(" ".join(map(str, arr1)))
    print("arr2")
    print(" ".join(map(str, arr2)))

    print("\nTask 4\n")
    print("arr2 reversed")
    arr2.reverse()
    print(" ".join(map(str, arr2)))

    print("\nTask 5\n")

    x = int(input("Введите число из массива для удаления: "))
    count = 0

    while x in arr2:
        count += 1
        arr2.remove(x)

    print(f"Количество вхождений: {count}")
    print(f" ".join(map(str, arr2)))
    
def task6():
    print("\nTask 6\n")

    arr = [random.randint(0, 9) for i in range(20)]
    print(" ".join(map(str, arr)))
    a, x = map(int, input("Введите индекс и число для вставки в массив: ").split(" "))

    arr.insert(a, x)
    print(" ".join(map(str, arr)))

def task7():
    print("\nTask 7\n")
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

    results = {i: (names[i], math_scores[i] + russian_scores[i] + computer_scores[i]) for i in range(len(names))}
    sorted_results = sorted(results.items(), key = lambda x: x[1][1], reverse = True)

    for index, (name, scores) in sorted_results[:10]:
        print(f"{index}: {name} - {scores}")

    print("\nTask 8\n")

    x = int(input("Введите номер студента: "))
    name, scores = results[x]
    print(f"Имя: {name}, баллы: {scores}")    

def task9():
    regions = { 
        "Архангельская область": ["Архангельск", "Новодвинск", "Северодвинск", "Шенкурск", "Котласс"],
        "Ленинградская область": ["Санкт-Петербург", "Пушкин", "Павловск"]
    }

    for i in range(5):
        city = input("Введите название города: ")
        for region, cities in regions.items():
            if city in cities:
                print(region)
    

if __name__ == "__main__":
    __main__()