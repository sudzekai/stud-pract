import tkinter as tk

def on_key_press(event):
    if event.char:
        current_text = label.cget("text")
        if current_text == "Нажатые клавиши: ":
            label.config(text=f"Нажатые клавиши: {event.char}")
        else:
            label.config(text=f"{current_text}{event.char}")

root = tk.Tk()
root.title("Нажатые клавиши")
root.geometry("400x300")

label = tk.Label(root, text="Нажатые клавиши: ")
label.pack(expand=True)

root.bind('<Key>', on_key_press)

root.mainloop()