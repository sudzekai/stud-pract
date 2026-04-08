import socket

HOST = 'localhost'
PORT = 50007

print("client")

login = input("Введите логин: ")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

s.sendall(login.encode())

while True:
    msg = input()
    s.sendall((msg).encode())