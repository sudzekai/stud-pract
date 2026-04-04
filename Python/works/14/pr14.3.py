import tkinter as tk

root = tk.Tk()
root.title("Связанные переменные")
root.geometry("450x350")

entry_var = tk.StringVar()
check_var = tk.IntVar()
radio_var = tk.StringVar(value="option1")

result_label = tk.Label(root, text="")
result_label.pack()

def update_label():
    entry_text = entry_var.get() if entry_var.get() else "(пусто)"
    check_text = "Да" if check_var.get() == 1 else "Нет"
    radio_text = ""
    if radio_var.get() == "option1":
        radio_text = "Красный"
    elif radio_var.get() == "option2":
        radio_text = "Зелёный"
    else:
        radio_text = "Синий"
    
    result_text = f"Поле ввода: {entry_text}, Флажок: {check_text}, Переключатель: {radio_text}"
    result_label.config(text=result_text)

frame1 = tk.Frame(root)
frame1.pack()
tk.Label(frame1, text="Введите текст:").pack(side='left')
tk.Entry(frame1, textvariable=entry_var).pack(side='left')
entry_var.trace_add('write', lambda *args: update_label())

frame2 = tk.Frame(root)
frame2.pack()
tk.Checkbutton(frame2, text="Согласен с условиями", variable=check_var, command=update_label).pack()

frame3 = tk.Frame(root)
frame3.pack()
tk.Label(frame3, text="Выберите цвет:").pack()
tk.Radiobutton(frame3, text="Красный", variable=radio_var, value="option1", command=update_label).pack()
tk.Radiobutton(frame3, text="Зелёный", variable=radio_var, value="option2", command=update_label).pack()
tk.Radiobutton(frame3, text="Синий", variable=radio_var, value="option3", command=update_label).pack()

update_label()

root.mainloop()