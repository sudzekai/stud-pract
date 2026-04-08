import socket
from datetime import datetime

HOST = ''
PORT = 50007

print("server")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

while True:
    conn, addr = s.accept()

    login = conn.recv(1024).decode('utf-8')
    print('подключился', login)

    while True:
        data = conn.recv(1024)
        if not data:
            break

        print(datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S"),
              login, ':', data.decode('utf-8'))

    conn.close()