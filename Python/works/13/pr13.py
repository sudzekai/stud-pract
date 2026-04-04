import json
import random
import os 

class Fruit:
    def __init__(self, name=None, price=None):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: {self.price} руб"
    
class Cat:
    def __init__(self, name=None, age=None, color=None):
        self.name = name
        self.age = age
        self.color = color   
    
    def __str__(self):
        return f"{self.name}: {self.age} лет, {self.color}"     
        
def main():
    task1()
    task2()

def task1():
    names = ["Мандарин", "Персик", "Банан", "Дыня", "Яблоко", 
             "Нектарин", "Ананас", "Драгонфрут", "Маракуйя", "Огурец"]
    
    fruits = [Fruit(name, random.randint(100, 300)) for name in names] 
    
    with open("pr13.fruits.json", "w", encoding='utf-8') as file:
        file.write(serialize(fruits))
    
def task2():
    filename = "pr13.cats.json"
    
    if os.path.exists(filename):
        with open(filename, "r", encoding='utf-8') as file:
            json_cats = deserialize(file.read(), Cat)
    else:
        json_cats = []
    
    while True:
        print("Управление списком котов\n")
        print("1. Показать всех котов")
        print("2. Добавить кота")
        print("3. Удалить кота по имени\n")
        print("4. Выход\n")
        print("="*25)
        
        choice = input("Выберите действие: ")
        
        if choice == "1":
            print("\nСписок котов:")
            if not json_cats:
                print("  Список пуст")
            else:
                for i, cat in enumerate(json_cats, 1):
                    print(f"  {i}. {cat}")
                    
        elif choice == "2":
            print("\nДобавление нового кота")
            data = input("Введите имя, возраст и окрас через пробел: ").split()
            
            if len(data) != 3:
                print("Ошибка: нужно ввести 3 параметра (имя возраст окрас)")
                continue
            
            try:
                new_cat = Cat(data[0], int(data[1]), data[2])
                json_cats.append(new_cat)
                print(f"Кот {data[0]} добавлен")
            except ValueError:
                print("Ошибка: возраст должен быть числом")
            except Exception as e:
                print(f"Ошибка: {e}")
                
        elif choice == "3":
            if not json_cats:
                print("Список пуст, некого удалять")
                continue
                
            name = input("Введите имя кота для удаления: ")
            found = False
            
            for i, cat in enumerate(json_cats):
                if cat.name.lower() == name.lower():
                    json_cats.pop(i)
                    print(f"Кот {name} удалён")
                    found = True
                    break
            
            if not found:
                print(f"Кот с именем {name} не найден")
                
        elif choice == "4":
            with open(filename, "w", encoding='utf-8') as file:
                file.write(serialize(json_cats))
            print("Данные сохранены. Выход...")
            break
            
        else:
            print("Неверный выбор, попробуйте снова")
        
        with open(filename, "w", encoding='utf-8') as file:
            file.write(serialize(json_cats))
            
def serialize(obj, filename=None):
    if isinstance(obj, list):
        result = [item.__dict__ for item in obj]
    else:
        result = obj.__dict__
    
    json_str = json.dumps(result, ensure_ascii=False, indent=4)
    
    if filename:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(json_str)
    return json_str

def deserialize(json_string, obj_class):
    data = json.loads(json_string)
    
    if isinstance(data, list):
        result = []
        for item in data:
            obj = obj_class()
            for key, value in item.items():
                setattr(obj, key, value)
            result.append(obj)
        return result
    
    else:
        obj = obj_class()
        for key, value in data.items():
            setattr(obj, key, value)
        return obj

if __name__ == "__main__":
    main()