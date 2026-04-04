import re

def main():
    task1()
    task2()
    task3()
    task4()

def task1():
    print("\nTask 1\n")
    expression = r"[.?!]"
    string = "Привет! Как дела? Пока."
    parts = re.split(expression, string)
    print("\n".join(parts))

def task2():
    print("\nTask 2\n")
    bad_words_expression = r"(?:\bредис[о]?к[а-я]*\b)|\bплох[а-я]*\s+(?:человек[а-я]*|люд[а-я]*)\b"
    string = "Привет редиски и плохие люди"
    print(re.sub(bad_words_expression,"давайте жить дружно", string=string))

def task3():
    print("\nTask 3\n")

def task4():
    print("\nTask 4\n")

if __name__ == "__main__":
    main()