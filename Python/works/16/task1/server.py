import socket

HOST = ''
PORT = 50007

print("server")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

conn, addr = s.accept()
print('Подключен клиент: ', addr)

while True:
    data = conn.recv(1024)
    if not data:
        break

    print('Получено сообщение:', data.decode('utf-8'))
    conn.sendall(data)

conn.close()