class Book:
    _content:list[str]
    
    def __init__(self, title:str):
        self.title = title
        self._content = []
        print(f"Книга {title} создана")
    
    def __del__(self):
        print(f"Книга {self.title} удалена")
    
    def add_creation(self, title):
        self._content.append(title)
        print(f"Произведение {title} добавлено в содержание")

    def __len__(self):
        return self._content.__len__()
    
    def print_info(self):
        print(f"Книга: {self.title}\nСодержание:\n{"\n".join(self._content)}")