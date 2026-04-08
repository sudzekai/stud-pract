def power(a: float , b: int = 2) -> float:
    """Функция возведения числа в степень
    Args:
        a (float): Основание степени
        b (int): Степень
    Returns:
        float: Число a возведенное в степень b
    """
    if (b < 0):
        return 1 / power(a, -b)
    
    result = 1.0
    for i in range(b):
        result *= a
    return result
    
def factorial(a: int) -> int:
    """Функция получения факториала числа
    Args:
        a (int): Основание факториала
    Returns:
        int: Факториал числа a
    Raises:
        ValueError: n < 0
        TypeError: неверный тип данных параметра
    """
    if not isinstance(a, int):
        raise TypeError("Получен неверный тип данных: ожидалось int")
    if a < 0:
        raise ValueError("Можно вычислить факториал только положительных чисел")

    if a == 0 or a == 1:
        return 1
    
    return a * factorial(a - 1)

def some_action(*args) -> None:
    """Функция вывода в консоль суммы, среднего, максимума, минимума и количества всех чисел
    Args:
        *args (int): Основание факториала
    Returns:
        None
    Raises:
        TypeError: неверный тип данных параметра
    """
    for num in args:
        if not isinstance(num, int):
            raise TypeError("Получен неверный тип данных: ожидалось int")
    
    count = len(args)
    total = sum(args)
    average = total / count
    maximum = max(args)
    minimum = min(args)
    
    print(f"Количество чисел: {count}")
    print(f"Сумма чисел: {total}")
    print(f"Среднее арифметическое: {average:.2f}")
    print(f"Максимальное число: {maximum}")
    print(f"Минимальное число: {minimum}")

def try_execute(func, *args):
    try:
        func(args)
    except Exception as e:
        print(e)

def multiply_list(arr: list, multiplier: int = -1) -> None:
    for i in range(arr.__len__()):
        if not isinstance(arr[i], (int, float)):
            raise TypeError(f"Один из элементов списка не является числом")
        arr[i] *= multiplier

lambda_function = lambda a, x, b: a * x + b  