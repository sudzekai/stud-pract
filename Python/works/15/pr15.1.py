import tkinter as tk
from tkinter import filedialog

def save_to_file():
    text = text_area.get("1.0", tk.END).strip()
    if not text:
        return
    
    file_path = filedialog.asksaveasfilename()
    if file_path:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(text)

def on_esc(event):
    root.destroy()

root = tk.Tk()
root.title("Сохранение текста")
root.geometry("400x440")

tk.Label(root, text="Введите текст:").pack()
text_area = tk.Text(root)
text_area.pack()

tk.Button(root, text="Сохранить", command=save_to_file).pack()

root.bind('<Control-s>', lambda event: save_to_file())
root.bind('<Escape>', on_esc)

root.mainloop()