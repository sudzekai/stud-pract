import tkinter as tk

def on_mouse_move(event):
    label.config(text=f"Координаты мыши: x = {event.x}, y = {event.y}")

root = tk.Tk()
root.title("Координаты мыши")
root.geometry("400x300")

label = tk.Label(root, text="Координаты мыши: x = 0, y = 0")
label.pack(expand=True)

root.bind('<Motion>', on_mouse_move)

root.mainloop()