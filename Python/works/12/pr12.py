import os
import subprocess

def main():
    while True:
        if (not menu()):
            break

def menu() -> bool:
    print("""\n====== Меню ======
          
1. Создать файл
2. Написать в файл
3. Прочитать файл
4. Переименовать файл
5. Удалить файл

14. Task 4
15. Task 5

0. Выход

==================\n""")
    x = input("Выберите пункт из меню: ")
    variants = ["1", "2", "3", "4", "5", "14", "15"]
    clear_console()
    if (x in variants):
        if (x == "1"):
            create_file_variant()
            
        elif (x == "2"):
            clear_console()
            var = input("Выберите режим ввода:\n1. Полная перезапись\n2. Добавление текста\n")
            if (var == "1"):
                write_text_variant()
            elif (var == "2"):
                write_text_variant(True)
            else:
                print("Такого варианта не существует")
                
        elif (x == "3"):
            read_file_variant()
        
        elif (x == "4"):
            rename_file_variant()
        
        elif (x == "5"):
            delete_file_variant()
        
        elif (x == "14"):
            task4()
            
        elif (x == "15"):
            task5()
        
        return True
        
    if (x == "0"):
        clear_console()
        print("Выход из программы")
        return False
    else:
        clear_console()
        print("Такого пункта в меню нет!")
        return True

def create_file_variant():
    filename = input("Введите название файла: ")
    try:
        create(filename)
        print(f"Файл с названием {filename} создан")
    except Exception as e:
        print(f"Ошибка при создании файла: {e}")
    finally:
        block_input()

def write_text_variant(append:bool = False):
    clear_console()
    
    filename = input("Введите название файла для ввода текста: ")
    if (is_file_exists(filename)):
        content = []
        
        print("Вводите текст для записи в файл, признаком окончания ввода является ключевое слово 'end'\n")
        
        if (append):
            text = read(filename)
            
            if (text.split("\n")[-1] != ""):
                content.append("")
            print(f"\nСодержание файла:\n{text}")
        
        while True:
            string = input()
            
            if string == "end":
                break
            elif string.endswith(" end"):
                content.append(string[:-4])
                break
            else:
                content.append(string)
        
        try:
            letters = write(filename, "\n".join(content), append)
            print(f"В файл записано {letters} символов")
        except Exception as e:
            print(f"Ошибка при изменении файла: {e}")
        finally:
            block_input()
    else:
        print(f"Ошибка при изменении файла: Указанный файл не существует")
        block_input()

def read_file_variant():
    filename = input("Введите название файла для чтения: ")
    try:
        if (not filename.endswith(".py")):
            print(f"\nСодержимое файла:")
        print(read(filename))
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
    finally:
        block_input()

def delete_file_variant():
    filename = input("Введите название файла для удаления: ")
    if (is_file_exists(filename)):
        try:
            os.remove(filename)
            print(f"Файл {filename} удалён")
        except Exception as e:
            print(f"Ошибка при удалении файла: {e}")
    else:
        print(f"Ошибка при удалении файла: Указанный файл не существует")
    block_input()

def rename_file_variant():
    filename = input("Введите название файла для переименования: ")
    new_filename = input("Введите новое название: ")
    if (is_file_exists(filename)):
        try:
            os.rename(filename, new_filename)
            print(f"Файл {filename} переименован\nНовое название: {new_filename}")
        except Exception as e:
            print(f"Ошибка при переименовании файла: {e}")
    else:
        print(f"Ошибка при переименовании файла: Указанный файл не существует")
    block_input()
    
def task4():
    filename = input("Введите название файла для чтения: ")
    try:
        if (filename.endswith(".py")):
            print(f"Невозможно прочитать файл:")
            return
        content = read(filename).split("\n")
        
        first = content[0]
        fifth = content[4]
        five = content[:5]
        
        print(f"Первая:\n{first}\n")
        print(f"Пятая:\n{fifth}\n")
        print(f"С первой по пятую:\n{"\n".join(five)}\n")
        print(f"Весь файл:\n{"\n".join(content)}")
        
        st = int(input("Строка 1: "))
        nd = int(input("Строка 2: "))
        
        result = content[st-1:nd]
        print("\n".join(result))
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
    finally:
        block_input()
    
def task5():
    filename = input("Введите название файла для чтения: ")
    try:
        lines = read(filename).split("\n")
        result = ""
        
        for line in lines:
            line = line.strip() 
            if not line: 
                continue
            
            while "  " in line:
                line = line.replace("  ", " ")
            
            nums = []
            for item in line.split(" "):
                if item.lstrip('-').isdigit(): 
                    nums.append(int(item))
            
            if nums:
                result += f"{line.replace(" ", "+")} = {sum(nums)}\n"
        
        print(result)
        
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
    finally:
        block_input()

def write(filename:str, content:str, append:bool = False) -> int:
    if (is_file_exists(filename)):
        mode = "w" if not append else "a"
        with open(filename, mode, encoding='utf-8') as file:
            return file.write(content)
    else:
        raise FileExistsError("Указанный файл не существует")

def read(filename:str) -> str:
    if (is_file_exists(filename)):
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            if (filename.endswith(".py")):
                try:
                    exec(content)
                    return "Выполнение скрипта завершено"
                except Exception as e:
                    print(f"Ошибка выполнения скрипта: {e}")
            else:
                return content
    else:
        raise FileExistsError("Указанный файл не существует")
    
def create(filename:str, content:str = "") -> bool:
    if (not is_file_exists(filename)):
        with open(filename, 'x', encoding='utf-8') as file:
            file.write(content)
            return True
    else:
        raise FileExistsError("Указанный файл уже существует")
            
def is_file_exists(filename:str) -> bool:
    return os.path.isfile(filename)

def clear_console():
    print("\n"*100)
    
def block_input():
    input("-->")
    clear_console()
    
if __name__ == "__main__":
    main()
    