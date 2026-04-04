import tkinter as tk

def on_left_click(event, field_name):
    label.config(text=f"Активное поле: {field_name}")

def on_right_click(event, field_name):
    print(f"Правая кнопка на поле: {field_name}")

root = tk.Tk()
root.title("Активные поля ввода")
root.geometry("400x200")

label = tk.Label(root, text="Активное поле: ")
label.pack()

frame = tk.Frame(root)
frame.pack()

tk.Label(frame, text="Поле 1:").grid(row=0, column=0)
entry1 = tk.Entry(frame)
entry1.grid(row=0, column=1)
entry1.bind('<Button-1>', lambda e, name="Поле 1": on_left_click(e, name))
entry1.bind('<Button-3>', lambda e, name="Поле 1": on_right_click(e, name))

tk.Label(frame, text="Поле 2:").grid(row=1, column=0)
entry2 = tk.Entry(frame)
entry2.grid(row=1, column=1)
entry2.bind('<Button-1>', lambda e, name="Поле 2": on_left_click(e, name))
entry2.bind('<Button-3>', lambda e, name="Поле 2": on_right_click(e, name))

tk.Label(frame, text="Поле 3:").grid(row=2, column=0)
entry3 = tk.Entry(frame)
entry3.grid(row=2, column=1)
entry3.bind('<Button-1>', lambda e, name="Поле 3": on_left_click(e, name))
entry3.bind('<Button-3>', lambda e, name="Поле 3": on_right_click(e, name))

root.mainloop()