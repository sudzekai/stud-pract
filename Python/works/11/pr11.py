import re

def main():
    task1()
    task2()
    task3()
    task4()
    
def task1():
    print("\nTask 1\n")
    text = "Привет! Как дела? Хорошо."
    regex = r"[.?!]"
    print("\n".join(re.split(regex, text)))
    
def task2():
    print("\nTask 2\n")
    regex = r"(редис[а-я]*к[а-я]*|плох[а-я]* человек[а-я]*)"
    text = "Ты плохой человек. Вы все редиски. Плохого человека я вижу за километр, как и всех редисок\nплохой редисок человека"
    replace = "давайте жить дружно"
    print(re.sub(regex, replace, text, flags=re.IGNORECASE))
    
def task3():
    print("\nTask 3\n")
    regex = r"(?:0[1-9]|[0-2][1-9]|3[0-1])\.(?:0[1-9]|1[0-2])\.\d{2,4}"
    text = "12.12.2020\n28.02.20\n28/02.20\n00.12.2020\n01.00.2020\n32.12.20\n30.13.2020"
    print(", ".join(re.findall(regex, text)))
    
def task4():
    print("\nTask 4\n")
    regex = r"^(?=.*[0-9])(?=.*[A-Z])(?=.*[a-z]).{6,}$"
    passwords = [ "Abc123", "Password1", "A1b2c3", "Hello123", "Qwerty1", "Test99A", "Aa1Aa1", "abcdef", "ABCDEF", "123456", "Abc12", "aB1", "ABC123", "abc123", "Abcdef", "123ABC", "A1", "1234567", "abcdefg", "ABCDEFG" ]
    for password in passwords:
        print(f"{password} - {'True' if re.search(regex, password) else 'False'}")
        
if __name__ == "__main__":
    main()