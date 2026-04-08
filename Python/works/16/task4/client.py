import socket
import tkinter as tk

HOST = 'localhost'
PORT = 50007

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

login_sent = False

def send(event=None):
    global login_sent

    text = entry.get()

    if not text:
        return

    global label

    if not login_sent:
        s.sendall(text.encode())
        login_sent = True
        entry.delete(0, tk.END)
        label.config(text="Сообщение")
        return

    s.sendall(text.encode())
    entry.delete(0, tk.END)

root = tk.Tk()

label = tk.Label(root, text="Сначала введите логин")
label.pack()

entry = tk.Entry(root)
entry.pack()

btn = tk.Button(root, text="Отправить", command=send)
btn.pack()

entry.bind("<Return>", send)

root.mainloop()