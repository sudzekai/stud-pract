def hello(name = "World"):
    print(f"Hello, {name}")

def change_base(num: int, base: int) -> str:
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if base < 2 or base > 36:
        raise ValueError("base value must be better than 1 and less than 37") 
    
    if num < base:
        return digits[num]
    
    return change_base(num // base, base) + digits[num % base]

def get_multiline(text: str):
    return text.replace(". ", "\n")

def get_caesar_string(input: str, key: int = 3):
    russian = [
        'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 
        'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 
        'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я'
    ]
    result = ""

    for letter in input:
        if letter in russian:
            index = russian.index(letter.lower()) + key

            if index >= russian.__len__():
                index -= russian.__len__()

            elif index < 0:
                index += russian.__len__()

            result += russian[index]
        else:
            result += letter

    return result