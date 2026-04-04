import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Авторизация")
root.geometry("200x300")
root.resizable(False, False)

login_var = tk.StringVar()
password_var = tk.StringVar()
remember_var = tk.IntVar()

def authorize():
    login = login_var.get()
    password = password_var.get()
    remember = remember_var.get()
    
    if login and password:
        if remember:
            messagebox.showinfo("Успех", f"Добро пожаловать, {login}!\nПароль будет сохранён")
        else:
            messagebox.showinfo("Успех", f"Добро пожаловать, {login}!")
    else:
        messagebox.showerror("Ошибка", "Введите логин и пароль!")

tk.Label(root, text="Вход в систему").pack()

tk.Label(root, text="Логин:").pack()
tk.Entry(root, textvariable=login_var).pack()

tk.Label(root, text="Пароль:").pack()
tk.Entry(root, textvariable=password_var, show="*").pack()

tk.Checkbutton(root, text="Запомнить пароль", variable=remember_var).pack()
tk.Button(root, text="Авторизоваться", command=authorize).pack()

root.mainloop()