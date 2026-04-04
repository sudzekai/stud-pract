import tkinter as tk

def change_color_red():
    root.config(bg='red')

def change_color_green():
    root.config(bg='green')

def change_color_blue():
    root.config(bg='blue')

def change_size_500x500():
    root.geometry("500x500")

def change_size_700x400():
    root.geometry("700x400")

root = tk.Tk()
root.title("Меню приложение")
root.geometry("400x300")

menubar = tk.Menu(root)
root.config(menu=menubar)

color_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Color", menu=color_menu)
color_menu.add_command(label="Red", command=change_color_red, accelerator="Ctrl+R")
color_menu.add_command(label="Green", command=change_color_green, accelerator="Ctrl+G")
color_menu.add_command(label="Blue", command=change_color_blue, accelerator="Ctrl+B")

size_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Size", menu=size_menu)
size_menu.add_command(label="500x500", command=change_size_500x500, accelerator="Ctrl+1")
size_menu.add_command(label="700x400", command=change_size_700x400, accelerator="Ctrl+2")

root.bind_all('<Control-r>', lambda event: change_color_red())
root.bind_all('<Control-g>', lambda event: change_color_green())
root.bind_all('<Control-b>', lambda event: change_color_blue())
root.bind_all('<Control-1>', lambda event: change_size_500x500())
root.bind_all('<Control-2>', lambda event: change_size_700x400())

root.mainloop()