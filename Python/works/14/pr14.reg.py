import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Форма регистрации")
root.geometry("800x800")

login_var = tk.StringVar()
password_var = tk.StringVar()
gender_var = tk.StringVar(value="male")
continent_var = tk.StringVar()

def register():
    login = login_var.get()
    password = password_var.get()
    about = about_text.get("1.0", tk.END).strip()
    gender = "Мужской" if gender_var.get() == "male" else "Женский"
    continent = continent_var.get()
    
    if not login or not password:
        messagebox.showerror("Ошибка", "Заполните логин и пароль!")
        return
    
    info = f"Регистрация успешна!\n\nЛогин: {login}\nПол: {gender}\nМатерик: {continent}\nО себе: {about}"
    messagebox.showinfo("Успех", info)

tk.Label(root, text="Регистрация нового пользователя").pack()

frame_login = tk.Frame(root)
frame_login.pack()
tk.Label(frame_login, text="Логин:").pack(side='left')
tk.Entry(frame_login, textvariable=login_var).pack(side='left')

frame_password = tk.Frame(root)
frame_password.pack()
tk.Label(frame_password, text="Пароль:").pack(side='left')
tk.Entry(frame_password, textvariable=password_var, show="*").pack(side='left')

tk.Label(root, text="О себе:").pack()
about_text = tk.Text(root)
about_text.pack()

tk.Label(root, text="Пол:").pack()
gender_frame = tk.Frame(root)
gender_frame.pack()
tk.Radiobutton(gender_frame, text="Мужской", variable=gender_var, value="male").pack(side='left')
tk.Radiobutton(gender_frame, text="Женский", variable=gender_var, value="female").pack(side='left')

tk.Label(root, text="Материк:").pack()
continents = ["Евразия", "Африка", "Северная Америка", "Южная Америка", "Австралия"]
continent_var.set(continents[0])
continent_listbox = tk.Listbox(root)
for c in continents:
    continent_listbox.insert(tk.END, c)
continent_listbox.pack()

def on_select(event):
    selection = continent_listbox.curselection()
    if selection:
        continent_var.set(continents[selection[0]])

continent_listbox.bind('<<ListboxSelect>>', on_select)

tk.Button(root, text="Зарегистрироваться", command=register).pack()

root.mainloop()